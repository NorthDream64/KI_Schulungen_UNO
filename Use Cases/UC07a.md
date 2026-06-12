# UC-07a: Arventis GmbH — Build vs. Buy: KI-Strategie für die SaaS-Plattform

---

## Szenario

Du bist KI-Manager:in bei der **Arventis GmbH**, einem mittelständischen HR-Dienstleister mit 920 Mitarbeitenden und drei zentralen SaaS-Plattformen: Salesforce (CRM), ServiceNow (ITSM), Workday (HCM + Finance). Die jährlichen Lizenzkosten für diese drei Systeme betragen rund **€910.000**.

Im Mai 2026 landen binnen weniger Wochen drei KI-Upgrade-Angebote der bestehenden Anbieter auf dem Schreibtisch des CFO Michael Kunz: Salesforce Agentforce für €75/Seat/Monat Aufpreis, ServiceNow Now Assist für +30 % auf die Basislizenz, Workday Extend noch ohne fixen Preis. Auf der anderen Seite liest er in der Tagespresse, dass Klarna und Duolingo Standardsoftware durch KI ersetzen — und dass die US-Kanzlei Kirkland & Ellis $500 Mio. in die KI-Plattform Harvey investiert, um Arbeit intern zu erledigen, die früher an externe Dienstleister ging.

Kunz hat dich beauftragt, bis zum Quartalsmeeting (September 2026) eine belastbare Entscheidungsgrundlage zu liefern. Seine Frage lautet: *„Was sollen wir tun — upgraden, wechseln oder selbst bauen?"*

---

## Aufgabe / Diskussionsfragen

Du hast drei strategische Optionen zu bewerten:

**Option A — Incumbent-Upgrade**  
Bestehende Anbieter behalten, KI-Add-ons zukaufen: Agentforce (Salesforce), Now Assist (ServiceNow), Workday Extend.

**Option B — KI-native Alternativen**  
Einen oder mehrere Anbieter durch KI-native Vertikalanbieter ersetzen. Beispiele aus dem Markt: Sierra (Customer Service, mitgegründet von Bret Taylor, früher Salesforce Co-CEO und OpenAI-Chairman), Serval (IT Service Management, Ziel $1 Mrd. Bewertung), Rippling oder Bamboo-KI-Layer als HR-Alternative.

**Option C — In-house / Foundation-Model-Direktanbindung**  
Eigene KI-Agenten auf Basis von OpenAI- oder Anthropic-APIs entwickeln; Salesforce/ServiceNow/Workday werden auf reine Datenhaltung reduziert. Analog zum Harvey-Modell, aber ohne die Skaleneffekte einer Großkanzlei.

---

### ① Marktstruktur verstehen

Beschreibe das Bedrohungsszenario für die SaaS-Incumbents mit dem „SaaSquatch"-Rahmen aus der Economist-Analyse:

| Bedrohung | Wer | Mechanismus |
|---|---|---|
| Horizontale KI-Labs | OpenAI, Google, Anthropic | Einbettung direkt in Arbeitsprozesse — ohne SaaS-Schicht |
| KI-native Vertikals | Sierra (CRM/CS), Serval (ITSM) | Speziallösungen mit KI-first-Architektur, keine Migration-Last |
| DIY In-house | Kirkland & Ellis, Klarna | Eigenbau auf Foundation-Models; „AI agents don't need seats" |
| Selbst-Kannibalisierung | Salesforce Agentforce, ServiceNow Now Assist | Reaktive KI-Add-ons validieren gleichzeitig das Disruptions-Risiko |

*Frage: In welchem dieser vier Muster bewegt sich Arventis heute — und wohin sollte sich das Unternehmen bewegen?*

---

### ② Optionenvergleich strukturieren

Bewerte die drei Optionen anhand der folgenden Dimensionen (Ergebnis: strukturierter Entscheidungsrahmen für den CFO):

