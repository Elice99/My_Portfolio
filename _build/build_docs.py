"""
Renders the two documentation pages (business insights + technical) for any
project that has hasDocs: True and a content file at _build/docs/<slug>.py
(slug dashes become underscores, e.g. sales-pipeline-prediction ->
sales_pipeline_prediction.py). The content file exposes BUSINESS and
TECHNICAL dicts; see docs/glowmart.py for the full shape.

Everything is escaped on the way out, so content files can use plain text.
"""
import html
import importlib.util
import os

IMG_EXTS = ["webp", "jpg", "jpeg", "png"]


def esc(s):
    return html.escape(str(s), quote=True)


def load_docs(build_dir, slug):
    path = os.path.join(build_dir, "docs", slug.replace("-", "_") + ".py")
    if not os.path.isfile(path):
        return None
    spec = importlib.util.spec_from_file_location("docs_" + slug.replace("-", "_"), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def find_image(root, basename):
    for ext in IMG_EXTS:
        if os.path.isfile(os.path.join(root, "images", f"{basename}.{ext}")):
            return f"/images/{basename}.{ext}"
    return None


def figure(root, spec):
    """spec = (image basename, caption). Real image if the file exists,
    otherwise a quiet placeholder that names the file to add."""
    name, caption = spec
    src = find_image(root, name)
    if src:
        inner = f'<img src="{esc(src)}" alt="{esc(caption)}" loading="lazy">'
    else:
        inner = (f'<div class="doc-figure-empty" data-img-swap="{esc(name)}" '
                 f'data-img-alt="{esc(caption)}">{esc(name)}.png</div>')
    return f'<figure class="doc-figure">{inner}<figcaption>{esc(caption)}</figcaption></figure>'


def table(t):
    head = "".join(f"<th>{esc(h)}</th>" for h in t["headers"])
    rows = "".join(
        "<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in t["rows"]
    )
    return f'<div class="doc-table-wrap"><table class="doc-table"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>'


def tabs(project, active):
    slug = project["slug"]
    items = [
        ("overview", "Overview", f"/projects/{slug}.html"),
        ("business", "Business insights", f"/projects/{slug}-business.html"),
        ("technical", "Technical documentation", f"/projects/{slug}-technical.html"),
    ]
    links = ""
    for key, label, href in items:
        is_active = key == active
        cls = "doc-tab active" if is_active else "doc-tab"
        current = ' aria-current="page"' if is_active else ""
        links += f'<a href="{href}" class="{cls}"{current}>{label}</a>'

    return f'<nav class="doc-tabs" aria-label="{esc(project["title"])} sections">{links}</nav>'


def go_deeper(project, show=("business", "technical")):
    slug = project["slug"]
    cards = {
        "business": (
            "fa-chart-pie", "Business insights",
            "The question, the evidence and what I would do about it, in plain language.",
            f"/projects/{slug}-business.html"),
        "technical": (
            "fa-gears", "Technical documentation",
            "The data model, formulas and measures, cleaning steps, and why I chose each visual.",
            f"/projects/{slug}-technical.html"),
        "overview": (
            "fa-table-columns", "Project overview",
            "The short version: problem, approach and outcome.",
            f"/projects/{slug}.html"),
    }
    out = ""
    for key in show:
        icon, title, text, href = cards[key]
        out += (
            f'<a href="{href}" class="go-deeper-card"><i class="fas {icon}"></i>'
            f'<div><h3>{title}</h3><p>{text}</p></div><span class="go-deeper-arrow">&rarr;</span></a>'
        )
    return f'<div class="go-deeper">{out}</div>'


def shell(project, kind_label, title, lede, active, toc_items, body_html, bottom_html):
    toc = "".join(f'<a href="#{i}">{esc(label)}</a>' for i, label in toc_items)
    return f"""    <section class="case-hero" style="padding-left:0;padding-right:0;padding-bottom:var(--space-6)">
        <div class="container">
            <a href="/projects/{project['slug']}.html" class="doc-back">&larr; {esc(project['title'])} overview</a>
            <span class="case-status">{kind_label}</span>
            <h1 class="case-title doc-title">{esc(title)}</h1>
            <p class="case-tagline">{esc(lede)}</p>
        </div>
    </section>

    <div class="container">
        {tabs(project, active)}
        <div class="doc-shell">
            <aside class="doc-toc" aria-label="On this page"><p>On this page</p>{toc}</aside>
            <article class="doc-body">
{body_html}
            </article>
        </div>
        <div class="doc-bottom">{bottom_html}</div>
    </div>
"""


def section(sid, heading, inner):
    return f'<section class="doc-section" id="{sid}"><h2>{esc(heading)}</h2>{inner}</section>'


def paras(items):
    return "".join(f"<p>{esc(p)}</p>" for p in items)


def github_btn(project):
    if not project.get("github"):
        return ""
    return (f'<a href="{esc(project["github"])}" target="_blank" rel="noopener" class="btn btn-secondary">'
            f'<i class="fab fa-github"></i> View on GitHub</a>')



# ------------------------------------------------------------ code + blocks
import re as _re

_DAX_KW = r"VAR|RETURN"
_M_KW = r"let|in|each|type|if|then|else|null|true|false"


def highlight(code, lang):
    """Single-pass tokenizer (comments, strings, numbers, keywords, function
    calls). Works on the RAW text and escapes each piece itself, so nested
    or mangled spans can't happen. Supports dax, m, python, sql."""
    lang = (lang or "").lower()
    kw = {"dax": _DAX_KW, "m": _M_KW,
          "python": r"def|return|import|from|if|else|elif|for|while|class|in|is|not|and|or|None|True|False|with|as",
          "sql": r"SELECT|FROM|WHERE|JOIN|ON|GROUP BY|ORDER BY|AS|WITH|AND|OR|NOT|IN|NULL"}.get(lang, "")
    comment = r"//[^\n]*|--[^\n]*" if lang in ("dax", "m", "sql") else r"#[^\n]*"
    parts = [
        ("com", comment),
        ("str", r'"(?:[^"\\]|\\.)*"' if lang != "m" else r'"[^"\n]*"'),
        ("num", r"\b\d+(?:\.\d+)?\b"),
    ]
    if kw:
        parts.append(("kw", r"\b(?:" + kw + r")\b"))
    parts.append(("fn", r"[A-Za-z_][A-Za-z0-9_.]*(?=\()"))
    pattern = _re.compile("|".join(f"(?P<{n}>{rx})" for n, rx in parts),
                          _re.IGNORECASE if lang in ("dax", "sql") else 0)
    out, last = [], 0
    for m in pattern.finditer(code):
        out.append(esc(code[last:m.start()]))
        out.append(f'<span class="tok-{m.lastgroup}">{esc(m.group())}</span>')
        last = m.end()
    out.append(esc(code[last:]))
    return "".join(out)


def code_block(title, lang, code):
    label = {"dax": "DAX", "m": "Power Query M"}.get(lang, lang.upper())
    cleaned = code.strip("\n")  # computed outside the f-string: no backslashes inside {} (needs Python 3.12+ otherwise)
    return (f'<div class="doc-code"><div class="doc-code-bar"><span>{esc(title)}</span>'
            f'<span class="doc-code-lang">{esc(label)}</span></div>'
            f'<pre><code>{highlight(cleaned, lang)}</code></pre></div>')


def finding_html(n, f, root):
    inner = f'<p class="doc-question">{esc(f["question"])}</p>'
    if f.get("paragraphs"):
        inner += paras(f["paragraphs"])
    if f.get("table"):
        inner += table(f["table"])
    inner += f'<p><strong>What it means.</strong> {esc(f["meaning"])}</p>'
    inner += f'<div class="doc-conclusion"><span>Conclusion</span><p>{esc(f["conclusion"])}</p></div>'
    if f.get("figure"):
        inner += figure(root, f["figure"])
    return (f'<div class="doc-finding" id="{f["id"]}"><div class="doc-finding-head">'
            f'<span class="doc-num">{n:02d}</span><h3>{esc(f["title"])}</h3></div>{inner}</div>')


def rec_html(n, r):
    chip = f'<span class="doc-chip doc-chip-priority">{esc(r["priority"])} priority</span>' if r.get("priority") else ""
    return (
        f'<div class="doc-rec"><div class="doc-finding-head"><span class="doc-num">{n:02d}</span>'
        f'<h3>{esc(r["title"])}</h3>{chip}</div>'
        f'<dl><dt>Evidence</dt><dd>{esc(r["evidence"])}</dd>'
        f'<dt>What to do</dt><dd>{esc(r["action"])}</dd>'
        f'<dt>What I expect</dt><dd>{esc(r["impact"])}</dd></dl></div>')


def render_blocks(root, blocks):
    """Generic block engine used by any docs file that defines `sections`."""
    out = ""
    for b in blocks:
        t = b["type"]
        if t == "p":
            out += paras(b["items"] if "items" in b else [b["text"]])
        elif t == "note":
            out += f'<div class="doc-note"><i class="fas fa-circle-info"></i><p>{esc(b["text"])}</p></div>'
        elif t == "verdict":
            out += f'<div class="doc-verdict"><p>{esc(b["text"])}</p></div>'
        elif t == "stat_grid":
            out += '<div class="doc-stat-grid">' + "".join(
                f'<div class="doc-stat"><span class="doc-stat-value">{esc(v)}</span>'
                f'<span class="doc-stat-label">{esc(l)}</span></div>' for v, l in b["items"]) + "</div>"
        elif t == "table":
            out += table(b)
        elif t == "steps":
            out += '<ol class="doc-steps">' + "".join(
                f'<li><strong>{esc(a)}</strong><span>{esc(c)}</span></li>' for a, c in b["items"]) + "</ol>"
        elif t == "pairs":
            out += '<div class="doc-pairs">' + "".join(
                f'<div><h3>{esc(a)}</h3><p>{esc(c)}</p></div>' for a, c in b["items"]) + "</div>"
        elif t == "figure":
            out += figure(root, b["spec"])
        elif t == "svg":
            cap = f'<figcaption>{esc(b["caption"])}</figcaption>' if b.get("caption") else ""
            out += f'<figure class="doc-diagram">{b["svg"]}{cap}</figure>'
        elif t == "code":
            out += code_block(b["title"], b["lang"], b["code"])
            if b.get("caption"):
                out += f'<p class="doc-code-caption">{esc(b["caption"])}</p>'
        elif t == "sub":
            out += f'<h3 class="doc-sub">{esc(b["text"])}</h3>'
        elif t == "findings":
            out += "".join(finding_html(n, f, root) for n, f in enumerate(b["items"], 1))
        elif t == "recs":
            out += "".join(rec_html(n, r) for n, r in enumerate(b["items"], 1))
        elif t == "code_cards":
            for it in b["items"]:
                inner = "".join(f"<p>{esc(x)}</p>" for x in it.get("text", []))
                note = (f'<p class="doc-review"><strong>Review note.</strong> {esc(it["note"])}</p>'
                        if it.get("note") else "")
                out += (f'<div class="doc-kpi doc-codecard"><div class="doc-kpi-top"><h3>{esc(it["name"])}</h3>'
                        f'<span class="doc-chip">{esc(it.get("kind", ""))}</span></div>'
                        f'{inner}{code_block(it["name"], it["lang"], it["code"])}{note}</div>')
        else:
            raise ValueError("unknown block type: " + t)
    return out


def render_sections(project, c, root, kind_label, active, bottom_html):
    secs = c["sections"]
    toc = [(s_["id"], s_["heading"]) for s_ in secs]
    body = "".join(section(s_["id"], s_["heading"], render_blocks(root, s_["blocks"])) for s_ in secs)
    return shell(project, kind_label, c["title"], c["lede"], active, toc, body, bottom_html)


# ---------------------------------------------------------------- business
def render_business(project, c, root):
    if "sections" in c:
        bottom = ("<p class=\"doc-bottom-label\">Want to see how it was built?</p>"
                  + go_deeper(project, ("technical", "overview"))
                  + f"<div class=\"case-links\">{github_btn(project)}</div>")
        return render_sections(project, c, root, "BUSINESS INSIGHTS", "business", bottom)
    toc = [("scenario", "The disagreement"), ("answer", "The short answer"),
           ("numbers", "Numbers at a glance"), ("findings", "What I found"),
           ("recommendations", "What I would do"), ("limits", "What this can't tell you")]

    body = ""
    if c.get("note"):
        body += f'<div class="doc-note"><i class="fas fa-circle-info"></i><p>{esc(c["note"])}</p></div>'

    body += section("scenario", c["scenario"]["heading"], paras(c["scenario"]["paragraphs"]))

    v = c["verdict"]
    body += section("answer", v["label"],
                    f'<div class="doc-verdict"><p>{esc(v["text"])}</p></div>')

    kpis = "".join(
        f'<div class="doc-stat"><span class="doc-stat-value">{esc(val)}</span>'
        f'<span class="doc-stat-label">{esc(label)}</span></div>' for val, label in c["kpis"])
    body += section("numbers", "Numbers at a glance", f'<div class="doc-stat-grid">{kpis}</div>')

    findings = "".join(finding_html(n, f, root) for n, f in enumerate(c["findings"], 1))
    body += section("findings", "What I found", findings)

    recs = "".join(rec_html(n, r) for n, r in enumerate(c["recommendations"], 1))
    body += section("recommendations", "What I would do", recs)

    body += section("limits", "What this can't tell you", paras(c["limits"]))

    bottom = (
        '<p class="doc-bottom-label">Want to see how it was built?</p>'
        + go_deeper(project, ("technical", "overview"))
        + f'<div class="case-links">{github_btn(project)}</div>')
    return shell(project, "BUSINESS INSIGHTS", c["title"], c["lede"], "business", toc, body, bottom)


# --------------------------------------------------------------- technical
def render_technical(project, c, root):
    if "sections" in c:
        bottom = ("<p class=\"doc-bottom-label\">Want the business side?</p>"
                  + go_deeper(project, ("business", "overview"))
                  + f"<div class=\"case-links\">{github_btn(project)}</div>")
        return render_sections(project, c, root, "TECHNICAL DOCUMENTATION", "technical", bottom)
    toc = [("stack", "The workflow"), ("dataset", "The data"), ("model", "Data model"),
           ("prep", "Data preparation"), ("approach", "Analytical approach"),
           ("kpis", "KPIs and formulas"), ("visuals", "Visual choices"),
           ("pages", "Dashboard layout"), ("features", "Excel features used"),
           ("principles", "Design principles"), ("reflection", "Challenges and lessons"),
           ("next", "If I took it further")]

    body = ""
    s = c["stack"]
    flow = "".join(
        f'<div class="doc-flow-step"><strong>{esc(a)}</strong><span>{esc(b)}</span></div>'
        + ('<span class="doc-flow-arrow">&rarr;</span>' if i < len(s["flow"]) - 1 else "")
        for i, (a, b) in enumerate(s["flow"]))
    body += section("stack", "The workflow", f'<p>{esc(s["intro"])}</p><div class="doc-flow">{flow}</div>')

    body += section("dataset", "The data", table(c["dataset"]))

    m = c["model"]
    tabs_html = ""
    for t in m["tables"]:
        tabs_html += (
            f'<div class="doc-model-table"><h3>{esc(t["name"])}</h3><p>{esc(t["purpose"])}</p>'
            f'<p class="doc-fields"><span>Columns</span> {esc(t["fields"])}</p>'
            f'{figure(root, t["figure"])}</div>')
    body += section("model", "Data model",
                    f'<p>{esc(m["intro"])}</p>{figure(root, m["figure"])}{tabs_html}')

    def steps(items):
        return '<ol class="doc-steps">' + "".join(
            f'<li><strong>{esc(a)}</strong><span>{esc(b)}</span></li>' for a, b in items) + "</ol>"

    body += section("prep", "Data preparation", f'<p>{esc(c["prep"]["intro"])}</p>{steps(c["prep"]["steps"])}')
    body += section("approach", "Analytical approach",
                    f'<p>{esc(c["approach"]["intro"])}</p>{steps(c["approach"]["steps"])}')

    k = c["kpis"]
    cards = ""
    for it in k["items"]:
        cards += (
            f'<div class="doc-kpi"><div class="doc-kpi-top"><h3>{esc(it["name"])}</h3>'
            f'<span class="doc-kpi-result">{esc(it["result"])}</span></div>'
            f'<code>{esc(it["formula"])}</code><p>{esc(it["why"])}</p></div>')
    body += section("kpis", "KPIs and formulas", f'<p>{esc(k["intro"])}</p><div class="doc-kpi-grid">{cards}</div>')

    vz = c["visuals"]
    vcards = ""
    for n, it in enumerate(vz["items"], 1):
        extra = (f'<p><strong>Why not:</strong> {esc(it["not_chosen"])}</p>' if it.get("not_chosen") else "")
        vcards += (
            f'<div class="doc-visual"><div class="doc-finding-head"><span class="doc-num">{n:02d}</span>'
            f'<h3>{esc(it["name"])}</h3></div><span class="doc-chip">{esc(it["type"])}</span>'
            f'<p><strong>Question:</strong> {esc(it["question"])}</p>'
            f'<p><strong>Why this choice:</strong> {esc(it["why"])}</p>{extra}'
            f'<p><strong>What it showed:</strong> {esc(it["insight"])}</p></div>')
    body += section("visuals", "Visual choices", f'<p>{esc(vz["intro"])}</p>{vcards}')

    body += section("pages", "Dashboard layout", f'<p>{esc(c["pages"]["intro"])}</p>{table(c["pages"])}')
    body += section("features", "Excel features used", table(c["features"]))

    pairs = lambda items: '<div class="doc-pairs">' + "".join(
        f'<div><h3>{esc(a)}</h3><p>{esc(b)}</p></div>' for a, b in items) + "</div>"
    body += section("principles", "Design principles", pairs(c["principles"]))
    body += section("reflection", "Challenges and lessons",
                    "<h3 class=\"doc-sub\">Challenges</h3>" + pairs(c["challenges"])
                    + "<h3 class=\"doc-sub\">Lessons</h3>" + pairs(c["lessons"]))
    body += section("next", "If I took it further", f'<p>{esc(" ".join(c["next"]))}</p>')

    bottom = (
        '<p class="doc-bottom-label">Want the business side?</p>'
        + go_deeper(project, ("business", "overview"))
        + f'<div class="case-links">{github_btn(project)}</div>')
    return shell(project, "TECHNICAL DOCUMENTATION", c["title"], c["lede"], "technical", toc, body, bottom)
