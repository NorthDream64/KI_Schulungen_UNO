# -*- coding: utf-8 -*-
"""Schreibt den Tag-3-Block in daten.py fort: 12 neue Fertig-Eintraege, 9 neue offene Punkte."""
import re, textwrap, hashlib, os

BASE = os.path.expanduser('~/mnt/KI_Schulungen_UNO/Werkzeuge/umsetzungsstand')
PROT = os.path.expanduser('~/mnt/Schulungsmaterial/Reviewer/Entscheidungsprotokoll.md')

# --- Entscheidungen des neuen Abschnitts aus dem Protokoll lesen
prot = open(PROT, encoding='utf-8').read()
ab = prot.index('## KIM Tag 3 · KI-Anwendungsfälle', prot.index('## KIM Handreichung'))
neu = {}
for z in prot[ab:].split('\n'):
    m = re.match(r'\| (CL-KIM-T3-\d+) \| (\S+) [^|]*\| ([^|]*)\| ([^|]*)\| (\S[^|]*)\|', z)
    if m:
        neu[m.group(1)] = dict(sev=m.group(2), fund=m.group(3).strip(),
                               kurz=m.group(4).strip(), ent=m.group(5).strip())
print("Zeilen gelesen:", len(neu))
fertig = {k: v for k, v in neu.items() if v['ent'] in ('erledigt', 'übernommen')}
offen = [k for k, v in neu.items() if v['ent'] == 'offen']
print("fertig:", len(fertig), "| offen:", len(offen), offen)

# --- 9 offene Punkte mit Zustaendigkeit und Empfehlung
WER = {'CL-KIM-T3-32': 'ent', 'CL-KIM-T3-33': 'ent', 'CL-KIM-T3-34': 'ent', 'CL-KIM-T3-35': 'ent',
       'CL-KIM-T3-36': 'ent', 'CL-KIM-T3-47': 'ich', 'CL-KIM-T3-49': 'du', 'CL-KIM-T3-50': 'du',
       'CL-KIM-T3-51': 'ich'}
TITEL = {
 'CL-KIM-T3-32': 'Erfolgsfaktoren und Erfolgskriterien in Leitfrage ③ trennen',
 'CL-KIM-T3-33': 'Braucht ein schneller Erfolg auch eine Wirtschaftlichkeitsrechnung?',
 'CL-KIM-T3-34': '„Scheitern selten an der Modellgüte“ — Häufigkeitsbehauptung ohne Beleg',
 'CL-KIM-T3-35': 'Mittelwert pauschal als falsch bezeichnet',
 'CL-KIM-T3-36': 'Das Studienkapitel wirkt belegter, als die Daten tragen',
 'CL-KIM-T3-47': 'NANDA-Aussage zum Haupthemmnis nicht am Primärtext prüfbar',
 'CL-KIM-T3-49': 'Mercedes-Fall: rechtliche Seite nicht bewertet',
 'CL-KIM-T3-50': 'Mercedes-Fall: Tag-5-Hinweis aus PM-Sicht nicht bewertet',
 'CL-KIM-T3-51': 'Digital-Omnibus-Link nicht geprüft',
}
DET = {
 'CL-KIM-T3-32': 'Die Leitfrage setzt kritische Erfolgsfaktoren (Voraussetzungen) mit Erfolgskriterien '
   'gleich (woran Erfolg gemessen wird). Der Einwand trägt — berührt aber T3-15, wo die KEF-Frage am '
   '17.11. bewusst nach ③ gewandert ist. Vorschlag: beide Fragen in ③ nebeneinander stellen, erst die '
   'Kennzahl mit Zielwert, dann die Voraussetzungen.',
 'CL-KIM-T3-33': 'Hier widerspricht Claudia Deiner Entscheidung vom 18.11. (T3-01, Achsentrennung). Ihr '
   'Argument ist feiner: Die Doppelzählung betrifft nur das Kosten-Nutzen-Verhältnis, nicht die '
   'Aufwandshöhe; in Impact-Effort-Matrizen ist Aufwand eine übliche Achse. Mein Vorschlag: '
   'Achsentrennung bleibt, ein Satz ergänzt, dass auch ein schneller Erfolg Zielwert, Aufwand und eine '
   'kleine Wirtschaftlichkeitsrechnung bekommt.',
 'CL-KIM-T3-34': 'Der Satz behauptet eine Häufigkeit ohne Beleg und steht im selben Kasten wie '
   '„Belastbar ist die Richtung, nicht die Rangfolge“. Bei generativen Anwendungen ist die '
   'Ergebnisqualität ein zentraler Machbarkeitspunkt, der in den fünf Dimensionen nur in der Querfrage '
   'steckt. Vorschlag: Superlativ abschwächen und die Ergebnisqualität ausdrücklich nennen.',
 'CL-KIM-T3-35': 'Berechtigt: Mittelwert mal Fallzahl ergibt gerade die Kapazität für die ROI-Rechnung, '
   'und eine kürzere Durchlaufzeit ist kein Bearbeitungsaufwand. Vorschlag: Median als Service-Ziel, '
   'Mittelwert für die Mengenrechnung — beides benannt, statt den Mittelwert pauschal für falsch zu '
   'erklären.',
 'CL-KIM-T3-36': 'Die NANDA-Einsparungen sind Selbstauskünfte und Einzelbeispiele, und die drei Größen '
   'stammen aus verschiedenen Erhebungen (BCG: KI insgesamt, 1.250 Befragte; NANDA: generative KI). '
   'Vorschlag: einen Satz zur eingeschränkten Vergleichbarkeit ergänzen.',
 'CL-KIM-T3-47': 'Das Primär-PDF des Berichts ist nicht abrufbar (HTTP 404), die Aussage „der '
   'NANDA-Bericht widerspricht der Vorstellung, Daten seien das Haupthemmnis, ausdrücklich“ also nicht '
   'prüfbar. Vorschlag: auf das abschwächen, was die Sekundärberichte tragen — oder streichen.',
 'CL-KIM-T3-49': 'Übergabe zwischen den Perspektiven: Rechenzentren in Europa und Austauschbarkeit der '
   'Modellanbieter hat keine Perspektive rechtlich bewertet. Erledigt sich mit dem nächsten Lauf von '
   '/claudia oder einem gezielten /compliance-review.',
 'CL-KIM-T3-50': 'Übergabe zwischen den Perspektiven: Der Hinweis „Austauschbarkeit als Thema für Tag 5“ '
   'ist aus PM-Sicht (Build vs. Buy) nicht bewertet. Gegenprobe von mir: Tag 5 behandelt Plattform, '
   'Agenten und „selbst bauen oder zukaufen“ — der Verweis trägt inhaltlich.',
 'CL-KIM-T3-51': 'Der Abruf des Links ist zweimal an einer unbeantworteten Freigabeanfrage gescheitert, '
   'nicht an der Seite. Über den Link selbst sage ich deshalb nichts. Nachholen, sobald die Freigabe '
   'durchgeht.',
}

