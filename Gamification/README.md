# FachKInesisch — Reisen durchs wilde KIgistan

Browser-basiertes Lern-Spiel für den KIM-Kurs (KI-Manager) und angrenzende Kursformate. Realistische Alltagssituationen einer KI-Managerin — Slack-Nachrichten, E-Mails, Anrufe, Chats — mit Multiple-Choice-Antworten, sokratischer Rückfrage bei Falsch-Klicks und einer didaktischen Vertiefung mit öffentlichen Quellen nach jeder Frage.

Live: https://northdream64.github.io/KI_Schulungen_UNO/Gamification/

## Was drin ist

Aktuell **46 Fragen in 8 „Reisen"**, jede Reise mit einem eigenen inhaltlichen Fokus. Reihenfolge folgt dem KI-Lebenszyklus:

| # | Reise | Fokus |
|---|-------|-------|
| 1 | Schiff, Flugzeug oder Auto? | KI-Grundbegriffe, Modellfamilien |
| 2 | Kofferpacken | Modell-Training, Daten-Aufbereitung |
| 3 | Routenwahl / Routenqual | Modell-Bewertung, Metriken, Fairness |
| 4 | Auf geht's | Rollout, Go-Live, Kill Switch |
| 5 | Navi und Karte | MLOps, Drift-Monitoring, Betrieb |
| 6 | Reiseapotheke | Schutzmaßnahmen und Erklärbarkeit |
| 7 | Exotische Ziele | GenAI, Agenten, RLHF/RLVR, Neuro-Symbolic |
| 8 | Zurück im Reisebüro | Abnahme, EU AI Act Art. 10, Model/Data Cards |

Pro Reise werden bis zu **5 Fragen** zufällig gezogen (`PAKET_GROESSE` in `game.js`). Die Fragen selbst enthalten zusätzlich eine Vertiefung mit 2–5 öffentlichen Quellen (Wikipedia, EU AI Act, Google SRE, AWS ML Lens, Nature, arXiv).

## Ordner-Struktur

```
Gamification/
├── index.html              Startseite (Datenschutz, Namenseingabe, Reise-Auswahl)
├── assets/
│   ├── style.css           Layout im Kurs-Design (warmes Papier, lila Akzent)
│   └── game.js             Spiel-Logik (Reise laden, Frage anzeigen, Feedback)
├── data/
│   ├── fragen.json         Alle Fragen, gefiltert per Feld `paket` (1–8)
│   └── pakete.json         Metadaten der 8 Reisen (Titel, Beschreibung, aktiv-Flag)
├── apps_script/
│   └── Code.gs             Google-Apps-Script-Backend (Google-Sheet-Logging)
├── docs/                   Interne Arbeitsdokumente (NotebookLM-Vorlagen etc.)
└── README.md               diese Datei
```

## Public URL & Deployment

Der Ordner `Gamification/` wird über **GitHub Pages** ausgeliefert:
`https://northdream64.github.io/KI_Schulungen_UNO/Gamification/`

Push auf `main` reicht — GitHub Pages baut automatisch neu (typisch 1–2 Minuten).

## Datenschutz-Setup

- Vornamen-Eingabe ist freiwillig; leer = „anonym"
- Datenschutzhinweis erscheint **vor** dem Namensfeld
- Speicherdauer: max. 14 Tage, dann automatische Löschung durch Apps-Script-Trigger
- Löschungs-Kontakt: `u.nord@pm-diagnostik.de`
- Kein Personenbezug erzwungen, kein Tracking, keine Cookies

## Google-Sheet-Backend einrichten (einmalig, ca. 5 Minuten)

1. Neues Google Sheet anlegen, z. B. `KIM-Gamification`.
2. Menü **Erweiterungen → Apps Script** öffnen.
3. Den Inhalt von `apps_script/Code.gs` komplett in den Script-Editor kopieren (den Beispiel-Inhalt vorher löschen).
4. Speichern (Diskettensymbol), dann oben rechts **Bereitstellen → Neue Bereitstellung**.
5. Als Typ **Web-App** wählen. Ausführen als „Ich", Zugriff „Jeder". **Bereitstellen**.
6. Google fragt nach Berechtigungen — bestätigen. Danach wird eine **URL** angezeigt: kopieren.
7. In `assets/game.js` die Konstante `APPS_SCRIPT_URL` mit der kopierten URL befüllen.
8. Im Apps-Script-Editor die Konstante `SHEET_ID` auf die eigene Sheet-ID setzen (aus der Sheet-URL).
9. Die Funktion `installTrigger` einmalig ausführen (Dropdown oben → `installTrigger` → **Ausführen**). Das aktiviert die tägliche Auto-Löschung.

