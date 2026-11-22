# -*- coding: utf-8 -*-
"""Inhalte des Umsetzungsstands. Quelle: Entscheidungsprotokoll Reviewer (Stand 18.11.2026)
sowie die eigenen Prueffunde der Kurstag-Reviews."""

# wer: 'du' = Dozent (Foliensaetze, Gamma) | 'ich' = Claude (Hand-Out, Handreichungen, Register)
#      'ent' = Entscheidung des Dozenten, danach baut Claude
# st : 'offen' | 'teil' (Hand-Out-Teil erledigt, Folienteil offen) | 'fertig'

QUER = []

QUER_FERTIG = [
    ('QS-01', '🟡', 'Haftungshinweis „keine Rechtsberatung im Einzelfall“ steht in der Fußzeile '
               'aller 16 KIM-Hand-Outs; Stand-Datum in Tag 1 entfernt, damit die Zeile überall '
               'gleich lautet. Folien vom Dozenten erledigt. Schließt CL-KIM-T1-92, T2-27, T3-23 '
               'und T4-34.', '18.11.2026'),
    ('QS-02', '⚪', 'Herkunft und Lizenz der Foliengrafiken vom Dozenten geprüft. Schließt '
               'CL-KIM-T2-28 und T3-27.', '18.11.2026'),
    ('QS-03', '⚪', 'Lizenz zur Weitergabe von Norm und Fachbüchern: gültig lizenzierte eBooks des '
               'Bildungszentrums, Nachweis vom 11.11.2026 auf CL-KIM-T2-34 übertragen.', '18.11.2026'),
]

T1_OFFEN = []

T1_MEINS = [
    dict(id='MIR-T1-02', sev='🟡', wer='ent', fund='Alle 16 KIM-Hand-Outs, Quellenverzeichnis', st='offen',
         titel='Tagesquellen ausklappbar machen — oder beim bisherigen Aufbau bleiben?',
         det='Korrektur meiner eigenen Darstellung: Das ist kein Tag-1-Mangel. Am 22.11. nachgezählt — '
             'alle 16 KIM-Hand-Outs haben denselben Aufbau („Für diesen Tag“ offen, darunter die '
             'Dauerreferenzen), und keines hat einen ausklappbaren Quellenblock. Ausklappbar ist die '
             'Zielstruktur aus der KIB-Vorlage. Tag 1 allein umzubauen würde ihn zum Ausreißer machen. '
             'Die Mechanik (CSS und Auf-/Zuklappen-Skript) liegt in allen Dateien bereits bereit, es '
             'fehlt nur das Markup. Also: so lassen oder alle 16 in einem Durchgang umstellen?'),
    dict(id='MIR-T1-04', sev='🟢', wer='ich', fund='Hand-Out, Taxonomie (Zeile Verstärkendes Lernen)', st='offen',
         titel='AlphaGo wird im Rumpf noch einmal genannt',
         det='Deine Weisung vom 17.11.: AlphaGo und Zug 37 haben im Hand-Out nichts zu suchen. Das '
             'Fallbeispiel ist draußen, in der Taxonomie steht der Name aber noch als Beispiel für '
             'verstärkendes Lernen. Soll er dort bleiben oder durch ein neutrales Beispiel ersetzt werden?'),
    dict(id='MIR-T1-05', sev='⚪', wer='ent', fund='Kursmaterialien/Lehrgangspfad_KIB_KIM.html', st='offen',
         titel='Lehrgangspfad: Fortschrittsmarke steht für beide Kurse auf 0',
         det='`bisTag: 0` für KIB und KIM — die Pfadgrafik zeigt damit keinen Fortschritt. Stehende '
             'Regel ist, Planungsartefakte nicht ungefragt nachzuziehen, deshalb liegt das hier als '
             'Entscheidung und nicht als Aufgabe.'),
]

