"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "motion/react";

const STEPS = [
  {
    n: "01",
    title: "Validate the metric",
    detail:
      "Confirm the drop is real, not a tracking bug, timezone shift, or reporting-period mismatch.",
  },
  {
    n: "02",
    title: "Locate the change",
    detail:
      "Narrow down when the drop started and whether it's sudden or gradual.",
  },
  {
    n: "03",
    title: "Segment the problem",
    detail:
      "Break revenue down by channel, region, product, and customer segment to isolate where it's coming from.",
  },
  {
    n: "04",
    title: "Identify the drivers",
    detail:
      "Cross-reference the affected segment against known changes: pricing, campaigns, seasonality, competitor activity.",
  },
  {
    n: "05",
    title: "Quantify the impact",
    detail:
      "Attach a number to each candidate driver so effort goes where it matters most.",
  },
  {
    n: "06",
    title: "Determine action",
    detail:
      "Translate the finding into a specific, owned next step — not just a report.",
  },
];

export function DecisionRoom() {
  const [started, setStarted] = useState(false);
  const [activeStep, setActiveStep] = useState<number | null>(null);

  return (
    <section className="mx-auto max-w-[1440px] px-5 py-16 md:px-10 lg:px-16 lg:py-24">
      <h2
        className="font-sans tracking-tight text-text-primary"
        style={{ fontSize: "var(--text-h2)" }}
      >
        How I think
      </h2>
      <p className="mt-4 font-mono text-technical text-text-muted">
        HOW WOULD YOU INVESTIGATE THIS?
      </p>
      <p
        className="mt-2 text-text-primary"
        style={{ fontSize: "var(--text-body-lg)" }}
      >
        Revenue dropped 18%.
      </p>

      {!started ? (
        <button
          onClick={() => setStarted(true)}
          className="group mt-8 inline-flex items-center gap-2 rounded-full bg-accent px-6 py-3 text-sm font-medium text-background transition-transform hover:-translate-y-0.5"
        >
          Start investigation
          <span className="transition-transform group-hover:translate-x-0.5">
            →
          </span>
        </button>
      ) : (
        <div className="mt-8 flex flex-col gap-2">
          {STEPS.map((step, i) => (
            <motion.div
              key={step.n}
              initial={{ opacity: 0, y: 8 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.35, delay: i * 0.08 }}
              className="border-b border-border"
            >
              <button
                onClick={() =>
                  setActiveStep(activeStep === i ? null : i)
                }
                className="flex w-full items-center gap-4 py-4 text-left"
              >
                <span className="font-mono text-technical text-accent">
                  {step.n}
                </span>
                <span className="text-text-primary">{step.title}</span>
              </button>
              <AnimatePresence>
                {activeStep === i && (
                  <motion.p
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: "auto", opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}
                    transition={{ duration: 0.25 }}
                    className="overflow-hidden pb-4 pl-9 text-sm text-text-secondary"
                  >
                    {step.detail}
                  </motion.p>
                )}
              </AnimatePresence>
            </motion.div>
          ))}
        </div>
      )}
    </section>
  );
}
