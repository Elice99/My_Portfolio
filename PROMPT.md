# Master prompt — "make my portfolio read senior"

Copy everything below the line and hand it to your AI coding agent
(the same one that maintains this repo works fine). Fill in the
`[BRACKETS]` first. If a phase needs your real project material, the
agent should stop and ask you for it — never let it invent fake
numbers, quotes, or code.

---

You are working on my portfolio. It lives in this folder as a plain
static site (HTML/CSS/JS) with a small Python build script in `_build/`.
Read `plan.md` and `architecture.md` in the repo root before doing
anything — they explain how the site works and what we're building.

## What this site is

A portfolio for Elisha Bassey, a data analyst / analytics engineer.
No framework, no node, no backend. Python only *generates* the HTML;
the output runs by double-clicking `index.html` or on any host.
The design language is a mineral-inspired palette (malachite green +
copper, stone neutrals) defined as CSS variables in `css/styles.css`.
The vibe is calm and editorial, not startup-y.

## The goal, in one sentence

Move the site from "here's my work" to "here's how I think" — every
change should reveal judgment and decision-making, because that's what
makes a portfolio read senior.

## Ground rules — break none of these

1. **Stay static.** No frameworks, no node_modules, no CDN JS libraries
   beyond what's already there. Any new behaviour is vanilla JS +
   CSS in the existing files.
2. **The site must always keep working.** After every phase, all pages
   still open by double-click, all local links/assets resolve, and
   `python _build/build.py` regenerates everything cleanly.
3. **Respect the existing patterns.** Page-relative links, WebP-first
   images, cache-busted asset URLs, keyboard access for clickable
   things (`role="button"`, `tabindex="0"`, Enter/Space), and
   `prefers-reduced-motion` fallbacks. If a new component animates,
   it must have a calm static fallback.
4. **Never fabricate content.** If a case study needs a real number,
   decision, failure, or code snippet, ask me. Do not invent plausible
   details. Honesty is a feature of this site.
5. **Content before chrome.** A well-written case study with plain
   styling beats a beautiful page that says nothing. Push me for
   material rather than decorating emptiness.
6. **Do not redesign.** The layout, palette, and typography stay.
   We're deepening, not repainting.
7. Work **one phase at a time**. Finish a phase, tell me what changed
   and how you verified it, and wait for my go-ahead.

## The phases (details in plan.md)

- **Phase 0 — material.** Help me pick the 3 flagship projects and
  interview me for each: the stakes, the 2–3 hard decisions, one
  honest failure, the real outcome numbers, one piece of code I'm
  proud of. You draft the copy from my answers; I approve it.
- **Phase 1 — flagship case studies.** Extend the case-study template
  with new sections (stakes, key decisions, what failed, what I'd do
  differently), turn on the existing unused code-snippet card for
  flagships, and move every non-flagship project to a small archive
  list. Nothing gets deleted — archived projects keep their pages.
- **Phase 2 — the homepage pipeline.** Make the existing DATA →
  INTELLIGENCE → DECISION section run a tiny synthetic dataset through
  itself, with an "inject bad data" button that shows the pipeline
  catching it. Vanilla JS, keyboard operable, reduced-motion fallback.
- **Phase 3 — core sample career scroll.** Rebuild the career timeline
  as a geological core sample you scroll down through, deepest layer =
  earliest role. Ties to my geology background. Must read fine with
  animations off.
- **Phase 4 — writing pages.** New Notes section (3 short essays I'll
  draft with your help), a "How I work" page, and a Methodology page
  that explains how I validate numbers — turning the site's existing
  honesty banners into a deliberate feature.
- **Phase 5 — print + proof.** A print stylesheet so case studies
  collapse into a clean PDF-style handout, plus a Lighthouse pass
  (target 95+ on all four categories) and the scores shown on the
  About page.
- **Phase 6 — "your visit, analyzed".** A tiny footer widget that
  renders the visitor's own scroll depth and time-on-page as a mini
  chart. Client-side only, no network calls, under 2KB, honest copy
  about no tracking.

## Definition of done for every phase

- `python _build/build.py` runs with no errors and every page rebuilt.
- All local links and assets resolve (check every HTML file).
- Keyboard-only walkthrough of new components works (tab in, Enter and
  Space activate, nothing traps focus).
- `prefers-reduced-motion` gets a calm static version.
- Phone-width check: nothing overflows, tap targets are decent.
- No console errors on any page.
- You give me a short summary: what changed, which files, how you
  verified it, and anything you need from me next.

## How to talk to me

Plain language, low jargon. If you need to use a technical term,
explain it in a few words. When you want a decision from me, give me
2–3 concrete options with your recommendation, not an open question.
