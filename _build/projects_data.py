"""
Single source of truth for project data. build.py generates BOTH
js/projects-data.js (for the command palette, work.html, index.html)
AND the static case-study pages in /projects/ from this one list --
so the displayed data can never drift between pages.

`verified: False` projects render a visible placeholder notice on
their case-study page instead of fabricated numbers.

`github` is each project's real repo link. `demo` is optional (a live
app / dashboard URL) -- leave as None if there isn't one yet.

Several entries below were last updated against "GitHub_repo_links.docx"
(an AI-drafted content review of Elice's real repos). That doc flagged
its own content varying by confidence: some projects had hard numbers
it trusted, others it explicitly said needed verification against the
actual README before publishing. That distinction is preserved here --
see the TODO comments on the newer entries. One claim from that doc was
NOT imported: it listed GlowMart's stack as "Power BI, DAX" -- wrong,
GlowMart was built in Excel (already verified) -- and used the exact
same line for Golden Wok, suggesting it was templated rather than
checked per-repo. Golden Wok's stack is left blank rather than guessed.

`imagePrefix` is the filename prefix to use in /images/ for that project's
screenshots -- e.g. GlowMart's is "GlowMart", so files named GlowMart_1.jpg
through GlowMart_5.jpg (any mix of .jpg/.jpeg/.png/.webp) are auto-detected
on the next build and replace the placeholder with a real scrollable
gallery. No other edit needed.

`flagship: True` marks the three front-page case studies (the deep
ones on work.html). It is NOT permanent -- when a newer project outgrows
the archive, flip the flags and rebuild. Only flagships carry the story
fields below; every other project still gets its full case-study page,
it just leads from the archive list instead.

Flagship-only optional fields -- fill in with REAL material, never
placeholders. A section only renders when its field is filled in:
    "stakes":     what the problem cost or risked, and who cared.
    "decisions":  [{"title": "...", "text": "..."}] -- the genuinely
                  ambiguous calls and how each was resolved.
    "failure":    one honest thing that went wrong and how you caught it.
    "differently": what you would change on a redo.

`codeSnippet` is optional and off (None) by default -- it renders a small
floating "editor window" card overlapping the case study's media area.
Only ever put REAL code you actually wrote in here; this field exists so
a genuine snippet can float over a screenshot, not so a plausible-looking
example can be invented. Shape:
    "codeSnippet": {
        "lang": "python",  # or "sql"
        "filename": "train_model.py",
        "code": "def train():\n    ...",
    }
"""

