// KI-Manager Gamification — Prototyp
// U. Nord 2026

const APPS_SCRIPT_URL = "";
const SHARED_TOKEN    = "kim-2026-alpha";
const FETCH_TIMEOUT_MS = 4000;

const LEVELS = [
  { nr: 1, datei: "data/level1.json" },
  { nr: 2, datei: "data/level2.json" },
  { nr: 3, datei: "data/level3.json" }
];

// Punkte-Skala (intern, wird im Log gespeichert; nicht prominent angezeigt)
const PUNKTE = {
  1: { voll: 20, teilweise: 10 },
  2: { voll: 40, teilweise: 20 },
  3: { voll: 60, teilweise: 30 }
};

const state = {
  spieler: "anonym",
  session_id: crypto.randomUUID ? crypto.randomUUID() : "s_" + Date.now(),
  levelIndex: 0,
  fragenAktuellesLevel: [],
  frageIndex: 0,
  daten: {},
  ausgewaehlt: new Set(),
  attempts: 0,
  gesperrt: false,
  bilanz: {
    total: 0, richtigBeimErstenVersuch: 0, richtigInsgesamt: 0,
    teilweise: 0, falsch: 0, uebersprungen: 0,
    punkte: 0
  },
  karten: []   // { begriff, status: 'meister'|'verstanden'|'teilweise'|'kennengelernt'|'übersprungen' }
};

const $ = (id) => document.getElementById(id);
const show = (id) => $(id).classList.remove("hidden");
const hide = (id) => $(id).classList.add("hidden");

document.addEventListener("DOMContentLoaded", () => {
  $("btn-start").addEventListener("click", startGame);
  $("btn-check").addEventListener("click", checkAnswer);
  $("btn-skip").addEventListener("click", skipToExplanation);
  $("btn-next").addEventListener("click", nextQuestion);
  $("btn-restart").addEventListener("click", () => location.reload());

  const gemerkt = localStorage.getItem("kim_game_vorname");
  if (gemerkt) $("vorname").value = gemerkt;
});

async function startGame() {
  const eingabe = $("vorname").value.trim();
  state.spieler = eingabe || "anonym";
  if (eingabe) localStorage.setItem("kim_game_vorname", eingabe);

  $("player-tag").textContent = "— " + state.spieler;

  hide("start-view");
  show("game-view");

  await ladeLevel(0);
}

async function ladeLevel(idx) {
  state.levelIndex = idx;
  state.frageIndex = 0;

  try {
    const resp = await fetch(LEVELS[idx].datei + "?v=" + Date.now());
    const data = await resp.json();
    state.daten[idx] = data;
    state.fragenAktuellesLevel = data.fragen;

    const tag = $("level-tag");
    tag.textContent = "Level " + data.level;
    tag.className = "strip-tag strip-level lvl-" + data.level;
    $("level-name").textContent = data.titel;

    zeigeFrage();
  } catch (e) {
    console.error("Level-Ladefehler:", e);
    $("q-text").textContent = "Fehler beim Laden des Levels. Bitte Seite neu laden.";
  }
}

function zeigeFrage() {
  const frage = state.fragenAktuellesLevel[state.frageIndex];

  state.ausgewaehlt = new Set();
  state.attempts = 0;
  state.gesperrt = false;

  $("progress-label").textContent =
    "Frage " + (state.frageIndex + 1) + " von " + state.fragenAktuellesLevel.length;
  const pct = ((state.frageIndex) / state.fragenAktuellesLevel.length) * 100;
  $("progress-fill").style.width = pct + "%";

  $("scenario-label").textContent = frage.kanal + " · " + frage.absender;
  $("scenario-text").textContent = frage.szenario;
  $("q-text").textContent = frage.frage;

  const list = $("opt-list");
  list.innerHTML = "";
  const opts = shuffle([...frage.optionen]);
  opts.forEach((opt) => {
    const row = document.createElement("div");
    row.className = "opt";
    row.dataset.id = opt.id;
    row.innerHTML = '<span class="opt-cb"></span><span class="opt-text">' + escapeHtml(opt.text) + '</span>';
    row.addEventListener("click", () => toggleOption(row, opt.id));
    list.appendChild(row);
  });

  $("feedback-slot").innerHTML = "";
  $("didaktik-slot").innerHTML = "";
  $("btn-check").classList.remove("hidden");
  $("btn-check").disabled = false;
  $("btn-next").classList.add("hidden");
  $("btn-next").textContent = "Weiter →";
  $("btn-next").classList.remove("btn-next-thema");

  if (frage.vertiefung) {
    $("btn-skip").classList.remove("hidden");
  } else {
    $("btn-skip").classList.add("hidden");
  }
}

