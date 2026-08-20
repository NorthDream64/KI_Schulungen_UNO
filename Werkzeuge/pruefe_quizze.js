#!/usr/bin/env node
/* ===================================================================
   Quiz-Prüfung — KI-Schulungen
   -------------------------------------------------------------------
   Prüft alle Quiz- und Übersichtsdateien beider Kurse auf
     1. Syntaxfehler (z. B. gerade Anführungszeichen im Fragetext)
     2. Strukturregeln (4 Optionen, 1–3 richtige Antworten, Quelle)
     3. Verweise in index.html auf nicht vorhandene Dateien

   Aufruf:  node Werkzeuge/pruefe_quizze.js
   Rückgabe: 0 = alles in Ordnung · 1 = Fehler gefunden
   =================================================================== */
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const WURZEL = path.resolve(__dirname, '..');
const KURSE = ['KI-Manager', 'KI-Beauftragte'];

let fehler = 0, warnungen = 0, geprueft = 0;
const rot = s => '\x1b[31m' + s + '\x1b[0m';
const gelb = s => '\x1b[33m' + s + '\x1b[0m';
const gruen = s => '\x1b[32m' + s + '\x1b[0m';

function skripte(html) {
  return [...html.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)].map(m => m[1]).join('\n');
}

function meldeFehler(datei, text, detail) {
  fehler++;
  console.log(rot('  FEHLER  ') + datei);
  console.log('          ' + text);
  if (detail) console.log('          ' + detail);
}
function meldeWarnung(datei, text) {
  warnungen++;
  console.log(gelb('  Hinweis ') + datei + ' — ' + text);
}

/* --- 1. Syntaxprüfung ------------------------------------------- */
function pruefeSyntax(datei, js) {
  try {
    new vm.Script(js, { filename: datei });
    return true;
  } catch (e) {
    let zeile = '';
    const m = /:(\d+)\s*$/.exec((e.stack || '').split('\n')[0] || '');
    const nr = m ? parseInt(m[1]) : null;
    if (nr) zeile = 'Zeile ' + nr + ' im Skriptteil: ' + (js.split('\n')[nr - 1] || '').trim().slice(0, 120);
    meldeFehler(datei, 'Datei lässt sich nicht ausführen — ' + e.message, zeile);
    console.log('          Häufigste Ursache: gerades Anführungszeichen (") im Fragetext.');
    console.log('          Abhilfe: typografische Anführungszeichen verwenden — „ und “');
    return false;
  }
}

/* --- 2. Fragen einlesen ----------------------------------------- */
function fragen(js) {
  let s = -1;
  for (const v of ['var QBANK', 'var QUESTIONS']) {
    const k = js.indexOf(v);
    if (k >= 0) { s = k; break; }
  }
  if (s < 0) return null;
  const a = js.indexOf('[', s), b = js.indexOf('{', s);
  const auf = (a >= 0 && (a < b || b < 0)) ? '[' : '{';
  const start = auf === '[' ? a : b, zu = auf === '[' ? ']' : '}';
  let d = 0, i = start;
  for (; i < js.length; i++) {
    if (js[i] === auf) d++;
    else if (js[i] === zu) { d--; if (d === 0) { i++; break; } }
  }
  try {
    const wert = vm.runInNewContext('(' + js.slice(start, i) + ')');
    return Array.isArray(wert) ? wert : Object.values(wert).flat();
  } catch (e) { return null; }
}

/* --- 3. Strukturregeln ------------------------------------------ */
function pruefeStruktur(datei, qs) {
  qs.forEach((q, i) => {
    const nr = q.nr || (i + 1);
    if (!q.opts || q.opts.length !== 4)
      meldeFehler(datei, 'Frage ' + nr + ': ' + ((q.opts || []).length) + ' Optionen statt 4');
    if (!q.correct || q.correct.length < 1 || q.correct.length > 3)
      meldeFehler(datei, 'Frage ' + nr + ': ' + ((q.correct || []).length) + ' richtige Antworten — erlaubt sind 1 bis 3, nie 4');
    if (q.correct && q.opts && q.correct.some(k => k < 0 || k >= q.opts.length))
      meldeFehler(datei, 'Frage ' + nr + ': verweist auf eine Option, die es nicht gibt');
    if (q.exp && /\bOption\s*\[?[A-D]\b|\bAntwort\s*[A-D]\b/.test(q.exp))
      meldeWarnung(datei, 'Frage ' + nr + ': Erklärung nennt einen Optionsbuchstaben — die Reihenfolge wird gemischt');
    if (!q.src) meldeWarnung(datei, 'Frage ' + nr + ': keine Quelle angegeben');
  });
}

/* --- 4. Durchlauf ----------------------------------------------- */
console.log('\nQuiz-Prüfung — ' + new Date().toLocaleString('de-DE') + '\n');

for (const kurs of KURSE) {
  const quizOrdner = path.join(WURZEL, kurs, 'Quiz');
  if (!fs.existsSync(quizOrdner)) continue;
  console.log('· ' + kurs);

  for (const name of fs.readdirSync(quizOrdner).filter(f => f.endsWith('.html'))) {
    const p = path.join(quizOrdner, name);
    const js = skripte(fs.readFileSync(p, 'utf-8'));
    geprueft++;
    if (!pruefeSyntax(kurs + '/Quiz/' + name, js)) continue;
    const qs = fragen(js);
    if (qs === null) { meldeWarnung(kurs + '/Quiz/' + name, 'keine Fragen gefunden'); continue; }
    pruefeStruktur(kurs + '/Quiz/' + name, qs);
  }

  // Übersichtsseite und ihre Verweise
  const idx = path.join(WURZEL, kurs, 'index.html');
  if (fs.existsSync(idx)) {
    const roh = fs.readFileSync(idx, 'utf-8');
    geprueft++;
    pruefeSyntax(kurs + '/index.html', skripte(roh));
    const block = /var QUIZ_FILES\s*=\s*\{([\s\S]*?)\}/.exec(roh);
    if (block) {
      for (const m of block[1].matchAll(/(\d+)\s*:\s*'([^']+)'/g)) {
        const ziel = path.join(WURZEL, kurs, decodeURIComponent(m[2]));
        if (!fs.existsSync(ziel))
          meldeFehler(kurs + '/index.html', 'Tag ' + m[1] + ' verweist auf eine Datei, die es nicht gibt: ' + m[2]);
      }
    }
  }
}

/* --- 5. Ergebnis ------------------------------------------------ */
console.log('\n' + '─'.repeat(58));
console.log(geprueft + ' Dateien geprüft · ' + fehler + ' Fehler · ' + warnungen + ' Hinweise');
if (fehler === 0) {
  console.log(gruen('Alles in Ordnung — die Dateien können übertragen werden.\n'));
  process.exit(0);
} else {
  console.log(rot('Bitte die Fehler beheben, bevor du überträgst.\n'));
  process.exit(1);
}
