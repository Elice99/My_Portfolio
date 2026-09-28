"use client";

import Link from "next/link";
import { motion } from "motion/react";
import { getFeatured, getSecondary } from "@/data/projects";

export function SelectedWork() {
  const featured = getFeatured();
  const secondary = getSecondary().filter((p) => p.verified).slice(0, 4);

  return (
    <section className="mx-auto max-w-[1440px] px-5 py-24 md:px-10 lg:px-16 lg:py-36">
      <div className="mb-12 flex items-end justify-between gap-6 border-b border-border pb-5">
        <div>
          <p className="mb-3 font-mono text-[10px] uppercase tracking-[0.2em] text-accent">02 / Selected work</p>
          <h2 className="text-4xl font-medium tracking-[-0.06em] text-text-primary md:text-6xl">Evidence of impact.</h2>
        </div>
        <Link href="/work" className="hidden text-sm text-text-secondary transition-colors hover:text-accent sm:block">
          View all work →
        </Link>
      </div>

      {featured && (
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ duration: 0.6 }}>
          <Link href={`/projects/${featured.slug}`} className="group relative block overflow-hidden rounded-[2rem] bg-surface-secondary p-6 transition-transform duration-500 hover:-translate-y-1 md:p-10 lg:p-14">
            <div className="absolute right-0 top-0 h-48 w-48 rounded-full bg-accent/10 blur-3xl transition-transform duration-700 group-hover:scale-150" />
            <div className="relative grid gap-12 lg:grid-cols-[1fr_auto] lg:items-end">
              <div>
                <div className="mb-16 flex items-center justify-between font-mono text-[10px] uppercase tracking-[0.16em] text-text-muted">
                  <span>Featured case study</span>
                  <span>{featured.status}</span>
                </div>
                <p className="font-mono text-xs uppercase tracking-[0.16em] text-accent">{featured.title}</p>
                <h3 className="mt-4 max-w-3xl text-3xl font-medium leading-tight tracking-[-0.05em] text-text-primary md:text-5xl">{featured.tagline}</h3>
                <p className="mt-6 max-w-xl text-sm leading-relaxed text-text-secondary">{featured.problem}</p>
                <p className="mt-8 font-mono text-[10px] uppercase tracking-[0.12em] text-text-muted">{featured.stack.join(" · ")}</p>
              </div>
              <div className="flex items-end justify-between gap-8 lg:block lg:text-right">
                <div>
                  <p className="text-4xl font-medium tracking-[-0.06em] text-text-primary">{featured.metric.value}</p>
                  <p className="mt-1 max-w-40 font-mono text-[10px] uppercase leading-relaxed text-text-muted lg:ml-auto">{featured.metric.label}</p>
                </div>
                <span className="text-2xl text-accent transition-transform duration-300 group-hover:translate-x-2">→</span>
              </div>
            </div>
          </Link>
        </motion.div>
      )}

      <div className="mt-4 grid grid-cols-1 gap-4 md:grid-cols-2">
        {secondary.map((project, index) => (
          <motion.div
            key={project.slug}
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: index * 0.1 }}
          >
            <Link href={`/projects/${project.slug}`} className="group rounded-[1.75rem] border border-border p-6 transition-all duration-300 hover:-translate-y-1 hover:border-accent hover:bg-surface-secondary md:p-8">
              <div className="flex items-start justify-between gap-4">
                <span className="font-mono text-[10px] text-text-muted">0{index + 2} / {project.status}</span>
                <span className="text-xl text-text-muted transition-colors group-hover:text-accent">→</span>
              </div>
              <h3 className="mt-16 text-2xl font-medium tracking-[-0.04em] text-text-primary">{project.title}</h3>
              <p className="mt-3 max-w-md text-sm leading-relaxed text-text-secondary">{project.tagline}</p>
              <div className="mt-8 flex items-end justify-between gap-4 border-t border-border pt-4">
                <span className="font-mono text-[10px] uppercase text-text-muted">{project.stack.slice(0, 2).join(" · ")}</span>
                <span className="font-mono text-xs font-medium text-accent">{project.metric.value}</span>
              </div>
            </Link>
          </motion.div>
        ))}
      </div>
    </section>
  );
}
