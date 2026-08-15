# UC-07 · Vermano AG und Tecnoval S.p.A. — Kontext und Aufgabenpaket
> ⚠️ Fiktive Unternehmen — alle Namen, Kennzahlen und Personen sind für Schulungszwecke erstellt und dienen ausschließlich der Lehre.

---

## 1 · Die Ausgangslage

Am **1. Juli 2026** ist der Kauf vollzogen: Die **Vermano AG** hat ihren wichtigsten europäischen Wettbewerber übernommen, die **Tecnoval S.p.A.** Beide Häuser erbringen technischen Service und Instandhaltung für Industrieanlagen — Chemie, Papier, Energie, Wasserwirtschaft. Beide leben davon, dass ihre Technikerinnen und Techniker vor Ort sind, wenn eine Anlage steht.

Der Vorstand hat das Ziel in einer Formel ausgegeben: **1 + 1 > 2.** Konkret bedeutet das **18 Mio. € jährliche Synergien ab dem dritten Jahr**. Der Integrationsplan soll bis zum **30. Juni 2027** umgesetzt sein.

Du bist **KI-Manager:in der Vermano AG** und sollst den Integrationsplan aus Sicht des KI-Managements verantworten. Du berichtest an den Chief Operating Officer.

---

## 2 · Die beiden Häuser

| | **Vermano AG** | **Tecnoval S.p.A.** |
|---|---|---|
| Sitz | Dortmund | Bologna |
| Gegründet | 1978 | 1994 |
| Mitarbeitende | ca. 2.400 | ca. 1.600 |
| Jahresumsatz | ca. 410 Mio. € | ca. 260 Mio. € |
| Märkte | Deutschland, Österreich, Benelux, Polen | Italien, Spanien, Portugal |
| Eigentum bisher | börsennotiert, Streubesitz 60 % | inhabergeführt, ein Gesellschafter |
| Kernsystem | SAP-basiert, seit 2011 | eigenentwickelt, seit 2016 |
| Arbeitssprachen | Deutsch, Englisch, Polnisch | Italienisch, Spanisch, Englisch |

**Was beide gemeinsam haben:** Ein Techniker fährt raus, prüft eine Anlage, schreibt einen Servicebericht, empfiehlt Maßnahmen und Ersatzteile. Aus dem Bericht entsteht ein Angebot. Bei Vermano dauert das im Schnitt **elf Tage**, bei Tecnoval **vier**.

---

## 3 · Personen

### Du — KI-Manager:in der Vermano AG
Seit zwei Jahren im Haus, Berichtsweg an den COO. Du hast die KI-Governance der Vermano aufgebaut — und weißt, dass sie bisher wenig zu steuern hatte.

### Dr. Andrea Wolters — Vorstandsvorsitzende Vermano
57 Jahre. Hat den Kauf durchgesetzt und verteidigt ihn öffentlich. Möchte im Geschäftsbericht sichtbare Fortschritte zeigen, bevor die Synergien tatsächlich anfallen.

### Jens Röttger — Finanzvorstand Vermano
51 Jahre. Kennt jeden Vertrag. Hat die 18 Mio. € in die Investorenkommunikation geschrieben und wird daran gemessen. Fragt bei jedem Vorschlag zuerst nach der Laufzeit bestehender Verträge.

### Marco Bassi — Gründer und bisheriger Geschäftsführer Tecnoval
62 Jahre. Bleibt für **18 Monate als Berater** an Bord. Stolz auf das, was sein Haus technisch aufgebaut hat, und misstrauisch gegenüber deutschen Freigabeprozessen. Sein Satz in der ersten gemeinsamen Sitzung: *„Wir haben sieben Anwendungen im Einsatz. Ihr habt elf in einer Tabelle.“*

### Elena Ferri — IT-Leiterin Tecnoval
39 Jahre. Hat die sieben Anwendungen möglich gemacht, meist indem sie Fachbereiche selbst beschaffen ließ und hinterher integrierte. Weiß genau, wo die Leichen liegen, und sagt es auch — wenn man sie fragt.

