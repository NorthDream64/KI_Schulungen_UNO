// KI-Manager Gamification — Paket-Modell
// U. Nord 2026

const APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzQSUgTDZ1VYk7mTLnb9hWaO1yXoDvWJT1-5mQ3-hC4kZbgz3l20rLeG6lhgn1T8EtFjw/exec";
const SHARED_TOKEN    = "kim-2026-alpha";
const FETCH_TIMEOUT_MS = 4000;

const FRAGEN_DATEI = "data/fragen.json";
const PAKETE_DATEI = "data/pakete.json";
const PAKET_GROESSE = 5;

const PUNKTE = {
  1: { voll: 20, teilweise: 10 },
  2: { voll: 40, teilweise: 20 },
  3: { voll: 60, teilweise: 30 }
};

const state = {
  spieler: "anonym",
  session_id: crypto.randomUUID ? crypto.randomUUID() : "s_" + Date.now(),
  pakete: [],           // Metadaten aller Pakete (aus pakete.json)
  paketNr: 1,           // aktuell gespieltes Paket
  fragen: [],           // Fragen des aktuellen Pakets
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

  // Konditionaler Datenschutz-Hinweis
  const dsBox = $("datenschutz-text");
  if (dsBox && !APPS_SCRIPT_URL) {
    dsBox.innerHTML =
      "Diese Version wird ohne Verbindung zu einem Backend betrieben. " +
      "Alle Antworten bleiben ausschließlich in Deinem Browser — nichts wird gespeichert oder übertragen. " +
      "Die Vornamen-Eingabe ist rein für die Anrede im Spiel; sie verlässt Deinen Rechner nicht.";
  }
});

async function startGame() {
  const eingabe = $("vorname").value.trim();
  state.spieler = eingabe || "anonym";
  if (eingabe) localStorage.setItem("kim_game_vorname", eingabe);
  $("player-tag").textContent = "— " + state.spieler;

  hide("start-view");
  await ladePaketeMeta();
  zeigePaketAuswahl();
}

async function ladePaketeMeta() {
  try {
    const resp = await fetch(PAKETE_DATEI + "?v=" + Date.now());
    const data = await resp.json();
    state.pakete = data.pakete || [];
  } catch (e) {
    console.warn("pakete.json nicht ladbar, Fallback:", e);
    state.pakete = [
      { nr: 1, titel: "Paket 1", beschreibung: "Grundlagen-Mix", aktiv: true },
      { nr: 2, titel: "Paket 2", beschreibung: "GenAI aktuell",  aktiv: true }
    ];
  }
}

function zeigePaketAuswahl() {
  show("paket-auswahl-view");
  const grid = $("paket-grid");
  grid.innerHTML = "";
  state.pakete.forEach(p => {
    const card = document.createElement("div");
    card.className = "paket-card" + (p.aktiv ? " aktiv" : " inaktiv");
    card.innerHTML =
      '<div class="paket-nr">Paket ' + p.nr + '</div>' +
      '<div class="paket-titel">' + escapeHtml(p.titel) + '</div>' +
      '<div class="paket-beschr">' + escapeHtml(p.beschreibung || "") + '</div>' +
      (p.aktiv
        ? '<button class="btn btn-submit paket-play">Spielen →</button>'
        : '<span class="paket-locked">bald verfügbar</span>');
    if (p.aktiv) {
      card.querySelector(".paket-play").addEventListener("click", () => {
        hide("paket-auswahl-view");
        show("game-view");
        ladePaket(p.nr);
      });
    }
    grid.appendChild(card);
  });
}

