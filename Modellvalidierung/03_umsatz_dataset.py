# -*- coding: utf-8 -*-
"""
Lab Modellvalidierung & Bias — Datensatz für den Reiter „Generalisierung"
Kurs: KI-Manager:in (KIM) · Fassung 3 (08.10.2026)

Domäne: Shop-Umsätze einer luxemburgischen Tankstellenkette (24/7-Betrieb). Alle Zahlen sind
synthetisch.

Aufbau: 8 Tankstellen (A–H) × 4 Warengruppen × 3 Preisgruppen, je Woche, sechs Jahre.
Ein Jahr hat hier vereinfacht 52 Wochen zu 7 Tagen; jedes Jahr beginnt an einem Montag.

Treiber der Nachfrage (auf Tagesebene erzeugt, dann zu Wochen summiert):
- Jahreszeit: gleitender Jahresverlauf plus Weihnachtswoche.
- Wochentag: Sonntage und Feiertage stark (Supermärkte zu, Tankstellen offen).
- Reiseverkehr zu Beginn und Ende der Ferien in Frankreich, Belgien, Deutschland und den
  Niederlanden (Ostern, Sommer, Herbst). Die Termine verschieben sich JEDES JAHR.
- Feier- und Brückentage (feste und bewegliche, Luxemburg).
- Umleitungen wegen Baustellen — je Tankstelle verschieden, vor allem Lkw-Verkehr.
- Zufall: Wetter (kettenweit), örtliche Schwankungen (je Tankstelle), Aktionen und Lieferengpässe
  (je Preisgruppe; Kundschaft weicht teils auf die Nachbar-Preisgruppe aus).

Aufteilung — bewusst zeitlich, nicht zufällig:
- Jahre 1–4 = Training · Jahr 5 = Validierung (Wahl der Modellstufe) · Jahr 6 = Test (einmal).

Vier Fragen der Verkaufsleitung, von grob nach fein:
  F1 alle Tankstellen · F2 Tankstelle A · F3 A, kohlensäurehaltige Getränke ·
  F4 A, kohlensäurehaltige Getränke, Preisgruppe 1,99–2,59 €

Fünf Modellstufen (lineare Regression auf dem Logarithmus des Wochenumsatzes):
  S1 nur der Durchschnitt · S2 + Jahreszeit (Monat) · S3 + Ereignisse (Reiseverkehr je Land,
  Feier-, Brückentage, Umleitungstage) · S4 + jede Kalenderwoche einzeln ·
  S5 + jedes Ereignis in jedem Quartal einzeln
Abweichung = gewichtete mittlere absolute Abweichung (WAPE): Summe |Prognose − Ist| / Summe Ist.
Zum Vergleich wird für F4 auch die Top-down-Variante berechnet (F3 vorhersagen und mit dem
historischen Anteil der Preisgruppe verteilen).

Für Auffälligkeit 3 im Lab: In allen sechs Jahren endeten in der letzten Augustwoche (KW 35)
die Sommerferien in Frankreich und in einigen deutschen Bundesländern.

Abhängigkeiten: numpy, pandas
"""
import json
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
JAHRE = [1, 2, 3, 4, 5, 6]
TAGE = 364
PEAK = 6                                            # Breite eines Reisepeaks in Tagen
MONAT = [int((pd.Timestamp(2023, 1, 1) + pd.Timedelta(days=i)).month) for i in range(365)]
LETZTE_AUG_KW = 35                                  # Tage 239–245

STATIONEN = list("ABCDEFGH")
GROESSE = dict(A=1.30, B=1.00, C=0.85, D=0.70, E=1.10, F=0.60, G=0.90, H=0.75)
REISE_EMPF = dict(A=1.20, B=0.90, C=0.35, D=0.25, E=0.70, F=0.20, G=0.50, H=0.30)

