---
name: teilnehmer-bewertung
description: >
  Wertet die im lokalen Ordner "Arbeitsproben/[Vollname]/" eingereichten Dateien
  einer Kursteilnehmerin oder eines Kursteilnehmers aus. Drei Modi: (1) "feedback"
  erzeugt das laufende, formative Kurs-Feed-back als HTML; (2) "bewertung" erstellt
  einen beschwerdesicheren Bewertungs-Entwurf der Projektarbeit (0–100 je Aufgabe,
  Gesamtzensur) zur Freigabe durch den Dozenten; (3) "profil" erstellt auf Wunsch
  ein neutrales Referenzdokument der geleisteten Arbeiten für Bewerbungsunterlagen.
  Auslösen, wenn der Dozent ein Feed-back, eine Projektarbeits-Bewertung oder ein
  Arbeits-Profil für eine namentlich genannte Person anfordert.
---

# Teilnehmer-Bewertung — Skill für die KI-Kurse (KIB / KIM / MAT)

Dieser Skill verarbeitet die von Teilnehmenden eingereichten Dateien und erzeugt
drei verschiedene Dokumente. **Welcher Modus gemeint ist, ergibt sich aus dem
Auftrag des Dozenten** — im Zweifel nachfragen, nicht raten.

## Gemeinsame Grundlagen (für alle Modi)

**Eingabeordner:** `Schulungsmaterial/KI-Beauftragte/Arbeitsproben/[Vollname]/`
(analog für KIM/MAT, sobald dort Ordner existieren). Der Vollname ist der
Ordnername; Sonderfälle siehe Memory (z. B. „Abdelrahman Mekki", Richard Leyser =
nur Woche 2).

**Vor jeder Auswertung lesen:**
- `Kursmaterialien/Zentrale_Vorgehensweise.md` — verbindliche Stil- und
  Governance-Regeln.
- Die einschlägige Referenzdatei in diesem Skill (`reference/…`).

**Durchgängige Regeln (aus der Zentralen Vorgehensweise):**
- **Du-Form** in Feed-back und Bewertung (Ausnahme: Profil, siehe dort).
- **Präzision vor Aufwertung:** Inhalte exakt so beschreiben, wie sie im Dokument
  erscheinen. Im Zweifel **zitieren statt interpretieren**. Keine Fachbegriffe
  erfinden, die das Original nicht verwendet.
- **Keine Zertifizierungsdruck-Aussagen** („prüfungsrelevant", „für die
  Zertifizierung zählt") und keine TÜV-/Prüfungsmarker.
- **Abkürzungen** beim ersten Auftreten ausschreiben (Level 1/2/3, nie L1/L2/L3).
- **Use Cases** im Feed-back nicht namentlich nennen, wo es um wiederverwendbare
  Inhalte geht; in der Bewertung ist der konkrete Use-Case-Bezug zulässig, weil die
  Projektarbeit fallbezogen ist.
- **Kursseparation:** Inhalte und Tonalität nie 1:1 zwischen KIB, KIM, MAT
  übertragen.

**Der Mensch entscheidet.** Dieser Skill erzeugt in allen Modi **Entwürfe**. Noten,
Zensuren und Profiltexte werden vom Dozenten geprüft und freigegeben, bevor sie
nach außen gehen. Kein Output wird als „endgültig" deklariert.

---

## Modus 1 — `feedback` (laufend, formativ)

**Zweck:** Entwicklungsorientierte Rückmeldung während des Kurses.

**Eingabe:** alle Dateien im Arbeitsproben-Ordner der Person + ihre Quiz-Ergebnisse
(`Kursmaterialien/Quiz_Daten.xlsx` bzw. `Quiz_Daten.csv`).

**Ausgabe:** `Schulungsmaterial/KI-Beauftragte/Feedback/[Vorname]_Feedback.html`
(bestehende Datei gleichen Namens wird überschrieben).

**Format:** siehe `reference/feedback-format.md` (5 Sektionen, Fortschrittsbanner
40/60/90/100 %, Quiz nur als Gesamtprozent, einzelne Tage nur bei < 60 %, keine
Selbsteinschätzungs-Werte). Kanonisches Referenzdokument: `Sabine_Feedback.html`.

---

## Modus 2 — `bewertung` (Projektarbeit für die Urkunde) → ausgelagert

Die summative Bewertung der Projektarbeit für die Abschlussurkunde übernimmt der
eigenständige Skill **`bewertung-projektarbeit`**: Er findet die Projektarbeits-Datei,
bestimmt die Variante (KIB_1 / KIB_2 / KIM), wendet die offizielle Skala
(100–81 / 80–50 / 49–0) und Gewichtung (34/33/33; KIM 40/40/20) an, hält die
Begründungstiefe nach Punktzahl ein (81–97 knapp · > 97 und < 81 ausführlich/
beschwerdesicher) und füllt den offiziellen Bewertungsbogen
`Kursmaterialien/Vorlage_Projektarbeit.docx` als **docx + PDF** aus.

Bei einem Auftrag „Bewerte die Projektarbeit von [Name]" bzw. „Bewertung für die
Urkunde" diesen Skill verwenden.

**Die Detailrubrik `reference/bewertungs-rubrik.md` ist seit 25.08.2026 abgelöst** und
enthält nur noch einen Wegweiser. Skala, Gewichtung, Leitprinzip und Begründungstiefe
stehen ausschließlich in `bewertung-projektarbeit`, Abschnitt 3 — eine Quelle, kein
Abgleich.

---

## Modus 3 — `profil` (auf Wunsch, Referenzdokument)

**Zweck:** Ein neutrales, vorzeigbares Profil der im Kurs geleisteten Arbeiten,
das die Person ihren Bewerbungsunterlagen beilegen kann. **Keine Note, keine
Bewertung** — eine sachliche, leistungsorientierte Darstellung des Arbeitskorpus.

**Eingabe:** alle eingereichten Unterlagen der Person.

**Ausgabe:** ein eigenständiges Dokument (HTML oder DOCX nach Wunsch).

**Format und Register:** siehe `reference/profil-format.md`. Standard-Register ist
**formell-neutral (Sie/3. Person)**, weil das Dokument extern eingereicht wird —
abweichend von der Du-Form der übrigen Kursmaterialien. Vor Erstellung den
gewünschten Umfang und das Register kurz mit dem Dozenten klären.

---

## Was dieser Skill NICHT tut
- Er vergibt keine endgültigen Noten und schreibt nichts in die Urkunde.
- Er erfindet keine Inhalte und keine Quellen; er beschreibt nur, was eingereicht
  wurde.
- Er überträgt keine Inhalte zwischen den drei Kursen ohne Anpassung.
