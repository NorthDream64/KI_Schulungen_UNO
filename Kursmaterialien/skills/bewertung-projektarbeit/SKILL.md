---
name: "bewertung-projektarbeit"
description: "Bewertet die Projektarbeit einer namentlich genannten Kursteilnehmerin/eines Teilnehmers für die Abschlussurkunde, füllt den offiziellen Bewertungsbogen (docx + PDF) aus und schreibt die zentrale Bewertungsübersicht fort. Auslösen, wenn der Dozent sagt „Bewerte die Projektarbeit von [Name]“, „Bewertung für die Urkunde“, „trag das in die Übersicht ein“, „Stand der Projektarbeiten“ o. Ä."
---

# Bewertung Projektarbeit — Skill für die TÜV-KI-Kurse (KIB / KIM)

Dieser Skill erstellt aus der eingereichten Projektarbeit einer Teilnehmerin oder eines
Teilnehmers eine **beschwerdesichere Bewertung** und füllt damit den **offiziellen
Bewertungsbogen** aus (Word + PDF). Das Ergebnis geht auf die Abschlussurkunde und dient
am Arbeitsmarkt als Referenz.

> **Der Mensch entscheidet.** Der Skill liefert einen **Freigabe-Vorschlag**. Der Dozent
> prüft und gibt frei, bevor der Bogen verwendet wird — insbesondere die Ausnahmefälle
> (> 97 und < 81 Punkte). Kein Ergebnis ist ohne Freigabe „endgültig“.

---

## 0 · Ablauf in Kürze

1. **Datei finden** im Ordner der Person. 2. **Variante bestimmen** und die passende
Aufgaben­datei als Maßstab lesen. 3. **Auswerten** nach Rubrik (34/33/33, Skala 100/81/50,
wohlwollend, Begründungstiefe nach Punktzahl). 4. **Bogen befüllen** (Kopie der offiziellen
Vorlage) und als **docx + PDF** im Zielordner ablegen. 5. **Ergebnis kurz zusammenfassen**;
Ausnahmen (> 97 / < 81) zum Gegenlesen markieren. 6. **Zeile in der Bewertungsübersicht
ergänzen** (Abschnitt 7).

Jede Person in **frischem, unbeeinflusstem Kontext** beurteilen (keine Ankerung an der
vorherigen Arbeit). Denselben Maßstab über alle Teilnehmenden konsistent anwenden.

> **Ein Chat pro Durchlauf, nicht pro Aufgabe.** Bewerten und Übersicht-Fortschreiben
> gehören in denselben Arbeitsgang (seit 25.08.2026). Getrennte Chats für Bewertung und
> Ergebnisliste führen dazu, dass die Ergebnisse nur im Gesprächsverlauf existieren.

---

## 1 · Eingabe finden

**Speicherort:** `Schulungsmaterial/KI-Beauftragte/Arbeitsproben/[Vollname]/` (bzw. ein vom
Dozenten genannter Sammelordner, z. B. `Projektarbeiten für Alfa`).

> **Zielordner pro Durchlauf abklären, bevor die ersten Bögen abgelegt werden.** Er ist nicht
> pro Durchlauf gleich: Der Hauptdurchlauf KLR-295 liegt unter `Arbeitsproben/[Name]/`, die
> Alfatraining-Kohorte unter `Projektarbeiten für Alfa/`. Nicht aus dem Vorgänger ableiten.

**Namensschema (Regelfall):** Dateiname enthält `[Vorname]_[Nachname]_Projektarbeit_KLR-…`
(Kursnummer variabel). Formate: pdf, html, docx.

**Abweichungen sind normal — prüfen, nicht raten:**
- **Aufgeteilt** in mehrere Dateien (z. B. `…_A1_…`, `…_Teil_B_…`, `_1.html`/`_2.html`) →
  alle Teile lesen und gemeinsam als eine Projektarbeit bewerten.
- **Abweichender Name** (nur „Projektarbeit_[Vorname]“, oder Titel wie
  „KI-Strategie …“) → per Datum (jüngste) und Inhalt identifizieren.
- **Cloud-only (OneDrive):** kann sein, dass `bash`/`ls` die Datei kurz nach dem Upload noch
  nicht sieht. Dann erneut prüfen oder per Read-Tool herunterladen.
