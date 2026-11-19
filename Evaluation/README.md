# Evaluation (Eval) · Prompts messen

Ein **setup-freier** Einstieg in die Evaluation von Prompts – für Menschen ohne Technik-Hintergrund.
Teil des Kurses *KI-Manager:in* (KIM).

> **Direkt öffnen (empfohlen):** Das interaktive Werkzeug läuft im Browser unter
> <https://northdream64.github.io/KI_Schulungen_UNO/Evaluation/>
> — kein Download, keine Installation.

Grundlage ist der fiktive Anwendungsfall [„Sammel Deinen Traum“](../Use%20Cases/UC05_Sammel_Deinen_Traum.md),
ein Online-Auktionshaus mit einem Kundenservice-Bot. Am Kontrollfall „Auktionszeiten“ zeigt das Werkzeug,
wie man vorab festlegt, was eine gute Antwort ist, wie Antworten nach festen Regeln und von einem
KI-Bewerter geprüft werden – und warum ein Kontrollfall sorgfältig gebaut werden muss.

## Dateien

| Datei | Zweck | Für wen |
|---|---|---|
| **index.html** | Im Browser öffnen. Reiter: *Übersicht*, *1 · Testprozedur*, *2 · Erstellung Kontrollfall*, *3 · Prompt*, *4 · Eval-Lauf*, *5 · Ergebnis*, *Back-Up: Daten und Code*, *Quellen*. **Kein Setup.** | Teilnehmende (Haupt-Werkzeug) |
| **Testliste_Kontrollfall_K1.csv** | Die 50 Kundenanfragen zum Kontrollfall als Tabelle (öffnet in Excel): Antwort des Bots, richtige Antwort laut erster und laut überarbeiteter Fassung des guten Ergebnisses, Ergebnis. | Alle – so sieht eine Testliste aus |
| **LICENSE** | Rechtevermerk für alle Inhalte dieses Ordners. | — |

## Nutzung

- **Ohne alles:** `index.html` im Browser öffnen (oder den Pages-Link teilen).
- Die Auswertungen in den Reitern *2* und *5* sind **Modellrechnungen** – sie laufen ohne KI.
- Der **Eval-Lauf** in Reiter *4* braucht eine Verbindung zu einem KI-Modell. Wie das geht, steht auf der
  *Übersicht* unter „Wie Du die HTML-Datei mit Deiner KI verbinden kannst“. Ohne Verbindung zeigt der Reiter,
  was geprüft würde, startet aber keinen Lauf.

## Die drei „Aha“-Momente

1. **Das gute Ergebnis steht vor dem ersten Lauf fest** – und es ist eine fachliche, keine technische Entscheidung.
2. **100 % können täuschen:** Eine unvollständige Messlatte übersieht Fehler, die es längst gibt.
3. **Anweisungen allein machen ein Modell nicht verlässlich** – Daten wie ein Feiertagskalender schon.

Alle Namen, Zahlen und Regeln sind fiktiv und für die Übung erstellt.

© 2026 Ulrich Nord · Alle Rechte vorbehalten – siehe [LICENSE](LICENSE).
