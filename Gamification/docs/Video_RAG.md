# Retrieval-Augmented Generation (RAG)

**Begriff:** Retrieval-Augmented Generation (RAG)

**Definition:** RAG ist ein KI-Verfahren, bei dem ein Sprachmodell vor der Antwortgenerierung gezielt relevante Informationen aus einer externen Wissensbasis abruft — statt ausschließlich auf sein trainiertes Wissen zurückzugreifen.

---

**Typisches Problem ohne diesen Ansatz:**
Ein Unternehmen setzt einen KI-Chatbot ein, der Mitarbeiterfragen zu internen Richtlinien beantworten soll. Der Chatbot gibt plausibel klingende, aber veraltete oder schlicht erfundene Antworten — weil er nur auf Trainingsdaten aus der Vergangenheit zugreifen kann und die aktuellen Unternehmensrichtlinien nicht kennt.

**Wie der Ansatz das Problem löst:**
RAG verbindet das Sprachmodell mit einer aktuellen Dokumentenbasis (z. B. dem internen Richtlinien-Wiki). Bei jeder Anfrage sucht das System zuerst die passenden Dokumente, übergibt sie als Kontext an das Modell — und das Modell antwortet auf Basis dieser konkreten, aktuellen Quellen.

**Konkretes Praxisbeispiel im Unternehmenskontext:**
Ein Versicherungsunternehmen nutzt RAG, um Sachbearbeitenden Fragen zu Vertragsbedingungen zu beantworten. Das System durchsucht automatisch die aktuellen Tarifunterlagen und gibt eine belegbare Antwort mit Quellenangabe zurück — anstatt auf veraltete Trainingsdaten zu verweisen.

**Häufiger Irrtum:**
RAG ist kein "schlaueres" Sprachmodell — es ist ein smarter Arbeitsprozess. Das Modell selbst bleibt unverändert; was sich ändert, ist die Qualität und Aktualität der Informationen, die es zur Verfügung gestellt bekommt.

---

*Dieses Dokument dient als Quelltext für NotebookLM Audio Overviews im KIM-Kurs.*
*Format: Situation – mögliche Lösung – Auflösung*
