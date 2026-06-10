# UC-01c: Rechtliche Grundlagen & EU AI Act

---

## Szenario

Das Bauplanungsbüro Dr. Seika hat das zugekaufte KI-System mit eigenen Kalkulationsdaten **fine-getuned**. Mit eigenen Projektdaten und Expertenschätzungen liefert das Modell jetzt automatisierte Preisvorschläge für Nachträge. Das System prüft nicht mehr nur Verträge — es kalkuliert Preise.

Das System funktioniert so gut, dass auf einer Branchenmesse drei Geschäftsführer befreundeter Bauplanungsbüros fragen: *„Können wir euer System auch nutzen? Wir würden 5000 € pro Monat zahlen."*

Die Geschäftsführung sieht eine zweite Einnahmequelle und plant, das Tool als **„Akies"** als SaaS-Angebot zu vermarkten — mit eigenem Namen, eigener Marke, monatlicher Abrechnung. Marco Brandt, der KI-Beauftragte, soll eine Empfehlung aussprechen.

---

## Lernziele

- Den Rollenwechsel von Betreiber zu Anbieter nach Art. 25 Abs. 1 EU AI Act erkennen und sicher begründen
- Den Unterschied zwischen lit. a (eigener Name in Verkehr bringen — eindeutig) und lit. b (wesentliche Veränderung — auslegungsbedürftig) verstehen
- Anbieterpflichten bei begrenztem Risiko benennen (Art. 50 Transparenz, Dokumentation, Vertragsgestaltung)
- Geschäftsmodell-Risiken bei einer KMU-SaaS-Vermarktung einschätzen
- Eskalationspunkte für den KI-Beauftragten identifizieren — und konkrete Empfehlungen an die Geschäftsführung formulieren

---

## Zwei Auslöser für den Rollenwechsel — Vergleich

```
Auslöser 1: Fine-Tuning (intern, ohne Vermarktung)
└── Art. 25 Abs. 1 lit. b — „wesentliche Veränderung"
    ├── Definitionsfrage: Wann ist eine Veränderung wesentlich?
    ├── Im Einzelfall auslegungsbedürftig — Anwälte streiten
    └── → Graubereich, im Zweifel Anwalt einschalten

Auslöser 2: Vermarktung als „Seika BauPrice" (SaaS)
└── Art. 25 Abs. 1 lit. a — „unter eigenem Namen in Verkehr bringen"
    ├── Klare Rechtslage: kein Auslegungsspielraum
    ├── Sobald Dritten angeboten → Anbieterstatus
    └── → Eindeutig: Dr. Seika wird Anbieter
```

---

## Diskussionsfragen

**Welche Rolle nimmt Dr. Seika nach dem Verkauf rechtlich ein?**

**Was ändert sich konkret durch den Anbieterstatus — bei einem System mit begrenztem Risiko?**

**Was empfiehlt der KI-Beauftragte der Geschäftsführung? Pro, Contra, alternative Modelle?**

**Was passiert, wenn ein Käufer das System für andere Zwecke einsetzt — z.B. für Personalentscheidungen?**

---

## Weiterführende Quellen

- EU AI Act Art. 25 (Rollenwechsel): https://artificialintelligenceact.eu/article/25/
- EU AI Act Art. 50 (Transparenzpflichten): https://artificialintelligenceact.eu/article/50/
- EU AI Act Anhang IV (Technische Dokumentation): https://artificialintelligenceact.eu/annex/4/
- GeschGehG: https://www.gesetze-im-internet.de/geschgehg/
- Rohrlich, *KI und Recht*, Hanser 2024, S. 164–167

---

## Analyse & Hinweise

### Einordnung

**KI-System-Typ:** Fine-tuned Commercial AI mit anschließender SaaS-Vermarktung
**Schwierigkeitsgrad:** Fortgeschrittene
**Parallelfall:** UC-02c (WellSeal SAP-Integration) — beide zeigen Rollenwechsel in verschiedenen Branchen

### Prüfdimensionen

| Dimension | Bewertung | Details |
|---|---|---|
| **Rollenwechsel — eindeutig** | Art. 25 Abs. 1 lit. a | „Unter eigenem Namen in Verkehr bringen" — keine Auslegung, keine Diskussion. SaaS-Verkauf = Anbieterstatus |
| **Rollenwechsel — Graubereich** | Art. 25 Abs. 1 lit. b | Fine-Tuning ohne Vermarktung: Ist das eine „wesentliche Veränderung"? Anwälte streiten. Im Zweifel Stufe 2 |
| **Anbieterpflichten bei begrenztem Risiko** | Art. 50, Doku, Verträge | Bei B2B-Preiskalkulation = begrenztes Risiko. Pflichten überschaubar — nicht CE/Konformitätsbewertung wie bei Hochrisiko |
| **Geschäftsgeheimnisse** | ⚠️ Hoch | AGB des Cloud-Anbieters: Werden Daten für Modelltraining genutzt? Was passiert mit den Käuferdaten? |
| **Bias / Datenqualität** | Art. 10 EU AI Act | Historische Kalkulationen können Verzerrungen enthalten — vor allem wenn das System auf andere Büros übertragen wird |
| **Halluzination bei Zahlen** | Kritisch | LLMs bei numerischen Ausgaben besonders fehleranfällig — relevant für Situation 3 (falscher Preis) |
| **Verwendungszweck-Drift** | ⚠️ Wichtig | Was, wenn Käufer das System für Personalentscheidungen einsetzt? → Anhang III Nr. 4 könnte greifen, neue Rolle für Käufer |