| Dimension | Option A (Incumbent-Upgrade) | Option B (KI-native Alt.) | Option C (In-house) |
|---|---|---|---|
| **Kostenstruktur (3 Jahre)** | Berechne: €910K Basis + Agentforce/Now Assist/Workday Extend Aufpreise | Schätze: Migrationsprojekt + neue Lizenzen | Schätze: Entwicklungskosten + laufende API-Kosten |
| **Datenschutz / DSGVO** | AVV-Erweiterung notwendig? Art. 22 Risiko bei HR-KI? | Neue AVVs mit unbekannten Anbietern; kleinere Anbieter = mehr Due-Diligence-Aufwand | Direktkontrolle über Datenflüsse; Art. 28 nur für Foundation-Model-Anbieter |
| **Vendor-Risiko** | Lock-in tiefer als heute; Preissetzungsmacht bei Renewals steigt | Startups mit Liquiditätsrisiko; keine Enterprise-SLAs | Eigenentwicklung = Eigenverantwortung; kein Support-Level-Agreement |
| **Change Management** | Geringste Disruption; bekannte Oberflächen | Mittlere Disruption; Lena Strauch (Sales) und Petra Höll (HR) müssen überzeugt werden | Höchste Disruption; IT-Kapazität ist kritischer Flaschenhals |
| **Governance / EU AI Act** | Anbieter tragen Compliance-Last (mit Vorbehalt); aber Hochrisiko-Funktionen in HR-KI prüfen | Prüfung der KI-Klassifizierung neuer Anbieter nötig | Vollständige Eigenverantwortung — Arventis wird zum „Provider" im Sinne des EU AI Act |

---

### ③ Die Kirkland-&-Ellis-Falle

Kirkland & Ellis hat ~$500 Mio. in Harvey investiert und kann mit ~500 Partnern à $40 Mio. Jahresumsatz rechnen — der ROI ist bei dieser Umsatzbasis rechnerisch plausibel.

*Aufgabe: Überprüfe, ob Option C für Arventis dieselbe ROI-Logik hat.*

Annahmen:
- Entwicklungskosten In-house KI-Agenten: geschätzt €180.000–€350.000 (Consultant + API-Kosten, 12 Monate)
- IT-Ressource: Dirk Haase hat heute keine Entwicklungskapazität; externe Beauftragung nötig
- Workday als reines Datensystem: Lizenzreduzierung theoretisch möglich, aber Vertragsbindung bis 2028

*Frage: Ab welcher Kosteneinsparung durch Automatisierung amortisiert sich Option C bei Arventis — und wie wahrscheinlich ist diese Einsparung realistisch?*

---

### ④ Entscheidungsempfehlung formulieren

Formuliere eine Empfehlung für Michael Kunz (CFO) im Format einer **Management-Briefing-Notiz** (max. 1 Seite):

1. **Ausgangslage** (Was ist das Problem?)
2. **Optionenüberblick** (3 Optionen, 2 Sätze je)
3. **Empfehlung** (Welche Option — oder welche Kombination?)
4. **Bedingungen** (Was muss vor einem Go geklärt sein?)
5. **Risiken** (Was könnte schiefgehen?)
6. **Nächste Schritte** (3 konkrete Maßnahmen in 60 Tagen)

*Zielgruppe der Notiz: CFO ohne technischen Hintergrund; Lesezeit max. 5 Minuten.*

---

### ⑤ Pricing-Modell-Risiko erklären

Der Wechsel von Seat-based zu Consumption-based Pricing (Zahlung pro Agenten-Transaktion) ist keine reine Lizenzfrage — es ist ein Planungsrisiko.

*Erkläre dem CFO mit einem konkreten Zahlenbeispiel:*
- Wie verhält sich der Kostenblock bei 50 % mehr Agentennutzung?
- Wie bei einem Systemausfall des Agenten, der 10.000 Transaktionen in einer Nacht wiederholt?
- Was bedeutet Consumption-based Pricing für das Budget-Controlling im nächsten Geschäftsjahr?

