/**
 * KI-Manager Gamification — Google Apps Script
 *
 * Nimmt POST-Requests aus der Spiel-HTML entgegen und schreibt eine Zeile
 * ans zugehörige Google Sheet. Löscht automatisch Einträge älter als 14 Tage.
 *
 * DEPLOYMENT (Klick-Reihenfolge):
 *   1. Neues Google Sheet anlegen (Name z. B. "KIM-Gamification").
 *   2. Erweiterungen → Apps Script öffnen. Diesen Code komplett einfügen.
 *   3. Oben rechts "Bereitstellen" → "Neue Bereitstellung" → Typ "Web-App":
 *        - Beschreibung:   KIM-Gamification v1
 *        - Ausführen als:  ich
 *        - Zugriff:        Jeder (nur so kann der Browser der Teilnehmenden
 *                          schreiben; Missbrauchsschutz via SHARED_TOKEN)
 *      Bereitstellen → URL kopieren.
 *   4. Diese URL in assets/game.js als APPS_SCRIPT_URL eintragen und
 *      SHARED_TOKEN in beiden Dateien identisch setzen.
 *   5. Im Apps-Script-Editor einmal die Funktion `installTrigger` ausführen
 *      (Zahnrad → Funktion auswählen → Ausführen), damit die tägliche
 *      Auto-Löschung aktiv wird. Beim ersten Ausführen fragt Google nach
 *      Berechtigungen — bestätigen.
 */

const SHARED_TOKEN     = "kim-2026-alpha";  // muss mit game.js übereinstimmen
const AUFBEWAHRUNGSTAGE = 14;
const SHEET_NAME       = "Log";
const SHEET_ID = "1rl2SofJfY6DPf6UYqYnB9tZ6WTihzkVr-FUwmTssoT0";

// ── POST-Handler ─────────────────────────────────────────────────────────
function doPost(e) {
  try {
    console.log("doPost aufgerufen");
    const payload = JSON.parse(e.postData.contents);
    console.log("Payload empfangen: " + JSON.stringify(payload));

    if (payload.token !== SHARED_TOKEN) {
      console.log("TOKEN FALSCH — erwartet: " + SHARED_TOKEN + ", bekommen: " + payload.token);
      return ausgabe({ ok: false, err: "invalid token" });
    }
    console.log("Token ok");

    const ss = SpreadsheetApp.openById(SHEET_ID);
    if (!ss) {
      console.log("KEIN SHEET GEBUNDEN — Script ist standalone");
      return ausgabe({ ok: false, err: "no bound sheet" });
    }
    console.log("Sheet: " + ss.getName() + " (ID " + ss.getId() + ")");

    let sheet = ss.getSheetByName(SHEET_NAME);
    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
      sheet.appendRow(["Zeit", "Session", "Spieler", "Paket", "Schwierigkeit", "Frage-ID", "Begriff", "Frage", "Gewählt", "Korrekt", "Richtig?", "Versuche"]);
      console.log("Log-Tab neu angelegt");
    }

    sheet.appendRow([
      payload.zeit || new Date().toISOString(),
      payload.session || "",
      payload.spieler || "anonym",
      payload.paket || payload.level || "",
      payload.schwierigkeit || "",
      payload.frage_id || "",
      payload.begriff || "",
      payload.frage_text || "",
      payload.gewaehlt || "",
      payload.korrekt || "",
      payload.richtig === true ? "ja" : (payload.richtig === null ? "übersprungen" : "nein"),
      payload.versuche || 1
    ]);
    console.log("Zeile geschrieben");

    return ausgabe({ ok: true });
  } catch (err) {
    console.log("EXCEPTION: " + err);
    return ausgabe({ ok: false, err: String(err) });
  }
}

// ── AUTO-LÖSCHUNG > 14 TAGE ──────────────────────────────────────────────
function cleanupAlt() {
  const ss = SpreadsheetApp.openById(SHEET_ID);
  const sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) return;

  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  const grenze = new Date();
  grenze.setDate(grenze.getDate() - AUFBEWAHRUNGSTAGE);

  const werte = sheet.getRange(2, 1, lastRow - 1, 1).getValues();
  const zeilenZuLoeschen = [];
  werte.forEach((row, i) => {
    const zeit = new Date(row[0]);
    if (zeit < grenze) zeilenZuLoeschen.push(i + 2); // Sheet-Zeilennummer
  });

  // Rückwärts löschen, damit Zeilenindizes stabil bleiben
  zeilenZuLoeschen.reverse().forEach(z => sheet.deleteRow(z));
}

// ── EINMALIG AUSFÜHREN, UM DEN TÄGLICHEN TRIGGER ZU INSTALLIEREN ────────
function installTrigger() {
  // Bestehende Trigger für cleanupAlt entfernen, um Duplikate zu vermeiden
  ScriptApp.getProjectTriggers().forEach(t => {
    if (t.getHandlerFunction() === "cleanupAlt") ScriptApp.deleteTrigger(t);
  });
  // Täglich zwischen 03:00 und 04:00 Uhr laufen lassen
  ScriptApp.newTrigger("cleanupAlt")
    .timeBased()
    .everyDays(1)
    .atHour(3)
    .create();
  Logger.log("Trigger cleanupAlt installiert (täglich, ca. 03:00 Uhr).");
}

function testeSheetVerbindung() {
  try {
    const ss = SpreadsheetApp.openById(SHEET_ID);
    console.log("Sheet geöffnet: " + ss.getName());
    let sheet = ss.getSheetByName(SHEET_NAME);
    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
      sheet.appendRow(["Zeit", "Session", "Spieler", "Level", "Frage-ID", "Gewählt", "Korrekt", "Richtig?", "Versuche"]);
      console.log("Log-Tab neu angelegt");
    }
    sheet.appendRow([new Date().toISOString(), "MANUELL", "Test", "0", "TEST", "a", "a", "ja", 1]);
    console.log("Testzeile geschrieben");
    return "OK";
  } catch (err) {
    console.log("FEHLER: " + err);
    throw err;
  }
}