function toggleOption(row, id) {
  if (state.gesperrt) return;
  if (state.ausgewaehlt.has(id)) {
    state.ausgewaehlt.delete(id);
    row.classList.remove("selected");
    row.querySelector(".opt-cb").classList.remove("chk");
  } else {
    state.ausgewaehlt.add(id);
    row.classList.add("selected");
    row.querySelector(".opt-cb").classList.add("chk");
  }
}

function levelNr() {
  return (state.daten[state.levelIndex] && state.daten[state.levelIndex].level) || (state.levelIndex + 1);
}

function begriffFuer(frage) {
  return (frage.glossar && frage.glossar.begriff) || frage.id;
}

function checkAnswer() {
  const frage = state.fragenAktuellesLevel[state.frageIndex];
  if (state.ausgewaehlt.size === 0) {
    zeigeFeedback("hint", "Bitte wähle mindestens eine Option.", "");
    return;
  }

  state.attempts++;
  const korrekt = new Set(frage.korrekt);
  const gewaehlt = state.ausgewaehlt;

  const allesRichtig = gewaehlt.size === korrekt.size &&
                       [...gewaehlt].every(id => korrekt.has(id));

  const anzahlKorrektGewaehlt = [...gewaehlt].filter(id => korrekt.has(id)).length;
  const anzahlFalschGewaehlt  = [...gewaehlt].filter(id => !korrekt.has(id)).length;
  // "teilweise" = mindestens eine richtige, aber keine falsche markiert
  const istTeilweise = anzahlKorrektGewaehlt > 0 && anzahlFalschGewaehlt === 0;

  const lvl = levelNr();
  const begriff = begriffFuer(frage);

  if (allesRichtig) {
    state.bilanz.total++;
    state.bilanz.richtigInsgesamt++;
    state.bilanz.punkte += (PUNKTE[lvl] || PUNKTE[1]).voll;
    if (state.attempts === 1) state.bilanz.richtigBeimErstenVersuch++;
    state.karten.push({ begriff, status: state.attempts === 1 ? "meister" : "verstanden" });

    markiereOptionen(korrekt, gewaehlt, true);
    zeigeFeedback("ok", "Richtig.", frage.feedback_richtig, frage.glossar);
    if (frage.vertiefung) zeigeDidaktik(frage.vertiefung);
    logAntwort(frage, true);
    schliesseFrageAb(true);
    return;
  }

  if (state.attempts === 1) {
    zeigeFeedback("hint",
      "Meinst Du wirklich, das passt hier?",
      "Lies das Szenario nochmal in Ruhe. Was ist das eigentliche Symptom — und welche Reaktion adressiert genau *das*?");
    return;
  }

  state.bilanz.total++;
  if (istTeilweise) {
    state.bilanz.teilweise++;
    state.bilanz.punkte += (PUNKTE[lvl] || PUNKTE[1]).teilweise;
    state.karten.push({ begriff, status: "teilweise" });
  } else {
    state.bilanz.falsch++;
    state.karten.push({ begriff, status: "kennengelernt" });
  }
  markiereOptionen(korrekt, gewaehlt, true);
  zeigeFeedback("wrong", "Nicht ganz.", frage.feedback_falsch, frage.glossar);
  if (frage.vertiefung) zeigeDidaktik(frage.vertiefung);
  logAntwort(frage, istTeilweise ? "teilweise" : false);
  schliesseFrageAb(false);
}

function markiereOptionen(korrekt, gewaehlt, final) {
  document.querySelectorAll(".opt").forEach(row => {
    const id = row.dataset.id;
    row.classList.remove("selected");
    if (final) {
      row.classList.add("disabled");
      if (korrekt.has(id) && gewaehlt.has(id)) row.classList.add("correct-sel");
      else if (!korrekt.has(id) && gewaehlt.has(id)) row.classList.add("wrong-sel");
      else if (korrekt.has(id) && !gewaehlt.has(id)) row.classList.add("missed");
    }
  });
}

