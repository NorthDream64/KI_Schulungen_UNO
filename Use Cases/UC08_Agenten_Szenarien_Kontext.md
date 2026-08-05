# UC08 · KI-Agenten-Szenarien 

> Fünf vollständig spezifizierte Agenten-Prompts als Übungsmaterial für den Praxisblock „Bau von Agenten". Live durch den Dozenten eingeführt — kein Bestandteil von Hand-Out oder Gamma-Skript.

---

## 1 · Freelance Opportunity Agent

"I want you to regularly scan relevant platforms, professional networks and selected websites for freelance opportunities within the EU that match my professional profile, expertise, availability and market offering.

Evaluate each opportunity using a predefined scoring model that considers factors such as service fit, required experience, location, remote-work options, contract duration, expected workload, budget, application deadline and likelihood of success.

Exclude opportunities that fail mandatory requirements, identify potential gaps or uncertainties, and rank the remaining opportunities by overall attractiveness. Avoid duplicate entries and update previously identified opportunities when their status or requirements change.

For each shortlisted opportunity, provide the source, publication date, deadline, key requirements, evaluation score and a brief explanation of the recommendation.

If an opportunity exceeds the defined qualification threshold, alert me by e-mail and prepare a tailored application package based on the opportunity's requirements and my approved profile and market offering. The package should include an application summary, a proposed cover letter or submission document, and a checklist of any information or documents still required.

Do not submit an application or contact the client without my explicit approval."

---

## 2 · Tender Identification and Bid Preparation Agent

"I want you to regularly identify public and private tenders within the EU that match my company's services, experience, capacity and delivery capabilities.

Review the available tender documentation and assess mandatory requirements, eligibility criteria, geographic restrictions, submission deadlines, contract value, required certifications, delivery timelines, commercial conditions, strategic fit and potential delivery risks.

Exclude tenders for which mandatory requirements cannot be met. Evaluate and rank the remaining opportunities using a predefined scoring model, clearly distinguishing confirmed information from assumptions or missing information.

Avoid duplicate entries and update previously identified tenders when amendments, deadline changes, clarifications or additional documents are published.

For each relevant tender, provide the source, contracting authority, deadline, estimated contract value, key requirements, evaluation score, major risks and a brief bid/no-bid recommendation.

If a tender exceeds the defined qualification threshold, alert me by e-mail and prepare a bid summary, a requirements-compliance matrix, a list of required evidence and documents, key clarification questions, and an initial proposal outline.

Do not submit a bid, make binding commitments or contact the contracting authority without my explicit approval."

---

## 3 · Sales Opportunity and Account Intelligence Agent

"I want you to monitor a predefined list of target companies for credible events that may indicate a current or emerging need for my services.

Relevant signals may include management changes, funding rounds, mergers or acquisitions, geographic expansion, new products or projects, strategic announcements, technology investments, job postings, operational problems, regulatory challenges or other significant business developments.

Evaluate each signal according to its source reliability, relevance to my offering, recency, urgency, estimated commercial potential and strength of the inferred customer need. Distinguish verified facts from assumptions and explain the reasoning behind each assessment.

Combine related signals, avoid duplicate alerts and maintain an updated opportunity history for each target company.

If a signal or combination of signals exceeds the defined qualification threshold, alert me by e-mail and prepare an account briefing containing the relevant developments, likely business needs, potential stakeholders, suggested value proposition, recommended contact strategy and a personalized outreach message.

Do not contact the company, send the outreach message or add personal data from unapproved sources without my explicit approval."

---

## 4 · EU Regulatory Monitoring and Impact Assessment Agent

"I want you to regularly monitor authoritative EU and national sources for regulatory developments that may affect my organization, products, services, operations or clients.

Relevant developments may include new or amended laws, regulations, standards, guidelines, regulatory consultations, supervisory decisions, enforcement actions and official interpretations.

For each development, verify the source and status, summarize the relevant changes, identify the affected jurisdictions, business areas and stakeholders, and assess the expected impact, urgency, implementation effort, compliance risk and relevant deadlines.

Distinguish between proposals, consultations, adopted legislation, applicable requirements and non-binding guidance. Avoid duplicate entries and update existing records when the legal status, scope, interpretation or implementation timeline changes.

