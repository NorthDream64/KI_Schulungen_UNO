#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Formalcheck für die Kursmaterialien (Hand-Outs, Handreichungen, Referenzdokumente).

Aufruf:
    python3 formalcheck.py datei.html [weitere.html ...]
    python3 formalcheck.py --alle "/pfad/zum/Schulungsmaterial"

Geprüft wird:
  1. CSS-Klassen      — jede im Rumpf benutzte Klasse muss in einem <style>-Block definiert sein.
                        Alle <style>-Blöcke werden gelesen, Template-Literale ${...} ausgeblendet.
  2. Tag-Balance      — Öffner und Schließer je Elementtyp, Leerelemente ausgenommen.
  3. Verschachtelung  — jeder Abschnitt (class="section") muss auf derselben Tiefe beginnen.
  4. Tabellen         — Spaltenzahl je Zeile, **mit Auflösung von colspan UND rowspan**.
  5. Pflichtstücke    — @media print und der Rechtevermerk müssen vorhanden sein.
  6. Verweise         — doppelte und schemalose Links.

Zu Punkt 4: Eine Tabelle mit rowspan hat von Natur aus weniger <td> in den Folgezeilen,
weil eine Zelle aus der Zeile darüber hineinragt. Wer nur <td> zählt, meldet dort einen
Fehler, der keiner ist. Dieses Skript führt ein Belegungsraster mit und zählt die
hineinragenden Zellen mit — deshalb keine Fehlalarme mehr bei Risikomatrizen.

