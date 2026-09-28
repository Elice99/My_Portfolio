"use client";

import { useEffect, useRef, useState } from "react";
import { motion, useInView } from "motion/react";
import Link from "next/link";
import { projects } from "@/data/projects";

// Only show verified projects here — placeholders (GlowMart, Golden Wok)
// stay out until real numbers are added, per the "no fake statistics" rule.
const evidence = projects.filter((p) => p.verified);

function AnimatedMetric({ value }: { value: string }) {
  const ref = useRef(null);
  const inView = useInView(ref, { once: true, margin: "-100px" });
  const isNumeric = /^[\d,]+$/.test(value);
  const [display, setDisplay] = useState(isNumeric ? "0" : value);

  useEffect(() => {
    if (!inView || !isNumeric) return;
    const target = parseInt(value.replace(/,/g, ""), 10);
    const duration = 900;
    const start = performance.now();

    function tick(now: number) {
      const progress = Math.min((now - start) / duration, 1);
      const current = Math.round(target * progress);
      setDisplay(current.toLocaleString());
      if (progress < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }, [inView, isNumeric, value]);

  return (
    <span
      ref={ref}
      className="font-mono text-text-primary"
      style={{ fontSize: "var(--text-h2)" }}
    >
      {display}
    </span>
  );
}

export function EvidenceSection() {
  return (
    <section className="mx-auto max-w-[1440px] px-5 py-16 md:px-10 lg:px-16 lg:py-24">
      <h2
        className="font-sans tracking-tight text-text-primary"
        style={{ fontSize: "var(--text-h2)" }}
      >
        Evidence
      </h2>
      <p className="mt-4 max-w-lg text-text-secondary">
        Okay, but what has he actually done?
      </p>

      <div className="mt-12 grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4">
        {evidence.map((project, i) => (
          <motion.div
            key={project.slug}
            initial={{ opacity: 0, y: 10 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-80px" }}
            transition={{ duration: 0.4, delay: i * 0.08 }}
          >
            <Link href={`/projects/${project.slug}`} className="group block">
              <AnimatedMetric value={project.metric.value} />
              <p className="mt-1 font-mono text-technical text-text-muted transition-colors group-hover:text-accent">
                {project.metric.label}
              </p>
            </Link>
          </motion.div>
        ))}
      </div>
    </section>
  );
}
