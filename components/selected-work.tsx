import Link from "next/link";
import { getFeatured, getSecondary } from "@/data/projects";

export function SelectedWork() {
  const featured = getFeatured();
  const secondary = getSecondary();

  return (
    <section className="mx-auto max-w-[1440px] px-5 py-16 md:px-10 lg:px-16 lg:py-24">
      <h2
        className="font-sans tracking-tight text-text-primary"
        style={{ fontSize: "var(--text-h2)" }}
      >
        Selected work
      </h2>

      {featured && (
        <Link
          href={`/projects/${featured.slug}`}
          className="group mt-10 block rounded-sm border border-border bg-surface-secondary p-8 transition-colors hover:border-accent md:p-12"
        >
          <div className="flex flex-col justify-between gap-6 md:flex-row md:items-end">
            <div>
              <p className="font-mono text-technical text-accent">
                {featured.title.toUpperCase()}
              </p>
              <h3
                className="mt-2 font-sans tracking-tight text-text-primary"
                style={{ fontSize: "var(--text-h3)" }}
              >
                {featured.tagline}
              </h3>
              <p className="mt-4 font-mono text-technical text-text-muted">
                {featured.stack.join(" · ")}
              </p>
            </div>
            <div className="shrink-0 text-right">
              <p
                className="font-mono text-text-primary"
                style={{ fontSize: "var(--text-h3)" }}
              >
                {featured.metric.value}
              </p>
              <p className="font-mono text-technical text-text-muted">
                {featured.metric.label}
              </p>
            </div>
          </div>
          <span className="mt-6 inline-flex items-center gap-2 text-sm text-accent">
            Explore case study
            <span className="transition-transform group-hover:translate-x-0.5">
              →
            </span>
          </span>
        </Link>
      )}

      <div className="mt-6 grid grid-cols-1 gap-6 md:grid-cols-2">
        {secondary.map((project) => (
          <Link
            key={project.slug}
            href={`/projects/${project.slug}`}
            className="group rounded-sm border border-border p-6 transition-colors hover:border-accent"
          >
            <p className="font-sans text-lg text-text-primary">
              {project.title}
            </p>
            <p className="mt-2 text-sm text-text-secondary">
              {project.tagline}
            </p>
            <p className="mt-4 font-mono text-technical text-text-muted">
              {project.stack.length > 0
                ? project.stack.join(" · ")
                : "IN PROGRESS"}
            </p>
          </Link>
        ))}
      </div>
    </section>
  );
}
