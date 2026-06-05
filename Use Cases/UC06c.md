# UC-06c: AIktiv-Invest (AI) GmbH — KI-gestütztes Portfoliomonitoring

---

## Szenario

Du bist Portfoliomanager:in der **AIktiv-Invest (AI) GmbH**. Das KI-Screening-System für neue Proposals läuft seit sechs Monaten erfolgreich. Jetzt steht das nächste Problem: das **laufende Monitoring** der sechs Portfoliounternehmen.

Julia Romberg (CFO) hat ein klares Bild davon, was sie braucht: *„Ich will bei jedem Quartalsbericht sofort sehen, welche Beteiligungen Alarm schlagen — ohne drei Tage händische Pivot-Tabellen."*

Aktuell liefern alle sechs Portfoliounternehmen monatliche KPI-Reports — in unterschiedlichen Formaten (PDF, Excel, Google Sheets). Die Konsolidierung dauert 2–3 Tage vor jedem Quartalsmeeting. Abweichungen vom Plan fallen oft erst im Nachhinein auf.

---

## Die Portfoliounternehmen (vereinfacht)

| Unternehmen | Segment | ARR (aktuell) | Wachstum YoY | EBITDA-Marge | Rule of 40 |
|---|---|---|---|---|---|
| **FlowML** | KI-Prozessautomatisierung | 1,2 Mio. € | +55 % | −12 % | **43 %** ✅ |
| **DataBridge** | Datenmigrations-KI | 800 T € | +22 % | +8 % | **30 %** ⚠️ |
| **ClearScan** | Dokumenten-KI (Health) | 2,1 Mio. € | +18 % | +14 % | **32 %** ⚠️ |
| **NexusChat** | Enterprise-LLM | 400 T € | +95 % | −45 % | **50 %** ✅ |
| **TrustLayer** | KI-Compliance | 600 T € | +10 % | +5 % | **15 %** 🔴 |
| **VizLogic** | KI-Visualisierung | 1,8 Mio. € | +35 % | +18 % | **53 %** ✅ |

*ARR = Annual Recurring Revenue · Rule of 40 = Wachstum % + EBITDA-Marge %*

---

## Aufgabe / Diskussionsfragen

### Aufgabe 1 — Rule of 40 verstehen und anwenden

Berechne die **Rule of 40** für jedes Portfoliounternehmen und interpretiere die Ergebnisse:
- Was bedeutet ein Wert unter 40 % in einem Frühphasen-Unternehmen?
- Welche zwei Portfoliounternehmen erfordern sofortige Aufmerksamkeit — und warum?
- Ist die Rule of 40 immer die richtige Metrik? Für welche Unternehmenstypen oder -phasen hat sie Schwächen?

---

### Aufgabe 2 — KPI-Monitoring-System konzipieren

Julia Romberg will ein KI-gestütztes Dashboard, das:
1. Monatliche KPI-Reports der Portfoliounternehmen **automatisch konsolidiert** (unabhängig vom Eingabeformat)
2. Plan-Ist-Abweichungen **visuell hervorhebt** (Ampel-Logik)
3. **Frühwarnsignale** ausgibt, wenn ein Unternehmen 2+ aufeinanderfolgende Monate negativ abweicht
4. Das **Quartalssreporting für LPs** (private Anleger) vorbereitet

Konzipiere dieses System:
- Welche KPIs sollen überwacht werden? (Mindestens 6, begründet)
- Wie funktioniert die Datenerfassung? (Format, Frequenz, Qualitätssicherung)
- Wie sieht das Dashboard aus? (Skizze oder Beschreibung der wichtigsten Ansichten)
- Welche KI-Funktionen sind sinnvoll — und welche sind Overkill?

---

### Aufgabe 3 — Interpretationsaufgabe

TrustLayer (Rule of 40: 15 %) und DataBridge (Rule of 40: 30 %) liegen unter der 40-%-Schwelle.

Entwickle für **einen dieser beiden Fälle** eine Analyse-Storyline:
- Warum liegt der Wert unter 40 %?
- Ist das ein strukturelles Problem oder eine Wachstumsphase?
- Welche drei Fragen würdest Du im nächsten Board-Meeting stellen?
- Welche KI-Tools könnten Dir bei der Vorbereitung dieses Gesprächs helfen?

---

### Aufgabe 4 — Grenzen der Metrik (Diskussionsaufgabe)

