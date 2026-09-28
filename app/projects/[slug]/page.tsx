import { notFound } from "next/navigation";
import Link from "next/link";
import { projects, getProject } from "@/data/projects";

export function generateStaticParams() {
  return projects.map((p) => ({ slug: p.slug }));
}

export function generateMetadata({ params }: { params: { slug: string } }) {
  const project = getProject(params.slug);
  if (!project) return {};
  return {
    title: `${project.title} — Elisha Bassey`,
    description: project.tagline,
    openGraph: { title: project.title, description: project.tagline },
  };
}

const SECTION_LABEL = "font-mono text-technical text-text-muted";

export default function ProjectCaseStudy({
  params,
}: {
  params: { slug: string };
}) {
  const project = getProject(params.slug);
  if (!project) notFound();

  const idx = projects.findIndex((p) => p.slug === project.slug);
  const next = projects[(idx + 1) % projects.length];

  return (
    <main className="mx-auto max-w-[1440px] px-5 py-16 md:px-10 lg:px-16 lg:py-24">
      {/* Hero */}
      <p className={SECTION_LABEL}>
        {project.status === "pre-mvp"
          ? "PRE-MVP"
          : project.status.toUpperCase()}
      </p>
      <h1
        className="mt-3 font-sans tracking-tight text-text-primary"
        style={{ fontSize: "var(--text-h1)" }}
      >
        {project.title.toUpperCase()}
      </h1>
      <p
        className="mt-4 max-w-xl text-text-secondary"
        style={{ fontSize: "var(--text-body-lg)" }}
      >
        {project.tagline}
      </p>
      <p className="mt-6 font-mono text-technical text-accent">
        {project.stack.length > 0
          ? project.stack.join(" · ")
          : "STACK TBD"}
      </p>

      {/* Key metric strip */}
      <div className="mt-10 flex items-center gap-3 border-y border-border py-6">
        <span
          className="font-mono text-text-primary"
          style={{ fontSize: "var(--text-h3)" }}
        >
          {project.metric.value}
        </span>
        <span className={SECTION_LABEL}>{project.metric.label}</span>
      </div>

      {!project.verified && (
        <div className="mt-6 rounded-sm border border-anomaly/40 bg-anomaly/10 p-4 text-sm text-anomaly">
          This case study has placeholder content. Replace the problem,
          stack, and metric in data/projects.ts before publishing.
        </div>
      )}

      {/* Problem */}
      <section className="mt-16 grid grid-cols-1 gap-8 lg:grid-cols-12">
        <h2 className={`lg:col-span-3 ${SECTION_LABEL}`}>THE PROBLEM</h2>
        <p
          className="lg:col-span-9"
          style={{ fontSize: "var(--text-body-lg)" }}
        >
          {project.problem}
        </p>
      </section>

      {/* Approach — placeholder prose block; fill in per project when ready */}
      <section className="mt-16 grid grid-cols-1 gap-8 border-t border-border pt-16 lg:grid-cols-12">
        <h2 className={`lg:col-span-3 ${SECTION_LABEL}`}>APPROACH</h2>
        <p className="lg:col-span-9 text-text-secondary">
          {/* Elice: replace with the real approach narrative for this project */}
          Add the approach narrative here — what you built, the order you
          built it in, and the key decisions along the way.
        </p>
      </section>

      {/* Outcome */}
      <section className="mt-16 grid grid-cols-1 gap-8 border-t border-border pt-16 lg:grid-cols-12">
        <h2 className={`lg:col-span-3 ${SECTION_LABEL}`}>OUTCOME</h2>
        <p className="lg:col-span-9 text-text-secondary">
          {/* Elice: replace with the real outcome / what changed */}
          Add what shipped, what it changed, and what you&apos;d do differently.
        </p>
      </section>

      {/* Next project */}
      <div className="mt-20 border-t border-border pt-10">
        <p className={SECTION_LABEL}>NEXT CASE STUDY</p>
        <Link
          href={`/projects/${next.slug}`}
          className="group mt-2 inline-flex items-center gap-2 font-sans tracking-tight text-text-primary transition-colors hover:text-accent"
          style={{ fontSize: "var(--text-h3)" }}
        >
          {next.title}
          <span className="transition-transform group-hover:translate-x-1">
            →
          </span>
        </Link>
      </div>
    </main>
  );
}
