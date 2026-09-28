export function CtaSection() {
  return (
    <section className="mx-auto max-w-[1440px] px-5 py-20 md:px-10 lg:px-16 lg:py-28">
      <div className="rounded-[2rem] border border-border bg-gradient-to-br from-accent/10 via-surface-primary to-surface-secondary p-8 md:p-12">
        <div className="flex flex-col gap-8 md:flex-row md:items-end md:justify-between">
          <div className="max-w-2xl">
            <p className="font-mono text-[10px] uppercase tracking-[0.2em] text-accent">Let’s work together</p>
            <h2 className="mt-4 text-3xl font-medium tracking-[-0.06em] text-text-primary md:text-5xl">
              Need a data-minded analyst who can build decisions, not just reports?
            </h2>
          </div>

          <div className="flex flex-col gap-3 sm:flex-row">
            <a href="mailto:elicexy@gmail.com" className="inline-flex items-center justify-center rounded-full bg-text-primary px-6 py-3 text-sm font-medium text-background transition-transform hover:-translate-y-0.5">
              Email me
            </a>
            <a href="https://github.com/Elice99" target="_blank" rel="noopener noreferrer" className="inline-flex items-center justify-center rounded-full border border-border px-6 py-3 text-sm font-medium text-text-primary transition-colors hover:border-accent hover:text-accent">
              GitHub
            </a>
          </div>
        </div>
      </div>
    </section>
  );
}