T1_FERTIG = [
    ('CL-KIM-T1-53', '🟠', 'Folie 10: Drift nicht mehr mit Anpassungsfähigkeit gleichgesetzt', '13.11.2026'),
    ('CL-KIM-T1-54', '🟠', 'Folie 14: irreführendes Beispiel zur Belohnungsfunktion entfernt', '13.11.2026'),
    ('CL-KIM-T1-55', '🟠', 'Folien 24/26: BAIT als Referenzrahmen gelöscht', '13.11.2026'),
    ('CL-KIM-T1-56', '🟠', 'Folie 27: Praxisarbeit um Stoppkriterien und Risikoappetit erweitert', '17.11.2026'),
    ('CL-KIM-T1-57', '🟡', 'Hand-Out: Vorbehalt der Fed-Atlanta-Autoren richtiggestellt', '13.11.2026'),
    ('CL-KIM-T1-58', '🟡', 'Hand-Out: CAPTCHA-Chronik 2003 vereinheitlicht', '13.11.2026'),
    ('CL-KIM-T1-59', '🟡', 'Hand-Out: Deep Blue der vorigen Epoche zugeordnet', '13.11.2026'),
    ('CL-KIM-T1-60', '🟡', 'Hand-Out: Krimi-Karte auf die Abnahme mit unbekannter Lösung umgestellt', '13.11.2026'),
    ('CL-KIM-T1-61', '🟡', 'Hand-Out: Taxonomie in zwei Achsen geteilt (Lernprinzipien, Bauform)', '17.11.2026'),
    ('CL-KIM-T1-62', '🟡', 'Folie 2: Kursübersicht didaktisch angepasst', '17.11.2026'),
    ('CL-KIM-T1-63', '🟡', 'Folie 7: Kachel Einstellungsbedarf gelöscht', '17.11.2026'),
    ('CL-KIM-T1-64', '🟡', 'Folie 7 und Quellenverzeichnis: Präsentation neu gestaltet', '17.11.2026'),
    ('CL-KIM-T1-65', '🟡', 'Folie 8 „Boom oder Doom“ entfernt', '17.11.2026'),
    ('CL-KIM-T1-66', '🟡', 'Folie 9: Prognosecharakter klargestellt', '17.11.2026'),
    ('CL-KIM-T1-67', '🟡', 'Folie 10: „wirkt weitgehend wie eine Black Box“', '17.11.2026'),
    ('CL-KIM-T1-68', '🟡', 'Folie 15: AlphaGo und Zug 37 nachgeprüft und neu gefasst', '17.11.2026'),
    ('CL-KIM-T1-69', '🟡', 'Folien 16/6 und Hand-Out: „verstehen“ auf einen gemeinsamen Stand gebracht', '17.11.2026'),
    ('CL-KIM-T1-70', '🟡', 'Folien 17/18: Kostenanker „Aufwand“ entfernt', '17.11.2026'),
    ('CL-KIM-T1-71', '🟡', 'Folie 18 „Pre-trained“: Text umgestellt und geklärt', '17.11.2026'),
    ('CL-KIM-T1-72', '🟡', 'Folie 18 „Transformer“: Aussage neu gefasst', '17.11.2026'),
    ('CL-KIM-T1-73', '🟡', 'Folie 19: Definition nach Art. 3 Nr. 63 KI-VO übernommen', '17.11.2026'),
    ('CL-KIM-T1-74', '🟡', 'Folie 19: Kennzeichnungspflicht für Marketingtexte relativiert', '17.11.2026'),
    ('CL-KIM-T1-75', '🟡', 'Folie 24: Meldeweg im Fall ergänzt', '17.11.2026'),
    ('CL-KIM-T1-76', '🟡', 'Folien 24/25/27: Zuständigkeit — im didaktischen Kontext nicht relevant', '17.11.2026'),
    ('CL-KIM-T1-77', '🟡', 'Folie 26: DORA-Formulierung auf „ICT third-party service provider“ gestellt', '17.11.2026'),
    ('CL-KIM-T1-78', '🟡', 'Folie 26: kein generelles Verbot vollautomatisierter Kreditentscheidungen', '17.11.2026'),
    ('CL-KIM-T1-79', '🟡', 'Folie 26: MaRisk-Aussage präzisiert', '17.11.2026'),
    ('CL-KIM-T1-80', '🟢', 'Hand-Out: Trainingsmenge früher Spamfilter korrigiert', '13.11.2026'),
    ('CL-KIM-T1-81', '🟢', 'Hand-Out: Top-5-Fehlerrate als Kennzahl ergänzt', '13.11.2026'),
    ('CL-KIM-T1-82', '🟢', 'Hand-Out: Synthese-Verweis auf den CAPTCHA-Einstieg bereinigt', '13.11.2026'),
    ('CL-KIM-T1-96', '⚪', 'Drucker-Zitat: Fundstelle vom Dozenten belegt, kein Änderungsbedarf', '13.11.2026'),
    ('CL-KIM-T1-97', '⚪', 'Epochengrenzen: Hand-Out ist richtig (1990–2012)', '13.11.2026'),
    ('CL-KIM-T1-98', '⚪', 'reCAPTCHA und autonomes Fahren: Zuschreibung entschärft', '13.11.2026'),
    ('MIR-T1-01', '🟡', 'Verwaiste Fed-Quellen aus dem Quellenverzeichnis entfernt (zwei Chips plus Erläuterung, ohne Bezug im Text)', '22.11.2026'),
    ('MIR-T1-03', '🟢', 'Entscheidung des Dozenten: Die Quellen des Use Case gehören nicht ins Hand-Out', '22.11.2026'),
    ('CL-KIM-T1-83', '🟢', 'Folie 5: Malik-Zitat als sinngemäße Wiedergabe gekennzeichnet', '22.11.2026'),
    ('CL-KIM-T1-84', '🟢', 'Folie 6: Mollicks Regeln nicht mehr als Managementprinzipien', '22.11.2026'),
    ('CL-KIM-T1-85', '🟢', 'Folie 6: dritte Regel vollständig wiedergegeben', '22.11.2026'),
    ('CL-KIM-T1-86', '🟢', 'Folie 7: Anstieg +52,3 %, „also“ gestrichen', '22.11.2026'),
    ('CL-KIM-T1-87', '🟢', 'Folie 10: Schwellenwert als Richtwert gekennzeichnet', '22.11.2026'),
    ('CL-KIM-T1-88', '🟢', 'Folien 12/13: Labels auch aus Geschäftsdaten, historischer Bias', '22.11.2026'),
    ('CL-KIM-T1-89', '🟢', 'Folie 17: Widerspruch zur eigenen Tabelle aufgelöst', '22.11.2026'),
    ('CL-KIM-T1-90', '🟢', 'Folie 19: Auslassung im Zitat aus Erwägungsgrund 97 gekennzeichnet', '22.11.2026'),
    ('CL-KIM-T1-91', '🟢', 'Folien 22/28: Musterlösung lässt „semi-supervised“ gelten', '22.11.2026'),
    ('CL-KIM-T1-93', '🟢', 'Folie 25: Kriterien, Ausgangswert, Verantwortliche und Termin ergänzt', '22.11.2026'),
    ('CL-KIM-T1-94', '🟢', 'Folie 26: Einstiegsquellen als Eigendarstellung gekennzeichnet', '22.11.2026'),
    ('CL-KIM-T1-95', '🟢', 'Folie 26: BaFin-Merkblatt dieses Titels existiert nicht — Titel ersetzt', '22.11.2026'),
    ('CL-KIM-T1-99', '⚪', 'Folie 6: Umfang der Wiedergabe aus Mollicks Buch geklärt', '22.11.2026'),
    ('CL-KIM-T1-92', '🟢', 'Hinweis „keine Rechtsberatung im Einzelfall“ in Hand-Out und Folien', '18.11.2026'),
    ('CL-KIM-T1-100', '⚪', 'Folie 24: Standort Guernsey didaktisch nicht einschlägig', '17.11.2026'),
    ('CL-KIM-T1-101', '⚪', 'Folie 24: Rolle als „Chief AI Officer“ umformuliert', '17.11.2026'),
]

