import json
import os
from projects_data import PROJECTS
import build_docs as _docs

# WebP first: it is what the optimizer writes and what browsers should load.
# The other formats stay as fallbacks for images that have not been converted.
IMG_EXTS = ["webp", "jpg", "jpeg", "png"]


def detect_images(root, prefix, max_n=12):
    """Scan /images/ for files named {prefix}_1.jpg, {prefix}_2.png, etc
    (case-insensitive extension, any of the supported formats), in order.
    Returns web-relative paths like "/images/GlowMart_1.jpg". This is the
    whole mechanism behind "just name your files right and they show up" --
    no project data needs hand-editing to add real photos."""
    images_dir = os.path.join(root, "images")
    found = []
    for n in range(1, max_n + 1):
        for ext in IMG_EXTS:
            candidate = f"{prefix}_{n}.{ext}"
            if os.path.isfile(os.path.join(images_dir, candidate)):
                found.append(f"/images/{candidate}")
                break
    return found


def detect_profile_images(root, max_n=5):
    """Same mechanism for profile photos: Elice_1.jpg .. Elice_5.jpg."""
    return detect_images(root, "Elice", max_n)


def detect_video(root, prefix):
    """Scan /video/ for {prefix}.mp4, case-insensitive on the filename,
    returning the web path with the file's real casing. Same philosophy as
    detect_images: drop a correctly-named file in, rebuild, done."""
    video_dir = os.path.join(root, "video")
    if not os.path.isdir(video_dir):
        return None
    for entry in sorted(os.listdir(video_dir)):
        if entry.lower() == f"{prefix.lower()}.mp4":
            return f"/video/{entry}"
    return None


def with_detected_images(root):
    """Returns a deep-ish copy of PROJECTS with an `images` list merged in
    from whatever files actually exist in /images/ right now. This runs
    fresh on every build, so dropping in GlowMart_1.jpg and rebuilding is
    the entire workflow -- no project_data.py edits needed for photos."""
    out = []
    for p in PROJECTS:
        p = dict(p)
        p["images"] = detect_images(root, p["imagePrefix"])
        p["video"] = detect_video(root, p["imagePrefix"])
        out.append(p)
    return out


def write_js_data(root):
    """Generate js/projects-data.js from the Python source of truth."""
    data = with_detected_images(root)
    for item in data:
        item["images"] = [i.lstrip("/") for i in item["images"]]  # JS adds the page-relative prefix
    js_array = json.dumps(data, indent=2, ensure_ascii=False)
    content = f"""// GENERATED FILE \u2014 do not hand-edit.
// Source of truth is /_build/projects_data.py. Edit there, then re-run
// `python3 _build/build.py` to regenerate this file and the case-study
// pages together, so they never drift apart.
//
// Add a new project by adding an object to PROJECTS in projects_data.py.

const PROJECTS = {js_array};

function getFeaturedProject() {{
  return PROJECTS.find((p) => p.featured);
}}
function getSecondaryProjects() {{
  return PROJECTS.filter((p) => !p.featured);
}}
function getVerifiedProjects() {{
  return PROJECTS.filter((p) => p.verified);
}}

// Shared card renderer used by index.html, work.html, and the capabilities
// filter results, so the GitHub icon / metric badge markup can't drift
// between the three places project cards get rendered.
function projectCardHTML(p, opts) {{
  opts = opts || {{}};
  var badge = p.verified
    ? '<div class="project-metric-badge"><span class="stat-value">' + p.metricValue + '</span><span class="stat-label">' + p.metricLabel + '</span></div>'
    : '';
  var ROOT = window.SITE_ROOT || '';
  var githubLink = p.github
    ? '<a href="' + p.github + '" target="_blank" rel="noopener" class="project-github-link" aria-label="View ' + p.title + ' on GitHub" onclick="event.stopPropagation()"><i class="fab fa-github"></i></a>'
    : '';
  var statusPill = (opts.showStatus && p.status)
    ? '<span class="project-badge" style="background:var(--bg-tertiary);color:var(--text-secondary);box-shadow:none">' + p.status + '</span>'
    : '';
  // Real screenshot as thumbnail once one exists; otherwise the original
  // icon placeholder. Nothing else about the card needs to change when
  // Elice adds photos later -- it upgrades itself on the next rebuild.
  var hasImage = p.images && p.images.length > 0;
  var visualContent = hasImage
    ? '<img src="' + ROOT + p.images[0] + '" alt="' + p.title + ' screenshot" loading="lazy" decoding="async">'
    : '<i class="fas fa-chart-line project-icon" data-img-swap="' + p.imagePrefix + '_1" data-img-alt="' + p.title + ' screenshot"></i>';
  return (
    '<div class="project-card' + (opts.extraClass ? ' ' + opts.extraClass : '') + '"' +
        (opts.dataCategory ? ' data-category="' + opts.dataCategory + '"' : '') + ' data-aos="' + (opts.aos || 'fade-up') + '">' +
      badge + githubLink +
      '<a href="' + ROOT + 'projects/' + p.slug + '.html" class="project-card-link" aria-label="View ' + p.title + ' case study"></a>' +
      '<div class="project-visual' + (hasImage ? ' has-image' : '') + '">' + visualContent + statusPill + '</div>' +
      '<div class="project-info">' +
        '<h3 class="project-title">' + p.title + '</h3>' +
        '<p class="project-description">' + p.tagline + '</p>' +
        '<div class="project-tech">' + (p.stack.length ? p.stack.map(function (s) {{ return '<span>' + s + '</span>'; }}).join('') : '<span>In progress</span>') + '</div>' +
      '</div>' +
    '</div>'
  );
}}
"""
    out_path = os.path.join(root, "js", "projects-data.js")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", out_path)