- **Nur Tages-Übungen / kein zusammenhängendes A/B/C / leerer Ordner** → **nicht bewerten**.
  Dem Dozenten melden und fragen, welche Datei die finale Projektarbeit ist bzw. ob sie noch
  aussteht. **Niemals eine Note erfinden.**
- **Unvollständige Einreichung → warten, nicht abwerten.** Fehlt ein Teil, wird **kein Bogen
  mit 0-Wertung** erzeugt. Melden, auf Nachreichung warten und erst bei Vollständigkeit in
  einem Rutsch bewerten. Nachreichungen sind der Normalfall, nicht die Ausnahme (Krankheit,
  gestaffelte Abgabe) — im Hauptdurchlauf kam eine Arbeit in drei Etappen.
- **Namensabweichung zwischen Datei und Ordner/Kundenliste** (z. B. Zweit- oder Geburtsname in
  der Datei) → **nicht stillschweigend zusammenführen**. Als vermutlich dieselbe Person
  bewerten, die Abweichung aber ausdrücklich zur Bestätigung vorlegen.

---

## 2 · Variante bestimmen (Aufgaben-Maßstab)

Aus der eingereichten Arbeit erkennen, welche Variante bearbeitet wurde, und die passende
**Aufgabendatei auf GitHub als Maßstab lesen** (`KI_Schulungen_UNO/Use Cases/`):

- **KIB Variante 1 — Recruiting & Onboarding einer KIB** (`Projektarbeit_KIB_1.md`)
  Perspektive „Head of AI“. Drei Teile:
  **A** Recruiting = Arbeitsplatzbeschreibung **und** öffentliche Stellenanzeige **und**
  Interviewleitfaden für CISO/GF **und** eigene Interviewvorbereitung.
  **B** Anforderungen an die 100-Tage-AI-Management-Roadmap (nicht die fertige Roadmap) +
  Rollenabgrenzung (KIB vs. Head of AI, DSB, KI-Projektmanager) + Priorisierungslogik mit
  **zwei** Beispielen.
  **C** Onboarding-Prozess + kennenzulernende Rollen + Erfolgskriterien + kulturelle
  „Druckbetankung“.
- **KIB Variante 2 — KI in der öffentlichen Verwaltung** (`Projektarbeit_KIB_2.md`),
  fiktive Gemeinde ~54.000 Einwohner. Drei Teile:
  **A** KI in der Verwaltung = Chancen/Risiken-Profil + spannende Initiativen/bewährte
  Praktiken **andernorts** (konkret benannt) + sektorspezifische Risiken + Anpassung an die
  Gemeinde.
  **B** KI bei uns = Inventarisierung bestehender KI (inkl. Schatten-KI) + Aufnahme und
  Bewertung neuer Anwendungsfälle.
  **C** Kommunikation & Change Management.
- **KIM** (`Projektarbeit_KIM_1.md`): eigene Struktur (Branche / eigener Use Case /
  „größtes Umdenken“) mit **anderer Gewichtung 40/40/20**. Nur verwenden, wenn die Arbeit
  tatsächlich dieser Struktur folgt. **Achtung:** Teilnehmende des KIM-Kurses bearbeiten in
  der Praxis oft trotzdem die KIB-Variante-1-Aufgabe — **immer nach der tatsächlich
  bearbeiteten Struktur bewerten**, nicht nach dem Kursnamen.

> **Variante und Gewichtung folgen der Struktur, das Fach-Feld folgt der Anweisung — beides
> ist voneinander unabhängig.** Im Alfatraining-Durchlauf lautete die Anweisung für zwei
> Personen zunächst „Fach: KI-Manager(in)“; beide hatten inhaltlich die KIB-Recruiting-/
> 100-Tage-/Onboarding-Struktur bearbeitet. Eine daraufhin vorgenommene Umstellung auf die
> KIM-Gewichtung 40/40/20 war falsch. Regel: **Gewichtung aus der eingereichten A/B/C-Struktur
> ableiten** (Abschnitt 3.2), **Fach-Kopf genau so eintragen, wie angesagt** (Abschnitt 4) —
> im Zweifel nachfragen, nie das eine aus dem anderen herleiten.