Rückgabewert: 0 wenn alles sauber, sonst 1.
"""

import re
import sys
import glob
import os
import collections

LEERELEMENTE = {"br", "hr", "img", "meta", "link", "input", "source", "col", "area", "base", "embed", "track", "wbr"}


def stylebloecke(html):
    return "".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S))


def rumpf(html):
    """
    Dokument ohne <style>- und <script>-Blöcke und ohne Template-Literale.

    Die <script>-Blöcke müssen raus, sonst liest die Tag-Erkennung JavaScript
    als HTML: Vergleiche wie `a < b`, Klassennamen in Zeichenketten und
    Template-Literale erzeugen sonst Dutzende Scheinbefunde.
    """
    h = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.S)
    h = re.sub(r"<script[^>]*>.*?</script>", "", h, flags=re.S)
    return re.sub(r"\$\{[^}]*\}", "", h)


def pruefe_klassen(html):
    definiert = set(re.findall(r"\.([a-zA-Z][\w-]*)", stylebloecke(html)))
    benutzt = set()
    for m in re.findall(r'class="([^"]+)"', rumpf(html)):
        benutzt.update(m.split())
    return sorted(benutzt - definiert)


def pruefe_balance(html):
    zaehler = collections.Counter()
    for m in re.finditer(r"<(/?)([a-zA-Z][\w-]*)([^>]*?)(/?)>", rumpf(html)):
        schliesser, name, _, selbst = m.groups()
        if name.lower() in LEERELEMENTE or selbst == "/":
            continue
        zaehler[name.lower()] += -1 if schliesser else 1
    return {k: v for k, v in zaehler.items() if v != 0}


def pruefe_verschachtelung(html):
    """Alle Abschnitte sollten auf derselben Tiefe beginnen."""
    tiefe = 0
    tiefen = []
    for m in re.finditer(r"<(/?)div([^>]*)>", html):
        if not m.group(1) and re.search(r'class="section[" ]', m.group(2)):
            titel = re.search(r'<div class="section-title">(.*?)</div>', html[m.start():m.start() + 600], re.S)
            name = re.sub(r"<[^>]+>", "", titel.group(1)).strip()[:55] if titel else "(ohne Titel)"
            tiefen.append((tiefe, name))
        tiefe += -1 if m.group(1) else 1
    if not tiefen:
        return [], tiefe
    soll = collections.Counter(t for t, _ in tiefen).most_common(1)[0][0]
    return [(t, n) for t, n in tiefen if t != soll], tiefe


def spalten_einer_tabelle(tabelle):
    """
    Spaltenzahl je Zeile unter Auflösung von colspan und rowspan.

    Geführt wird ein Belegungsraster: ueberhang hält für jede durch ein rowspan
    vorbelegte Spalte, für wie viele *weitere* Zeilen sie noch belegt ist.

    Wichtig ist die Reihenfolge am Zeilenende: In der Zeile, in der ein rowspan
    deklariert wird, zählt die Zelle bereits als eigene Zelle — der Überhang
    beginnt erst in der Folgezeile. Neu entstandene Überhänge werden deshalb
    erst nach dem Herunterzählen der alten übernommen. Ohne diese Trennung
    fehlt der letzten Zeile genau eine Spalte.
    """
    zeilen = re.findall(r"<tr.*?</tr>", tabelle, re.S)
    ueberhang = []          # Liste verbleibender Zeilen je vorbelegter Spalte
    ergebnis = []
    for zeile in zeilen:
        belegt = len(ueberhang)
        eigene = 0
        neu = []
        for z in re.finditer(r"<(t[dh])([^>]*)>", zeile):
            attr = z.group(2)
            cs = re.search(r'colspan=["\']?(\d+)', attr)
            rs = re.search(r'rowspan=["\']?(\d+)', attr)
            c = int(cs.group(1)) if cs else 1
            r = int(rs.group(1)) if rs else 1
            eigene += c
            if r > 1:
                neu.extend([r - 1] * c)
        ergebnis.append(belegt + eigene)
        ueberhang = [v - 1 for v in ueberhang if v - 1 > 0] + neu
    return ergebnis


def pruefe_tabellen(html):
    auffaellig = []
    for nr, tabelle in enumerate(re.findall(r"<table.*?</table>", rumpf(html), re.S), 1):
        spalten = spalten_einer_tabelle(tabelle)
        if len(set(spalten)) > 1:
            auffaellig.append((nr, spalten, "rowspan" in tabelle))
    return auffaellig


def pruefe_pflichtstuecke(html):
    """
    Rechtevermerk und Druckregel gehören in jedes Teilnehmerdokument — aber
    nicht in Quizze, Werkzeuge oder von Teilnehmenden eingereichte Arbeiten.
    Deshalb werden sie getrennt gemeldet und nicht als Strukturfehler gezählt.
    """
    fehlt = []
    if "@media print" not in html:
        fehlt.append("@media print")
    if "rechtevermerk" not in html:
        fehlt.append("Rechtevermerk")
    return fehlt


def pruefe_verweise(html):
    links = re.findall(r'href="([^"]+)"', html)
    extern = [u for u in links if u.startswith("http")]
    doppelt = [u for u, c in collections.Counter(extern).items() if c > 1]
    schemalos = [u for u in links if u.startswith("www.")]
    return sorted(doppelt), sorted(schemalos)


def pruefe_datei(pfad):
    with open(pfad, encoding="utf-8") as f:
        html = f.read()

    befunde = []

    k = pruefe_klassen(html)
    if k:
        befunde.append(f"undefinierte CSS-Klassen: {', '.join(k)}")

    b = pruefe_balance(html)
    if b:
        befunde.append(f"unbalancierte Tags: {b}")

    abw, endtiefe = pruefe_verschachtelung(html)
    for t, n in abw:
        befunde.append(f"Abschnitt auf abweichender Tiefe {t}: {n}")
    if endtiefe != 0:
        befunde.append(f"am Dateiende {endtiefe} div nicht geschlossen")

    for nr, spalten, hat_rowspan in pruefe_tabellen(html):
        zusatz = " (enthält rowspan — Raster bereits aufgelöst, also echte Abweichung)" if hat_rowspan else ""
        befunde.append(f"Tabelle {nr}: ungleiche Spaltenzahl {spalten}{zusatz}")

    fehlende = pruefe_pflichtstuecke(html)

    # Mehrfach verlinkte Adressen sind in Quellenverzeichnissen normal (dieselbe
    # Arbeit an zwei Stellen zitiert) und deshalb kein Befund, sondern ein Hinweis.
    doppelt, schemalos = pruefe_verweise(html)
    if schemalos:
        befunde.append(f"Verweise ohne Schema: {', '.join(schemalos)}")

    hinweise = []
    if fehlende:
        hinweise.append("fehlt: " + ", ".join(fehlende))
    if doppelt:
        hinweise.append(f"{len(doppelt)} Adresse(n) mehrfach verlinkt — in Quellenverzeichnissen meist beabsichtigt")

    return befunde, hinweise, fehlende


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 1

    # --aus MUSTER schließt Pfade aus (mehrfach erlaubt); sinnvoll für von
    # Teilnehmenden eingereichte Arbeiten und fremderzeugte Exporte.
    ausschluss = []
    while "--aus" in args:
        i = args.index("--aus")
        ausschluss.append(args[i + 1])
        del args[i:i + 2]

    if args and args[0] == "--alle":
        wurzel = args[1] if len(args) > 1 else "."
        dateien = sorted(glob.glob(os.path.join(wurzel, "**", "*.html"), recursive=True))
    else:
        dateien = args
    if ausschluss:
        dateien = [d for d in dateien if not any(m in d for m in ausschluss)]

    fehler = 0
    ohne_vermerk = []
    for pfad in dateien:
        befunde, hinweise, fehlende = pruefe_datei(pfad)
        name = os.path.relpath(pfad)
        if fehlende:
            ohne_vermerk.append((name, fehlende))
        if befunde:
            fehler += 1
            print(f"\n✗ {name}")
            for b in befunde:
                print(f"    · {b}")

    print(f"\n{len(dateien)} Datei(en) geprüft, {fehler} mit Strukturbefund.")
    if ohne_vermerk:
        print(f"\nGetrennt davon — Rechtevermerk oder Druckregel fehlt in {len(ohne_vermerk)} Datei(en):")
        for name, fehlende in ohne_vermerk[:40]:
            print(f"    · {name}  ({', '.join(fehlende)})")
        if len(ohne_vermerk) > 40:
            print(f"    … und {len(ohne_vermerk) - 40} weitere")
        print("    (Bei Quizzen, Werkzeugen und eingereichten Arbeiten ist das in Ordnung.)")
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main())