def media_block(project):
    """Return the creative media HTML for a project's case-study page,
    chosen by its `media` field. Each treatment accepts an <img> or
    <video> in the same slot — swapping a screenshot for a short clip
    later is a one-line change, not a redesign."""
    m = project["media"]
    placeholder = lambda label: (
        f'<div style="display:flex;align-items:center;justify-content:center;'
        f'height:100%;min-height:220px;color:var(--text-tertiary);'
        f'font-family:\'JetBrains Mono\',monospace;font-size:0.8125rem">{label}</div>'
    )
    title_upper = project["title"].upper()

    if m == "layered":
        return f'''<div class="media-frame media-layered">
            <div class="media-frame-inner primary">{placeholder(title_upper + " / 01")}</div>
            <div class="media-frame-inner secondary">{placeholder(title_upper + " / 02")}</div>
        </div>'''
    if m == "diagonal":
        return f'''<div class="media-frame">
            <div class="media-frame-inner media-diagonal">{placeholder(title_upper)}</div>
            <div class="media-diagonal-accent"></div>
        </div>'''
    if m == "split":
        return f'''<div class="media-split">
            <figure>
                <div class="media-frame-inner" style="aspect-ratio:4/3">{placeholder("BEFORE")}</div>
                <figcaption>PERCEIVED: SUPPLY CONFLICT</figcaption>
            </figure>
            <figure>
                <div class="media-frame-inner" style="aspect-ratio:4/3;border-color:var(--teal-500)">{placeholder("AFTER")}</div>
                <figcaption>ACTUAL: 0.3% VARIANCE</figcaption>
            </figure>
        </div>'''
    # default: "browser" — device-chrome frame, good for dashboard/app screenshots
    return f'''<div class="media-browser">
        <div class="media-browser-bar"><span class="media-browser-dot"></span><span class="media-browser-dot"></span><span class="media-browser-dot"></span></div>
        <div class="media-frame-inner" style="aspect-ratio:16/10;border:none;border-radius:0">{placeholder(title_upper)}</div>
    </div>'''


import html as _html
import re as _re

_PY_KEYWORDS = r"\b(def|return|import|from|if|else|elif|for|while|class|try|except|with|as|in|is|not|and|or|None|True|False|self|lambda|yield|raise)\b"
_SQL_KEYWORDS = r"\b(SELECT|FROM|WHERE|JOIN|LEFT|RIGHT|INNER|ON|GROUP BY|ORDER BY|AS|WITH|CASE|WHEN|THEN|END|AND|OR|NOT|IN|NULL|INSERT|INTO|VALUES|UPDATE|SET|CREATE|TABLE)\b"


def highlight_code(code, lang):
    """Minimal, dependency-free syntax highlighting for the floating code
    card -- good enough for a short real snippet, not a full tokenizer.
    Escapes HTML first so the snippet is always safe to inline."""
    escaped = _html.escape(code)
    # Order matters: strings/comments first so keyword regex doesn't touch
    # text inside them.
    escaped = _re.sub(r"(#.*?)(\n|$)", r'<span class="tok-com">\1</span>\2', escaped)
    escaped = _re.sub(r"(&quot;.*?&quot;|&#x27;.*?&#x27;)", r'<span class="tok-str">\1</span>', escaped)
    kw_pattern = _PY_KEYWORDS if lang == "python" else _SQL_KEYWORDS
    flags = 0 if lang == "python" else _re.IGNORECASE
    escaped = _re.sub(kw_pattern, r'<span class="tok-kw">\g<0></span>', escaped, flags=flags)
    escaped = _re.sub(r"\b(\d+\.?\d*)\b", r'<span class="tok-num">\1</span>', escaped)
    return escaped


