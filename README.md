# Elisha Bassey Portfolio

## Local setup
```
npm install
npm run dev
```
Open http://localhost:3000

## Pages built so far
- / (home) — hero, system section, selected work, evidence, decision room, career journey
- /work — project listing with category filters
- /projects/[slug] — reusable case-study template (6 projects wired up)
- /capabilities — clickable skill groups filtering into projects
- /about — real bio from your profile
- /experience — full real work history timeline
- /now — current focus, built from real active work
- /resume — CV download page (needs a real PDF dropped into /public/documents/)
- /contact — real contact links
- Global command palette (Cmd/Ctrl+K)

## Project data
Everything project-related lives in /data/projects.ts as a flat array —
add a new project by adding an object, no other code changes needed.
Golden Wok is still a placeholder (marked verified: false, with a visible
warning banner on its case-study page) — swap in real details whenever
you have them, same pattern as GlowMart.

## Known gaps (deliberately left for you)
- Resume PDF file itself
- Portrait photos (currently placeholder boxes in Hero — see section 13
  of the design spec for the 4 photo roles)
- Portfolio Intelligence section (needs real analytics wired up — Day 3)
- "Currently Building" section on homepage — Now page exists, homepage
  card version not yet built
- Golden Wok project details

## Deploy
Push to GitHub, connect the repo in Netlify. Next.js runtime is
auto-detected; no special build config needed.
