"use client";

import { useState } from "react";

const STAGES = [
  { key: "DATA", detail: "SQL · Python · Excel · Data Cleaning" },
  { key: "INTELLIGENCE", detail: "Power BI · EDA · ML · Analytics" },
  { key: "DECISION", detail: "Business Analysis · Product · Operations" },
] as const;

export function SystemSection() {
  const [active, setActive] = useState<number | null>(null);

  return (
    <section className="mx-auto max-w-[1440px] px-5 py-16 md:px-10 lg:px-16 lg:py-24">
      <p className="max-w-lg text-text-secondary" style={{ fontSize: "var(--text-body-lg)" }}>
        I work across analytics, business intelligence, machine learning and
        data-driven systems.
      </p>

      <div className="mt-12 flex flex-col gap-2">
        {STAGES.map((stage, i) => (
          <div key={stage.key}>
            <button
              onClick={() => setActive(active === i ? null : i)}
              onMouseEnter={() => setActive(i)}
              className="flex w-full items-center justify-between border-b border-border py-6 text-left transition-colors"
            >
              <span
                className="font-sans tracking-tight text-text-primary"
                style={{ fontSize: "var(--text-h2)" }}
              >
                {stage.key}
              </span>
              {i < STAGES.length - 1 && (
                <span className="hidden font-mono text-technical text-text-muted md:inline">
                  ↓
                </span>
              )}
            </button>
            <div
              className={`grid transition-all duration-300 ease-out ${
                active === i ? "grid-rows-[1fr] opacity-100" : "grid-rows-[0fr] opacity-0"
              }`}
            >
              <div className="overflow-hidden">
                <p className="py-3 font-mono text-technical text-accent">
                  {stage.detail}
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
