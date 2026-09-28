const ROLES = [
  {
    year: "2025 — PRESENT",
    title: "Product Analyst — Data & Product Intelligence",
    org: "Dechsoft",
    detail:
      "Remote, pre-launch. Currently focused on the quantitative market research track — customer and business-audience research for an Abuja-based business OS built for Nigerian SMEs.",
  },
  {
    year: "2024 — 2025",
    title: "Data Analyst",
    org: "RespecTECH",
    detail:
      "Owned end-to-end MIS reporting for workforce performance, attrition, and recruitment efficiency. Identified a 12% spike in mid-level attrition that triggered an HR retention initiative. Automated 5 recurring reports via Power Query/Power BI, cutting manual reporting time by ~40% weekly. Built multi-source Power BI dashboards connecting MongoDB, internal databases, and Excel.",
  },
  {
    year: "2024",
    title: "Sales & Marketing Representative (Volunteer)",
    org: "NoOnes",
    detail:
      "Proactive outreach to prospective customers, objection handling, lead qualification and follow-up.",
  },
  {
    year: "2024",
    title: "Virtual Intern, Controllers Division",
    org: "Goldman Sachs (via Forage)",
    detail:
      "Calculated Net Asset Value (NAV), performed reconciliation and variance analysis, prepared financial performance reports.",
  },
  {
    year: "2023",
    title: "GIS and Data Analyst (NYSC)",
    org: "National Centre for Remote Sensing",
    detail:
      "Generated geospatial analysis reports for a government agency, maintaining data accuracy across 10+ deliverables.",
  },
  {
    year: "2022 — 2023",
    title: "Social Media & Team Lead (Intern)",
    org: "Oigetit",
    detail:
      "Led client-facing content and engagement strategy, achieving 70% growth in audience engagement.",
  },
  {
    year: "2022",
    title: "Device and Inventory Manager",
    org: "Spatial Layer Limited",
    detail:
      "Managed device inventory across multiple active projects, coordinating resource allocation across teams.",
  },
  {
    year: "2019",
    title: "Industrial Training Intern",
    org: "NASRDA (National Space Research and Development Agency)",
    detail:
      "First introduction to ArcGIS and EDAS. Used GPS to map noisy areas and analyzed population, vegetation, and pollution data.",
  },
];

export default function ExperiencePage() {
  return (
    <main className="mx-auto max-w-[1440px] px-5 py-16 md:px-10 lg:px-16 lg:py-24">
      <h1
        className="font-sans tracking-tight text-text-primary"
        style={{ fontSize: "var(--text-h1)" }}
      >
        Experience
      </h1>

      <div className="mt-12 flex flex-col">
        {ROLES.map((role) => (
          <div
            key={`${role.title}-${role.org}`}
            className="grid grid-cols-1 gap-2 border-t border-border py-8 lg:grid-cols-12 lg:gap-8"
          >
            <p className="font-mono text-technical text-text-muted lg:col-span-2">
              {role.year}
            </p>
            <div className="lg:col-span-10">
              <p className="text-text-primary">{role.title}</p>
              <p className="mt-1 font-mono text-technical text-accent">
                {role.org}
              </p>
              <p className="mt-3 max-w-2xl text-sm text-text-secondary">
                {role.detail}
              </p>
            </div>
          </div>
        ))}
      </div>
    </main>
  );
}
