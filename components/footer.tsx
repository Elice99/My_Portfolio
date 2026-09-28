import Link from "next/link";

export function Footer() {
  return (
    <footer className="border-t border-border bg-surface-primary px-5 py-12 md:px-10 lg:px-16">
      <div className="mx-auto max-w-[1440px]">
        <div className="grid gap-12 md:grid-cols-4">
          <div>
            <p className="font-mono text-xs uppercase tracking-[0.2em] text-text-muted">Navigation</p>
            <nav className="mt-6 flex flex-col gap-3">
              <Link href="/" className="text-sm text-text-secondary hover:text-accent">
                Home
              </Link>
              <Link href="/work" className="text-sm text-text-secondary hover:text-accent">
                Work
              </Link>
              <Link href="/about" className="text-sm text-text-secondary hover:text-accent">
                About
              </Link>
              <Link href="/now" className="text-sm text-text-secondary hover:text-accent">
                Now
              </Link>
            </nav>
          </div>

          <div>
            <p className="font-mono text-xs uppercase tracking-[0.2em] text-text-muted">Socials</p>
            <div className="mt-6 flex flex-col gap-3">
              <a href="https://github.com/Elice99" target="_blank" rel="noopener noreferrer" className="text-sm text-text-secondary hover:text-accent">
                GitHub
              </a>
              <a href="https://linkedin.com/in/elisha-bassey" target="_blank" rel="noopener noreferrer" className="text-sm text-text-secondary hover:text-accent">
                LinkedIn
              </a>
              <a href="https://twitter.com/elice99" target="_blank" rel="noopener noreferrer" className="text-sm text-text-secondary hover:text-accent">
                Twitter
              </a>
            </div>
          </div>

          <div>
            <p className="font-mono text-xs uppercase tracking-[0.2em] text-text-muted">Contact</p>
            <div className="mt-6 flex flex-col gap-3">
              <a href="mailto:elicexy@gmail.com" className="text-sm text-text-secondary hover:text-accent">
                Email
              </a>
              <a href="https://calendly.com/elisha" target="_blank" rel="noopener noreferrer" className="text-sm text-text-secondary hover:text-accent">
                Calendar
              </a>
            </div>
          </div>

          <div>
            <p className="font-mono text-xs uppercase tracking-[0.2em] text-text-muted">Projects</p>
            <div className="mt-6 flex flex-col gap-3">
              <a href="/projects/trustlake" className="text-sm text-text-secondary hover:text-accent">
                TrustLake
              </a>
              <a href="/projects/sales-pipeline" className="text-sm text-text-secondary hover:text-accent">
                Sales Pipeline
              </a>
              <a href="/projects/glowmart" className="text-sm text-text-secondary hover:text-accent">
                GlowMart
              </a>
            </div>
          </div>
        </div>

        <div className="mt-12 border-t border-border pt-8">
          <div className="flex items-center justify-between">
            <p className="text-xs text-text-muted">© 2026 Elisha Bassey. All rights reserved.</p>
            <p className="font-mono text-[10px] text-text-muted">Built with Next.js + Tailwind + Motion</p>
          </div>
        </div>
      </div>
    </footer>
  );
}
