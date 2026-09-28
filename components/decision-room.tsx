"use client";

import { motion } from "motion/react";
import { useState } from "react";

const STEPS = [
  {
    n: "01",
    title: "Understand the problem",
    detail: "What decision needs to be made? What information is missing? What's at stake?",
  },
  {
    n: "02",
    title: "Assess the data",
    detail: "What data exists? How clean is it? What validation is required before analysis begins?",
  },
  {
    n: "03",
    title: "Explore and analyze",
    detail: "What patterns emerge? Which factors drive outcomes? What assumptions need testing?",
  },
  {
    n: "04",
    title: "Build the system",
    detail: "How can this analysis be operationalized? What dashboards, models, or APIs are needed?",
  },
  {
    n: "05",
    title: "Communicate findings",
    detail: "What does the evidence say? What are the limitations? What should happen next?",
  },
  {
    n: "06",
    title: "Enable action",
    detail: "How can teams actually use this to make better decisions? What's the next step?",
  },
];

export function DecisionRoom() {
  const [started, setStarted] = useState(false);
  const [activeStep, setActiveStep] = useState<number | null>(null);

  return (
    <section className="mx-auto max-w-[1440px] px-5 py-24 md:px-10 lg:px-16 lg:py-36">
      <div className="mb-8 border-b border-border pb-8">
        <p className="mb-3 font-mono text-[10px] uppercase tracking-[0.2em] text-accent">Process</p>
        <h2 className="text-4xl font-medium tracking-[-0.06em] text-text-primary md:text-5xl">How I work.</h2>
      </div>
      <p className="font-mono text-[10px] uppercase tracking-[0.2em] text-text-muted">The six-step analytical process</p>
      <p className="mt-4 text-lg text-text-primary md:text-xl">From problem to decision.</p>

      {!started ? (
        <motion.button
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          onClick={() => setStarted(true)}
          className="group mt-10 inline-flex items-center gap-2 rounded-full bg-accent px-6 py-3 text-sm font-medium text-background transition-transform hover:-translate-y-0.5"
        >
          Start
          <span className="transition-transform group-hover:translate-x-0.5">→</span>
        </motion.button>
      ) : (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="mt-12 flex flex-col gap-2">
          {STEPS.map((step, i) => (
            <motion.div
              key={step.n}
              initial={{ opacity: 0, y: 8 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.35, delay: i * 0.08 }}
              className="border-b border-border"
            >
              <button
                onClick={() => setActiveStep(activeStep === i ? null : i)}
                className="flex w-full items-center gap-4 py-4 text-left"
              >
                <span className="font-mono text-[10px] font-medium text-accent">{step.n}</span>
                <span className="text-text-primary">{step.title}</span>
                <span className="ml-auto text-text-muted transition-transform" style={{ transform: activeStep === i ? "rotate(180deg)" : "rotate(0deg)" }}>↓</span>
              </button>
              {activeStep === i && (
                <motion.p initial={{ height: 0, opacity: 0 }} animate={{ height: "auto", opacity: 1 }} exit={{ height: 0, opacity: 0 }} transition={{ duration: 0.25 }} className="overflow-hidden pb-4 pl-9 text-sm text-text-secondary">
                  {step.detail}
                </motion.p>
              )}
            </motion.div>
          ))}
        </motion.div>
      )}
    </section>
  );
}