Die Rule of 40 ist eine verbreitete Heuristik in der SaaS- und VC-Welt. Aber sie hat blinde Flecken.

Diskutiert in der Gruppe:
- In welchen Situationen wäre ein Unternehmen mit Rule-of-40-Wert von 15 % trotzdem ein gutes Investment?
- Welche zusätzlichen Metriken würdet ihr in ein robustes KI-Monitoring einbauen?

---

## Weiterführende Quellen

Die **Rule of 40** wurde popularisiert durch Brad Feld (Foundry Group) und ist heute ein Standard-KPI in der SaaS-Investmentwelt.

**Formel:** Rule of 40 = Wachstumsrate (% YoY) + EBITDA-Marge (%)

**Interpretation:**
- **≥ 40 %:** Gesundes Wachstums-Profitabilitäts-Gleichgewicht
- **30–40 %:** Grenzbereich — beobachten
- **< 30 %:** Alarm — entweder zu langsam wachsend oder zu unprofitabel (oder beides)

**Wichtig:** Die Metrik ist für **SaaS/Subscription-Modelle** konzipiert. Sie funktioniert weniger gut für Hardware-Unternehmen, Marktplätze mit netto-negativer Unit Economics oder sehr frühphasige Pre-Revenue-Startups.

Quelle: [Techcrunch — The Rule of 40 for SaaS Companies](https://techcrunch.com/2015/02/01/the-rule-of-40-for-saas-companies/) · [Brad Feld — Rule of 40](https://feld.com/archives/2015/02/rule-40-healthy-saas-company.html)

---

## Analyse & Hinweise

### Einordnung

**Kurs:** KI-Manager angewandte Transformation
**KI-System-Typ:** KI-gestütztes Dashboard / Monitoring-System (Datenkonsolidierung + Anomalie-Erkennung)
**Schwierigkeitsgrad:** Mittel–Fortgeschritten
**Didaktische Funktion:** Anwendung von KPI-Frameworks in einem Investment-Kontext; kritisches Denken über Metriken; KI als Monitoring-Werkzeug (nicht als Entscheidungsersatz)

### Musterlösung — Aufgabe 1: Rule of 40

| Unternehmen | Wachstum | EBITDA-Marge | Rule of 40 | Status |
|---|---|---|---|---|
| FlowML | +55 % | −12 % | **43 %** | ✅ Gesund — wächst stark, akzeptables Defizit |
| DataBridge | +22 % | +8 % | **30 %** | ⚠️ Grenzbereich — wächst zu langsam für Defizit-Trade-off |
| ClearScan | +18 % | +14 % | **32 %** | ⚠️ Grenzbereich — profitabel, aber Wachstum flacht ab |
| NexusChat | +95 % | −45 % | **50 %** | ✅ Stark — Hyperwachstum rechtfertigt Verluste temporär |
| TrustLayer | +10 % | +5 % | **15 %** | 🔴 Alarm — weder Wachstum noch Profitabilität |
| VizLogic | +35 % | +18 % | **53 %** | ✅ Stark — ausgewogenes Profil |

**Sofortige Aufmerksamkeit:**
- **TrustLayer (15 %):** Weder Wachstum noch Marge. Klassisches "stuck in the middle"-Problem.
- **DataBridge (30 %):** 22 % Wachstum für Early-Stage-SaaS ist zu niedrig — Erwartung wäre 40–60 %+.

### Musterlösung — Aufgabe 2: KPI-Monitoring-System

**Empfohlene KPIs:**

| KPI | Warum wichtig | Frühwarn-Schwelle |
|---|---|---|
| ARR (Annual Recurring Revenue) | Kernmetrik Subscriptionwachstum | < 15 % YoY-Wachstum |
| MRR-Wachstum MoM | Kurzfristige Wachstumsdynamik | 2× aufeinanderfolgende Rückgänge |
| Churn Rate | Kundenbindung / Produktqualität | > 5 % jährlich |
| Burn Rate / Runway | Liquiditätssicherung | Runway < 12 Monate |
| CAC Payback Period | Vertriebseffizienz | > 18 Monate |
| Gross Margin | Skalierbarkeit des Geschäftsmodells | < 60 % |
| Rule of 40 | Wachstums-Profitabilitäts-Balance | < 30 % für 2+ Quartale |
| Headcount-Wachstum vs. ARR | Effizienz der Skalierung | Headcount wächst schneller als ARR |

**Systemarchitektur:**
```
Portfoliounternehmen (6×) liefern monatlich KPI-Reports
 → Verschiedene Formate: PDF, Excel, Google Sheets, Notion
        │
        ▼
KI-Konsolidierungsschicht
 • Document-Parsing (LLM-gestützt oder Template-basiert)
 • Mapping auf einheitliches KPI-Schema
 • Anomalie-Erkennung (statistische Abweichung von Plan/Trend)
        │
        ▼
Dashboard (z. B. Power BI, Metabase oder benutzerdefiniert)
 • Ampel-Ansicht: alle Portfoliounternehmen im Überblick
 • Drill-down: KPI-Verlauf je Unternehmen
 • Frühwarnreport: automatische E-Mail bei Schwellenwert-Verletzung
        │
        ▼
LP-Reporting-Assistent
 • Quartalsreport-Drafting auf Basis konsolidierter Daten
 • Julia Romberg reviewt und finalisiert — Human-in-the-Loop
```

**Was KI sinnvoll macht:** Automatisches Parsen unterschiedlicher Report-Formate · Trendanalyse und Anomalie-Erkennung · Erstentwurf LP-Report

**Was Overkill ist:** KI-gestützte Investitionsentscheidungen (KAGB-Konformität!) · Predictive Analytics für Exit-Timing · Automatisches Gründer-Scoring im laufenden Monitoring

### Musterlösung — Aufgabe 3: TrustLayer-Analyse

**Mögliche Storylines:**
1. **Marktproblem:** Compliance-KI ist erklärungsbedürftig — lange Sales-Cycles, zögerliche Kaufentscheidung in regulierten Unternehmen.
2. **Go-to-Market-Problem:** Falscher ICP, zu breiter Ansatz, kein klarer Land-and-Expand-Mechanismus.
3. **Produktproblem:** Zu wenig Differenzierung — Wettbewerber könnten ähnliche Lösungen schneller skalieren.

**Drei Board-Fragen:**
1. *„Welches sind Ihre drei größten Kunden — und warum haben Sie gewählt, nicht zu churnen?"*
2. *„Wo liegt Ihr größter Engpass im Sales-Funnel?"*
3. *„Was müsste passieren, damit Sie in 12 Monaten 40 % Wachstum schaffen?"*

**KI-Tools für Vorbereitung:** Marktrecherche (Perplexity/ChatGPT) · Nachrichten-Monitoring (Google Alerts + KI-Zusammenfassung) · Gesprächsvorbereitung (strukturiertes Prompting für Board-Questions)

### Didaktische Hinweise

**Das Hauptlernziel:** Der neue Lerninhalt ist die **KI-gestützte Operationalisierung**: Wie automatisiere ich das Monitoring, ohne die Interpretationskompetenz aus der Hand zu geben?

**Kritische Diskussion ist erwünscht:** NexusChat hat −45 % EBITDA-Marge — das klingt alarmierend. Aber bei 95 % Wachstum und nachweislich skalierbarem Geschäftsmodell ist das normal (vgl. Salesforce-Wachstumsjahre).

**Julia Romberg als Anker:** Die CFO-Rolle ist der Realitätscheck. Sie will Zeitersparnis beim Reporting und frühzeitige Warnsignale — kein autonomes Entscheidungssystem.

**KAGB-Hinweis:** Anlageentscheidungen müssen dokumentiert und von qualifizierten Personen getroffen werden. Das System darf Informationen aufbereiten und Alarme setzen — nicht entscheiden.

### Verbindungen im Curriculum

| Kurs / Thema | Verbindung |
|---|---|
| KI-Manager Tag 5 (UC-06b) | Dieselbe Fallstudie — UC-06c zeigt die nächste Ausbaustufe nach dem Investment |
| KI-Manager angewandte Transformation allgemein | UC-06c ist ein paradigmatisches Beispiel für "KI als Monitoring-Werkzeug" im Transformationskontext |
| Datenstrategie & Datenqualität | Die Hauptherausforderung des Monitoring-Systems ist nicht die KI, sondern die Datenqualität der Reports |
| ISO 42001 Monitoring & Continuous Improvement | Kontinuierliches Monitoring von KI-Systemen und Portfoliounternehmen folgt ähnlicher Logik: Abweichung erkennen, eingreifen, dokumentieren |
