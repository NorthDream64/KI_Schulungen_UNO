# -*- coding: utf-8 -*-
"""Erzeugt Umsetzungsstand_Kurstage.html aus daten.py."""
import html as H
import re
import hashlib
from daten import QUER, QUER_FERTIG, TAGE

HEUTE = '22.11.2026'

WER_LABEL = {'du': 'Bei Dir', 'ich': 'Bei mir', 'ent': 'Entscheidung'}
WER_TITEL = {'du': 'Bei Dir · Foliensatz und Präsentation',
             'ich': 'Bei mir · Hand-Out, Handreichungen, Register',
             'ent': 'Zur Entscheidung · danach baue ich'}

CSS = """
  :root{--blue:#1a3a5c;--gruen:#2a7a3a;--kim:#1a3a5c;--quer:#7a5a1a;--bg:#f0f2f5;
        --card:#fff;--rule:#e0e0e0;--du:#8a4a1a;--ich:#1a5a7a;--ent:#6a3a7a}
  *{box-sizing:border-box}
  body{font-family:Arial,Helvetica,sans-serif;font-size:13px;margin:0;background:var(--bg);color:#222}
  h1{background:var(--blue);color:#fff;margin:0;padding:14px 16px;font-size:17px;line-height:1.3}
  .subtitle{background:#2a4a6c;color:#cde;padding:6px 16px;font-size:12px}
  .legend{background:#fff;padding:8px 16px;border-bottom:1px solid var(--rule);font-size:11.5px;color:#555;line-height:1.7}
  .hinweis{background:#fff8e6;border:1px solid #e8d4a0;border-radius:6px;margin:12px 16px;padding:10px 14px;font-size:12px;line-height:1.55}
  .hinweis b{color:#7a4a00}

  /* Werkzeugleiste */
  .bar{position:sticky;top:0;z-index:20;background:#fff;border-bottom:1px solid var(--rule);
       padding:8px 16px;display:flex;flex-wrap:wrap;gap:6px;align-items:center}
  .bar button{font:inherit;font-size:11.5px;padding:4px 9px;border:1px solid #c0c8d4;background:#f7f9fc;
       border-radius:5px;cursor:pointer;color:#234}
  .bar button:hover{background:#eaf0f8}
  .bar button.an{background:var(--blue);border-color:var(--blue);color:#fff}
  .bar .sep{width:1px;height:20px;background:var(--rule);margin:0 4px}
  .fortschritt{flex:1;min-width:150px;display:flex;align-items:center;gap:8px}
  .balken{flex:1;height:9px;background:#e4e8ee;border-radius:5px;overflow:hidden;min-width:60px}
  .balken i{display:block;height:100%;width:0;background:var(--gruen);transition:width .25s}
  .fz{font-size:11.5px;color:#456;white-space:nowrap;font-weight:bold}

  /* Tagesblöcke */
  .day-block{background:var(--card);border:1px solid var(--rule);border-radius:8px;margin:12px 16px;overflow:hidden}
  .day-header{display:flex;flex-wrap:wrap;align-items:center;gap:10px;background:var(--kim);color:#fff;padding:9px 14px}
  .day-block.quer .day-header{background:var(--quer)}
  .day-num{font-size:15px;font-weight:bold}
  .day-label{flex:1;font-size:13px;opacity:.92;min-width:120px}
  .day-count{font-size:11px;background:rgba(255,255,255,.22);padding:2px 8px;border-radius:10px;white-space:nowrap}
  .day-topic{background:#e8f0fe;padding:6px 14px;font-size:11.5px;color:#345;border-bottom:1px solid #c5d4f0}
  .grp{padding:10px 14px 2px}
  .grp-title{font-size:11.5px;font-weight:bold;text-transform:uppercase;letter-spacing:.04em;
       color:#567;border-bottom:1px solid var(--rule);padding-bottom:4px;margin-bottom:9px}
  .grp.du .grp-title{color:var(--du);border-bottom-color:#e8cdb8}
  .grp.ich .grp-title{color:var(--ich);border-bottom-color:#b8d4e8}
  .grp.ent .grp-title{color:var(--ent);border-bottom-color:#d8c4e8}
  .grp-zahl{font-weight:normal;color:#8a9aaa;letter-spacing:0;text-transform:none}
  .leer{color:#999;font-style:italic;font-size:12px;margin:0 0 10px}

  /* Einzelpunkt */
  .pt{display:grid;grid-template-columns:20px 1fr;gap:9px;border:1px solid #ddd;border-radius:5px;
       padding:9px 11px;margin-bottom:9px;border-left:4px solid #bbb;background:#fff}
  .pt.du{border-left-color:var(--du)}
  .pt.ich{border-left-color:var(--ich)}
  .pt.ent{border-left-color:var(--ent)}
  .pt input[type=checkbox]{width:17px;height:17px;margin:1px 0 0;cursor:pointer;accent-color:#2a7a3a}
  .pt.ab{background:#f6faf6;border-color:#cde0cd}
  .pt.ab .pt-titel{text-decoration:line-through;color:#678}
  .pt-kopf{display:flex;flex-wrap:wrap;gap:6px;align-items:baseline;margin-bottom:3px}
  .pid{font-size:10.5px;font-weight:bold;color:#678;font-family:Consolas,monospace}
  .sev{font-size:11px}
  .marke{font-size:10px;padding:1px 6px;border-radius:8px;background:#eef2f7;color:#456;white-space:nowrap}
  .marke.du{background:#fbf0e6;color:var(--du)}
  .marke.ich{background:#e6f0fb;color:var(--ich)}
  .marke.ent{background:#f3e9fb;color:var(--ent)}
  .marke.teil{background:#fff4d6;color:#7a5a00}
  .fundst{font-size:10.5px;color:#789}
  .pt-titel{font-weight:bold;line-height:1.4;margin:0 0 4px}
  .pt-det{font-size:12px;color:#445;line-height:1.55;margin:0}
  .ts{font-size:10.5px;color:#2a7a3a;margin-top:4px}

  /* Erledigtes */
  details.fertig{margin:0 14px 12px;border:1px solid #dde4dd;border-radius:6px;background:#fafcfa}
  details.fertig>summary{cursor:pointer;padding:7px 11px;font-size:12px;font-weight:bold;color:#3a6a3a}
  details.fertig>summary::marker{color:#8ab08a}
  .fliste{margin:0;padding:2px 11px 10px 11px;list-style:none}
  .fliste li{font-size:12px;color:#556;padding:3px 0;border-top:1px dotted #e0e6e0;line-height:1.45}
  .fliste li:first-child{border-top:0}
  .fliste .pid{margin-right:6px}
  .fliste .d{color:#8a9a8a;font-size:10.5px;white-space:nowrap}

  /* Übergabe */
  .uebergabe{background:#fff;border:1px solid var(--rule);border-radius:8px;margin:12px 16px;padding:11px 14px}
  .uebergabe h2{font-size:13px;margin:0 0 6px;color:var(--blue)}
  .uebergabe p{font-size:12px;color:#456;margin:0 0 7px;line-height:1.55}
  textarea{width:100%;min-height:92px;font-family:Consolas,monospace;font-size:11.5px;
       border:1px solid #c8d0da;border-radius:5px;padding:7px;resize:vertical;color:#234;background:#fbfcfd}
  footer{padding:14px 16px 26px;font-size:11px;color:#789;line-height:1.6}

  @media (max-width:520px){
    .pt{grid-template-columns:18px 1fr;gap:7px;padding:8px 9px}
    .day-block,.hinweis,.uebergabe{margin-left:8px;margin-right:8px}
    details.fertig{margin-left:8px;margin-right:8px}
    h1{font-size:15px}
    .bar{padding:7px 8px}
    .fortschritt{flex:1 0 100%;order:9}
    .fz{white-space:normal}
    #meldung{flex:1 0 100%;order:10}
  }
  @media print{
    .bar,.uebergabe,.no-print{display:none!important}
    body{background:#fff}
    .day-block{break-inside:auto;page-break-inside:auto}
    .day-header{-webkit-print-color-adjust:exact;print-color-adjust:exact}
    details.fertig{display:none}
    .pt{break-inside:avoid}
  }
"""

