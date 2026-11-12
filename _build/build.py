#!/usr/bin/env python3
"""
Dev-time assembly script. Takes shared chrome (nav, footer, command
palette) + per-page content fragments and writes final, plain static
HTML files. Nothing here ships — the output in /portfolio/*.html and
/portfolio/projects/*.html is what gets deployed, and it needs no
build step, templating engine, or server to run.

Run: python3 build.py
"""
import hashlib
import json
import os
import re

# Public base URL used for canonical links, og:url and og:image.
# Change this one line when the site moves (e.g. a Netlify domain), then
# rebuild. No trailing slash. Leave it as "" to omit canonical/social tags.
SITE_URL = "https://elishabassey.netlify.app"

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRAGMENTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fragments")

NAV_LINKS = [
    ("/work.html", "Work"),
    ("/about.html", "About"),
    ("/experience.html", "Experience"),
    ("/capabilities.html", "Capabilities"),
    ("/now.html", "Now"),
]


def read(name):
    with open(os.path.join(FRAGMENTS, name), encoding="utf-8") as f:
        return f.read()


def nav_html(current_path, depth_prefix):
    links = []
    for href, label in NAV_LINKS:
        full_href = depth_prefix + href.lstrip("/")
        current = ' aria-current="page"' if href == current_path else ""
        links.append(f'<li><a href="{full_href}" class="nav-link"{current}>{label}</a></li>')
    cv_current = ' aria-current="page"' if current_path == "/resume.html" else ""
    contact_current = ' aria-current="page"' if current_path == "/contact.html" else ""
    return f"""    <nav class="navbar" id="navbar">
        <div class="nav-container">
            <a href="{depth_prefix}index.html" class="nav-logo">
                <span class="logo-bracket">&lt;</span>
                <span class="logo-text">EB</span>
                <span class="logo-bracket">/&gt;</span>
            </a>
            <ul class="nav-menu" id="navMenu">
                {''.join(links)}
            </ul>
            <div class="nav-controls">
                <button class="theme-toggle" id="themeToggle" aria-label="Toggle Dark Mode"><i class="fas fa-moon"></i></button>
                <a href="{depth_prefix}resume.html" class="nav-link" style="margin-right:0.5rem"{cv_current}>CV</a>
                <a href="{depth_prefix}contact.html" class="nav-link" style="margin-right:0.5rem"{contact_current}>Contact</a>
                <button class="theme-toggle" data-cmdk-trigger aria-label="Open command palette (Cmd/Ctrl+K)"><i class="fas fa-magnifying-glass"></i></button>
                <button class="mobile-toggle" id="mobileToggle" aria-label="Toggle Menu">
                    <span class="hamburger-line"></span><span class="hamburger-line"></span><span class="hamburger-line"></span>
                </button>
            </div>
        </div>
    </nav>"""


def footer_html(depth_prefix):
    return f"""    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    &lt;EB/&gt;
                    <p>I build systems that turn messy data into useful decisions.</p>
                </div>
                <div class="footer-links">
                    <a href="{depth_prefix}work.html">Work</a>
                    <a href="{depth_prefix}about.html">About</a>
                    <a href="{depth_prefix}resume.html">Resume</a>
                    <a href="https://github.com/Elice99" target="_blank">GitHub</a>
                    <a href="https://linktr.ee/elice99" target="_blank">LinkedIn</a>
                    <a href="{depth_prefix}contact.html">Contact</a>
                </div>
            </div>
            <div class="footer-bottom">
                <span>&copy; 2026 Elisha Bassey &middot; SYSTEM STATUS <span style="color:var(--teal-600)">&#9679; ONLINE</span></span>
            </div>
        </div>
    </footer>
    <button class="back-to-top" id="backToTop" aria-label="Back to top"><i class="fas fa-arrow-up"></i></button>

    <div class="cmdk-overlay" id="cmdkOverlay">
        <div class="cmdk-modal">
            <input type="text" id="cmdkInput" class="cmdk-input" placeholder="Search Elisha's portfolio..." autocomplete="off">
            <div class="cmdk-list" id="cmdkList"></div>
        </div>
    </div>
    <div class="cmdk-hint"><kbd>&#8984;</kbd><kbd>K</kbd><span>Search</span></div>

    <!-- Visitor analytics: add a GoatCounter (or similar) script here when
         the site is deployed, then restore the counter in the footer. -->"""


def asset_version(rel_path):
    """Short content hash appended to local asset URLs.

    Browsers cache CSS/JS aggressively. Adding ?v=<hash> means a returning
    visitor automatically gets the new file after a rebuild instead of a
    stale cached copy. Returns an empty string if the file is missing.
    """
    path = os.path.join(ROOT, rel_path)
    try:
        with open(path, "rb") as f:
            return "?v=" + hashlib.md5(f.read()).hexdigest()[:8]
    except OSError:
        return ""


def canonical_url(url_path):
    """Absolute URL for a page path. The homepage canonicalises to "/"."""
    if not SITE_URL:
        return ""
    if not url_path or url_path in ("/", "/index.html"):
        return SITE_URL + "/"
    return SITE_URL + url_path


