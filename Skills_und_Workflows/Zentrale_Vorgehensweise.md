# Zentrale Vorgehensweise — KI-Kurse

> Dieses Dokument ist die **einzige verbindliche Referenz** für Quellenrecherche, Content-Pflege und Quiz-Erstellung in den drei Kursen.  
> Es ersetzt `Quellen_Workflow.md` (archiviert).  
> Gilt für: KI-Beauftragter (KIB · Modul 764), KI-Manager (KIM · Modul 763), Manager KI-Transformation (MAT).  
> Letzte Aktualisierung: 2026-09-17

---

> ## ⚠️ Ablageänderung vom 17.09.2026 — bitte zuerst lesen
>
> *(Ergänzt 18.09.2026: **Auch der Intake liegt jetzt dort.** Register und Intake sind damit im selben Ordner `Schulungsmaterial\Zentrale Referenzdokumente\` — zusammen mit den Referenz-PDFs. Die Einträge unten sind angepasst. Die inhaltliche Trennung bleibt: Register = Ergebnis und öffentlich zitierfähig, Intake = Werkstatt mit Verwerfungsgründen.)*
>
> **Das Quellenregister und das News-Update liegen nicht mehr im GitHub-Repositorium.** Beide wurden in einen neuen lokalen Ordner **verschoben** (nicht kopiert — es gibt jeweils nur eine Fassung):
>
> `OneDrive\Schulungsmaterial\Zentrale Referenzdokumente\`
>
> In demselben Ordner liegen seither auch die Referenz-PDFs, die zuvor unter „Interessante Dokumente" geführt wurden — KI-Verordnung, DSGVO/BDSG, DIN EN ISO/IEC 42001:2026-08, NIST-Rahmenwerk, ICB 4 und weitere.
>
> **Zwei Folgen, die zu beachten sind:**
> 1. **Im öffentlichen Repositorium fehlen beide Dateien nach dem nächsten Commit.** Wer sie über GitHub Pages verlinkt hatte, muss den Verweis anpassen oder entfernen.
> 2. **Der Intake bleibt, wo er ist** (`Schulungsmaterial\Kursmaterialien\`). Die Trennung ist gewollt: Das Register ist Ergebnis, der Intake ist Werkstatt.

---

## 1 · Fünf Informationsquellen — Funktionen und Pfade

### 1a · Quellen_und_Dokumente_KI-Kurse.md (lokal — Zentrale Referenzdokumente · Pflichtlektüre vor jedem Kurstag-Review)

**Pfad:** `OneDrive\Schulungsmaterial\Zentrale Referenzdokumente\Quellen_und_Dokumente_KI-Kurse.md`  
**Funktion:** Verbindliches Quellenregister. Alle für die Kurse freigegebenen Quellen sind hier gelistet, mit Kurszuordnung und Verwendungskontext. Dieses Dokument wird **zuerst** gelesen, bevor Kursmaterialien erstellt oder aktualisiert werden.

**Qualitätsanspruch:** Hoch — ausschließlich Tier-1-Quellen (siehe Abschnitt 1c).

---

### 1b · Neue_Quellen_Intake.md (lokal — `Schulungsmaterial\Zentrale Referenzdokumente\`)

**Funktion:** Ideensammlung. Neue Informationen mit didaktischem Potenzial werden hier gesammelt und bewertet, bevor sie in Kursmaterialien eingebaut werden.

**Wann hierhin:**
- Studien, Artikel, Grafiken oder Use Cases mit Kurspotenzial
- Noch nicht verifizierte Preprints oder Working Papers
- LinkedIn-Posts, Unternehmensberichte, Konferenzbeiträge
- Neue KI-Tools oder Praxisbeispiele
- Diskussionsimpulse (auch mit Qualitätsvorbehalt)

**Qualitätsanspruch:** Niedrig bis mittel — auch Tier-3-Quellen erlaubt, müssen als solche gekennzeichnet sein. Entscheidend ist der **didaktische Wert**, nicht der akademische Rang.

**Format je Eintrag:** Bewertung (✅ / ⚠️ / ⛔) · Passend zu (Kurs + Tag) · Kurzbeschreibung · Kernargument · Qualitätsvorbehalt · Quelle + Urheber.

---

### 1c · KI_News_Update.html (lokal — Zentrale Referenzdokumente · regulatorischer Stand)

**Pfad:** `OneDrive\Schulungsmaterial\Zentrale Referenzdokumente\KI_News_Update.html`  
**Funktion:** Verbindliche Referenz für den aktuellen regulatorischen und technologischen Stand. Wird bei Kurstag-Reviews geprüft.

**Wann hierhin:**
- Änderungen an Gesetzen oder Normen (EU AI Act, DSGVO, ISO 42001 etc.)
- Neue oder geänderte Fristen mit direkter Kursrelevanz
- Offizielle Publikationen von Behörden (BSI, EDPB, NIST, EU-Kommission)
- Verifizierte Marktdaten aus Tier-1-Quellen
- Neue Standards oder Leitlinien (ISO, NIST, BSI)

**Tier-1-Quellen (immer erlaubt):**
- Behörden: eur-lex.europa.eu · bsi.bund.de · edpb.europa.eu · nist.gov · federalreserve.gov
- Offizielle Anbieter-Dokumentation: learn.microsoft.com · cloud.google.com · openai.com/research
- Standards-Organisationen: iso.org · nist.gov
- Peer-reviewte Institute: arXiv · PNAS · Stanford HAI · NBER · MIT Media Lab

**Nicht erlaubt:** Unternehmens-Blogs, Handelsmedien, Einzelperson-Blogs — es sei denn als explizit gekennzeichneter Praxishinweis.

---

### 1d · Wochenberichte (lokal — Schulungsmaterial/Wochenberichte/)

**Pfad:** `Schulungsmaterial/Wochenberichte/` (OneDrive, lokal)  
**Funktion:** Markt- und Branchenupdates — **kein** Teilnehmermaterial. Die Wochenberichte sind wöchentlich erstellte Zusammenfassungen relevanter KI-Entwicklungen aus dem Markt. Sie dienen ausschließlich der Aktualisierung und Anreicherung der Kursinhalte.

> ⚠️ Wichtig: Wochenberichte ≠ Teilnehmer-Unterlagen. Inhalte aus den Wochenberichten fließen in Hand-Outs, Gamma-Präsentationen und Quizze ein — nicht umgekehrt.

---

### 1e · DIN EN ISO/IEC 42001:2026-08 (lokal — Normtext im Volltext)

**Pfad:** `Schulungsmaterial/Zentrale Referenzdokumente/Norm DIN ISO-IEC 42001 Künstliche Intelligenz_08-2026.pdf` *(seit 17.09.2026; zuvor „Interessante Dokumente")*  
**Vollständiger Titel:** DIN EN ISO/IEC 42001:2026-08 — *Informationstechnik – Künstliche Intelligenz – Managementsystem*  
**Ausgabe:** E-Book-Sonderausgabe 2026 (alfatraining), 72 Seiten

**Funktion:** Der **Normtext selbst** — die maßgebliche Quelle für alle Aussagen zu ISO/IEC 42001 in den Kursmaterialien. Bisher wurde die Norm über Sekundärquellen zitiert (Beratungs-Websites, ISO-Einführungsseiten). Ab sofort gilt: **Aussagen über Normanforderungen werden am Normtext geprüft, nicht an Sekundärliteratur.**

**Wann zu prüfen:**
- Immer, wenn eine Kursaussage eine **Anforderung, ein Kapitel oder eine Anhang-A-Kontrolle** der ISO 42001 benennt
- Bei Aktualisierung der Kurstage mit ISO-Bezug — u. a. KIB Tag 1, 8, 10–17; KIM Tag 2, 11, 12
- Vor jeder Aussage zur **Zertifizierungsreife** oder zum Anwendungsbereich
- Bei Änderungen an der ISO-42001-Checkliste und am Anwendbarkeitsnachweis (SoA)

**Wichtige Änderung gegenüber dem bisherigen Stand:** Die Kursmaterialien zitieren überwiegend **ISO/IEC 42001:2023**. Die hier vorliegende Fassung ist die **europäisch übernommene deutsche Ausgabe DIN EN ISO/IEC 42001:2026-08**. Bezeichnung und Ausgabestand sind bei jeder Aktualisierung anzugleichen — die Zitierregel steht in `Quellen_und_Dokumente_KI-Kurse.md`, Abschnitt K.4.

> ⚠️ **Urheberrecht — zwingend beachten.** Normtexte sind urheberrechtlich geschützt; dies ist eine lizenzierte Ausgabe. **Kein Wortlaut aus dem Normtext in Teilnehmermaterialien.** Zulässig sind: sinngemäße Wiedergabe mit Kapitelverweis, Nennung von Kapitel- und Kontrollnummern, eigene Formulierungen. Nicht zulässig: Abdruck von Anforderungstexten, Tabellen oder Anhang-A-Formulierungen im Wortlaut.

---

### 1f · Die Hand-Outs selbst (lokal — in den Tagesordnern, **dort bleiben sie**)

**Pfade:** `Schulungsmaterial/KI-Beauftragte/Tag NN/TagNN_HandOut.html` · `Schulungsmaterial/KI-Manager/Tag NN/TagNN_HandOut.html`

**Hier wird nichts verschoben.** Dieser Abschnitt legt keinen neuen Ablageort fest, sondern eine **Prüfpflicht**: Die Hand-Outs sind bei jeder Quellenfrage **mit zu durchsuchen**.

> ### ⚠️ Die Regel, die aus einem Fehler vom 17.09.2026 stammt
>
> An diesem Tag wurde gemeldet, zwei Quellen zur Datendokumentation (Gebru „Datasheets for Datasets"; „Data Statements") seien **nicht** in unseren Beständen. Geprüft worden waren Register und Intake. **Beide standen längst im Quellenverzeichnis von KIB Tag 15**, eine dritte (Data Cards) war seit Monaten in einer Praxisaufgabe in KIM Tag 7 im Einsatz — **ohne je im Register zu stehen**.
>
> **Daraus folgt:**
> 1. **Das Register ist gegenüber den Hand-Outs unvollständig.** Es ist damit **keine hinreichende** Prüfinstanz für die Frage „haben wir das schon?".
> 2. **Der Prüfumfang bei jeder Quellenfrage lautet: Register + Intake + Hand-Outs.** Nicht zwei von dreien.
> 3. Ein **Negativbefund** („diese Quelle ist neu") darf erst ausgesprochen werden, wenn alle drei geprüft sind — sonst wird er als „geprüft" gelesen, obwohl er es nicht ist.

**Nachgelagerte Aufgabe, noch offen:** Ein systematischer Abgleich **Hand-Outs → Register**. Alle Quellen, die in einem Hand-Out-Quellenverzeichnis stehen, aber nicht im Register, sind nachzutragen. Der Umfang ist unbekannt; die drei oben waren ein Zufallsfund.

---

### 1g · Werkzeug: `Werkzeuge/Quellencheck.html` (GitHub-Repositorium)

**Funktion:** Beantwortet in Sekunden, ob eine Quelle bereits bewertet wurde — einzeln oder für eine ganze Liste aus einem Newsletter.

**Arbeitsweise:** Die Seite hält **keine Kopie** der Bestände vor, sondern liest die Dateien, die man hineinzieht. Damit ist sie nie veraltet. Alles bleibt im Browser, es wird nichts gesendet.

**Was hineingehört — entsprechend der Regel in 1f alle drei:**
`Quellen_und_Dokumente_KI-Kurse.md` · `Neue_Quellen_Intake.md` · die betroffenen `TagNN_HandOut.html`

**Erkennt als dieselbe Quelle:** arXiv-Adressen über die Nummer (`abs/` = `html/` = `pdf/`, auch bloßes `arXiv:1910.07467` ohne Adresse), SSRN über `abstract_id`, DOI über die DOI, alles Übrige über Adresse und Pfad ohne `www.` und **ohne Anhängsel wie `?utm_source=…`**.

> **Grenze:** Ein Nicht-Treffer beweist nicht, dass eine Quelle neu ist — manches steht ohne Adresse im Bestand (Bezahlschranke, PDF-Download, Buch). Dafür hat das Werkzeug die Volltextsuche nach Autorenname oder Titelwort. **Bei einem Treffer kann man sich verlassen; bei einem Nicht-Treffer ist zusätzlich im Volltext zu suchen.**

---

## 2 · Entscheidungslogik: Was kommt wohin?

```
Neue Information empfangen
        │
        ├─ Regulatorische Änderung (Gesetz, Norm, Frist)?
        │         └─ Ja + verifiziert + Tier-1-Quelle  →  KI_News_Update.html + Quellenregister
        │
        ├─ Technologische Tatsache (neues Modell, Standard, offizielle Kennzahl)?
        │         └─ Ja + Primärquelle verfügbar        →  KI_News_Update.html + Quellenregister
        │
        └─ Alles andere (Studie, Use Case, Diskussionsimpuls, Praxisbeispiel)?
                  └─ Didaktisches Potenzial vorhanden   →  Neue_Quellen_Intake.md
```

**Grenzfälle:**
- McKinsey-Bericht → Neue_Quellen_Intake (Praxisrelevanz) UND Quellenregister (wenn Kernzahlen zitiert werden)
- OpenAI Policy-Dokument → Neue_Quellen_Intake (Diskussionsimpuls), NICHT KI_News (keine neutrale Quelle)
- BSI-Veröffentlichung → KI_News + Quellenregister (Behörde, Tier 1)
- LinkedIn-Infografik → Neue_Quellen_Intake (wenn didaktisch wertvoll), NIE KI_News

---

## 3 · Kursseparation

Inhalte dürfen **nie 1:1** zwischen Kursen übertragen werden. Differenzierung nach Perspektive und Tiefe:

| Kurs | Perspektive | Tiefe |
|------|-------------|-------|
| **KIB** (Modul 764) | Compliance, Regulierung, operative Umsetzung | EU AI Act als Kerninhalt; Normen und Fristen detailliert |
| **KIM** (Modul 763) | Strategie, Führung, organisationale Transformation | EU AI Act nur als Hintergrundkontext |
| **MAT** | Angewandte Transformation, Projektsteuerung | Praxis und Umsetzung im Vordergrund |

EU AI Act ist **nur im KIB** ein eigenständiger Themenblock. In KIM und MAT erscheint er ausschließlich als Hintergrundreferenz.

Tagesinhalte (Hand-Out, Gamma, Quiz) dürfen nie ohne Adaption der Perspektive und Tiefe zwischen Kursen übertragen werden.

---

## 4 · Tages-Review-Workflow (Pflichtschritte)

Wird ein Kurstag (z.B. „KIB Tag 7") reviewed oder aktualisiert, gelten folgende vier Schritte in dieser Reihenfolge:

> **Seit 23.09.2026 als Skill hinterlegt: `kurstag-review`.** Der Workflow in diesem Abschnitt ist die inhaltliche Grundlage; der Skill ist die ausführbare Fassung mit fester Phasenfolge und Token-Disziplin. Aufruf: „Schau Dir KIM Tag 9 an" oder `/kurstag-review`. Diese Datei bleibt die Referenz für die *Regeln*, der Skill regelt den *Ablauf*. Ändert sich hier etwas Grundsätzliches, muss der Skill nachgezogen werden — er liegt nicht in diesem Repositorium, sondern im Konto und wird über `save_skill` aktualisiert.

### Schritt 1 — Quellenrecherche (immer zuerst)

1. `Quellen_und_Dokumente_KI-Kurse.md` lesen → alle für diesen Tag freigegebenen Quellen identifizieren
2. `Neue_Quellen_Intake.md` lesen → neue didaktische Ideen mit Relevanz für diesen Tag prüfen
2a. **Das Quellenverzeichnis des betroffenen Hand-Outs selbst lesen** → siehe Abschnitt 1f. Quellen können dort stehen, ohne im Register zu stehen. Wer diesen Schritt überspringt, hält Vorhandenes für neu und trägt womöglich doppelt ein.
3. `Wochenberichte/` lesen → aktuelle Markt- und Branchenupdates mit Relevanz prüfen
4. `KI_News_Update.html` prüfen → regulatorischen Stand für diesen Tag verifizieren
5. **Bei jedem ISO-42001-Bezug:** Normtext `DIN EN ISO/IEC 42001:2026-08` prüfen (Pfad siehe 1e) → Kapitel- und Kontrollnummern sowie Bezeichnung und Ausgabestand am Original verifizieren, nicht an Sekundärquellen
6. Web-Suche für Fakten, die älter als 6 Monate sein könnten (Fristen, Zahlen, Regulierungsstand)

> Alle inhaltlichen Aussagen in Kursmaterialien müssen mit einer nachvollziehbaren Quelle belegt sein. URLs nur verwenden, wenn sie als direktes Ergebnis einer Recherche vorlagen — keine konstruierten oder erinnerten URLs.

### Schritt 2 — Bestandsprüfung

Alle vorhandenen Dateien des Kurstages lesen:
- Hand-Out (HTML oder DOCX) — **führendes Tagesdokument**
- Gamma-Präsentation (Link oder exportierte Folien) — speist sich aus dem Hand-Out
- Quiz (falls vorhanden — beide Schwierigkeitsstufen, beide Rollen)

Bestandsaudit prüft: Inhaltliche Aktualität · Quellenbelege vorhanden? · Formatregeln eingehalten?

### Schritt 3 — Content-Update

Das **Hand-Out ist das führende Tagesdokument** und wird auf Basis der Quellenrecherche aktualisiert:
- Veraltete Fakten ersetzen (mit Quellenangabe)
- Neue relevante Inhalte aus Intake/Wochenberichten einbauen
- Stilregeln (Abschnitt 6) einhalten

Die **Gamma-Präsentation speist sich aus dem Hand-Out** (Zusammenfassung in separatem Chat) und wird nicht parallel doppelt gepflegt. Ein eigenständiges Dozenten-„Labor" wird nicht mehr geführt.

#### Schritt 3a — Formatprüfung nach jedem HTML-Einbau (Pflicht)

**Hand-Outs teilen sich kein gemeinsames Stylesheet.** Jede Datei trägt ihr eigenes `<style>`-Element. Eine Klasse, die in Tag 10 definiert ist, existiert in Tag 11 möglicherweise nicht — der Kasten wird dann als Fließtext ohne Rahmen gerendert, ohne dass eine Fehlermeldung erscheint.

Am 21.09.2026 fiel dadurch auf, dass **elf Hand-Outs** Klassen verwendeten, die dort nie definiert waren (vor allem die `.note`-Familie). Alle wurden nachgetragen. Damit das nicht wiederkehrt, nach **jedem** Einbau in eine HTML-Datei:

1. **Klassenabgleich** — jede im Rumpf verwendete `class` muss im `<style>`-Element derselben Datei eine Regel haben.
2. **Tag-Bilanz** — `<div>`/`</div>`, `<p>`/`</p>`, `<table>`/`</table>` zählen; bei Abweichung die Stelle suchen, nicht nur die Zahl ausgleichen.
3. **Kernbotschaften-Reihenfolge** — die Nummern in `kb-nr` müssen aufsteigend stehen. Neue Botschaften erhalten einen Buchstabenzusatz (⑦a), damit bestehende Nummern nicht verrutschen.

Punkte 1 und 2 laufen als Skript über alle Hand-Outs; Punkt 3 braucht eine Sichtprüfung der betroffenen Liste.

### Schritt 4 — Quiz prüfen oder erstellen

→ Vollständige Anforderungen: Abschnitt 5

Falls kein Quiz existiert: Vor der Erstellung **die zweite Rolle erfragen** (neben KIB-Beauftragter bzw. KIM-Manager — variiert je Kurstag und Themenkontext).

Falls Quiz existiert: Aktualität der Antworten prüfen (Fristen, Zahlen, regulatorische Aussagen können sich geändert haben). Veraltete Antworten korrigieren und Korrektheit verifizieren.

---

## 5 · Quiz-Anforderungen (vollständig)

### 5.1 Struktur

- **Keine Schwierigkeitsstufen.** Pro Quiz **2 × 5 Fragen**: ein Set für die Primärrolle des Kurses (KI-Manager:in bzw. KI-Beauftragte:r) und ein zweites für eine pro Kurstag festzulegende Rolle (z. B. Datenschutzbeauftragte:r, Betriebsrat, IT-Leitung, Geschäftsführer:in — je nach Thema des Tages).
- Vor der Erstellung eines neuen Quizzes: **Zweite Rolle erfragen**, sofern nicht bereits vorgegeben.
- Format: Multiple Choice, 4 Antwortoptionen. **1–3 richtige Antworten** je Frage — Verteilung ca. 20 % eine, 40 % zwei, 40 % drei richtige; **nie vier**. (Maßgeblich ist der KIM-Fragenpool; ersetzt die frühere Vorgabe „eine korrekte Antwort".)
- **Tonalität wie die TÜV-Prüfungsfragen:** Jede Frage beginnt mit einer knappen, konkreten Situationsschilderung (1–3 Sätze, generisch/anonym, **kein benannter Use Case**) und schließt mit „Welche Aussage(n) … ist/sind korrekt?". Die Situation ist **in die Frage eingewoben** — kein separater, dauerhaft eingeblendeter Use-Case-Block. Beispiel: „Ein Unternehmen will Belege anhand optischer Merkmale auf Betrug prüfen; die zugehörige Projektnummer wird oft handschriftlich eingetragen, sodass die KI mit verschiedenen Schriftbildern umgehen muss. Welche Aussage(n) über bildverarbeitende KI (Computer Vision) ist/sind korrekt?"

### 5.2 Formulierungsregeln

- **Niemals identische Formulierungen** zu den tatsächlichen TÜV-Prüfungsfragen verwenden — weder in Fragestellung noch in Antwortoptionen. Eigene Wortwahl ist Pflicht.
- **Du-Form** durchgehend (Fragestellung, Antwortoptionen, Erklärungen)
- **Keine Optionsbuchstaben in Erklärungen:** Erklärungsfelder (`explanation`/`exp`) dürfen niemals auf „A", „B", „C" oder „D" verweisen. Der Shuffle-Mechanismus macht Buchstaben bedeutungslos. Stattdessen inhaltlich erklären, warum die richtige Antwort korrekt ist.
- **Keine Zertifizierungsaussagen:** Nie formulieren „für die Prüfung wichtig", „für die Zertifizierung zählt" o.ä. — das erzeugt unnötigen Druck. Stattdessen inhaltliche Bedeutung betonen.
- **Abkürzungen ausschreiben:** Fachbegriffe wie Schutzbedarfsfeststellung (SBF), Datenschutz-Folgenabschätzung (DSFA), Risikoprioritätszahl (RPZ) beim ersten Auftreten ausschreiben.
- **Erklärungen gehören an eine shuffle-sichere Position.** Antwortoptionen werden bei jedem Durchlauf neu gemischt — eine Option darf deshalb nie voraussetzen, dass eine andere Option vorher gelesen wurde. Konkret: Die Auflösung einer Abkürzung, eine Legende oder eine Definition steht **im Szenario (`sc`) oder im Fragestamm (`q`)**, nicht in einer Antwortoption. Beide Felder werden nicht gemischt und erscheinen immer oberhalb der Optionen.
  - Zulässig: Abkürzung und Auflösung stehen **innerhalb derselben Option** („Der Population Stability Index (PSI) misst …").
  - Zulässig: Auflösung steht im Erklärungsfeld (`exp`) — dieses erscheint erst nach der Auswertung und ist daher unkritisch.
  - Unzulässig: Auflösung in Option A, Abkürzung in Option C.
  - Bei mehreren Kürzeln aus einem System (z. B. Mendelow-Matrix) gehört eine **Legende in den Fragestamm**: „… korrekt? (HI = hohes Interesse, GI = geringes Interesse, HM = hohe Macht, GM = geringe Macht)".
- **Jede Frage steht für sich.** Weil auch die Fragenreihenfolge gemischt wird, greift „beim ersten Auftreten erklären" nicht auf Quiz-Ebene, sondern **je Frage**. Was in Frage 3 erklärt wurde, ist in Frage 71 nicht vorausgesetzt.

### 5.3 Aktualitätsprüfung bei bestehenden Quizzen

Vor Verwendung eines bestehenden Quiz prüfen:
- Sind alle genannten Fristen noch korrekt? (EU AI Act, DSGVO, nationale Gesetze)
- Sind Marktdaten und Statistiken noch aktuell? (Adoptionsraten, Anzahl Hochrisikomodelle etc.)
- Entsprechen regulatorische Aussagen dem aktuellen Stand der Gesetzgebung?
- Wurden Normen (ISO 42001, ISO 31000) überarbeitet?

Veraltete Antworten müssen korrigiert werden, bevor das Quiz verwendet wird.

### 5.4 Qualitätssicherung

- Alle Antworten einer Überprüfung unterziehen: Ist die als „richtig" markierte Antwort tatsächlich korrekt?
- Distraktoren (falsche Antworten) müssen plausibel aber eindeutig falsch sein — keine Trick-Fragen
- Antwortzahl-Verteilung prüfen: Mix aus Fragen mit einer, zwei und drei richtigen Antworten (ca. 20/40/40); nie vier richtige
- Nach Quiz-Erstellung: Korrektheit aller Antworten verifizieren, bevor abgeliefert wird

---

## 6 · Stilregeln für alle Kursmaterialien

Diese Regeln gelten für Hand-Outs, Gamma-Präsentationen, Quizze, Übungsblätter und alle anderen Teilnehmer-zugewandten Materialien:

| Regel | Beschreibung |
|-------|-------------|
| **Du-Form** | Alle Materialien verwenden die Du-Form (nicht Sie) |
| **Abkürzungen** | Beim ersten Auftreten ausschreiben, danach Kurzform. Level 1/2/3 (nie L1/L2/L3). In Quizzen gilt „erstes Auftreten" **je Frage**, nicht je Quiz — und die Auflösung gehört ins Szenario oder den Fragestamm, nie in eine einzelne Antwortoption (siehe 5.2) |
| **Keine Zertifizierungsdruck-Aussagen** | Nie „für die Prüfung wichtig" o.ä. — inhaltliche Bedeutung betonen |
| **Optionsbuchstaben** | In Quiz-Erklärungen nie A/B/C/D referenzieren |
| **Quellenbelege** | Jede inhaltliche Aussage muss belegbar sein; keine konstruierten URLs |
| **Kursseparation** | Inhalte nie 1:1 zwischen KIB, KIM und MAT übertragen |
| **Nur Tier-1 in offiziellen Materialien** | In Hand-Outs und Gamma ausschließlich verifizierte Quellen |
| **Use Cases nicht im Hand-Out** | Use Cases werden im Hand-Out **nicht namentlich genannt** (keine Firmennamen, keine fallspezifischen Kennzahlen). Sie wohnen im Ordner `Use Cases/` (GitHub) und werden live durch den Dozenten eingeführt. Übungen im Hand-Out bleiben **use-case-neutral** formuliert (z. B. „das heute vorgestellte Unternehmen"). Vorteil: Hand-Out bleibt wiederverwendbar und kursübergreifend konfliktfrei. |
| **Keine Zeitangaben in Gamma** | Uhrzeiten und Zeitblöcke (z. B. „11:50–12:35 Uhr") gehören nicht in Gamma-Folien — weder als Folientitel noch als Unterzeile. Zeitplanung liegt beim Dozenten, nicht in der Präsentation. |
| **Tagesordnung → „Was uns heute erwartet?"** | Die Tagesstruktur-Folie heißt immer „Was uns heute erwartet?" und enthält eine einfache Bullet-Liste der Themenblöcke — keine Kernfragen-Spalte, keine Uhrzeiten. |
| **Übungsformat: immer „Praxisübung"** | Statt „Gruppenarbeit", „Einzelarbeit" oder „Partnerarbeit" wird einheitlich „Praxisübung" verwendet. Ob Einzel- oder Gruppenformat, entscheidet der Dozent situativ — das gehört nicht in die Folie. |

---

## 7 · Quiz-Auswertung: Quelle & Score-Definition

Für alle Auswertungen von Teilnehmer-Quizzen (Tagesquizze **und** Tag-17-„Prüfungssimulation"):

- **Einzige verbindliche Quelle:** das Live-Google-Sheet **„KI_Beauftragter_Quiz_Auswertung"**, Reiter „KI-Beauftragter" (bzw. „KI-Manager"). Immer **als XLSX** exportieren (alle Reiter) und **frisch** ziehen — die Stände ändern sich täglich, auch morgens.
- **Nicht verwenden:** `Auswertung_*.pbix` (statischer, oft veralteter/unvollständiger Stand) und der CSV-Export (liefert nur einen Reiter — Tag 17 fehlt dabei). Beides nur als Notbehelf, nie als Wahrheit.
- **Score-Definition (deckt sich mit dem Power BI des Dozenten):** **alle Antwortzeilen** werten — richtig / gesamt über sämtliche Antworten, **inklusive Wiederholungen**. Nicht „Erstantwort je Frage", nicht „Letztantwort". Bestehensgrenze **60 %**.
- **Teilabbrüche kenntlich machen:** Wer weniger als die volle Fragenzahl (Tag 17 = 51) beantwortet hat, wird als unvollständig markiert — sein Prozentwert ist nicht mit einem vollen Durchlauf vergleichbar.
- **Datenhygiene:** „Anonym"-Einträge und offensichtliche Doppelerfassungen (uneinheitliche Namensschreibung) vor der Auswertung prüfen bzw. ausschließen.

---

*Erstellt: 2026-06-22 · Zuletzt ergänzt: 2026-07-22 (Abschnitt 7) · Ersetzt: Quellen_Workflow.md · Maintainer: Uli Nord · Dozenten-Assistent: Claude (Anthropic)*