def code_float_html(snippet):
    """snippet = {"lang": "python", "filename": "train_model.py", "code": "..."}
    Returns '' if no snippet is set -- this component only ever shows
    real code Elice actually wrote, never a fabricated example."""
    if not snippet:
        return ""
    lang = snippet.get("lang", "python")
    if lang in ("dax", "m"):
        highlighted = _docs.highlight(snippet["code"], lang)  # DAX and Power Query M
    else:
        highlighted = highlight_code(snippet["code"], lang)  # python and sql
    return f'''<div class="code-float">
        <div class="code-float-bar">
            <span class="code-float-dot"></span><span class="code-float-dot"></span><span class="code-float-dot"></span>
            <span style="margin-left:6px;font-family:'JetBrains Mono',monospace;font-size:0.6875rem;color:#8a8a8a">{snippet.get("filename", "")}</span>
        </div>
        <pre>{highlighted}</pre>
    </div>'''


def media_or_gallery(project):
    """Real screenshots win once they exist; otherwise the placeholder
    treatment for this project's configured style. Works the same
    whether Elice drops in 1 image or 5 -- no per-count layout decisions."""
    images = project.get("images") or []
    out = ""
    if not images:
        out = media_block(project)
    else:
        frames = "".join(
            f'<div class="media-gallery-frame{" single" if len(images) == 1 else ""}">'
            f'<img src="{src}" alt="{project["title"]} screenshot {i+1}" loading="lazy" decoding="async"></div>'
            for i, src in enumerate(images)
        )
        count_label = (
            f'<p class="media-gallery-count">{len(images)} SCREENSHOTS, SCROLL TO SEE MORE &rarr;</p>'
            if len(images) > 1 else ""
        )
        out = f'<div class="media-gallery">{frames}</div>{count_label}'
    video = project.get("video")
    if video:
        out += (
            f'<div class="media-video">'
            f'<video controls preload="metadata" src="{video}"></video>'
            f'<p class="media-gallery-count">PRODUCT WALKTHROUGH &middot; PRESS PLAY</p>'
            f'</div>'
        )
    return out


def case_study_fragment(project, next_project):
    notice = ""
    if not project["verified"]:
        notice = (
            '<div class="case-placeholder-notice">'
            '<i class="fas fa-triangle-exclamation"></i>&nbsp; This case study has placeholder content. '
            'Edit it in <code>_build/projects_data.py</code>, set <code>verified: True</code>, then re-run the build script.'
            '</div>'
        )
    stack_line = " &middot; ".join(project["stack"]) if project["stack"] else "STACK TBD"

    links_html = ""
    if project.get("github") or project.get("demo"):
        buttons = []
        if project.get("github"):
            buttons.append(
                f'<a href="{project["github"]}" target="_blank" rel="noopener" class="btn btn-secondary">'
                f'<i class="fab fa-github"></i> View on GitHub</a>'
            )
        if project.get("demo"):
            buttons.append(
                f'<a href="{project["demo"]}" target="_blank" rel="noopener" class="btn btn-primary">'
                f'<i class="fas fa-arrow-up-right-from-square"></i> Live Demo</a>'
            )
        links_html = f'<div class="case-links">{"".join(buttons)}</div>'

    # Documentation tabs + entry cards only appear for projects that actually
    # have documentation pages -- never a dead link.
    # No image at build time? Mark the media area so the browser can find GlowMart_1.jpg etc. itself.
    gallery_attr = "" if project.get("images") else f' data-gallery="{project["imagePrefix"]}"'
    docs_tabs = ""
    docs_cards = ""
    if project.get("hasDocs"):
        docs_tabs = _docs.tabs(project, "overview")
        docs_cards = (
            '<p class="doc-bottom-label" style="margin-top:var(--space-8)">Go deeper</p>'
            + _docs.go_deeper(project, ("business", "technical"))
        )

    # Flagship-only story sections. Each renders only when the field has
    # real content, so a project never ships a half-written section.
    stakes_html = ""
    if project.get("stakes"):
        stakes_html = f'''<section class="case-section case-stakes" data-aos="fade-up">
            <h2>THE STAKES</h2>
            <p>{project["stakes"]}</p>
        </section>'''

    decisions_html = ""
    if project.get("decisions"):
        items = "".join(
            f'<div class="case-decision"><p class="case-decision-title">{d["title"]}</p>'
            f'<p>{d["text"]}</p></div>'
            for d in project["decisions"]
        )
        decisions_html = f'''<section class="case-section" data-aos="fade-up">
            <h2>THE HARD PART</h2>{items}</section>'''

    failure_html = ""
    if project.get("failure"):
        failure_html = f'''<section class="case-section case-failure" data-aos="fade-up">
            <h2>WHAT FAILED</h2>
            <p>{project["failure"]}</p>
        </section>'''

    differently_html = ""
    if project.get("differently"):
        differently_html = f'''<section class="case-section" data-aos="fade-up">
            <h2>WHAT I'D DO DIFFERENTLY</h2>
            <p>{project["differently"]}</p>
        </section>'''

    return f"""    <section class="case-hero" style="padding-left:0;padding-right:0">
        <div class="container">
            <span class="case-status">{project['status'].upper()}</span>
            <h1 class="case-title">{project['title'].upper()}</h1>
            <p class="case-tagline">{project['tagline']}</p>
            <p class="case-stack">{stack_line}</p>
            {links_html}
        </div>
    </section>

    <div class="container">
        {docs_tabs}
        <div class="media-frame code-float-wrap" data-aos="fade-up"{gallery_attr}>{media_or_gallery(project)}{code_float_html(project.get("codeSnippet"))}</div>

        <div class="case-metric-strip">
            <span class="case-metric-value">{project['metricValue']}</span>
            <span class="case-metric-label">{project['metricLabel']}</span>
        </div>

        {notice}
        {docs_cards}

        {stakes_html}
        <section class="case-section" data-aos="fade-up">
            <h2>THE PROBLEM</h2>
            <p>{project['problem']}</p>
        </section>
        <section class="case-section" data-aos="fade-up">
            <h2>APPROACH</h2>
            <p>{project['approach']}</p>
        </section>
        <section class="case-section" data-aos="fade-up">
            <h2>OUTCOME</h2>
            <p>{project['outcome']}</p>
        </section>

        {decisions_html}
        {failure_html}
        {differently_html}

        <div class="case-next">
            <p class="case-next-label">NEXT CASE STUDY</p>
            <a href="/projects/{next_project['slug']}.html">{next_project['title']} &rarr;</a>
        </div>
    </div>
"""


