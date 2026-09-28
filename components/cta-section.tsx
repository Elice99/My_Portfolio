const NOW = [
  {
    status: "BUILDING",
    title: "TrustLake",
    detail:
      "A data quality and trust engine focused on deterministic validation, explainable scoring, and human decision support. The project is still in active development as a pre-MVP system foundation.",
    href: "/projects/trustlake",
  },
  {
    status: "PARTICIPATING",
    title: "DataDNA / Onyx Monthly Data Challenge",
    detail:
      "Monthly challenge work focused on analytical storytelling, practical BI, and evidence-based business reporting across modern data problems.",
  },
  {
    status: "LEARNING",
    title: "AI Engineering & Product Systems",
    detail:
      "Strengthening my understanding of AI workflows, backend systems, product thinking, and how analytics can become more usable in real operational settings.",
  },
];

const RECENT = [
  {
    title: "GlowMart Sales & Inventory Dashboard",
    detail:
      "Executive BI project that resolved a sales vs inventory dispute using transactional evidence and business-first analysis.",
    href: "/projects/glowmart",
  },
  {
    title: "Sales Pipeline Prediction API",
    detail:
      "XGBoost-based pipeline model and FastAPI service that turns CRM data into actionable deal-outcome predictions.",
    href: "/projects/sales-pipeline-prediction",
  },
  {
    title: "Airbnb Market Intelligence",
    detail:
      "End-to-end analytics and pricing project combining warehouse-style processing, ML, and market intelligence.",
    href: "/projects/airbnb-market-intelligence",
  },
];

export default function NowPage() {
  return (
    <main className="mx-auto max-w-[1440px] px-5 py-20 md:px-10 lg:px-16 lg:py-28">
      <div className="max-w-3xl">
        <p className="font-mono text-[10px] uppercase tracking-[0.2em] text-accent">Now</p>
        <h1 className="mt-6 text-5xl font-medium tracking-[-0.07em] text-text-primary md:text-7xl">
          What I’m building right now.
        </h1>
      </div>

      <div className="mt-16 space-y-8">
        {NOW.map((item) => (
          <div key={item.title} className="rounded-[1.75rem] border border-border bg-surface-secondary/40 p-6 md:p-8">
            <p className="font-mono text-[10px] uppercase tracking-[0.2em] text-accent">{item.status}</p>
            <h2 className="mt-4 text-2xl font-medium tracking-[-0.05em] text-text-primary md:text-3xl">{item.title}</h2>
            <p className="mt-4 max-w-3xl text-base leading-relaxed text-text-secondary">{item.detail}</p>
            {item.href && (
              <a href={item.href} className="mt-6 inline-flex text-sm text-text-primary hover:text-accent">
                View project ↗
              </a>
            )}
          </div>
        ))}
      </div>

      <div className="mt-20 border-t border-border pt-10">
        <p className="font-mono text-[10px] uppercase tracking-[0.2em] text-text-muted">Recently shipped</p>
        <div className="mt-8 space-y-6">
          {RECENT.map((item) => (
            <div key={item.title} className="border-b border-border pb-6">
              <p className="text-xl font-medium tracking-[-0.04em] text-text-primary">{item.title}</p>
              <p className="mt-2 max-w-2xl text-base text-text-secondary">{item.detail}</p>
              {item.href && (
                <a href={item.href} className="mt-4 inline-flex text-sm text-text-primary hover:text-accent">
                  View case study ↗
                </a>
              )}
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
