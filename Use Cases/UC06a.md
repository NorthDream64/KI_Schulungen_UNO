# UC-06a: AIktiv-Invest (AI) GmbH — Go/No-Go-Screening

---

## Szenario

Du bist Portfoliomanager:in der **AIktiv-Invest (AI) GmbH**, einem Hamburger Venture-Capital-Fonds mit Fokus auf KI-Investitionen. Das Fondvolumen liegt heute bei 15 Mio. EUR, soll aber nach den Wünschen der Geschäftsführerin in den nächsten vier Jahren auf 100 Mio. EUR wachsen.

Monatlich landen **15–20 Investitionsvorschläge** auf Deinem Schreibtisch — von Gründerteams, Co-Investoren und Deal-Sourcing-Plattformen. Jeder dieser Proposals muss zunächst in einer **Go/No-Go-Entscheidung (Phase 1)** vorqualifiziert werden, bevor aufwendige Detailanalysen starten.

**Das heutige Problem:** Die Grobprüfung eines Proposals dauert durchschnittlich 2–3 Stunden — Recherche zu Markt, Wettbewerbern, Technologie-Reifegrad und Gründer-Background. Bei 17 Proposals pro Monat bindet das mehr als 40 Analysten-Stunden allein für die Vorauswahl. Das sind Kapazitäten, die für tiefere Analysen fehlen.

Dr. Vogt (Geschäftsführerin) hat Dich gebeten, ein KI-gestütztes Screening-System zu konzipieren, das die Phase-1-Bearbeitung deutlich beschleunigt — ohne die Entscheidungsqualität zu verschlechtern — und gleichzeitig den wirtschaftlichen Nutzen dieser Investition als ROI-Berechnung zu belegen.

---

## Aufgabe / Diskussionsfragen

Entwickle ein **Konzept für ein KI-gestütztes Go/No-Go-Screening**, das folgende Anforderungen erfüllt:

**① Bewertungsrahmen definieren**
Welche Kriterien soll das KI-System prüfen? Definiere 5–8 Kriterien, die für eine erste Einschätzung eines KI-Investitionsvorhabens relevant sind — z. B.:
- Strategischer Fit mit Fondsstrategie (Technologie, Markt, Ticket-Größe)
- Marktgröße (TAM/SAM) und Wachstumspotenzial
- Wettbewerbssituation (differenzierte Positionierung?)
- Team-Background (Gründertrack-Record, technische Kompetenz)
- Red Flags (regulatorische Risiken, fehlende IP, Marktreife-Fragen)

**② Informationsquellen festlegen**
Welche Quellen soll das System automatisiert recherchieren oder auswerten? (z. B. Crunchbase, LinkedIn, Pitchbook, Nachrichtenartikel, Patentdatenbanken, eigene Datenbank bisheriger Proposals)

**③ Ausgabeformat definieren**
Was soll das System als Ergebnis liefern? Definiere ein strukturiertes Ausgabeformat, das Dir als Analyst:in hilft, in 15–20 Minuten eine fundierte Go/No-Go-Entscheidung zu treffen.

**④ Human-in-the-Loop sicherstellen**
Wie stellst Du sicher, dass das System als Entscheidungsunterstützung — nicht als Entscheidungsersatz — fungiert? Welche Rolle verbleibt beim Analysten?

**⑤ Risiken benennen**
Was könnte bei einem KI-gestützten Screening schief gehen? Benenne mindestens zwei konkrete Risiken und wie Du ihnen begegnest.

**⑥ ROI berechnen**
Berechne den **Return on Investment (ROI)** für die Einführung des KI-gestützten Screening-Systems bei der AIktiv-Invest (AI) GmbH. Nutze dafür das **ROI-Template (Excel)** oder den **interaktiven ROI-Rechner (HTML)** als Werkzeug. Die detaillierte Rechnung findest Du in den Schritten 1–6 am Ende dieses Dokuments.

---

## Rahmenbedingungen

- Vorhandene Systeme: Notion, Airtable, Crunchbase Pro, PitchBook (Light), M365
- Teamgröße: 1 Senior Analyst (Ben Fischer) mit Python/Data-Engineering-Hintergrund
- Budget für die Konzeptphase: nicht definiert — Dein Konzept soll u. a. den Investitionsrahmen für Phase 2 begründen
- Regulatorischer Hinweis: KAGB-Konformität und DSGVO-Konformität sind Mindestanforderungen; KI-Entscheidungen über natürliche Personen (Gründer-Scoring) können Art. 22 DSGVO berühren

---

## Ergebnis

Präsentiere Dein Konzept in einem strukturierten Dokument oder einer Kurzpräsentation (4–6 Folien oder 3–4 Seiten). Adressat ist Dr. Vogt im wöchentlichen Team-Meeting — sie hat 20 Minuten für Deine Präsentation eingeplant.

