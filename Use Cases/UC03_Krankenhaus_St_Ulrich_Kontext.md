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

**Markus Brandt — IT-Leiter**  
Zuständig für SAP, Krankenhausinformationssystem (KIS) und die neue EPA-Anbindung. Überlastet. Hat Bedenken zur Cybersicherheit — Krankenhäuser sind häufiges Angriffsziel. Kein Datenschutzbeauftragter im Haus (extern beauftragt).

**Sie — KI-Beauftragter:in (neue Stelle)**  
Direkt der Geschäftsführerin zugeordnet. Kein eigenes Budget. Beratende Funktion. Der Betriebsrat hat die Stelle mit gemischten Gefühlen zur Kenntnis genommen.

---

## Die fünf KI-Initiativen

| Stufe | System | Risikoniveau | Datenquelle |
|---|---|---|---|
| UC-03a | Verbrauchsmaterialien | Minimal | ERP / Bestellhistorie |
| UC-03b | Patienten-Onboarding-App | Begrenzt → Grenzfall | Keine Patientendaten (nur FAQ) |
| UC-03c | Administrative Automatisierung | Mittel bis hoch | EPA |
| UC-03d | Diagnoseunterstützung | Hochrisiko | EPA + Bilddaten |
| UC-03e | Externe Kooperationen | Hoch bis sehr hoch | EPA (anonymisiert?) |

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

## Verwendung in der Schulung

| Kontext | Verwendung |
|---|---|
| UC-03a bis e (Teilnehmer-Dateien) | Szenario-Grundlage für alle fünf Stufen |
| Tag 9 (SWOT + Risikomanagement) | Diagnosesystem als Hauptszenario |
| Abschluss-Steckbrief | UC-03c + UC-03d kombiniert |
| Woche 4 (Change Management) | Ärzteteam-Widerstand als Übungsfall |

---
*Letzte Aktualisierung: April 2026 — Ulrich Nord / Claude (Anthropic)*
