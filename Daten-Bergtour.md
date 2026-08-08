# Die Datenreise — woran muss ich denken?

> Arbeitshilfe zu **Datenmanagement, Datenqualität und Daten-Governance** in KI-Vorhaben.
> Acht Etappen, 45 Prüffragen. Jede Etappe fragt, sie schreibt nicht vor: *Hast du daran gedacht?*
>
> **Bildidee:** Eine Bergtour vom Tal zum Gipfel — mit Rückweg. Eine Tour plant man nicht am Gipfel, sondern im Basislager.

---

## Aufbau für die Visualisierung

| # | Etappe | Metapher | Farbe | Leitfrage |
|---|---|---|---|---|
| 0 | Bestandsaufnahme | **Das Basislager** | Fels-Grau | Wissen wir überhaupt, welche Daten wir haben? |
| 1 | Daten | **Die Ausrüstung** | Petrol | Taugt das Material für genau diesen Zweck? |
| 2 | Zugriffe *(Authentifizierung)* | **Das Seil** | Blau | Wer hängt am Seil? |
| 3 | Rechte *(Autorisierung)* | **Die Karabiner** | Violett | Wer darf was — und wirklich nur das? |
| 4 | Menschliche Kontrollen | **Die Seilschaft** | Grün | Wer sichert, und merkt er es rechtzeitig? |
| 5 | Technische Kontrollen | **Die Fixseile** | Dunkelblau | Was schützt, wenn niemand hinsieht? |
| 6 | Betrieb & Notausstieg | **Der Umkehrpunkt** | Rot | Wann brechen wir ab — und wer entscheidet? |
| 7 | Nachweis | **Das Gipfelbuch** | Bernstein | Können wir belegen, was wir getan haben? |

**Wichtig für die Grafik:** Es ist **kein linearer Aufstieg**. Vom Umkehrpunkt und von der Seilschaft führen Rückwege zum Basislager und zur Ausrüstung. Die IMDA beschreibt Governance ausdrücklich als iterativen Prozess — wird eine Auffälligkeit entdeckt, werden frühere Stufen neu bewertet.

---

## 0 · Das Basislager — Bestandsaufnahme

> *Bevor jemand losgeht, wird gezählt, was da ist und wer mitkommt.*

**Leitfrage: Wissen wir überhaupt, welche Daten wir haben — und wem sie gehören?**

*Normbezug: ISO/IEC 42001 Kl. 6.1 · DSGVO Art. 30 · DAMA-DMBOK*

- **Gibt es ein Verzeichnis der Datenbestände, die für KI genutzt werden sollen?**
  Ohne Inventar ist jede weitere Aussage über Qualität oder Schutzbedarf geraten.
- **Hat jeder Datenbestand eine benannte verantwortliche Person — keine Abteilung, eine Person?**
  Eigentümerschaft ohne Namen ist Eigentümerschaft ohne Ansprechpartner.
- **Sind die Bestände nach Schutzbedarf klassifiziert?**
  Die Klassifizierung entscheidet später über Verschlüsselung, Zugriff und Speicherort.
- **Wissen wir, welche Daten außerhalb der freigegebenen Systeme bewegt werden?**
  Ungesteuerte KI-Nutzung ist laut Verizon DBIR 2026 die dritthäufigste nicht-böswillige Insider-Handlung.
- **Ist geklärt, welche Daten wir gar nicht erst verwenden wollen?**
  Die bewusste Nicht-Nutzung ist eine Governance-Entscheidung und gehört dokumentiert.

> **Bergsteigerregel:** Wer im Basislager nicht zählt, merkt erst in der Wand, dass etwas fehlt.

---

## 1 · Daten — die Ausrüstung

> *Mit schlechtem Material startet niemand eine Tour.*

**Leitfrage: Taugt das Material für genau diesen Zweck?**

*Normbezug: DAMA-DMBOK (Data Quality) · EU AI Act Art. 10 · DSGVO Art. 5*

- **Sind die sechs Qualitätsdimensionen bewertet — Vollständigkeit, Konsistenz, Genauigkeit, Aktualität, Relevanz, Eindeutigkeit?**
  Nicht alle auf 100 %, sondern: welche sind für diesen Anwendungsfall entscheidend?
- **Ist die Herkunft jedes Datenbestands nachvollziehbar dokumentiert?**
  Ohne Herkunftsnachweis lässt sich weder Lizenz noch Qualität noch Bias zurückverfolgen.
