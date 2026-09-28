"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useTheme } from "next-themes";
import { projects } from "@/data/projects";

interface Item {
  label: string;
  action: () => void;
}

export function CommandPalette() {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState("");
  const router = useRouter();
  const { setTheme, theme } = useTheme();

  useEffect(() => {
    function onKeyDown(e: KeyboardEvent) {
      const isMod = e.metaKey || e.ctrlKey;
      if (isMod && e.key.toLowerCase() === "k") {
        e.preventDefault();
        setOpen((o) => !o);
      }
      if (e.key === "Escape") setOpen(false);
    }
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, []);

  if (!open) return null;

  const staticItems: Item[] = [
    { label: "About Elisha", action: () => router.push("/about") },
    { label: "Experience", action: () => router.push("/experience") },
    { label: "Capabilities", action: () => router.push("/capabilities") },
    { label: "Resume", action: () => router.push("/resume") },
    { label: "Now", action: () => router.push("/now") },
    { label: "Contact", action: () => router.push("/contact") },
    {
      label: "GitHub",
      action: () => window.open("https://github.com/Elice99", "_blank"),
    },
    {
      label: "LinkedIn",
      action: () => window.open("https://linktr.ee/elice99", "_blank"),
    },
    {
      label: `Toggle theme (currently ${theme ?? "system"})`,
      action: () =>
        setTheme(theme === "dark" ? "light" : theme === "light" ? "system" : "dark"),
    },
  ];

  const projectItems: Item[] = projects.map((p) => ({
    label: `Project: ${p.title}`,
    action: () => router.push(`/projects/${p.slug}`),
  }));

  const allItems = [...staticItems, ...projectItems];
  const filtered = allItems.filter((item) =>
    item.label.toLowerCase().includes(query.toLowerCase())
  );

  function run(item: Item) {
    item.action();
    setOpen(false);
    setQuery("");
  }

  return (
    <div
      className="fixed inset-0 z-[100] flex items-start justify-center bg-black/40 pt-24"
      onClick={() => setOpen(false)}
    >
      <div
        role="dialog"
        aria-label="Command palette"
        onClick={(e) => e.stopPropagation()}
        className="w-full max-w-lg rounded-sm border border-border bg-surface-elevated shadow-xl"
      >
        <input
          autoFocus
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search Elisha's portfolio"
          className="w-full border-b border-border bg-transparent px-4 py-4 font-mono text-technical text-text-primary outline-none placeholder:text-text-muted"
        />
        <div className="max-h-80 overflow-y-auto py-2">
          {filtered.length === 0 && (
            <p className="px-4 py-3 text-sm text-text-muted">No results</p>
          )}
          {filtered.map((item) => (
            <button
              key={item.label}
              onClick={() => run(item)}
              className="flex w-full items-center gap-2 px-4 py-2.5 text-left text-sm text-text-secondary transition-colors hover:bg-surface-secondary hover:text-accent"
            >
              <span aria-hidden="true">→</span>
              {item.label}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
