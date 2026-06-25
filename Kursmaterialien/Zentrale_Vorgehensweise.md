# Zentrale Vorgehensweise — KI-Kurse

> Dieses Dokument ist die **einzige verbindliche Referenz** für Quellenrecherche, Content-Pflege und Quiz-Erstellung in den drei Kursen.  
> Es ersetzt `Quellen_Workflow.md` (archiviert).  
> Gilt für: KI-Beauftragter (KIB · Modul 764), KI-Manager (KIM · Modul 763), Manager KI-Transformation (MAT).  
> Letzte Aktualisierung: 2026-06-25

---

## 1 · Vier Informationsquellen — Funktionen und Pfade

### 1a · Quellen_und_Dokumente_KI-Kurse.md (GitHub — Pflichtlektüre vor jedem Kurstag-Review)

**Pfad:** `KI_Schulungen_UNO/Quellen_und_Dokumente_KI-Kurse.md`  
**Funktion:** Verbindliches Quellenregister. Alle für die Kurse freigegebenen Quellen sind hier gelistet, mit Kurszuordnung und Verwendungskontext. Dieses Dokument wird **zuerst** gelesen, bevor Kursmaterialien erstellt oder aktualisiert werden.

**Qualitätsanspruch:** Hoch — ausschließlich Tier-1-Quellen (siehe Abschnitt 1c).

---

### 1b · Neue_Quellen_Intake.md (lokal — Schulungsmaterial-Ordner)

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

### 1c · KI_News_Update.html (GitHub — regulatorischer Stand)

**Pfad:** `KI_Schulungen_UNO/KI_News_Update.html`  
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

### Schritt 1 — Quellenrecherche (immer zuerst)

1. `Quellen_und_Dokumente_KI-Kurse.md` lesen → alle für diesen Tag freigegebenen Quellen identifizieren
2. `Neue_Quellen_Intake.md` lesen → neue didaktische Ideen mit Relevanz für diesen Tag prüfen
3. `Wochenberichte/` lesen → aktuelle Markt- und Branchenupdates mit Relevanz prüfen
4. `KI_News_Update.html` prüfen → regulatorischen Stand für diesen Tag verifizieren
5. Web-Suche für Fakten, die älter als 6 Monate sein könnten (Fristen, Zahlen, Regulierungsstand)

> Alle inhaltlichen Aussagen in Kursmaterialien müssen mit einer nachvollziehbaren Quelle belegt sein. URLs nur verwenden, wenn sie als direktes Ergebnis einer Recherche vorlagen — keine konstruierten oder erinnerten URLs.

### Schritt 2 — Bestandsprüfung

Alle vorhandenen Dateien des Kurstages lesen:
- Hand-Out (HTML oder DOCX)
- Gamma-Präsentation (Link oder exportierte Folien)
- Quiz (falls vorhanden — beide Schwierigkeitsstufen, beide Rollen)
- Laborübungen / Fallstudien (falls vorhanden)

Bestandsaudit prüft: Inhaltliche Aktualität · Quellenbelege vorhanden? · Formatregeln eingehalten?

### Schritt 3 — Content-Update

Hand-Out und Gamma-Präsentation auf Basis der Quellenrecherche aktualisieren:
- Veraltete Fakten ersetzen (mit Quellenangabe)
- Neue relevante Inhalte aus Intake/Wochenberichten einbauen
- Stilregeln (Abschnitt 6) einhalten

### Schritt 4 — Quiz prüfen oder erstellen

→ Vollständige Anforderungen: Abschnitt 5

Falls kein Quiz existiert: Vor der Erstellung **die zweite Rolle erfragen** (neben KIB-Beauftragter bzw. KIM-Manager — variiert je Kurstag und Themenkontext).

Falls Quiz existiert: Aktualität der Antworten prüfen (Fristen, Zahlen, regulatorische Aussagen können sich geändert haben). Veraltete Antworten korrigieren und Korrektheit verifizieren.

---

## 5 · Quiz-Anforderungen (vollständig)

