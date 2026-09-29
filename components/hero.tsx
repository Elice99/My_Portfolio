"use client";

import { motion } from "motion/react";
import Link from "next/link";

const EASE = [0.16, 1, 0.3, 1] as const;

export function Hero() {
  return (
    <section className="relative mx-auto grid min-h-[calc(100svh-88px)] max-w-[1440px] items-end gap-12 px-5 pb-16 pt-24 md:px-10 lg:grid-cols-12 lg:gap-8 lg:px-16 lg:pb-24">
      <div className="pointer-events-none absolute left-5 right-5 top-12 h-px bg-border/70 md:left-10 md:right-10 lg:left-16 lg:right-16" />
      <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.5, ease: EASE }} className="absolute left-5 top-5 font-mono text-[10px] tracking-[0.2em] text-text-muted md:left-10 lg:left-16">
        ANALYST / BUILDER / DECISION SUPPORT
      </motion.div>

      <div className="relative lg:col-span-8">
        <motion.p initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.5, ease: EASE }} className="mb-6 font-mono text-[11px] uppercase tracking-[0.2em] text-accent">
          Data analyst · BI analyst · Analytics systems
        </motion.p>
        <motion.h1 initial={{ opacity: 0, y: 18 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.75, delay: 0.12, ease: EASE }} className="max-w-5xl text-[clamp(3.8rem,10vw,10rem)] font-medium leading-[0.82] tracking-[-0.08em] text-text-primary">
          I turn messy<br /><span className="text-accent">data into</span><br />useful decisions.
        </motion.h1>
        <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.55, delay: 0.35, ease: EASE }} className="mt-10 max-w-xl space-y-6">
          <p className="text-base leading-relaxed text-text-secondary md:text-lg">
            I help teams make sense of complex information, validate the signal, and build the systems required to act on it.
          </p>
          <div className="flex flex-col gap-4 sm:flex-row sm:items-center">
            <Link href="/work" className="group inline-flex w-fit items-center gap-3 border-b border-text-primary pb-2 text-sm text-text-primary transition-colors hover:border-accent hover:text-accent">
              Explore selected work <span className="transition-transform group-hover:translate-x-1">↗</span>
            </Link>
            <Link href="/resume" className="group inline-flex w-fit items-center gap-3 rounded-full border border-border px-5 py-2 text-sm text-text-primary transition-colors hover:border-accent hover:text-accent">
              View CV
            </Link>
          </div>
        </motion.div>
      </div>

      <motion.div initial={{ opacity: 0, scale: 0.96 }} animate={{ opacity: 1, scale: 1 }} transition={{ duration: 0.8, delay: 0.25, ease: EASE }} className="relative hidden aspect-[4/5] overflow-hidden rounded-[2rem] bg-accent p-6 lg:col-span-4 lg:block">
        <div className="absolute -right-16 -top-16 h-64 w-64 rounded-full border border-background/30" />
        <div className="absolute -bottom-24 -left-12 h-72 w-72 rounded-full border border-background/30" />
        <div className="relative flex h-full flex-col justify-between text-background">
          <span className="font-mono text-[10px] tracking-[0.2em]">ELISHA BASSEY</span>
          <div>
            <p className="text-4xl font-medium leading-none tracking-[-0.06em]">DATA<br />TO<br />DECISIONS</p>
            <p className="mt-5 max-w-[13rem] text-sm leading-relaxed text-background/75">
              Analytics, BI, machine learning, and systems designed for clearer business action.
            </p>
          </div>
          <span className="font-mono text-[10px] tracking-[0.2em]">SCROLL TO EXPLORE ↓</span>
        </div>
      </motion.div>
    </section>
  );
}
