export type ProjectStatus = "active" | "shipped" | "pre-mvp";
export type ProjectCategory =
  | "analytics"
  | "bi"
  | "ml"
  | "business"
  | "systems";

export interface Project {
  slug: string;
  title: string;
  category: ProjectCategory[];
  tagline: string;
  problem: string;
  stack: string[];
  metric: { value: string; label: string };
  status: ProjectStatus;
  featured: boolean;
  // Set to true once the two placeholder projects below have real,
  // verified figures. Do NOT fabricate numbers to fill this in —
  // per the design spec: "No fake statistics. No invented project results."
  verified: boolean;
}

export const projects: Project[] = [
  {
    slug: "trustlake",
    title: "TrustLake",
    category: ["systems", "analytics"],
    tagline: "Deterministic data validation with AI-assisted explanations.",
    problem:
      "Data quality issues can silently damage downstream decisions. TrustLake scores datasets on a deterministic Trust Score (0–100) and explains why in plain English.",
    stack: ["FastAPI", "PostgreSQL", "Python", "React/Next.js"],
    metric: { value: "0–100", label: "DETERMINISTIC TRUST SCORE" },
    status: "pre-mvp",
    featured: true,
    verified: true,
  },
  {
    slug: "sales-pipeline-prediction",
    title: "Sales Pipeline Prediction",
    category: ["ml", "business"],
    tagline: "XGBoost model predicting deal outcomes for a B2B sales team.",
    problem:
      "Built for SPOTA, a mid-sized B2B tech and manufacturing company, to flag which open deals are likely to close.",
    stack: ["XGBoost", "FastAPI", "Docker", "Render"],
    metric: { value: "8,300", label: "SALES PIPELINE RECORDS" },
    status: "shipped",
    featured: false,
    verified: true,
  },
  {
    slug: "airbnb-market-intelligence",
    title: "Airbnb Market Intelligence",
    category: ["analytics", "bi", "ml"],
    tagline: "Price prediction and market analytics platform for hosts.",
    problem:
      "Helps hosts price smarter against neighbourhood benchmarks using a full ETL pipeline and price prediction model.",
    stack: ["PostgreSQL", "XGBoost", "FastAPI", "Streamlit", "Power BI"],
    metric: { value: "R² 0.4553", label: "PRICE MODEL FIT" },
    status: "shipped",
    featured: false,
    verified: true,
  },
  {
    slug: "ecommerce-demand-forecasting",
    title: "Nigerian E-Commerce Market Intelligence",
    category: ["analytics", "ml", "systems"],
    tagline: "Demand forecasting platform on a medallion data architecture.",
    problem:
      "Production-grade market intelligence and demand forecasting for Nigerian e-commerce, built on free-tier infrastructure end to end.",
    stack: ["dbt", "Airflow", "XGBoost", "MLflow", "FastAPI", "Power BI"],
    metric: { value: "6", label: "PLANNING DOCS SHIPPED" },
    status: "active",
    featured: false,
    verified: true,
  },
  {
    // TODO(Elice): fill in real tagline/problem/stack/metric before launch.
    // Left as a structural placeholder only — do not publish with these values.
    slug: "golden-wok",
    title: "Golden Wok",
    category: ["business"],
    tagline: "PLACEHOLDER — needs your real project details",
    problem: "PLACEHOLDER — needs your real project details",
    stack: [],
    metric: { value: "—", label: "NEEDS REAL DATA" },
    status: "shipped",
    featured: false,
    verified: false,
  },
  {
    // TODO(Elice): fill in real tagline/problem/stack/metric before launch.
    slug: "glowmart",
    title: "GlowMart",
    category: ["analytics"],
    tagline: "PLACEHOLDER — needs your real project details",
    problem: "PLACEHOLDER — needs your real project details",
    stack: [],
    metric: { value: "—", label: "NEEDS REAL DATA" },
    status: "shipped",
    featured: false,
    verified: false,
  },
];

export function getProject(slug: string) {
  return projects.find((p) => p.slug === slug);
}

export function getFeatured() {
  return projects.find((p) => p.featured);
}

export function getSecondary() {
  return projects.filter((p) => !p.featured);
}
