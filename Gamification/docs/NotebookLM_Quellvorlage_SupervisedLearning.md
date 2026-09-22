# Supervised Learning

**Begriff:** Supervised Learning (Überwachtes Lernen)

**Definition:** Supervised Learning ist die häufigste Form des Machine Learning. Ein Modell wird mit beschrifteten Beispielen trainiert — d. h. mit Eingaben, bei denen die richtige Antwort bereits bekannt ist. Das Modell lernt, aus neuen Eingaben die richtige Antwort vorherzusagen.

---

**Typisches Problem ohne diesen Ansatz:**
Eine Versicherung erhält täglich Hunderte von Schadensmeldungen per E-Mail. Ein Team prüft jede Meldung manuell und entscheidet: legitimer Schaden oder Betrugsverdacht? Der Prozess ist langsam, teuer und inkonsistent — verschiedene Mitarbeitende kommen bei ähnlichen Fällen zu unterschiedlichen Einschätzungen.

**Wie der Ansatz das Problem löst:**
Das Unternehmen nutzt seine historischen Schadensdaten: Tausende von Fällen, bei denen Betrug bestätigt oder ausgeschlossen wurde. Ein Supervised-Learning-Modell lernt aus diesen beschrifteten Beispielen, welche Merkmale auf Betrug hindeuten — ungewöhnliche Schadenshöhe, kurze Vertragslaufzeit, bestimmte Formulierungsmuster. Neue Meldungen werden automatisch eingestuft und priorisiert.

**Konkretes Praxisbeispiel im Unternehmenskontext:**
Allianz und andere Versicherer setzen Supervised-Learning-Modelle zur Betrugserkennung ein. Das Ergebnis: Hochrisiko-Fälle landen sofort bei spezialisierten Prüfern, klare Standardfälle werden automatisch freigegeben. Die manuelle Prüfzeit sinkt um bis zu 60 %, die Erkennungsrate für Betrug steigt.

**Häufiger Irrtum:**
Das Modell kann nur so gut sein wie die Trainingsdaten. Waren in der Vergangenheit bestimmte Betrugsformen unterrepräsentiert oder wurden sie systematisch übersehen, lernt das Modell diese blinden Flecken mit. "Garbage in, garbage out" gilt hier besonders — die Qualität der Beschriftungen ist entscheidend.

---

*Dieses Dokument dient als Quelltext für NotebookLM Audio Overviews im KIM-Kurs.*
*Format: Situation – mögliche Lösung – Auflösung*
