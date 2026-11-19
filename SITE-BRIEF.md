# Site brief — everything an AI (or human) needs to know about this website

Paste this document as the first message to any AI assistant and it will
know the site well enough to help. It's written in plain language on
purpose. Companion files in this repo: `PROMPT.md` (how to run the
senior-level build), `plan.md` (the roadmap), `architecture.md` (how the
site works under the hood).

---

## What this website is

A personal portfolio for **Elisha Bassey**, a data analyst and analytics
engineer with a geology background, based in Nigeria. It shows his work:
data analysis, business intelligence dashboards, machine learning, and
small data tools.

The whole thing is **plain HTML, CSS and JavaScript**. No framework, no
React, no node, no backend, no database. You can double-click
`index.html` and the site just works. A small Python script exists only
to *generate* the pages so shared parts (nav, footer, head) never drift
apart — the generated output is what counts.

The site's personality: calm, editorial, honest. Mineral-inspired design
(malachite green + copper on stone neutrals — a nod to the geology
background). No startup gradients, no hype words, no skill bars. The
senior-level goal of the whole site: shift it from *"look at my work"*
to *"watch how I think"*.

## Who Elisha is (context for any writing)

- Data analyst / analytics engineer. Geology degree first, data career after.
- Comfortable across SQL, Python, Excel (Power Query / Power Pivot), Power BI (DAX, M), and ML with XGBoost.
- Writes honestly: real numbers when he has them, explicit "this is synthetic data" when he doesn't, "this needs verifying" when unsure. That honesty is a deliberate feature — never replace it with confident-sounding padding.
- Email: basseyelisha99@gmail.com · GitHub: github.com/Elice99

## The pages

| Page | What's on it |
|---|---|
| `index.html` | Hero with typing effect, profile photo, the DATA → INTELLIGENCE → DECISION section, a **live pipeline demo** (see below), "Selected work" cards, contact strip |
| `work.html` | The 3 **flagship** case-study cards on top, then a compact "Everything else" archive list of the other 9 projects. Category filters work across both |
| `about.html` | Story, second profile photo, career timeline |
| `experience.html` | Detailed roles and a "decision room" walkthrough |
| `capabilities.html` | Skill areas with an interactive filter (cards → matching projects) |
| `now.html` | What he's currently learning/building |
| `resume.html` | Resume page; links a real PDF in `documents/` |
| `contact.html` | Contact details + a form that opens the visitor's email app (mailto hand-off, no backend) |
| `projects/*.html` | 14 case-study pages; several have tabs to **Business insights** and **Technical documentation** pages |

## How it's built (the short version)

```
_build/                    the machine room
  build.py                 main generator: shared head/nav/footer, SEO tags,
                           the PAGES list, SITE_URL constant
  projects_data.py         THE single source of truth for all projects
  build_projects.py        turns that data into case-study pages + JS data
  optimize_images.py       makes WebP copies of every photo
  fragments/               each page's content lives here, one file per page
  docs/                    long-form documentation content per project
css/styles.css             ALL styling; design tokens at the top
js/main.js                 ALL behaviour; one file, guarded per feature
index.html, work.html, …   GENERATED — do not hand-edit
js/projects-data.js        GENERATED — do not hand-edit
images/                    photos; originals AND WebP copies live together
```

The two rules that keep the site healthy:

1. **Edit the `_build/` side, never the generated HTML.** It gets
   overwritten on the next build.
2. **Run `python _build/build.py` after any change.** Adding photos:
   run `python _build/optimize_images.py` first, then the build.

## The project data system (important)

Everything about a project lives in one object in
`_build/projects_data.py`. From that single object, the build generates
its case-study page, its cards on the homepage and work page, its entry
in the command palette, and its image gallery. The data can't drift
between pages because there is only one copy.

Key fields per project:

- `slug`, `title`, `tagline`, `category`, `stack` — the basics
- `problem` / `approach` / `outcome` — the case-study core
- `metricValue` / `metricLabel` — the number badge on cards
- `github`, `demo` — links (demo often None; never invent one)
- `verified` — **if False, the case study shows a visible "placeholder
  content" notice.** This is how the site stays honest while content
  catches up
- `featured` — the homepage hero project (currently TrustLake)
- `flagship` — the three front-of-work-page case studies (currently
  GlowMart, Sales Pipeline Prediction, ER Patient Analysis). NOT
  permanent — flip the flag to promote a project
- `codeSnippet` — optional real code shown in a floating editor-style
  card. Only ever real code, never invented examples
- `hasDocs` — adds Business insights / Technical documentation tabs

**Flagship-only story fields** (new, all currently empty, waiting for
real material — a section renders only when its field is filled):

- `stakes` — what the problem cost or risked, and who cared
- `decisions` — list of `{"title", "text"}`: the genuinely ambiguous
  calls and how each was resolved
- `failure` — one honest thing that went wrong and how it was caught
- `differently` — what he'd change on a redo

**Images need no data edits.** Drop files into `images/` named
`{imagePrefix}_1.png` (or jpg/jpeg/webp), rebuild, done. WebP is
preferred everywhere; originals are kept as the source of truth.

