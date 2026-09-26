"use client";

import { useTheme } from "next-themes";
import { useEffect, useState } from "react";

// Compact icon control cycling Light -> Dark -> System.
// Spec explicitly rules out a plain "Dark / Light" label switch (section 11).
const MODES = ["light", "dark", "system"] as const;
type Mode = (typeof MODES)[number];

const ICON: Record<Mode, string> = {
  light: "○",
  dark: "●",
  system: "◐",
};

const LABEL: Record<Mode, string> = {
  light: "Light theme",
  dark: "Dark theme",
  system: "System theme",
};

export function ThemeSwitcher() {
  const { theme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);

  // Avoid hydration mismatch: theme is only known client-side.
  // This is the standard next-themes mount-check pattern; the lint rule
  // flags any setState-in-effect generically, but there's no external
  // system to subscribe to here — mount itself is the "event."
  // eslint-disable-next-line react-hooks/set-state-in-effect
  useEffect(() => setMounted(true), []);

  const current = (mounted ? (theme as Mode) : "system") ?? "system";

  function cycle() {
    const idx = MODES.indexOf(current);
    const next = MODES[(idx + 1) % MODES.length];
    setTheme(next);
  }

  return (
    <button
      onClick={cycle}
      aria-label={`Theme: ${LABEL[current]}. Click to change.`}
      title={LABEL[current]}
      className="flex h-8 w-8 items-center justify-center rounded-full border border-border text-sm text-text-secondary transition-colors hover:border-accent hover:text-accent"
    >
      <span aria-hidden="true">{ICON[current]}</span>
    </button>
  );
}
