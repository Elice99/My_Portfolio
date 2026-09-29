"use client";

import { motion } from "motion/react";
import type { ReactNode } from "react";

export const EASE = [0.16, 1, 0.3, 1] as const;

// Fades and lifts content into place the first time it scrolls into view.
export function Reveal({ children, delay = 0, y = 24, className }: { children: ReactNode; delay?: number; y?: number; className?: string }) {
  return (
    <motion.div
      initial={{ opacity: 0, y }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-80px" }}
      transition={{ duration: 0.8, delay, ease: EASE }}
      className={className}
    >
      {children}
    </motion.div>
  );
}

// Splits a line of text into words that rise out of a mask one after another.
export function SplitReveal({ text, className, delay = 0, as = "h2" }: { text: string; className?: string; delay?: number; as?: "h1" | "h2" | "p" }) {
  const Tag = motion[as];
  const words = text.split(" ");
  return (
    <Tag
      className={className}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, margin: "-60px" }}
      transition={{ staggerChildren: 0.06, delayChildren: delay }}
      aria-label={text}
    >
      {words.map((word, i) => (
        <span key={i} aria-hidden className="inline-block overflow-hidden pb-[0.08em] align-bottom">
          <motion.span
            className="inline-block"
            variants={{ hidden: { y: "110%" }, visible: { y: "0%", transition: { duration: 0.8, ease: EASE } } }}
          >
            {word}
            {i < words.length - 1 ? " " : ""}
          </motion.span>
        </span>
      ))}
    </Tag>
  );
}