**Ein Pflichtteil kann unter eigenem Namen oder in anderer Reihenfolge stehen.** Vor jedem
Abzug wegen „fehlt“ prüfen, ob der geforderte Teil unter abweichender Überschrift oder an
anderer Stelle im Dokument vorhanden ist. Beispiel: Ein Teil B stand als „100-Day Flight Plan“
und vor der Stellenanzeige und wurde zunächst als lückenhaft gewertet (87 statt 91). Im Zweifel
zugunsten der Vollständigkeit entscheiden.

**Extrapunkte** stehen jeweils in der Aufgabendatei (z. B. attraktive, den Firmencharakter
spiegelnde Stellenanzeige und kreative kulturelle Einarbeitung bei V1; SWOT, fundierte
Stakeholder-Analyse, konkrete Erfolgs-/Warnindikatoren bei V2). **Extrapunkte sind Kür, nicht
Pflicht** — ihr Fehlen ist **kein** Abzugsgrund; ihr Erreichen rechtfertigt das obere Ende.

---

## 3 · Rubrik

### 3.1 Offizielle Skala (Bewertungsbogen)

Gesamt max. **100 Punkte**:

| Gesamtpunkte | Bewertung |
|---|---|
| 100–81 | mit ausgezeichnetem Erfolg |
| 80–50 | mit sehr gutem Erfolg |
| 49–0 | erfolgreich |

### 3.2 Gewichtung (Aufgaben-Maxima)

Standard **34 / 33 / 33** (Teil A/1 = 34, Teil B/2 = 33, Teil C/3 = 33; Summe 100).
Ausnahme KIM-Struktur: **40 / 40 / 20**. Die Maxima werden im Bogen je Aufgabe eingetragen.

### 3.3 Leitprinzip (wohlwollend, beschwerdesicher)

Die Norm des Anbieters ist ein Spitzenergebnis: Teilnehmende erreichen in der Regel **≈ 85+**
(„mit ausgezeichnetem Erfolg“). Ziel ist **nicht** feines Ranking, sondern:

> Die Norm wohlwollend abbilden — und **jede Abweichung nach unten belegen**, weil nur
> Minderbewertungen zu Beschwerden führen.

- Erfüllt die Arbeit die Aufgabenstellung → zügig in den Normbereich (≈ 85–100) einordnen.
- **Punktabzug nur bei einem konkreten, im Dokument belegbaren Mangel** gegenüber der
  Aufgabenstellung. Mehrdeutigkeit oder ein unkonventioneller, aber vertretbarer Ansatz sind
  **kein** Abzugsgrund. Im Zweifel die höhere Bewertung.
- **Faktische / regulatorische Fehler** (z. B. Verwechslung von EU-AI-Act-Artikeln, falsche
  Fristen) sind ein **belastbarer** Abzugsgrund.
- Ein **vollständig fehlender Pflichtbestandteil** (z. B. Stellenanzeige fehlt in V1-A;
  Rollenabgrenzung/Priorisierungsbeispiele fehlen in V1-B) ist ein belegbarer Mangel.

### 3.4 Begründungstiefe (nach Punktzahl)

| Gesamtpunktzahl | Begründung je Aufgabe |
|---|---|
| **81–97** (Normbereich) | **knappe Zeile** je Aufgabe; Vorschlagswert genügt |
| **> 97** (Spitze) | **ausführlich** – herausragende Qualität und erreichte Extrapunkte konkret benennen (mit Fundstelle) |
| **< 81** (unter „ausgezeichnet“) | **ausführlich und beschwerdesicher** (siehe 3.5) |

### 3.5 Belegpflicht bei Punktabzug (< 81 bzw. jede Minderbewertung)

Die Begründung muss:
1. den Mangel **konkret benennen** (nicht „etwas dünn“, sondern „der geforderte
   Kommunikationsplan fehlt vollständig“),
2. ihn mit **wörtlichem Beleg oder präziser Fundstelle** aus der Arbeit verankern (zitieren
   statt interpretieren),
3. ihn auf die **Aufgabenstellung** zurückbinden („gefordert war …, geliefert wurde …“),
4. **sachlich, nicht wertend** formuliert sein (beschreibt die Lücke, nicht die Person).

### 3.6 Was NICHT in die Bewertung einfließt