JS = r"""
(function () {
  var KEY = 'umsetzungsstand.kim.v1';
  var stand = {};
  try { stand = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { stand = {}; }

  function sichern() {
    try { localStorage.setItem(KEY, JSON.stringify(stand)); } catch (e) {}
  }
  function heute() {
    var d = new Date();
    function z(n) { return (n < 10 ? '0' : '') + n; }
    return z(d.getDate()) + '.' + z(d.getMonth() + 1) + '.' + d.getFullYear();
  }

  var punkte = [].slice.call(document.querySelectorAll('.pt[data-id]'));

  function zeichnen() {
    var offenGes = 0, offenAb = 0, jeTag = {};
    punkte.forEach(function (p) {
      var id = p.dataset.id, tag = p.dataset.tag;
      var box = p.querySelector('input[type=checkbox]');
      if (p.dataset.fertig === '1') return;
      offenGes++;
      jeTag[tag] = jeTag[tag] || { ab: 0, ges: 0 };
      jeTag[tag].ges++;
      var ab = !!(stand[id] && stand[id].ab);
      if (box) box.checked = ab;
      p.classList.toggle('ab', ab);
      var ts = p.querySelector('.ts');
      if (ts) ts.textContent = ab ? 'abgehakt am ' + (stand[id].d || heute()) : '';
      if (ab) { offenAb++; jeTag[tag].ab++; }
    });

    var pz = offenGes ? Math.round(offenAb / offenGes * 100) : 100;
    var b = document.querySelector('.balken i'); if (b) b.style.width = pz + '%';
    var fz = document.querySelector('.fz');
    if (fz) fz.textContent = offenAb + ' von ' + offenGes + ' offenen Punkten erledigt (' + pz + ' %)';

    Object.keys(jeTag).forEach(function (t) {
      var el = document.querySelector('[data-count="' + t + '"]');
      if (!el) return;
      var o = jeTag[t].ges - jeTag[t].ab;
      el.textContent = o === 0 ? 'alle ' + jeTag[t].ges + ' erledigt'
                               : o + ' offen von ' + jeTag[t].ges;
    });

    gruppenZaehlen();
    uebergabeText(offenAb, offenGes);
  }

  function gruppenZaehlen() {
    [].slice.call(document.querySelectorAll('.grp')).forEach(function (g) {
      var ps = g.querySelectorAll('.pt[data-id]');
      var o = 0;
      [].slice.call(ps).forEach(function (p) {
        if (p.dataset.fertig === '1') return;
        if (!(stand[p.dataset.id] && stand[p.dataset.id].ab)) o++;
      });
      var z = g.querySelector('.grp-zahl');
      if (z) z.textContent = o ? '(' + o + ' offen)' : '(erledigt)';
    });
  }

  function uebergabeText(ab, ges) {
    var zeilen = ['UMSETZUNGSSTAND KI-Manager:in — Tage 1 bis 3',
                  'Stand: ' + heute() + ' · ' + ab + ' von ' + ges + ' offenen Punkten erledigt', ''];
    var abgehakt = [];
    punkte.forEach(function (p) {
      if (p.dataset.fertig === '1') return;
      var s = stand[p.dataset.id];
      if (s && s.ab) abgehakt.push('  ' + p.dataset.id + '  (' + (s.d || '') + ')  ' + p.dataset.kurz);
    });
    if (abgehakt.length) { zeilen.push('Neu abgehakt:'); zeilen = zeilen.concat(abgehakt); }
    else { zeilen.push('Neu abgehakt: nichts'); }
    zeilen.push('');
    ['1', '2', '3'].forEach(function (t) {
      var el = document.querySelector('[data-count="T' + t + '"]');
      if (el) zeilen.push('Tag ' + t + ': ' + el.textContent);
    });
    var ta = document.getElementById('uebergabe');
    if (ta) ta.value = zeilen.join('\n');
  }

  document.addEventListener('change', function (ev) {
    var box = ev.target;
    if (!box || box.type !== 'checkbox') return;
    var p = box.closest('.pt'); if (!p || !p.dataset.id) return;
    if (p.dataset.fertig === '1') { box.checked = true; return; }
    if (box.checked) stand[p.dataset.id] = { ab: true, d: heute() };
    else delete stand[p.dataset.id];
    sichern(); zeichnen();
  });

  /* Filter */
  var filter = 'alle';
  function filtern(f) {
    filter = f;
    [].slice.call(document.querySelectorAll('.bar [data-filter]')).forEach(function (b) {
      b.classList.toggle('an', b.dataset.filter === f);
    });
    punkte.forEach(function (p) {
      var zeig = true;
      var ab = p.dataset.fertig === '1' || !!(stand[p.dataset.id] && stand[p.dataset.id].ab);
      if (f === 'offen') zeig = !ab;
      else if (f === 'du' || f === 'ich' || f === 'ent') zeig = (p.dataset.wer === f);
      p.style.display = zeig ? '' : 'none';
    });
    [].slice.call(document.querySelectorAll('.grp')).forEach(function (g) {
      var sicht = [].slice.call(g.querySelectorAll('.pt')).some(function (p) { return p.style.display !== 'none'; });
      var leer = g.querySelector('.leer');
      g.style.display = (sicht || (leer && f === 'alle')) ? '' : 'none';
    });
    [].slice.call(document.querySelectorAll('.day-block')).forEach(function (d) {
      var sicht = [].slice.call(d.querySelectorAll('.grp')).some(function (g) { return g.style.display !== 'none'; });
      d.style.display = sicht ? '' : 'none';
    });
  }

  function alleKlapp(auf) {
    [].slice.call(document.querySelectorAll('details.fertig')).forEach(function (d) { d.open = auf; });
  }

  function kopieren() {
    var ta = document.getElementById('uebergabe');
    if (!ta) return;
    ta.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (e) {}
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(ta.value).then(function () { melden('In die Ablage kopiert — in den Chat einfügen.'); },
        function () { melden(ok ? 'In die Ablage kopiert.' : 'Bitte den Text unten markieren und kopieren.'); });
    } else {
      melden(ok ? 'In die Ablage kopiert.' : 'Bitte den Text unten markieren und kopieren.');
    }
  }

  function melden(t) {
    var m = document.getElementById('meldung');
    if (!m) return;
    m.textContent = t;
    setTimeout(function () { if (m.textContent === t) m.textContent = ''; }, 6000);
  }

  function speichern() {
    var d = { datei: 'Umsetzungsstand KIM Tage 1-3', stand: heute(), punkte: stand };
    var b = new Blob([JSON.stringify(d, null, 1)], { type: 'application/json' });
    var a = document.createElement('a');
    a.href = URL.createObjectURL(b);
    a.download = 'Umsetzungsstand_KIM.json';
    document.body.appendChild(a); a.click(); document.body.removeChild(a);
    melden('Datei Umsetzungsstand_KIM.json gespeichert — in den Ordner Reviewer legen, dann lese ich sie.');
  }

  function laden(ev) {
    var f = ev.target.files && ev.target.files[0];
    if (!f) return;
    var r = new FileReader();
    r.onload = function () {
      try {
        var d = JSON.parse(r.result);
        stand = (d && d.punkte) ? d.punkte : (d || {});
        sichern(); zeichnen(); filtern(filter);
        melden('Stand geladen.');
      } catch (e) { melden('Die Datei ließ sich nicht lesen.'); }
    };
    r.readAsText(f);
    ev.target.value = '';
  }

  function zuruecksetzen() {
    if (!confirm('Alle Haken der offenen Punkte entfernen?')) return;
    stand = {}; sichern(); zeichnen(); filtern(filter);
  }

  document.querySelector('.bar').addEventListener('click', function (ev) {
    var b = ev.target.closest('button'); if (!b) return;
    if (b.dataset.filter) filtern(b.dataset.filter);
    else if (b.dataset.akt === 'auf') alleKlapp(true);
    else if (b.dataset.akt === 'zu') alleKlapp(false);
    else if (b.dataset.akt === 'kopieren') kopieren();
    else if (b.dataset.akt === 'speichern') speichern();
    else if (b.dataset.akt === 'laden') document.getElementById('dateiwahl').click();
    else if (b.dataset.akt === 'reset') zuruecksetzen();
    else if (b.dataset.akt === 'drucken') window.print();
  });
  document.getElementById('dateiwahl').addEventListener('change', laden);

  zeichnen(); filtern('alle');
})();
"""


