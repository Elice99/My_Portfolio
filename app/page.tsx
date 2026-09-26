import { Hero } from "@/components/hero";
import { SystemSection } from "@/components/system-section";
import { SelectedWork } from "@/components/selected-work";

export default function Home() {
  return (
    <main>
      <Hero />
      <SystemSection />
      <SelectedWork />
      {/* Remaining Day 1 sections (What I Build, Career Journey, Currently
          Building, Portfolio Intelligence, final CTA) get added once the
          case-study template and remaining pages exist — see roadmap. */}
    </main>
  );
}
