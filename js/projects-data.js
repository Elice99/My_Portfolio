// GENERATED FILE — do not hand-edit.
// Source of truth is /_build/projects_data.py. Edit there, then re-run
// `python3 _build/build.py` to regenerate this file and the case-study
// pages together, so they never drift apart.
//
// Add a new project by adding an object to PROJECTS in projects_data.py.

const PROJECTS = [
  {
    "slug": "trustlake",
    "imagePrefix": "TrustLake",
    "title": "TrustLake",
    "category": [
      "systems",
      "analytics"
    ],
    "tagline": "Deterministic data validation with AI-assisted explanations.",
    "problem": "Data quality issues can silently damage downstream decisions. TrustLake scores datasets on a deterministic Trust Score (0-100) and explains why in plain English, with a strict boundary: the AI explains and recommends, deterministic rules enforce, humans approve.",
    "approach": "Currently at Stage 1 of a 10-stage roadmap -- landing page shipped, moving into backend foundation (FastAPI, PostgreSQL, SQLAlchemy) with a provider-agnostic AI layer that works with AI fully disabled.",
    "outcome": "Pre-MVP. Full PRD, principles doc, and staged build roadmap are already written -- this case study will fill in with real metrics as each stage ships.",
    "stack": [
      "FastAPI",
      "PostgreSQL",
      "Python",
      "React/Next.js"
    ],
    "metricValue": "0–100",
    "metricLabel": "Deterministic Trust Score",
    "status": "Pre-MVP",
    "featured": true,
    "verified": true,
    "media": "layered",
    "github": "https://github.com/Elice99/TrustLake",
    "demo": null,
    "codeSnippet": null,
    "images": [],
    "video": null
  },
  {
    "slug": "sales-pipeline-prediction",
    "imagePrefix": "SalesPipeline",
    "title": "CRM Sales Analytics",
    "category": [
      "ml",
      "business"
    ],
    "tagline": "XGBoost model estimating win probability for B2B sales opportunities.",
    "problem": "Built for SPOTA, a mid-sized B2B tech and manufacturing company, to help the sales team evaluate CRM opportunities and prioritize effort toward deals most likely to close.",
    "approach": "Cleaned the pipeline tables in SQL Server, then trained a tuned XGBoost classifier on 6,711 closed deals with a slim 28-feature set, an experiment harness that cut the features that hurt cross-validated scores, and a single evaluation on the held-out test set. Wrapped the model in a FastAPI service with single and batch endpoints, containerized it with Docker, and scored all 1,589 open deals through it.",
    "outcome": "Held-out test ROC-AUC 0.6085, 62.8% accuracy with 94.8% recall at the shipped threshold, selected by 3x5 repeated cross-validation. Every quoted number traces to metrics.json, the file the training run writes; the open-deal scoring run is documented as a path test, not a pipeline read.",
    "stack": [
      "Python",
      "SQL Server",
      "XGBoost",
      "FastAPI",
      "Docker",
      "Power BI"
    ],
    "metricValue": "8,800",
    "metricLabel": "Opportunities in the pipeline",
    "status": "Shipped",
    "hasDocs": true,
    "featured": false,
    "flagship": true,
    "verified": true,
    "media": "browser",
    "github": "https://github.com/Elice99/Sales-Pipeline-Prediction-Model",
    "demo": null,
    "stakes": null,
    "decisions": null,
    "failure": null,
    "differently": null,
    "codeSnippet": null,
    "images": [
      "images/SalesPipeline_1.webp",
      "images/SalesPipeline_2.webp",
      "images/SalesPipeline_3.webp",
      "images/SalesPipeline_4.webp",
      "images/SalesPipeline_5.webp",
      "images/SalesPipeline_6.webp",
      "images/SalesPipeline_7.webp",
      "images/SalesPipeline_8.webp",
      "images/SalesPipeline_9.webp",
      "images/SalesPipeline_10.webp",
      "images/SalesPipeline_11.webp"
    ],
    "video": null
  },
  {
    "slug": "glowmart",
    "imagePrefix": "GlowMart",
    "title": "GlowMart",
    "category": [
      "analytics",
      "bi"
    ],
    "tagline": "Sales & inventory dashboard that reframed a supply crisis as a perception gap.",
    "problem": "GlowMart Nigeria's Sales Manager said Port Harcourt and Kano were short of stock. The Inventory Manager said stock was already shared equally across the five cities. The Managing Director wanted evidence, not opinions.",
    "approach": "I built a three-page Excel dashboard on 15,000 transactions from 2022 to 2024. Power Query cleaned the data, Power Pivot held the model, and PivotTables and PivotCharts drove the visuals.",
    "outcome": "Stock was already fair: revenue share and customer share were within 0.3% in every city. The real issues were flat growth (-0.5% in 2023 and +1.6% in 2024 against a 5% target), ₦72.4M in discounts with no clear lift in order value, and two cities that shrank in 2024, Abuja (-5.7%) and Kano (-2.9%).",
    "stack": [
      "Excel",
      "Power Query",
      "Power Pivot",
      "PivotTables/Charts"
    ],
    "metricValue": "₦652.6M",
    "metricLabel": "Total revenue analyzed",
    "status": "Shipped",
    "hasDocs": true,
    "featured": false,
    "flagship": true,
    "verified": true,
    "media": "split",
    "github": "https://github.com/Elice99/glowmart-sales-inventory-dashboard",
    "demo": null,
    "stakes": null,
    "decisions": null,
    "failure": null,
    "differently": null,
    "codeSnippet": null,
    "images": [
      "images/GlowMart_1.webp",
      "images/GlowMart_2.webp",
      "images/GlowMart_3.webp"
    ],
    "video": null
  },
  {
    "slug": "airbnb-market-intelligence",
    "imagePrefix": "Airbnb",
    "title": "Airbnb Market Intelligence",
    "hasDocs": true,
    "category": [
      "analytics",
      "bi",
      "ml"
    ],
    "tagline": "Price prediction and market analytics for the NYC short-term rental market.",
    "problem": "Hosts need to price competitively against neighbourhood benchmarks in New York City's short-term rental market but usually have no structured way to see where they sit relative to comparable listings.",
    "approach": "I built an ETL pipeline into PostgreSQL, wrote 16 SQL analytics queries, and trained an XGBoost price prediction model served through a FastAPI /predict endpoint, with a Streamlit app for exploring the market data.",
    "outcome": "RMSE $83.10, R² 0.4553 on price prediction -- a documented baseline for how much listing attributes explain price variation, not a claim of fully accurate market pricing.",
    "stack": [
      "PostgreSQL",
      "XGBoost",
      "FastAPI",
      "Streamlit"
    ],
    "metricValue": "R² 0.4553",
    "metricLabel": "Price model fit",
    "status": "Shipped",
    "featured": false,
    "verified": true,
    "media": "browser",
    "github": "https://github.com/Elice99/airbnb-market-intelligence",
    "demo": null,
    "codeSnippet": null,
    "images": [
      "images/Airbnb_1.webp",
      "images/Airbnb_2.webp",
      "images/Airbnb_3.webp"
    ],
    "video": "/video/AirBnB.mp4"
  },
  {
    "slug": "golden-wok",
    "imagePrefix": "GoldenWok",
    "title": "Golden Wok Delivery Intelligence",
    "category": [
      "business",
      "analytics"
    ],
    "hasDocs": true,
    "tagline": "Investigating how delivery distance and traffic friction constrain service reliability.",
    "problem": "Examines how delivery distance, urban traffic friction, kitchen capacity, and service-level performance interact within a food delivery network -- looking at delivery-zone performance, SLA breaches, and kitchen-level profitability across delivery corridors.",
    "approach": "I built a five-page Power BI report on the DataDNA September 2026 challenge dataset: 5,000 orders across 4 kitchens, 15 destination zones and 24 active riders in Lagos, spanning 2023 to 2024. Power Query prepared the data, a star-schema model carries the analysis, and DAX measures drive SLA severity bands, distance-band economics and dynamic pressure cards.",
    "outcome": "Half of all orders miss their delivery promise (49.9% SLA breach rate, -4.97 minute average gap) on a 0.65% profit margin -- pressure concentrates from the 6-8 km distance band up, and the Ikeja GRA to Alimosho corridor is worst at 64.52%.",
    "stack": [
      "Power BI",
      "DAX",
      "Power Query"
    ],
    "metricValue": "49.9%",
    "metricLabel": "SLA breach rate",
    "status": "Shipped",
    "featured": false,
    "verified": true,
    "media": "browser",
    "github": "https://github.com/Elice99/DataDNA-Challenge/blob/main/DataDNA%20Dataset%20Challenge%20-%202026-09%20-%20Golden%20Wok%20Food%20Delivery/Golden_Wok_Business_README.md",
    "demo": null,
    "codeSnippet": null,
    "images": [
      "images/GoldenWok_1.webp",
      "images/GoldenWok_2.webp",
      "images/GoldenWok_3.webp",
      "images/GoldenWok_4.webp",
      "images/GoldenWok_5.webp"
    ],
    "video": null
  },
  {
    "slug": "african-digital-wallet-risk",
    "imagePrefix": "DigitalWallet",
    "title": "PayPesa Wallet Risk Intelligence",
    "category": [
      "analytics",
      "bi",
      "business"
    ],
    "hasDocs": true,
    "tagline": "A validation-first fraud investigation: what survives the audit, and what the platform's own risk scores miss.",
    "problem": "Investigates fraud and financial risk across 50,000 digital-wallet transactions from 5,000 gig workers in Nigeria, Kenya, Ghana and South Africa -- after discovering the dataset's documentation did not match the data itself, the project became a prove-it-first audit of every hypothesis before any finding was reported.",
    "approach": "I built a five-page Excel dashboard on Power Query and Power Pivot with every KPI as a live DAX measure, then tested each fraud hypothesis the brief named formally: chi-square and Cramér's V for all ten categorical dimensions, point-biserial correlation for the continuous ones, and a two-way channel-by-market cut when every one-way test came back flat.",
    "outcome": "Ten single-dimension tests all returned negligible Cramér's V (below 0.04), the platform's worker risk score shows zero correlation with actual fraud losses (r = -0.003), and losses are dispersed: the top 10% of workers carry 20.4% of fraud losses, about twice their fair share but far from watchlist territory.",
    "stack": [
      "Excel",
      "Power Query",
      "Power Pivot",
      "DAX"
    ],
    "metricValue": "<0.04",
    "metricLabel": "max Cramér's V across 10 dimensions",
    "status": "Shipped",
    "featured": false,
    "verified": true,
    "media": "diagonal",
    "github": "https://github.com/Elice99/DataDNA-Challenge/blob/main/DataDNA%20Dataset%20Challenge%20-%202026-08%20-%20African%20Gig-Economy%20and%20Digital%20Wallet%20Risk/README.md",
    "demo": null,
    "codeSnippet": null,
    "images": [
      "images/DigitalWallet_1.webp",
      "images/DigitalWallet_2.webp",
      "images/DigitalWallet_3.webp",
      "images/DigitalWallet_4.webp",
      "images/DigitalWallet_5.webp"
    ],
    "video": null
  },
  {
    "slug": "customer-churn-prediction",
    "imagePrefix": "CustomerChurn",
    "title": "Customer Churn Prediction",
    "category": [
      "ml",
      "business"
    ],
    "hasDocs": true,
    "tagline": "A logistic regression churn model taken from notebook to a served API, with the business case it feeds.",
    "problem": "Telecom retention teams react to churn after it happens. I built a model that ranks 7,043 customers by their probability of leaving, so outreach goes to the right people first, plus an executive dashboard that shows where the risk lives.",
    "approach": "I trained a logistic regression on 19 features (DictVectorizer one-hot plus tenure and charges), validated with 5-fold cross-validation on ROC-AUC, pickled the vectorizer and model together, and served real-time predictions through a FastAPI endpoint with Swagger docs.",
    "outcome": "Test ROC-AUC 0.858 with cross-validation at 0.842 +/- 0.007, reproduced on re-run. The model separates risk cleanly: month-to-month customers churn at 42.7% versus 2.8% on two-year contracts, and I flagged the 1,869 churned-profile customers (26.5% of the base) whose lifetime billing totals $2.86M.",
    "stack": [
      "Python",
      "pandas",
      "scikit-learn",
      "FastAPI"
    ],
    "metricValue": "0.858",
    "metricLabel": "test ROC-AUC",
    "status": "Shipped",
    "featured": false,
    "verified": true,
    "media": "browser",
    "github": "https://github.com/Elice99/customer-churn-retention",
    "demo": null,
    "codeSnippet": null,
    "images": [
      "images/CustomerChurn_1.webp",
      "images/CustomerChurn_2.webp"
    ],
    "video": null
  },
  {
    "slug": "customer-retention-dashboard",
    "imagePrefix": "CustomerRetention",
    "title": "Customer Retention Dashboard",
    "category": [
      "analytics",
      "bi",
      "business"
    ],
    "hasDocs": true,
    "tagline": "The executive view of the same churn problem: 1,869 at-risk customers, where they come from, and what they are worth.",
    "problem": "The churn model can rank every customer, but leadership needs one screen that says who is at risk, how much revenue walks with them, and which segments to act on. I built that screen in Excel on the same 7,043-customer dataset.",
    "approach": "I built the analysis in Excel on PivotTables rather than formulas alone: a raw-data sheet, a pivot layer computing every share and total, and a two-level dashboard with slicers for contract type, gender and internet service so every card and chart filters in one click.",
    "outcome": "The dashboard reconciles to the row: 1,869 customers at risk, $139,131 of monthly billing and $2.86M of lifetime billing in that segment, 2,173 tech tickets behind them, and the service gaps that mark them: tech support adoption 29%, online security 29%, against 90% phone-service uptake.",
    "stack": [
      "Excel",
      "PivotTables",
      "Slicers"
    ],
    "metricValue": "1,869",
    "metricLabel": "customers flagged at risk",
    "status": "Shipped",
    "featured": false,
    "verified": true,
    "media": "diagonal",
    "github": null,
    "demo": null,
    "codeSnippet": null,
    "images": [
      "images/CustomerRetention_1.webp"
    ],
    "video": null
  },
  {
    "slug": "ecommerce-demand-forecasting",
    "imagePrefix": "Ecommerce",
    "title": "Nigerian E-Commerce Market Intelligence",
    "category": [
      "analytics",
      "ml",
      "systems"
    ],
    "tagline": "Demand forecasting platform on a medallion data architecture.",
    "problem": "Nigerian e-commerce sellers lack production-grade demand forecasting tools that run on realistic, low-cost infrastructure rather than enterprise cloud budgets.",
    "approach": "Designed a medallion architecture (bronze/silver/gold) orchestrated with Airflow and GitHub Actions, modeled with dbt, validated with Great Expectations. XGBoost models tracked via MLflow, served through FastAPI, visualized in Power BI -- the whole stack mapped entirely to free-tier infrastructure (Neon.tech, Render, Vercel).",
    "outcome": "Six planning documents shipped (PRD, 30-day build plan, BRD, Technical Architecture Document, KPI Framework, PROGRESS.md) -- build is active.",
    "stack": [
      "dbt",
      "Airflow",
      "XGBoost",
      "MLflow",
      "FastAPI",
      "Power BI"
    ],
    "metricValue": "6",
    "metricLabel": "Planning docs shipped",
    "status": "Active",
    "featured": false,
    "verified": true,
    "media": "diagonal",
    "github": null,
    "demo": null,
    "codeSnippet": null,
    "images": [],
    "video": null
  },
  {
    "slug": "er-patient-analysis",
    "imagePrefix": "ERPatient",
    "title": "Emergency Room Patient Analysis",
    "category": [
      "bi",
      "analytics"
    ],
    "tagline": "A one-page Power BI report on ER visit volume, waiting time and satisfaction, built on synthetic data.",
    "problem": "Emergency departments watch volume, waiting time, satisfaction and referrals, but usually in separate reports. This project puts them in one view so the first questions are easier to ask. The dataset is synthetic, so nothing here describes a real hospital.",
    "approach": "I loaded a 9,216 row synthetic CSV into Power BI with Power Query, added calculated columns and a date table in DAX, wrote reusable measures in a dedicated Calculation table, and built a one-page report. A field parameter lets one heatmap switch between satisfaction and wait time.",
    "outcome": "A working monitoring and exploration prototype, plus an honest list of what to fix. Most visits have no satisfaction rating, the wait time has no stated unit, two report numbers do not match the source file, and the model has a duplicate patient table.",
    "stack": [
      "Power BI",
      "DAX",
      "Power Query (M)"
    ],
    "metricValue": "9,216",
    "metricLabel": "Synthetic ER visits",
    "status": "Prototype",
    "hasDocs": true,
    "featured": false,
    "flagship": true,
    "verified": true,
    "media": "browser",
    "github": null,
    "demo": null,
    "stakes": null,
    "decisions": null,
    "failure": null,
    "differently": null,
    "codeSnippet": {
      "lang": "dax",
      "filename": "Parameter (field parameter)",
      "code": "{\n    (\"Avg Satisfaction\", NAMEOF('Calculation'[Average Satisfaction Score]), 0),\n    (\"Avg wait Time\", NAMEOF('Calculation'[Average wait Time]), 1)\n}"
    },
    "images": [
      "images/ERPatient_1.webp"
    ],
    "video": null
  },
  {
    "slug": "zion-finance-data-challenge",
    "imagePrefix": "ZionFinance",
    "title": "The Cost of Failed Transactions",
    "category": [
      "business",
      "analytics"
    ],
    "tagline": "Finding the concentrated card and account leak inside $2.84M of failed fee revenue.",
    "problem": "A finance challenge brief mixed two failure rates and asked where payment failures concentrated, why January 2024 spiked, and what a realistic fix could recover. The supplied extract holds 62,684 monthly aggregate rows across five East African markets.",
    "approach": "I built a deterministic Python pipeline: prepare the raw CSVs once, analyse them into monthly, channel, country, sector, account, ticket and recovery tables, then generate a 15-sheet Excel workbook, six report charts and a 64-check QA suite. Both failure lenses stay separate throughout.",
    "outcome": "10 accounts hold 49.3 percent of the $2,842,676 failed fee revenue. Card holds 79.7 percent of the leak and fails 93.8 percent by fee value. January 2024 was a volume and mix shock from a few accounts. A credible fix recovers $319,853 stacked, or $399,575 in the stretch case, not the full $2.84M.",
    "stack": [
      "Python",
      "pandas",
      "openpyxl",
      "matplotlib",
      "Excel"
    ],
    "metricValue": "$2.84M",
    "metricLabel": "failed fee revenue",
    "status": "Shipped",
    "hasDocs": true,
    "featured": false,
    "verified": true,
    "media": "browser",
    "github": null,
    "demo": null,
    "codeSnippet": {
      "lang": "python",
      "filename": "scripts/analyse.py",
      "code": "def kpis(d: pd.DataFrame) -> dict:\n    att = float(d[\"total_count\"].sum())\n    fatt = float(d[\"FailedCount\"].sum())\n    rev = float(d[\"Rev_USD\"].sum())\n    frev = float(d[\"FailedRev_USD\"].sum())\n    succ_att = att - fatt\n    return {\n        \"attempts\": att,\n        \"failed_attempts\": fatt,\n        \"count_fail_rate\": fatt / att if att else np.nan,\n        \"revenue_usd\": rev,\n        \"failed_revenue_usd\": frev,\n        \"revenue_fail_rate\": frev / rev if rev else np.nan,\n        \"avg_fee_failed_att\": frev / fatt if fatt else np.nan,\n        \"avg_fee_success_att\": (rev - frev) / succ_att if succ_att else np.nan,\n    }"
    },
    "images": [
      "images/ZionFinance_1.webp",
      "images/ZionFinance_2.webp",
      "images/ZionFinance_3.webp",
      "images/ZionFinance_4.webp",
      "images/ZionFinance_5.webp",
      "images/ZionFinance_6.webp"
    ],
    "video": null
  },
  {
    "slug": "developer-survey-analysis",
    "imagePrefix": "DevSurvey",
    "title": "Developer Survey Analysis",
    "category": [
      "bi",
      "analytics"
    ],
    "tagline": "Interactive Power BI dashboard exploring developer survey patterns.",
    "problem": "Raw survey responses are hard to compare across respondent groups without a structured way to explore them.",
    "approach": "Organized developer survey responses and built an interactive Power BI dashboard for comparing respondent segments.",
    "outcome": "Confirm the specific findings and segments explored here before publishing.",
    "stack": [
      "Python",
      "SQL",
      "Power BI"
    ],
    "metricValue": "—",
    "metricLabel": "Needs verified finding",
    "status": "Shipped",
    "featured": false,
    "verified": false,
    "media": "browser",
    "github": "https://github.com/Elice99/Developer_survey/blob/main/powerbi/README.md",
    "demo": null,
    "codeSnippet": null,
    "images": [
      "images/DevSurvey_1.webp"
    ],
    "video": null
  },
  {
    "slug": "inventory-log-analysis",
    "imagePrefix": "InventoryLog",
    "title": "Inventory Log Analysis",
    "category": [
      "analytics",
      "business"
    ],
    "tagline": "Turning inventory logs into operational visibility.",
    "problem": "Raw inventory logs don't by themselves show stock movement patterns or where operational visibility is weakest.",
    "approach": "Used SQL (CTEs) against inventory records to investigate stock movements and changes over time, visualized in Power BI.",
    "outcome": "Confirm the specific findings here before publishing.",
    "stack": [
      "SQL",
      "Power BI"
    ],
    "metricValue": "—",
    "metricLabel": "Needs verified finding",
    "status": "Shipped",
    "featured": false,
    "verified": false,
    "media": "browser",
    "github": "https://github.com/Elice99/inventory-log-analysis-/blob/main/README.md",
    "demo": null,
    "codeSnippet": null,
    "images": [
      "images/InventoryLog_1.webp",
      "images/InventoryLog_2.webp"
    ],
    "video": null
  },
  {
    "slug": "data-cleaning-eda",
    "imagePrefix": "DataCleaningEDA",
    "title": "Data Cleaning & Exploratory Analysis",
    "category": [
      "analytics"
    ],
    "tagline": "A structured workflow for preparing raw data for reliable analysis.",
    "problem": "Raw data with quality issues and inconsistencies produces unreliable downstream analysis if used as-is.",
    "approach": "AnalystLab Africa Batch B internship deliverable -- identified data quality issues, handled inconsistencies, and explored distributions and relationships before preparing the dataset for reporting.",
    "outcome": "Confirm the specific dataset and findings here before publishing.",
    "stack": [
      "SQL"
    ],
    "metricValue": "—",
    "metricLabel": "Needs verified finding",
    "status": "Shipped",
    "featured": false,
    "verified": false,
    "media": "browser",
    "github": "https://github.com/Elice99/analystlab-batch-b-week1-2/blob/main/README.md",
    "demo": null,
    "codeSnippet": null,
    "images": [],
    "video": null
  }
];