- **Das Ergebnis der TÜV-Zertifizierungsprüfung.** Die Projektarbeit wird eigenständig
  bewertet. Eine nicht bestandene Prüfung ist weder ein Abzugsgrund noch wird sie im Bogen
  erwähnt — im Hauptdurchlauf trug die Arbeit der einzigen Nichtbesteherin regulär
  „mit ausgezeichnetem Erfolg“ (89).
- **Quiz-Ergebnisse, Anwesenheit, Mitarbeit, das laufende Kurs-Feedback.** Diese gehören in
  den Skill `teilnehmer-bewertung`, nicht in den Bewertungsbogen.
- **Die Leistung anderer Teilnehmender.** Kein Ranking, keine Ankerung an der zuletzt
  bewerteten Arbeit.

### 3.7 Kalibrierung

Denselben Maßstab konsequent anwenden. Vollständigkeit gegenüber der Aufgabenstellung schlägt
Stil: eine vollständige, aber generische Arbeit steht über einer unvollständigen, aber
polierten. Regulatorische Präzision (artikelgenaue Bezüge, aktuelle Fristen), belegte
Referenzbeispiele und ausgeführte (statt nur genannte) Pflichtbestandteile heben nach oben.
Bei Unsicherheit über die relative Einordnung dem Dozenten die Kalibrierung vorlegen.

### 3.8 Stil der Begründungen

Du-Form ist hier **nicht** nötig (der Bogen ist ein Dozenten-Dokument); sachlich in der
3. Person/neutral. Deutsch. Abkürzungen beim ersten Auftreten ausschreiben. Keine
Optionsbuchstaben, keine erfundenen Quellen/URLs.

---

## 4 · Kopf-Standardwerte (pro Durchlauf)

Diese Werte sind für alle Bögen eines Durchlaufs gleich, unterscheiden sich aber **zwischen
Kursen/Durchläufen**. **Vor der ersten Bewertung eines neuen Durchlaufs bestätigen lassen:**

- **Fach:** je Kurs — z. B. „KI-Beauftragte(r)“ oder „KI-Manager(in)“.
- **Datum:** Prüfungs-/Bewertungsdatum des Durchlaufs.
- **Zeitdauer / Zeitraum:** z. B. „01.–02.07.2026“ oder „Juli 2026“.
- **Dozent:** i. d. R. „Ulrich Nord“.
- **Ort:** i. d. R. „remote“.
- **Hilfsmittel:** i. d. R. „Mammouth AI“.

Bekannte Werte als Anhaltspunkt (immer gegenprüfen): KIB-Hauptdurchlauf KLR-295 = Fach
„KI-Beauftragte(r)“, Datum 03.07.2026, Zeitdauer „01.–02.07.2026“. Alfatraining-Durchlauf =
Datum 31.07.2026, Zeitraum „Juli 2026“.

> **Das Fach-Feld ist keine Ableitung aus der Bewertung.** Es folgt ausschließlich der
> Durchlauf-Anweisung des Dozenten. Ein Bogen kann „Fach: KI-Beauftragte(r)“ tragen und
> zugleich nach KIM-Struktur bewertet sein — oder umgekehrt. Bei Unklarheit nachfragen,
> nicht aus der erkannten Variante herleiten. Ändert sich zwischen zwei Durchläufen nur ein
> Teil der Kopfwerte („Datum und Zeitraum haben sich geändert, der Rest bleibt gleich“), die
> unveränderten Werte trotzdem einmal bestätigen lassen.

---

## 5 · Ausgabe: den offiziellen Bogen befüllen

**Vorlage:** `Kursmaterialien/Vorlage_Projektarbeit.docx` — eine **Kopie** wird per
`python-docx` befüllt. Aufbau der Vorlage: Kopf-Absätze (Fach/Datum/Zeitdauer/Dozent/Ort/
Hilfsmittel), Bewertungsschlüssel-Tabelle, je Aufgabe „Aufgabe N:“ + „Erreichte Punktzahl: __
Punkte von maximal __ Punkten“ + „Begründung:“, sowie eine Namens-/Gesamtpunkt-Tabelle
(„Name, Vorname“ und „Erreichte Punktzahl … von maximal 100 Punkten“).