def head_html(title, description, depth_prefix, url_path="/", og_image=""):
    canonical = canonical_url(url_path)
    image = og_image or (SITE_URL + "/images/Elice_1.webp" if SITE_URL else "")

    social = ""
    if canonical:
        social = f"""
    <link rel="canonical" href="{canonical}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:image" content="{image}">
    <meta property="og:image:alt" content="Elisha Bassey">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{image}">"""

    person = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Elisha Bassey",
        "jobTitle": "Data Analyst & Analytics Engineer",
        "sameAs": ["https://github.com/Elice99", "https://linktr.ee/elice99"],
        "knowsAbout": [
            "Data Analysis",
            "Business Intelligence",
            "Machine Learning",
            "Analytics Engineering",
        ],
    }
    if canonical:
        person["url"] = canonical_url("/")
    if image:
        person["image"] = image
    person_json = json.dumps(person, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <meta name="description" content="{description}">
    <meta name="author" content="Elisha Bassey">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">{social}
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <link rel="stylesheet" href="{depth_prefix}css/styles.css{asset_version('css/styles.css')}">
    <script type="application/ld+json">{person_json}</script>
    <script>window.SITE_ROOT = "{depth_prefix}";</script>
</head>"""


def scripts_html(depth_prefix):
    return f"""    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script src="{depth_prefix}js/projects-data.js{asset_version('js/projects-data.js')}"></script>
    <script src="{depth_prefix}js/main.js{asset_version('js/main.js')}"></script>
</body>
</html>"""


def tools_grid_html():
    from toolbox_data import TOOLS
    items = "".join(
        f'<div class="tool-item"><i class="{icon}"></i><span>{label}</span></div>'
        for icon, label in TOOLS
    )
    return f'<div class="tools-grid">{items}</div>'


def profile_photo_html(src, alt, placeholder_label):
    """Real photo once Elice_N.jpg exists in /images/, same ring-frame
    markup either way so swapping a placeholder for a real photo later
    needs no CSS changes."""
    if src:
        return f'<img src="{src}" alt="{alt}" class="profile-photo" style="width:100%;height:100%;object-fit:cover">'
    swap = "Elice_1" if placeholder_label == "PROFILE PHOTO" else "Elice_2,Elice_1"
    return (
        f'<div data-img-swap="{swap}" data-img-alt="Elisha Bassey" data-img-class="profile-photo" '
        f'style="display:flex;align-items:center;justify-content:center;height:100%;'
        f'background:var(--bg-secondary);color:var(--text-tertiary);font-family:\'JetBrains Mono\',monospace;'
        f'font-size:0.8125rem;text-align:center;padding:0.5rem">{placeholder_label}</div>'
    )


def assemble(page_path, title, description, current_path, depth_prefix, url_path=None):
    from build_projects import detect_profile_images
    content = read(page_path)
    content = content.replace("{{TOOLS_GRID}}", tools_grid_html())
    profile_imgs = detect_profile_images(ROOT)
    hero_src = profile_imgs[0] if len(profile_imgs) > 0 else None
    about_src = profile_imgs[1] if len(profile_imgs) > 1 else hero_src
    content = content.replace(
        "{{PROFILE_PHOTO_HERO}}",
        profile_photo_html(hero_src, "Elisha Bassey", "PROFILE PHOTO"),
    )
    content = content.replace(
        "{{PROFILE_PHOTO_ABOUT}}",
        profile_photo_html(about_src, "Elisha Bassey", "PHOTO"),
    )
    og_image = SITE_URL + profile_imgs[0] if (SITE_URL and profile_imgs) else ""
    html = "\n".join([
        head_html(title, description, depth_prefix, url_path or current_path, og_image),
        "<body>",
        nav_html(current_path, depth_prefix),
        '    <main id="main-content">',
        content,
        "    </main>",
        footer_html(depth_prefix),
        scripts_html(depth_prefix),
    ])
    # Root-relative links ("/work.html") only work on a web server. Rewrite them to
    # page-relative ones so the site also works when index.html is double-clicked.
    # "//host/..." (protocol-relative) is deliberately left alone.
    html = re.sub(r'(href|src)="/(?!/)', lambda m: m.group(1) + '="' + depth_prefix, html)
    return html


PAGES = [
    # (fragment file, output path, title, description, current_path (for nav active state), depth_prefix)
    ("home.html", "index.html", "Elisha Bassey | Data Analyst & Analytics Engineer",
     "I build systems that turn messy data into useful decisions.", "/index.html", ""),
    ("work.html", "work.html", "Work | Elisha Bassey",
     "A collection of analytical systems, business intelligence projects, and experiments.", "/work.html", ""),
    ("about.html", "about.html", "About | Elisha Bassey",
     "Geology to data: how Elisha Bassey's work evolved across increasingly analytical systems.", "/about.html", ""),
    ("experience.html", "experience.html", "Experience | Elisha Bassey",
     "Full work history across data analytics, BI, and remote sensing.", "/experience.html", ""),
    ("capabilities.html", "capabilities.html", "Capabilities | Elisha Bassey",
     "Skills mapped directly to the projects that demonstrate them.", "/capabilities.html", ""),
    ("now.html", "now.html", "Now | Elisha Bassey",
     "What Elisha Bassey is actively building right now.", "/now.html", ""),
    ("resume.html", "resume.html", "Resume | Elisha Bassey",
     "Download Elisha Bassey's resume as a PDF.", "/resume.html", ""),
    ("contact.html", "contact.html", "Contact | Elisha Bassey",
     "Get in touch with Elisha Bassey.", "/contact.html", ""),
]

PROJECT_PAGES_DEPTH = "../"

if __name__ == "__main__":
    # Project case-study pages. Load the module up front so projects-data.js
    # can be regenerated BEFORE the main pages, which lets asset_version()
    # hash the fresh copy for the ?v= cache-busting query.
    import importlib.util
    spec = importlib.util.spec_from_file_location("build_projects", os.path.join(os.path.dirname(__file__), "build_projects.py"))
    bp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bp)
    bp.write_js_data(ROOT)

    for fragment, out_name, title, desc, current, depth in PAGES:
        html = assemble(fragment, title, desc, current, depth, "/" + out_name)
        out_path = os.path.join(ROOT, out_name)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", out_path)

    bp.build_all(assemble, ROOT)
