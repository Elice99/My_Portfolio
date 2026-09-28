"use client";

import { motion } from "motion/react";
import { Project } from "@/data/projects";
import Link from "next/link";
import { useEffect, useRef, useState } from "react";

const projectDetails: Record<string, any> = {
  "trustlake": {
    problem: "Data quality issues can silently damage downstream decisions. Organizations struggle to validate data without clear, explainable frameworks. How do you know if your data is trustworthy before you make critical business decisions?",
    dataEvidence: [
      { label: "Current Status", value: "Pre-MVP (Stage 0)" },
      { label: "Focus Area", value: "Environment & Project Foundations" },
      { label: "Trust Dimensions", value: "Completeness, Uniqueness, Consistency, Freshness" },
      { label: "Philosophy", value: "Rules Decide. AI Explains. Humans Approve." },
    ],
    approach: "Building a deterministic data trust engine that scores datasets on a 0–100 Trust Score and explains findings in plain English. The system uses explicit validation rules (not AI arbitrarily deciding), then uses AI to explain recommendations.",
    findings: "Still in development. The core principle is that AI should enhance human decision-making, not replace it. Deterministic rules provide consistency; AI provides explainability.",
    techStack: ["FastAPI", "PostgreSQL", "Python", "Pydantic", "React/Next.js", "TypeScript", "Tailwind CSS", "Docker Compose"],
    features: [
      "CSV data ingestion",
      "PostgreSQL read-only connectors",
      "Multi-dimensional trust scoring (4 core dimensions)",
      "AI-powered explanations (Gemini 2.5 Flash / Groq)",
      "Human approval workflows",
      "Audit logging",
    ],
    learnings: "Data quality is foundational. Too many organizations focus on dashboards without ensuring the underlying data is trustworthy. This project exists because I believe that conversation needs to happen first.",
    nextSteps: [
      "Complete Docker Compose setup",
      "Implement FastAPI backend",
      "Build React frontend",
      "Deploy V1 MVP to production",
    ],
    links: [
      { label: "GitHub Repository", href: "https://github.com/Elice99/TrustLake" },
    ],
  },
  "sales-pipeline-prediction": {
    problem: "Sales teams lack visibility into deal outcomes. CRM data sits unused. How do you allocate resources to deals most likely to close? Which factors actually predict success? Without predictive capability, sales forecasts rely on intuition rather than evidence.",
    dataEvidence: [
      { label: "Total Records", value: "8,300 deals" },
      { label: "Training Dataset", value: "6,711 closed deals (80%)" },
      { label: "Test Dataset", value: "1,589 active deals (20%)" },
      { label: "Features Engineered", value: "50 (8 categorical + 42 numerical)" },
      { label: "Data Quality", value: "SQL Server CRM extract, cleaned & validated" },
    ],
    approach: "Extracted deal history from SQL Server CRM, engineered 50 features capturing agent performance, deal characteristics, temporal patterns, and interaction effects. Built and compared Linear Regression, Random Forest, and XGBoost models. Selected XGBoost based on cross-validation performance and deployed via FastAPI.",
    findings: {
      metric: "ROC-AUC: 0.6482",
      detail: "Model discriminates between won and lost deals better than random chance. Identifies high-probability opportunities that deserve attention.",
    },
    performanceMetrics: [
      { label: "ROC-AUC", value: "0.6482" },
      { label: "Accuracy", value: "58.38%" },
      { label: "Precision", value: "70.37%" },
      { label: "Recall", value: "61.88%" },
      { label: "F1-Score", value: "0.6585" },
    ],
    topFeatures: [
      "Deal Age (9.2%)",
      "Velocity Complexity Index (4.7%)",
      "Days Into Year (4.3%)",
      "Sales Velocity Ratio (4.1%)",
      "Is Quarter End (4.0%)",
    ],
    techStack: ["Python", "XGBoost", "scikit-learn", "FastAPI", "PostgreSQL", "Docker", "Uvicorn"],
    businessImplication: "A sales manager can now input deal characteristics and receive a real-time probability score. Sales teams can prioritize follow-ups on deals predicted to close. Forecast accuracy improves. Resource allocation becomes data-driven.",
    learnings: "Temporal features matter more than we think. When a deal enters the pipeline, what quarter it is, how many days remain in the year—these patterns are stronger predictors than agent experience alone. Also learned that high precision (correct when predicting WIN) is more valuable than raw accuracy.",
    apiEndpoint: {
      url: "https://sales-pipeline-api.onrender.com/predict",
      method: "POST",
      example: {
        "sales_agent": "john_smith",
        "product": "gtx_basic",
        "account": "acme_corporation",
        "sector": "finance",
        "deal_age": 45,
      },
    },
    links: [
      { label: "GitHub Repository", href: "https://github.com/Elice99/Sales-Pipeline-Prediction-Model" },
      { label: "Live API (Render)", href: "https://sales-pipeline-api.onrender.com/docs" },
    ],
  },
  "glowmart": {
    problem: "A disagreement erupted between Sales and Inventory managers at GlowMart Nigeria. Sales blamed inventory allocation for poor performance. Inventory claimed allocation was fair. Without data, management was stuck. Who was right? What was actually driving business performance?",
    businessContext: "GlowMart Nigeria Ltd — FMCG retailer operating across 5 cities (Abuja, Ibadan, Kano, Lagos, Port Harcourt). Three years of sales data. 500 customers. 15,000 transactions.",
    dataEvidence: [
      { label: "Analysis Period", value: "2022 – 2024" },
      { label: "Total Transactions", value: "15,000" },
      { label: "Total Customers", value: "500" },
      { label: "Total Revenue", value: "₦652.6 Million" },
      { label: "Gross Profit", value: "₦180.4 Million" },
      { label: "Data Quality", value: "Cleaned with Power Query, modeled in Power Pivot" },
    ],
    investigation: {
      question: "Is inventory allocation fair?",
      method: "Compared Revenue Share vs Customer Share across all 5 cities",
      finding: "Maximum variance: 0.3%. Revenue distribution closely mirrored customer distribution. Inventory allocation was already balanced.",
    },
    realIssues: [
      "Revenue declined 0.5% in 2023. Growth recovered only 1.6% in 2024 (below 5% target).",
      "Abuja is the only city showing negative YoY growth.",
      "₦72.4M spent on discounts produced little measurable return on Average Order Value.",
      "Brand performance varied significantly despite similar city-level demand.",
    ],
    techStack: ["Excel", "Power Query", "Power Pivot", "PivotTables", "PivotCharts", "Conditional Formatting"],
    dashboards: [
      { name: "Executive Overview", purpose: "Resolve the inventory dispute with evidence" },
      { name: "Brand & City Deep Dive", purpose: "Explore real drivers of business performance" },
      { name: "Customer & Efficiency", purpose: "Identify actionable improvement opportunities" },
    ],
    keyMetrics: [
      { label: "Total Revenue", value: "₦652.6M" },
      { label: "Gross Profit", value: "₦180.4M (27.6% margin)" },
      { label: "Average Order Value", value: "₦43,507" },
      { label: "Discount Rate", value: "11.1% of revenue" },
    ],
    businessImplication: "The analysis proved that operational issues were not an inventory problem. Instead of redistributing stock, management should focus on pricing strategy, customer acquisition, and city-specific performance improvement. Discount spending should be re-evaluated based on ROI.",
    learnings: "Great dashboards don't just show what happened—they answer the question nobody else could answer with certainty. This project taught me that 'proving someone wrong' with data requires neutrality and complete evidence. Also learned that business disagreements often mask deeper issues.",
    links: [
      { label: "GitHub Repository", href: "https://github.com/Elice99/glowmart-sales-inventory-dashboard" },
    ],
  },
};