GRUPPEN = {  # Stück je Tag bei Tankstelle der Größe 1 · Empfindlichkeit Reise / Umleitung / Feiertag
    "Sandwiches":                 dict(stueck=70,  reise=1.0, uml=1.0, feier=0.8),
    "kohlensäurehaltige Getränke": dict(stueck=110, reise=1.0, uml=0.8, feier=0.9),
    "Bier":                       dict(stueck=45,  reise=0.4, uml=0.2, feier=1.4),
    "Süßwaren":                   dict(stueck=90,  reise=0.9, uml=0.5, feier=1.0),
}
PREISE = {  # (Bezeichnung, Durchschnittspreis €, Anteil an der Stückzahl)
    "Sandwiches":                 [("bis 3,99 €", 3.49, 0.40), ("4,00–5,49 €", 4.79, 0.45), ("ab 5,50 €", 6.29, 0.15)],
    "kohlensäurehaltige Getränke": [("bis 1,98 €", 1.69, 0.45), ("1,99–2,59 €", 2.29, 0.35), ("ab 2,60 €", 2.99, 0.20)],
    "Bier":                       [("bis 1,49 €", 1.19, 0.35), ("1,50–2,49 €", 1.89, 0.45), ("ab 2,50 €", 2.89, 0.20)],
    "Süßwaren":                   [("bis 0,99 €", 0.79, 0.30), ("1,00–1,99 €", 1.49, 0.50), ("ab 2,00 €", 2.49, 0.20)],
}
GEWICHT = {"fr": 0.40, "be": 0.20, "de": 0.25, "nl": 0.15}

def j(a, b):
    return int(rng.integers(a, b + 1))

def peak(tag, mitte):
    return max(0.0, 1 - abs(tag - mitte) / PEAK)

def kalender():
    ostern = 7 * j(12, 16)                              # ein Sonntag zwischen Tag 84 und 112
    ferien = {  # (Beginn, Ende) je Ferienblock
        "fr": [(ostern - 9, ostern + 6), (j(186, 192), j(239, 244)), (j(291, 298), j(305, 308))],
        "be": [(ostern - 2, ostern + 13), (j(181, 186), j(232, 240)), (j(298, 302), j(306, 309))],
        "de": [(ostern - 6, ostern + 9), (j(176, 210), j(239, 245)), (j(275, 292), j(290, 306))],
        "nl": [(ostern - 2, ostern + 8), (j(188, 206), j(229, 248)), (j(287, 294), j(295, 302))],
    }
    feier = {1, 121, 129, 174, 227, 305, 359, 360, ostern + 1, ostern + 39, ostern + 50}
    bruecke = {ostern + 40}                              # Freitag nach Christi Himmelfahrt
    return ferien, feier, bruecke

def umleitungen():
    tage = set()
    for _ in range(j(1, 3)):
        a = j(20, 330); tage |= set(range(a, a + j(10, 25)))
    return tage