Das Dokument soll u. a. beantworten:
- Wie sieht das Screening-System aus? (Architektur, Quellen, Ausgabe)
- Was ist die erwartete Zeitersparnis — und was ist der ROI der Investition?
- Welche Risiken gibt es — und wie geht das System damit um?
- Was brauchen wir als nächsten Schritt (Phase 2)?

---

## Teil B — ROI-Berechnung

*Die folgenden Schritte liefern das Zahlenfundament für Aufgabe ⑥ und den Business-Case-Baustein "Kosten & Nutzen" in Aufgabe ⑥.*

### Schritt 1 — IST-Prozesskosten ermitteln

Berechne die jährlichen Personalkosten des heutigen manuellen Screening- und Bewertungsprozesses:

| Parameter | Wert |
|---|---|
| Vorgänge / Monat | Ø 17 (15–20) |
| Grobprüfung (Phase 1) je Vorgang | 3,0 h |
| Anteil mit Detailprüfung (Phase 2) | 50 % |
| Detailprüfung je Vorgang | 12,0 h |
| Vollkosten Analyst:in | 120 €/h |

Berechne: Gesamt-Analyststunden IST pro Jahr → Jährl. Prozesskosten IST.

---

### Schritt 2 — SOLL-Prozesskosten mit KI-Unterstützung

Schätze die Zeitersparnis durch ein KI-Bewertungssystem — basierend auf Benchmarks für NLP-Screening-Systeme:

| Effizienzgewinn | Annahme |
|---|---|
| Zeitersparnis Grobprüfung (Phase 1) | 70 % |
| Zeitersparnis Detailprüfung (Phase 2) | 50 % |

Berechne: Gesamt-Analyststunden SOLL → Jährl. Prozesskosten SOLL → **Jährl. Einsparung**.

---

### Schritt 3 — Investitionskosten schätzen

Schätze die Kosten für Aufbau und Betrieb des Systems:

| Kostenart | Betrag |
|---|---|
| Entwicklung & Implementierung | 55.000 € |
| Datenvorbereitung & Integration (Crunchbase-API, interne DB) | 15.000 € |
| Schulung & Change Management | 5.000 € |
| **Einmalige Investition gesamt** | **75.000 €** |
| Cloud-Infrastruktur / Jahr | 8.000 € |
| Updates, Re-Training & Fine-Tuning / Jahr | 7.000 € |
| **Jährl. Betriebskosten** | **15.000 €** |

---

### Schritt 4 — ROI-Kennzahlen berechnen

Berechne die drei Kernindikatoren für eine Management-Entscheidung:

1. **Payback Period** (Amortisationsdauer in Monaten)
2. **Break-even-Punkt** (erster Monat mit positivem kumulierten Cashflow)
3. **ROI über 3 Jahre** (Return on Investment in %)

Erstelle eine **5-Jahres-Timeline** mit kumuliertem Cashflow.

---

### Schritt 5 — Sensitivitätsanalyse (Erweiterungsaufgabe)

Teste die Robustheit Deiner Empfehlung mit mindestens zwei Alternativszenarien:

- **Weniger Volumen:** Was passiert, wenn die AI GmbH nur 10 statt 17 Proposals/Monat erhält?
- **Schlechtere Effizienz:** Was passiert, wenn die KI nur 50 %/35 % statt 70 %/50 % Effizienzgewinn bringt?

Ab welchem Minimalvolumen oder welcher Mindeffizienz ist das Projekt noch wirtschaftlich?

---

### Schritt 6 — Business Case formulieren

Formuliere eine Management-Empfehlung für Dr. Vogt mit den **7 Business-Case-Bausteinen**:

1. Problem / Ausgangslage (Was kostet die heutige Situation?)
2. Lösungsansatz (Was soll das KI-System tun?)
3. Kosten (TCO über 3 Jahre)
4. Harter Nutzen (messbar, belegbar)
5. Weicher Nutzen (real, aber nicht eingerechnet)
6. Opportunitätskosten (Was passiert, wenn wir es nicht tun?)
7. Empfehlung (Go / No-Go mit Bedingungen)

---

## Ergebnisdokumentation

Trage Deine Ergebnisse in das **ROI-Template** ein (Dateiname: `ROI_UC06_AIktivInvest_v1.xlsx`) und halte die Eckdaten im **Steckbrief §4** fest.

Ziel: Du kannst Dr. Vogt in einem 10-Minuten-Gespräch sagen, ob das Projekt wirtschaftlich ist — und warum.

---

## Analyse & Hinweise

### Einordnung

**Kurs:** KI-Manager — Woche 1, Tag 3 (Use-Case-Identifikation & Priorisierung)
**KI-System-Typ:** NLP-gestütztes Screening-System (Dokumentenanalyse + strukturierte Recherche)
**Schwierigkeitsgrad:** Mittel
**Didaktische Funktion:** Use-Case-Canvas und Impact/Effort-Einordnung im Kontext eines realen Investment-Workflows — zeigt, warum Strukturierung vor Automatisierung kommt