def esc(t):
    return H.escape(t, quote=True)


def punkt(p, tag):
    kurz = re.sub(r'<[^>]+>', '', p['titel'])[:70]
    cls = 'pt ' + p['wer']
    marken = ['<span class="marke %s">%s</span>' % (p['wer'], WER_LABEL[p['wer']])]
    if p['st'] == 'teil':
        marken.append('<span class="marke teil">Hand-Out erledigt · Folie offen</span>')
    return (
        '<div class="%s" data-id="%s" data-tag="%s" data-wer="%s" data-fertig="0" data-kurz="%s">'
        '<input type="checkbox" aria-label="Punkt %s abhaken">'
        '<div><div class="pt-kopf"><span class="pid">%s</span><span class="sev">%s</span>%s'
        '<span class="fundst">%s</span></div>'
        '<p class="pt-titel">%s</p><p class="pt-det">%s</p><div class="ts"></div></div></div>'
        % (cls, esc(p['id']), tag, p['wer'], esc(kurz), esc(p['id']), esc(p['id']), p['sev'],
           ''.join(marken), esc(p['fund']), esc(p['titel']), esc(p['det']))
    )


def gruppe(wer, pl, tag):
    inner = ''.join(punkt(p, tag) for p in pl)
    if not inner:
        inner = '<p class="leer">Keine offenen Punkte.</p>'
    return ('<div class="grp %s"><div class="grp-title">%s <span class="grp-zahl"></span></div>%s</div>'
            % (wer, esc(WER_TITEL[wer]), inner))


