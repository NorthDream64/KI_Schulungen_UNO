# -*- coding: utf-8 -*-
"""
Lab Modellvalidierung & Bias — Zweiter Datensatz für Abschnitt 4 (Overfitting vs. Underfitting)
Kurs: KI-Manager:in (KIM)

Anderes Beispiel als der Bewerber-Datensatz (01_dataset_und_kennzahlen.py), bewusst aus einer
anderen Domäne: Tagesumsatz (Sandwiches & Getränke) einer Tankstellenkette in Luxemburg.

Warum dieses Beispiel Overfitting besonders gut zeigt:
- Der Haupttreiber ist die Nähe zum Ferienbeginn in Frankreich, Belgien, Deutschland und den
  Niederlanden (grenznahe Reise-/Pendlertankstellen). Diese Termine verschieben sich JEDES JAHR.
- Ein zu komplexes Modell kann sich exakte Kalendertage aus den Trainingsjahren merken, statt das
  robuste Muster "Nähe zum Ferienbeginn" zu lernen — und scheitert dann im Testjahr, weil dort die
  Ferien auf andere Tage fallen.
- Trainings-/Test-Split ist deshalb bewusst NICHT zufällig, sondern nach Jahren getrennt
  (Jahre 1-3 = Training, Jahr 4 = Test) — nur so wird der Effekt sichtbar.

Zusätzlich: ein zweites, unabhängiges Beispiel für MODEL DRIFT (nicht Overfitting!) — drei neue
Snack-Trends, die es in den Trainingsjahren noch gar nicht gab. Keine Baumtiefe kann das lösen,
weil dem Modell dafür schlicht das Merkmal fehlt.

Zielgröße vereinfacht als Ja/Nein ("überdurchschnittlicher Umsatztag?"), damit dieselbe
Trainings-/Test-Grafik wie beim Bewerbermodell genutzt werden kann. Alle Zahlen synthetisch.

Abhängigkeiten: numpy, pandas, scikit-learn
"""
import numpy as np, pandas as pd, json
from sklearn.tree import DecisionTreeClassifier

rng = np.random.default_rng(7)
JITTER = 14          # Tage, um die der Ferienbeginn jährlich schwankt
HOL_EFFECT = 1.3      # Stärke des Ferien-Effekts auf den Umsatz-Score
NOISE = 0.25

# --- 1. Ferienbeginn je Land und Jahr (mit jährlichem Jitter) ---
base_start = {"fr": 195, "be": 200, "de": 205, "nl": 198}  # ungefährer Tag im Jahr (Mitte/Ende Juli)
hol_len = 40
weights = {"fr": 0.45, "be": 0.20, "de": 0.20, "nl": 0.15}  # Anteil am grenznahen Reiseverkehr
starts_by_year = {jahr: {l: base_start[l] + int(rng.integers(-JITTER, JITTER + 1)) for l in base_start}
                   for jahr in [1, 2, 3, 4]}

# --- 2. Tagesdaten erzeugen (4 Jahre à 365 Tage) ---
rows = []
for jahr in [1, 2, 3, 4]:
    for tag in range(1, 366):
        wochentag = (tag - 1) % 7  # 0=Mo ... 6=So
        wd_effekt = 0.15 if wochentag in (4, 5, 6) else -0.05  # Fr/Sa/So stärker
        naehe = {}
        for l in base_start:
            start = starts_by_year[jahr][l]
            dist = abs(tag - (start + hol_len / 2))
            naehe[l] = max(0.0, 1 - dist / (hol_len / 2 + 10))  # dreieckige Nähe-Kurve, 0-1
        hol_effekt = sum(weights[l] * naehe[l] for l in base_start) * HOL_EFFECT
        regen = rng.random() < 0.3
        regen_effekt = -0.08 if regen else 0.0
        score = 0.3 + wd_effekt + hol_effekt + regen_effekt + rng.normal(0, NOISE)
        rows.append(dict(jahr=jahr, tag_im_jahr=tag, wochentag=wochentag,
                          naehe_ferien_fr=round(naehe["fr"], 3), naehe_ferien_be=round(naehe["be"], 3),
                          naehe_ferien_de=round(naehe["de"], 3), naehe_ferien_nl=round(naehe["nl"], 3),
                          regen=int(regen), score=score))