T2_OFFEN = [
    dict(id='CL-KIM-T2-03', sev='🟡', wer='du', fund='Folien 2 und 3', st='offen',
         titel='KI-Beauftragte:r und KI-Auditor:in werden gleich beschrieben',
         det='Zusätzlich geben die Folien den Aufbau normativer Rahmenwerke beiden Rollen. Das ist die '
             'Trennlinie, die der TÜV-Fragenpool abfragt: Die Beauftragte überwacht laufend, die '
             'Auditorin erteilt ein unabhängiges Prüfurteil. Wer umsetzt, prüft nicht sich selbst.'),
    dict(id='CL-KIM-T2-04', sev='🟡', wer='du', fund='Folie 9, Anhang A, Kachel A.7', st='offen',
         titel='Modellqualität ist im Anhang A nicht der Datenbereich',
         det='Die Folie ordnet die Sicherung der Modellqualität A.7 (Daten) zu. Dort gehört sie nicht hin. '
             'Vor der Korrektur sage mir Bescheid — dann sehe ich die Zuordnung in der Normausgabe nach, '
             'damit die Kachel beim richtigen Bereich landet.'),
    dict(id='CL-KIM-T2-05', sev='🟡', wer='du', fund='Folie 15, Praxisaufgabe d)', st='offen',
         titel='Praxisaufgabe plant eine Datenerhebung über Beschäftigte ohne Datenschutz und Betriebsrat',
         det='In einer Managementrolle ist genau das der Fehler, der teuer wird. Zwei Sätze in der '
             'Aufgabenstellung genügen: Rechtsgrundlage und Beteiligung des Betriebsrats mitdenken.'),
    dict(id='CL-KIM-T2-14', sev='🟢', wer='du', fund='Folie 8', st='offen',
         titel='Oberste Leitung erfüllt die Normkonformität nicht selbst',
         det='Sie verantwortet sie. Erfüllt wird sie durch die Organisation. Im Hand-Out ist die '
             'Rollentabelle seit 17.11. entsprechend gefasst (CL-KIM-T2-01).'),
    dict(id='CL-KIM-T2-15', sev='🟢', wer='du', fund='Folie 14', st='offen',
         titel='Satz wirkt wie eine Aussage des SEI-Modells, stammt aber aus der Führungsanalogie',
         det='Herkunft Hersey/Blanchard. Zuschreibung ergänzen, sonst wirkt eine Analogie wie ein Modellbefund.'),
    dict(id='CL-KIM-T2-16', sev='🟢', wer='du', fund='Folie 15, Praxisaufgabe d)', st='offen',
         titel='Selbstauskünfte überschätzen die Reife — das in die Aufgabe schreiben',
         det='Die Antworten hängen davon ab, wer befragt wird. Für eine Reifegradbestimmung ist das '
             'die wichtigste Einschränkung.'),
    dict(id='CL-KIM-T2-17', sev='🟢', wer='du', fund='Folien 15 und 11', st='offen',
         titel='Praxisaufgabe ohne Auftragsklärung, GAP-Tabelle ohne Verantwortliche, Priorität und Kosten',
         det='Drei Spalten in der GAP-Tabelle ergänzen; die Aufgabe um einen Satz zum Auftrag und zu '
             'den Bewertungskriterien erweitern.'),
    dict(id='CL-KIM-T2-21', sev='🟢', wer='ich', fund='Hand-Out, Quellenchip White House Accord', st='offen',
         titel='Quellenchip ohne Hinweis auf die fehlende amtliche Fundstelle',
         det='Ich ergänze den Vorbehalt, sobald Du freigibst. Vorher suche ich noch einmal nach einer '
             'amtlichen Veröffentlichung; finde ich keine, sage ich das im Chip.'),
    dict(id='CL-KIM-T2-24', sev='🟢', wer='ich', fund='Hand-Out, Analogie, Tabelle M1–M4', st='offen',
         titel='Reifegrade nach Hersey/Blanchard ungenau und mit dem SLII-Modell vermischt',
         det='Das sind zwei Modelle aus zwei Jahrzehnten. Ich trenne die Tabelle und nenne die Herkunft; '
             'die Analogie selbst bleibt, sie trägt den Abschnitt.'),
    dict(id='CL-KIM-T2-26', sev='🟢', wer='ich', fund='Hand-Out, Kasten vor „Der Verstärker“; PDF-Titel', st='offen',
         titel='Tagesverweise im Hand-Out inkonsistent und teils falsch',
         det='Ich ziehe sie gegen die geltende Tagesstruktur nach. Dabei prüfe ich auch, welche Verweise '
             'ganz entfallen können — Tagesverweise im Teilnehmermaterial sind ohnehin sparsam zu halten.'),
    dict(id='CL-KIM-T2-29', sev='⚪', wer='ich', fund='Hand-Out, Abschnitt Marktbedeutung', st='offen',
         titel='Gilt die Konformitätsvermutung von EN 18286 wirklich „nur für Art. 17“?',
         det='Nicht bestätigt. Ich prüfe das gegen den Normungsauftrag der Kommission und den Stand der '
             'Veröffentlichung im Amtsblatt, sobald Du freigibst — Ergebnis offen, die Aussage kann auch fallen.'),
    dict(id='CL-KIM-T2-30', sev='⚪', wer='ich', fund='Hand-Out, Angabe „identischer Normtext“', st='offen',
         titel='Hat die DIN-Fassung einen identischen Normtext?',
         det='Ich habe am 17.11. das Deckblatt der Ausgabe gelesen und die Bezeichnung bestätigt — über '
             'die Textidentität sagt das nichts. Belastbar wäre die Übernahmeerklärung im Vorwort der '
             'DIN-Ausgabe; die sehe ich nach, wenn Du es möchtest.'),
    dict(id='CL-KIM-T2-31', sev='⚪', wer='ent', fund='Hand-Out, Reifegradmodell', st='offen',
         titel='Dimensionsnamen und die Aussage „nicht beschrieben“ ohne Modelldokument nicht prüfbar',
         det='Entweder wir nennen die Quelle des Modells, oder die Kurzfassung wird ausdrücklich als '
             'Kursfassung gekennzeichnet. Letzteres ist der ehrlichere und schnellere Weg — sag, was Du willst.'),
    dict(id='CL-KIM-T2-33', sev='⚪', wer='ich', fund='Hand-Out, Quellenverzeichnis', st='offen',
         titel='Seitenzahlen der Norm und die Ausgabe 2026-08 prüfen',
         det='Teilweise schon erledigt: Bezeichnung und Ausgabestand DIN EN ISO/IEC 42001:2026-08 sowie '
             'Kapitel 9 „Leistungsbewertung“ auf Seite 24 habe ich am 17.11. gegen die lokale '
             'Normausgabe geprüft. Offen sind die übrigen Seitenangaben.'),
]

