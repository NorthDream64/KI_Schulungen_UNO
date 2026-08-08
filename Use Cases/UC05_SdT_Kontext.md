# UC-05 · Sammel Deinen Traum (SdT GmbH) — Kontext und Aufgabenpaket

> ⚠️ Fiktives Unternehmen — alle Namen, Kennzahlen und Personen sind für Schulungszwecke erstellt und dienen ausschließlich der Lehre. Vorbild und Inspiration ist das reale Auktionshaus Heritage Auctions, Dallas (<https://www.ha.com/>); die dort öffentlich einsehbaren Auktionsarchive (<https://www.ha.com/c/ref/information-archive.zx>) zeigen, wie eine solche Datenbasis in der Praxis aussieht.

---

## 1 · Das Unternehmen

Du hast Dir mit zwei Freunden einen Traum erfüllt und Dein Hobby zum Beruf gemacht. Seit Jahren habt Ihr sogenannte **„Collectibles"** selbst gesammelt — Fußballbilder, Comics, Musikalben, Memorabilia. Dann habt Ihr Stücke von anderen Sammlern in Kommission genommen und verkauft, schließlich eine regelmäßige Online-Auktion eingerichtet. Auf Eurer Webseite versteigert Ihr **zweimal täglich**. Die Preise reichen von wenigen Euro für ein Comic-Heft bis zu vielen Tausend Euro, etwa für eine Originalgitarre von Bob Dylan.

**Kennzahlen (Geschäftsjahr 2025)**

| | |
|---|---|
| Gegründet | 2020, Sitz Berlin |
| Mitarbeitende | 34 fest, saisonal bis zu 20 Aushilfen (überwiegend Studierende) |
| Standorte | Büro Berlin - Chalottenburg, Hauptlager Berlin - Spandau, Kleinlager Falkensee |
| Lose pro Jahr | ca. 62.000 |
| Hammerpreisvolumen | ca. 41 Mio. EUR |
| Durchschnittlicher Zuschlag | 660 EUR (Median 95 EUR — die Verteilung ist extrem schief) |
| Nicht verkaufte Lose | 18 % (werden meist wieder eingestellt) |

**Märkte.** In den ersten Jahren wart Ihr nur in Deutschland tätig. Heute reicht Euer Kundenkreis über die gesamte EU (Schwerpunkte Belgien, Frankreich, Spanien), Großbritannien und die USA, vereinzelt bis Japan und Südkorea. In den USA habt Ihr enge Geschäftsverbindungen zur Firma **Heritage Auctions** (<https://www.ha.com/>).

**Bestehende Systeme.** Microsoft 365 (Teams, SharePoint, Outlook — solide genutzt), eine selbst entwickelte Auktionsplattform auf Basis eines PHP-Shopsystems, DATEV für die Buchhaltung, ein Lagerverwaltungsmodul, das ein ehemaliger Werkstudent gebaut hat. Eure KI würde aller Voraussicht nach auf **Azure** betrieben werden.

**Kostenstruktur.** Lager- und Versicherungskosten sind ein bedeutender Kostenblock. Ihr wollt keine zu teuren Stücke zu lange im Regal haben, weil sie sich nicht verkaufen.

---

## 2 · Personen

### Du — Geschäftsführung Finanzen, Personal und Technik
Du bist kein Techniker, und Deine Kolleginnen und Kollegen sind es noch weniger. Was Du vorschlägst, muss klar, verständlich, möglichst in Bildern und „business-like" kommuniziert werden. Du hast das Thema KI übernommen, weil es niemand sonst tut.

### Karl — Geschäftsführung Ankauf und Bewertung
Bewertet die Stücke und verhandelt mit den Einlieferern. Vertraut oft seinem Instinkt und ist überzeugt, dass sich seine Trefferquote mit KI und Machine Learning schlagen lässt: Bestimmte Collectibles steigen abhängig von Alterskohorten im Preis, weil Menschen Mitte 30 Sammlungen wieder aufnehmen, die sie als Jugendliche begonnen haben („Pokémon-Effekt"). Karl ist der lauteste Befürworter — und derjenige, der die Grenzen der Technik am wenigsten sieht.

### Vasili — Geschäftsführung Logistik
Transport, Einlagerung, Versand. Skeptisch gegenüber allem, was zusätzliche Arbeitsschritte im Lager erzeugt. Sein Einwand: „Jedes Foto, das Ihr zusätzlich haben wollt, kostet mich 40 Sekunden pro Stück — mal 62.000."

### Nadine Beckmann — externe Beraterin
Hat mit Euch und fünf Teamleitern in zwei Workshops die Use-Case-Liste erarbeitet und priorisiert. Sie ist Wirtschaftsinformatikerin, keine Data Scientist. Ihr Mandat endet mit der Übergabe der Liste.

### Eure IT-Unterstützung
Eine örtliche IT-Beratung, die Euch seit Jahren zuverlässig betreut — aber kaum KI-Erfahrung und keine internationale Expertise besitzt.

---

## 3 · Eure Datenlage

Ihr habt in elf Jahren ein Archiv aufgebaut, das Euch niemand nachmacht: **rund 380.000 abgeschlossene Lose** mit Fotos, Beschreibungstexten, Kategorien, Kommissionspreis, Startpreis, Bietverlauf und Zuschlagspreis. Das ist Euer eigentlicher Vermögenswert.

Es ist allerdings über elf Jahre gewachsen, nicht geplant worden:

- **Fotos.** Von 2015 bis 2018 mit dem Privathandy wechselnder Mitarbeitender aufgenommen — unterschiedliche Hintergründe, Beleuchtung, Auflösung. 2019 bis 2020 mit einer Spiegelreflexkamera auf grauem Karton. Seit 2021 in einer Fotobox mit standardisiertem weißem Hintergrund und Ringlicht.
- **Zustandsangaben.** Erst seit 2019 in einem strukturierten Feld (Skala 1–10). Davor Freitext im Beschreibungstext oder gar nicht erfasst — rund 40 % der Altbestände haben keine verwertbare Zustandsangabe.
- **Kategorien.** Von wechselnden Aushilfen gepflegt. Im Archiv finden sich nebeneinander „Comics", „Comic", „Hefte", „US-Comic" und „Comicheft" für dieselbe Warengruppe.
- **Währungen.** Zuschläge sind in der Währung des Käufers gespeichert (EUR, USD, GBP). Der Wechselkurs zum Zuschlagstag wurde nicht mitgespeichert; nachträglich umgerechnet wird zum Monatsmittel.
- **Dubletten.** Unverkaufte Lose werden in der Folgeauktion als **neues Los** angelegt. Ein Stück, das viermal durchgelaufen ist, steht viermal im Archiv — mit vier unterschiedlichen Startpreisen und einem einzigen echten Verkauf.
- **Zuordnung Bild zu Los.** Die Fotos liegen in SharePoint-Ordnern nach Auktionsnummer, nicht mit der Los-ID verknüpft. Die Zuordnung erfolgt über eine Dateinamens-Konvention, die 2019 einmal geändert wurde. Für etwa 9 % der Altbestände ist die Zuordnung unsicher.
- **Beschreibungstexte.** Enthalten häufig bereits eine Schätzung („Schätzpreis 400–600 EUR", „Zustand sehr gut, vergleichbares Stück erzielte 2022 über 1.200 EUR").

Externe Daten habt Ihr bisher nicht systematisch angebunden: Preise von Vergleichsplattformen zieht Karl manuell, wenn er unsicher ist.

---

## 4 · Das Use-Case-Portfolio

Ihr habt zusammen mit einer Beratung folgende Vorschläge zusammengetragen. Sie stehen unterschiedlich reif und unterschiedlich gut belegt nebeneinander.

### A · Wertermittlung — die Kernanwendung

**A1 · Abschätzung der voraussichtlichen Verkaufspreise.**
Je besser der mögliche Erlös in einer Auktion abgeschätzt werden kann, desto attraktiver kann der Mindestpreis sein, zu dem Ihr ein Stück in Kommission nehmt — und desto seltener bleibt teure Ware im Regal liegen. Datengrundlage ist Euer Archiv: Kommissionspreis, Startpreis, Zuschlag, Kategorie, Zustand, Saison, Käuferregion. Dies ist der Fall, an dem Karl hängt.

**A2 · Visuelle Ähnlichkeitssuche: „Zeig mir vergleichbare Lose".**
Bevor man einen Preis schätzen kann, braucht man Vergleichsstücke. Ein Bild eines eingelieferten Objekts wird in einen numerischen Merkmalsvektor („Embedding") übersetzt und gegen die Vektoren aller 380.000 Archivbilder verglichen. Ergebnis: die zehn ähnlichsten je verkauften Stücke samt erzielter Preise. Ein solches Verfahren muss nicht trainiert werden — es lässt sich mit fertigen Modellen und einer Vektorsuche im Azure-Umfeld aufbauen. Dieselbe Technik trägt eine Empfehlungsfunktion für Bieter („Sammler, die dieses Los beobachtet haben, …").

### B · Ware und Vertrauen

**B1 · Automatische Katalogisierung und Zustandsvorbewertung aus Fotos.**
Ein Foto aus der Fotobox soll erkennen, um welche Objektart, Serie und welches Erscheinungsjahr es sich handelt, einen Beschreibungsentwurf erzeugen und eine **Zustandsvorbewertung** vorschlagen — Zentrierung, Ecken, Kanten, Oberfläche. Für Sammelkarten ist genau das kommerziell verfügbar (siehe <https://agscard.com/> und <https://www.ximilar.com/services/visual-ai-for-collectibles/>); auch Auktionsplattformen bieten inzwischen automatische Katalogisierung an (<https://www.bidsquarecloud.com/blog/how-ai-is-transforming-auction-house-operations/>). Für Euren gemischten Bestand ist offen, wie weit sich das übertragen lässt.

**B2 · Fälschungs- und Autogrammprüfung.**
Der Markt für Collectibles ist massiv von Fälschungen betroffen. Der Grading-Dienstleister PSA berichtet für 2025, über 200 Mio. USD an gefälschten oder manipulierten Stücken abgefangen zu haben, bei einem Anstieg der Fälschungseinreichungen um 45,3 % (<https://www.sportscollectorsdaily.com/psa-report-details-increasing-card-counterfeit-attempts/>). Für die Prüfung von Unterschriften auf Memorabilia gibt es einen etablierten Forschungsstand: Zwei Signaturbilder werden von einem sogenannten Siamese Network direkt miteinander verglichen (<https://arxiv.org/pdf/2311.05579>). Die Besonderheit dieses Falls: Die Gegenseite lernt mit — bessere Drucktechnik und generative Bildmodelle verbessern auch die Fälschungen.

**B3 · Provenienz-, Sanktions- und Geldwäscheprüfung.**
Bei hochpreisigen Einlieferungen müsst Ihr wissen, woher ein Stück kommt und wer es einliefert. Interpol betreibt die einzige globale Datenbank zu gestohlenen Kulturgütern mit über 52.000 Objekten aus 134 Ländern; die zugehörige App ID-Art nutzt Bilderkennung für den Abgleich, und die Zeitstempel gespeicherter Suchen können als Nachweis der Sorgfaltspflicht dienen (<https://www.interpol.int/en/Crimes/Cultural-heritage-crime/ID-Art-mobile-app>). Parallel dazu zieht sich der Regulierungsrahmen an: Die EU-Geldwäscheverordnung (EU) 2024/1624 gilt ab dem **10. Juli 2027** unmittelbar in allen Mitgliedstaaten und zählt unter anderem Händler mit hochwertigen Gütern zu den Verpflichteten (<https://eur-lex.europa.eu/eli/reg/2024/1624/oj/eng>, Zusammenfassung: <https://eur-lex.europa.eu/EN/legal-content/summary/preventing-abuse-of-the-financial-system-for-money-laundering-and-terrorism-purposes-from-2027.html>). Für den Kunst- und Sammlermarkt wird üblicherweise ein Schwellenwert von 10.000 EUR je Transaktion oder Transaktionskette genannt. Ob und ab wann Euer Sortiment darunter fällt, ist eine offene Frage, die Ihr klären müsst — Ihr versteigert vom 8-Euro-Comic bis zur Gitarre für 40.000 EUR.

**B4 · Erkennung manipulativer Bietmuster.**
Bei zwei Auktionen täglich fallen Bietverläufe in großer Zahl an. „Shill Bidding" — das Hochtreiben des Preises durch Scheinbieter im Umfeld des Einlieferers — ist in der Forschung ein gut untersuchtes Erkennungsproblem, das mit Verfahren wie Random Forests und Support Vector Machines angegangen wird (<https://link.springer.com/chapter/10.1007/978-3-319-92058-0_29>). Der Reiz für Euch: Hier gibt es weder Bilder noch Texte, sondern nur Verhaltensdaten — und keine gesicherten Beispiele, weil niemand weiß, welche Gebote in der Vergangenheit manipuliert waren.

### C · Back-Office

**C1 · Automatisierte Einbuchung von Rechnungen und Belegen.**
Texterkennung, Plausibilitäts- und Betrugsprüfung, Kontierung, Berechnung der Wechselkurse. Ein großer Teil davon ist regelbasiert lösbar und braucht gar kein lernendes System.

**C2 · Scannen einschlägiger Sammlerforen in sozialen Medien.**
Sowohl Eure Kunden als auch die Leute, von denen Ihr Collectibles kauft, sind häufig auf Facebook oder Instagram unterwegs, aber auch in exotischen Foren und Chatgruppen. Ihr geht davon aus, dass die Teilnehmenden kein Problem damit haben werden, wenn Ihr als „stille Zuhörer" ihren Austausch mitbekommt — die Foren sind öffentlich, beziehungsweise Ihr seid privat ohnehin schon Mitglied in den wichtigsten. Eine fachliche Meinung dazu habt Ihr Euch noch nicht eingeholt.

### D · Weitere Vorschläge aus dem Team (unpriorisiert)

**D1 · Onboarding neuer Mitarbeitender.** Gerade in den Lagern arbeiten viele Teilzeitkräfte, etwa Studierende, die nur ein paar Ferienwochen für SdT tätig sind und rasch Informationen über Arbeitszeiten, Versicherung, Krankmeldung und Arbeitssicherheit brauchen. Für den Einstellungsprozess habt Ihr Euch <https://aws.amazon.com/de/products/connect/talent/> als Beispiel angesehen.

**D2 · Projektmanagement-Assistent.** Ihr habt viele Projekte, vor allem vermeintlich agile, die immer wieder nach eigenen Regeln und ohne planbaren Erfolg ablaufen. Ein Sprachmodell soll feste Standards für Statusberichte, Phasenpläne und Dokumentation verankern und internen wie externen Projektmitarbeitenden als Bot zur Verfügung stehen.

---

## 5 · Didaktischer Rahmen

Didaktisch aufbereitet warden sollen:

Datenmanagement · Tool-Einsatz · Datenaufbereitung · Datenqualität · Datenintegration · MLOps-Konzepte · KI-Automatisierung im Betrieb · Training und Validierung von Modellen · Testverfahren · Monitoring · Integration von KI-Agenten in Projekte

Dabei gilt:

1. **Adressatengerecht.** Karl und Vasili sind keine Techniker. Was sie nicht in einem Bild verstehen, verstehen sie nicht.
2. **Ehrlich zur Datenlage.** Chris Ivy, Leiter der Sport-Auktionen bei Heritage Auctions, formuliert die Grundregel so: Damit Machine Learning sinnvoll hilft, braucht es Qualitäts-Inputs — sonst gilt „garbage in, garbage out" (<https://www.cllct.com/sports-collectibles/memorabilia/the-year-in-collectibles-how-will-ai-impact-the-hobby>).
3. **Begründet priorisiert.** Nicht alles gleichzeitig. Welcher Fall zuerst, und woran messt Ihr, ob er funktioniert hat?
4. **Mit Betriebsperspektive.** Wer betreut das Modell in zwei Jahren, wenn der Werkstudent weg ist?

| Tag | Thema | Anknüpfungspunkte im Fall |
|---|---|---|
| **T06** | Datenmanagement & Datenqualität | Abschnitt 3 vollständig — jeder Aufzählungspunkt bildet eine Qualitätsdimension ab (Vollständigkeit: Zustandsangaben vor 2019; Konsistenz: Kategoriebezeichnungen und Währungen; Eindeutigkeit: Dubletten durch Wiedereinlieferung; Zugänglichkeit: Bild-Los-Zuordnung). Einstieg über das Ivy-Zitat. |
| **T07** | Tool-Einsatz & Datenintegration | A2 als Make-or-Buy-Beispiel: Embeddings und Vektorsuche erfordern kein eigenes Training. B1 als Gegenbeispiel: Zukaufbare Dienste decken Sammelkarten ab, nicht den gemischten Bestand. Anbindung DATEV / Eigenplattform / M365 / Azure. |
| **T08** | MLOps-Konzepte & KI-Automatisierung | C1 als Kontrast klassische Automatisierung (RPA) gegen KI. Betreiberfrage aus Abschnitt 5 Punkt 4. Vasilis 40-Sekunden-Einwand als Prozesskostenrechnung. |
| **T09** | Training, Validierung & Testverfahren | **Kernstunde.** Drei Fallen stecken bewusst im Material: (a) Die Beschreibungstexte enthalten bereits Schätzpreise — wer sie als Eingabe für A1 nutzt, hat das Ziel in den Eingangsdaten (Data Leakage). (b) Die Foto-Historie korreliert mit dem Aufnahmejahr — ein Modell kann über den Hintergrund auf das Jahr und darüber auf das Preisniveau schließen, ohne das Objekt zu erkennen (Confounder/Shortcut Learning). (c) Bei B1 ist die Referenz eine menschliche Zustandsbewertung, die selbst nicht reproduzierbar ist — Diskussion: Was heißt „richtig", wenn das Label verrauscht ist? B4 liefert das Beispiel für stark unbalancierte Daten ohne gesicherte Beispiele. Karls „Pokémon-Effekt" ist der Aufhänger für Overfitting. |
| **T10** | Monitoring, Model Drift & KI-Agenten | B2 zeigt Drift, die kein langsamer Verfall ist, sondern ein aktiver Gegner: Fälscher passen sich an das Prüfsystem an. B3 als Beispiel für KI in einer dokumentationspflichtigen Sorgfaltsprüfung inklusive Prüfpfad. Human-in-the-Loop bei allen Fällen der Gruppe B. |