function schliesseFrageAb(richtig) {
  state.gesperrt = true;
  $("btn-check").classList.add("hidden");
  $("btn-skip").classList.add("hidden");
  const isLast = state.frageIndex === state.fragenAktuellesLevel.length - 1 &&
                 state.levelIndex === LEVELS.length - 1;
  if (richtig) {
    $("btn-next").textContent = isLast ? "Ergebnis anzeigen →" : "OK, nächstes Thema →";
    $("btn-next").classList.add("btn-next-thema");
  } else {
    $("btn-next").textContent = isLast ? "Ergebnis anzeigen →" : "Weiter →";
  }
  $("btn-next").classList.remove("hidden");
}

function skipToExplanation() {
  const frage = state.fragenAktuellesLevel[state.frageIndex];
  if (!frage.vertiefung) return;

  state.bilanz.total++;
  state.bilanz.uebersprungen++;
  state.karten.push({ begriff: begriffFuer(frage), status: "uebersprungen" });

  state.gesperrt = true;
  document.querySelectorAll(".opt").forEach(row => row.classList.add("disabled"));

  zeigeFeedback("hint",
    "Alles klar — hier ist die Erklärung.",
    "Du hast diese Frage übersprungen, um direkt zur Vertiefung zu kommen. Kein Malus — das ist Teil des Spiels.");

  zeigeDidaktik(frage.vertiefung, true);

  logAntwort(frage, null);
  schliesseFrageAb(false);
}

function zeigeDidaktik(vert, aufgeklappt) {
  const quellenHtml = (vert.quellen || []).map(q =>
    '<div class="didaktik-source">' +
    '<div class="didaktik-source-titel">' + escapeHtml(q.titel) + '</div>' +
    '<div class="didaktik-source-meta">' + escapeHtml(q.institution) + ' · ' + escapeHtml(q.art) + '</div>' +
    '<a href="' + escapeHtml(q.url) + '" target="_blank" rel="noopener noreferrer">' + escapeHtml(q.url) + '</a>' +
    '</div>'
  ).join("");

  const absaetze = (vert.laien_erklaerung || "").split(/\n\n+/)
    .map(p => '<p>' + escapeHtml(p).replace(/\n/g, "<br>") + '</p>').join("");

  const bodyCls   = aufgeklappt ? "" : " hidden";
  const toggleCls = aufgeklappt ? " open" : "";
  const ariaOpen  = aufgeklappt ? "true" : "false";

  const html =
    '<div class="didaktik-panel">' +
      '<div class="didaktik-head">Didaktische Pause · ' + escapeHtml(vert.begriff) + '</div>' +
      '<button class="didaktik-toggle' + toggleCls + '" id="didaktik-toggle" aria-expanded="' + ariaOpen + '">' +
        '<span>Erkläre mir die Fachbegriffe</span>' +
        '<span class="caret">›</span>' +
      '</button>' +
      '<div class="didaktik-body' + bodyCls + '" id="didaktik-body">' +
        absaetze +
        '<div class="didaktik-sources">' +
          '<div class="didaktik-sources-title">Zum Weiterlesen — öffentliche Quellen</div>' +
          quellenHtml +
        '</div>' +
      '</div>' +
    '</div>';
  $("didaktik-slot").innerHTML = html;

  document.getElementById("didaktik-toggle").addEventListener("click", (ev) => {
    const btn = ev.currentTarget;
    const body = document.getElementById("didaktik-body");
    const isOpen = !body.classList.contains("hidden");
    if (isOpen) {
      body.classList.add("hidden");
      btn.classList.remove("open");
      btn.setAttribute("aria-expanded", "false");
    } else {
      body.classList.remove("hidden");
      btn.classList.add("open");
      btn.setAttribute("aria-expanded", "true");
    }
  });
}

function zeigeFeedback(type, titel, text, glossar) {
  const cls = type === "ok" ? "fb-ok" : type === "wrong" ? "fb-wrong" : "fb-hint";
  let html = '<div class="feedback ' + cls + '">' +
    '<div class="fb-title">' + escapeHtml(titel) + '</div>' +
    '<div class="fb-text">' + escapeHtml(text) + '</div>';
  if (glossar) {
    html += '<div class="fb-glossar"><strong>' + escapeHtml(glossar.begriff) + ':</strong> ' + escapeHtml(glossar.erklaerung) + '</div>';
  }
  html += '</div>';
  $("feedback-slot").innerHTML = html;
}

function nextQuestion() {
  state.frageIndex++;
  if (state.frageIndex >= state.fragenAktuellesLevel.length) {
    if (state.levelIndex + 1 < LEVELS.length) {
      ladeLevel(state.levelIndex + 1);
    } else {
      zeigeErgebnis();
    }
  } else {
    zeigeFrage();
  }
}

