"use client";

import { motion } from "motion/react";
import { Project } from "@/data/projects";

const EASE = [0.16, 1, 0.3, 1] as const;

export function CaseStudyHero({ project }: { project: Project }) {
  return (
    <section className="relative mx-auto max-w-[1440px] px-5 py-24 md:px-10 lg:px-16 lg:py-32">
      <div className="pointer-events-none absolute left-5 right-5 top-0 h-px bg-border/50 md:left-10 md:right-10 lg:left-16 lg:right-16" />

      <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.5, ease: EASE }} className="mb-8 flex items-center gap-3">
        <span className="h-2 w-2 rounded-full bg-accent" />
        <p className="font-mono text-[10px] uppercase tracking-[0.2em] text-accent">Case Study 01</p>
      </motion.div>

      <motion.h1 initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.1, ease: EASE }} className="max-w-4xl text-5xl font-medium leading-tight tracking-[-0.06em] text-text-primary md:text-7xl">
        {project.title}
      </motion.h1>

      <motion.p initial={{ opacity: 0, y: 16 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.55, delay: 0.25, ease: EASE }} className="mt-6 max-w-2xl text-lg text-text-secondary">
        {project.tagline}
      </motion.p>

      <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.5, delay: 0.35, ease: EASE }} className="mt-12 flex flex-wrap gap-8 border-t border-border pt-8">
        <div>
          <p className="font-mono text-[10px] uppercase text-text-muted">Status</p>
          <p className="mt-2 text-sm font-medium text-text-primary capitalize">{project.status}</p>
        </div>
        <div>
          <p className="font-mono text-[10px] uppercase text-text-muted">Category</p>
          <p className="mt-2 text-sm font-medium text-text-primary">{project.category.join(" · ")}</p>
        </div>
        <div>
          <p className="font-mono text-[10px] uppercase text-text-muted">Key Metric</p>
          <p className="mt-2 text-sm font-medium text-accent">{project.metric.value}</p>
        </div>
      </motion.div>
    </section>
  );
}