### Karsten Oel — Betriebsratsvorsitzender Vermano
Hat der KI-Governance 2024 zugestimmt, weil sie Mitbestimmung vorsah. Beobachtet die Übernahme aufmerksam und hat bereits angekündigt, jede Ausweitung italienischer Werkzeuge auf deutsche Standorte zu prüfen.

### Beatrice Lombardi — Leiterin Servicedisposition Tecnoval
44 Jahre. Ihre Disponentinnen arbeiten seit zwei Jahren mit der Ersatzteilprognose und vertrauen ihr. Sie hält die deutsche Terminplanung für rückständig und sagt das freundlich, aber oft.

---

## 4 · Die KI-Landschaft — und ihre Unsymmetrie

Das eigentliche Problem der Fusion ist nicht, dass die beiden Häuser unterschiedlich weit sind. Es ist, dass sie **in entgegengesetzte Richtungen** unterschiedlich weit sind.

### Vermano — Steuerung ohne viel zu steuern

- **KI-Board** seit 2024, tagt quartalsweise, entscheidet über Freigaben
- **Inventar** mit 11 Einträgen, davon 2 produktiv, 4 als Pilot gestoppt, 5 als Idee erfasst
- **Freigabeprozess** mit Risikoeinstufung, Datenschutz-Folgenabschätzung und Betriebsratsbeteiligung
- Produktiv im Einsatz: ein **Angebotsassistent** im Vertriebsinnendienst und eine **Rechnungsprüfung** in der Buchhaltung

### Tecnoval — Einsatz ohne Steuerung

Sieben Anwendungen laufen produktiv. Ein Inventar gibt es nicht; die Liste unten hat Elena Ferri auf Nachfrage in zwei Tagen zusammengestellt.

| Anwendung | Was sie tut | Beschafft von | Bemerkung |
|---|---|---|---|
| **Serviceberichte per Sprache** | Technikerinnen diktieren unterwegs, das System schreibt und strukturiert | Servicebereich, 2024 | Aufnahmen enthalten Gespräche mit Kundenpersonal |
| **Ersatzteilprognose** | Sagt Bedarf je Anlagentyp und Region voraus | Disposition, 2023 | Eigenentwicklung, gepflegt von **einer** Person |
| **Angebotsgenerator** | Erzeugt aus dem Bericht einen Angebotsentwurf | Vertrieb, 2024 | Grund für die vier statt elf Tage |
| **Einsatzplanung** | Verteilt Aufträge auf Technikerinnen und Routen | Disposition, 2025 | Bewertet indirekt die Auslastung Einzelner |
| **Übersetzung** | Berichte und Angebote zwischen drei Sprachen | IT, 2023 | Frei zugänglicher Dienst, kein Vertrag |
| **Kundenportal-Chat** | Beantwortet Statusfragen zu laufenden Aufträgen | Vertrieb, 2025 | Keine Kennzeichnung als maschinelles System |
| **Anlagenfotos** | Erkennt Bauteile und Schäden auf Fotos der Technikerinnen | Servicebereich, 2025 | Trainiert auf Kundenanlagen; Rechtelage ungeklärt |

**Keine dieser sieben Anwendungen hat eine dokumentierte Risikoeinstufung.** Vier davon wären nach dem Freigabeprozess der Vermano zustimmungspflichtig gewesen.

---

## 5 · Überschneidungen bei Werkzeugen und Verträgen

Für zwei Aufgaben haben beide Häuser bereits eine Lösung — mit sehr unterschiedlichen Verträgen.

| Aufgabe | Vermano | Tecnoval |
|---|---|---|
| **Angebotserstellung** | Anbieter A · 340 Plätze · **212.000 € pro Jahr** · Laufzeit bis 31.12.2028 · vorzeitiger Ausstieg nur gegen 60 % der Restlaufzeit | Anbieter B · mengenbasiert · 2025: **96.000 €** · jährlich kündbar · Verbrauch 2026 bereits +40 % |
| **Rechnungsprüfung** | Anbieter C · im Kernsystem enthalten | keine |
| **Ersatzteilprognose** | keine | Eigenentwicklung, keine Lizenzkosten, **kein zweiter Kenner** |

