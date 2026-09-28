"use client";

import { useState } from "react";
import Link from "next/link";
import { projects, type ProjectCategory } from "@/data/projects";

const FILTERS: { key: "all" | ProjectCategory; label: string }[] = [
  { key: "all", label: "ALL" },
  { key: "analytics", label: "ANALYTICS" },
  { key: "bi", label: "BI" },
  { key: "ml", label: "ML" },
  { key: "business", label: "BUSINESS" },
  { key: "systems", label: "SYSTEMS" },
];

export default function WorkPage() {
  const [filter, setFilter] = useState<"all" | ProjectCategory>("all");

  const visible =
    filter === "all"
      ? projects
      : projects.filter((p) => p.category.includes(filter));

  return (
    <main className="mx-auto max-w-[1440px] px-5 py-16 md:px-10 lg:px-16 lg:py-24">
      <h1
        className="font-sans tracking-tight text-text-primary"
        style={{ fontSize: "var(--text-h1)" }}
      >
        Work
      </h1>
      <p
        className="mt-4 max-w-lg text-text-secondary"
        style={{ fontSize: "var(--text-body-lg)" }}
      >
        A collection of analytical systems, business intelligence projects,
        experiments and products.
      </p>

      <div className="mt-10 flex flex-wrap gap-2">
        {FILTERS.map((f) => (
          <button
            key={f.key}
            onClick={() => setFilter(f.key)}
            className={`rounded-full border px-4 py-2 font-mono text-technical transition-colors ${
              filter === f.key
                ? "border-accent bg-accent text-background"
                : "border-border text-text-secondary hover:border-accent hover:text-accent"
            }`}
          >
            {f.label}
          </button>
        ))}
      </div>

      <div className="mt-10 grid grid-cols-1 gap-6 md:grid-cols-2">
        {visible.map((project) => (
          <Link
            key={project.slug}
            href={`/projects/${project.slug}`}
            className="group rounded-sm border border-border p-6 transition-colors hover:border-accent"
          >
            <div className="flex items-center justify-between">
              <p className="font-sans text-lg text-text-primary">
                {project.title}
              </p>
              <span className="font-mono text-technical text-text-muted">
                {project.status.toUpperCase()}
              </span>
            </div>
            <p className="mt-2 text-sm text-text-secondary">
              {project.tagline}
            </p>
            <p className="mt-4 font-mono text-technical text-text-muted">
              {project.category.join(" · ").toUpperCase()}
            </p>
          </Link>
        ))}
      </div>
    </main>
  );
}