T2_MEINS = [
    dict(id='MIR-T2-01', sev='🟢', wer='ich', fund='Hand-Out, Fließtext', st='offen',
         titel='Eine Du-Form-Abweichung angleichen',
         det='Gezählt am 18.11.: achtmal „Du“, zweimal „Dich“, einmal kleines „du“. Die eine Stelle '
             'ziehe ich mit dem nächsten Durchgang nach. Dieselbe Prüfung steht für die KIM-Tage 9 und 11 aus.'),
]

T2_FERTIG = [
    ('CL-KIM-T2-01', '🟠', 'Rollentabelle: Zeile „Oberste Leitung“ ergänzt, A-Rolle richtig verteilt', '17.11.2026'),
    ('CL-KIM-T2-02', '🟠', 'Ebene ③ ist externe Zusicherung außerhalb der drei Linien', '17.11.2026'),
    ('CL-KIM-T2-06', '🟡', 'RACI steht nicht mehr als Normvorgabe (Normtext 5.3 zitiert)', '17.11.2026'),
    ('CL-KIM-T2-07', '🟡', 'Auditor:in auf Klausel 9.2 (internes Audit) begrenzt', '17.11.2026'),
    ('CL-KIM-T2-08', '🟡', 'Zeile „Unabhängigkeit“: gute Praxis statt Pflicht', '17.11.2026'),
    ('CL-KIM-T2-09', '🟡', 'Norm verlangt erste und zweite Linie, nicht alle vier Ebenen', '17.11.2026'),
    ('CL-KIM-T2-10', '🟡', 'Reifegrad-Kurzfassung führt vier Dimensionen inkl. Risk & Governance', '17.11.2026'),
    ('CL-KIM-T2-11', '🟡', 'Governance-Intensität: Risiko neben Reife gestellt', '17.11.2026'),
    ('CL-KIM-T2-12', '🟡', '„Der Verstärker“: Zitat dem Mitautor Slattery zugeschrieben', '17.11.2026'),
    ('CL-KIM-T2-13', '🟡', 'Belegstufen gleich angewendet, Vorbehalt beim Leitmodell ergänzt', '17.11.2026'),
    ('CL-KIM-T2-18', '🟢', '„Aufsicht“ ersetzt — Behörden verlangen ISO/IEC 42001 nicht', '17.11.2026'),
    ('CL-KIM-T2-19', '🟢', 'Eskalationsweg: Grenze des Leitungsentscheids ergänzt', '17.11.2026'),
    ('CL-KIM-T2-20', '🟢', '„Ausrichtung“ als Fachbegriff Alignment erklärt', '17.11.2026'),
    ('CL-KIM-T2-22', '🟢', 'Kostenaussage als Einschätzung des Kurses gekennzeichnet', '17.11.2026'),
    ('CL-KIM-T2-23', '🟢', 'P3M3: geschützt sind Texte und Darstellungen, nicht die Methode', '17.11.2026'),
    ('CL-KIM-T2-25', '🟢', 'SoA ist Grundlage einer GAP-Analyse, nicht selbst eine', '17.11.2026'),
    ('CL-KIM-T2-27', '🟢', 'Haftungshinweis in der Fußzeile ergänzt', '18.11.2026'),
    ('CL-KIM-T2-28', '⚪', 'Bildherkunft und Lizenz der Folien 1, 4, 5 vom Dozenten geprüft', '18.11.2026'),
    ('CL-KIM-T2-32', '⚪', 'Link auf die Microsoft-Broschüre aus dem Teilnehmermaterial entfernt', '17.11.2026'),
    ('CL-KIM-T2-34', '⚪', 'Lizenz zur Weitergabe von Norm und Fachbüchern nachgewiesen (eBooks des Bildungszentrums)', '18.11.2026'),
]

