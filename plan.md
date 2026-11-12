# Plan — turning the portfolio senior

Casual companion to `architecture.md` (how the site works) and
`PROMPT.md` (what to paste into an AI agent). This file is the
roadmap: what we're doing, why, in what order, and what "done"
looks like.

## The idea in one sentence

The site currently says *"look at my work"*; senior says
*"watch how I think"* — so every change we make should expose a
decision, a tradeoff, or a reason.

## The five things that actually move the needle

1. **Three flagship case studies with the full story.** Stakes, the
   messy middle, one honest failure, real outcome numbers. This is
   ~70% of the value and it needs Elisha's real project material —
   no amount of design can fake it.
2. **The homepage pipeline.** The DATA → INTELLIGENCE → DECISION
   section stops being a diagram and starts being a tiny machine the
   visitor can play with (and break).
3. **Writing.** A Notes section, a "How I work" page, a Methodology
   page. Short, sharp, honest. Writing is the fastest seniority
   signal there is.
4. **Craft as a credential.** Print stylesheet, 95+ Lighthouse scores
   shown on the site, keyboard + reduced-motion everywhere.
5. **One memorable personal signature.** The geological core sample
   career scroll — nobody else has it, and it explains why the
   portfolio sticks in someone's head.

## Ground rules

- Stay static and framework-free. Double-click `index.html` must
  always work.
- Keep the mineral palette and the honest "to confirm" banners —
  honesty is a feature, not a bug to clean up.
- New interactive things: keyboard accessible, mobile-safe, and they
  calm down when `prefers-reduced-motion` is set.
- No WebGL, no heavy animation libraries, no scrolljacking, no skill
  bars, no stock testimonials. Ever.
- Content before chrome. We don't decorate pages that don't say
  anything yet.

## Phases

### Phase 0 — pick your three (homework, no code) · ~a week of thinking
Choose the 3 flagship projects. For each, fill in the template below.
Everything else moves to an archive list later.

- **Stakes:** what did the problem cost — money, hours, risk? Who
  cared and why?
- **Two or three hard decisions:** where was it genuinely ambiguous,
  and how did you resolve it?
- **One failure:** what did you build that turned out wrong, and how
  did you catch it?
- **Outcome:** honest numbers, before/after.
- **One code snippet** you're proud of (SQL, Python, DAX — whatever
  shows real craft).

**Done when:** three filled-in templates exist.

### Phase 1 — flagship case studies (biggest bang) · agent + you
- Extend the case-study template (`_build/build_projects.py` +
  `_build/projects_data.py`) with new sections: stakes, key
  decisions, what failed, what I'd do differently.
- Turn on the built-but-unused code snippet card for the flagships,
  with real code.
- Add an archive list for every other project — one line each,
  their pages keep working.
- Clear all "to confirm" banners on flagships by confirming or
  removing the claims.

**Done when:** every flagship reads problem → stakes → decisions →
failure → outcome, with zero placeholders.

### Phase 2 — the homepage pipeline (the wow) · agent
The existing system-stages section runs a small synthetic dataset
through itself: raw rows appear at DATA, get cleaned and aggregated
at INTELLIGENCE, and resolve into a one-line recommendation at
DECISION. A button injects bad data; the pipeline flags it and the
recommendation downgrades to "insufficient confidence."

Why: a data analyst whose own portfolio demonstrates data-quality
handling is making the argument no bullet point can.

**Done when:** it runs smoothly on a mid-range phone, works with
keyboard only, has a static reduced-motion fallback, and the whole
thing is vanilla JS under ~10KB.

### Phase 3 — core sample career scroll · agent
Career journey rendered as a geological column you scroll down
through — deepest stratum is the earliest role, each layer labelled
like a core sample. Ties the geology background into the identity of
the site.

**Done when:** it reads perfectly with animations off, works on
mobile, and doesn't need a single library.

### Phase 4 — writing pages · you draft, agent builds
- **Notes:** three short essays (e.g. "Why most dashboards get
  ignored", "How I validate a metric before it ships").
- **How I work:** requirements gathering, ambiguity, stakeholder
  communication — the page hiring managers actually read.
- **Methodology:** how numbers on this site were validated, with
  confidence levels. Turns the honesty banners into a system.

**Done when:** real writing is published — no filler, no lorem.

### Phase 5 — print + proof · agent
- Print stylesheet: a case study prints as a clean one/two-page
  handout.
- Lighthouse pass targeting 95+ on performance, accessibility, best
  practices, SEO — then show the scores on the About page.

**Done when:** print preview looks like something you'd hand a
recruiter, and the scores are real.

### Phase 6 — "your visit, analyzed" · agent
A tiny footer widget that charts the visitor's own scroll depth and
time-on-page for the current visit. Client-side only, nothing leaves
the browser, honest one-line caption.

**Done when:** under 2KB of JS, works everywhere, and it makes
people smile.

## Order and effort

| Phase | Depends on | Who does the heavy lifting | Effort |
|---|---|---|---|
| 0 material | — | Elisha | a week of thinking |
| 1 case studies | 0 | agent builds, Elisha writes | biggest chunk |
| 2 pipeline | — (safe anytime after 1) | agent | ~a focused day |
| 3 core sample | — | agent | ~a day |
| 4 writing | 0 mindset | Elisha drafts, agent builds | spread out |
| 5 print + proof | 1 | agent | half a day |
| 6 visit widget | — | agent | a couple of hours |

Phases 2, 3, and 6 are independent — they can slot in whenever.
Phases 1 and 4 are the ones that need real material from Elisha.

## How we'll know it worked

A stranger can land on the site and, within two minutes, describe
what kind of thinker Elisha is — not just what tools he lists.
