// KI-Manager Gamification — Paket-Modell (Pilot: Paket 1)
// U. Nord 2026

const APPS_SCRIPT_URL = "";
const SHARED_TOKEN    = "kim-2026-alpha";
const FETCH_TIMEOUT_MS = 4000;

const FRAGEN_DATEI = "data/fragen.json";
const PAKET_GROESSE = 10;   // Zielgröße; falls Pool kleiner, werden alle Fragen genommen
const PAKET_NR = 1;         // Piloten-Paket

// Punkte-Skala je nach Frage-Schwierigkeit (intern, nicht prominent angezeigt)
const PUNKTE = {
  1: { voll: 20, teilweise: 10 },
  2: { voll: 40, teilweise: 20 },
  3: { voll: 60, teilweise: 30 }
};

const state = {
  spieler: "anonym",
  session_id: crypto.randomUUID ? crypto.randomUUID() : "s_" + Date.now(),
  fragen: [],
  frageIndex: 0,
  ausgewaehlt: new Set(),
  attempts: 0,
  gesperrt: false,
  bilanz: {
    total: 0, richtigBeimErstenVersuch: 0, richtigInsgesamt: 0,
    teilweise: 0, falsch: 0, uebersprungen: 0,
    punkte: 0
  },
  karten: []
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

  await ladePaket();
}

async function ladePaket() {
  try {
    const resp = await fetch(FRAGEN_DATEI + "?v=" + Date.now());
    const data = await resp.json();
    const pool = data.fragen || [];
    const gezogen = shuffle([...pool]).slice(0, PAKET_GROESSE);
    state.fragen = gezogen;
    state.frageIndex = 0;

    $("level-tag").textContent = "Paket " + PAKET_NR;
    $("level-tag").className = "strip-tag strip-paket";
    $("level-name").textContent = gezogen.length + " Fragen";

    zeigeFrage();
  } catch (e) {
    console.error("Paket-Ladefehler:", e);
    $("q-text").textContent = "Fehler beim Laden der Fragen. Bitte Seite neu laden.";
  }
}