T3_OFFEN = [
    dict(id='CL-KIM-T3-01', sev='🟠', wer='du', fund='Folie 6, Feld ④ und Folie 7, Einleitungssatz', st='teil',
         titel='Machbarkeit: ④ Finanziell durch Compliance ersetzen — der Nutzen zählt sonst doppelt',
         det='Am Foliensatz nachgeprüft und bestätigt: Folie 6 definiert oben Wirkung als geschäftlichen '
             'Nutzen und führt unten „④ Finanziell — positives Kosten-Nutzen-Verhältnis (KNV)“ als '
             'Machbarkeitsdimension; Folie 8 stellt beide Achsen gegeneinander. Damit wirkt der Nutzen '
             'auf beiden Achsen, und die Matrix sortiert nicht mehr. Vorschlag für Folie 6: '
             '„④ Compliance — branchenspezifische Vorgaben, Datenschutz, Betriebsratsrechte? Rote '
             'Flaggen: Rechtsgrundlage unklar · Hochrisiko-Einstufung offen · Betriebsrat nicht '
             'eingebunden“. Folie 7: „Neben Daten, Technik, Kompetenz und Compliance …“. Die KNV-Frage '
             'wandert in den Business Case. Das Hand-Out führt seit 18.11. die fünf Dimensionen '
             'Daten · Technik und Infrastruktur · Kompetenz und Betrieb · Compliance · Akzeptanz und '
             'benennt die Achsentrennung ausdrücklich.'),
    dict(id='CL-KIM-T3-02', sev='🟡', wer='du', fund='Folie 2', st='teil',
         titel='MIT NANDA: Selbstauskünfte nicht als gemessenen Befund „des MIT“ darstellen',
         det='Im Hand-Out seit 17.11.: „belegte“ → „berichtete“, die Zurechenbarkeit ist als Deutung der '
             'Autoren gekennzeichnet, der Chip heißt „Fortune über MIT NANDA — Sekundärquelle“.'),
    dict(id='CL-KIM-T3-03', sev='🟡', wer='du', fund='Folie 5, Feld Chancen', st='offen',
         titel='Leitfrage zu „Chancen“ beschreibt eine SO-Strategie statt einer externen Chance',
         det='In der SWOT sind Chancen Umfeldentwicklungen, keine Maßnahmen. Vorschlag: „Welche '
             'Entwicklungen im Markt, in der Technik oder in der Regulierung könnten uns nützen?“ — '
             'die Verbindung zu den eigenen Stärken kommt erst im nächsten Schritt.'),
    dict(id='CL-KIM-T3-04', sev='🟡', wer='du', fund='Folie 6, KNV', st='offen',
         titel='„Positives KNV“ ist als Kriterium nicht bestimmt',
         det='Erledigt sich mit CL-KIM-T3-01, wenn die KNV-Frage aus der Machbarkeit herausgenommen wird.'),
    dict(id='CL-KIM-T3-05', sev='🟡', wer='du', fund='Folien 6, 7, 9, 16', st='offen',
         titel='Machbarkeitscheck der Folien prüft die rechtliche Zulässigkeit nicht',
         det='Auf den Folien steht Recht nur als „DSGVO-Konflikt“ innerhalb der Datendimension. '
             'Mit der Compliance-Dimension aus CL-KIM-T3-01 ist auch dieser Befund erledigt — '
             'und die Übergabe an die KI-Beauftragte:r wird sichtbar.'),
    dict(id='CL-KIM-T3-06', sev='🟡', wer='du', fund='Folie 7', st='offen',
         titel='Aussage zu Beschäftigungseffekten ohne Quelle und ohne Einschränkung',
         det='Die Folie behauptet selektive Effekte in Kundenservice, Softwareentwicklung und Verwaltung. '
             'Belastbare Quellen dafür gibt es, aber mit engen Einschränkungen. Sag Bescheid, dann suche '
             'ich eine zitierfähige Fundstelle und formuliere die Zeile mit dem passenden Vorbehalt.'),
    dict(id='CL-KIM-T3-08', sev='🟡', wer='du', fund='Folie 9', st='offen',
         titel='Übungsdatei mit den zehn Initiativen liegt nicht im Tagesordner',
         det='Im Ordner „Tag 3“ liegen Foliensatz, Hand-Out und die Audioaufnahme. Wenn Du mir die Liste '
             'gibst oder sie beschreibst, baue ich die Übungsdatei und lege sie dort ab.'),
    dict(id='CL-KIM-T3-09', sev='🟡', wer='du', fund='Folie 12, Abschnittszahl', st='teil',
         titel='Abschnittszahl des Canvas auf Folie 12 stimmt nicht',
         det='Im Hand-Out seit 17.11. als Kurzform ausgewiesen, mit Hinweis auf die ausführlichen '
             'Steckbriefe. Die Zahl auf der Folie muss zum Werkzeug passen, das Du im Unterricht '
             'austeilst — sag mir, welches das ist, dann nenne ich Dir die Zahl.'),
    dict(id='CL-KIM-T3-11', sev='🟡', wer='du', fund='Folie 13', st='offen',
         titel='„Scoring“ legt eine Punktwertung nahe — die Einstufung nach Art. 6 ist eine Ja-Nein-Prüfung',
         det='Vorschlag: „Einstufung“ statt „Scoring“. Im Canvas ist der Punktwert inzwischen '
             'ausdrücklich als Orientierung gekennzeichnet, nicht als Prüfmaßstab.'),
    dict(id='CL-KIM-T3-12', sev='🟡', wer='du', fund='Folie 15, Proof of Concept', st='offen',
         titel='PoC soll operativen Nutzen zeigen, läuft aber ohne Produktivbetrieb',
         det='Und es fehlen vorab festgelegte Erfolgs- und Abbruchkriterien. Der PoC klärt eine '
             'Machbarkeitsfrage, nicht den Nutzen — im Canvas steht das so seit dem Durchgang vom 17.11.'),
    dict(id='CL-KIM-T3-13', sev='🟡', wer='du', fund='Folie 15, Rote Flaggen', st='offen',
         titel='Warnung fehlt: im PoC gemessene Modellgüte überschätzt die späteren Werte regelmäßig',
         det='Eine Zeile genügt: „Im PoC gemessene Güte ist eine Obergrenze, keine Prognose.“ Das ist '
             'derselbe Mechanismus, der an Tag 9 unter Überanpassung behandelt wird.'),
    dict(id='CL-KIM-T3-19', sev='🟢', wer='du', fund='Folie 4, Zitat', st='offen',
         titel='Wortlaut und Zuschreibung des Steve-Jobs-Zitats sind nicht belegt',
         det='Entweder eine belegte Fundstelle oder als sinngemäße Wiedergabe kennzeichnen — so wie '
             'beim Malik-Zitat an Tag 1.'),
    dict(id='CL-KIM-T3-20', sev='🟢', wer='du', fund='Folie 10', st='offen',
         titel='Verweis führt in den anderen Kurs',
         det='Teilnehmende, die nur KIM belegen, können dem nicht folgen. Verweis auf den eigenen '
             'Kursweg umstellen oder streichen.'),
    dict(id='CL-KIM-T3-21', sev='🟢', wer='du', fund='Folie 12, Canvas', st='offen',
         titel='Anbieterpflichten für Hochrisiko-Systeme stehen als Regelabschnitte für jeden Use Case',
         det='Die meisten Fälle im Kurs sind Betreiberfälle. Im Canvas führt die Einstufung inzwischen '
             'über die Reihenfolge Definition → Anhang I → Anhang III → Profiling → Filter; die '
             'Anbieterpflichten erscheinen erst, wenn sie greifen.'),
    dict(id='CL-KIM-T3-22', sev='🟢', wer='du', fund='Folie 15', st='offen',
         titel='Verweis auf Woche 3 ist ungenau',
         det='Projektinitialisierung, Meilensteine und Projektstrukturplan kommen schon an Tag 4.'),
    dict(id='CL-KIM-T3-28', sev='⚪', wer='du', fund='Folien 12 und 13', st='offen',
         titel='Feldzahlen des Canvas nicht nachzählbar, Quelle des „Selbstchecks der Zertifizierer“ unklar',
         det='Die Feldzahl hängt daran, welches Werkzeug Du austeilst (siehe CL-KIM-T3-09). Für den '
             'Selbstcheck brauche ich von Dir, woher er stammt — sonst nehme ich die Bezeichnung heraus.'),
]

