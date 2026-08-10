# Das Daten-Quartett

> **36 Karten · 9 Familien · 4 Karten je Familie**
> Arbeitshilfe zu Datenmanagement, Datenqualität und Daten-Governance.
> Spielprinzip: *Finde alle vier Karten einer Familie.* Jede Karte nennt ihre drei Geschwister —
> wer eine Karte in der Hand hält, sieht sofort, was ihm noch fehlt.
> Das ist die Kernfrage: **Hast du auch an die anderen drei gedacht?**

---

## Die neun Familien im Überblick

| | Familie | Karte 1 | Karte 2 | Karte 3 | Karte 4 |
|---|---|---|---|---|---|
| **A** | Bestandsaufnahme | Datenverzeichnis | Eigentümerschaft | Schutzbedarf | Schattennutzung |
| **B** | Datenqualität | Die sechs Dimensionen | Herkunftsnachweis | Reproduzierbare Aufbereitung | Zukunftswissen |
| **C** | Datenrecht | Lizenz & Einwilligung | Zweckbindung | Speicherort | Löschkonzept |
| **D** | Zugriffe | Eindeutige Identität | Technische Identitäten | Mehrfaktor | Entzug |
| **E** | Rechte | Rollenbasierte Vergabe | Geringste Rechte | Technisch erzwungen | Rezertifizierung |
| **F** | Menschliche Kontrollen | Datenvertrag | Freigabe-Gate | Override-Rate | Eskalationsweg |
| **G** | Technische Kontrollen | Verschlüsselung | Anonymisierung | Abschottung | Automatische Prüfung |
| **H** | Betrieb & Notausstieg | Abbruchkriterium | Drift-Überwachung | Rückroll-Verfahren | Not-Aus |
| **I** | Nachweis | Protokollierung | Rückverfolgbarkeit | Dokumentation | Wirksamkeitsprüfung |

**D und E gehören zusammen und werden trotzdem getrennt:** Authentifizierung beantwortet „wer bist du?", Autorisierung „was darfst du?". Es ist das am häufigsten verwechselte Begriffspaar im ganzen Feld — deshalb zwei Familien statt einer.

---

# A · Bestandsaufnahme

> *Datenverzeichnis · Eigentümerschaft · Schutzbedarf · Schattennutzung*

### A1 — Datenverzeichnis
**Gibt es ein Verzeichnis der Datenbestände, die für KI genutzt werden sollen?**
Ohne Inventar ist jede weitere Aussage über Qualität oder Schutzbedarf geraten. Das Verzeichnis ist die Voraussetzung für alle 35 anderen Karten.
*Familie A: **Datenverzeichnis** · Eigentümerschaft · Schutzbedarf · Schattennutzung*

### A2 — Eigentümerschaft
**Hat jeder Datenbestand eine benannte verantwortliche Person — keine Abteilung, eine Person?**
Eigentümerschaft ohne Namen ist Eigentümerschaft ohne Ansprechpartner. „Die IT" ist keine Antwort.
*Familie A: Datenverzeichnis · **Eigentümerschaft** · Schutzbedarf · Schattennutzung*

### A3 — Schutzbedarf
**Sind die Bestände klassifiziert — öffentlich, intern, vertraulich, besondere Kategorien?**
Die Einstufung entscheidet später über Verschlüsselung, Zugriffsrechte und Speicherort. Wer sie überspringt, trifft diese Entscheidungen unbewusst.
*Familie A: Datenverzeichnis · Eigentümerschaft · **Schutzbedarf** · Schattennutzung*

### A4 — Schattennutzung
**Wissen wir, welche Daten außerhalb der freigegebenen Systeme bewegt werden?**
Laut Verizon DBIR 2026 ist ungesteuerte KI-Nutzung die dritthäufigste nicht-böswillige Insider-Handlung; am häufigsten übertragen wird Quellcode. Ein Verbot verlagert sie nur.
*Familie A: Datenverzeichnis · Eigentümerschaft · Schutzbedarf · **Schattennutzung***

---

# B · Datenqualität

> *Die sechs Dimensionen · Herkunftsnachweis · Reproduzierbare Aufbereitung · Zukunftswissen*

