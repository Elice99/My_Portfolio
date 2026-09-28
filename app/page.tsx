import { Hero } from "@/components/hero";
import { SystemSection } from "@/components/system-section";
import { SelectedWork } from "@/components/selected-work";
import { EvidenceSection } from "@/components/evidence-section";
import { DecisionRoom } from "@/components/decision-room";
import { CareerJourney } from "@/components/career-journey";
import { CtaSection } from "@/components/cta-section";

export default function Home() {
  return (
    <main>
      <Hero />
      <SystemSection />
      <SelectedWork />
      <EvidenceSection />
      <DecisionRoom />
      <CareerJourney />
      <CtaSection />
    </main>
  );
}