function zeigeErgebnis() {
  hide("game-view");
  show("result-view");
  const b = state.bilanz;

  // Karten-Chips rendern
  const chips = state.karten.map(k => {
    const cls = "karte karte-" + k.status;
    const label = statusLabel(k.status);
    return '<span class="' + cls + '" title="' + label + '">' + escapeHtml(k.begriff) + '</span>';
  }).join(" ");

  // Warmherziger, personalisierter Text
  const anz = {
    meister:       state.karten.filter(k => k.status === "meister").length,
    verstanden:    state.karten.filter(k => k.status === "verstanden").length,
    teilweise:     state.karten.filter(k => k.status === "teilweise").length,
    kennengelernt: state.karten.filter(k => k.status === "kennengelernt").length,
    uebersprungen: state.karten.filter(k => k.status === "uebersprungen").length
  };

  $("result-grade").textContent = "Deine Sammlung";
  $("result-label").textContent =
    "Du hast heute " + state.karten.length + " Fachbegriff" +
    (state.karten.length === 1 ? "" : "e") + " kennengelernt.";
  $("result-sub").textContent = ergebnisSatz(anz);

  $("stats-row").innerHTML =
    '<div class="karten-collection">' + chips + '</div>' +
    '<div class="karten-legende">' +
      legendeEintrag("meister",       "sofort verstanden") +
      legendeEintrag("verstanden",    "im zweiten Versuch") +
      legendeEintrag("teilweise",     "teilweise erfasst") +
      legendeEintrag("kennengelernt", "durch Erklärung") +
      legendeEintrag("uebersprungen",  "direkt zur Erklärung") +
    '</div>';
}

function statusLabel(s) {
  return {
    "meister": "sofort verstanden",
    "verstanden": "im zweiten Versuch verstanden",
    "teilweise": "teilweise richtig",
    "kennengelernt": "durch die Erklärung kennengelernt",
    "uebersprungen": "direkt zur Erklärung gesprungen"
  }[s] || s;
}

function legendeEintrag(status, text) {
  return '<span class="legende-item"><span class="karte karte-' + status + ' karte-mini"></span>' + escapeHtml(text) + '</span>';
}

function ergebnisSatz(a) {
  const teile = [];
  if (a.meister)       teile.push(a.meister + " davon " + (a.meister === 1 ? "hattest Du" : "hattest Du") + " im ersten Anlauf parat");
  if (a.verstanden)    teile.push(a.verstanden + " " + (a.verstanden === 1 ? "hast Du im zweiten Anlauf geknackt" : "hast Du im zweiten Anlauf geknackt"));
  if (a.teilweise)     teile.push(a.teilweise + " " + (a.teilweise === 1 ? "war teilweise richtig" : "waren teilweise richtig"));
  if (a.kennengelernt) teile.push(a.kennengelernt + " " + (a.kennengelernt === 1 ? "hast Du über die Erklärung kennengelernt" : "hast Du über die Erklärung kennengelernt"));
  if (a.uebersprungen) teile.push(a.uebersprungen + " " + (a.uebersprungen === 1 ? "hast Du Dir direkt erklären lassen" : "hast Du Dir direkt erklären lassen"));
  if (!teile.length) return "Danke fürs Mitspielen.";
  return teile.join("; ") + ". Fachbegriffe fühlen sich mit jedem Durchgang vertrauter an.";
}

function logAntwort(frage, richtig) {
  if (!APPS_SCRIPT_URL) return;

  const payload = {
    token: SHARED_TOKEN,
    session: state.session_id,
    spieler: state.spieler,
    level: state.daten[state.levelIndex].level,
    frage_id: frage.id,
    gewaehlt: [...state.ausgewaehlt].join(","),
    korrekt: frage.korrekt.join(","),
    richtig: richtig,
    versuche: state.attempts,
    punkte_gesamt: state.bilanz.punkte,
    zeit: new Date().toISOString()
  };

  const ctrl = new AbortController();
  const t = setTimeout(() => ctrl.abort(), FETCH_TIMEOUT_MS);
  fetch(APPS_SCRIPT_URL, {
    method: "POST",
    mode: "no-cors",
    headers: { "Content-Type": "text/plain;charset=utf-8" },
    body: JSON.stringify(payload),
    signal: ctrl.signal
  }).catch(err => {
    console.warn("Log-Fehler (ignoriert):", err);
  }).finally(() => clearTimeout(t));
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[c]));
}

function shuffle(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}
