// ===== SHARED PORTFOLIO JAVASCRIPT =====
// Loaded on every page. Each block guards for element existence so this
// one file works whether a page has a navbar-only layout or the full
// homepage — no page-specific script files needed.

// ===== PAGE-RELATIVE ROOT + AUTOMATIC IMAGE DISCOVERY =====
// SITE_ROOT is set in every page's <head> ("" on top-level pages, "../" inside
// /projects/). Building links from it means the site works when index.html is
// double-clicked AND when it is hosted. No build step is needed for images:
// the browser simply tries images/<Name>.jpg, .jpeg, .png, .webp for every slot
// and uses the first one that loads. Use lowercase extensions (hosts are
// case-sensitive).
const ROOT = window.SITE_ROOT || '';
const IMG_EXTS = ['webp', 'jpg', 'jpeg', 'png'];

function probeImage(base) {
  return new Promise((resolve) => {
    let i = 0;
    (function next() {
      if (i >= IMG_EXTS.length) return resolve(null);
      const url = ROOT + 'images/' + base + '.' + IMG_EXTS[i++];
      const img = new Image();
      img.onload = () => resolve(url);
      img.onerror = next;
      img.src = url;
    })();
  });
}

async function probeFirst(names) {
  for (const n of names) {
    const url = await probeImage(n.trim());
    if (url) return url;
  }
  return null;
}

// Placeholders marked data-img-swap="Name[,Fallback]" turn into the real image if it exists.
function hydrateImages(scope) {
  (scope || document).querySelectorAll('[data-img-swap]').forEach(async (el) => {
    if (el.dataset.imgDone) return;
    el.dataset.imgDone = '1';
    const url = await probeFirst(el.getAttribute('data-img-swap').split(','));
    if (!url) return;
    const img = document.createElement('img');
    img.src = url;
    img.alt = el.getAttribute('data-img-alt') || '';
    img.loading = 'lazy';
    img.decoding = 'async';
    const cls = el.getAttribute('data-img-class');
    if (cls) img.className = cls;
    if (cls === 'profile-photo') img.style.cssText = 'width:100%;height:100%;object-fit:cover;display:block';
    el.replaceWith(img);
    if (img.parentElement && img.parentElement.classList.contains('project-visual')) {
      img.parentElement.classList.add('has-image');
    }
  });
}

// Case-study pages: look for <Prefix>_1 .. _5 and build the scrollable gallery.
function hydrateGalleries() {
  document.querySelectorAll('[data-gallery]').forEach(async (box) => {
    const prefix = box.getAttribute('data-gallery');
    const results = await Promise.all([1, 2, 3, 4, 5].map((n) => probeImage(prefix + '_' + n)));
    const found = results.filter(Boolean);
    if (!found.length) return;
    const title = document.title.split('|')[0].trim();
    const frames = found.map((src, i) =>
      '<div class="media-gallery-frame' + (found.length === 1 ? ' single' : '') + '">' +
      '<img src="' + src + '" alt="' + title + ' screenshot ' + (i + 1) + '" loading="lazy"></div>').join('');
    const label = found.length > 1
      ? '<p class="media-gallery-count">' + found.length + ' SCREENSHOTS, SCROLL TO SEE MORE &rarr;</p>' : '';
    const keep = box.querySelector('.code-float'); // keep any floating code card
    box.innerHTML = '<div class="media-gallery">' + frames + '</div>' + label;
    if (keep) box.appendChild(keep);
  });
}