- **Ist die Aufbereitung dokumentiert und wiederholbar — oder war es Handarbeit in einer Tabelle?**
  Nicht reproduzierbare Aufbereitung heißt: Beim nächsten Training kommt ein anderes Ergebnis heraus.
- **Nutzen wir ausschließlich Daten, die zum Entscheidungszeitpunkt tatsächlich vorliegen?**
  Sonst droht Datenleckage: Im Test glänzt das Modell, in der Praxis versagt es.
- **Sind Lizenzen, Einwilligungen und Zweckbindungen für die geplante Nutzung geprüft?**
  Vorhandene Daten sind nicht automatisch nutzbare Daten.
- **Ist geklärt, auf welcher Reifestufe gearbeitet wird — roh, geprüft oder aufbereitet?**
  Wer direkt auf Rohdaten zugreift, spart Aufwand und kauft ein Nachvollziehbarkeitsproblem ein.

> **Merksatz:** Datenqualität ist relativ zum Zweck. „Gut genug für den Jahresabschluss" ist nicht automatisch „gut genug für ein Modell".

---

## 2 · Zugriffe — das Seil

> *Am Seil hängt nur, wer angeseilt ist. Die erste Frage ist nie „was darf jemand", sondern „wer ist das überhaupt".*

**Leitfrage: Wer hängt am Seil — und ist das zweifelsfrei feststellbar?**

*Normbezug: Authentifizierung · ISO/IEC 42001 Kl. 8.3 · DSGVO Art. 32*

- **Hat jede zugreifende Person eine eindeutige, persönliche Identität — keine geteilten Konten?**
  Geteilte Konten machen jede spätere Zurechnung unmöglich.
- **Haben auch technische Nutzer — Dienste, Schnittstellen, KI-Agenten — eigene Identitäten?**
  Ein Agent, der unter dem Konto seiner Entwicklerin läuft, ist im Protokoll nicht von ihr unterscheidbar.
- **Ist mehrstufige Authentifizierung für sensible Datenbestände verpflichtend?**
  Nach dem Verizon DBIR 2026 ist Schwachstellenausnutzung erstmals der häufigste Einstiegspunkt.
- **Gilt der Grundsatz, dass kein Zugriff allein aufgrund des Netzwerkstandorts vertraut wird?**
  Zero Trust: „im internen Netz" ist kein Nachweis von Identität.
- **Werden Identitäten beim Rollenwechsel und Austritt zuverlässig entzogen?**
  Verwaiste Konten sind der stillste Weg zum Datenabfluss.

---

## 3 · Rechte — die Karabiner

> *Ein Karabiner verbindet genau zwei Dinge — nicht alles mit allem.*

**Leitfrage: Wer darf was mit welchen Daten — und wirklich nur das?**

*Normbezug: Autorisierung · DSGVO Art. 5 (Zweckbindung) · IMDA (Least Privilege)*

- **Sind Rechte an Rollen geknüpft statt an Personen?**
  Personengebundene Rechte wachsen über Jahre und werden nie zurückgenommen.
- **Gilt durchgängig das Prinzip der geringsten Rechte?**
  Die IMDA nennt Least Privilege als zentrale Maßnahme, um die Wirkung eines Agenten auf seine Umgebung zu begrenzen.
- **Sind Rechte technisch erzwungen — nicht nur als Anweisung im System-Prompt formuliert?**
  Anweisungen im Prompt können umgangen oder schlicht nicht befolgt werden.
- **Ist für jedes Werkzeug festgelegt, welche Aktionen es auslösen darf — und welche nie?**
  Lesen, schreiben, nach außen wirken: Drei sehr verschiedene Rechtestufen.
- **Ist der Zweck der Freigabe festgehalten — und wird eine Zweckänderung neu geprüft?**
  Zweckbindung ist keine Formalie, sondern die Grenze der Freigabe.
- **Werden Rechte regelmäßig überprüft und entzogen, wenn sie nicht mehr gebraucht werden?**
  Rechte-Rezertifizierung ist unbeliebt und unverzichtbar.

> **Die Verwechslung, die am meisten kostet:** Authentifizierung beantwortet „wer bist du?", Autorisierung beantwortet „was darfst du?". Wer beides vermischt, hat am Ende korrekt angemeldete Nutzende mit viel zu weitreichenden Rechten.

---

## 4 · Menschliche Kontrollen — die Seilschaft

> *Sichern heißt nicht danebenstehen. Es heißt: rechtzeitig merken, dass etwas nicht stimmt.*

**Leitfrage: Wer sichert — und merkt er es rechtzeitig?**