### B1 — Die sechs Dimensionen
**Sind Vollständigkeit, Konsistenz, Genauigkeit, Aktualität, Relevanz und Eindeutigkeit bewertet?**
Nicht alle auf 100 % — das ist unbezahlbar. Die Frage ist, welche für *diesen* Anwendungsfall entscheidend sind. Datenqualität ist relativ zum Zweck.
*Familie B: **Die sechs Dimensionen** · Herkunftsnachweis · Reproduzierbare Aufbereitung · Zukunftswissen*

### B2 — Herkunftsnachweis
**Ist dokumentiert, woher jeder Datenbestand stammt?**
Ohne Herkunft lässt sich weder Lizenz noch Qualität noch Verzerrung zurückverfolgen. Der Nachweis ist die Voraussetzung dafür, einen Fehler überhaupt einzugrenzen.
*Familie B: Die sechs Dimensionen · **Herkunftsnachweis** · Reproduzierbare Aufbereitung · Zukunftswissen*

### B3 — Reproduzierbare Aufbereitung
**Ist die Aufbereitung dokumentiert und wiederholbar — oder war es Handarbeit in einer Tabelle?**
Nicht reproduzierbare Aufbereitung heißt: Beim nächsten Training kommt ein anderes Ergebnis heraus, und niemand kann sagen, warum.
*Familie B: Die sechs Dimensionen · Herkunftsnachweis · **Reproduzierbare Aufbereitung** · Zukunftswissen*

### B4 — Zukunftswissen im Training
**Nutzen wir ausschließlich Daten, die zum Entscheidungszeitpunkt tatsächlich vorliegen?**
Sonst trainiert das Modell mit Wissen, das es im Betrieb nie hat. Im Test glänzt es, in der Praxis versagt es. Englisch: Look-ahead Bias bzw. Data Leakage — nicht zu verwechseln mit Datenabfluss.
*Familie B: Die sechs Dimensionen · Herkunftsnachweis · Reproduzierbare Aufbereitung · **Zukunftswissen***

---

# C · Datenrecht

> *Lizenz & Einwilligung · Zweckbindung · Speicherort · Löschkonzept*

### C1 — Lizenz & Einwilligung
**Ist geprüft, ob wir diese Daten für diesen Zweck überhaupt verwenden dürfen?**
Vorhandene Daten sind nicht automatisch nutzbare Daten — vertraglich, urheberrechtlich, datenschutzrechtlich. Zugriff haben heißt nicht Nutzen dürfen.
*Familie C: **Lizenz & Einwilligung** · Zweckbindung · Speicherort · Löschkonzept*

### C2 — Zweckbindung
**Ist festgehalten, wofür die Freigabe gilt — und wird eine Zweckänderung neu geprüft?**
Zweckbindung ist keine Formalie, sondern die Grenze der Freigabe. Der häufigste Verstoß ist kein Diebstahl, sondern schleichende Zweckerweiterung.
*Familie C: Lizenz & Einwilligung · **Zweckbindung** · Speicherort · Löschkonzept*

### C3 — Speicherort
**Wissen wir, wo die Daten physisch liegen — und ist das mit den Anforderungen vereinbar?**
Die Datenresidenz entscheidet über anwendbares Recht und über mögliche Zugriffe Dritter. Seit dem EU Data Act ist auch der Wechsel des Anbieters weitgehend Rechtsanspruch.
*Familie C: Lizenz & Einwilligung · Zweckbindung · **Speicherort** · Löschkonzept*

### C4 — Löschkonzept
**Gibt es Aufbewahrungsfristen — und werden sie tatsächlich vollzogen?**
Ein Löschkonzept, das niemand ausführt, ist ein Dokument, keine Maßnahme. Daten, die man nicht mehr hat, können nicht mehr abfließen.
*Familie C: Lizenz & Einwilligung · Zweckbindung · Speicherort · **Löschkonzept***

---

# D · Zugriffe *(Authentifizierung)*

> *Eindeutige Identität · Technische Identitäten · Mehrfaktor · Entzug*
> **Leitfrage der Familie: Wer ist das überhaupt?**

### D1 — Eindeutige Identität
**Hat jede zugreifende Person eine persönliche Identität — keine geteilten Konten?**
Geteilte Konten machen jede spätere Zurechnung unmöglich. Ohne diese Karte ist die gesamte Familie I (Nachweis) wertlos.
*Familie D: **Eindeutige Identität** · Technische Identitäten · Mehrfaktor · Entzug*

