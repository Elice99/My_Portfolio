"use client";

import { motion, useMotionValue, useSpring } from "motion/react";
import { useEffect, useState } from "react";

// Two-part cursor: a precise dot and a lagging ring that swells over anything
// clickable. Only enabled for fine pointers with motion allowed, so touch and
// reduced-motion visitors keep their native cursor.
export function Cursor() {
  const [enabled, setEnabled] = useState(false);
  const [hovering, setHovering] = useState(false);
  const [pressed, setPressed] = useState(false);
  const [label, setLabel] = useState<string | null>(null);

  const x = useMotionValue(-100);
  const y = useMotionValue(-100);
  const ringX = useSpring(x, { stiffness: 350, damping: 30, mass: 0.6 });
  const ringY = useSpring(y, { stiffness: 350, damping: 30, mass: 0.6 });

  useEffect(() => {
    const fine = window.matchMedia("(pointer: fine)").matches;
    const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (!fine || reduced) return;

    setEnabled(true);
    document.documentElement.classList.add("has-custom-cursor");

    function onMove(e: PointerEvent) {
      x.set(e.clientX);
      y.set(e.clientY);
      const target = (e.target as HTMLElement | null)?.closest<HTMLElement>(
        "a, button, input, textarea, select, label, [data-cursor]",
      );
      setHovering(Boolean(target));
      setLabel(target?.dataset.cursor ?? null);
    }
    const onDown = () => setPressed(true);
    const onUp = () => setPressed(false);
    const onLeave = () => {
      x.set(-100);
      y.set(-100);
    };

    window.addEventListener("pointermove", onMove);
    window.addEventListener("pointerdown", onDown);
    window.addEventListener("pointerup", onUp);
    document.addEventListener("pointerleave", onLeave);
    return () => {
      document.documentElement.classList.remove("has-custom-cursor");
      window.removeEventListener("pointermove", onMove);
      window.removeEventListener("pointerdown", onDown);
      window.removeEventListener("pointerup", onUp);
      document.removeEventListener("pointerleave", onLeave);
    };
  }, [x, y]);

  if (!enabled) return null;

  const ringSize = label ? 84 : hovering ? 52 : 32;

  return (
    <>
      <motion.div
        aria-hidden
        className="pointer-events-none fixed left-0 top-0 z-[200] h-1.5 w-1.5 rounded-full bg-accent"
        style={{ x, y, translateX: "-50%", translateY: "-50%" }}
      />
      <motion.div
        aria-hidden
        className="pointer-events-none fixed left-0 top-0 z-[199] flex items-center justify-center rounded-full border border-accent/70 font-mono text-[9px] uppercase tracking-[0.18em] text-background"
        style={{ x: ringX, y: ringY, translateX: "-50%", translateY: "-50%" }}
        animate={{
          width: ringSize,
          height: ringSize,
          scale: pressed ? 0.85 : 1,
          backgroundColor: label ? "var(--accent)" : hovering ? "color-mix(in srgb, var(--accent) 12%, transparent)" : "rgba(0,0,0,0)",
        }}
        transition={{ type: "spring", stiffness: 300, damping: 24 }}
      >
        {label}
      </motion.div>
    </>
  );
}
