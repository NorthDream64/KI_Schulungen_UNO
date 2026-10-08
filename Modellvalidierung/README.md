# Bias & Modellvalidierung

Ein **setup-freier**, praktischer Einblick in Modellvalidierung und algorithmische Fairness —
für Menschen ohne Technik-Hintergrund. Teil des Kurses *KI-Manager:in* (KIM).

> **Direkt öffnen (empfohlen):** Das interaktive Tool läuft im Browser unter
> <https://northdream64.github.io/KI_Schulungen_UNO/Modellvalidierung/>
> — kein Download, keine Installation.

Grundlage ist ein **synthetischer** Bewerber-Screening-Datensatz (alle Personen und Zahlen
erfunden), in dessen historische Entscheidungen bewusst eine Voreingenommenheit eingebaut ist.
So lässt sich zeigen, wie ein Modell die Diskriminierung der Vergangenheit lernt — und warum
das bloße Weglassen des Merkmals „Geschlecht" das Problem nicht behebt.

Für den Reiter *Generalisierung* kommt ein zweiter, ebenfalls synthetischer Datensatz hinzu:
Tagesumsätze einer luxemburgischen Tankstellenkette über sechs Jahre.

## Dateien

| Datei | Zweck | Für wen |
|---|---|---|
| **DATA_CARD.md** | Beschreibung des Datenbestands nach dem Muster einer Data Card: Herkunft, Erzeugung, Abdeckung und **die absichtlich eingebauten Verzerrungen**. | Alle — Grundlage für den Reiter *Quellen* im Werkzeug |
| **index.html** | Im Browser öffnen. Fünf Reiter: *Ausgangssituation*, *Confusion Matrix* (Schwelle, Precision, Recall, F1-Score, Kosten), *Mögliche Maßnahmen* (Bias je Gruppe, Proxy-Falle), *Generalisierung* (Tankstellen-Fall, Over-/Underfitting, Extrapolation), *Quellen*. **Kein Setup.** | Teilnehmende (Haupt-Werkzeug) |
| **02_demo_erklaert.py** | Zum Live-Vorführen: lädt den Datensatz und erklärt alles in einfacher Sprache im Terminal. | Dozent / Neugierige |
| **01_dataset_und_kennzahlen.py** | Erzeugt den Datensatz neu und berechnet alle Kennzahlen. | zum Nachbauen/Anpassen |
| **bewerber_screening.csv** | Der Datensatz (2000 Zeilen). | — |
| **03_umsatz_dataset.py** | Erzeugt den Tankstellen-Datensatz neu — zeitlich getrennt in Training (Jahre 1–4), Validierung (Jahr 5) und Test (Jahr 6) — und berechnet die Werte für den Reiter *Generalisierung*. | zum Nachbauen/Anpassen |
| **tankstelle_umsatz.csv** | Der Tankstellen-Datensatz (2190 Zeilen, ein Tag je Zeile). | — |

## Nutzung

- **Ohne alles:** `index.html` im Browser öffnen (oder den Pages-Link teilen).
- **Mit Python** (optional): `pip install scikit-learn pandas matplotlib`, dann `python3 02_demo_erklaert.py`.

## Die vier „Aha"-Momente

1. **Schwelle & Trade-off** — es gibt kein „genau", nur die Abwägung Precision ↔ Recall.
2. **Bias** — dieselbe Regel, ungleiche Wirkung, weil das Modell die Vergangenheit gelernt hat.
3. **Proxy-Falle** — „Geschlecht" wegzulassen behebt Bias *nicht* (die Karrierelücke verrät es weiter).
4. **Generalisierung** — Auswendiglernen (Training top, neue Daten schlecht) ≠ Verstehen; und eine Anfrage außerhalb der Daten beantwortet kein Modell verlässlich.

## Lizenz

Code unter **MIT**, Lehr-Inhalte zusätzlich unter **CC BY 4.0** (Namensnennung: Ulrich Nord). Siehe `LICENSE`.

## Hinweis

Alle Daten sind **synthetisch** und dienen ausschließlich der Lehre. Es handelt sich nicht um
reale Personen oder reale Einstellungsentscheidungen.