*Normbezug: EU AI Act Art. 14 · ISO/IEC 42001 Kl. 5.1 · IMDA (Human Accountability)*

- **Gibt es zu jedem Datenbestand einen Datenvertrag — Struktur, Bedeutung, Zusagen, Verantwortung?**
  Das häufigste Integrationsproblem ist organisatorisch: Ein Feld ändert sich, und drei Wochen später liefert ein Modell stillschweigend Unsinn.
- **Ist festgelegt, an welchen Punkten ein Mensch freigeben muss, bevor es weitergeht?**
  Die IMDA empfiehlt menschliche Freigabe an bedeutsamen Kontrollpunkten — und die Prüfung, ob diese Freigaben wirksam sind.
- **Ist jede irreversible Aktion an eine ausdrückliche Freigabe gebunden?**
  Umkehrbar oder nicht — das ist die Trennlinie, nicht „wichtig oder unwichtig".
- **Messen wir, wie oft Menschen die KI-Empfehlung tatsächlich verwerfen?**
  Die IMDA nennt Override-Rate und Reaktionszeit ausdrücklich als Mittel gegen Automation Bias. Eine Quote nahe null ist genauso verdächtig wie eine sehr hohe.
- **Gibt es einen Eskalationsweg, der auch dann funktioniert, wenn es unbequem wird?**
  Ein Eskalationspfad, der über die Person führt, deren Projekt gestoppt würde, ist keiner.
- **Können die Beteiligten die Ergebnisse so weit erklären, dass sie sie verantworten können?**
  Wer eine Entscheidung freigibt, die er nicht erklären kann, hat nicht entschieden, sondern durchgewinkt.

> **Bergsteigerregel:** Der Sichernde schaut nicht auf die Aussicht.

---

## 5 · Technische Kontrollen — die Fixseile

> *Fixseile halten auch dann, wenn niemand zuschaut. Genau deshalb gibt es sie.*

**Leitfrage: Was schützt die Daten, wenn niemand hinsieht?**

*Normbezug: DSGVO Art. 25 & 32 · EU AI Act Art. 15 · ISO/IEC 42001 Kl. 8.6*

- **Sind Daten bei Übertragung und Speicherung verschlüsselt?**
  Die Grundlage, die am häufigsten stillschweigend vorausgesetzt wird.
- **Werden personenbezogene Daten anonymisiert oder pseudonymisiert, wo der Zweck es zulässt?**
  Der beste Schutz ist, die Daten gar nicht zu haben.
- **Ist der Speicherort bekannt und mit den rechtlichen Anforderungen vereinbar?**
  Datenresidenz entscheidet über anwendbares Recht und mögliche Zugriffe Dritter.
- **Laufen automatische Qualitätsprüfungen auf den eingehenden Daten?**
  Regelbasiert prüft, was du vorgibst. Musterlernend meldet Abweichungen vom Normalzustand. Beides schlägt „fällt schon jemandem auf".
- **Sind Systeme so abgeschottet, dass ein Fehler nicht sofort alles betrifft?**
  Testumgebungen, getrennte Mandanten, begrenzte Wirkungsräume — Schadensbegrenzung by Design.
- **Ist beim Werkzeugeinsatz auf Portierbarkeit geachtet — offene Formate, zugesicherter Export?**
  Seit dem EU Data Act (gilt ab 12.09.2025) ist Portabilität in weiten Teilen Rechtsanspruch; Wechselentgelte sind ab 12.01.2027 verboten.

---

## 6 · Der Umkehrpunkt — Betrieb & Notausstieg

> *Den Umkehrpunkt legt man vor dem Aufstieg fest — nicht oben, wenn das Gipfelfieber schon wirkt.*

**Leitfrage: Wann brechen wir ab — und wer entscheidet das?**

*Normbezug: EU AI Act Art. 72/73 · ISO/IEC 42001 Kl. 9 · DSGVO Art. 33*

- **Ist vorab und schriftlich festgelegt, bei welchen Werten das Vorhaben gestoppt wird?**
  Der stärkste Punkt dieser ganzen Liste. Wer das Abbruchkriterium erst im Ernstfall definiert, definiert es nie.
- **Wird überwacht, ob sich Daten oder Modellverhalten über die Zeit verschieben?**
  Drift kündigt sich in den Daten an, bevor sie im Ergebnis sichtbar wird.
- **Gibt es einen erprobten Weg zurück auf einen früheren Stand?**
  Ein Rückroll-Verfahren, das noch nie geübt wurde, ist eine Hoffnung, kein Verfahren.