def fertigblock(liste):
    if not liste:
        return ''
    li = ''.join('<li><span class="pid">%s</span>%s %s <span class="d">· %s</span></li>'
                 % (esc(i), s, esc(t), esc(d)) for i, s, t, d in liste)
    return ('<details class="fertig"><summary>%d erledigte Punkte anzeigen</summary>'
            '<ul class="fliste">%s</ul></details>' % (len(liste), li))


teile = ["""<!DOCTYPE html><html lang="de"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Umsetzungsstand KI-Manager:in — nach Kurstagen</title><style>%s</style></head><body>
<h1>Umsetzungsstand nach Kurstagen — KI-Manager:in</h1>
<div class="subtitle">Tage 1 bis 3 &middot; Stand %s &middot; Quelle: Entscheidungsprotokoll Reviewer und die eigenen Prüffunde</div>
<div class="bar no-print">
 <button data-filter="alle" class="an">Alle</button>
 <button data-filter="offen">Nur offene</button>
 <button data-filter="du">Nur meine (Dozent)</button>
 <button data-filter="ich">Nur Claude</button>
 <button data-filter="ent">Entscheidungen</button>
 <span class="sep"></span>
 <button data-akt="auf">Erledigtes aufklappen</button>
 <button data-akt="zu">zuklappen</button>
 <span class="sep"></span>
 <button data-akt="kopieren">Stand kopieren</button>
 <button data-akt="speichern">Stand speichern</button>
 <button data-akt="laden">Stand laden</button>
 <button data-akt="reset">Haken zurücksetzen</button>
 <button data-akt="drucken">Drucken</button>
 <input type="file" id="dateiwahl" accept="application/json,.json" style="display:none">
 <span class="fortschritt"><span class="balken"><i></i></span><span class="fz"></span></span>
 <span class="fz" id="meldung" style="color:#2a7a3a;font-weight:normal"></span>
</div>
<div class="legend">
 🟠 hoch &middot; 🟡 mittel &middot; 🟢 niedrig &middot; ⚪ zu prüfen &nbsp;·&nbsp;
 <span class="marke du">Bei Dir</span> Foliensatz und Präsentation &nbsp;·&nbsp;
 <span class="marke ich">Bei mir</span> Hand-Out, Handreichungen, Register &nbsp;·&nbsp;
 <span class="marke ent">Entscheidung</span> Du entscheidest, danach baue ich &nbsp;·&nbsp;
 <span class="marke teil">Hand-Out erledigt · Folie offen</span> die Hälfte steht schon
</div>
<div class="hinweis"><b>Diese Übersicht ist eine Ansicht, kein zweites Protokoll.</b> Maßgeblich bleibt
<code>Reviewer\\Entscheidungsprotokoll.md</code> — dort trage ich jede Entscheidung ein, und aus diesem Stand wird die Seite hier neu erzeugt.
Nichts wird doppelt geführt.<br>
<b>Erledigtes meldest Du am einfachsten im Chat</b> — ein Satz genügt („QS-01 bis QS-03 sind erledigt“), ein Bildausschnitt ist nicht nötig.
Die Haken hier sind Dein Arbeitsmittel für zwischendurch; sie bleiben im Browser gespeichert. Wenn Du magst, gibt „Stand kopieren“
den Zwischenstand als Text aus, den Du einfügen kannst. Erledigte Punkte stehen je Tag zugeklappt am Ende und zählen nicht in den Fortschritt.</div>
""" % (CSS, HEUTE)]

