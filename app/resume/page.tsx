export default function ResumePage() {
  return (
    <main className="mx-auto max-w-[1440px] px-5 py-16 md:px-10 lg:px-16 lg:py-24">
      <div className="flex flex-col items-start justify-between gap-6 sm:flex-row sm:items-center">
        <h1
          className="font-sans tracking-tight text-text-primary"
          style={{ fontSize: "var(--text-h1)" }}
        >
          Resume
        </h1>
        {/* Elice: drop your real CV PDF into /public/documents/ and point
            this href at it, e.g. /documents/elisha-bassey-cv.pdf */}
        <a
          href="/documents/elisha-bassey-cv.pdf"
          className="group inline-flex items-center gap-2 rounded-full bg-accent px-6 py-3 text-sm font-medium text-background transition-transform hover:-translate-y-0.5"
        >
          Download PDF
          <span className="transition-transform group-hover:translate-x-0.5">
            →
          </span>
        </a>
      </div>

      <p className="mt-6 max-w-lg text-text-secondary">
        See the full breakdown on the{" "}
        <a href="/experience" className="text-accent underline">
          Experience
        </a>{" "}
        page, or download the recruiter-friendly PDF version above.
      </p>
    </main>
  );
}
