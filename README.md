# Elisha Bassey Portfolio

## Local setup
```
npm install
npm run dev
```
Open http://localhost:3001

## What's built (Day 1 foundation)
- Design tokens (colors, spacing, type scale) wired via CSS variables + Tailwind v4 @theme
- Geist + IBM Plex Mono fonts
- Light/dark/system theme switcher (persisted via next-themes)
- Nav with scroll-compress behavior
- Hero section with load animation sequence
- DATA → INTELLIGENCE → DECISION interactive section
- Selected Work section (featured + secondary project cards)
- Footer
- Project data model in /data/projects.ts — real verified numbers for TrustLake,
  Sales Pipeline, Airbnb, and the e-commerce platform. GlowMart and Golden Wok
  are placeholders — fill in real tagline/problem/stack/metric before launch,
  marked with TODO(Elice) comments.

## Next steps (Day 2)
- Build /projects/[slug] case-study template reading from data/projects.ts
- Build /projects listing page with category filters
- Build Capabilities, About, Experience, Now pages
- Decision Room interactive component
- Command palette (Cmd/Ctrl+K)

## Deploy
Push to GitHub, then connect the repo in Netlify (build command `npm run build`,
publish directory `.next`, or use the Next.js runtime Netlify auto-detects).