### Musterlösung — Screening-Konzept (Kurzform)

**Was ein gutes Konzept enthält — Bewertungsrahmen (5–8 Kriterien):**

| Kriterium | Automatisierbar? | Begründung |
|---|---|---|
| Marktgröße (TAM/SAM) | ✅ Gut | Crunchbase, Gartner-Reports, Statista — strukturierte Daten |
| Wettbewerbssituation | ✅ Gut | Crunchbase-Wettbewerber, G2/Capterra-Kategorien |
| Team-Background | ⚠️ Teilweise | LinkedIn-Profil analysierbar, aber Qualitätsurteil bleibt beim Menschen |
| Strategischer Fit | ⚠️ Schwer | Erfordert Interpretationsleistung — eher Checklisten-Support |
| Red Flags (regulatorisch) | ✅ Regelbasiert | Stichwort-basierte Prüfung in Presseartikeln, Sanktionslisten |
| IP / Technologie-Differenzierung | ⚠️ Schwer | Patentdatenbanken ja, aber Qualitätsurteil komplex |

**Schwacher Kandidat für Automatisierung:** Bewertung des Gründer-Chemie-Faktors, kultureller Fit.

**Systemarchitektur:**
```
Proposal (PDF/E-Mail) → Parsing → Daten-Extraktion
        │
        ├── Crunchbase API (Marktdaten, Funding-Historie, Wettbewerber)
        ├── LinkedIn (Gründer-Background — manuell oder über API)
        ├── News-Aggregator (Red-Flag-Prüfung: Stichwortsuche)
        └── Interne DB (ähnliche Proposals aus der Vergangenheit)
        │
        ▼
Strukturiertes Screening-Profil (1 Seite)
 • Kriterien-Scorecard (grün/gelb/rot)
 • Key Facts (Markt, Team, Finanzierung)
 • Red-Flag-Hinweise (automatisch)
 • Empfehlung: Go / Prüfen / No-Go (nicht bindend)
        │
        ▼
Analyst entscheidet in 15–20 Min → Go/No-Go
```

**Musterlösung ROI:**
- IST: 1.836 h/Jahr → 220.320 €/Jahr
- SOLL: 795,6 h/Jahr → 95.472 €/Jahr
- Jährl. Einsparung: **124.848 €/Jahr** (1.040,4 h = 0,59 FTE)
- Payback Period: **8,2 Monate** · Break-even: **Monat 9** · ROI (3 Jahre): **212 %**

### Didaktische Hinweise

**Das Hauptlernziel:** Ein KI-gestütztes Screening-System ist in erster Linie ein **Strukturierungsinstrument** — nicht ein Entscheidungsautomaten. Der Wert liegt in der konsistenten Anwendung eines Frameworks, nicht in der KI-Magie.

**Typischer Fehler:** Teilnehmende wollen "die KI entscheiden lassen". Korrektur: *"Was entscheidet die KI? Sie aggregiert öffentliche Informationen nach einem definierten Kriterienset — das ist kein qualitativer Erkenntnisgewinn, sondern Zeitersparnis und Konsistenz."*

**Ben Fischer als Hebel:** Senior Analyst Ben Fischer hat Python-Kompetenz. Ein realistisches Minimal-System könnte ein Python-Skript sein, das per Crunchbase-API Basisdaten zieht und ein standardisiertes Profil erzeugt — kein LLM-Training erforderlich.

**DSGVO-Falle:** Gründer-Scoring berührt möglicherweise Art. 22 DSGVO. Das System liefert Informationen, nicht Entscheidungen.

**DCF-Frage:** Bei internen Effizienzprojekten mit kurzer Amortisation und hoher Unsicherheit in den Eingangsdaten schafft DCF Scheingenauigkeit. Der ROI reicht für Go/No-Go auf dieser Entscheidungsebene.

**Robustheit der Empfehlung:** Selbst im Worst Case (50 %/35 % Effizienz) liegt der ROI bei 120 % über 3 Jahre — und selbst bei halbiertem Volumen (10/Monat) noch bei 84 %. Alle Szenarien sind Go.

### Verbindungen im Curriculum

| UC | Thema | Verbindung |
|---|---|---|
| UC-06a Teil B | ROI-Berechnung (in diesem UC integriert) | Die vollständige ROI-Rechnung (Schritt 1–6) ist Bestandteil dieses Use Cases — Tag 5 |
| UC-06b | KI-Modelle verstehen & bewerten | Woche 2, Tag 6 — nutzt Portfoliounternehmen der AI GmbH als Analysebeispiele |
| UC-04a (SolidFinanz) | Schatten-KI-Inventur | Ähnliche Architektur-Frage: Was macht das System, welche Daten fließen wohin? |
| UC-06c | Portfoliomonitoring | Phase 3 nutzt ähnliche Dateninfrastruktur (strukturierte KPIs), aber für bestehende Investments |