T3_MEINS = [
    dict(id='CL-KIM-T3-29', sev='⚪', wer='ich', fund='Hand-Out, Mercedes-Fall', st='offen',
         titel='Zwei Detailangaben im Mercedes-Fall an der Primärquelle prüfen',
         det='Betroffen sind der Belegvorbehalt und zwei Zahlenangaben. Ich suche die Primärbelege, '
             'sobald Du freigibst; finde ich sie nicht, nehme ich die Angaben heraus und lasse den Fall '
             'mit den belegten Teilen stehen.'),
    dict(id='CL-KIM-T3-30', sev='⚪', wer='ich', fund='Hand-Out, GAP-Abschnitt', st='offen',
         titel='Entspricht die GAP-Logik der Anwendbarkeitserklärung nach ISO/IEC 42001?',
         det='Die Zuordnung steht im Hand-Out als Brücke zum KI-Beauftragten-Kurs. Ich prüfe sie gegen '
             'die lokale Normausgabe (Anwendbarkeitserklärung, Anhang A) und melde, wenn die Analogie '
             'nicht trägt.'),
    dict(id='MIR-T3-01', sev='🟡', wer='ent', fund='Hand-Out, Abschnitt SMART und Sensitivität', st='offen',
         titel='Rechenbeispiel auf belastbare Größen umstellen — Angebot steht',
         det='Das SMART-Beispiel und die Sensitivitätsbetrachtung rechnen mit Werten, die den Fall '
             'günstig aussehen lassen. Mit Investition 150.000 € und laufenden Kosten 40.000 € käme der '
             'schlechte Fall auf 4,7 % — der Fall kann dann kippen. Du hast beim ROI-Rechner gesagt, '
             'dass Dir das Kippen recht ist; sag Bescheid, dann ziehe ich es hier genauso nach.'),
]