function getFeaturedProject() {
  return PROJECTS.find((p) => p.featured);
}
function getSecondaryProjects() {
  return PROJECTS.filter((p) => !p.featured);
}
function getVerifiedProjects() {
  return PROJECTS.filter((p) => p.verified);
}

// Shared card renderer used by index.html, work.html, and the capabilities
// filter results, so the GitHub icon / metric badge markup can't drift
// between the three places project cards get rendered.
function projectCardHTML(p, opts) {
  opts = opts || {};
  var badge = p.verified
    ? '<div class="project-metric-badge"><span class="stat-value">' + p.metricValue + '</span><span class="stat-label">' + p.metricLabel + '</span></div>'
    : '';
  var ROOT = window.SITE_ROOT || '';
  var githubLink = p.github
    ? '<a href="' + p.github + '" target="_blank" rel="noopener" class="project-github-link" aria-label="View ' + p.title + ' on GitHub" onclick="event.stopPropagation()"><i class="fab fa-github"></i></a>'
    : '';
  var statusPill = (opts.showStatus && p.status)
    ? '<span class="project-badge" style="background:var(--bg-tertiary);color:var(--text-secondary);box-shadow:none">' + p.status + '</span>'
    : '';
  // Real screenshot as thumbnail once one exists; otherwise the original
  // icon placeholder. Nothing else about the card needs to change when
  // Elice adds photos later -- it upgrades itself on the next rebuild.
  var hasImage = p.images && p.images.length > 0;
  var visualContent = hasImage
    ? '<img src="' + ROOT + p.images[0] + '" alt="' + p.title + ' screenshot" loading="lazy" decoding="async">'
    : '<i class="fas fa-chart-line project-icon" data-img-swap="' + p.imagePrefix + '_1" data-img-alt="' + p.title + ' screenshot"></i>';
  return (
    '<div class="project-card' + (opts.extraClass ? ' ' + opts.extraClass : '') + '"' +
        (opts.dataCategory ? ' data-category="' + opts.dataCategory + '"' : '') + ' data-aos="' + (opts.aos || 'fade-up') + '">' +
      badge + githubLink +
      '<a href="' + ROOT + 'projects/' + p.slug + '.html" class="project-card-link" aria-label="View ' + p.title + ' case study"></a>' +
      '<div class="project-visual' + (hasImage ? ' has-image' : '') + '">' + visualContent + statusPill + '</div>' +
      '<div class="project-info">' +
        '<h3 class="project-title">' + p.title + '</h3>' +
        '<p class="project-description">' + p.tagline + '</p>' +
        '<div class="project-tech">' + (p.stack.length ? p.stack.map(function (s) { return '<span>' + s + '</span>'; }).join('') : '<span>In progress</span>') + '</div>' +
      '</div>' +
    '</div>'
  );
}
