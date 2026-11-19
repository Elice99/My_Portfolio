# Elisha Bassey Portfolio (static HTML/CSS/JS)

No framework, no build step to run the site. A Python build script keeps
shared chrome, all case-study pages, and now images/code snippets in
sync automatically.

## View it locally
```
python3 -m http.server 8080
```
Open http://localhost:8080

## Latest content pass: Zion Tech Hub finance challenge

Added a full case study for the failed-transactions analysis:

- `projects/zion-finance-data-challenge.html`
- `projects/zion-finance-data-challenge-business.html`
- `projects/zion-finance-data-challenge-technical.html`
- `_build/docs/zion_finance_data_challenge.py`

The technical page includes the inline architecture diagram. Six chart images
live in `images/ZionFinance_1.webp` through `ZionFinance_6.webp`. Content
source is `_build/projects_data.py`; generated HTML was rebuilt with
`python _build/build.py` and the images optimised with
`python _build/optimize_images.py`.

## Latest pass: quick wins (SEO, performance, accessibility)

### Site URL / canonical + social tags
`_build/build.py` now has a single `SITE_URL` constant at the top. It is
currently set to `https://elice99.github.io/Portfolio` (GitHub Pages).
Change that one line when the site moves (for example to a Netlify
domain), then rebuild. It drives the canonical link, `og:url`,
`og:image`, Twitter card tags and the `Person` JSON-LD. Set it to `""`
to omit those tags entirely.

### Image optimization (WebP)
All PNG/JPG images in `images/` now have a `.webp` copy. The build and
the browser image loader prefer WebP and fall back to the original
format. The WebP set is ~3.9 MB versus ~13.7 MB of originals (about 70%
smaller). Originals are kept.

Re-run after replacing a photo (keep the same filename):
```
python _build/optimize_images.py
```
The script skips files that already have a newer `.webp` and keeps the
original when WebP would not actually be smaller (some flat table
screenshots).

### Cache-busting for CSS/JS
Local stylesheet and script URLs get a `?v=<content-hash>` query at
build time, so returning visitors pick up a new `styles.css` or
`main.js` after a rebuild instead of a stale cached copy.

### Contact form
There is no form backend. Submitting the form now opens the visitor's
email app with the message prefilled, addressed to
`basseyelisha99@gmail.com`. A small note under the form explains this.
To use a real service later (Formspree, Netlify Forms), replace the
`mailto:` block in `js/main.js` with a `fetch()` POST.

### Visitor counter
Removed. The unconfigured GoatCounter badge and script are gone, so the
footer no longer shows a "— visits" placeholder. Add analytics back when
the site is deployed.

### Accessibility
- Every page wraps its content in `<main id="main-content">`.
- Homepage system-stage headings are `<h2>` (were `<h3>`), fixing the
  heading order.
- Clickable cards/stage headers are keyboard operable (Enter/Space,
  `role="button"`, `tabindex="0"`).
- Small secondary text (metric labels, footer, command-palette hint)
  uses a darker `--teal-600` / secondary colour for better contrast.
- Mobile nav transition now uses the defined `--transition-base` token.

### Name consistency
The hero name is "Elisha Bassey" everywhere (it previously said
"Bassey Elisha" in the homepage hero).

---

## Earlier changes

### 1. New color palette
Replaced the generic teal/violet SaaS gradient with a mineral-inspired
palette grounded in your geology background: malachite green + copper
as the two accents, basalt/stone neutrals instead of cool blue-grey,
hematite rust / azurite blue / moss green for the small category tags.
Light and dark mode use different accent shades (not simple inversions).
All defined as CSS variables in css/styles.css -- search for "mineral"
in the comments to find every spot that changed.

### 2. "Data -> Intelligence -> Decision" section rebuilt
Was a plain click-to-expand text list. Now it's a connected pipeline:
a vertical line with small colored pulses continuously flowing down it
(ambient motion, respects prefers-reduced-motion), each stage has a
large faint watermark icon, and expanding a stage reveals a staggered
constellation of real tool icons instead of a comma-separated list.

### 3. Real photos and project screenshots -- fully automatic
Drop files in /images/ using the naming convention in
**images/README.md** (e.g. `GlowMart_1.jpg`, `Elice_1.jpg`), rebuild,
done. No data file edits needed:
- Profile photos: Elice_1 (hero) and Elice_2 (About page) through
  Elice_5 are detected; 1 and 2 are wired in, ask if you want the
  others placed somewhere.
- Project photos: up to 5 per project (see the full prefix list in
  images/README.md). The first photo becomes that project's card
  thumbnail everywhere (homepage, /work.html, capability filter
  results); all of them appear as a scrollable gallery on its
  case-study page.
