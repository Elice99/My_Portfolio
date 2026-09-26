"use client";

import { motion } from "motion/react";
import Link from "next/link";

// Entrance sequence per the wireframe doc:
// 1. small technical metadata  2. name resolves  3. large type enters
// 4. portrait reveals  5. subtle pass-through (handled by the accent line)
// This is the ONE orchestrated load moment for the whole site — everything
// else uses scroll-triggered reveals or hover, not autoplay animation.
const EASE = [0.16, 1, 0.3, 1] as const;

export function Hero() {
  return (
    <section className="relative mx-auto grid max-w-[1440px] grid-cols-1 items-center gap-12 px-5 py-16 md:px-10 lg:grid-cols-12 lg:gap-8 lg:px-16 lg:py-24">
      <div className="lg:col-span-7">
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5, ease: EASE }}
          className="font-mono text-technical text-text-muted"
        >
          DATA ANALYST → ANALYTICS ENGINEER
        </motion.p>

        <motion.h1
          initial={{ opacity: 0, y: 12 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.15, ease: EASE }}
          className="mt-4 font-sans leading-[0.95] tracking-tight text-text-primary"
          style={{ fontSize: "var(--text-display)" }}
        >
          DATA
          <br />
          BUSINESS
          <br />
          INTELLIGENCE
        </motion.h1>

        <motion.p
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.4, ease: EASE }}
          className="mt-8 max-w-md text-body-lg text-text-secondary"
          style={{ fontSize: "var(--text-body-lg)" }}
        >
          I build systems that turn messy data into useful decisions.
        </motion.p>

        <motion.div
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.55, ease: EASE }}
          className="mt-10 flex flex-wrap items-center gap-4"
        >
          <Link
            href="/work"
            className="group inline-flex items-center gap-2 rounded-full bg-accent px-6 py-3 text-sm font-medium text-background transition-transform hover:-translate-y-0.5"
          >
            Explore my work
            <span className="transition-transform group-hover:translate-x-0.5">
              →
            </span>
          </Link>
          <Link
            href="/resume"
            className="inline-flex items-center rounded-full border border-border px-6 py-3 text-sm text-text-primary transition-colors hover:border-accent hover:text-accent"
          >
            View CV
          </Link>
        </motion.div>
      </div>

      {/* Portrait — replace the placeholder surface with the real photo asset.
          Editorial rectangular crop per spec section 13/14, not a circular avatar. */}
      <motion.div
        initial={{ opacity: 0, scale: 0.98 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.7, delay: 0.3, ease: EASE }}
        className="relative aspect-[4/5] overflow-hidden rounded-sm border border-border bg-surface-secondary lg:col-span-5"
      >
        <div className="flex h-full w-full items-center justify-center">
          <span className="font-mono text-technical text-text-muted">
            PORTRAIT / 01
          </span>
        </div>
        <span className="absolute bottom-3 right-3 font-mono text-technical text-text-muted">
          01/04
        </span>
      </motion.div>
    </section>
  );
}