---

## Rahmenbedingungen

- Salesforce-Vertrag läuft im **Januar 2027** aus — Entscheidung nötig bis spätestens Oktober 2026
- IT-Team hat **keine freien Entwicklungskapazitäten** für Option C ohne externe Beauftragung
- Betriebsrat muss bei jeder KI-Einführung im HR-Bereich (Option A und C gleichermaßen) vor Go-live einbezogen werden (**BetrVG § 87** — Betriebsvereinbarung erforderlich)
- Workday-AVV deckt KI-Add-ons noch nicht ab — Nachtragsverhandlung steht an (Frist: Q3 2026)

---

## Ergebnis

Du präsentierst deine Analyse Michael Kunz in einem **30-Minuten-Jour fixe**. Die Agenda:
1. Marktkontext (5 Min): Warum ist das heute eine andere Entscheidung als 2021?
2. Optionenvergleich (10 Min): Was spricht wofür — und was spricht dagegen?
3. Empfehlung (10 Min): Dein Votum — und welche Vorbedingungen gelten?
4. Offene Fragen (5 Min): Was musst du noch klären, bevor du Recht bekommst?

---

## Analyse & Hinweise

### Einordnung

**Kurs:** KI-Manager — Woche 2, Tag 10 (Build vs. Buy, strategische KI-Entscheidungen)  
**Sekundär:** KI-Manager Tag 7 (Tool-Bewertung), Tag 4 (Stakeholder-Management)  
**KI-System-Typ:** Keine einzelne KI — es geht um die Architekturentscheidung, *in welcher Schicht* KI eingebettet werden soll  
**Schwierigkeitsgrad:** Hoch  
**Didaktische Funktion:** Transferaufgabe — das Vier-Quadranten-Denken aus dem Kurs (Impact/Effort, Build vs. Buy, Human-in-the-Loop) auf eine echte strategische Entscheidung anwenden; kein richtiges Ergebnis, aber ein *rigoroses Vorgehen*

---

### Musterlösung — Tendenzrahmen

*Kein Absoluturteil, aber eine didaktisch vertretbare Orientierung:*

**Option A (Incumbent-Upgrade) — Kurzfristig wahrscheinlichste Wahl**, wenn:
- Salesforce-Vertrag im Januar 2027 verlängert werden muss
- IT-Kapazität fehlt für Migration (Dirk Haase)
- Betriebsrat-Prozess Zeit braucht

Risiko: Anbieter haben Pricing-Macht, da Lock-in tief. Agentforce ist Seat-plus-Consumption-Hybrid — Kostenplanung wird schwieriger.

**Option B (KI-native Vertikals) — Mittelfristig strategisch interessant**, aber:
- Sierra und Serval sind junge Startups ohne Enterprise-SLA-Track-Record
- Migration Salesforce → Sierra dauert realistisch 9–15 Monate, nicht 3
- Für Arventis-Größe (€115 Mio.) sind diese Anbieter oft noch nicht „enterprise-ready"

Empfehlung: Beobachten, nicht sofort. 2028 kann das Bild anders aussehen.

**Option C (In-house) — Skalenargument fehlt bei Arventis:**
- Kirkland & Ellis skaliert den ROI mit Partnergehältern; ein 920-MA-HR-Dienstleister ohne eigenes Tech-Team hat diesen Hebel nicht
- Nicht ausschließen — aber auf Teilbereiche begrenzen (z. B. eigener Chatbot für interne HR-Fragen auf Workday-Datenbasis)

**Realistische Hybridempfehlung:**
> Option A als Basis-Fortsetzung + gezielte In-house-Piloten in kontrollierten Bereichen (interner HR-Bot auf Workday-Basis; Vertriebsassistent als Copilot-Erweiterung auf Salesforce-Daten) + Marktbeobachtungsmandat für Option B bis Ende 2027.

