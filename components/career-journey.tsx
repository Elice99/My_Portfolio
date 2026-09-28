"use client";

import { motion } from "motion/react";

const STAGES = [
  "EARTH SCIENCE",
  "REMOTE SENSING",
  "FIELD DATA",
  "DATA VALIDATION",
  "ANALYTICS",
  "BUSINESS INTELLIGENCE",
  "MACHINE LEARNING",
  "SYSTEMS & APIs",
];

export function CareerJourney() {
  return (
    <section className="mx-auto max-w-[1440px] px-5 py-16 md:px-10 lg:px-16 lg:py-24">
      <div className="mb-12 border-b border-border pb-8">
        <p className="mb-3 font-mono text-[10px] uppercase tracking-[0.2em] text-text-muted">Career progression</p>
        <h2 className="text-3xl font-medium tracking-[-0.05em] text-text-primary md:text-5xl">From questions to systems.</h2>
      </div>
      <div className="flex flex-col gap-3 lg:flex-row lg:items-center lg:gap-2">
        {STAGES.map((stage, i) => (
          <motion.div
            key={stage}
            initial={{ opacity: 0, y: 10 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: i * 0.05 }}
            className="flex items-center gap-2 lg:flex-1"
          >
            <div className="flex-1 border-l-2 border-border py-4 pl-4 lg:border-l-0 lg:border-t-2 lg:py-0 lg:pl-0 lg:pt-4">
              <p className="font-mono text-[10px] uppercase tracking-[0.16em] text-text-secondary">{stage}</p>
            </div>
            {i < STAGES.length - 1 && <span className="hidden font-mono text-text-muted lg:inline">→</span>}
          </motion.div>
        ))}
      </div>
    </section>
  );
}