### D2 — Technische Identitäten
**Haben auch Dienste, Schnittstellen und KI-Agenten eigene Identitäten?**
Ein Agent, der unter dem Konto seiner Entwicklerin läuft, ist im Protokoll nicht von ihr zu unterscheiden. Bei agentischen Systemen die am häufigsten übersehene Karte.
*Familie D: Eindeutige Identität · **Technische Identitäten** · Mehrfaktor · Entzug*

### D3 — Mehrfaktor
**Ist mehrstufige Authentifizierung für sensible Bestände verpflichtend?**
Ein Passwort ist ein Geheimnis, das man verlieren kann. Der zweite Faktor ist der Unterschied zwischen einem geleakten Zugangsdatum und einem Vorfall.
*Familie D: Eindeutige Identität · Technische Identitäten · **Mehrfaktor** · Entzug*

### D4 — Entzug
**Werden Identitäten beim Rollenwechsel und beim Austritt zuverlässig entzogen?**
Verwaiste Konten sind der stillste Weg zum Datenabfluss — sie fallen niemandem auf, weil sie niemandem gehören.
*Familie D: Eindeutige Identität · Technische Identitäten · Mehrfaktor · **Entzug***

---

# E · Rechte *(Autorisierung)*

> *Rollenbasierte Vergabe · Geringste Rechte · Technisch erzwungen · Rezertifizierung*
> **Leitfrage der Familie: Was darf diese Identität — und wirklich nur das?**

### E1 — Rollenbasierte Vergabe
**Sind Rechte an Rollen geknüpft statt an Personen?**
Personengebundene Rechte wachsen über Jahre mit und werden nie zurückgenommen. Nach zehn Jahren im Haus hat man Zugriff auf alles, was man je gebraucht hat.
*Familie E: **Rollenbasierte Vergabe** · Geringste Rechte · Technisch erzwungen · Rezertifizierung*

### E2 — Geringste Rechte
**Gilt durchgängig: so wenig Zugriff wie zur Aufgabe nötig?**
Die IMDA nennt Least Privilege als zentrale Maßnahme, um die Wirkung eines Agenten auf seine Umgebung zu begrenzen. Lesen, Schreiben und Nach-außen-Wirken sind drei verschiedene Stufen.
*Familie E: Rollenbasierte Vergabe · **Geringste Rechte** · Technisch erzwungen · Rezertifizierung*

### E3 — Technisch erzwungen
**Sind Rechte auf Infrastrukturebene gesetzt — nicht nur als Anweisung im System-Prompt?**
Anweisungen im Prompt können umgangen oder schlicht nicht befolgt werden. Sie ersetzen keine erzwungenen Rechte. Die Karte, die bei KI-Projekten am häufigsten fehlt.
*Familie E: Rollenbasierte Vergabe · Geringste Rechte · **Technisch erzwungen** · Rezertifizierung*

### E4 — Rezertifizierung
**Werden Rechte regelmäßig überprüft und entzogen, wenn sie nicht mehr gebraucht werden?**
Unbeliebt und unverzichtbar. Ohne diese Karte verfallen E1 und E2 innerhalb weniger Jahre von selbst.
*Familie E: Rollenbasierte Vergabe · Geringste Rechte · Technisch erzwungen · **Rezertifizierung***

---

# F · Menschliche Kontrollen

> *Datenvertrag · Freigabe-Gate · Override-Rate · Eskalationsweg*

### F1 — Datenvertrag
**Gibt es je Datenbestand eine Zusage über Struktur, Bedeutung, Aktualität und Verantwortung?**
Das häufigste Integrationsproblem ist organisatorisch: Ein Fachbereich ändert ein Feld, und drei Wochen später liefert ein Modell stillschweigend Unsinn.
*Familie F: **Datenvertrag** · Freigabe-Gate · Override-Rate · Eskalationsweg*

### F2 — Freigabe-Gate
**Ist festgelegt, an welchen Punkten ein Mensch freigeben muss — und ist jede irreversible Aktion gebunden?**
Umkehrbar oder nicht ist die Trennlinie, nicht „wichtig oder unwichtig". Das Gate ist zugleich der Ort, an dem die Daten für F3 überhaupt entstehen.
*Familie F: Datenvertrag · **Freigabe-Gate** · Override-Rate · Eskalationsweg*

