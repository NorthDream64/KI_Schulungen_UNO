# -*- coding: utf-8 -*-
"""
Lab Modellvalidierung & Bias — Zweiter Datensatz für den Reiter „Generalisierung"
Kurs: KI-Manager:in (KIM) · Fassung 2 (08.10.2026)

Domäne: Tagesumsatz (Shop, 24/7-Betrieb) einer luxemburgischen Tankstellenkette.
Alle Zahlen sind synthetisch.

Treiber der Nachfrage:
- Reiseverkehr zu Ferienbeginn und Ferienende in Frankreich, Belgien, Deutschland und den
  Niederlanden. Die Termine verschieben sich JEDES JAHR.
- Feier- und Brückentage (feste und bewegliche).
- Umleitungen wegen Baustellen im Umkreis, die vor allem den Lkw-Verkehr an der Station vorbeiführen.
- Wochentag, Regen.

Aufteilung — bewusst zeitlich, nicht zufällig:
- Jahre 1–4  = Trainingsdaten
- Jahr 5     = Validierungsdaten (hier wird die Modell-Komplexität gewählt)
- Jahr 6     = Testdaten (isoliert belassen, genau EINMAL am Schluss gemessen)

Die „Overfitting-Falle" ist das Merkmal tag_im_jahr: Ein zu fein eingestelltes Modell merkt sich
exakte Kalendertage der Trainingsjahre statt der wandernden Ereignisse.

Für Auffälligkeit 4 im Lab: In allen sechs Jahren endeten in der letzten Augustwoche die
Sommerferien in Frankreich und in einigen deutschen Bundesländern (Rückreiseverkehr). Ein Jahr, in
dem das nicht so ist, kommt in den Daten nicht vor.

Zielgröße vereinfacht als Ja/Nein („überdurchschnittlicher Umsatztag?"), damit dieselbe Art von
Trainings-/Validierungsgrafik wie beim Bewerbermodell genutzt werden kann.

Abhängigkeiten: numpy, pandas, scikit-learn
"""
import json
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

rng = np.random.default_rng(7)
JAHRE = [1, 2, 3, 4, 5, 6]
NOISE = 0.30
PEAK = 6            # Tage: Breite des Reisepeaks um Ferienbeginn/-ende
LETZTE_AUG = list(range(237, 244))   # 25.–31. August (Nicht-Schaltjahr)
MONAT = [int((pd.Timestamp(2023, 1, 1) + pd.Timedelta(days=i)).month) for i in range(365)]

# Ferientermine je Land und Jahr (Tag im Jahr), mit jährlicher Verschiebung
def ferien(jahr):
    j = lambda a, b: int(rng.integers(a, b + 1))
    t = {
        "fr": (j(186, 192), j(237, 243)),   # Anfang Juli · Rentrée Ende August
        "be": (j(181, 186), j(229, 240)),
        "de": (j(176, 214), j(236, 243)),   # Bundesländer gestaffelt; einige enden Ende August
        "nl": (j(188, 206), j(224, 245)),
    }
    return t

GEWICHT = {"fr": 0.40, "be": 0.20, "de": 0.25, "nl": 0.15}

def peak(tag, mitte):
    return max(0.0, 1 - abs(tag - mitte) / PEAK)

def feiertage(jahr):
    ostern = int(rng.integers(82, 116))          # bewegliches Osterdatum
    fest = {1, 121, 174, 227, 305, 359, 360}     # 1.1., 1.5., 23.6. (LU), 15.8., 1.11., 25./26.12.
    beweglich = {ostern + 1, ostern + 39, ostern + 50}   # Ostermontag, Himmelfahrt, Pfingstmontag
    bruecke = {ostern + 40}                      # Freitag nach Himmelfahrt
    return fest | beweglich, bruecke

def umleitungen():
    tage = set()
    for _ in range(int(rng.integers(2, 4))):
        a = int(rng.integers(20, 340)); tage |= set(range(a, a + int(rng.integers(10, 22))))
    return tage

def wd_effekt(wochentag):
    return 0.18 if wochentag in (4, 6) else (0.10 if wochentag == 5 else -0.05)

zeilen = []
tag_global = 0
for jahr in JAHRE:
    fe = ferien(jahr); ft, br = feiertage(jahr); um = umleitungen()
    for tag in range(1, 366):
        wochentag = tag_global % 7; tag_global += 1
        monat = MONAT[tag - 1]
        reise = {l: max(peak(tag, a), peak(tag, e)) for l, (a, e) in fe.items()}
        reise_eff = sum(GEWICHT[l] * reise[l] for l in reise) * 1.6
        wd_eff = wd_effekt(wochentag)
        f_eff = 0.35 if tag in ft else 0.0
        b_eff = 0.30 if tag in br else 0.0
        u_eff = 0.25 if tag in um else 0.0
        regen = rng.random() < 0.3
        score = 0.30 + wd_eff + reise_eff + f_eff + b_eff + u_eff - (0.08 if regen else 0) \
            + rng.normal(0, NOISE)
        zeilen.append(dict(jahr=jahr, tag_im_jahr=tag, monat=monat, wochentag=wochentag,
                           reise_fr=round(reise["fr"], 3), reise_be=round(reise["be"], 3),
                           reise_de=round(reise["de"], 3), reise_nl=round(reise["nl"], 3),
                           feiertag=int(tag in ft), brueckentag=int(tag in br),
                           umleitung=int(tag in um), regen=int(regen), score=score))