Das Sheet legt sich beim ersten eingehenden Event automatisch einen Reiter `Log` mit Kopfzeile an.

## Fragen ergänzen oder ändern

Alle Fragen leben in `data/fragen.json`. Schema pro Frage:

```json
{
  "id": "L4-10",
  "schwierigkeit": 3,
  "paket": 4,
  "absender": "IT-Sicherheit",
  "kanal": "Anruf",
  "szenario": "Der Leiter IT-Sicherheit ruft nachts um 23:15 an: ...",
  "frage": "Welche Aussagen sind zutreffend? (Mehrfachauswahl)",
  "optionen": [
    { "id": "a", "text": "..." },
    { "id": "b", "text": "..." },
    { "id": "c", "text": "..." },
    { "id": "d", "text": "..." }
  ],
  "korrekt": ["a", "b"],
  "feedback_richtig": "Genau. ...",
  "feedback_falsch": "Nicht ganz. ...",
  "glossar": { "begriff": "...", "erklaerung": "..." },
  "vertiefung": {
    "begriff": "...",
    "laien_erklaerung": "Ausführlicher Fließtext mit \\n\\n als Absatz-Trenner.",
    "quellen": [
      { "titel": "...", "art": "...", "institution": "...", "url": "..." }
    ]
  }
}
```

**Feste Regeln** (im Regel-Check `data/fragen.json`):
- Immer **genau 4 Optionen**.
- **1–3 korrekte Antworten**, nie vier.
- Frage-Text muss angeben, ob Mehrfachauswahl möglich ist.

**Neue Reise anlegen**: Eintrag in `pakete.json` ergänzen, `aktiv: true` setzen. Die Fragen bekommen das entsprechende `paket`-Feld.

## Karten-Sammlung und Auswertung

Nach jeder Reise sieht die Teilnehmer:in eine Karten-Sammlung mit den bearbeiteten Begriffen, farblich nach Erfolgs-Status:

- **sofort verstanden** (dunkelgrün, fett): Beim ersten Versuch richtig.
- **im zweiten Versuch** (klarblau): Nach der sokratischen Rückfrage geknackt.
- **teilweise erfasst** (gelb): Ein Teil der richtigen Antworten war dabei.
- **durch Erklärung** (violett): Erst über die didaktische Vertiefung verstanden.
- **direkt zur Erklärung** (grau gestrichelt): „Ich weiß nicht"-Klick.

## Sicherheit

- Die Apps-Script-URL steht öffentlich im Quelltext (unvermeidbar, der Browser muss sie aufrufen).
- Missbrauchsschutz erfolgt über den `SHARED_TOKEN`, den das Script prüft. Ohne gültiges Token wird kein Eintrag geschrieben.
- Kein 100-%-Schutz gegen gezielten Missbrauch, aber effektiv gegen zufällige Bots.
- Für den Testbetrieb bewusst ohne komplizierte Auth-Kette gebaut. Wer produktive Daten hinter einer echten Auth-Schicht braucht: den Apps-Script-Aufruf durch einen serverseitigen Proxy ersetzen.

## Bekannte Grenzen

- `no-cors`-Fetch bedeutet: der Browser sieht keine Antwort vom Apps Script (Erfolg oder Fehler). Für „best effort logging" ausreichend.
- Wer den Browser komplett schließt, bevor eine Frage abgeschickt ist, verliert nur diese eine Antwort — der Rest ist im Sheet.
- Kein Offline-Modus. Wer ohne Netz spielen will: alle drei Dateien lokal bereitstellen und `APPS_SCRIPT_URL` leer lassen — die Datenschutz-Hinweis passt sich dann automatisch an.

## Weiterentwicklung

Backlog steht im Kurs-Repo und wird in der Regel gemeinsam mit dem Dozenten U. Nord besprochen. Vorschläge, Fehlermeldungen und Verbesserungswünsche gehen an `u.nord@pm-diagnostik.de` oder als Issue in dieses Repo.

---

**Autor:** Ulrich Nord · 2026