**Zu füllen:**
- Kopf-Werte (Abschnitt 4).
- **Name, Vorname** der Person (Format „Nachname, Vorname“).
- Je Aufgabe: kurze **Beschreibung** (Teil A/B/C der erkannten Variante) + **Punkte** +
  **Maximum** (34/33/33) + **Begründung**.
- **Gesamtpunktzahl** /100 und **Bewertungsstufe** (aus 3.1). Die Gesamtstufe zusätzlich als
  eine deutliche Zeile vor dem Bewertungsschlüssel eintragen
  („Gesamtergebnis: N von 100 Punkten – mit ausgezeichnetem Erfolg“).
- **Kein Entwurfs-Vermerk im Dokument** (die Freigabe erfolgt außerhalb, durch Sichtung vor
  dem Hochladen).

**Robustes Füll-Skript** (Absätze per Text-Label finden, nicht per fester Indexnummer):

```python
from docx import Document
from docx.shared import RGBColor
import shutil, subprocess, os

TPL  = "<Pfad>/Kursmaterialien/Vorlage_Projektarbeit.docx"
OUT  = "<Zielordner>/[Vorname]_[Nachname]_Projektarbeit_Bewertung_KLR-<nr>.docx"

# --- Eingaben ---
KOPF = {"Fach:":"KI-Beauftragte(r)", "Datum:":"31.07.2026", "Zeitdauer:":"Juli 2026",
        "Dozent:":"Ulrich Nord", "Ort:":"remote", "Hilfsmittel:":"Mammouth AI"}
NAME = "Nachname, Vorname"
GESAMT = 95
STUFE  = "mit ausgezeichnetem Erfolg"
AUFG = [  # (Beschreibung, Punkte, Maximum, Begründung)
    ("Teil A – …", 32, 34, "…"),
    ("Teil B – …", 32, 33, "…"),
    ("Teil C – …", 31, 33, "…"),
]

d = Document(TPL); paras = d.paragraphs

def append(par, text, bold=False):
    r = par.add_run(text)
    if bold: r.bold = True

# Kopf: Label-Absatz finden, Wert anhängen
for label, val in KOPF.items():
    for p in paras:
        if p.text.strip().startswith(label):
            append(p, val); break

# Gesamtergebnis-Zeile in den leeren Absatz direkt vor "Bewertungsschlüssel"
for i, p in enumerate(paras):
    if p.text.strip().startswith("Bewertungsschlüssel"):
        j = i-1
        while j>0 and not paras[j].text.strip(): j-=1  # letzter nichtleerer davor
        # in den ersten leeren Absatz oberhalb schreiben:
        target = paras[i-1] if not paras[i-1].text.strip() else paras[i]
        append(target, f"Gesamtergebnis: {GESAMT} von 100 Punkten – {STUFE}", bold=True)
        break

# Aufgaben-Überschriften / Punkte / Begründungen (jeweils in Reihenfolge)
head = [p for p in paras if p.text.strip() in ("Aufgabe 1:","Aufgabe 2:","Aufgabe 3:")]
pkt  = [p for p in paras if p.text.strip().startswith("Erreichte Punktzahl:")]
begr = [p for p in paras if p.text.strip().startswith("Begründung:")]
for k,(besch,pt,mx,bg) in enumerate(AUFG):
    append(head[k], " "+besch)
    # Punktzahl-Absatz hat Runs: [0]Label [1]\t [2]\t [3]"Punkte von maximal " [4]spaces [5]"Punkten"
    P = pkt[k]
    if len(P.runs) >= 5:
        P.runs[1].text = f"  {pt}  "; P.runs[4].text = f"  {mx}  "
    else:
        append(P, f"  {pt}  von maximal  {mx}  ")
    append(begr[k], " "+bg)

# Namens-Tabelle: "Name, Vorname"-Zeile + Gesamtpunkt-Zeile
t = d.tables[0]
for row in t.rows:
    cells = [c.text.strip() for c in row.cells]
    if cells and cells[0].startswith("Name, Vorname"):
        row.cells[1].text = NAME
    if cells and cells[0].startswith("Erreichte Punktzahl"):
        row.cells[1].text = str(GESAMT)

d.save(OUT)
# PDF erzeugen (LibreOffice headless)
subprocess.run(["soffice","--headless","--convert-to","pdf","--outdir",
                os.path.dirname(OUT), OUT], check=False)
```