zeilen = []
for jahr in JAHRE:
    ferien, feier, bruecke = kalender()
    uml = {s: umleitungen() for s in STATIONEN}
    # Tagesmerkmale
    reise = {l: np.array([max([peak(t, a) for a, e in fe] + [peak(t, e) for a, e in fe]) for t in range(1, TAGE + 1)])
             for l, fe in ferien.items()}
    reise_eff = sum(GEWICHT[l] * reise[l] for l in reise)              # 0 … ~1
    tag = np.arange(1, TAGE + 1); wtag = (tag - 1) % 7                  # 0 = Montag … 6 = Sonntag
    saison = 1 + 0.12 * np.sin(2 * np.pi * (tag - 100) / TAGE) + np.where(tag > 350, 0.20, 0)
    wt = np.select([wtag == 6, wtag == 5, wtag == 4], [1.35, 1.15, 1.10], 1.0)
    ist_feier = np.isin(tag, list(feier)); ist_br = np.isin(tag, list(bruecke))
    wetter_woche = np.exp(rng.normal(0, 0.03, 52))                     # kettenweit
    for s in STATIONEN:
        ist_uml = np.isin(tag, list(uml[s]))
        ort_woche = np.exp(rng.normal(0, 0.04, 52))
        for g, gp in GRUPPEN.items():
            grp_woche = np.exp(rng.normal(0, 0.05, 52))
            # Aktionen / Lieferengpässe je Preisgruppe; teilweise Ausweichen auf Nachbargruppen
            roh = np.exp(rng.normal(0, 0.30, (52, 3)))
            band_woche = roh / (roh.mean(axis=1, keepdims=True) ** 0.8)
            lam_tag = (gp["stueck"] * GROESSE[s] * saison * wt
                       * (1 + REISE_EMPF[s] * gp["reise"] * 1.3 * reise_eff)
                       * np.where(ist_feier, 1 + 0.40 * gp["feier"], 1.0)
                       * np.where(ist_br, 1 + 0.25 * gp["feier"], 1.0)
                       * np.where(ist_uml, 1 + 0.30 * gp["uml"], 1.0))
            for b, (bez, preis, anteil) in enumerate(PREISE[g]):
                for w in range(52):
                    sl = slice(7 * w, 7 * w + 7)
                    lam = lam_tag[sl] * anteil * wetter_woche[w] * ort_woche[w] * grp_woche[w] * band_woche[w, b]
                    stueck = int(rng.poisson(lam).sum())
                    zeilen.append(dict(
                        jahr=jahr, kw=w + 1, monat=MONAT[7 * w + 3], tankstelle=s, warengruppe=g,
                        preisgruppe=bez, stueck=stueck, umsatz_eur=round(stueck * preis, 2),
                        reise_fr=round(float(reise["fr"][sl].sum()), 2), reise_be=round(float(reise["be"][sl].sum()), 2),
                        reise_de=round(float(reise["de"][sl].sum()), 2), reise_nl=round(float(reise["nl"][sl].sum()), 2),
                        feiertage=int(ist_feier[sl].sum()), brueckentage=int(ist_br[sl].sum()),
                        umleitung_tage=int(ist_uml[sl].sum())))

df = pd.DataFrame(zeilen)
df.to_csv("tankstelle_umsatz.csv", index=False)

# ------------------------------------------------------------------ die vier Fragen
EREIG = ["reise_fr", "reise_be", "reise_de", "reise_nl", "feiertage", "brueckentage", "umleitung_tage"]

def reihe(maske):
    d = df[maske]
    y = d.groupby(["jahr", "kw"]).umsatz_eur.sum()
    x = d.groupby(["jahr", "kw"])[["monat"] + EREIG].first()
    x["umleitung_tage"] = d.groupby(["jahr", "kw"]).umleitung_tage.mean() if maske.sum() > 0 else 0
    return x.assign(y=y).reset_index()

FRAGEN = {
    "F1": reihe(df.tankstelle.notna()),
    "F2": reihe(df.tankstelle == "A"),
    "F3": reihe((df.tankstelle == "A") & (df.warengruppe == "kohlensäurehaltige Getränke")),
    "F4": reihe((df.tankstelle == "A") & (df.warengruppe == "kohlensäurehaltige Getränke")
                & (df.preisgruppe == "1,99–2,59 €")),
}
# F1: Umleitungstage als Durchschnitt über die acht Tankstellen
f1u = df.groupby(["jahr", "kw", "tankstelle"]).umleitung_tage.first().groupby(["jahr", "kw"]).mean().values
FRAGEN["F1"]["umleitung_tage"] = f1u

def matrix(d, stufe):
    spalten = [np.ones(len(d))]
    if stufe >= 2:
        spalten += [(d.monat == m).astype(float).values for m in range(2, 13)]
    if stufe >= 3:
        spalten += [d[e].values.astype(float) for e in EREIG]
    if stufe >= 4:
        spalten += [(d.kw == k).astype(float).values for k in range(2, 53)]
    if stufe >= 5:
        q = (d.monat.values - 1) // 3
        spalten += [d[e].values * (q == k) for e in EREIG for k in range(1, 4)]
    return np.column_stack(spalten)

