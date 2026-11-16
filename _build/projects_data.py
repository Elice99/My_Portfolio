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
        "hasDocs": True,
        "category": ["analytics", "bi", "ml"],
        "tagline": "Price prediction and market analytics for the NYC short-term rental market.",
        "problem": "Hosts need to price competitively against neighbourhood benchmarks in New York City's short-term rental market but usually have no structured way to see where they sit relative to comparable listings.",
        "approach": "I built an ETL pipeline into PostgreSQL, wrote 16 SQL analytics queries, and trained an XGBoost price prediction model served through a FastAPI /predict endpoint, with a Streamlit app for exploring the market data.",
        "outcome": "RMSE $83.10, R\u00b2 0.4553 on price prediction -- a documented baseline for how much listing attributes explain price variation, not a claim of fully accurate market pricing.",
        "stack": ["PostgreSQL", "XGBoost", "FastAPI", "Streamlit"],
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
        # Verified against the local project folder (DataDNA September 2026
        # challenge): Golden_Wok_Business_README.md, Golden_Wok_Technical_README.md,
        # the dashboard screenshots and a direct profile of the CSVs.
        "slug": "golden-wok",
        "imagePrefix": "GoldenWok",
        "title": "Golden Wok Delivery Intelligence",
        "category": ["business", "analytics"],
        "hasDocs": True,
        "tagline": "Investigating how delivery distance and traffic friction constrain service reliability.",
        "problem": "Examines how delivery distance, urban traffic friction, kitchen capacity, and service-level performance interact within a food delivery network -- looking at delivery-zone performance, SLA breaches, and kitchen-level profitability across delivery corridors.",
        "approach": "I built a five-page Power BI report on the DataDNA September 2026 challenge dataset: 5,000 orders across 4 kitchens, 15 destination zones and 24 active riders in Lagos, spanning 2023 to 2024. Power Query prepared the data, a star-schema model carries the analysis, and DAX measures drive SLA severity bands, distance-band economics and dynamic pressure cards.",
        "outcome": "Half of all orders miss their delivery promise (49.9% SLA breach rate, -4.97 minute average gap) on a 0.65% profit margin -- pressure concentrates from the 6-8 km distance band up, and the Ikeja GRA to Alimosho corridor is worst at 64.52%.",
        "stack": ["Power BI", "DAX", "Power Query"],
        "metricValue": "49.9%",
        "metricLabel": "SLA breach rate",
        "status": "Shipped",
        "featured": False,
        "verified": True,
        "media": "browser",
        "github": "https://github.com/Elice99/DataDNA-Challenge/blob/main/DataDNA%20Dataset%20Challenge%20-%202026-09%20-%20Golden%20Wok%20Food%20Delivery/Golden_Wok_Business_README.md",
        "demo": None,
        "codeSnippet": None,
    },
    {
        # Verified against the local project folder (DataDNA August 2026
        # challenge): PayPesa_Project_Documentation.docx, README.md, the
        # five dashboard screenshots (copied as DigitalWallet_1..5) and a
        # direct profile of the shipped CSV files.
        "slug": "african-digital-wallet-risk",
        "imagePrefix": "DigitalWallet",
        "title": "PayPesa Wallet Risk Intelligence",
        "category": ["analytics", "bi", "business"],
        "hasDocs": True,
        "tagline": "A validation-first fraud investigation: what survives the audit, and what the platform's own risk scores miss.",
        "problem": "Investigates fraud and financial risk across 50,000 digital-wallet transactions from 5,000 gig workers in Nigeria, Kenya, Ghana and South Africa -- after discovering the dataset's documentation did not match the data itself, the project became a prove-it-first audit of every hypothesis before any finding was reported.",
        "approach": "I built a five-page Excel dashboard on Power Query and Power Pivot with every KPI as a live DAX measure, then tested each fraud hypothesis the brief named formally: chi-square and Cramér's V for all ten categorical dimensions, point-biserial correlation for the continuous ones, and a two-way channel-by-market cut when every one-way test came back flat.",
        "outcome": "Ten single-dimension tests all returned negligible Cramér's V (below 0.04), the platform's worker risk score shows zero correlation with actual fraud losses (r = -0.003), and losses are dispersed: the top 10% of workers carry 20.4% of fraud losses, about twice their fair share but far from watchlist territory.",
        "stack": ["Excel", "Power Query", "Power Pivot", "DAX"],
        "metricValue": "<0.04",
        "metricLabel": "max Cramér's V across 10 dimensions",
        "status": "Shipped",
        "featured": False,
        "verified": True,
        "media": "diagonal",
        "github": "https://github.com/Elice99/DataDNA-Challenge/blob/main/DataDNA%20Dataset%20Challenge%20-%202026-08%20-%20African%20Gig-Economy%20and%20Digital%20Wallet%20Risk/README.md",
        "demo": None,
        "codeSnippet": None,
    },
    {
        # Verified: direct profile of Telco-Customer-Churn.csv plus an exact
        # re-run of Churn.py's pipeline (CV 0.842 +- 0.007, test AUC 0.8585),
        # and the FastAPI predict.py / Swagger screenshot.
        "slug": "customer-churn-prediction",
        "imagePrefix": "CustomerChurn",
        "title": "Customer Churn Prediction",
        "category": ["ml", "business"],
        "hasDocs": True,
        "tagline": "A logistic regression churn model taken from notebook to a served API, with the business case it feeds.",
        "problem": "Telecom retention teams react to churn after it happens. I built a model that ranks 7,043 customers by their probability of leaving, so outreach goes to the right people first, plus an executive dashboard that shows where the risk lives.",
        "approach": "I trained a logistic regression on 19 features (DictVectorizer one-hot plus tenure and charges), validated with 5-fold cross-validation on ROC-AUC, pickled the vectorizer and model together, and served real-time predictions through a FastAPI endpoint with Swagger docs.",
        "outcome": "Test ROC-AUC 0.858 with cross-validation at 0.842 +/- 0.007, reproduced on re-run. The model separates risk cleanly: month-to-month customers churn at 42.7% versus 2.8% on two-year contracts, and I flagged the 1,869 churned-profile customers (26.5% of the base) whose lifetime billing totals $2.86M.",
        "stack": ["Python", "pandas", "scikit-learn", "FastAPI"],
        "metricValue": "0.858",
        "metricLabel": "test ROC-AUC",
        "status": "Shipped",
        "featured": False,
        "verified": True,
        "media": "browser",
        "github": "https://github.com/Elice99/Elisha-ML-Journey/blob/main/customer%20churn%2FBUSINESS_README.md",
        "demo": None,
        "codeSnippet": None,
    },
    {
        # Verified: openpyxl read of Customer Retention (AutoRecovered).xlsx
        # (5 sheets) and the dashboard screenshot; every KPI reconciles to
        # the Telco CSV the churn model uses.
        "slug": "customer-retention-dashboard",
        "imagePrefix": "CustomerRetention",
        "title": "Customer Retention Dashboard",
        "category": ["analytics", "bi", "business"],
        "hasDocs": True,
        "tagline": "The executive view of the same churn problem: 1,869 at-risk customers, where they come from, and what they are worth.",
        "problem": "The churn model can rank every customer, but leadership needs one screen that says who is at risk, how much revenue walks with them, and which segments to act on. I built that screen in Excel on the same 7,043-customer dataset.",
        "approach": "I built the analysis in Excel on PivotTables rather than formulas alone: a raw-data sheet, a pivot layer computing every share and total, and a two-level dashboard with slicers for contract type, gender and internet service so every card and chart filters in one click.",
        "outcome": "The dashboard reconciles to the row: 1,869 customers at risk, $139,131 of monthly billing and $2.86M of lifetime billing in that segment, 2,173 tech tickets behind them, and the service gaps that mark them: tech support adoption 29%, online security 29%, against 90% phone-service uptake.",
        "stack": ["Excel", "PivotTables", "Slicers"],
        "metricValue": "1,869",
        "metricLabel": "customers flagged at risk",
        "status": "Shipped",
        "featured": False,
        "verified": True,
        "media": "diagonal",
        "github": None,
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
