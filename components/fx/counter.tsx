"use client";

import { animate, useInView } from "motion/react";
import { useEffect, useRef, useState } from "react";

// Counts up to the numeric part of a value ("₦652.6M", "8,300", "R² 0.4553")
// while keeping any prefix/suffix. Non-numeric values render as-is.
export function Counter({ value, className }: { value: string; className?: string }) {
  const ref = useRef<HTMLSpanElement>(null);
  const inView = useInView(ref, { once: true, margin: "-60px" });
  const match = value.match(/^(.*?)(\d[\d,]*(?:\.\d+)?)(.*)$/);
  const [display, setDisplay] = useState(value);

  useEffect(() => {
    if (!match) return;
    const [, prefix, num, suffix] = match;
    const target = parseFloat(num.replace(/,/g, ""));
    const decimals = num.includes(".") ? num.split(".")[1].length : 0;
    const grouped = num.includes(",");
    const format = (n: number) =>
      prefix + (grouped ? n.toLocaleString("en-US", { minimumFractionDigits: decimals, maximumFractionDigits: decimals }) : n.toFixed(decimals)) + suffix;

    if (!inView) {
      setDisplay(format(0));
      return;
    }
    const controls = animate(0, target, { duration: 1.4, ease: [0.16, 1, 0.3, 1], onUpdate: (n) => setDisplay(format(n)) });
    return () => controls.stop();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [inView, value]);

  return (
    <span ref={ref} className={className}>
      {display}
    </span>
  );
}
