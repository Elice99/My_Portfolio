"use client";

import { useState } from "react";
import Link from "next/link";
import { projects, type ProjectCategory } from "@/data/projects";

const GROUPS: { key: ProjectCategory; label: string; skills: string[] }[] = [
  {
    key: "analytics",
    label: "DATA",
    skills: ["SQL", "Python", "Excel", "Data Cleaning", "Data Validation"],
  },
  {
    key: "bi",
    label: "INTELLIGENCE",
    skills: ["Power BI", "EDA", "Statistics", "Data Storytelling"],
  },
  {
    key: "ml",
    label: "PREDICTION",
    skills: ["Machine Learning", "XGBoost", "Predictive Analytics"],
  },
  {
    key: "systems",
    label: "SYSTEMS",
    skills: ["FastAPI", "PostgreSQL", "Docker", "APIs"],
  },
  {
    key: "business",
    label: "BUSINESS",
    skills: [
      "Business Analysis",
      "Product Analytics",
      "Operations",
      "Decision Support",
    ],
  },
];

export default function CapabilitiesPage() {
  const [active, setActive] = useState<ProjectCategory | null>(null);

  const evidencing = active
    ? projects.filter((p) => p.category.includes(active))
    : [];

  return (
    <main className="mx-auto max-w-[1440px] px-5 py-16 md:px-10 lg:px-16 lg:py-24">
      <h1
        className="font-sans tracking-tight text-text-primary"
        style={{ fontSize: "var(--text-h1)" }}
      >
        Capabilities
      </h1>
      <p className="mt-4 max-w-lg text-text-secondary">
        Click a category to see the projects that put it into practice.
      </p>

      <div className="mt-12 grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-5">
        {GROUPS.map((group) => (
          <button
            key={group.key}
            onClick={() => setActive(active === group.key ? null : group.key)}
            className={`rounded-sm border p-5 text-left transition-colors ${
              active === group.key
                ? "border-accent"
                : "border-border hover:border-accent"
            }`}
          >
            <p className="font-mono text-technical text-accent">
              {group.label}
            </p>
            <ul className="mt-3 flex flex-col gap-1">
              {group.skills.map((skill) => (
                <li key={skill} className="text-sm text-text-secondary">
                  {skill}
                </li>
              ))}
            </ul>
          </button>
        ))}
      </div>

      {active && (
        <div className="mt-12 border-t border-border pt-8">
          <p className="font-mono text-technical text-text-muted">
            PROJECTS DEMONSTRATING {active.toUpperCase()}
          </p>
          <div className="mt-4 grid grid-cols-1 gap-4 md:grid-cols-2">
            {evidencing.length === 0 && (
              <p className="text-text-secondary">Nothing here yet.</p>
            )}
            {evidencing.map((p) => (
              <Link
                key={p.slug}
                href={`/projects/${p.slug}`}
                className="rounded-sm border border-border p-4 transition-colors hover:border-accent"
              >
                <p className="text-text-primary">{p.title}</p>
                <p className="mt-1 text-sm text-text-secondary">
                  {p.tagline}
                </p>
              </Link>
            ))}
          </div>
        </div>
      )}
    </main>
  );
}
