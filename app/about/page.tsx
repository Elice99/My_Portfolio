export default function AboutPage() {
  return (
    <main className="mx-auto max-w-[1440px] px-5 py-16 md:px-10 lg:px-16 lg:py-24">
      <h1
        className="max-w-3xl font-sans tracking-tight text-text-primary"
        style={{ fontSize: "var(--text-h1)" }}
      >
        I&apos;m interested in what happens between data and decisions.
      </h1>

      <div className="mt-16 grid grid-cols-1 gap-12 lg:grid-cols-12">
        <div className="lg:col-span-8 flex flex-col gap-10">
          <div>
            <p className="font-mono text-technical text-text-muted">
              ORIGIN
            </p>
            <p className="mt-2 text-text-secondary">
              {/* Elice: expand this with the real personal story — what
                  drew you to geology, and the moment data started to pull
                  harder than rock. */}
              I hold a B.Sc. (Honours) in Geology from Prince Audu Abubakar
              University, Kogi State. My first real exposure to structured
              data analysis came through remote sensing and GIS work — using
              ArcGIS to map and analyze population, vegetation, and pollution
              patterns.
            </p>
          </div>

          <div>
            <p className="font-mono text-technical text-text-muted">
              EVOLUTION
            </p>
            <p className="mt-2 text-text-secondary">
              That fieldwork became the bridge into analytics. Over the past
              3–4 years I&apos;ve worked across healthcare, blockchain, sales,
              and e-commerce data — moving from spreadsheets and geospatial
              reports into SQL, Power BI, and eventually machine learning.
            </p>
          </div>

          <div>
            <p className="font-mono text-technical text-text-muted">
              CURRENT
            </p>
            <p className="mt-2 text-text-secondary">
              I&apos;m now a Product Analyst at Dechsoft, an Abuja-based
              startup building a business OS for Nigerian SMEs, while
              continuing to build analytics engineering and BI systems on my
              own — with a particular interest in fintech, healthtech, and
              e-commerce.
            </p>
          </div>

          <div>
            <p className="font-mono text-technical text-text-muted">
              PHILOSOPHY
            </p>
            <p className="mt-2 text-text-secondary">
              Data is only useful when it changes understanding or improves
              a decision.
            </p>
          </div>
        </div>

        <div className="lg:col-span-4">
          <p className="font-mono text-technical text-text-muted">
            WHAT I CARE ABOUT
          </p>
          <ul className="mt-3 flex flex-col gap-2 text-text-secondary">
            <li>Useful analysis</li>
            <li>Trustworthy data</li>
            <li>Understandable systems</li>
            <li>Measurable outcomes</li>
            <li>Continuous learning</li>
          </ul>
        </div>
      </div>
    </main>
  );
}