eintraege = []
for kid in offen:
    v = neu[kid]
    eintraege.append("    dict(id=%r, sev=%r, wer=%r, fund=%r, st='offen',\n"
                     "         titel=%r,\n         det=%r),\n"
                     % (kid, v['sev'], WER[kid], v['fund'], TITEL[kid], DET[kid]))

# --- 12 Fertig-Tupel
def kurz(t, n=150):
    t = re.sub(r'^\[[^\]]*\] ', '', t)
    return (t[:n].rsplit(' ', 1)[0] + ' …') if len(t) > n else t
tupel = []
for kid in sorted(fertig, key=lambda k: int(re.search(r'\d+$', k).group())):
    v = fertig[kid]
    vorsatz = '' if v['ent'] == 'erledigt' else 'übernommen · '
    kopf = "    (%r, %r, " % (kid, v['sev'])
    einr = ' ' * len(kopf)
    stck = textwrap.wrap(vorsatz + kurz(v['kurz']), 100 - len(einr))
    txt = ('\n' + einr).join(repr(x + (' ' if i < len(stck) - 1 else '')) for i, x in enumerate(stck))
    tupel.append(f"{kopf}{txt},\n{einr}'24.11.2026'),\n")

# --- einsetzen
P = os.path.join(BASE, 'daten.py')
s = open(P, encoding='utf-8').read()
v0 = hashlib.sha256(s.encode()).hexdigest()[:8]
i = s.index('T3_MEINS = [')                       # vor T3_MEINS: ans Ende von T3_OFFEN
j = s.rindex(']\n\n', 0, i)
s = s[:j] + ''.join(eintraege) + s[j:]
k = s.index('TAGE = [')
l = s.rindex(']\n\n', 0, k)                        # Ende von T3_FERTIG
s = s[:l] + ''.join(tupel) + s[l:]
s = s.replace("offen=T3_OFFEN + T3_MEINS, fertig=T3_FERTIG, gesamt=31",
              "offen=T3_OFFEN + T3_MEINS, fertig=T3_FERTIG, gesamt=52")
open(P, 'w', encoding='utf-8', newline='').write(s)
print('daten.py sha', v0, '->', hashlib.sha256(s.encode()).hexdigest()[:8])