export function CaseStudyContent({ project }: { project: Project }) {
  const details = projectDetails[project.slug];
  const [scrollProgress, setScrollProgress] = useState(0);

  useEffect(() => {
    function handleScroll() {
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const scrolled = window.scrollY / docHeight;
      setScrollProgress(scrolled);
    }
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  if (!details) {
    return (
      <section className="mx-auto max-w-[1440px] px-5 py-24 md:px-10 lg:px-16">
        <p className="text-text-secondary">Case study coming soon.</p>
      </section>
    );
  }

  return (
    <section className="mx-auto max-w-[1440px] px-5 py-16 md:px-10 lg:px-16 lg:py-24">
      {/* Progress bar */}
      <motion.div className="fixed left-0 top-0 h-1 bg-accent" style={{ width: `${scrollProgress * 100}%` }} />

      {/* Problem Section */}
      <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ duration: 0.6 }} className="mb-20 border-b border-border pb-12">
        <div className="mb-6 inline-flex items-center gap-2 rounded-full bg-accent/10 px-4 py-2">
          <span className="h-2 w-2 rounded-full bg-accent" />
          <span className="font-mono text-[10px] uppercase text-accent">The Problem</span>
        </div>
        <h2 className="mb-6 text-3xl font-medium tracking-[-0.05em] text-text-primary md:text-4xl">{project.title === "TrustLake" ? "Data Quality Without Trust" : project.title === "Sales Pipeline Prediction" ? "Invisible Deal Outcomes" : "Breaking the Deadlock"}</h2>
        <p className="max-w-2xl text-lg leading-relaxed text-text-secondary">{details.problem}</p>
        {details.businessContext && <p className="mt-4 text-sm text-text-muted">{details.businessContext}</p>}
      </motion.div>

      {/* Data Evidence */}
      <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ duration: 0.6, delay: 0.1 }} className="mb-20 border-b border-border pb-12">
        <div className="mb-6 inline-flex items-center gap-2 rounded-full bg-accent/10 px-4 py-2">
          <span className="h-2 w-2 rounded-full bg-accent" />
          <span className="font-mono text-[10px] uppercase text-accent">The Data</span>
        </div>
        <h2 className="mb-8 text-3xl font-medium tracking-[-0.05em] text-text-primary md:text-4xl">Evidence & Scale</h2>
        <div className="grid gap-4 sm:grid-cols-2 md:grid-cols-3">
          {details.dataEvidence.map((item: any, idx: number) => (
            <motion.div key={idx} initial={{ opacity: 0, y: 10 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ delay: idx * 0.05 }} className="rounded-lg border border-border bg-surface-secondary/30 p-4">
              <p className="font-mono text-[10px] uppercase text-text-muted">{item.label}</p>
              <p className="mt-2 text-xl font-medium text-accent">{item.value}</p>
            </motion.div>
          ))}
        </div>
      </motion.div>

      {/* Approach */}
      <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ duration: 0.6, delay: 0.1 }} className="mb-20 border-b border-border pb-12">
        <div className="mb-6 inline-flex items-center gap-2 rounded-full bg-accent/10 px-4 py-2">
          <span className="h-2 w-2 rounded-full bg-accent" />
          <span className="font-mono text-[10px] uppercase text-accent">The Approach</span>
        </div>
        <h2 className="mb-6 text-3xl font-medium tracking-[-0.05em] text-text-primary md:text-4xl">Methodology</h2>
        <p className="max-w-3xl text-lg leading-relaxed text-text-secondary">{details.approach}</p>
      </motion.div>

      {/* Performance Metrics */}
      {details.performanceMetrics && (
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ duration: 0.6, delay: 0.1 }} className="mb-20 border-b border-border pb-12">
          <div className="mb-6 inline-flex items-center gap-2 rounded-full bg-accent/10 px-4 py-2">
            <span className="h-2 w-2 rounded-full bg-accent" />
            <span className="font-mono text-[10px] uppercase text-accent">Model Performance</span>
          </div>
          <h2 className="mb-8 text-3xl font-medium tracking-[-0.05em] text-text-primary md:text-4xl">Results & Metrics</h2>
          <div className="grid gap-6 sm:grid-cols-2 md:grid-cols-3">
            {details.performanceMetrics.map((metric: any, idx: number) => (
              <motion.div key={idx} initial={{ opacity: 0, scale: 0.95 }} whileInView={{ opacity: 1, scale: 1 }} viewport={{ once: true }} transition={{ delay: idx * 0.08 }} className="rounded-lg border border-border/50 bg-gradient-to-br from-accent/5 to-transparent p-6">
                <p className="font-mono text-xs uppercase text-text-muted">{metric.label}</p>
                <p className="mt-3 text-4xl font-bold text-accent">{metric.value}</p>
              </motion.div>
            ))}
          </div>
          {details.topFeatures && (
            <div className="mt-12">
              <h3 className="mb-4 text-lg font-medium text-text-primary">Top Feature Importance</h3>
              <div className="space-y-2">
                {details.topFeatures.map((feature: string, idx: number) => (
                  <motion.div key={idx} initial={{ opacity: 0, x: -10 }} whileInView={{ opacity: 1, x: 0 }} viewport={{ once: true }} transition={{ delay: idx * 0.05 }} className="flex items-center gap-3 text-sm text-text-secondary">
                    <span className="h-1 w-1 rounded-full bg-accent" />
                    {feature}
                  </motion.div>
                ))}
              </div>
            </div>
          )}
        </motion.div>
      )}

      {/* Tech Stack */}
      <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ duration: 0.6, delay: 0.1 }} className="mb-20 border-b border-border pb-12">
        <div className="mb-6 inline-flex items-center gap-2 rounded-full bg-accent/10 px-4 py-2">
          <span className="h-2 w-2 rounded-full bg-accent" />
          <span className="font-mono text-[10px] uppercase text-accent">Built With</span>
        </div>
        <h2 className="mb-6 text-3xl font-medium tracking-[-0.05em] text-text-primary md:text-4xl">Technology Stack</h2>
        <div className="flex flex-wrap gap-2">
          {details.techStack.map((tech: string, idx: number) => (
            <motion.div key={idx} initial={{ opacity: 0 }} whileInView={{ opacity: 1 }} viewport={{ once: true }} transition={{ delay: idx * 0.03 }} className="rounded-full border border-accent/30 bg-accent/5 px-4 py-2 font-mono text-sm text-accent">
              {tech}
            </motion.div>
          ))}
        </div>
      </motion.div>

      {/* Key Learnings */}
      <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ duration: 0.6, delay: 0.1 }} className="mb-20 border-b border-border pb-12">
        <div className="mb-6 inline-flex items-center gap-2 rounded-full bg-accent/10 px-4 py-2">
          <span className="h-2 w-2 rounded-full bg-accent" />
          <span className="font-mono text-[10px] uppercase text-accent">Lessons</span>
        </div>
        <h2 className="mb-6 text-3xl font-medium tracking-[-0.05em] text-text-primary md:text-4xl">What I Learned</h2>
        <div className="max-w-3xl space-y-4 rounded-lg border border-border/30 bg-surface-secondary/20 p-6">
          <p className="text-lg leading-relaxed text-text-secondary">{details.learnings}</p>
        </div>
      </motion.div>

      {/* Links */}
      <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ duration: 0.6, delay: 0.1 }}>
        <div className="mb-6 inline-flex items-center gap-2 rounded-full bg-accent/10 px-4 py-2">
          <span className="h-2 w-2 rounded-full bg-accent" />
          <span className="font-mono text-[10px] uppercase text-accent">Explore</span>
        </div>
        <div className="flex flex-wrap gap-4">
          {details.links.map((link: any, idx: number) => (
            <a key={idx} href={link.href} target="_blank" rel="noopener noreferrer" className="group inline-flex items-center gap-2 rounded-lg border border-accent/50 bg-accent/5 px-6 py-3 font-mono text-sm text-accent transition-all hover:border-accent hover:bg-accent/10">
              {link.label} <span className="transition-transform group-hover:translate-x-1">↗</span>
            </a>
          ))}
        </div>
      </motion.div>
    </section>
  );
}