> Vor dem ersten Lauf auf einer **neuen** Vorlage kurz die Absatzstruktur prüfen
> (`for i,p in enumerate(d.paragraphs): print(i, repr(p.text))`), falls Labels abweichen.
> `python-docx` und `pdfplumber` ggf. per `pip install … --break-system-packages` nachziehen.

**Dateiname:** `[Vorname]_[Nachname]_Projektarbeit_Bewertung_KLR-<Kursnummer>.docx` (+ `.pdf`).
**Ablageort:** der Ordner der Person **oder** ein vom Dozenten genannter Sammelordner. Immer
**beide Formate** (docx + PDF) ablegen, sofern nicht anders gewünscht.

---

## 6 · Abschluss

Ergebnis **knapp** zusammenfassen: je Aufgabe Punkte + ein Satz, Gesamt + Bewertungsstufe, und
eine kalibrierende Einordnung (relative Stärke). **Ausnahmen ausdrücklich zum Gegenlesen
markieren:** Arbeiten **> 97** (Spitze) und **< 81** (Minderbewertung) — dort trägt die
Begründung eine mögliche Rückfrage. Den ausgefüllten Bogen (docx + PDF) dem Dozenten
präsentieren.

---

## 7 · Ergebnisübersicht fortschreiben (Pflichtschritt)

**Datei:** `Schulungsmaterial/Kursmaterialien/Bewertungsuebersicht_Projektarbeiten.xlsx`
— die **alleinige Quelle** für Ergebnisse über alle Kurse und Durchläufe hinweg. Sie ist
personenbezogen und gehört **nicht** ins GitHub-Repo.

**Nach jeder Bewertung** eine Zeile im Blatt `Bewertungen` ergänzen: Durchlauf · Nachname ·
Vorname · Kurs · Variante · Teil A/B/C · Gesamt · Zensur · Bewertungsdatum · Bogen erstellt ·
Referenz · Anmerkung. Spalte **Gesamt** und **Zensur** sind Formeln — aus der Zeile darüber
kopieren, nie Werte eintragen. Auf dem Blatt `Kennzahlen` die Formelbereiche erweitern.

**Formatregeln (vereinbart, nicht verhandelbar):**
- **Sortierung** alphabetisch nach Nachname innerhalb des Durchlaufs, wie in der offiziellen
  Kundenliste.
- **Anomalien werden sichtbar gehalten, nicht bereinigt.** Doppelte Einträge in der
  Kundenliste, abweichende Dateinamen, unklare Personenidentitäten kommen in die Spalte
  „Anmerkung“ **und** auf das Blatt `Offene Punkte` — nicht stillschweigend zusammenführen.
- **Personen ohne Einreichung bleiben in der Liste**, rot hinterlegt, mit „—“ bzw. „n/a“.
  Löschen würde die Lücke unsichtbar machen.
- **Referenz:** „Ja“ = erstellt · **„n/a“ = nicht angefragt** (nie „Nein“ — das läse sich wie
  eine verweigerte Leistung).
- **Rundung** der Durchschnittspunktzahl auf eine Nachkommastelle.
- **Zensur** ausschließlich nach der Skala aus 3.1.

**Was auf die Urkunde geht, ist bislang nicht festgelegt.** Übernommen wird bis auf Weiteres
nur die Gesamtpunktzahl aus dem Bewertungsbogen. Nicht eigenmächtig ergänzen — beim Dozenten
nachfragen.

---

## Verhältnis zu den anderen Skills

- **`teilnehmer-bewertung`** — laufendes formatives Kurs-Feedback und Referenzprofile.
  Dessen `reference/bewertungs-rubrik.md` ist **abgelöst**: Der Maßstab für die Projektarbeit
  steht ausschließlich hier in Abschnitt 3. Bei Widerspruch gilt dieser Skill.
- **`gesamtreferenz`** — kursübergreifende Kompetenzreferenz für Teilnehmende mehrerer Kurse.

## Was dieser Skill NICHT tut
- Keine endgültige Note; er schreibt nichts selbst in die Urkunde.
- Er erfindet keine Inhalte, keine Quellen und keine Bewertung bei fehlender/unvollständiger
  Einreichung — dann wird nachgefragt.
- Er überträgt Maßstäbe nicht ungeprüft zwischen Kursen/Varianten.