### F3 — Override-Rate
**Messen wir, wie oft Menschen die KI-Empfehlung tatsächlich verwerfen?**
Die IMDA nennt Override-Rate und Reaktionszeit ausdrücklich als Mittel gegen Automation Bias. Eine Quote nahe null ist so verdächtig wie eine sehr hohe — sie bedeutet Durchwinken.
*Familie F: Datenvertrag · Freigabe-Gate · **Override-Rate** · Eskalationsweg*

### F4 — Eskalationsweg
**Gibt es einen Weg nach oben, der auch dann funktioniert, wenn es unbequem wird?**
Ein Eskalationspfad, der über die Person führt, deren Projekt gestoppt würde, ist keiner.
*Familie F: Datenvertrag · Freigabe-Gate · Override-Rate · **Eskalationsweg***

---

# G · Technische Kontrollen

> *Verschlüsselung · Anonymisierung · Abschottung · Automatische Prüfung*

### G1 — Verschlüsselung
**Sind Daten bei Übertragung und Speicherung verschlüsselt?**
Die Grundlage, auf der alles Weitere aufbaut — und die am häufigsten stillschweigend vorausgesetzt statt geprüft wird.
*Familie G: **Verschlüsselung** · Anonymisierung · Abschottung · Automatische Prüfung*

### G2 — Anonymisierung
**Werden personenbezogene Daten anonymisiert oder pseudonymisiert, wo der Zweck es zulässt?**
Was nicht identifizierbar ist, muss nicht geschützt werden. Der beste Schutz ist, die Daten gar nicht erst zu haben.
*Familie G: Verschlüsselung · **Anonymisierung** · Abschottung · Automatische Prüfung*

### G3 — Abschottung
**Sind Systeme so getrennt, dass ein Fehler nicht sofort alles betrifft?**
Testumgebungen, getrennte Mandanten, begrenzte Wirkungsräume. Schadensbegrenzung wird beim Entwurf entschieden, nicht im Ernstfall.
*Familie G: Verschlüsselung · Anonymisierung · **Abschottung** · Automatische Prüfung*

### G4 — Automatische Prüfung
**Laufen automatische Qualitätsprüfungen auf den eingehenden Daten?**
Regelbasiert prüft, was du vorgibst; musterlernend meldet Abweichungen vom Normalzustand. Beides schlägt „fällt schon jemandem auf". Diese Karte macht B1 dauerhaft wirksam.
*Familie G: Verschlüsselung · Anonymisierung · Abschottung · **Automatische Prüfung***

---

# H · Betrieb & Notausstieg

> *Abbruchkriterium · Drift-Überwachung · Rückroll-Verfahren · Not-Aus*

### H1 — Abbruchkriterium
**Ist vorab und schriftlich festgelegt, bei welchen Werten das Vorhaben gestoppt wird?**
Die stärkste Karte im Deck. Wer das Abbruchkriterium erst im Ernstfall definiert, definiert es nie — dann wirkt bereits der Druck, weiterzumachen.
*Familie H: **Abbruchkriterium** · Drift-Überwachung · Rückroll-Verfahren · Not-Aus*

### H2 — Drift-Überwachung
**Wird überwacht, ob sich Daten oder Modellverhalten über die Zeit verschieben?**
Drift kündigt sich in den Daten an, bevor sie im Ergebnis sichtbar wird. Ohne diese Karte merkt man den Qualitätsverfall an Beschwerden.
*Familie H: Abbruchkriterium · **Drift-Überwachung** · Rückroll-Verfahren · Not-Aus*

### H3 — Rückroll-Verfahren
**Gibt es einen erprobten Weg zurück auf einen früheren Stand?**
Ein Rückroll-Verfahren, das noch nie geübt wurde, ist eine Hoffnung, kein Verfahren.
*Familie H: Abbruchkriterium · Drift-Überwachung · **Rückroll-Verfahren** · Not-Aus*

### H4 — Not-Aus
**Kann das System schnell und vollständig abgeschaltet werden — und weiß jemand, wie?**
Der Not-Aus muss auch funktionieren, wenn die Person, die ihn gebaut hat, im Urlaub ist. Dazu gehört die Frage, wer ihn auslösen darf.
*Familie H: Abbruchkriterium · Drift-Überwachung · Rückroll-Verfahren · **Not-Aus***

---

# I · Nachweis

> *Protokollierung · Rückverfolgbarkeit · Dokumentation · Wirksamkeitsprüfung*