For each relevant development, provide links to the primary sources, publication and applicability dates, a concise summary, the assessment score and an explanation of its relevance.

If a development exceeds the defined risk or relevance threshold, alert me by e-mail and prepare an impact assessment, a list of recommended actions, responsible functions, important deadlines and a short management briefing.

Clearly flag areas that require review by qualified legal or compliance professionals. Do not present the assessment as formal legal advice or initiate implementation actions without human approval."

---

## 5 · AI Risk Intelligence and Risk Register Agent

"I want you to regularly scan a defined set of authoritative and relevant sources for newly identified or materially changed AI-related risks, vulnerabilities, incidents, control weaknesses and regulatory concerns.

Sources may include NIST, ENISA, the EU AI Office, national authorities, recognized standards bodies, major AI providers, Hugging Face, research repositories, vulnerability databases, incident databases and selected security publications. Prioritize primary sources and record the source, publication date and access date for every finding.

Assess each finding for relevance to my organization's approved AI systems, use cases, data, vendors, processes and business environment. Classify relevant findings by risk category, affected assets or processes, threat or failure scenario, existing vulnerabilities, likelihood, potential impact, urgency and confidence level.

Compare each finding with the existing risk register. Avoid duplicate entries, link related findings and update an existing risk only when new evidence materially changes its description, likelihood, impact, controls or status. Maintain a clear change history.

For each relevant risk, propose proportionate preventive, detective and corrective measures. Identify possible control owners, implementation priorities, dependencies, residual-risk considerations, monitoring indicators and recommended follow-up actions. Clearly distinguish existing controls from proposed controls.

Each proposed risk-register entry should include:

- a unique risk identifier;
- the risk title and description;
- the source and supporting evidence;
- affected systems, assets, processes or stakeholders;
- the risk category;
- causes, threat events and potential consequences;
- likelihood, impact and overall risk rating;
- existing controls;
- proposed preventive, detective and corrective controls;
- potential control owners;
- recommended actions and target dates;
- the residual-risk estimate;
- the confidence level and any unresolved questions.

If a finding exceeds the defined risk threshold, alert me by e-mail and prepare a draft risk-register entry, a short management summary and a prioritized action plan for human review.

Do not automatically accept, close, downgrade or assign a risk, change an approved control, or initiate remediation activities without explicit human approval."

---

## Deine Aufgabe

Wählt mindestens eines der fünf Szenarien. Der Prompt-Text beschreibt, *was* der Agent tun soll — für den Bau fehlt noch, *wie* er es tun soll. Konkretisiert für jeden gewählten Agenten mindestens:

- **Quellen** — welche konkreten Plattformen, Register, Websites, APIs?
- **Prüfintervall** — wie oft läuft der Agent (täglich, wöchentlich, ereignisgesteuert)?
- **Bewertungsmodell** — welche Kriterien, welche Gewichtung, wie wird der Score berechnet?
- **Schwellenwert** — ab welchem Score bzw. welcher Bewertung erfolgt die Eskalation an den Menschen?
- **Ausgabeformat** — wie sieht die Alarmierung bzw. der Bericht konkret aus (Struktur, Felder)?
- **Zulässige Aktionen** — was darf der Agent eigenständig tun, was braucht explizite Freigabe?

**Drei Prüffragen an euer Ergebnis:**

1. Könnte ein anderes Team euren Agenten allein aus eurer Konkretisierung nachbauen?
2. Ist an jeder Stelle klar, wo der Mensch entscheidet und wo der Agent nur vorbereitet?
3. Welche der Basics aus dem Hand-Out (Agent vs. Workflow, Eignungssignale, drei Bausteine, Leitplanken-Pflicht) erkennt ihr in eurem Szenario wieder — und wo fehlt im Original-Prompt noch eine Leitplanke?

---

## Hinweis

Die fünf Szenarien sind Übungsmaterial für den Praxisblock, keine realen Kundenaufträge. Alle Konkretisierungen (Schwellenwerte, Plattformen, Bewertungsmodelle) sind von den Teilnehmenden selbst zu entwickeln, nicht vorgegeben.