### Didaktische Hinweise

**Der zentrale Aha-Moment:** Vorher unterrichteten viele Materialien das Fine-Tuning als „klassischen" Auslöser für den Rollenwechsel. Das ist juristisch zu unscharf — Art. 25 Abs. 1 lit. b ist tatsächlich auslegungsbedürftig. Die SaaS-Vermarktung („Seika BauPrice") schafft einen **eindeutigen** Auslöser nach lit. a, an dem sich der Rollenwechsel didaktisch klar erklären lässt.

**KMU-Realismus mit guter Nachricht:** Anders als bei Hochrisiko-KI sind die Anbieterpflichten bei begrenztem Risiko für ein 15-Personen-Büro tatsächlich umsetzbar — Transparenzhinweise, technische Dokumentation für Käufer, klare Verträge. Das macht die SaaS-Idee nicht unmöglich, aber teurer als gedacht. Die spannende Frage ist wirtschaftlich: Lohnt sich das Geschäftsmodell bei 500 €/Monat × 3 Käufer × Compliance-Aufwand?

**Kontraststrategie:** UC-01a (Betreiber, klar) → UC-01c (Anbieter, klar) — gleiches Büro, gleiches Ausgangssystem, dramatisch unterschiedliche Compliance-Last. Das macht Art. 25 erfahrbar.

**Verbindung zu Air Canada:** Wenn ein Käufer von „Akies" einen falschen Preis erhält und den Schaden bei Dr. Seika geltend macht — wer haftet? Genau die Air-Canada-Logik. Dr. Seika kann sich nicht damit herausreden, dass „die KI" das gesagt habe.

---

**Empfohlene Diskussionsführung**

**Schritt 1 — Eindeutigkeit etablieren:**
Bevor inhaltlich über Pro/Contra des Geschäftsmodells gesprochen wird: Klären, dass der Rollenwechsel hier *nicht zur Diskussion steht*. Sobald Dr. Seika SaaS verkauft, ist Dr. Seika Anbieter. Das ist Tatsache, nicht Meinung.

**Schritt 2 — Konsequenzen sortieren:**
Was kommt auf Dr. Seika zu?
- Transparenzpflicht (Art. 50): Käufer und Endnutzer müssen wissen, dass es sich um KI handelt
- Technische Dokumentation: Was kann das System, was nicht? Welche Trainingsdaten? Welche bekannten Grenzen?
- Vertragsgestaltung: Vorgesehener Zweck, Verbot bestimmter Anwendungen, Haftungsbegrenzung, Update-Verpflichtungen
- Post-Market-Monitoring: Wie reagiert Dr. Seika, wenn ein Käufer Probleme meldet?

**Schritt 3 — Geschäftsmodell hinterfragen:**
3 Käufer × 500 € = 1.500 €/Monat. Was kostet die laufende Compliance? Was kostet einmalig die Aufsetzung (Anwalt, Dokumentation, AGB)? Wann lohnt sich das? Antwort meist: Bei 3 Käufern selten — bei 30 Käufern ja.

**Schritt 4 — Alternativen aufzeigen:**
- Lizenz an EIN befreundetes Büro statt SaaS — weniger Compliance-Aufwand
- Kooperation/Beratung statt Tool-Verkauf — Wissen weitergeben, nicht das System
- Eigenes Tool aufgeben, gemeinsam mit anderen ein professionelles Tool kaufen

---

**Empfohlener Eskalationsweg für Marco**

**Stufe 1** (KI-BA entscheidet selbst):
- Das Geschäftsmodell strukturieren — Pro/Contra-Analyse, Zahlen aufstellen
- Vorgesehenen Verwendungszweck klar definieren
- Erste Vertragsklauseln-Skizze

**Stufe 2** (KI-BA bereitet auf, GF entscheidet, ggf. Anwalt):
- Anwalt mit AI-Act-Expertise einschalten — vor Vertragsabschluss
- Geschäftsmodell durchrechnen mit Compliance-Aufwand
- Entscheidung über Geschäftsmodell

**Stufe 3** (immer Anwalt):
- Vertragsverhandlungen mit ersten Käufern
- Falls später ein Schadensfall eintritt (siehe Situation 3 GA)

### Verbindungen im Curriculum

- **Voraussetzungen:** UC-01a (Betreiber, Tag 1+3), UC-01b (Personalplanung, Tag 3)
- **Theorieblock:** EU AI Act Akteursrollen (Tag 4), Art. 25 Rollenübergang (Tag 4)
- **Praktische Übung:** Gruppenarbeit Tag 4 — Situation 1 nutzt diesen Use Case direkt
- **Vorausblick:** Tag 5 vertieft die Risikoklassen weiter (Anhang III) am Krankenhaus-Beispiel UC-03
