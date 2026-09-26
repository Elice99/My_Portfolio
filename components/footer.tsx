import Link from "next/link";

const LINKS = [
  { href: "/work", label: "WORK" },
  { href: "/about", label: "ABOUT" },
  { href: "/resume", label: "RESUME" },
  { href: "https://github.com/Elice99", label: "GITHUB" },
  { href: "https://linktr.ee/elice99", label: "LINKEDIN" },
  { href: "/contact", label: "CONTACT" },
];

export function Footer() {
  return (
    <footer className="mt-auto border-t border-border">
      <div className="mx-auto max-w-[1440px] px-5 py-12 md:px-10 lg:px-16">
        <p className="font-mono text-technical text-text-muted">
          ELISHA BASSEY
        </p>
        <p className="mt-3 max-w-sm text-text-secondary">
          I build systems that turn messy data into useful decisions.
        </p>

        <nav className="mt-8 flex flex-wrap gap-x-6 gap-y-2">
          {LINKS.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              className="font-mono text-technical text-text-secondary transition-colors hover:text-accent"
            >
              {link.label}
            </Link>
          ))}
        </nav>

        <div className="mt-10 flex flex-col gap-2 border-t border-border pt-6 font-mono text-technical text-text-muted md:flex-row md:items-center md:justify-between">
          <span>© {new Date().getFullYear()} Elisha Bassey</span>
          <span className="flex items-center gap-2">
            SYSTEM STATUS <span className="text-accent">● ONLINE</span>
          </span>
        </div>
      </div>
    </footer>
  );
}