Dazu kommt der Datenschnitt: Die Servicedaten liegen in zwei getrennten Kernsystemen, in vier Sprachen und mit unterschiedlichen Anlagenschlüsseln. Eine gemeinsame Auswertung gibt es nicht.

---

## 6 · Das Entscheidungsfeld

Sechs Richtungsentscheidungen liegen auf deinem Tisch. Keine davon ist rein technisch, und keine lässt sich vertagen, ohne dass sie an anderer Stelle entschieden wird.

1. **Welches Portfolio bleibt?** Zusammenlegen, nebeneinander weiterlaufen lassen oder eine Seite abschalten — und nach welchem Maßstab entscheidest du das?
2. **Welches Betriebsmodell trägt nach der Fusion?** Zentral, dezentral oder föderiert. Die bisherige Vermano-Governance ist zentral gebaut und hatte zwei Anwendungen zu steuern. Jetzt sind es neun.
3. **Was passiert mit den sieben ungeprüften Anwendungen?** Sofort stilllegen, weiterlaufen lassen und nachträglich einstufen, oder einzeln entscheiden? Jede Antwort hat einen Preis: Stillstand, Rechtsrisiko oder Glaubwürdigkeitsverlust der eigenen Regeln.
4. **Welcher Anbieter bei der Angebotserstellung?** Der teurere mit Bindung bis 2028 oder der billigere mit stark steigendem Verbrauch — und was kostet der Ausstieg jeweils wirklich?
5. **Wie behandelst du die Sprachaufnahmen?** In den Aufnahmen sind Gespräche mit Kundenpersonal. Die Einsatzplanung bewertet mittelbar die Leistung Einzelner. Beides berührt Mitbestimmung, und die Rechtslage ist in Deutschland und Italien nicht dieselbe.
6. **In welcher Reihenfolge?** Erst die Governance ausrollen und damit den schnelleren Partner ausbremsen — oder erst die Anwendungen absichern und die Regeln nachziehen?

---

## 7 · Didaktischer Rahmen

Der Fall eignet sich für Themenfelder, in denen **Richtungsentscheidungen** verlangt sind und nicht Optimierung im Bestand:

- **KI-Strategie und Portfolio** — Bewertung, Priorisierung, bewusstes Beenden
- **Governance-Strukturen** — Betriebsmodell, Gremien, Freigabewege unter Skalierungsdruck
- **Beschaffung und Anbieterbindung** — Vertragslaufzeiten, Ausstiegskosten, Abhängigkeit
- **Risikoarten und Freigabe** — nachträgliche Einstufung eines gewachsenen Bestands
- **Organisation und Veränderung** — Mitbestimmung, zwei Rechtsräume, ein übernommenes Haus, das sich als das fortschrittlichere erlebt
- **Reifegradbestimmung** — und die Frage, warum ein eindimensionales Modell hier zum falschen Ergebnis führt

**Die Falle, die der Fall stellt:** Wer nur den Einsatzgrad misst, erklärt Tecnoval zum reiferen Haus. Wer nur die Steuerung misst, erklärt Vermano zum reiferen. Beides ist falsch, und beide Fehler haben in der Integration unterschiedliche, aber gleich teure Folgen.

---

## 8 · Marktkontext

Zwei belastbare Bezugspunkte für die Diskussion, beide mit dem Vorbehalt, dass es sich um Veröffentlichungen von Beratungshäusern mit eigenem Geschäftsinteresse handelt:

- Die **10-20-70-Regel** — rund 10 % des Aufwands entfallen auf Algorithmen, 20 % auf Daten und Technik, 70 % auf Menschen, Prozesse und Kultur. Für einen Integrationsfall ist das die zentrale Erwartungskorrektur. [BCG — From Potential to Profit](https://www.bcg.com/publications/2025/closing-the-ai-impact-gap)
- Organisationen mit messbarem Ergebnisbeitrag aus KI haben **rund dreimal so häufig einzelne Arbeitsabläufe grundlegend neu zugeschnitten**, statt KI in bestehende einzusetzen. [McKinsey — The state of AI](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)

---

*Letzte Aktualisierung: August 2026 — Ulrich Nord / Claudia*
