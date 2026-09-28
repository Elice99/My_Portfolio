import { getProject } from "@/data/projects";
import { notFound } from "next/navigation";
import Link from "next/link";
import { CaseStudyHero } from "@/components/case-study-hero";
import { CaseStudyContent } from "@/components/case-study-content";

export default function ProjectPage({ params }: { params: { slug: string } }) {
  const project = getProject(params.slug);

  if (!project) {
    notFound();
  }

  return (
    <main>
      <CaseStudyHero project={project} />
      <CaseStudyContent project={project} />
    </main>
  );
}