### I1 — Protokollierung
**Werden Zugriffe, Änderungen und Entscheidungen unveränderlich protokolliert?**
Ein Protokoll, das sich nachträglich ändern lässt, ist als Nachweis wertlos. Baut zwingend auf D1 auf — ohne eindeutige Identität protokolliert man Konten, nicht Menschen.
*Familie I: **Protokollierung** · Rückverfolgbarkeit · Dokumentation · Wirksamkeitsprüfung*

### I2 — Rückverfolgbarkeit
**Lässt sich ein einzelnes Ergebnis bis zu seinen Eingangsdaten zurückverfolgen?**
Die eigentliche Prüfung jeder Datenarchitektur. Wer diese Frage nicht beantworten kann, kann im Zweifelsfall nicht erklären, wie eine Entscheidung zustande kam.
*Familie I: Protokollierung · **Rückverfolgbarkeit** · Dokumentation · Wirksamkeitsprüfung*

### I3 — Dokumentation
**Sind Datenquellen, Aufbereitung und getroffene Annahmen festgehalten?**
Annahmen, die nirgends stehen, gelten später als Fakten. Das ist der Weg, auf dem Schätzwerte zu Kennzahlen werden.
*Familie I: Protokollierung · Rückverfolgbarkeit · **Dokumentation** · Wirksamkeitsprüfung*

### I4 — Wirksamkeitsprüfung
**Wird regelmäßig überprüft, ob all das noch funktioniert — nicht nur einmal zur Einführung?**
Einmalige Abnahme ist keine Governance. Diese Karte schließt den Kreis zurück zu A1: Beim Nachprüfen fällt auf, dass das Verzeichnis nicht mehr stimmt.
*Familie I: Protokollierung · Rückverfolgbarkeit · Dokumentation · **Wirksamkeitsprüfung***

---

## Spielvarianten für den Unterricht

**Familien sammeln (Grundform).** Karten mischen und verteilen. Wer eine Karte hat, sieht ihre drei Geschwister und fragt gezielt danach. Vollständige Familie wird abgelegt und in einem Satz erklärt.

**Die fehlende Karte.** Der Dozent legt drei Karten einer Familie offen aus. Die Gruppe benennt die vierte — und begründet, warum sie dazugehört.

**Selbsteinschätzung.** Jede Gruppe zieht eine Familie und bewertet alle vier Karten für den eigenen Betrieb: erfüllt, teilweise, offen. Am Ende steht sichtbar, welche Familie im Haus die schwächsten Karten hat.

**Querverbindungen.** Mehrere Karten verweisen ausdrücklich auf andere Familien — D1 auf I1, G4 auf B1, I4 zurück auf A1. Diese Verweise sind der eigentliche Lernstoff: Governance ist kein Sortierproblem, sondern ein Netz.

---

## Quellen

| Quelle | Einordnung |
|---|---|
| [DAMA-DMBOK (2. Aufl., Rev. 2024)](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/) | herstellerneutraler Fachstandard — Grundlage für Familie B |
| [IMDA Singapur — MGF for Agentic AI (v1.5, 2026)](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf) | behördliche Guidance, in der EU nicht verbindlich — Grundlage für E2 und F3 |
| [EU Data Act — VO (EU) 2023/2854](https://eur-lex.europa.eu/eli/reg/2023/2854/oj?locale=de) | Rechtsakt, gilt seit 12.09.2025 — Grundlage für C3 |
| [EU AI Act — VO (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202401689) | Rechtsakt |
| [Verizon — DBIR 2026](https://www.verizon.com/business/resources/reports/dbir/) | Branchenbericht, nicht begutachtet — Grundlage für A4 |
| [Data Contract Specification](https://datacontract.com/) | offener Community-Standard — Grundlage für F1 |
| [Sambasivan et al. (2021) — Data Cascades, ACM CHI](https://dl.acm.org/doi/abs/10.1145/3411764.3445518) | einzige begutachtete Forschungsquelle |
| ISO/IEC 42001:2023 · DSGVO (EU) 2016/679 | Norm bzw. Rechtsakt |

Artikelangaben sind Orientierung, keine Rechtsberatung. Das Deck soll verhindern, dass etwas *vergessen* wird — ob es im Einzelfall *ausreicht*, beurteilen die zuständigen Fachfunktionen.

---

*Das Daten-Quartett · Ulrich Nord · August 2026*