df = pd.DataFrame(zeilen)
schwelle = df[df.jahr <= 4].score.median()           # Schwelle nur aus den Trainingsjahren
df["ueberdurchschnittlich"] = (df.score > schwelle).astype(int)
df.drop(columns=["score"]).to_csv("tankstelle_umsatz.csv", index=False)

FEAT = ["wochentag", "monat", "tag_im_jahr", "reise_fr", "reise_be", "reise_de", "reise_nl",
        "feiertag", "brueckentag", "umleitung", "regen"]
tr, va, te = df[df.jahr <= 4], df[df.jahr == 5], df[df.jahr == 6]
X = lambda d: d[FEAT].values
y = lambda d: d.ueberdurchschnittlich.values

kurve = {"depth": [], "train": [], "val": []}
modelle = {}
for d in range(1, 16):
    m = DecisionTreeClassifier(max_depth=d, random_state=1).fit(X(tr), y(tr))
    modelle[d] = m
    kurve["depth"].append(d)
    kurve["train"].append(round(m.score(X(tr), y(tr)), 3))
    kurve["val"].append(round(m.score(X(va), y(va)), 3))

beste = kurve["depth"][int(np.argmax(kurve["val"]))]
# Erst nach der Wahl: Training auf 1–5, EINMAL am Testjahr 6 messen
tr5 = df[df.jahr <= 5]
final = DecisionTreeClassifier(max_depth=beste, random_state=1).fit(X(tr5), y(tr5))
test_acc = round(final.score(X(te), y(te)), 3)
test_acc_tief = round(DecisionTreeClassifier(max_depth=15, random_state=1)
                      .fit(X(tr5), y(tr5)).score(X(te), y(te)), 3)

# --- Auffälligkeit 1/2: dieselbe Vorhersage, verschiedene Prüfebenen (Testjahr 6) ---
te_ = te.assign(pred=final.predict(X(te)), woche=(te.tag_im_jahr - 1) // 7)
mae_monat = float((te_.groupby("monat").pred.mean() - te_.groupby("monat").ueberdurchschnittlich.mean()).abs().mean())
mae_woche = float((te_.groupby("woche").pred.mean() - te_.groupby("woche").ueberdurchschnittlich.mean()).abs().mean())
ebenen = {"mae_monat_pp": round(mae_monat * 100, 1), "mae_woche_pp": round(mae_woche * 100, 1),
          "tag_falsch_pct": round((1 - test_acc) * 100, 1)}

# --- Auffälligkeit 4: die letzte Augustwoche (25.–31.8.) in den sechs Datenjahren ---
hist = df[df.tag_im_jahr.isin(LETZTE_AUG)]
letzte_aug = {"anteil_hoch": round(float(hist.ueberdurchschnittlich.mean()), 3),
              "rueckreise_jedes_jahr": bool((hist.groupby("jahr")[["reise_fr", "reise_de"]].max().max(axis=1) > 0).all())}

out = {"overfit": kurve, "beste_tiefe": beste, "test_acc": test_acc, "test_acc_tief15": test_acc_tief,
       "base_rate_train": round(float(y(tr).mean()), 3), "base_rate_val": round(float(y(va).mean()), 3),
       "base_rate_test": round(float(y(te).mean()), 3), "letzte_aug": letzte_aug, "ebenen": ebenen,
       "n": {"train": len(tr), "val": len(va), "test": len(te)}}
with open("umsatz_kennzahlen.json", "w") as f:
    json.dump(out, f, indent=1, ensure_ascii=False)

print("Basisraten Train/Val/Test:", out["base_rate_train"], out["base_rate_val"], out["base_rate_test"])
for d, a, b in zip(kurve["depth"], kurve["train"], kurve["val"]):
    print(f"  Tiefe {d:2d}: Training {a:.3f} · Validierung {b:.3f} · Lücke {a-b:+.3f}")
print("Beste Tiefe (Validierung):", beste, "· Test (einmalig):", test_acc, "· Test bei Tiefe 15:", test_acc_tief)
print("Prüfebenen Testjahr:", ebenen)
print("Letzte Augustwoche (Jahre 1–6):", letzte_aug)