async function ladePaket(nr) {
  state.paketNr = nr;
  // Bilanz für dieses Spiel zurücksetzen
  state.bilanz = { total: 0, richtigBeimErstenVersuch: 0, richtigInsgesamt: 0, teilweise: 0, falsch: 0, uebersprungen: 0, punkte: 0 };
  state.karten = [];
  state.frageIndex = 0;

  try {
    const resp = await fetch(FRAGEN_DATEI + "?v=" + Date.now());
    const data = await resp.json();
    const pool = (data.fragen || []).filter(f => f.paket === nr);
    const gezogen = shuffle([...pool]).slice(0, PAKET_GROESSE);
    state.fragen = gezogen;

    $("level-tag").textContent = "Reise " + nr;
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

function schwierigkeitVon(f) { return f.schwierigkeit || 1; }
function begriffFuer(f) { return (f.glossar && f.glossar.begriff) || f.id; }

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

  const nRichtig = [...gewaehlt].filter(id => korrekt.has(id)).length;
  const nFalsch  = [...gewaehlt].filter(id => !korrekt.has(id)).length;
  const istTeilweise = nRichtig > 0 && nFalsch === 0;

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
    $("btn-next").textContent = isLast ? "Reise abschließen →" : "OK, nächstes Thema →";
    $("btn-next").classList.add("btn-next-thema");
  } else {
    $("btn-next").textContent = isLast ? "Reise abschließen →" : "Weiter →";
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

function feuerwerk(gross) {
  if (typeof confetti !== "function") return;
  const farben = ["#5a3a7a", "#2a7a50", "#7a4a00", "#0a4a7a", "#f0eaf7", "#eaf5ee"];
  confetti({ particleCount: gross ? 180 : 100, spread: 80, origin: { y: 0.55 }, colors: farben });
  setTimeout(() => confetti({ particleCount: gross ? 90 : 55, angle: 60,  spread: 55, origin: { x: 0, y: 0.7 }, colors: farben }), 250);
  setTimeout(() => confetti({ particleCount: gross ? 90 : 55, angle: 120, spread: 55, origin: { x: 1, y: 0.7 }, colors: farben }), 400);
  if (gross) setTimeout(() => confetti({ particleCount: 120, spread: 100, origin: { y: 0.3 }, colors: farben }), 900);
}

function zeigeErgebnis() {
  hide("game-view");
  show("result-view");
  const b = state.bilanz;
  const alleErsterVersuch = b.total > 0 && b.richtigBeimErstenVersuch === b.total;
  feuerwerk(alleErsterVersuch);

  const chips = state.karten.map(k => {
    const cls = "karte karte-" + k.status;
    return '<span class="' + cls + '" title="' + statusLabel(k.status) + '">' + escapeHtml(k.begriff) + '</span>';
  }).join(" ");

  const anz = {
    meister:       state.karten.filter(k => k.status === "meister").length,
    verstanden:    state.karten.filter(k => k.status === "verstanden").length,
    teilweise:     state.karten.filter(k => k.status === "teilweise").length,
    kennengelernt: state.karten.filter(k => k.status === "kennengelernt").length,
    uebersprungen: state.karten.filter(k => k.status === "uebersprungen").length
  };

  const gruss = alleErsterVersuch
    ? "Reise " + state.paketNr + " glatt durchgezogen — alle Fragen im ersten Anlauf!"
    : "Reise " + state.paketNr + " geschafft.";

  $("result-grade").textContent = gruss;
  $("result-label").textContent = "Du hast " + state.karten.length + " Fachbegriff" +
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
    token: SHARED_TOKEN, session: state.session_id, spieler: state.spieler,
    paket: state.paketNr, schwierigkeit: schwierigkeitVon(frage), frage_id: frage.id,
    begriff: begriffFuer(frage), frage_text: frage.frage,
    optionen: frage.optionen,
    gewaehlt: [...state.ausgewaehlt].join(","), korrekt: frage.korrekt.join(","),
    richtig: richtig, versuche: state.attempts, punkte_gesamt: state.bilanz.punkte,
    zeit: new Date().toISOString()
  };
  const ctrl = new AbortController();
  const t = setTimeout(() => ctrl.abort(), FETCH_TIMEOUT_MS);
  fetch(APPS_SCRIPT_URL, {
    method: "POST", mode: "no-cors",
    headers: { "Content-Type": "text/plain;charset=utf-8" },
    body: JSON.stringify(payload), signal: ctrl.signal
  }).catch(err => console.warn("Log-Fehler (ignoriert):", err))
    .finally(() => clearTimeout(t));
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
