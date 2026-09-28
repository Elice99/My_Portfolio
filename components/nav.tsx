"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { ThemeSwitcher } from "@/components/theme-switcher";

const LINKS = [
  { href: "/work", label: "Work" },
  { href: "/about", label: "About" },
  { href: "/experience", label: "Experience" },
  { href: "/capabilities", label: "Capabilities" },
  { href: "/now", label: "Now" },
];

export function Nav() {
  const [compact, setCompact] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);

  useEffect(() => {
    function onScroll() {
      setCompact(window.scrollY > 32);
    }
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <header
      className={`sticky top-0 z-50 px-4 pt-4 transition-all duration-300 sm:px-6 lg:px-10 ${compact ? "pt-3" : "pt-5"}`}
    >
      <div className="mx-auto flex max-w-[1440px] items-center justify-between rounded-full border border-border/80 bg-background/80 px-4 py-3 shadow-sm backdrop-blur-xl sm:px-5">
        <Link href="/" className="group flex items-center gap-2 font-mono text-xs tracking-[0.18em] text-text-primary">
          <span className="h-2 w-2 rounded-full bg-accent transition-transform group-hover:scale-150" />
          ELISHA BASSEY
        </Link>

        <nav className="hidden items-center gap-6 md:flex">
          {LINKS.map((link) => (
            <Link key={link.href} href={link.href} className="text-xs text-text-secondary transition-colors hover:text-accent">
              {link.label}
            </Link>
          ))}
        </nav>

        <div className="flex items-center gap-3">
          <Link href="/contact" className="hidden rounded-full bg-text-primary px-4 py-2 text-xs font-medium text-background transition-transform hover:-translate-y-0.5 sm:inline-flex">
            Let&apos;s talk <span className="ml-2">↗</span>
          </Link>
          <ThemeSwitcher />
          <button
            onClick={() => setMenuOpen((open) => !open)}
            className="rounded-full border border-border px-3 py-2 text-xs text-text-primary md:hidden"
            aria-label="Toggle menu"
            aria-expanded={menuOpen}
          >
            {menuOpen ? "CLOSE" : "MENU"}
          </button>
        </div>
      </div>

      {menuOpen && (
        <nav className="mx-auto mt-2 max-w-[1440px] rounded-3xl border border-border bg-surface-primary p-5 shadow-lg md:hidden">
          <div className="grid gap-1">
            {LINKS.map((link) => (
              <Link key={link.href} href={link.href} onClick={() => setMenuOpen(false)} className="rounded-xl px-3 py-3 text-sm text-text-secondary hover:bg-surface-secondary hover:text-text-primary">
                {link.label}
              </Link>
            ))}
            <Link href="/contact" onClick={() => setMenuOpen(false)} className="mt-2 rounded-xl bg-text-primary px-3 py-3 text-center text-sm text-background">
              Let&apos;s talk ↗
            </Link>
          </div>
        </nav>
      )}
    </header>
  );
}