def build_all(assemble_fn, root):
    projects_dir = os.path.join(root, "projects")
    os.makedirs(projects_dir, exist_ok=True)
    write_js_data(root)

    projects_with_images = with_detected_images(root)
    depth_prefix = "../"
    for i, project in enumerate(projects_with_images):
        next_project = projects_with_images[(i + 1) % len(projects_with_images)]
        content = case_study_fragment(project, next_project)

        # Reuse the same head/nav/footer assembly as every other page —
        # write content to a temp fragment path assemble_fn can read.
        tmp_fragment_name = f"_project_{project['slug']}.html"
        tmp_path = os.path.join(os.path.dirname(__file__), "fragments", tmp_fragment_name)
        with open(tmp_path, "w", encoding="utf-8") as f:
            f.write(content)

        title = f"{project['title']} | Elisha Bassey"
        html = assemble_fn(tmp_fragment_name, title, project["tagline"], "", depth_prefix,
                           f"/projects/{project['slug']}.html")
        out_path = os.path.join(projects_dir, f"{project['slug']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", out_path)
        os.remove(tmp_path)

        # Documentation pages (business insights + technical), if this project has them
        if project.get("hasDocs"):
            mod = _docs.load_docs(os.path.dirname(os.path.abspath(__file__)), project["slug"])
            if mod is None:
                print("WARNING:", project["slug"], "has hasDocs=True but no _build/docs file; skipped")
            else:
                for kind, render, content in (
                    ("business", _docs.render_business, mod.BUSINESS),
                    ("technical", _docs.render_technical, mod.TECHNICAL),
                ):
                    frag_name = f"_doc_{project['slug']}_{kind}.html"
                    frag_path = os.path.join(os.path.dirname(__file__), "fragments", frag_name)
                    with open(frag_path, "w", encoding="utf-8") as f:
                        f.write(render(project, content, root))
                    label = "Business insights" if kind == "business" else "Technical documentation"
                    doc_html = assemble_fn(frag_name, f"{project['title']}: {label} | Elisha Bassey",
                                           content["lede"], "", depth_prefix,
                                           f"/projects/{project['slug']}-{kind}.html")
                    doc_out = os.path.join(projects_dir, f"{project['slug']}-{kind}.html")
                    with open(doc_out, "w", encoding="utf-8") as f:
                        f.write(doc_html)
                    print("wrote", doc_out)
                    os.remove(frag_path)
