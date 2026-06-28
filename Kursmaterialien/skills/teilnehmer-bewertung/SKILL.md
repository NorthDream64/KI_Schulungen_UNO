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

## Modus 2 — `bewertung` (summativ, Projektarbeit)

**Zweck:** Auftragsgemäße Bewertung der Projektarbeit für die Abschlussurkunde.

**Realitätsrahmen (wichtig):** Die Norm des Anbieters ist ein **gutes Ergebnis
(≥ 85 Punkte)**. Die Bewertung soll wohlwollend und reibungslos diese Norm
abbilden. Die eigentliche Sorgfalt des Skills liegt **nicht** im feinen Ranking,
sondern darin, jede **Abweichung nach unten beschwerdesicher zu belegen** — weil
nur Minderbewertungen zu Beschwerden führen.

**Eingabe:** die als **Projektarbeit gekennzeichnete Datei** im Ordner der Person.
Erkennung: Dateiname enthält „Projektarbeit" (Groß-/Kleinschreibung egal). Findet
sich keine eindeutige Datei, **den Dozenten fragen**, welche Datei die Projektarbeit
ist — nicht raten.

**Ausgabe:** ein Bewertungs-Entwurf je Person, der die Struktur von
`Kursmaterialien/Projektarbeit_Bewertung.html` bedient (2–3 Aufgaben, je 0–100,
Gesamtpunktzahl /300, Gesamtzensur). Kopf des Entwurfs trägt deutlich den Vermerk
**„Entwurf — Freigabe durch den Dozenten erforderlich"**.

**Vorgehen und Rubrik:** siehe `reference/bewertungs-rubrik.md`. Kernpunkte:
1. Die 2–3 Aufgaben der Projektarbeit identifizieren (UC04a SolidFinanz AG:
   Strategieplan, Change Management, Business Case).
2. Je Aufgabe ein **Rating** (Punktzahl + Zensur-Stufe) und eine **Begründung**.
3. **Default ≥ 85**, sofern die Aufgabenstellung erfüllt ist.
4. Eine Punktzahl **< 85** nur, wenn ein konkreter, im Dokument belegbarer Mangel
   vorliegt — und dann mit **wörtlichem Beleg** und beschwerdesicherer Formulierung.
5. **Gesamtzensur** aus dem Mittel der Aufgaben (Zensur-Stufen wie im bestehenden
   Formular).

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
