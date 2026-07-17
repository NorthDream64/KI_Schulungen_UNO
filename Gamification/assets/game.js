// KI-Manager Gamification — Prototyp
// U. Nord 2026

// ── KONFIGURATION ──────────────────────────────────────────────────────────
const APPS_SCRIPT_URL = "";
const SHARED_TOKEN    = "kim-2026-alpha";
const FETCH_TIMEOUT_MS = 4000;

const LEVELS = [
  { nr: 1, datei: "data/level1.json" },
  { nr: 2, datei: "data/level2.json" },
  { nr: 3, datei: "data/level3.json" }
];

// ── STATE ──────────────────────────────────────────────────────────────────
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
  bilanz: { total: 0, richtigBeimErstenVersuch: 0, richtigInsgesamt: 0, falsch: 0 }
};

// ── DOM-HELFER ─────────────────────────────────────────────────────────────
const $ = (id) => document.getElementById(id);
const show = (id) => $(id).classList.remove("hidden");
const hide = (id) => $(id).classList.add("hidden");

// ── INIT ───────────────────────────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  $("btn-start").addEventListener("click", startGame);
  $("btn-check").addEventListener("click", checkAnswer);
  $("btn-next").addEventListener("click", nextQuestion);
  $("btn-restart").addEventListener("click", () => location.reload());

  const gemerkt = localStorage.getItem("kim_game_vorname");
  if (gemerkt) $("vorname").value = gemerkt;
});

// ── SPIELSTART ─────────────────────────────────────────────────────────────
async function startGame() {
  const eingabe = $("vorname").value.trim();
  state.spieler = eingabe || "anonym";
  if (eingabe) localStorage.setItem("kim_game_vorname", eingabe);

  $("player-tag").textContent = "— " + state.spieler;

  hide("start-view");
  show("game-view");

  await ladeLevel(0);
}

// ── LEVEL LADEN ────────────────────────────────────────────────────────────
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

// ── FRAGE ANZEIGEN ─────────────────────────────────────────────────────────
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

// ── ANTWORT PRÜFEN ─────────────────────────────────────────────────────────
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

  if (allesRichtig) {
    state.bilanz.total++;
    state.bilanz.richtigInsgesamt++;
    if (state.attempts === 1) state.bilanz.richtigBeimErstenVersuch++;

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
  state.bilanz.falsch++;
  markiereOptionen(korrekt, gewaehlt, true);
  zeigeFeedback("wrong", "Nicht ganz.", frage.feedback_falsch, frage.glossar);
  logAntwort(frage, false);
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

// ── DIDAKTISCHE SEITE ─────────────────────────────────────────────────────
function zeigeDidaktik(vert) {
  const quellenHtml = (vert.quellen || []).map(q =>
    '<div class="didaktik-source">' +
    '<div class="didaktik-source-titel">' + escapeHtml(q.titel) + '</div>' +
    '<div class="didaktik-source-meta">' + escapeHtml(q.institution) + ' · ' + escapeHtml(q.art) + '</div>' +
    '<a href="' + escapeHtml(q.url) + '" target="_blank" rel="noopener noreferrer">' + escapeHtml(q.url) + '</a>' +
    '</div>'
  ).join("");

  const absaetze = (vert.laien_erklaerung || "").split(/\n\n+/)
    .map(p => '<p>' + escapeHtml(p).replace(/\n/g, "<br>") + '</p>').join("");

  const html =
    '<div class="didaktik-panel">' +
      '<div class="didaktik-head">Didaktische Pause · ' + escapeHtml(vert.begriff) + '</div>' +
      '<button class="didaktik-toggle" id="didaktik-toggle" aria-expanded="false">' +
        '<span>Erkläre mir die Fachbegriffe</span>' +
        '<span class="caret">›</span>' +
      '</button>' +
      '<div class="didaktik-body hidden" id="didaktik-body">' +
        absaetze +
        '<div class="didaktik-sources">' +
          '<div class="didaktik-sources-title">Zum Weiterlesen — akademische Quellen</div>' +
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

// ── FEEDBACK-BOX ───────────────────────────────────────────────────────────
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

// ── WEITER ─────────────────────────────────────────────────────────────────
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

// ── ERGEBNIS ───────────────────────────────────────────────────────────────
function zeigeErgebnis() {
  hide("game-view");
  show("result-view");
  const b = state.bilanz;
  const quote = b.total ? Math.round((b.richtigInsgesamt / b.total) * 100) : 0;
  const grade = quote >= 80 ? "Sehr gut" : quote >= 60 ? "Gut" : "Weiter dranbleiben";
  $("result-grade").textContent = grade;
  $("result-label").textContent = "Du hast " + quote + " % geschafft.";
  $("result-sub").textContent = "Danke fürs Mitspielen — Fachbegriffe fühlen sich mit jedem Durchgang vertrauter an.";
  $("stats-row").innerHTML =
    '<div class="stat"><div class="stat-n">' + b.total + '</div><div class="stat-l">Fragen</div></div>' +
    '<div class="stat"><div class="stat-n">' + b.richtigBeimErstenVersuch + '</div><div class="stat-l">1. Versuch richtig</div></div>' +
    '<div class="stat"><div class="stat-n">' + b.richtigInsgesamt + '</div><div class="stat-l">insgesamt richtig</div></div>';
}

// ── LOGGING AN GOOGLE SHEET ────────────────────────────────────────────────
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

// ── UTILS ──────────────────────────────────────────────────────────────────
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