- **Kann das System im Ernstfall schnell und vollständig abgeschaltet werden — und weiß jemand, wie?**
  Der Not-Aus muss auch dann funktionieren, wenn die Person, die ihn gebaut hat, im Urlaub ist.
- **Ist geregelt, wer Vorfälle wem in welcher Frist meldet?**
  Meldefristen laufen ab Kenntnisnahme, nicht ab dem Moment, in dem man sich einig geworden ist.
- **Gibt es ein Löschkonzept — und wird es tatsächlich ausgeführt?**
  Daten, die man nicht mehr hat, können nicht mehr abfließen.

> **Warum das die wichtigste Etappe ist:** Am Berg wie im Projekt wirkt dieselbe Psychologie — je näher der Gipfel, desto größer die Bereitschaft, Warnsignale wegzuerklären.

---

## 7 · Das Gipfelbuch — Nachweis

> *Wer sich nicht einträgt, war offiziell nicht oben.*

**Leitfrage: Können wir hinterher belegen, was wir getan haben — und warum?**

*Normbezug: EU AI Act Art. 12 & 17 · ISO/IEC 42001 Kl. 9 · DSGVO Art. 5 Abs. 2*

- **Werden Zugriffe, Änderungen und Entscheidungen unveränderlich protokolliert?**
  Ein Protokoll, das sich nachträglich ändern lässt, ist als Nachweis wertlos.
- **Lässt sich ein einzelnes Ergebnis bis zu seinen Eingangsdaten zurückverfolgen?**
  Das ist die eigentliche Prüfung jeder Datenarchitektur — und der Grund für getrennte Reifestufen.
- **Sind Datenquellen, Aufbereitung und getroffene Annahmen dokumentiert?**
  Annahmen, die nirgends stehen, gelten später als Fakten.
- **Ist geprüft, welche rechtlichen Anforderungen konkret gelten — und wer das verantwortet?**
  DSGVO, EU AI Act, Data Act, branchenspezifische Aufsicht: Die Kombination entscheidet.
- **Wird die Wirksamkeit regelmäßig überprüft — nicht nur einmal zur Einführung?**
  Einmalige Abnahme ist keine Governance.

---

## Der Rückweg — keine Einbahnstraße

Die IMDA beschreibt ihre Governance-Dimensionen ausdrücklich als **iterativen Prozess**: Wird bei der Umsetzung oder im laufenden Betrieb eine Auffälligkeit entdeckt, sollen die früheren Dimensionen erneut bewertet und die Risiken neu eingeschätzt werden.

Genauso funktioniert eine Tour: Wetterumschwung am Grat heißt Rückkehr ins Lager, nicht Weitergehen.

**Für die Grafik:** Rückpfeile vom *Umkehrpunkt* und von der *Seilschaft* zurück zur *Ausrüstung* und zum *Basislager*.

---

## Quellen & normative Anker

| Quelle | Einordnung |
|---|---|
| [DAMA-DMBOK (2. Aufl., Rev. 2024)](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/) | herstellerneutraler Datenmanagement-Fachstandard |
| [IMDA Singapur — Model AI Governance Framework for Agentic AI (v1.5, 2026)](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf) | behördliche Best-Practice-Guidance, in der EU nicht verbindlich |
| [EU Data Act — VO (EU) 2023/2854](https://eur-lex.europa.eu/eli/reg/2023/2854/oj?locale=de) | Rechtsakt (Tier 1), gilt seit 12.09.2025 |
| [EU AI Act — VO (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202401689) | Rechtsakt (Tier 1) |
| [Verizon — Data Breach Investigations Report 2026](https://www.verizon.com/business/resources/reports/dbir/) | Branchenbericht, breite Datenbasis, nicht begutachtet |
| [Data Contract Specification](https://datacontract.com/) | offener Community-Standard, kein Normcharakter |
| [Sambasivan et al. (2021) — Data Cascades, ACM CHI](https://dl.acm.org/doi/abs/10.1145/3411764.3445518) | einzige begutachtete Forschungsquelle dieser Übersicht |
| ISO/IEC 42001:2023 | KI-Managementsystem-Norm |
| DSGVO — VO (EU) 2016/679 | Rechtsakt (Tier 1) |

Die Artikelangaben sind Orientierungshilfen, keine Rechtsberatung. Diese Liste soll verhindern, dass etwas *vergessen* wird — ob es im Einzelfall *ausreicht*, beurteilen die zuständigen Fachfunktionen.

---

*Die Datenreise · Arbeitshilfe Datenmanagement, Datenqualität & Daten-Governance · Ulrich Nord · August 2026*
