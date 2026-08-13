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

## Dateien

| Datei | Zweck | Für wen |
|---|---|---|
| **DATA_CARD.md** | Beschreibung des Datenbestands nach dem Muster einer Data Card: Herkunft, Erzeugung, Abdeckung und **die absichtlich eingebauten Verzerrungen**. | Alle — Grundlage für Abschnitt 0b im Werkzeug |
| **index.html** | Im Browser öffnen. Regler schieben: Konfusionsmatrix, Precision/Recall/F1/F2, Bias je Gruppe, Proxy-Falle, Overfitting-Kurve. **Kein Setup.** | Teilnehmende (Haupt-Werkzeug) |
| **02_demo_erklaert.py** | Zum Live-Vorführen: lädt den Datensatz und erklärt alles in einfacher Sprache im Terminal. | Dozent / Neugierige |
| **01_dataset_und_kennzahlen.py** | Erzeugt den Datensatz neu und berechnet alle Kennzahlen. | zum Nachbauen/Anpassen |
| **bewerber_screening.csv** | Der Datensatz (2000 Zeilen). | — |

## Nutzung

- **Ohne alles:** `index.html` im Browser öffnen (oder den Pages-Link teilen).
- **Mit Python** (optional): `pip install scikit-learn matplotlib`, dann `python3 02_demo_erklaert.py`.

## Die vier „Aha"-Momente

1. **Schwelle & Trade-off** — es gibt kein „genau", nur die Abwägung Precision ↔ Recall.
2. **Bias** — dieselbe Regel, ungleiche Wirkung, weil das Modell die Vergangenheit gelernt hat.
3. **Proxy-Falle** — „Geschlecht" wegzulassen behebt Bias *nicht* (die Karrierelücke verrät es weiter).
4. **Overfitting** — Auswendiglernen (Training top, neue Daten schlecht) ≠ Verstehen.

## Lizenz

Code unter **MIT**, Lehr-Inhalte zusätzlich unter **CC BY 4.0** (Namensnennung: Ulrich Nord). Siehe `LICENSE`.

## Hinweis

Alle Daten sind **synthetisch** und dienen ausschließlich der Lehre. Es handelt sich nicht um
reale Personen oder reale Einstellungsentscheidungen.
