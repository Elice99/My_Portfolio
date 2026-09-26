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

  useEffect(() => {
    function onScroll() {
      setCompact(window.scrollY > 40);
    }
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <header
      className={`sticky top-0 z-50 border-b border-border bg-background/90 backdrop-blur transition-[padding] duration-300 ${
        compact ? "py-3" : "py-6"
      }`}
    >
      <div className="mx-auto flex max-w-[1440px] items-center justify-between px-5 md:px-10 lg:px-16">
        <Link
          href="/"
          className="font-mono text-sm tracking-wide text-text-primary"
        >
          ELISHA BASSEY
        </Link>

        <nav className="hidden items-center gap-8 md:flex">
          {LINKS.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              className="text-sm text-text-secondary transition-colors hover:text-accent"
            >
              {link.label}
            </Link>
          ))}
        </nav>

        <div className="hidden items-center gap-6 md:flex">
          <Link
            href="/resume"
            className="text-sm text-text-secondary transition-colors hover:text-accent"
          >
            CV
          </Link>
          <Link
            href="/contact"
            className="text-sm text-text-secondary transition-colors hover:text-accent"
          >
            Contact
          </Link>
          <ThemeSwitcher />
        </div>

        {/* Mobile: hamburger placeholder — command palette / drawer wired up later */}
        <button
          className="text-text-primary md:hidden"
          aria-label="Open menu"
        >
          <span aria-hidden="true">☰</span>
        </button>
      </div>
    </header>
  );
}