T3_FERTIG = [
    ('CL-KIM-T3-07', '🟡', 'Matrix: verankerte Skala 1–5 je Achse, hoch ab 3,5, mit Herkunft', '17.11.2026'),
    ('CL-KIM-T3-10', '🟡', 'Canvas-Feld ⑥ um die Kostenseite erweitert (einmalig, laufend, Nebenwirkungen)', '17.11.2026'),
    ('CL-KIM-T3-14', '🟡', 'BCG modelliert Wertpotenzial und beobachtet keine Budgets — am Primärtext bestätigt', '17.11.2026'),
    ('CL-KIM-T3-15', '🟡', 'Canvas-Nummerierung bereinigt (③ doppelt, ⑦ fehlte)', '17.11.2026'),
    ('CL-KIM-T3-16', '🟡', 'Quick Wins als Annahme gekennzeichnet, mit Zielwert und Stopp-Kriterium', '17.11.2026'),
    ('CL-KIM-T3-17', '🟡', 'Engpass: Superlativ gestrichen, Richtung statt Rangfolge', '17.11.2026'),
    ('CL-KIM-T3-18', '🟡', 'SMART-Beispiel neu: Median, Messdefinition, 24 → unter 4 Arbeitsstunden', '17.11.2026'),
    ('CL-KIM-T3-23', '🟢', 'Haftungshinweis in der Fußzeile ergänzt', '18.11.2026'),
    ('CL-KIM-T3-24', '🟢', 'MIT-NANDA-Chip als Sekundärquelle benannt, Bericht gesondert geführt', '17.11.2026'),
    ('CL-KIM-T3-25', '🟢', 'Canvas-Leitfrage ② fragt nach Tätigkeit und Datenart, Mehrfachnennung erlaubt', '17.11.2026'),
    ('CL-KIM-T3-26', '🟢', 'SMART: Median statt Mittelwert, Messdefinition ergänzt', '17.11.2026'),
    ('CL-KIM-T3-27', '⚪', 'Bildherkunft und Lizenz der Folien 1, 8, 9, 10, 15 vom Dozenten geprüft', '18.11.2026'),
    ('CL-KIM-T3-31', '⚪', 'Normbezeichnung DIN EN ISO/IEC 42001 am Deckblatt bestätigt', '17.11.2026'),
]

TAGE = [
    dict(nr=1, titel='Einführung und KI-Grundlagen',
         datei='KI-Manager/Tag 1 · Tag1_HandOut.html · 1-KIM-Grundlagen-der-KI.pptx',
         offen=T1_OFFEN + T1_MEINS, fertig=T1_FERTIG, gesamt=49),
    dict(nr=2, titel='Wo stehen wir — und wie steuern wir?',
         datei='KI-Manager/Tag 2 · Tag2_HandOut.html · Foliensatz Tag 2',
         offen=T2_OFFEN + T2_MEINS, fertig=T2_FERTIG, gesamt=34),
    dict(nr=3, titel='KI-Anwendungsfälle · Welche KI — und wer macht was?',
         datei='KI-Manager/Tag 3 · Tag3_HandOut.html · 3-KIM-SWOT-Analyse-und-Use-Cases.pdf',
         offen=T3_OFFEN + T3_MEINS, fertig=T3_FERTIG, gesamt=31),
]
