export default function AboutPage() {
  return (
    <main className="mx-auto max-w-[1440px] px-5 py-20 md:px-10 lg:px-16 lg:py-28">
      <div className="max-w-4xl">
        <p className="font-mono text-[10px] uppercase tracking-[0.2em] text-accent">About</p>
        <h1 className="mt-6 text-5xl font-medium tracking-[-0.07em] text-text-primary md:text-7xl">
          I work where data meets decision-making.
        </h1>
      </div>

      <div className="mt-16 grid gap-12 lg:grid-cols-12">
        <div className="space-y-12 lg:col-span-8">
          <div>
            <p className="font-mono text-[10px] uppercase tracking-[0.2em] text-text-muted">Origin</p>
            <p className="mt-4 max-w-2xl text-lg leading-relaxed text-text-secondary">
              I studied Geology and built my early technical foundation around scientific data, mapping,
              observations, and interpretation. That work trained me to look beyond the surface and ask
              better questions before drawing conclusions.
            </p>
          </div>

          <div>
            <p className="font-mono text-[10px] uppercase tracking-[0.2em] text-text-muted">Evolution</p>
            <p className="mt-4 max-w-2xl text-lg leading-relaxed text-text-secondary">
              From remote sensing and field work, I moved into data analysis, business intelligence,
              and machine learning — especially in areas where messy real-world data needs structure,
              validation, and clear business meaning. My work has evolved across analytics, BI,
              product thinking, and systems building.
            </p>
          </div>

          <div>
            <p className="font-mono text-[10px] uppercase tracking-[0.2em] text-text-muted">Current focus</p>
            <p className="mt-4 max-w-2xl text-lg leading-relaxed text-text-secondary">
              I&#39;m focused on the space between analytics and systems: turning data into useful,
              explainable decisions, then building tools that make those decisions easier to act on.
              My strongest work sits at the intersection of data quality, analytics, BI, ML, and
              operational problem-solving.
            </p>
          </div>

          <div>
            <p className="font-mono text-[10px] uppercase tracking-[0.2em] text-text-muted">Philosophy</p>
            <p className="mt-4 max-w-2xl text-lg leading-relaxed text-text-secondary">
              I care most about evidence, clarity, and business relevance. A dashboard is only useful if it
              helps someone understand what happened, why it happened, and what should happen next.
            </p>
          </div>
        </div>

        <div className="lg:col-span-4">
          <div className="rounded-[1.75rem] border border-border bg-surface-secondary p-6">
            <p className="font-mono text-[10px] uppercase tracking-[0.2em] text-text-muted">What I bring</p>
            <ul className="mt-6 space-y-3 text-base text-text-secondary">
              <li>• Data analysis and validation</li>
              <li>• BI and operations reporting</li>
              <li>• Predictive modeling</li>
              <li>• Analytical systems and APIs</li>
              <li>• Business-first problem solving</li>
            </ul>
          </div>
        </div>
      </div>
    </main>
  );
}