## The design system

All tokens live at the top of `css/styles.css`:

- **Palette**: light and dark variants. Malachite green (`--teal-500`
  family) for the primary accent, copper (`--purple-500`, despite the
  variable name) for the secondary. Stone/grey neutrals, not blue-greys.
  `--teal-600` exists for better small-text contrast.
- **Type**: Inter for UI, JetBrains Mono for anything data-flavoured
  (labels, code, badges).
- **Spacing/radii/shadows/transitions**: all tokenised
  (`--space-*`, `--radius-*`, `--shadow-*`, `--transition-*`).
- **Dark mode**: a `data-theme` attribute on `<html>`, auto-detected
  from `prefers-color-scheme`, with a manual toggle. Dark mode uses
  brighter mineral tones, not a flat inversion.

New styles follow the existing pattern: component classes in the same
file, tokens only (no raw hex values), mobile handled with the same
media-query style the file already uses.

## The JavaScript (one file, lots of small guards)

`js/main.js` runs on every page. Every feature checks "does this
element exist here?" before running, so one file serves all pages.
It contains: the theme toggle, mobile nav, typing effect, the
DATA → INTELLIGENCE → DECISION accordion, the **live pipeline** (below),
capability + category filters, the Cmd/Ctrl+K command palette, runtime
image probing (placeholder slots try WebP → jpg → jpeg → png and swap
in whatever loads), the mailto contact form, and keyboard access for
clickable divs (`role="button"`, `tabindex="0"`, Enter/Space).

Three non-negotiable conventions:

1. **Keyboard access** for anything clickable that isn't a real button
   — the `makeClickable()` helper does this; add new selectors there.
2. **`prefers-reduced-motion` gets a calm fallback** for anything that
   animates.
3. **No new libraries.** The only external scripts are Font Awesome,
   AOS, and Google Fonts. If a feature needs a dependency, rethink it.

## The live pipeline (homepage signature piece)

A panel titled "SEE IT RUN" sits under the three system stages. Nine
synthetic orders flow through DATA (validation: missing amounts,
duplicate ids, negative values, unknown cities get flagged or dropped)
→ INTELLIGENCE (clean revenue by branch, mini bar chart) → DECISION
(a one-line recommendation with a confidence tag).

The **"Inject bad data"** button adds dirty rows one at a time; with
enough bad data the confidence tag drops from HIGH to MID to LOW, and
at LOW the pipeline refuses to recommend anything. The point it makes:
this analyst's portfolio *demonstrates* data-quality discipline instead
of claiming it.

Implementation notes: vanilla JS (~6KB), no canvas, no libraries,
triple-fallback auto-start (IntersectionObserver + first scroll + a
timer, first one wins), keyboard operable, reduced-motion renders the
final state instantly.

## Honesty features (keep these)

- `verified: False` projects wear a visible placeholder notice.
- The ER case study openly lists what doesn't match its source file.
- Outcome copy uses calibrated language ("a documented baseline", not
  "an accurate model").
- The contact form says plainly that it opens an email app.
- When a number is synthetic, the page says so.

## Current state (as of November 2026)

**Done**: SEO plumbing (canonical, Open Graph, Twitter cards, Person
JSON-LD driven by one `SITE_URL` constant), WebP image optimisation
(13.7 MB → 3.9 MB), cache-busted local CSS/JS, `<main>` landmark on
every page, keyboard access, contrast fixes, mailto contact form, the
live pipeline, the flagship/archive split on the work page, and the
render-if-present story sections in the case-study template.

**In progress**: filling the three flagships' story fields with real
material (GlowMart interview under way; Sales Pipeline and ER next).

**Not started yet** (see `plan.md`): Notes/essays section, "How I work"
page, Methodology page, print stylesheet, geological core-sample career
scroll, "your visit, analyzed" footer widget, a fresh Lighthouse pass
(target: 95+ everywhere).

**Deliberately not being dealt with right now**: deployment. The site
is not live anywhere yet. `SITE_URL` in `_build/build.py` currently
points at a GitHub Pages URL as a placeholder.

## Rules for anyone (or any AI) working on this site

1. Never fabricate content — numbers, quotes, code, links, demos. Ask
   Elisha instead. If something is unknown, say so on the page.
2. Keep the site static and framework-free; double-click must always work.
3. New interactive things: keyboard accessible, mobile-safe, calm under
   reduced motion.
4. Edit `_build/` sources, then rebuild — never the generated HTML.
5. One phase at a time; report what changed and how it was verified;
   wait for a go-ahead.
6. When a decision is needed, offer 2–3 concrete options with a
   recommendation, not an open-ended question.
7. Match the existing voice (below). If a sentence could appear on a
   LinkedIn hustler profile, rewrite it.

## Voice and writing style

First person, plain words, short sentences. Specific numbers when real,
honesty when not. Dry humour is welcome; hype is not. Banned words:
passionate, ninja, rockstar, synergy, leverage (as a verb), cutting-edge.
Good sentences sound like: *"Stock was already fair — revenue share and
customer share were within 0.3% in every city."* — evidence, stated
calmly, then the actual point.