PROJECTS = [
    {
        "slug": "trustlake",
        "imagePrefix": "TrustLake",
        "title": "TrustLake",
        "category": ["systems", "analytics"],
        "tagline": "Deterministic data validation with AI-assisted explanations.",
        "problem": "Data quality issues can silently damage downstream decisions. TrustLake scores datasets on a deterministic Trust Score (0-100) and explains why in plain English, with a strict boundary: the AI explains and recommends, deterministic rules enforce, humans approve.",
        "approach": "Currently at Stage 1 of a 10-stage roadmap -- landing page shipped, moving into backend foundation (FastAPI, PostgreSQL, SQLAlchemy) with a provider-agnostic AI layer that works with AI fully disabled.",
        "outcome": "Pre-MVP. Full PRD, principles doc, and staged build roadmap are already written -- this case study will fill in with real metrics as each stage ships.",
        "stack": ["FastAPI", "PostgreSQL", "Python", "React/Next.js"],
        "metricValue": "0\u2013100",
        "metricLabel": "Deterministic Trust Score",
        "status": "Pre-MVP",
        "featured": True,
        "verified": True,
        "media": "layered",
        "github": "https://github.com/Elice99/TrustLake",
        "demo": None,
        "codeSnippet": None,
    },
    {
        "slug": "sales-pipeline-prediction",
        "imagePrefix": "SalesPipeline",
        "title": "CRM Sales Analytics",
        "category": ["ml", "business"],
        "tagline": "XGBoost model estimating win probability for B2B sales opportunities.",
        "problem": "Built for SPOTA, a mid-sized B2B tech and manufacturing company, to help the sales team evaluate CRM opportunities and prioritize effort toward deals most likely to close.",
        "approach": "Cleaned the pipeline tables in SQL Server, then trained a tuned XGBoost classifier on 6,711 closed deals with a slim 28-feature set, an experiment harness that cut the features that hurt cross-validated scores, and a single evaluation on the held-out test set. Wrapped the model in a FastAPI service with single and batch endpoints, containerized it with Docker, and scored all 1,589 open deals through it.",
        "outcome": "Held-out test ROC-AUC 0.6085, 62.8% accuracy with 94.8% recall at the shipped threshold, selected by 3x5 repeated cross-validation. Every quoted number traces to metrics.json, the file the training run writes; the open-deal scoring run is documented as a path test, not a pipeline read.",
        "stack": ["Python", "SQL Server", "XGBoost", "FastAPI", "Docker", "Power BI"],
        "metricValue": "8,800",
        "metricLabel": "Opportunities in the pipeline",
        "status": "Shipped",
        "hasDocs": True,
        "featured": False,
        "flagship": True,
        "verified": True,
        "media": "browser",
        "github": "https://github.com/Elice99/Sales-Pipeline-Prediction-Model",
        "demo": None,
        # Flagship story fields -- real material only, rebuild after filling.
        "stakes": None,
        "decisions": None,
        "failure": None,
        "differently": None,
        "codeSnippet": None,
    },
    {
        "slug": "glowmart",
        "imagePrefix": "GlowMart",
        "title": "GlowMart",
        "category": ["analytics", "bi"],
        "tagline": "Sales & inventory dashboard that reframed a supply crisis as a perception gap.",
        "problem": "GlowMart Nigeria's Sales Manager said Port Harcourt and Kano were short of stock. The Inventory Manager said stock was already shared equally across the five cities. The Managing Director wanted evidence, not opinions.",
        "approach": "I built a three-page Excel dashboard on 15,000 transactions from 2022 to 2024. Power Query cleaned the data, Power Pivot held the model, and PivotTables and PivotCharts drove the visuals.",
        "outcome": "Stock was already fair: revenue share and customer share were within 0.3% in every city. The real issues were flat growth (-0.5% in 2023 and +1.6% in 2024 against a 5% target), \u20a672.4M in discounts with no clear lift in order value, and two cities that shrank in 2024, Abuja (-5.7%) and Kano (-2.9%).",
        "stack": ["Excel", "Power Query", "Power Pivot", "PivotTables/Charts"],
        "metricValue": "\u20a6652.6M",
        "metricLabel": "Total revenue analyzed",
        "status": "Shipped",
        "hasDocs": True,
        "featured": False,
        "flagship": True,
        "verified": True,
        "media": "split",
        "github": "https://github.com/Elice99/glowmart-sales-inventory-dashboard",
        "demo": None,
        # Flagship story fields -- real material only, rebuild after filling.
        "stakes": None,
        "decisions": None,
        "failure": None,
        "differently": None,
        "codeSnippet": None,
    },
    {
        "slug": "airbnb-market-intelligence",
        "imagePrefix": "Airbnb",
        "title": "Airbnb Market Intelligence",
        "category": ["analytics", "bi", "ml"],
        "tagline": "Price prediction and market analytics for the NYC short-term rental market.",
        "problem": "Hosts need to price competitively against neighbourhood benchmarks in New York City's short-term rental market but usually have no structured way to see where they sit relative to comparable listings.",
        "approach": "Built a full ETL pipeline into PostgreSQL, wrote 15+ SQL analytics queries, and built a 6-page Power BI dashboard. Trained an XGBoost price prediction model served through a FastAPI /predict endpoint, with a separate 5-page Streamlit app for exploring the market data, all containerized with Docker.",
        "outcome": "RMSE $83.10, R\u00b2 0.4553 on price prediction -- a documented baseline for how much listing attributes explain price variation, not a claim of fully accurate market pricing.",
        "stack": ["PostgreSQL", "XGBoost", "FastAPI", "Streamlit", "Power BI"],
        "metricValue": "R\u00b2 0.4553",
        "metricLabel": "Price model fit",
        "status": "Shipped",
        "featured": False,
        "verified": True,
        "media": "browser",
        "github": "https://github.com/Elice99/airbnb-market-intelligence",
        "demo": None,
        "codeSnippet": None,
    },
    {
        # TODO(Elice): the source doc gave problem framing but no verified
        # outcome metric or confirmed tech stack for this one (its listed
        # "Power BI, DAX" was identical to GlowMart's entry, which was
        # wrong for GlowMart -- so it's not trusted here either). Confirm
        # the real stack and add a specific verified finding, then flip
        # verified to True.
        "slug": "golden-wok",
        "imagePrefix": "GoldenWok",
        "title": "Golden Wok",
        "category": ["business", "analytics"],
        "tagline": "Investigating how delivery distance and traffic friction constrain service reliability.",
        "problem": "Examines how delivery distance, urban traffic friction, kitchen capacity, and service-level performance interact within a food delivery network -- looking at delivery-zone performance, SLA breaches, and kitchen-level profitability across delivery corridors.",
        "approach": "Confirm your actual analytical approach here -- which tool, which data, which time period.",
        "outcome": "Confirm your actual verified finding here before publishing a specific number.",
        "stack": [],
        "metricValue": "\u2014",
        "metricLabel": "Needs verified finding",
        "status": "Shipped",
        "featured": False,
        "verified": False,
        "media": "browser",
        "github": "https://github.com/Elice99/DataDNA-Challenge/blob/main/DataDNA%20Dataset%20Challenge%20-%202026-09%20-%20Golden%20Wok%20Food%20Delivery/Golden_Wok_Business_README.md",
        "demo": None,
        "codeSnippet": None,
    },
    {
        # TODO(Elice): source doc explicitly called this description
        # "deliberately conservative" and said to verify findings/stack
        # against your README before publishing specifics.
        "slug": "african-digital-wallet-risk",
        "imagePrefix": "DigitalWallet",
        "title": "African Digital Wallet Risk Intelligence",
        "category": ["analytics", "bi", "business"],
        "tagline": "Risk indicators across the African gig-economy and digital wallet ecosystem.",
        "problem": "Explores financial risk patterns in the African gig economy and digital wallet ecosystem -- investigating risk indicators across transaction and user segments to flag areas needing closer monitoring.",
        "approach": "Built from transaction data spanning Jan 2023 to Dec 2024 (USD), across 4 dimension tables and 1 fact table, as an Onyx Data monthly challenge.",
        "outcome": "Confirm your actual verified finding here before publishing a specific number.",
        "stack": ["Excel"],
        "metricValue": "\u2014",
        "metricLabel": "Needs verified finding",
        "status": "Shipped",
        "featured": False,
        "verified": False,
        "media": "diagonal",
        "github": "https://github.com/Elice99/DataDNA-Challenge/blob/main/DataDNA%20Dataset%20Challenge%20-%202026-08%20-%20African%20Gig-Economy%20and%20Digital%20Wallet%20Risk/README.md",
        "demo": None,
        "codeSnippet": None,
    },
    {
        "slug": "customer-churn-prediction",
        "imagePrefix": "CustomerChurn",
        "title": "Customer Churn Prediction",
        "category": ["ml", "business"],
        "tagline": "Predicting which customers are at risk of leaving, and why.",
        "problem": "Organizations need to know which customers are at risk of churning before they leave, not after, so retention efforts can be targeted rather than reactive.",
        "approach": "Built a churn prediction workflow covering data preparation, exploratory analysis, feature engineering, and model training with scikit-learn and XGBoost, served through a FastAPI endpoint.",
        "outcome": "Flagged approximately 1,869 at-risk customers from the evaluated dataset for targeted retention follow-up.",
        "stack": ["scikit-learn", "XGBoost", "FastAPI"],
        "metricValue": "1,869",
        "metricLabel": "At-risk customers flagged",
        "status": "Shipped",
        "featured": False,
        "verified": True,
        "media": "browser",
        "github": "https://github.com/Elice99/Elisha-ML-Journey/blob/main/customer%20churn%2FBUSINESS_README.md",
        "demo": None,
        "codeSnippet": None,
    },
    {
        "slug": "ecommerce-demand-forecasting",
        "imagePrefix": "Ecommerce",
        "title": "Nigerian E-Commerce Market Intelligence",
        "category": ["analytics", "ml", "systems"],
        "tagline": "Demand forecasting platform on a medallion data architecture.",
        "problem": "Nigerian e-commerce sellers lack production-grade demand forecasting tools that run on realistic, low-cost infrastructure rather than enterprise cloud budgets.",
        "approach": "Designed a medallion architecture (bronze/silver/gold) orchestrated with Airflow and GitHub Actions, modeled with dbt, validated with Great Expectations. XGBoost models tracked via MLflow, served through FastAPI, visualized in Power BI -- the whole stack mapped entirely to free-tier infrastructure (Neon.tech, Render, Vercel).",
        "outcome": "Six planning documents shipped (PRD, 30-day build plan, BRD, Technical Architecture Document, KPI Framework, PROGRESS.md) -- build is active.",
        "stack": ["dbt", "Airflow", "XGBoost", "MLflow", "FastAPI", "Power BI"],
        "metricValue": "6",
        "metricLabel": "Planning docs shipped",
        "status": "Active",
        "featured": False,
        "verified": True,
        "media": "diagonal",
        "github": None,
        "demo": None,
        "codeSnippet": None,
    },
    {
        "slug": "er-patient-analysis",
        "imagePrefix": "ERPatient",
        "title": "Emergency Room Patient Analysis",
        "category": ["bi", "analytics"],
        "tagline": "A one-page Power BI report on ER visit volume, waiting time and satisfaction, built on synthetic data.",
        "problem": "Emergency departments watch volume, waiting time, satisfaction and referrals, but usually in separate reports. This project puts them in one view so the first questions are easier to ask. The dataset is synthetic, so nothing here describes a real hospital.",
        "approach": "I loaded a 9,216 row synthetic CSV into Power BI with Power Query, added calculated columns and a date table in DAX, wrote reusable measures in a dedicated Calculation table, and built a one-page report. A field parameter lets one heatmap switch between satisfaction and wait time.",
        "outcome": "A working monitoring and exploration prototype, plus an honest list of what to fix. Most visits have no satisfaction rating, the wait time has no stated unit, two report numbers do not match the source file, and the model has a duplicate patient table.",
        "stack": ["Power BI", "DAX", "Power Query (M)"],
        "metricValue": "9,216",
        "metricLabel": "Synthetic ER visits",
        "status": "Prototype",
        "hasDocs": True,
        "featured": False,
        "flagship": True,
        "verified": True,
        "media": "browser",
        "github": None,
        "demo": None,
        # Flagship story fields -- real material only, rebuild after filling.
        "stakes": None,
        "decisions": None,
        "failure": None,
        "differently": None,
        "codeSnippet": {
            "lang": "dax",
            "filename": "Parameter (field parameter)",
            "code": """{
    ("Avg Satisfaction", NAMEOF('Calculation'[Average Satisfaction Score]), 0),
    ("Avg wait Time", NAMEOF('Calculation'[Average wait Time]), 1)
}""",
        },
    },
    {
        # TODO(Elice): add the specific survey questions, segments, and
        # findings your dashboard covers, then flip verified to True.
        "slug": "developer-survey-analysis",
        "imagePrefix": "DevSurvey",
        "title": "Developer Survey Analysis",
        "category": ["bi", "analytics"],
        "tagline": "Interactive Power BI dashboard exploring developer survey patterns.",
        "problem": "Raw survey responses are hard to compare across respondent groups without a structured way to explore them.",
        "approach": "Organized developer survey responses and built an interactive Power BI dashboard for comparing respondent segments.",
        "outcome": "Confirm the specific findings and segments explored here before publishing.",
        "stack": ["Python", "SQL", "Power BI"],
        "metricValue": "\u2014",
        "metricLabel": "Needs verified finding",
        "status": "Shipped",
        "featured": False,
        "verified": False,
        "media": "browser",
        "github": "https://github.com/Elice99/Developer_survey/blob/main/powerbi/README.md",
        "demo": None,
        "codeSnippet": None,
    },
    {
        # TODO(Elice): add the specific questions investigated and findings
        # obtained, then flip verified to True.
        "slug": "inventory-log-analysis",
        "imagePrefix": "InventoryLog",
        "title": "Inventory Log Analysis",
        "category": ["analytics", "business"],
        "tagline": "Turning inventory logs into operational visibility.",
        "problem": "Raw inventory logs don't by themselves show stock movement patterns or where operational visibility is weakest.",
        "approach": "Used SQL (CTEs) against inventory records to investigate stock movements and changes over time, visualized in Power BI.",
        "outcome": "Confirm the specific findings here before publishing.",
        "stack": ["SQL", "Power BI"],
        "metricValue": "\u2014",
        "metricLabel": "Needs verified finding",
        "status": "Shipped",
        "featured": False,
        "verified": False,
        "media": "browser",
        "github": "https://github.com/Elice99/inventory-log-analysis-/blob/main/README.md",
        "demo": None,
        "codeSnippet": None,
    },
    {
        # TODO(Elice): confirm the actual tools used in this repo before
        # adding a stack -- "EDA, SQL" is the only confirmed detail on file.
        "slug": "data-cleaning-eda",
        "imagePrefix": "DataCleaningEDA",
        "title": "Data Cleaning & Exploratory Analysis",
        "category": ["analytics"],
        "tagline": "A structured workflow for preparing raw data for reliable analysis.",
        "problem": "Raw data with quality issues and inconsistencies produces unreliable downstream analysis if used as-is.",
        "approach": "AnalystLab Africa Batch B internship deliverable -- identified data quality issues, handled inconsistencies, and explored distributions and relationships before preparing the dataset for reporting.",
        "outcome": "Confirm the specific dataset and findings here before publishing.",
        "stack": ["SQL"],
        "metricValue": "\u2014",
        "metricLabel": "Needs verified finding",
        "status": "Shipped",
        "featured": False,
        "verified": False,
        "media": "browser",
        "github": "https://github.com/Elice99/analystlab-batch-b-week1-2/blob/main/README.md",
        "demo": None,
        "codeSnippet": None,
    },
]
