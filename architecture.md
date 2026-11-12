# Architecture — how this site actually works

Written for future-Elisha and for any AI agent working on the repo.
Casual on purpose: if you read this once, you'll know where everything
lives and why the odd choices are the right ones.

## The one big idea

**The published site is plain files.** There is no framework, no node,
no server needed. You can double-click `index.html` and everything
works. A Python script exists only to *generate* those files so you
don't hand-edit the same header on twenty pages.

```
_build/                  ← the machine room (never deployed, but harmless if it is)
  build.py               ← the main generator: shared head, nav, footer, pages
  build_projects.py      ← turns project data into case-study pages + js data
  projects_data.py       ← THE single source of truth for projects
  optimize_images.py     ← makes .webp copies of every photo
  fragments/             ← page content, one file per page ("home.html" etc.)
  docs/                  ← long-form documentation content per project
  toolbox_data.py        ← the tools grid data

css/styles.css           ← all styling, palette as CSS variables at the top
js/main.js               ← all behaviour, one file, every page
js/projects-data.js      ← GENERATED, do not hand-edit
images/                  ← photos; originals AND .webp copies live here
documents/               ← the CV pdf
projects/*.html          ← GENERATED case-study pages
index.html, work.html …  ← GENERATED pages
```

If you only remember two rules:

1. **Edit the `_build/` side, never the generated HTML** (it gets
   overwritten on the next build).
2. **Run `python _build/build.py`** after any change, and
   `python _build/optimize_images.py` after adding photos.

## How a page gets built

`build.py` keeps a list called `PAGES` — each entry is basically
"fragment + title + description + where it lives". For each one it
calls `assemble()`, which stitches together:

```
<head>      title, description, canonical/social tags, JSON-LD, css link
<body>      shared nav
<main>      the page's fragment content
<footer>    shared footer
scripts     aos + projects-data.js + main.js
</body>
```

Nice details baked in:

- `SITE_URL` at the top of `build.py` is the one place the real web
  address is written. Every canonical/og/JSON-LD tag derives from it.
- Local CSS/JS links get a `?v=<hash>` suffix at build time, so when
  you ship an update, returning visitors don't get stuck with an old
  cached file.
- Every page gets `<main id="main-content">` — good for
  accessibility and screen readers.

## Projects and the "just name your files right" trick

All project content lives in `_build/projects_data.py`. The build
script scans `images/` for files named like `GlowMart_1.png`,
`GlowMart_2.png`… and wires them up automatically. No data file edits
to add a photo.

Format preference is WebP first, with jpg/jpeg/png as fallbacks.
That order exists in two places, and they must match:

- `_build/build_projects.py` → `IMG_EXTS` (used when *generating* pages)
- `js/main.js` → `IMG_EXTS` (used when the browser fills in image
  slots at runtime for things that were only placeholders)

Why both? Because some image slots aren't known at build time — pages
that say "TRUSTLAKE / LANDING" in grey text are placeholders, and the
browser tries the extensions live and swaps in the real image if it
exists. If nothing exists, the tidy placeholder stays. (This is also
why a couple of 404s in the console are normal and harmless.)

After adding photos, run `python _build/optimize_images.py`. It makes
a `.webp` next to each original (originals are kept), skips anything
already converted, and keeps the original file when WebP wouldn't
actually be smaller.

## The JS: one file, lots of small guards

`js/main.js` runs on every page, so every feature checks "does this
element exist on this page?" before doing anything. Features include:
the typing effect, the system-stages accordion, the command palette
(Cmd/Ctrl+K), image probing, the contact form, and keyboard access for
clickable divs.

Three conventions to keep:

1. **Keyboard access for anything clickable that isn't a real button:**
   `role="button"`, `tabindex="0"`, and Enter/Space trigger a click.
   The `makeClickable()` helper does this — add new selectors there.
2. **Reduced motion:** anything that animates should check
   `prefers-reduced-motion` and fall back to something calm.
3. **No dependencies.** The only external scripts are Font Awesome,
   AOS, and Google Fonts. Keep it that way.

## The CSS: variables at the top, everything else below

`css/styles.css` starts with the palette — malachite green + copper,
stone neutrals, light and dark variants. Everything references the
variables, so a colour change is a one-line edit. There's a comment
marking the mineral palette if you're hunting for it.

Small screen sizes are handled inline per component (max-widths,
clamp for font sizes). Mobile is a first-class case, not an
afterthought.

## Where the senior-level work will plug in

This is the map for the work described in `plan.md`:

- **Flagship case study sections** → new fields in
  `_build/projects_data.py`, rendered by `case_study_fragment()` in
  `_build/build_projects.py`. The unused code-snippet card is already
  built — flipping it on is a data change, not a code change.
- **Homepage pipeline** → lives in the existing system-stages section
  (fragment `_build/fragments/home.html`), animated by a new block in
  `js/main.js`. Synthetic data and animation only; no libraries.
- **Core sample career scroll** → replaces the career timeline in
  `about.html` / `experience.html` fragments, styled in
  `styles.css`, small JS for the scroll behaviour.
- **Notes / How I work / Methodology** → new fragments + new entries
  in the `PAGES` list in `build.py`. Same pattern as every existing
  page — that's the whole point of the build system.
- **Print stylesheet** → a `@media print` block at the end of
  `styles.css`.
- **"Your visit, analyzed"** → a small self-contained block in
  `main.js` plus a footer slot added in `build.py`'s `footer_html`.
  No network calls, ever.

## Things that look like mistakes but aren't

- **Both PNG and WebP in `images/`.** On purpose: originals are the
  source of truth, WebP is what ships to browsers.
- **404s for TrustLake/Airbnb images.** Those projects have no photos
  yet; the placeholder probe checks a few extensions and gives up.
  Harmless noise.
- **`js/projects-data.js` in the repo.** It's generated, but keeping
  it means the site works without running Python first.
- **No git in this folder yet.** Before the big phases start, put this
  under version control — it's the cheapest safety net there is.