document.addEventListener('DOMContentLoaded', function () {

  // ===== AOS INIT =====
  if (window.AOS) {
    AOS.init({
      duration: 700,
      once: true,
      offset: 80,
      easing: 'ease-out-cubic',
      disable: window.matchMedia('(prefers-reduced-motion: reduce)').matches
    });
  }

  // ===== THEME TOGGLE (persisted, respects system preference on first visit) =====
  const themeToggle = document.getElementById('themeToggle');
  const html = document.documentElement;

  function systemPrefersDark() {
    return window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
  const stored = localStorage.getItem('theme');
  const initialTheme = stored || (systemPrefersDark() ? 'dark' : 'light');
  html.setAttribute('data-theme', initialTheme);
  updateThemeIcon(initialTheme);

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const current = html.getAttribute('data-theme');
      const next = current === 'light' ? 'dark' : 'light';
      html.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
      updateThemeIcon(next);
      const icon = themeToggle.querySelector('i');
      if (icon) {
        icon.style.transform = 'rotate(360deg)';
        setTimeout(() => (icon.style.transform = 'rotate(0deg)'), 300);
      }
    });
  }
  function updateThemeIcon(theme) {
    if (!themeToggle) return;
    const icon = themeToggle.querySelector('i');
    if (icon) icon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
  }

  // ===== MOBILE NAVIGATION =====
  const mobileToggle = document.getElementById('mobileToggle');
  const navMenu = document.getElementById('navMenu');
  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      mobileToggle.classList.toggle('active');
      navMenu.classList.toggle('active');
    });
    document.querySelectorAll('.nav-link').forEach((link) => {
      link.addEventListener('click', () => {
        mobileToggle.classList.remove('active');
        navMenu.classList.remove('active');
      });
    });
  }

  // ===== STICKY NAVBAR =====
  const navbar = document.getElementById('navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.pageYOffset > 50);
    });
  }

  // ===== BACK TO TOP =====
  const backToTop = document.getElementById('backToTop');
  if (backToTop) {
    window.addEventListener('scroll', () => {
      backToTop.classList.toggle('visible', window.pageYOffset > 500);
    });
    backToTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // ===== HERO ROLE TYPING ANIMATION (home page only) =====
  const roleElement = document.getElementById('roleText');
  if (roleElement) {
    const roles = ['Data Analyst', 'Analytics Engineer', 'BI Specialist', 'Problem Solver'];
    let roleIndex = 0, charIndex = 0, isDeleting = false;
    function typeRole() {
      const currentRole = roles[roleIndex];
      roleElement.textContent = isDeleting
        ? currentRole.substring(0, charIndex - 1)
        : currentRole.substring(0, charIndex + 1);
      charIndex += isDeleting ? -1 : 1;
      let speed = isDeleting ? 50 : 100;
      if (!isDeleting && charIndex === currentRole.length) { speed = 2000; isDeleting = true; }
      else if (isDeleting && charIndex === 0) { isDeleting = false; roleIndex = (roleIndex + 1) % roles.length; }
      setTimeout(typeRole, speed);
    }
    typeRole();
  }

  // ===== SYSTEM SECTION: DATA -> INTELLIGENCE -> DECISION (click to expand) =====
  document.querySelectorAll('.system-stage').forEach((stage) => {
    stage.addEventListener('click', () => {
      const wasActive = stage.classList.contains('active');
      document.querySelectorAll('.system-stage').forEach((s) => s.classList.remove('active'));
      if (!wasActive) stage.classList.add('active');
    });
  });

  // These controls are clickable <div>s. Give them keyboard access so
  // Enter/Space work the same as a mouse click.
  function makeClickable(selector) {
    document.querySelectorAll(selector).forEach((el) => {
      el.setAttribute('role', 'button');
      el.setAttribute('tabindex', '0');
      el.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          el.click();
        }
      });
    });
  }
  makeClickable('.system-stage-head');
  makeClickable('.capability-card');
  makeClickable('.decision-step-head');

  // ===== LIVE PIPELINE (homepage): the three stages above, running =====
  // A tiny synthetic order book flows through DATA -> INTELLIGENCE ->
  // DECISION using the same rules I apply on real work. "Inject bad
  // data" adds a dirty row so visitors can watch the checks catch it
  // and the recommendation lose confidence. Synthetic data, real rules.
  const pipe = document.getElementById('pipe');
  if (pipe) {
    const rowsEl = document.getElementById('pipeRows');
    const detailEl = document.getElementById('pipeDetail');
    const stageChips = pipe.querySelectorAll('.pipe-stage');
    const injectBtn = document.getElementById('pipeInject');
    const resetBtn = document.getElementById('pipeReset');
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const fmt = (n) => '\u20A6' + n.toLocaleString('en-NG');

    const BRANCHES = ['Lagos', 'Abuja', 'Kano', 'Port Harcourt'];
    const TYPOS = { 'Lagiis': 'Lagos' };

    const seedRows = () => [
      { id: 'GM-1001', city: 'Lagos', amount: 42000 },
      { id: 'GM-1002', city: 'Abuja', amount: 31500 },
      { id: 'GM-1003', city: 'Lagos', amount: 27500 },
      { id: 'GM-1004', city: 'Kano', amount: 18800 },
      { id: 'GM-1005', city: 'Port Harcourt', amount: 22400 },
      { id: 'GM-1006', city: 'Lagos', amount: 36200 },
      { id: 'GM-1007', city: 'Abuja', amount: 19900 },
      { id: 'GM-1008', city: 'Kano', amount: 14300 },
      { id: 'GM-1009', city: 'Lagiis', amount: 24000 }, // typo the pipeline fixes
    ];

    // Each break case demonstrates a different rule: drop, dedupe,
    // impossible value, or keep-but-flag.
    const BAD_POOL = [
      { id: 'GM-1010', city: 'Lagos', amount: null, note: 'amount missing' },
      { id: 'GM-1003', city: 'Kano', amount: 5000, note: 'duplicate id' },
      { id: 'GM-1011', city: 'Lagos', amount: -8000, note: 'negative amount' },
      { id: 'GM-1012', city: 'Nnewi', amount: 26000, note: 'city not on file' },
    ];

    let rows = seedRows();
    let injected = 0;
    let running = false;
    let finished = false;

    function runPipeline(input) {
      const seen = new Set();
      const state = input.map((r) => {
        const problems = [];
        let keep = true;
        let city = r.city;
        if (r.amount === null) { problems.push('amount missing'); keep = false; }
        else if (r.amount < 0) { problems.push('negative amount'); keep = false; }
        if (seen.has(r.id)) { problems.push('duplicate id'); keep = false; }
        seen.add(r.id);
        if (TYPOS[city]) { problems.push('city misspelt'); city = TYPOS[city]; }
        else if (!BRANCHES.includes(city)) { problems.push('city not on file'); city = 'Other'; }
        return Object.assign({}, r, { city, keep, problems });
      });
      const used = state.filter((r) => r.keep);
      const total = used.reduce((s, r) => s + r.amount, 0);
      const byCity = {};
      used.forEach((r) => { byCity[r.city] = (byCity[r.city] || 0) + r.amount; });
      const ranked = Object.keys(byCity).map((c) => [c, byCity[c]]).sort((a, b) => b[1] - a[1]);
      const flagged = state.filter((r) => r.problems.length > 0).length;
      const ratio = state.length ? flagged / state.length : 0;
      const confidence = ratio <= 0.2 ? 'high' : ratio <= 0.35 ? 'mid' : 'low';
      return { state: state, used: used, total: total, ranked: ranked, flagged: flagged, ratio: ratio, confidence: confidence };
    }

    function chipFor(r) {
      if (!r.keep) return '<span class="pipe-chip drop">DROPPED</span>';
      if (r.problems.length) return '<span class="pipe-chip flag">FLAGGED</span>';
      return '<span class="pipe-chip ok">OK</span>';
    }

    function renderRows(result) {
      rowsEl.innerHTML = result.state.map((r) => {
        const amount = r.amount === null ? '&mdash;' : fmt(r.amount);
        return '<div class="pipe-row' + (r.keep ? '' : ' dropped') + '">' +
          '<span>' + r.id + '</span><span>' + r.city + '</span>' +
          '<span>' + amount + '</span>' + chipFor(r) + '</div>';
      }).join('');
    }

    function dataView(result) {
      const head = '<div class="pipe-detail-title">DATA &middot; VALIDATION LOG</div>';
      const problems = result.state.filter((r) => r.problems.length > 0);
      if (!problems.length) {
        return head + '<div class="pipe-log-line clean"><i class="fas fa-check"></i><span>' +
          result.state.length + ' rows in, nothing flagged</span></div>';
      }
      const lines = problems.map((r) =>
        '<div class="pipe-log-line"><i class="fas fa-triangle-exclamation"></i><span>' +
        r.id + ' &middot; ' + r.problems[0] + '</span></div>');
      return head + lines.join('') +
        '<div class="pipe-note">' + result.state.length + ' rows in &middot; ' +
        result.flagged + ' flagged</div>';
    }

    function intelView(result) {
      const max = result.ranked.length ? result.ranked[0][1] : 0;
      const bars = result.ranked.slice(0, 4).map((pair) =>
        '<div class="pipe-bar-row"><span>' + pair[0] + '</span>' +
        '<div class="pipe-bar"><div class="pipe-fill" style="width:' +
        (max ? Math.round(pair[1] / max * 100) : 0) + '%"></div></div>' +
        '<span>' + fmt(pair[1]) + '</span></div>').join('');
      return '<div class="pipe-detail-title">INTELLIGENCE &middot; CLEAN REVENUE BY BRANCH</div>' + bars +
        '<div class="pipe-note">' + result.used.length + ' of ' + result.state.length +
        ' rows used &middot; ' + fmt(result.total) + ' clean total</div>';
    }

    function decisionView(result) {
      const head = '<div class="pipe-detail-title">DECISION</div>';
      if (result.confidence === 'low' || !result.ranked.length) {
        return head + '<div class="pipe-verdict">Insufficient confidence to recommend anything.</div>' +
          '<div class="pipe-note">Too much of the data failed checks (' + Math.round(result.ratio * 100) +
          '%). Fix the source and re-run &mdash; deciding on this would be guessing.</div>' +
          '<span class="pipe-confidence low">CONFIDENCE: LOW</span>';
      }
      const city = result.ranked[0][0];
      const share = Math.round(result.ranked[0][1] / result.total * 100);
      let note = 'Based on ' + result.used.length + ' clean rows.';
      if (result.confidence === 'mid') note += ' Directional only &mdash; verify before committing budget.';
      return head + '<div class="pipe-verdict">Restock <span class="accent">' + city +
        '</span> first &mdash; it is ' + share + '% of clean revenue.</div>' +
        '<div class="pipe-note">' + note + '</div>' +
        '<span class="pipe-confidence ' + result.confidence + '">CONFIDENCE: ' +
        result.confidence.toUpperCase() + '</span>';
    }

    function setChips(upTo) {
      stageChips.forEach((chip) => {
        chip.classList.toggle('active', chip.getAttribute('data-pipe-stage') === upTo);
      });
    }

    function viewFor(key, result) {
      if (key === 'intelligence') return intelView(result);
      if (key === 'decision') return decisionView(result);
      return dataView(result);
    }

    // After a run, the panel follows whichever accordion stage is open.
    function syncToStage(result) {
      const active = document.querySelector('.system-stage.active');
      if (active) detailEl.innerHTML = viewFor(active.getAttribute('data-stage'), result);
    }

    function run(step) {
      const result = runPipeline(rows);
      renderRows(result);
      if (reduceMotion) {
        stageChips.forEach((c) => c.classList.add('active'));
        finished = true;
        syncToStage(result);
        return;
      }
      running = true; finished = false;
      const wait = step || 650;
      setChips('data');
      detailEl.innerHTML = dataView(result);
      window.setTimeout(() => { setChips('intelligence'); detailEl.innerHTML = intelView(result); }, wait);
      window.setTimeout(() => {
        setChips('decision');
        detailEl.innerHTML = decisionView(result);
        running = false; finished = true;
        syncToStage(result);
      }, wait * 2);
    }

    // Clicking an accordion stage re-aims the panel at that stage's view.
    document.querySelectorAll('.system-stage').forEach((stage) => {
      stage.addEventListener('click', () => {
        if (!finished || running) return;
        detailEl.innerHTML = viewFor(stage.getAttribute('data-stage'), runPipeline(rows));
      });
    });

    injectBtn.addEventListener('click', () => {
      if (injected >= BAD_POOL.length) return;
      rows.push(Object.assign({}, BAD_POOL[injected]));
      injected += 1;
      if (injected >= BAD_POOL.length) {
        injectBtn.disabled = true;
        injectBtn.innerHTML = '<i class="fas fa-check"></i> every break case used';
      }
      run(reduceMotion ? 0 : 420);
    });

    resetBtn.addEventListener('click', () => {
      rows = seedRows();
      injected = 0;
      injectBtn.disabled = false;
      injectBtn.innerHTML = '<i class="fas fa-vial"></i> Inject bad data';
      run();
    });

    // First run happens the first time the panel scrolls into view.
    // Three triggers race: IntersectionObserver, first scroll, and a
    // timer. First one wins — the demo always starts.
    let started = false;
    let startTimer = null;
    const startOnce = () => {
      if (started) return;
      started = true;
      window.removeEventListener('scroll', startOnce);
      if (startTimer) window.clearTimeout(startTimer);
      run();
    };
    if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver((entries) => {
        if (entries.some((e) => e.isIntersecting)) startOnce();
      }, { threshold: 0.2 });
      io.observe(pipe);
    }
    window.addEventListener('scroll', startOnce, { passive: true });
    startTimer = window.setTimeout(startOnce, 1500);
  }

  // ===== DECISION ROOM =====
  const startBtn = document.getElementById('startInvestigation');
  const decisionSteps = document.getElementById('decisionSteps');
  if (startBtn && decisionSteps) {
    startBtn.addEventListener('click', () => {
      startBtn.style.display = 'none';
      decisionSteps.style.display = 'block';
    });
  }
  document.querySelectorAll('.decision-step-head').forEach((head) => {
    head.addEventListener('click', () => {
      const step = head.closest('.decision-step');
      const wasActive = step.classList.contains('active');
      document.querySelectorAll('.decision-step').forEach((s) => s.classList.remove('active'));
      if (!wasActive) step.classList.add('active');
    });
  });

  // ===== CAPABILITY FILTER (capabilities.html) =====
  const capabilityCards = document.querySelectorAll('.capability-card');
  const capabilityResults = document.getElementById('capabilityResults');
  if (capabilityCards.length && capabilityResults && typeof PROJECTS !== 'undefined') {
    capabilityCards.forEach((card) => {
      card.addEventListener('click', () => {
        const wasActive = card.classList.contains('active');
        capabilityCards.forEach((c) => c.classList.remove('active'));
        if (wasActive) {
          capabilityResults.innerHTML = '';
          capabilityResults.style.display = 'none';
          return;
        }
        card.classList.add('active');
        const category = card.getAttribute('data-category');
        const matches = PROJECTS.filter((p) => p.category.includes(category));
        capabilityResults.style.display = 'block';
        capabilityResults.innerHTML =
          '<p class="decision-prompt">PROJECTS DEMONSTRATING ' + category.toUpperCase() + '</p>' +
          '<div class="projects-grid" style="margin-top:1.5rem">' +
          matches.map((p) => (typeof projectCardHTML === 'function' ? projectCardHTML(p, { aos: 'fade-up' }) : '')).join('') +
          '</div>';
        if (window.AOS) AOS.refreshHard();
        hydrateImages(capabilityResults);
      });
    });
  }

  // ===== EVIDENCE COUNTER ANIMATION =====
  const evidenceValues = document.querySelectorAll('.evidence-value[data-count]');
  if (evidenceValues.length) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        const raw = el.getAttribute('data-count');
        const numeric = raw.replace(/[^\d]/g, '');
        if (!numeric) { observer.unobserve(el); return; } // non-numeric metrics (e.g. "R² 0.4553") display as-is
        const target = parseInt(numeric, 10);
        const prefix = raw.split(numeric)[0] || '';
        const start = performance.now();
        const duration = 900;
        function tick(now) {
          const progress = Math.min((now - start) / duration, 1);
          el.textContent = prefix + Math.round(target * progress).toLocaleString();
          if (progress < 1) requestAnimationFrame(tick);
        }
        requestAnimationFrame(tick);
        observer.unobserve(el);
      });
    }, { threshold: 0.4 });
    evidenceValues.forEach((el) => observer.observe(el));
  }

  // ===== PROJECT FILTERING (work.html) =====
  const filterBtns = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card[data-category], .archive-row[data-category]');
  if (filterBtns.length) {
    filterBtns.forEach((btn) => {
      btn.addEventListener('click', () => {
        filterBtns.forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
        const filter = btn.getAttribute('data-filter');
        projectCards.forEach((card) => {
          const categories = (card.getAttribute('data-category') || '').split(' ');
          const show = filter === 'all' || categories.includes(filter);
          card.style.display = show ? '' : 'none';
        });
      });
    });

    // Arriving from the homepage pipeline icons (e.g. work.html?category=bi)
    // applies that filter automatically instead of landing on "All" and
    // making the visitor redo the click themselves.
    const requestedCategory = new URLSearchParams(window.location.search).get('category');
    if (requestedCategory) {
      const matchingBtn = document.querySelector('.filter-btn[data-filter="' + requestedCategory + '"]');
      if (matchingBtn) matchingBtn.click();
    }
  }

  // ===== COMMAND PALETTE (Cmd/Ctrl+K) =====
  const cmdkOverlay = document.getElementById('cmdkOverlay');
  const cmdkInput = document.getElementById('cmdkInput');
  const cmdkList = document.getElementById('cmdkList');
  if (cmdkOverlay && cmdkInput && cmdkList) {
    const staticItems = [
      { label: 'Home', icon: 'fa-house', href: ROOT + 'index.html' },
      { label: 'Work', icon: 'fa-briefcase', href: ROOT + 'work.html' },
      { label: 'About Elisha', icon: 'fa-user', href: ROOT + 'about.html' },
      { label: 'Experience', icon: 'fa-clock-rotate-left', href: ROOT + 'experience.html' },
      { label: 'Capabilities', icon: 'fa-layer-group', href: ROOT + 'capabilities.html' },
      { label: 'Now', icon: 'fa-bolt', href: ROOT + 'now.html' },
      { label: 'Resume', icon: 'fa-file', href: ROOT + 'resume.html' },
      { label: 'Contact', icon: 'fa-envelope', href: ROOT + 'contact.html' },
      { label: 'GitHub', icon: 'fa-github', href: 'https://github.com/Elice99' },
      { label: 'LinkedIn / Linktree', icon: 'fa-link', href: 'https://linktr.ee/elice99' },
      { label: 'Toggle theme', icon: 'fa-circle-half-stroke', action: () => themeToggle && themeToggle.click() },
    ];
    const projectItems = (typeof PROJECTS !== 'undefined' ? PROJECTS : []).map((p) => ({
      label: 'Project: ' + p.title,
      icon: 'fa-diagram-project',
      href: ROOT + 'projects/' + p.slug + '.html',
    }));
    const allItems = staticItems.concat(projectItems);

    function render(items) {
      if (!items.length) {
        cmdkList.innerHTML = '<div class="cmdk-empty">No results</div>';
        return;
      }
      cmdkList.innerHTML = items.map((item, i) =>
        '<button type="button" class="cmdk-item' + (i === 0 ? ' selected' : '') + '" data-index="' + i + '">' +
          '<i class="fas ' + item.icon + '"></i><span>' + item.label + '</span>' +
        '</button>'
      ).join('');
      cmdkList.querySelectorAll('.cmdk-item').forEach((btn, i) => {
        btn.addEventListener('click', () => runItem(items[i]));
      });
    }
    function runItem(item) {
      closeCmdk();
      if (item.action) item.action();
      else if (item.href) window.location.href = item.href;
    }
    function openCmdk() {
      cmdkOverlay.classList.add('open');
      cmdkInput.value = '';
      render(allItems);
      setTimeout(() => cmdkInput.focus(), 10);
    }
    function closeCmdk() {
      cmdkOverlay.classList.remove('open');
    }
    cmdkInput.addEventListener('input', () => {
      const q = cmdkInput.value.toLowerCase();
      render(allItems.filter((item) => item.label.toLowerCase().includes(q)));
    });
    cmdkOverlay.addEventListener('click', (e) => {
      if (e.target === cmdkOverlay) closeCmdk();
    });
    document.addEventListener('keydown', (e) => {
      const isMod = e.metaKey || e.ctrlKey;
      if (isMod && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        cmdkOverlay.classList.contains('open') ? closeCmdk() : openCmdk();
      }
      if (e.key === 'Escape') closeCmdk();
    });
    document.querySelectorAll('[data-cmdk-trigger]').forEach((btn) => {
      btn.addEventListener('click', openCmdk);
    });
  }

  // ===== CONTACT FORM (contact.html) =====
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const formData = new FormData(this);
      const data = Object.fromEntries(formData);
      if (!data.name || !data.email || !data.message) {
        showNotification('Please fill in all required fields', 'error');
        return;
      }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)) {
        showNotification('Please enter a valid email address', 'error');
        return;
      }
      // No backend needed: hand the message to the visitor's email client.
      // If a form service (Formspree, Netlify Forms) is added later, replace
      // this block with a fetch() POST to that endpoint.
      const subject = encodeURIComponent('Portfolio enquiry from ' + data.name);
      const body = encodeURIComponent(
        'Name: ' + data.name + '\n' +
        'Email: ' + data.email + '\n\n' +
        data.message
      );
      window.location.href = 'mailto:basseyelisha99@gmail.com?subject=' + subject + '&body=' + body;
      showNotification('Opening your email app — the message is ready to send.', 'success');
      this.reset();
    });
  }
  function showNotification(message, type) {
    const existing = document.querySelector('.notification');
    if (existing) existing.remove();
    const notification = document.createElement('div');
    notification.className = 'notification notification-' + type;
    notification.innerHTML = '<i class="fas ' + (type === 'success' ? 'fa-check-circle' : 'fa-exclamation-circle') + '"></i><span>' + message + '</span>';
    document.body.appendChild(notification);
    setTimeout(() => {
      notification.style.animation = 'slideOutRight 0.3s ease';
      setTimeout(() => notification.remove(), 300);
    }, 5000);
  }
});


// Runs after the page's own scripts (which render the project cards), so cards exist.
document.addEventListener('DOMContentLoaded', function () {
  hydrateImages();
  hydrateGalleries();
});
