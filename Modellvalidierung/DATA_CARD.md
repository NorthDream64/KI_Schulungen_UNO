# Data Card — `bewerber_screening.csv`

> Beschreibung des Datenbestands, der dem Lab *Modellvalidierung & Bias* zugrunde liegt.
> Aufbau angelehnt an den [Data Cards Playbook](https://sites.research.google/datacardsplaybook/) von Google PAIR
> und an [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) (Gebru et al.).
> Teil des Kurses **KI-Manager:in (KIM)**.

---

## 1 · Überblick

Ein **vollständig synthetischer** Datensatz mit 2.000 fiktiven Bewerbungen für eine
Personalvorauswahl. Jede Zeile ist eine Bewerbung mit sechs Merkmalen und der historischen
Entscheidung, ob eingestellt wurde.

**Kein einziger Wert stammt von einer realen Person.** Der Bestand wurde per Skript erzeugt,
um ein Lehrbeispiel zu haben, dessen Eigenschaften vollständig bekannt sind.

## 2 · Zweck — und ausdrücklich nicht

**Wofür:** Zeigen, wie sich Schwellenwert, Precision, Recall und F-Wert gegenseitig bedingen —
und wie ein Modell eine Voreingenommenheit aus historischen Entscheidungen übernimmt, auch
wenn das betreffende Merkmal weggelassen wird.

**Wofür ausdrücklich nicht:**

- Kein Beleg für tatsächliche Einstellungspraxis in irgendeinem Unternehmen.
- Keine Grundlage für Aussagen über reale Benachteiligungen — die eingebauten Effekte sind
  gesetzt, nicht gemessen.
- Keine Vorlage für ein produktives Auswahlmodell. Personalauswahl ist nach
  EU AI Act, Anhang III Nr. 4 ein Hochrisiko-Bereich.

## 3 · Herkunft

| | |
|---|---|
| **Erzeugt von** | `01_dataset_und_kennzahlen.py` in diesem Ordner |
| **Verfahren** | Zufallszahlen mit festem Startwert (`default_rng(42)`) — der Bestand ist damit exakt reproduzierbar |
| **Bibliotheken** | numpy, pandas, scikit-learn |
| **Rechtsgrundlage** | entfällt — keine personenbezogenen Daten |
| **Lizenz** | wie das Repository (siehe `LICENSE`) |

## 4 · Umfang und Struktur

**2.000 Zeilen**, davon 800 im Testteil. Der Anteil positiver Entscheidungen liegt bei
rund **36 %**.

| Feld | Bedeutung | Wertebereich |
|---|---|---|
| `geschlecht` | binäre Vereinfachung für das Lab | 0 = weiblich, 1 = männlich |
| `alter_monate` | Lebensalter, kontinuierlich | 240–780 (≈ 20–65 Jahre) |
| `fachscore` | fachliche Passung aus den Unterlagen | 0–100 |
| `interview` | „passt ins Team", weiche Faktoren | 0–100 |
| `erfahrung_jahre` | Berufsjahre laut Lebenslauf | 0–40 |
| `karriere_luecke_monate` | Unterbrechung ohne Erwerbstätigkeit | 0–60 |
| `eingestellt` | historische Entscheidung — die Zielgröße | 0 / 1 |

## 5 · Erhebung und Beschriftung

Es gab keine Erhebung. Alle Merkmale sind gezogene Zufallswerte, die Zielgröße `eingestellt`
ist aus einer festgelegten Formel abgeleitet:

```
logit = −1,15 + 2,2 · Verdienst  + 0,9 · männlich
                − 0,025 · (Alter in Jahren − 40)
                − 0,035 · Karrierelücke in Monaten
```

Der Begriff **Verdienst** fasst dabei Fachscore, Interview und Erfahrung zusammen — das,
was jemanden tatsächlich geeignet macht. Fachscore und Interview sind **unabhängig** von
Geschlecht und Alter gezogen.

## 6 · Abdeckung und Lücken — die eingebauten Verzerrungen

Dies ist der Abschnitt, der bei einem fremden Datensatz meist leer bleibt. Hier lässt er sich
vollständig füllen, weil die Verzerrung **absichtlich gesetzt** wurde:

- **Bevorzugung von Männern.** Ein fester Bonus im Entscheidungsmodell, unabhängig von der
  Eignung. Er bildet ab, was ein Modell aus voreingenommenen historischen Entscheidungen lernt.
- **Schleichender Alterseffekt.** Kein harter Schnitt bei 40, sondern ein kleiner linearer
  Auf- oder Abschlag je Lebensjahr. Bewusst so gewählt: Eine harte Altersgrenze würde kein
  Unternehmen so codieren; Altersdiskriminierung wirkt in der Praxis graduell.
- **Überzogene Bestrafung der Karrierelücke.** Der Abschlag geht über das hinaus, was durch
  tatsächlich fehlende Erfahrung erklärbar wäre.
- **Die Karrierelücke ist der Stellvertreter.** Sie ist bei Frauen im Mittel um rund zwölf
  Monate größer angesetzt. Dadurch gelangt das Geschlecht zurück ins Modell, **auch wenn man
  die Spalte `geschlecht` entfernt** — das ist der Kern von Abschnitt 3 im Lab.
  Der Größenunterschied ist an reale Größenordnungen angelehnt: Nach Angaben des Statistischen
  Bundesamts beziehen Mütter im Schnitt rund 10–12 Monate Elterngeld, Väter rund 3–4 Monate.

**Was der Bestand nicht abbildet:** Geschlecht jenseits einer binären Erfassung · Branche,
Region, Position · Bewerbungen, die vor der Erfassung ausgesiebt wurden · alles, was reale
Auswahlprozesse sonst noch beeinflusst.

## 7 · Bekannte Einschränkungen

- Die Zusammenhänge sind **einfacher als in der Wirklichkeit**. Der Bestand eignet sich zum
  Verstehen von Mechanismen, nicht zum Abschätzen realer Effektstärken.
- Es gibt keine fehlenden Werte, keine Erfassungsfehler und keine Dubletten — reale Bestände
  haben all das. Wer nur mit diesem Datensatz arbeitet, unterschätzt den Aufbereitungsaufwand.
- Der Bestand ist **statisch**. Drift lässt sich daran nicht zeigen; dafür gibt es im selben
  Ordner `tankstelle_umsatz.csv`.

## 8 · Verantwortung und Pflege

Verantwortlich: **Ulrich Nord**, Dozent des Kurses. Der Bestand wird nur geändert, wenn sich
das Lehrziel ändert; jede Änderung erfolgt über das Erzeugungsskript, nicht an der CSV-Datei.
Wiedervorlage: mit jedem Kursdurchlauf.

---

### Warum diese Karte existiert

Weil man an einem Bestand, dessen Entstehung man vollständig kennt, sehen kann, **wie eine
Data Card aussieht, wenn sie ausnahmsweise lückenlos ist**. Bei fremden Datenbeständen — etwa
denen auf öffentlichen Plattformen — bleiben Abschnitt 5 und 6 in aller Regel leer. Genau
dieser Unterschied ist die Lehre.

*Zur Vertiefung: [Pushkarna, Zaldivar & Kjartansson — Data Cards, ACM FAccT 2022](https://arxiv.org/abs/2204.01075)
· [Mitchell et al. — Model Cards for Model Reporting, ACM FAccT 2019](https://arxiv.org/abs/1810.03993)*