---

### Häufige Fehler im Seminar

**Fehler 1 — „In-house ist günstiger":** Teilnehmende vergleichen API-Kosten (~€0,01/Anfrage) mit Lizenzkosten (~€1.000/Seat/Jahr) und schlussfolgern fälschlicherweise, Option C sei viel billiger. Korrektur: Der Vergleich ignoriert Entwicklungszeit, Wartung, Testing, Datenmigration und Governance-Aufwand. Die richtige Frage ist: *Was kostet die Stunde Entwicklung, und wie viele Stunden brauchen wir?*

**Fehler 2 — „Wir wechseln einfach":** Salesforce-Migration wird regelmäßig unterschätzt. Typische Realzeit: 9–18 Monate für einen vollständigen CRM-Wechsel in dieser Unternehmensgröße. Dirk Haases Einwand ist keine Blockade — er ist realistisches Erfahrungswissen.

**Fehler 3 — Betriebsrat ignorieren:** CHRO Petra Höll ist kein Widerstandsmuster — sie stellt eine echte rechtliche Anforderung. BetrVG § 87 Abs. 1 Nr. 6 schreibt Mitbestimmung bei technischen Überwachungseinrichtungen vor; KI-Systeme fallen regelmäßig darunter. Betriebsvereinbarung dauert 3–12 Monate.

**Fehler 4 — Consumption-Pricing als neutral betrachten:** Der Shift von Seat zu Consumption bedeutet: Im Monat des größten Erfolgs (höchste Agentennutzung = höchster Geschäftserfolg) ist die Softwarerechnung am höchsten. Das ist eine Planungslogik, die Finanzabteilungen explizit erklären werden muss.

---

### Amdahl's Law auf Organisationen — Kernbotschaft für Tag 10

Der Übergang zu KI-Agenten verlagert den Engpass: Wenn KI 80 % der Ticket-Bearbeitung übernimmt, sind die restlichen 20 % — die komplexen Fälle, die Eskalationen, die Edge Cases — plötzlich der limitierende Faktor. Dirk Haase (IT) und das Support-Team werden nicht entlastet; sie werden mit einem *anderen* Problem beschäftigt, für das KI keine Hilfe ist. Wer KI-ROI berechnet, muss diesen Bottleneck-Shift explizit benennen.

*Verweis: Quelle #35 (Amdahl's Law auf Organisationen — Favaro & Clark / Anthropic Institute)*

---

### Verbindungen im Curriculum

| Quelle/UC | Thema | Verbindung |
|---|---|---|
| #43 (Economist, SaaSpocalypse) | Marktstruktur-Analyse, SaaSquatches | Direkte Grundlage für Aufgabe ① |
| #3 (Vendor Risk Transfer Illusion) | Wer haftet bei Outage? | Option A — was ist im SLA wirklich garantiert? |
| #14 (Co-Intelligence, Mollick) | Vier Aufgabentypen | Welche Aufgaben soll der Agent übernehmen — und für welche ist das riskant? |
| #21 (Jagged Frontier, Dell'Acqua) | Wo versagt KI heute noch? | Grenzen von Option B/C: Was kann der Agent *nicht*, und wer erkennt das? |
| #35 (Amdahl's Law, Anthropic Institute) | Organisationaler Flaschenhals nach KI | Kernbotschaft für ③ (ROI-Rechnung) und ⑤ (Consumption-Pricing) |
| UC-04 (SolidFinanz AG) | Schatten-KI-Inventur | Parallelthema: Wie entsteht unkontrollierte KI-Nutzung, wenn offizielle Tools zu teuer sind? |
| UC-06a (AIktiv-Invest) | ROI-Berechnung Build vs. Buy | Methodentransfer: ROI-Rechnung aus UC-06 auf Option-C-Szenario anwenden |

---

*Letzte Aktualisierung: Juni 2026 — Ulrich Nord / Claude (Anthropic)*