function zeigeFrage() {
  const frage = state.fragen[state.frageIndex];

  state.ausgewaehlt = new Set();
  state.attempts = 0;
  state.gesperrt = false;

  $("progress-label").textContent =
    "Frage " + (state.frageIndex + 1) + " von " + state.fragen.length;
  const pct = (state.frageIndex / state.fragen.length) * 100;
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

function schwierigkeitVon(frage) {
  return frage.schwierigkeit || 1;
}

function begriffFuer(frage) {
  return (frage.glossar && frage.glossar.begriff) || frage.id;
}

function checkAnswer() {
  const frage = state.fragen[state.frageIndex];
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
  const istTeilweise = anzahlKorrektGewaehlt > 0 && anzahlFalschGewaehlt === 0;

  const s = schwierigkeitVon(frage);
  const begriff = begriffFuer(frage);

  if (allesRichtig) {
    state.bilanz.total++;
    state.bilanz.richtigInsgesamt++;
    state.bilanz.punkte += (PUNKTE[s] || PUNKTE[1]).voll;
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
    state.bilanz.punkte += (PUNKTE[s] || PUNKTE[1]).teilweise;
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
  const isLast = state.frageIndex === state.fragen.length - 1;
  if (richtig) {
    $("btn-next").textContent = isLast ? "Paket abschließen →" : "OK, nächstes Thema →";
    $("btn-next").classList.add("btn-next-thema");
  } else {
    $("btn-next").textContent = isLast ? "Paket abschließen →" : "Weiter →";
  }
  $("btn-next").classList.remove("hidden");
}

function skipToExplanation() {
  const frage = state.fragen[state.frageIndex];
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
  if (state.frageIndex >= state.fragen.length) {
    zeigeErgebnis();
  } else {
    zeigeFrage();
  }
}

// ── FEUERWERK ─────────────────────────────────────────────────────────────
function feuerwerk(gross) {
  if (typeof confetti !== "function") return;   // Library nicht geladen — Fallback still

  const farben = ["#5a3a7a", "#2a7a50", "#7a4a00", "#0a4a7a", "#f0eaf7", "#eaf5ee"];

  // Zentraler Regen
  confetti({
    particleCount: gross ? 180 : 100,
    spread: 80,
    origin: { y: 0.55 },
    colors: farben
  });

  // Von den Seiten
  setTimeout(() => confetti({
    particleCount: gross ? 90 : 55,
    angle: 60, spread: 55, origin: { x: 0, y: 0.7 }, colors: farben
  }), 250);
  setTimeout(() => confetti({
    particleCount: gross ? 90 : 55,
    angle: 120, spread: 55, origin: { x: 1, y: 0.7 }, colors: farben
  }), 400);

  // Bonus-Salve nur beim großen Feuerwerk
  if (gross) {
    setTimeout(() => confetti({
      particleCount: 120,
      spread: 100, origin: { y: 0.3 }, colors: farben
    }), 900);
  }
}

function zeigeErgebnis() {
  hide("game-view");
  show("result-view");
  const b = state.bilanz;

  // Bonus-Feuerwerk, wenn alle Fragen im 1. Versuch richtig
  const alleErsterVersuch = b.total > 0 && b.richtigBeimErstenVersuch === b.total;
  feuerwerk(alleErsterVersuch);

  const chips = state.karten.map(k => {
    const cls = "karte karte-" + k.status;
    const label = statusLabel(k.status);
    return '<span class="' + cls + '" title="' + label + '">' + escapeHtml(k.begriff) + '</span>';
  }).join(" ");

  const anz = {
    meister:       state.karten.filter(k => k.status === "meister").length,
    verstanden:    state.karten.filter(k => k.status === "verstanden").length,
    teilweise:     state.karten.filter(k => k.status === "teilweise").length,
    kennengelernt: state.karten.filter(k => k.status === "kennengelernt").length,
    uebersprungen: state.karten.filter(k => k.status === "uebersprungen").length
  };

  const gruss = alleErsterVersuch
    ? "Paket " + PAKET_NR + " glatt durchgezogen — alle Fragen im ersten Anlauf!"
    : "Paket " + PAKET_NR + " geschafft.";

  $("result-grade").textContent = gruss;
  $("result-label").textContent =
    "Du hast " + state.karten.length + " Fachbegriff" +
    (state.karten.length === 1 ? "" : "e") + " kennengelernt.";
  $("result-sub").textContent = ergebnisSatz(anz);

  $("stats-row").innerHTML =
    '<div class="karten-collection">' + chips + '</div>' +
    '<div class="karten-legende">' +
      legendeEintrag("meister",       "sofort verstanden") +
      legendeEintrag("verstanden",    "im zweiten Versuch") +
      legendeEintrag("teilweise",     "teilweise erfasst") +
      legendeEintrag("kennengelernt", "durch Erklärung") +
      legendeEintrag("uebersprungen", "direkt zur Erklärung") +
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
  if (a.meister)       teile.push(a.meister + " davon hattest Du im ersten Anlauf parat");
  if (a.verstanden)    teile.push(a.verstanden + " hast Du im zweiten Anlauf geknackt");
  if (a.teilweise)     teile.push(a.teilweise + " " + (a.teilweise === 1 ? "war teilweise richtig" : "waren teilweise richtig"));
  if (a.kennengelernt) teile.push(a.kennengelernt + " hast Du über die Erklärung kennengelernt");
  if (a.uebersprungen) teile.push(a.uebersprungen + " hast Du Dir direkt erklären lassen");
  if (!teile.length) return "Danke fürs Mitspielen.";
  return teile.join("; ") + ". Fachbegriffe fühlen sich mit jedem Durchgang vertrauter an.";
}

function logAntwort(frage, richtig) {
  if (!APPS_SCRIPT_URL) return;

  const payload = {
    token: SHARED_TOKEN,
    session: state.session_id,
    spieler: state.spieler,
    paket: PAKET_NR,
    schwierigkeit: schwierigkeitVon(frage),
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
