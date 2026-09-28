const STAGES = [
  "EARTH SCIENCE",
  "REMOTE SENSING",
  "FIELD DATA",
  "ANALYTICS",
  "BUSINESS INTELLIGENCE",
  "AI / ML",
];

export function CareerJourney() {
  return (
    <section className="mx-auto max-w-[1440px] px-5 py-16 md:px-10 lg:px-16 lg:py-24">
      <h2
        className="font-sans tracking-tight text-text-primary"
        style={{ fontSize: "var(--text-h2)" }}
      >
        Career journey
      </h2>
      <p className="mt-4 max-w-lg text-text-secondary">
        My work with data evolved across increasingly analytical systems.
      </p>

      <div className="mt-12 flex flex-col lg:flex-row lg:items-center lg:gap-2">
        {STAGES.map((stage, i) => (
          <div key={stage} className="flex items-center gap-2 lg:flex-1">
            <div className="flex-1 border-l-2 border-border py-4 pl-4 lg:border-l-0 lg:border-t-2 lg:py-0 lg:pl-0 lg:pt-4">
              <p className="font-mono text-technical text-text-secondary">
                {stage}
              </p>
            </div>
            {i < STAGES.length - 1 && (
              <span className="hidden font-mono text-text-muted lg:inline">
                →
              </span>
            )}
          </div>
        ))}
      </div>
    </section>
  );
}