def fit(d, stufe):
    b, *_ = np.linalg.lstsq(matrix(d, stufe), np.log(d.y.values), rcond=None)
    return b

def wape(y, p):
    return float(np.abs(p - y).sum() / y.sum())

def prog(d, b, stufe):
    return np.exp(matrix(d, stufe) @ b)

STUFEN = [1, 2, 3, 4, 5]
erg = {}
for f, d in FRAGEN.items():
    tr, va, te, tv = d[d.jahr <= 4], d[d.jahr == 5], d[d.jahr == 6], d[d.jahr <= 5]
    k = {"train": [], "val": []}
    for st in STUFEN:
        b = fit(tr, st)
        k["train"].append(round(wape(tr.y.values, prog(tr, b, st)), 3))
        k["val"].append(round(wape(va.y.values, prog(va, b, st)), 3))
    beste = STUFEN[int(np.argmin(k["val"]))]
    # erst nach der Wahl: auf 1–5 neu trainieren, EINMAL am Testjahr 6 messen
    test = round(wape(te.y.values, prog(te, fit(tv, beste), beste)), 3)
    test5 = round(wape(te.y.values, prog(te, fit(tv, 5), 5)), 3)
    erg[f] = dict(train=k["train"], val=k["val"], beste=beste, test=test, test_s5=test5,
                  wochenumsatz=round(float(d.y.mean()), 0))

# Top-down für F4: F3 vorhersagen (beste Stufe) und mit dem Anteil der Preisgruppe in den Jahren 1–5 verteilen
d3, d4 = FRAGEN["F3"], FRAGEN["F4"]
b3 = fit(d3[d3.jahr <= 5], erg["F3"]["beste"])
anteil = d4[d4.jahr <= 5].y.sum() / d3[d3.jahr <= 5].y.sum()
td = round(wape(d4[d4.jahr == 6].y.values, anteil * prog(d3[d3.jahr == 6], b3, erg["F3"]["beste"])), 3)

# Auffälligkeit 1: Modell, das nur die Jahreszeit kennt (S2), Tankstelle A, Testjahr — Monat vs. Woche
d2 = FRAGEN["F2"]; t2 = d2[d2.jahr == 6].copy()
t2["p"] = prog(t2, fit(d2[d2.jahr <= 5], 2), 2)
mon = t2.groupby("monat")[["y", "p"]].sum()
ebenen = {"wape_monat": round(wape(mon.y.values, mon.p.values), 3), "wape_woche": round(wape(t2.y.values, t2.p.values), 3)}

# Auffälligkeit 3: letzte Augustwoche, Tankstelle A, alle sechs Jahre
la = []
for jahr in JAHRE:
    dj = d2[d2.jahr == jahr]
    la.append(float(dj[dj.kw == LETZTE_AUG_KW].y.iloc[0] / dj.y.mean() - 1))
letzte_aug = {"plus_je_jahr": [round(x, 3) for x in la], "min": round(min(la), 3), "mittel": round(float(np.mean(la)), 3)}

out = {"fragen": erg, "stufen": STUFEN, "topdown_f4_test": td, "anteil_preisgruppe": round(float(anteil), 3),
       "ebenen_f2_s2": ebenen, "letzte_aug_f2": letzte_aug, "zeilen": len(df)}
with open("umsatz_kennzahlen.json", "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1, ensure_ascii=False)

for f, e in erg.items():
    print(f, "Ø Wochenumsatz", e["wochenumsatz"], "| Training", e["train"], "| Validierung", e["val"],
          "| beste", e["beste"], "| Test", e["test"], "| Test S5", e["test_s5"])
print("Top-down F4 (Test):", td, "· Anteil Preisgruppe:", out["anteil_preisgruppe"])
print("Auffälligkeit 1 (F2, Stufe 2, Testjahr):", ebenen)
print("Letzte Augustwoche (F2):", letzte_aug)
