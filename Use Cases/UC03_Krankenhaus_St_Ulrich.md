# UC-03 Unternehmensakte — Krankenhaus St. Ulrich
> ⚠️ Fiktives Unternehmen — alle Namen und Details sind für Schulungszwecke erstellt

---

## Das Krankenhaus

**Krankenhaus St. Ulrich**, Nordrhein-Westfalen  
Krankenhaus St. Ulrich · 800 Betten · 2.200 Mitarbeitende  
Träger: Gemeinnützige GmbH (Gesellschafter: Stadt + Wohlfahrtsverband)

**Ausgangslage (Bezug zum Artikel):**
- Wartezeiten in der Notaufnahme haben sich seit 2020 verdoppelt
- Bettenauslastung dauerhaft über 90%
- Drei von vier Stationen melden Personalengpässe
- Verlust 2024: ca. 8 Mio. EUR — trotz gestiegener Fallzahlen

---

## Personen

**Dr. Claudia Mertens — Neue Geschäftsführerin**  
Seit 6 Monaten im Amt. Betriebswirtin mit Gesundheitsmanagement-Hintergrund. Unter Druck der Gesellschafter, die Verluste zu stoppen. Sieht KI als Werkzeug zur Effizienzsteigerung — nicht als Selbstzweck. Pragmatisch und entscheidungsfreudig, aber wenig Erfahrung mit Compliance-Fragen.

**Prof. Dr. Heinrich Sommer — Ärztlicher Direktor**  
Kardiologe, 30 Jahre Klinik-Erfahrung. Skeptisch gegenüber KI in der Diagnose ("Die Haftung liegt beim Arzt, nicht beim Algorithmus"). Unterstützt administrative Automatisierung, wenn sie ihm und seinen Kollegen Zeit spart.

**Birgit Klassen — Pflegedienstleiterin**  
Erfahrene Krankenpflegerin, seit 20 Jahren im Haus. Repräsentiert den größten Personalblock. Burnout im Team ist ihr Hauptthema. Offen für KI, wenn sie echte Entlastung bringt — misstrauisch gegenüber "Technik, die uns überwachen soll".

**Peter Miese — IT-Leiter**  
Zuständig für SAP, Krankenhausinformationssystem (KIS) und die neue EPA-Anbindung. Überlastet. Hat Bedenken zur Cybersicherheit — Krankenhäuser sind häufiges Angriffsziel. Kein Datenschutzbeauftragter im Haus (extern beauftragt).

**Sie — KI-Beauftragter:in (neue Stelle)**  
Direkt der Geschäftsführerin zugeordnet. Kein eigenes Budget. Beratende Funktion. Der Betriebsrat hat die Stelle mit gemischten Gefühlen zur Kenntnis genommen.

---

## Die vier laufenden KI-Initiativen