# ------------------------------------------------------------ Querschnitt ---
teile.append('<div class="day-block quer"><div class="day-header">'
             '<span class="day-num">Querschnitt</span>'
             '<span class="day-label">Wirkt auf mehrere Tage — einmal entscheiden genügt</span>'
             '<span class="day-count" data-count="QS">alle 3 erledigt</span></div>'
             '<div class="day-topic">Diese drei Punkte stehen in mehreren Tagen gleichlautend im Protokoll. '
             'Eine Entscheidung schließt jeweils alle.</div>')
for w in ('ent', 'du', 'ich'):
    pl = [p for p in QUER if p['wer'] == w]
    if pl:
        teile.append(gruppe(w, pl, 'QS'))
if not QUER:
    teile.append('<div class="grp"><p class="leer">Alle Querschnittspunkte sind entschieden '
                 '(18.11.2026). Sie schließen zusammen sieben Zeilen im Protokoll.</p></div>')
teile.append(fertigblock(QUER_FERTIG))
teile.append('</div>')

# ------------------------------------------------------------------ Tage ----
for t in TAGE:
    tag = 'T%d' % t['nr']
    fertig_n = len(t['fertig'])
    teile.append('<div class="day-block"><div class="day-header">'
                 '<span class="day-num">Tag %d</span><span class="day-label">%s</span>'
                 '<span class="day-count" data-count="%s"></span></div>'
                 '<div class="day-topic">%s &nbsp;·&nbsp; %d Befunde im Protokoll, davon %d erledigt</div>'
                 % (t['nr'], esc(t['titel']), tag, esc(t['datei']), t['gesamt'], fertig_n))
    for w in ('du', 'ich', 'ent'):
        pl = [p for p in t['offen'] if p['wer'] == w]
        teile.append(gruppe(w, pl, tag))
    teile.append(fertigblock(t['fertig']))
    teile.append('</div>')

