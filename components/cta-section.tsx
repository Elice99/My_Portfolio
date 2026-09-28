"use client";

import Link from "next/link";

export function CtaSection() {
  return (
    <section className="mx-auto max-w-[1440px] px-5 py-20 md:px-10 lg:px-16 lg:py-28">
      <div className="rounded-[2rem] border border-border bg-gradient-to-br from-accent/10 via-surface-primary to-surface-secondary p-8 md:p-12 lg:p-16">
        <div className="grid gap-8 lg:grid-cols-2 lg:items-center lg:gap-12">
          <div>
            <p className="font-mono text-[10px] uppercase tracking-[0.2em] text-accent">Get in touch</p>
            <h2 className="mt-4 text-4xl font-medium tracking-[-0.06em] text-text-primary md:text-5xl">Ready to work together?</h2>
            <p className="mt-6 max-w-xl text-lg leading-relaxed text-text-secondary">
              I'm interested in roles where analytical work connects directly to business outcomes. Let's talk about how data can inform better decisions.
            </p>
          </div>

          <div className="flex flex-col gap-3 sm:flex-row lg:flex-col">
            <a
              href="mailto:elicexy@gmail.com"
              className="inline-flex items-center justify-center rounded-full bg-text-primary px-6 py-3 text-sm font-medium text-background transition-transform hover:-translate-y-0.5"
            >
              Email me
            </a>
            <a
              href="https://github.com/Elice99"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center justify-center rounded-full border border-border px-6 py-3 text-sm font-medium text-text-primary transition-colors hover:border-accent hover:text-accent"
            >
              GitHub
            </a>
            <a
              href="https://www.linkedin.com/in/elisha-bassey"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center justify-center rounded-full border border-border px-6 py-3 text-sm font-medium text-text-primary transition-colors hover:border-accent hover:text-accent"
            >
              LinkedIn
            </a>
          </div>
        </div>
      </div>
    </section>
  );
}
