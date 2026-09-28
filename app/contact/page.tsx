const LINKS = [
  { label: "Email me", href: "mailto:basseyelisha99@gmail.com" },
  { label: "GitHub", href: "https://github.com/Elice99" },
  { label: "Linktree", href: "https://linktr.ee/elice99" },
  { label: "Download CV", href: "/resume" },
];

export default function ContactPage() {
  return (
    <main className="mx-auto max-w-[1440px] px-5 py-16 md:px-10 lg:px-16 lg:py-24">
      <h1
        className="max-w-2xl font-sans tracking-tight text-text-primary"
        style={{ fontSize: "var(--text-h1)" }}
      >
        Have a problem worth solving?
      </h1>

      <div className="mt-12 flex flex-col gap-2">
        {LINKS.map((link) => (
          <a
            key={link.label}
            href={link.href}
            className="group flex items-center justify-between border-t border-border py-5 transition-colors hover:text-accent"
          >
            <span
              className="font-sans text-text-primary group-hover:text-accent"
              style={{ fontSize: "var(--text-h3)" }}
            >
              {link.label}
            </span>
            <span className="font-mono text-text-muted transition-transform group-hover:translate-x-1 group-hover:text-accent">
              →
            </span>
          </a>
        ))}
        <div className="border-t border-border" />
      </div>
    </main>
  );
}
