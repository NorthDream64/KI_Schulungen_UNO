# KIM-Gamification — Prototyp

Kleines Browser-Spiel, das Fachbegriffe aus dem KIM-Kurs in realistische Alltagssituationen einbettet. Zielgruppe: Teilnehmende ohne IT-Vorkenntnisse.

## Struktur

```
Gamification/
├── index.html            Startseite mit Datenschutzhinweis + Namenseingabe
├── assets/
│   ├── style.css         Layout, passend zum bestehenden Kurs-Design
│   └── game.js           Spiel-Logik, Fetch ans Apps-Script
├── data/
│   ├── level1.json       Vokabeln im Alltag
│   ├── level2.json       Diagnose (Symptom → Maßnahme)
│   └── level3.json       Governance-Fall (mehrere richtige Antworten)
└── apps_script/
    └── Code.gs           Google-Apps-Script-Backend
```

## Öffentliche URL nach dem Push

`https://northdream64.github.io/KI_Schulungen_UNO/Gamification/`

## Datenschutz-Setup

- Vornamen-Eingabe ist freiwillig; leer = „anonym"
- Datenschutzhinweis erscheint **vor** dem Namensfeld
- Speicherdauer: max. 14 Tage, dann automatische Löschung durch Trigger
- Kein Personenbezug erzwungen, kein Tracking

## Google-Sheet-Backend einrichten (einmalig, ca. 5 Minuten)

1. Neues Google Sheet anlegen, z. B. `KIM-Gamification`.
2. Menü **Erweiterungen → Apps Script** öffnen.
3. Den Inhalt von `apps_script/Code.gs` komplett in den Script-Editor kopieren (den Beispiel-Inhalt vorher löschen).
4. Speichern (Diskettensymbol), dann oben rechts **Bereitstellen → Neue Bereitstellung**.
5. Als Typ **Web-App** wählen. Ausführen als „Ich", Zugriff „Jeder". **Bereitstellen**.
6. Google fragt nach Berechtigungen — bestätigen. Danach wird eine **URL** angezeigt: kopieren.
7. In `assets/game.js` die Zeile `const APPS_SCRIPT_URL = "";` befüllen mit der kopierten URL.
8. Zurück im Apps-Script-Editor die Funktion `installTrigger` einmalig ausführen (Dropdown oben → `installTrigger` → **Ausführen**). Das aktiviert die tägliche Auto-Löschung.

Das Sheet legt sich beim ersten eingehenden Event automatisch einen Reiter `Log` mit Kopfzeile an.

## Erweitern

- **Neue Fragen:** in `data/levelN.json` ergänzen. Schema: `id`, `absender`, `kanal`, `szenario`, `frage`, `optionen[]`, `korrekt[]`, `feedback_richtig`, `feedback_falsch`, `glossar { begriff, erklaerung }`.
- **Neues Level:** neue JSON-Datei anlegen und in `assets/game.js` in `LEVELS[]` eintragen.
- **Token wechseln:** Wert von `SHARED_TOKEN` in `game.js` und `Code.gs` synchron ändern.

## Sicherheit

- Die Apps-Script-URL steht öffentlich im HTML-Quelltext (unvermeidbar, weil der Browser sie aufrufen muss).
- Missbrauchsschutz erfolgt über den `SHARED_TOKEN`, den das Script prüft. Ohne gültiges Token wird kein Eintrag geschrieben.
- Kein 100-%-Schutz gegen gezielten Missbrauch, aber effektiv gegen zufällige Bots.

## Bekannte Grenzen

- `no-cors`-Fetch bedeutet: der Browser sieht keine Antwort vom Apps Script (Erfolg oder Fehler). Für den Zweck „best effort logging" ausreichend.
- Wer den Browser komplett schließt, bevor eine Frage abgeschickt ist, verliert nur diese eine Antwort — der Rest ist im Sheet.
