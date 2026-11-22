# Reinforcement Learning

**Begriff:** Reinforcement Learning (Bestärkendes Lernen)

**Definition:** Reinforcement Learning ist ein Lernverfahren, bei dem ein KI-Agent durch Ausprobieren lernt: Er führt Aktionen aus, erhält dafür Belohnungen oder Strafen, und optimiert sein Verhalten schrittweise in Richtung maximaler Belohnung — ähnlich wie ein Mensch, der ein neues Spiel erlernt.

---

**Typisches Problem ohne diesen Ansatz:**
Ein Onlinehändler möchte seinen Lagerrobotern beibringen, wie sie Pakete möglichst effizient einlagern und kommissionieren. Das Problem: Die optimale Strategie hängt von Hunderten von Variablen ab — Lagerauslastung, Paketgröße, Bestellhäufigkeit, Gangbreite. Menschliche Programmierer können keine Regeln schreiben, die alle Kombinationen abdecken.

**Wie der Ansatz das Problem löst:**
Die Roboter lernen durch Simulation: In einer virtuellen Lagerumgebung probieren sie Millionen von Szenarien durch. Jede Aktion, die zu schnellerer Kommissionierung führt, wird belohnt; Kollisionen oder Umwege werden bestraft. Nach dem Training in der Simulation werden die gelernten Strategien auf die realen Roboter übertragen.

**Konkretes Praxisbeispiel im Unternehmenskontext:**
Betreiber großer automatisierter Lager erproben Reinforcement Learning, um Lagerroboter zu trainieren (Beispiel zur Veranschaulichung, ohne belegte Unternehmenszahlen). Die Systeme können Strategien entwickeln, die menschliche Planer nicht entworfen hätten — z. B. dynamische Umlagerungen in Niedriglastzeiten, die die Kommissionierung in den Spitzenstunden beschleunigen. Wie stark, muss im eigenen Lager gemessen werden; dem stehen Aufwand für Simulation, Überwachung und Nachtrainieren gegenüber.

**Häufiger Irrtum:**
Reinforcement Learning ist kein universelles Optimierungswerkzeug. Es funktioniert gut, wenn eine klare Belohnungsfunktion definierbar ist. Ist das Ziel schwer messbar (z. B. „Kundenzufriedenheit“), kann das System auf Wege trainieren, die die Kennzahl optimieren, aber das eigentliche Ziel verfehlen — ein bekanntes Problem namens „Reward Hacking“.

---

*Dieses Dokument dient als Quelltext für NotebookLM Audio Overviews im KIM-Kurs.*
*Format: Situation – mögliche Lösung – Auflösung*