# -------------------------------------------------------------- Übergabe ----
teile.append("""
<div class="uebergabe no-print">
 <h2>Stand für Claude</h2>
 <p>Nur ein Hilfsmittel: Dieser Text wird bei jedem Haken neu erzeugt. „Stand kopieren“ legt ihn in die Ablage.
 Ein Satz im Chat tut es genauso — die Entscheidung landet so oder so im Entscheidungsprotokoll, und von dort kommt sie in diese Seite zurück.</p>
 <textarea id="uebergabe" readonly></textarea>
</div>
<footer>
 Arbeitsdokument für die Kursvorbereitung &middot; nicht für Teilnehmende.
 Maßgeblich bleibt das Entscheidungsprotokoll im Ordner <code>Reviewer</code>; diese Übersicht führt daraus
 die noch offenen Punkte der Tage 1 bis 3 zusammen und nennt je Punkt den vorgeschlagenen Schritt.
 Reviewer-Befunde sind Material, kein Auftrag — jeder Punkt ist am Primärtext geprüft, bevor er umgesetzt wird.
</footer>
<script>%s</script>
</body></html>""" % JS)

s = ''.join(teile)

# ------------------------------------------------------------- Prüfungen ----
for tg in ['div', 'p', 'span', 'details', 'summary', 'ul', 'li', 'button', 'textarea', 'style', 'script', 'footer', 'h1', 'h2']:
    o = len(re.findall(r'<%s\b' % tg, s))
    c = s.count('</%s>' % tg)
    assert o == c, (tg, o, c)
off = s.index('<body')
d = 0
for m in re.finditer(r'<div\b[^>]*>|</div>', s[off:]):
    d += -1 if m.group(0) == '</div>' else 1
assert d == 0, d

klassen = set(re.findall(r'class="([^"]+)"', s))
benutzt = set()
for k in klassen:
    for x in k.split():
        benutzt.add(x)
stil = ''.join(re.findall(r'<style>(.*?)</style>', s, re.S))
definiert = set(re.findall(r'[.#]([A-Za-z][\w-]*)', stil))
fehlt = sorted(x for x in benutzt if x not in definiert)
print('Klassen ohne Regel:', fehlt if fehlt else 'keine')

ids = re.findall(r'data-id="([^"]+)"', s)
assert len(ids) == len(set(ids)), [i for i in ids if ids.count(i) > 1]
print('Punkte:', len(ids))
print('Bytes:', len(s.encode()), 'sha', hashlib.sha256(s.encode()).hexdigest()[:8])
open('Umsetzungsstand_Kurstage.html', 'w', encoding='utf-8', newline='').write(s)