### 5.1 Struktur

- **Zwei Schwierigkeitsstufen:** Grundlagen (Level 1/2) und Fortgeschritten (Level 3)
- **Zwei Rollen:** Primärrolle des Kurses (z.B. KI-Beauftragter) + eine zweite, vom Dozenten festzulegende Rolle (z.B. Datenschutzbeauftragte:r, Betriebsrat, IT-Leitung — je nach Thema des Kurstages)
- Vor der Erstellung eines neuen Quizzes: **Zweite Rolle erfragen**, sofern nicht bereits vorgegeben
- Format: Multiple Choice, 4 Antwortoptionen (a/b/c/d), eine korrekte Antwort

### 5.2 Formulierungsregeln

- **Niemals identische Formulierungen** zu den tatsächlichen TÜV-Prüfungsfragen verwenden — weder in Fragestellung noch in Antwortoptionen. Eigene Wortwahl ist Pflicht.
- **Du-Form** durchgehend (Fragestellung, Antwortoptionen, Erklärungen)
- **Keine Optionsbuchstaben in Erklärungen:** Erklärungsfelder (`explanation`/`exp`) dürfen niemals auf „A", „B", „C" oder „D" verweisen. Der Shuffle-Mechanismus macht Buchstaben bedeutungslos. Stattdessen inhaltlich erklären, warum die richtige Antwort korrekt ist.
- **Keine Zertifizierungsaussagen:** Nie formulieren „für die Prüfung wichtig", „für die Zertifizierung zählt" o.ä. — das erzeugt unnötigen Druck. Stattdessen inhaltliche Bedeutung betonen.
- **Abkürzungen ausschreiben:** Level 1/2/3 (nie L1/L2/L3). Fachbegriffe wie Schutzbedarfsfeststellung (SBF), Datenschutz-Folgenabschätzung (DSFA), Risikoprioritätszahl (RPZ) beim ersten Auftreten ausschreiben.

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
- Schwierigkeitsverteilung prüfen: nicht alle Fragen Level 1, nicht alle Level 3
- Nach Quiz-Erstellung: Korrektheit aller Antworten verifizieren, bevor abgeliefert wird

---

## 6 · Stilregeln für alle Kursmaterialien

Diese Regeln gelten für Hand-Outs, Gamma-Präsentationen, Quizze, Übungsblätter und alle anderen Teilnehmer-zugewandten Materialien:

| Regel | Beschreibung |
|-------|-------------|
| **Du-Form** | Alle Materialien verwenden die Du-Form (nicht Sie) |
| **Abkürzungen** | Beim ersten Auftreten ausschreiben, danach Kurzform. Level 1/2/3 (nie L1/L2/L3) |
| **Keine Zertifizierungsdruck-Aussagen** | Nie „für die Prüfung wichtig" o.ä. — inhaltliche Bedeutung betonen |
| **Optionsbuchstaben** | In Quiz-Erklärungen nie A/B/C/D referenzieren |
| **Quellenbelege** | Jede inhaltliche Aussage muss belegbar sein; keine konstruierten URLs |
| **Kursseparation** | Inhalte nie 1:1 zwischen KIB, KIM und MAT übertragen |
| **Nur Tier-1 in offiziellen Materialien** | In Hand-Outs und Gamma ausschließlich verifizierte Quellen |
| **Use Cases nicht im Hand-Out** | Use Cases werden im Hand-Out **nicht namentlich genannt** (keine Firmennamen, keine fallspezifischen Kennzahlen). Sie werden im Labor (Dozentendokument) und live durch den Dozenten eingeführt. Übungen im Hand-Out bleiben **use-case-neutral** formuliert (z. B. „das heute vorgestellte Unternehmen"). Vorteil: Hand-Out bleibt wiederverwendbar und kursübergreifend konfliktfrei. |

---

*Erstellt: 2026-06-22 · Ersetzt: Quellen_Workflow.md · Maintainer: Uli Nord · Dozenten-Assistent: Claude (Anthropic)*