df = pd.DataFrame(rows)
# Schwelle NUR aus den Trainingsjahren bestimmen (nicht aus dem Testjahr!)
schwelle = df[df.jahr <= 3].score.median()
df["ueberdurchschnittlich"] = (df.score > schwelle).astype(int)
df.drop(columns=["score"]).to_csv("tankstelle_umsatz.csv", index=False)

# --- 3. Overfitting-Kurve: Training = Jahre 1-3, Test = Jahr 4 (NICHT zufällig gesplittet!) ---
feat = ["wochentag", "naehe_ferien_fr", "naehe_ferien_be", "naehe_ferien_de", "naehe_ferien_nl",
        "regen", "tag_im_jahr"]  # tag_im_jahr ist die "Overfitting-Falle": exaktes Kalenderdatum
tr = df[df.jahr <= 3]; te = df[df.jahr == 4]
Xtr, ytr = tr[feat].values, tr.ueberdurchschnittlich.values
Xte, yte = te[feat].values, te.ueberdurchschnittlich.values

overfit = {"depth": [], "train": [], "test": []}
for d in range(1, 16):
    t = DecisionTreeClassifier(max_depth=d, random_state=1).fit(Xtr, ytr)
    overfit["depth"].append(d)
    overfit["train"].append(round(t.score(Xtr, ytr), 3))
    overfit["test"].append(round(t.score(Xte, yte), 3))

# --- 4. Model Drift (eigenständiges Beispiel, unabhängig von Overfitting) ---
# Drei neue Snack-Trends, die es NUR in Jahr 4 gibt und im Training nicht vorkamen.
rng2 = np.random.default_rng(11)
te2 = te.copy()
def trend_share(naehe_col, peak):
    return np.where(te2[naehe_col] > 0.5, te2[naehe_col] * peak * rng2.uniform(0.7, 1.0, len(te2)), 0.0)
te2["anteil_matjespizza"] = trend_share("naehe_ferien_nl", 0.14)      # Niederlande
te2["anteil_pommespizza"] = trend_share("naehe_ferien_be", 0.10)      # Belgien
te2["anteil_pizza_tricolore"] = trend_share("naehe_ferien_fr", 0.16)  # Frankreich
te2["anteil_trend_gesamt"] = (te2["anteil_matjespizza"] + te2["anteil_pommespizza"]
                               + te2["anteil_pizza_tricolore"])
betroffene_tage = te2[te2["anteil_trend_gesamt"] > 0]

drift = {
    "jahresdurchschnitt": round(float(te2["anteil_trend_gesamt"].mean() * 100), 1),
    "spitzendurchschnitt": round(float(betroffene_tage["anteil_trend_gesamt"].mean() * 100), 1),
    "spitzenmax": round(float(te2["anteil_trend_gesamt"].max() * 100), 1),
    "n_tage_betroffen": int((te2["anteil_trend_gesamt"] > 0).sum()),
    "n_tage_gesamt": int(len(te2)),
}

out = {"overfit": overfit,
       "base_rate_train": round(float(ytr.mean()), 3), "base_rate_test": round(float(yte.mean()), 3),
       "drift": drift}
with open("umsatz_kennzahlen.json", "w") as f:
    json.dump(out, f, indent=1)

# --- Sanity-Ausgabe ---
print("Basisrate 'überdurchschnittlich' Training/Test:", out["base_rate_train"], "/", out["base_rate_test"])
print("Overfitting-Kurve (Tiefe: train/test):")
for d, trv, tev in zip(overfit["depth"], overfit["train"], overfit["test"]):
    print(f"  {d:2d}: {trv:.3f} / {tev:.3f}  (Lücke {trv-tev:+.3f})")
print("\nDrift (Jahr 4, synthetisch):")
print(f"  Jahresdurchschnitt Trend-Anteil: {drift['jahresdurchschnitt']}%")
print(f"  Ø an betroffenen Tagen ({drift['n_tage_betroffen']}/{drift['n_tage_gesamt']}): {drift['spitzendurchschnitt']}%")
print(f"  Spitzenwert: {drift['spitzenmax']}%")