- Projects with no photos yet keep their current placeholder treatment
  exactly as before -- nothing breaks or looks unfinished in the
  meantime.

### 4. Floating code snippet component (built, currently unused)
You asked for real code to float as readable text over a screenshot
rather than appear as a picture of code -- that's a good instinct
(accessible, copy-pasteable, loads faster, matches the editorial feel
of the rest of the site) so it's fully built. It's off by default on
every project because I don't have your actual source code to show,
and didn't want to invent a plausible-looking fake snippet. To turn
it on for a project: in `_build/projects_data.py`, find that project's
`"codeSnippet": None` line and replace it with real code, e.g.:
```python
"codeSnippet": {
    "lang": "python",  # or "sql"
    "filename": "train_model.py",
    "code": "def train():\n    ...",
},
```
Rebuild, and it appears as a small VS-Code-style floating card
(with lightweight syntax highlighting) overlapping that project's
screenshot.



## Opening the site (fixed)
All links are now page-relative, so the site works when you double-click
index.html AND when hosted on Netlify or GitHub Pages. Photos and
screenshots are found by the browser at load time
(images/<Name>.webp|jpg|jpeg|png, WebP first), so adding an image never
needs Python. Python (`_build/build.py`) is only needed when you edit
project data or documentation content. Run
`python _build/optimize_images.py` first if you added new photos so a
WebP copy exists.

## Three-page project documentation (new)

A project can now have three pages: **Overview** (the short version),
**Business insights** (the question, evidence and advice, in plain
language) and **Technical documentation** (data model, formulas, cleaning
steps, why each visual was chosen). A tab bar links them, and the overview
page has two "Go deeper" cards. Projects without documentation show none
of this, so there are never dead links.

GlowMart is the first one, built from its GitHub README:
- projects/glowmart.html
- projects/glowmart-business.html
- projects/glowmart-technical.html

### To add documentation for another project
1. Copy `_build/docs/glowmart.py` to `_build/docs/<slug>.py` (dashes in
   the slug become underscores, e.g. `sales-pipeline-prediction` ->
   `sales_pipeline_prediction.py`).
2. Replace its content with that project's real material. Same shape,
   keep or drop sections as the project needs (an ML project would swap
   "Excel features" for model evaluation, for instance).
3. In `_build/projects_data.py`, add `"hasDocs": True,` to that project.
4. Rebuild: `cd _build && python3 build.py`.

Writing rules used in the GlowMart content (worth keeping): first person,
plain words, short sentences, only claims the source README supports.

### Image names for documentation figures
See images/README.md (bottom section) for the GlowMart names.

### Decision for you: Abuja and Kano
The GlowMart README says Abuja was the ONLY city to decline in 2024, but
its own city table also shows Kano at -2.9%. These pages follow the table.
If the table is the part that's wrong, edit `_build/docs/glowmart.py` and
the GlowMart `outcome` in `_build/projects_data.py`.

### Bugs fixed this round (found by testing every page at phone width)
- Footer links overflowed on every page on phones.
- Capabilities page overflowed on phones (the wide "Business" card).


### ER Patient Analysis (new, uses the same three-page structure)
- projects/er-patient-analysis.html, -business.html, -technical.html
- Content lives in `_build/docs/er_patient_analysis.py`. It uses the newer
  "sections" format, so a project's docs can have any structure (code blocks
  for DAX and Power Query M, tables, an inline diagram). GlowMart still uses
  the older fixed format and its pages are unchanged.
- The dataset is synthetic and every page says so.
- Open items for you, written into the pages as "to confirm":
  1. Satisfaction: the report shows 5.47 average and 75.10% not rated, a
     direct CSV count gave 4.99 and 72.7% blank. About 222 scores of 0
     would explain both. Count zeros in patient_sat_score to confirm.
  2. Referral: a CSV profile counted 5,400 blanks, the report shows a
     "None" category of 5,400. Check whether None is literal text.
  3. No GitHub link yet (add "github" in projects_data.py).

## To edit project content
Edit `_build/projects_data.py` (single source of truth), then:
```
cd _build
python3 build.py
```
This regenerates js/projects-data.js AND every page together, and
re-scans /images/ for any new photos.

## Known gaps
- Contact form has no backend: it opens a prefilled `mailto:` instead.
  Wire it to Formspree/Netlify Forms if you want in-page submission.
- Analytics is not wired up (the old unconfigured visitor counter was
  removed). Add GoatCounter or similar after deploying.
- `SITE_URL` points at `https://elice99.github.io/Portfolio`; change it
  in `_build/build.py` if you deploy to Netlify or a custom domain.
- 5 projects still need their findings verified before their warning
  banner comes off (see prior notes -- unchanged this round)
