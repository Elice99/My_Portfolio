const NOW = [
  {
    status: "BUILDING",
    title: "TrustLake",
    detail:
      "Data quality platform centered on a deterministic Trust Score with AI-assisted explanations. Currently at Stage 1 (landing page complete), moving into backend foundation.",
    href: "/projects/trustlake",
  },
  {
    status: "WORKING ON",
    title: "Dechsoft Market Research",
    detail:
      "Weekly quantitative research track covering market size, competitor landscape, and adoption barriers for an Abuja-based business OS.",
  },
  {
    status: "EXPLORING",
    title: "Onyx Data Gig-Economy Challenge",
    detail:
      "Monthly data challenge analyzing African gig-economy and digital wallet fraud/risk, built as an Excel-based analytical report.",
  },
];

const RECENT = [
  {
    title: "The Resilience Gap — Workforce Resilience Index",
    detail:
      "DataDNA/Onyx Data Analytics Challenge (July 2026). Four-page Power BI report on AI adoption outpacing workforce adaptability.",
  },
  {
    title: "GlowMart Sales & Inventory Dashboard",
    detail:
      "SkillAhead Data Analytics Challenge (June 2026). Reframed a perceived supply conflict as a growth problem.",
    href: "/projects/glowmart",
  },
];

export default function NowPage() {
  return (
    <main className="mx-auto max-w-[1440px] px-5 py-16 md:px-10 lg:px-16 lg:py-24">
      <h1
        className="font-sans tracking-tight text-text-primary"
        style={{ fontSize: "var(--text-h1)" }}
      >
        Now
      </h1>
      <p className="mt-4 max-w-lg text-text-secondary">
        {/* This page is meant to be updated regularly — keep it current. */}
        What I&apos;m actively working on, updated as things move.
      </p>

      <div className="mt-12 flex flex-col gap-8">
        {NOW.map((item) => (
          <div key={item.title} className="border-t border-border pt-6">
            <p className="font-mono text-technical text-accent">
              {item.status}
            </p>
            <p className="mt-1 text-text-primary">{item.title}</p>
            <p className="mt-2 max-w-2xl text-sm text-text-secondary">
              {item.detail}
            </p>
          </div>
        ))}
      </div>

      <div className="mt-16 border-t border-border pt-8">
        <p className="font-mono text-technical text-text-muted">
          RECENTLY SHIPPED
        </p>
        <div className="mt-4 flex flex-col gap-4">
          {RECENT.map((item) => (
            <div key={item.title}>
              <p className="text-text-primary">{item.title}</p>
              <p className="mt-1 text-sm text-text-secondary">
                {item.detail}
              </p>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