| Stufe | System | Status | Datenquelle |
|---|---|---|---|
| UC-03a | Optimierte Steuerung der Verbrauchsmaterialien (Verbände, Handschuhe, Spritzen usw.) | Pilot | ERP / Bestellhistorie |
| UC-03b | Patienten-Onboarding-App (Öffnungszeiten, Kantinenplan, FAQ, Chatfunktion usw.) | Pilot | Keine Patientendaten (nur FAQ) |
| UC-03c | Automatisierung administrativer Abläufe (Prüfung der KV-Schlüssel, Terminvorschläge, Entwürfe für Entlassbriefe | Test | interne Dokumente / KV-Webseiten / Kalender |
| UC-03d | Diagnoseunterstützung (Scanning von CRTs mittels einer in Indien gehosteten App  | Test | EPA + Bilddaten |

---

## Hintergrund: Der Doom Loop

Der Artikel "Hospitals are stuck in a deadly doom loop" (The Economist, April 2026) beschreibt das systemische Problem: Längere Wartezeiten → kränkere Patienten → längere Behandlungen → Kapazitätsengpässe → noch längere Wartezeiten. St. Ulrich ist ein typisches Beispiel.

**Relevanz für den KI-Beauftragten:** Die Daten, auf denen KI-Modelle trainiert werden, spiegeln eine durch den Doom Loop verzerrte Realität wider. Trainingsdaten aus 2020–2024 zeigen ein überlastetes System als "normal". Das ist ein strukturelles Bias-Risiko nach Art. 10 EU AI Act.

---

## Hintergrundstudie: KI-Chatbots im Gesundheitsbereich

Costa-Gomes et al. (*Nature Health*, April 2026) analysierten über 500.000 Gesundheitsanfragen an Microsoft Copilot. Für den KI-Beauftragten des St. Ulrich-Krankenhauses relevante Befunde:

- Fast jedes fünfte Gespräch betrifft persönliche Symptombewertung oder Erkrankungsmanagement
- Jede siebte Anfrage wird für eine andere Person gestellt (Kind, Elternteil, Partner) — KI als Pflegehilfe
- Abends und nachts steigen persönliche Gesundheitsanfragen deutlich an — genau wenn das Krankenhaus am schlechtesten erreichbar ist
- Mobil = persönliche Gesundheitsanliegen; Desktop = professionelle/akademische Arbeit
- LLMs bestehen medizinische Prüfungen, versagen aber in Triage-Situationen — starke Benchmark-Performance bedeutet keine reale Zuverlässigkeit

**Implikation für UC-03b:** Die App würde reale Nutzernachfrage bedienen. Aber: Die Nutzungssituation (nachtaktiv, Caregiver, vulnerabel) erhöht die Anforderungen an Genauigkeit und Sicherheit erheblich.

Quelle: https://www.nature.com/articles/s44360-026-00117-x

---

## Reale Vorbilder — Memorial Healthcare System

Die folgenden Fälle sind öffentlich dokumentierte Entsprechungen zu den Initiativen aus dem vorigen Abschnitt. Sie stammen aus **einem** realen Klinikunternehmen — Memorial Healthcare System, einem mittelgroßen Verbund in den USA mit mehreren Häusern. Sie dienen als Orientierung, nicht als Beweis dafür, dass dasselbe in St. Ulrich funktioniert.

| Initiative St. Ulrich | Entsprechung bei Memorial | Was dokumentiert ist | Belegstärke |
|---|---|---|---|
| **UC-03c** Verwaltungsautomatisierung (Entlassbriefe) | **Nuance DAX Copilot** — Dokumentation nebenher während der Visite | Reduzierte abendliche Nachdokumentation laut Aussage des Digitalchefs; **kein veröffentlichter Basiswert**, keine unabhängig geprüfte Produktivitätszahl | Führungsinterview, unquantifiziert |
| **UC-03d** Diagnoseunterstützung (Bildauswertung) | **Aidoc** (Zufallsbefunde) und **RapidAI** (Schlaganfall-Alarme auf Diensthandy und Smartwatch) | RapidAI-Pilot ab 2017, später vier Häuser; Mitteilung vom Mai 2022: über 8.400 Schlaganfälle identifiziert | Organisationsmitteilung, zeitlich veraltet |
| **UC-03b** Patienten-Onboarding-App | **Talkdesk** — Patientenkontakt; zuvor **12 getrennte Callcenter zu einem Patient Access Center konsolidiert**, dann automatisiert | Anbieter nennt niedrigere Abbruchquote und kürzere Bearbeitungszeit; **kein öffentlicher Basiswert, keine unabhängige Prüfung** | Anbieter-Kundenstory |
| *(bisher keine Entsprechung)* | **Artsight** — kamerabasierte virtuelle Pflege und Sturzrisiko-Beobachtung, ergänzend zum Klinikinformationssystem | Zentrale Leitstelle mit 31 Arbeitsplätzen, eröffnet Oktober 2024; Baukosten 1,7 Mio. USD, **projizierte** Einsparung im ersten Jahr 1,6 Mio. USD | Fachpresse, Projektion — nicht als realisiert bestätigt |
| *(bisher keine Entsprechung)* | **Atlas MAP** — Erkennung von Medikamenten-Hilfsprogrammen, Antragsautomatisierung | Anbieter nennt Fördersummen für eine begrenzte Patientenzahl in acht Monaten | Anbieter-Kundenstory |

### Die Vorgehenslogik — das eigentlich Übertragbare

Memorial beschrieb sich selbst als **„fast follower"**: keine Eigenentwicklung, sondern eingekaufte Spezialwerkzeuge, angebunden an das bestehende Klinikinformationssystem. Alle Fälle folgen derselben Reihenfolge — ein sichtbares betriebliches Problem benennen, eine etablierte Lösung kaufen, sie in den vorhandenen Arbeitsablauf integrieren, und **erst dann** fragen, ob das veröffentlichte Ergebnis sich vor Ort reproduzieren lässt.

Drei Muster sind für St. Ulrich unmittelbar verwertbar:

**Erstens: mit einem Ablauf beginnen, dessen Entlastung die Fachleute selbst wollen.** Memorial gewann Ärztinnen und Ärzte als Fürsprecher, statt die Einführung aus der IT anzuordnen. Das macht den ersten Piloten zum kollegialen Beweis — und deckt Fehler früher auf, weil angesehene Nutzende benennen können, ob das Problem an der Aufnahmequalität, der Platzierung im Arbeitsablauf oder der Dokumentationsrichtlinie liegt.

**Zweitens: fragmentierte Abläufe konsolidieren, bevor automatisiert wird.** Die 12 Callcenter wurden zuerst zusammengelegt — das schuf überhaupt erst eine messbare Warteschlange und eine gemeinsame Datenbasis. Erst danach kam die Automatisierung. Ein KI-System kann kein Betriebsmodell reparieren, das es nicht sehen kann.

**Drittens: Kosten erheben, bevor gekauft wird.** Vor der Anschaffung einer kamerabasierten Beobachtung wurden 90 Tage Sitzwachen-Stunden, Sturzereignisse je 1.000 Behandlungstage, Eskalationszeiten und der Aufwand der Datenschutzprüfung veranschlagt. Erst dann folgte ein Pilot mit einer Risikogruppe und einer Vergleichsstation.

**Dieser dritte Punkt schließt direkt an den Doom-Loop-Befund oben an:** Wenn Trainings- und Vergleichsdaten aus 2020–2024 ein überlastetes System als „normal" codieren, ist ein sauber erhobener Basiswert *vor* der Einführung nicht Bürokratie, sondern die einzige Absicherung gegen ein verzerrtes Erfolgsmaß.

### Der Konfliktfall für die Übung

Die kamerabasierte Sturzbeobachtung trifft den Widerstand von **Birgit Klassen** im Kern — sie ist ausdrücklich misstrauisch gegenüber „Technik, die uns überwachen soll". Genau dieser Fall zeigt, dass ihr Einwand nicht Technikfeindlichkeit ist, sondern ein Governance-Argument: Kameraüberwachung im Patientenzimmer erfordert eine Einwilligungs- und Aufbewahrungsregelung, und die zugehörige Prüfung ist eine eigene Budgetposition. Wer sie nicht einplant, hat nicht gespart, sondern verschoben.

### Der Governance-Befund — Kontinuität als Prüfstein

Memorial verzichtete **bewusst** auf eine eigene KI-Leitungsfunktion und band KI in bestehende IT- und Klinikgremien ein. Das ist vertretbar: Es vermeidet eine parallele Bürokratie und hält Entscheidungen nah an der klinischen Praxis.

Fragil wurde das Modell, als der langjährige Digitalchef im September 2025 das Haus verließ — ohne öffentlich benannte Nachfolge oder Stellvertretung. Ende Juni 2026 führte die Fachpresse Memorial noch unter den Häusern ohne dauerhafte IT-Leitung. Wichtig für die saubere Deutung: **Die öffentliche Aktenlage zeigt nicht, dass die Technik gestoppt hat.** Sie zeigt, wie schnell ein schlankes Governance-Modell zur Nachfolgefrage wird.

Der Prüfsatz daraus, übertragbar auf St. Ulrich: *Der Test eines KI-Programms ist nicht, ob sein Fürsprecher es erklären kann — sondern ob Ablauf, Belege und Verantwortung am Montag nach dessen Abgang noch tragen.*

Für jeden produktiven KI-Ablauf gehören deshalb fünf Angaben schriftlich vor: **welcher Ablauf** sich ändert (eine benannte Prozessänderung, keine allgemeine Fähigkeit) · **welcher Basiswert** verbessert werden muss (aus dem Quellsystem, mit festem Zeitraum) · **wer primär verantwortet** (benannt, mit Befugnis und Zeit) · **wer stellvertritt** (kann morgen übernehmen und der Leitung berichten) · **welcher Beleg** das Ziel stützt (mit Belegstärke und Reproduktionsplan). Jede Leerstelle ist kein Verwaltungsdetail, sondern das nächste zu behebende Risiko.

### Quellenkritischer Hinweis — wichtig für die Bewertung

**Für keines der Memorial-Ergebnisse existiert ein unabhängig geprüfter Nachweis.** Das stellt die zugrunde liegende Fallstudie selbst fest. Die Belege verteilen sich auf drei ungleiche Kategorien, die nicht zu einer ROI-Schlagzeile verschmolzen werden dürfen:

- **Organisationsmitteilungen und Führungsinterviews** — mit Datum und Geltungsbereich verwendbar
- **Anbieter-Kundenstories** — als Hypothese verwendbar, danach zwingend lokal reproduzieren
- **Projektionen** — die 1,6 Mio. USD Einsparung ist eine Vorausschau, kein Ergebnis

Eine vierte Kategorie ist ausdrücklich **unbrauchbar**: Zu Memorial kursiert im Netz eine Angabe von 43 Prozent weniger Personalaufwand und 28 Prozent höherer Patientenzufriedenheit durch einen KI-Sprachassistenten. Die Spur endet auf einer Werbeseite ohne Primärquelle, ohne Methode, ohne Basiswert und ohne erkennbaren Bezug zu Memorial. Solche Zahlen gehören nicht in ein Finanzmodell — sie können ein Pilotprojekt genehmigt bekommen und gleichzeitig die Glaubwürdigkeit aller belastbaren Ergebnisse im selben Portfolio beschädigen.

**Und die Grenze der Übertragbarkeit:** Memorial arbeitet im US-Gesundheitssystem — anderes Abrechnungswesen, philanthropische Medikamentenhilfe, kein Betriebsrat, keine DSGVO, kein EU AI Act. Die Vorgehenslogik überträgt sich auf St. Ulrich, die Zahlen nicht.

**Quelle:** Kamil Banc / AI Adopters Club — „Inside Memorial Healthcare System's AI Adoption", Report AIAC-CSR-2026-016, Rev. 14. August 2026. Die Fallstudie stützt sich auf Fachpresse (Chief Healthcare Executive 27.08.2024, HFM Magazine 09.04.2025, Becker's Hospital Review 15.09.2025 und 29.06.2026), Pressemitteilungen von Memorial (28.10.2024, 12.05.2022) sowie herstellerpublizierte Kundenstories. Einzelautor, kein Peer Review, kein eigenes Interview mit Memorial. Registereintrag: Neue_Quellen_Intake #65.

---

## Verwendung in der Schulung

| Kontext | Verwendung |
|---|---|
| UC-03a bis e (Teilnehmer-Dateien) | Szenario-Grundlage für alle fünf Stufen |
| Tag 9 (SWOT + Risikomanagement) | Diagnosesystem als Hauptszenario |
| Abschluss-Steckbrief | UC-03c + UC-03d kombiniert |
| Woche 4 (Change Management) | Ärzteteam-Widerstand als Übungsfall; Kamerabeobachtung als Konfliktfall mit der Pflegedienstleitung |
| Business Case / Belegbewertung | Reale Vorbilder oben — Übung: Welche der Memorial-Zahlen dürfen in eine Investitionsvorlage, welche nicht? |

---
*Letzte Aktualisierung: August 2026 — Ulrich Nord / Claude (Anthropic)*
