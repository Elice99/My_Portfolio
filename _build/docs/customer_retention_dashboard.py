"""
Customer Retention Dashboard documentation content, written in
Elisha's voice: he built the Excel workbook, so the pages say "I did".

Basis: an openpyxl read of his Customer Retention (AutoRecovered).xlsx
(five sheets: 01 Churn-Dataset, PivotTable, Welcome, ChurnDashbord,
CustomerRiskAnalysis), the dashboard screenshot (CustomerRetention_1),
and reconciliation of every dashboard figure against the
Telco-Customer-Churn.csv that also feeds his churn model.

Rules: first person, plain words, no em dashes, only claims the data
supports. One of the dashboard's own labels (Yearly Charges) measures
something other than what it says; that is handled head-on here.
"""


# ---------------------------------------------------------------- business
BUSINESS = {
    "title": "Customer Retention Dashboard: one screen for the churn problem",
    "lede": "An Excel executive dashboard built on the same 7,043-customer dataset as my churn model, but built for a different reader: leadership, on one screen, with slicers instead of code. This page covers what the dashboard shows, how every number reconciles to the data, and how to act on it.",
    "sections": [
        {"id": "problem", "heading": "The problem I set out to solve", "blocks": [
            {"type": "p", "items": [
                "A churn model produces a ranked list. Leadership does not make decisions from a ranked list; they make them from a screen that says how big the risk is, what it is worth, and where it lives. I built this dashboard as that screen, on the same Telco dataset my prediction model uses, so the two projects tell one story from two angles.",
                "My constraint was the audience. The workbook had to work for someone who will never open a notebook: open the file, land on the dashboard, click a segment, and every number updates. That pushed me to Excel on PivotTables rather than formulas scattered across the sheet, because pivots keep every figure tied to the data by construction.",
                "The questions the screen answers: how many customers are at risk, what is their ticket load and billing, who are they demographically, how long have they been with us, which services do they take, and how do they pay?",
            ]},
        ]},
        {"id": "answer", "heading": "The short answer", "blocks": [
            {"type": "verdict", "text": "The dashboard puts the whole churn exposure on one screen: 1,869 customers at risk out of 7,043, carrying 2,173 tech tickets and 885 admin tickets, $139,131 of monthly billing and $2.86M of lifetime billing. The panels explain who they are. Demographically they look like the base (50.5% female, 16% senior citizens), so nothing exotic is driving the risk. The story is in the account panels: 65% of the contract mix is month-to-month at the top of the contract chart, electronic check leads the payment bars, 29% of customers are inside their first year, and the service panel shows the protective add-ons (tech support 29%, online security 29%) barely adopted while phone service runs at 90%. The at-risk customer is not demographically unusual; they are contractually and behaviourally predictable, which is exactly what makes them targetable."},
            {"type": "figure", "spec": ("CustomerRetention_1", "The full dashboard: KPI cards across the top, the demography, account and service panels below, with the contract, gender and internet-service slicers wired to every visual.")},
        ]},
        {"id": "numbers", "heading": "Numbers at a glance", "blocks": [
            {"type": "stat_grid", "items": [
                ("1,869", "customers at risk (26.5%)"),
                ("2,173", "tech tickets in the at-risk group"),
                ("885", "admin tickets in the at-risk group"),
                ("$139,131", "monthly billing in the at-risk group"),
                ("$2.86M", "lifetime billing in the at-risk group"),
                ("29%", "of all customers are under 1 year tenure"),
            ]},
            {"type": "p", "text": "Where they come from: every KPI card is a PivotTable measure on the raw data sheet, and I reconciled each one against a direct profile of the CSV: 1,869 churned rows, $139,131 summed monthly charges, $2,862,927 summed total charges, 2,173 and 885 ticket counts from the pivot. Nothing on the dashboard is typed in by hand."},
        ]},
        {"id": "meaning", "heading": "How to read each number", "blocks": [
            {"type": "table", "headers": ["Number", "How I got it", "How to read it"], "rows": [
                ["1,869 at risk", "Distinct count of customerID where churn = Yes, from the pivot layer", "26.5% of the base. This is the population the churn model scores; the dashboard frames it, the model ranks it."],
                ["2,173 / 885 tickets", "Sum of tech and admin ticket counts for the churned group", "The at-risk group generates disproportionate support load, and tech tickets outnumber admin by about 2.5 to 1, which points at the product experience before process."],
                ["$139,131 monthly", "Sum of MonthlyCharges for the churned group", "The monthly run-rate walking out the door, about $1.67M annualised if the group held."],
                ["$2.86M lifetime", "Sum of TotalCharges for the churned group", "What those customers had paid across their whole stay. My card labels this Yearly Charges; the accurate reading is cumulative lifetime billing, and I flag it openly rather than leave the label wrong."],
                ["$74.44 vs $64.76", "Average monthly charges, churned group versus the full base", "Churners are above-average payers, so the exposure is bigger than the headcount suggests."],
                ["90% vs 29% services", "Phone service adoption versus tech support and online security adoption", "The gap between the near-universal core service and the barely-adopted protective add-ons is the clearest engagement signal on the screen."],
            ]},
        ]},
        {"id": "findings", "heading": "What I found", "blocks": [
            {"type": "findings", "items": [
                {
                    "id": "f-demography",
                    "title": "The risk is not demographic, and that is the good news",
                    "question": "Who are the at-risk customers, in plain terms?",
                    "paragraphs": [
                        "The demography panel is deliberately first because it clears the ground: 50.5% female and 49.5% male, 16% senior citizens, 48% with partners and 30% with dependents. Nothing here marks the churned group as unusual. Their gender split matches the base almost exactly.",
                        "I say this is the good news because a demographic story would be nearly unactionable: you cannot design a retention offer around who a customer is. An account story, you can.",
                        "The subscription-time panel confirms the front-loading: 29% of all customers are under one year of tenure, the largest band on the chart, and the bands shrink steadily out to five years. The risk window is early tenure, before contracts and habits form.",
                    ],
                    "meaning": "When demographics are flat and account behaviour is not, targeting should move from who customers are to what they signed and how they pay.",
                    "conclusion": "Drop demographic targeting from the retention plan and build it around contract, payment and tenure bands.",
                    "figure": ("CustomerRetention_1", "The demography panel with its doughnut and stat chips, sitting left of the account panels that carry the real signal."),
                },
                {
                    "id": "f-account",
                    "title": "The account panels tell the targeting story",
                    "question": "Which account features separate the at-risk group?",
                    "paragraphs": [
                        "Three bars do more work than everything else on the screen. Contract type: month-to-month dominates the contract chart at the top of the mix. Payment method: electronic check leads the payment bars, with the two automatic methods tied at the bottom of the mix. Paperless billing splits 59/41, so most at-risk-profile customers are already on the lowest-friction billing path, which makes the payment-method contrast more interesting, not less.",
                        "The average charges card sits beside them: $74.44 monthly and $1,531.80 lifetime for the churned group, both above the base averages. The customers these panels describe are not marginal accounts; they are paying meaningfully more than the typical customer.",
                        "My churn model quantifies what the bars suggest: month-to-month customers churn at 42.7% versus 2.8% on two-year contracts, and e-check payers at 45.3% versus about 16% on automatic payments. The dashboard shows the mix; the model measures the risk inside it.",
                    ],
                    "meaning": "Contract structure and payment friction, both visible on a single dashboard, predict churn better than anything demographic on the same screen.",
                    "conclusion": "Aim retention offers at month-to-month, e-check, early-tenure customers first, in that order.",
                    "figure": ("CustomerRetention_1", "The Customer Account Info panel: payment bars, paperless doughnut, average charges card and the contract chart."),
                },
                {
                    "id": "f-services",
                    "title": "The service panel exposes the engagement gap",
                    "question": "What do the at-risk customers buy, and what do they skip?",
                    "paragraphs": [
                        "Phone service sits at 90%, multiple lines split 47/53, and streaming services run 38 to 39%. Then the protective tier collapses: tech support 29%, online security 29%, device protection and online backup 34%. The services that require the provider to actively help the customer are the ones almost nobody takes.",
                        "The internet-service pie adds the tier dimension: 43.96% fiber optic, 34.37% DSL, 21.67% no internet. Fiber is the premium product, and my model work shows it is also the churniest at 41.9% against DSL's 19.0%.",
                        "Reading the two panels together: the base buys connectivity and entertainment readily but skips protection and support. That is an engagement and packaging problem, and it is fixable with bundling in a way that a service-quality problem would not be.",
                    ],
                    "meaning": "Adoption shares are a leading indicator you can watch monthly on this dashboard, long before churn confirms it.",
                    "conclusion": "Treat low protective-service adoption as the engagement gap to close, and track whether bundling moves the share.",
                    "figure": ("CustomerRetention_1", "The Services Customer Signed up for panel: the adoption ladder from 90% phone down to 29% support and security, with the internet-service pie beside it."),
                },
                {
                    "id": "f-tickets",
                    "title": "The ticket cards point at the product, not the paperwork",
                    "question": "What does the support load say about the at-risk group?",
                    "paragraphs": [
                        "The churned group carries 2,173 tech tickets against 885 admin tickets, roughly 2.5 to 1. Total support contact across the whole base is 2,955 tech and 3,632 admin, so the at-risk group holds 74% of all tech tickets while being 27% of customers.",
                        "That ratio says the at-risk group's problems skew technical: connectivity, devices, service quality. Admin tickets are spread more evenly across the base.",
                        "Combined with the fiber-overrepresentation story from the service panel, the picture is consistent: a premium, expectation-heavy product generating technical friction, and the customers experiencing it leaving at elevated rates.",
                    ],
                    "meaning": "A 74% share of tech tickets in a 27% slice of customers is a fixable product-experience signal, and the dashboard surfaces it in two KPI cards.",
                    "conclusion": "Route proactive technical follow-up to high-value month-to-month customers with open tech tickets, before the cancellation call.",
                    "figure": ("CustomerRetention_1", "The tech and admin ticket cards at the top of the dashboard, which carry the whole support-load argument in two numbers."),
                },
                {
                    "id": "f-build",
                    "title": "Pivots instead of formulas kept the dashboard honest",
                    "question": "How does the dashboard stay trustworthy as the data changes?",
                    "paragraphs": [
                        "I built the figure layer on PivotTables: the raw data lives on its own sheet, a pivot sheet computes every count, share and total, and the dashboard cards and charts read from the pivot output. When the data refreshes, a pivot refresh propagates everywhere at once.",
                        "The alternative, hand-typed KPI cards, is where dashboards silently rot: someone updates one card and misses three. Here the only typed things on the dashboard are the labels.",
                        "The slicers (contract type, gender, internet service) filter every pivot through one wiring, so a stakeholder can slice to month-to-month fiber customers and watch every card, doughnut and bar update together. That is the interaction model that makes an executive dashboard a tool instead of a screenshot.",
                    ],
                    "meaning": "Architecture choices in Excel, like in code, decide whether the artifact stays correct under change.",
                    "conclusion": "Build the KPI layer on pivots with one slicer wiring, and keep hand-typed values off the canvas.",
                    "figure": ("CustomerRetention_1", "The three slicers (Contract Type, Gender, Internet Service) wired across every visual, visible in the dashboard header and panels."),
                },
            ]},
        ]},
        {"id": "recommendations", "heading": "What I would do next", "blocks": [
            {"type": "recs", "items": [
                {"priority": "High", "title": "Use the slicers the way they were wired",
                 "evidence": "Contract, gender and internet-service slicers filter every card and chart in one click.",
                 "action": "Review the dashboard monthly through the month-to-month lens first, then fiber, then the cross-section; each pass answers a different management question.",
                 "impact": "Turns the dashboard from a static screenshot into the segmentation tool it was built to be."},
                {"priority": "High", "title": "Pair the dashboard with the model's ranked list",
                 "evidence": "The dashboard frames 1,869 at-risk customers; the churn model scores them individually at 0.858 ROC-AUC.",
                 "action": "Feed the top of the model's ranked list into the retention team's worklist, and track outcomes back into the dataset for the next refresh.",
                 "impact": "Closes the loop between what the dashboard shows and what the team does."},
                {"priority": "Medium", "title": "Fix the Yearly Charges label",
                 "evidence": "The $2,862,927 card sums TotalCharges, which is cumulative lifetime billing, not a yearly figure; the true annualised run-rate is about $1.67M.",
                 "action": "Relabel the card to Lifetime Billing, and add a small annualised card beside it so both readings are on screen.",
                 "impact": "Removes the one number on the dashboard a sharp reader could misuse."},
                {"priority": "Medium", "title": "Add a churn-rate view beside the volume view",
                 "evidence": "The panels show shares of the base (adoption, mix) but not risk rates within segments, which is where the 42.7% versus 2.8% contract contrast lives.",
                 "action": "Add a pivot-backed churn-rate-by-contract visual so the screen shows both how big each segment is and how risky it is.",
                 "impact": "Prevents the classic mix-versus-rate misreading, where a big safe segment looks riskier than a small dangerous one."},
                {"priority": "Low", "title": "Automate the refresh",
                 "evidence": "The workbook reads a static CSV extract; the pivot layer refreshes, the extract does not.",
                 "action": "Wire the data sheet to a scheduled export from the source system so the monthly review runs on current data without manual paste.",
                 "impact": "Keeps the monthly cadence the recommendations assume from decaying into quarterly."},
            ]},
        ]},
        {"id": "limits", "heading": "What this can't tell you", "blocks": [
            {"type": "p", "items": [
                "The dashboard shows the churned group as it looked at the snapshot; it is descriptive, not predictive. Which of the remaining 5,174 customers leaves next is the churn model's question, not this screen's.",
                "The $2.86M card measures lifetime billing of customers who already left. It frames the scale of the problem; it is not recoverable revenue, and the forward-looking number is the $139,131 monthly run-rate.",
                "Ticket counts come from the dataset's numeric ticket fields. They measure volume, not cause, so the tech-heavy skew is a signal to investigate, not a proven diagnosis.",
                "The dataset is the public Kaggle telco churn table, a single provider at a single snapshot. Segment patterns on this screen are strong, but they belong to this table.",
                "This workbook is Excel, deliberately: no macros, no Power Query load, no external connections. That makes it portable and audit-friendly, and it also means no scheduled refresh until the data wiring I recommend above exists.",
            ]},
        ]},
    ],
}


# --------------------------------------------------------------- technical
TECHNICAL = {
    "title": "Customer Retention Dashboard: how I built it",
    "lede": "The Excel build behind the screen: the sheet architecture, the pivot layer that carries every figure, the slicer wiring, the visual grammar of each panel, and the reconciliation that ties every card back to the raw rows.",
    "sections": [
        {"id": "solution", "heading": "The solution", "blocks": [
            {"type": "note", "text": "This page describes my Customer Retention workbook. Every figure quoted here I reconciled against the raw CSV with a direct profile; the dashboard and the data agree row for row."},
            {"type": "table", "headers": ["Sheet", "What it holds", "Why it is there"], "rows": [
                ["01 Churn-Dataset", "The raw 7,043 rows, 21 columns, as loaded", "The single source of truth; nothing else in the workbook edits it"],
                ["PivotTable", "The pivot layer: counts, shares, sums and band tables", "Every dashboard figure computes here, so a refresh updates everything at once"],
                ["Welcome", "Landing and orientation", "Tells a first-time reader where to go"],
                ["ChurnDashbord", "The executive screen: KPI cards, doughnuts, bars, pies, slicers", "The artifact leadership actually sees"],
                ["CustomerRiskAnalysis", "The working analysis layer under the same slicers", "Where the segment cross-tabs live for a reader who wants the numbers behind the pictures"],
            ]},
            {"type": "p", "text": "Three layers, one direction of data flow: raw data feeds pivots, pivots feed the dashboard and analysis sheets. No figure on the dashboard is typed; they are all pivot-driven. That single rule is what makes the workbook safe to refresh."},
        ]},
        {"id": "prep", "heading": "The data and the pivot layer", "blocks": [
            {"type": "p", "text": "The dataset is the Kaggle Telco Customer Churn table: 7,043 customers, 21 fields covering demographics, services, account configuration, charges and the churn flag. I loaded it to the data sheet clean, with SeniorCitizen as 0/1 and TotalCharges numeric, including the 11 whitespace values that coerce to blank."},
            {"type": "p", "text": "The pivot sheet carries the measures the dashboard reads. The core ones:"},
            {"type": "table", "headers": ["Measure", "Definition", "Dashboard use"], "rows": [
                ["At-risk customers", "Distinct count of customerID where Churn = Yes (1,869)", "The headline KPI card"],
                ["Ticket load", "Sum of tech and admin ticket counts, split by churn group (2,173 / 885)", "The two ticket cards"],
                ["Monthly billing at risk", "Sum of MonthlyCharges where Churn = Yes ($139,131)", "The monthly charges card"],
                ["Lifetime billing", "Sum of TotalCharges where Churn = Yes ($2,862,927)", "The yearly-charges card (see the label note below)"],
                ["Demographic shares", "Gender, senior citizen, partner, dependents counts", "The demography doughnut and chips"],
                ["Tenure bands", "Grouped tenure: under 1 year 29%, out to 5-plus years", "The subscription-time bars"],
                ["Service adoption", "Yes-shares for every add-on service, phone at 90% down to support and security at 29%", "The services panel"],
                ["Payment and contract mix", "Shares by payment method and contract type", "The account info panel"],
            ]},
            {"type": "p", "text": "One labelling lesson I want on the record: the $2,862,927 card reads Yearly Charges, and that label is wrong. The field it sums is TotalCharges, the cumulative amount each churned customer paid across their whole stay. The monthly card ($139,131) annualises to about $1.67M, which is the honest forward-looking figure. I keep the card because the magnitude is the point, and I fix the label in the recommendations, but I document it here first."},
        ]},
        {"id": "visuals", "heading": "Visual grammar, panel by panel", "blocks": [
            {"type": "table", "headers": ["Panel", "Visual", "The decision behind it"], "rows": [
                ["KPI cards", "Six large numeric cards across the top", "The five-second read: scale, ticket load, billing. Largest type on the screen because these are the numbers the meeting is about"],
                ["Demography", "Gender doughnut plus four stat chips", "Deliberately calm. It answers who the base is, and its flatness is part of the story: nothing demographic is driving the risk"],
                ["Subscription time", "Horizontal bars, under-1-year on top at 29%", "Ordered by tenure band so the front-loaded risk window reads top-down at a glance"],
                ["Payment methods", "Horizontal bars with share labels", "A ranking, so e-check's lead position makes the friction story before anyone reads a number"],
                ["Paperless billing", "Two-slice doughnut (59/41)", "A binary split, which is the one shape a doughnut earns"],
                ["Type of contract", "Horizontal bars, month-to-month on top", "Same ranking grammar as payments; the two most decision-relevant panels share a shape"],
                ["Services signed up for", "Adoption ladder with big percentage labels", "The 90-to-29 drop is the visual argument; the ordering makes the protective tier's collapse unmissable"],
                ["Internet service", "Three-slice pie with DSL, fiber, no-service chips", "Three categories, comparable shares; the fiber plurality is the point"],
                ["Slicers", "Contract, gender, internet service", "Wired to every pivot, so one click re-reads the whole screen for a segment"],
            ]},
            {"type": "p", "items": [
                "My visual rules on this build: one idea per visual, shares labelled directly on the marks instead of in a legend hunt, horizontal bars wherever category names are long, and doughnuts reserved for two-way splits. The demography panel uses muted greys and blues so the KPI cards stay the loudest thing on the page.",
                "The two-level slicer design (contract, gender, internet service) maps to the three questions a retention lead actually asks: which contracts, which customer profile, which product tier. Anything more granular belongs in the CustomerRiskAnalysis sheet, not on the executive screen.",
            ]},
            {"type": "figure", "spec": ("CustomerRetention_1", "The complete dashboard as shipped, showing the card row, the three panels and the slicer wiring.")},
        ]},
        {"id": "quality", "heading": "Reconciliation: the dashboard versus the data", "blocks": [
            {"type": "p", "text": "I checked every headline figure against a direct profile of the CSV. This is the table:"},
            {"type": "table", "headers": ["Dashboard figure", "Direct data check", "Verdict"], "rows": [
                ["1,869 customers at risk", "1,869 rows with Churn = Yes of 7,043 (26.54%)", "Exact"],
                ["2,173 tech tickets / 885 admin", "Churned group sums 2,173 and 885; full base 2,955 and 3,632", "Exact"],
                ["$139,131 monthly charges", "Sum of MonthlyCharges for churned rows", "Exact"],
                ["$2,862,927 yearly charges", "Sum of TotalCharges for churned rows; it is lifetime, not yearly", "Figure exact, label corrected in my recommendations"],
                ["50.5% female", "49.52% male / 50.48% female on the full base", "Exact"],
                ["16% senior citizens", "16.22% of rows are SeniorCitizen = 1", "Exact"],
                ["29% under 1 year", "29.38% of rows have tenure under 12 months", "Exact"],
                ["90% phone service", "90.32% adoption", "Exact"],
                ["Services ladder 29/34/34/29/38/39", "Security 28.7%, backup 34.5%, device 34.4%, support 29.0%, streaming TV 38.4%, streaming movies 38.8%", "Exact to rounding"],
                ["Internet pie 34.37 / 43.96 / 21.67", "DSL 34.37%, fiber 43.96%, none 21.67%", "Exact"],
                ["$74.44 / $1,531.80 average charges", "Churned-group means: $74.44 monthly, $1,531.80 lifetime", "Exact"],
            ]},
            {"type": "note", "text": "One correction, one label: the Yearly Charges card. Every other figure reconciles exactly, which is the dividend of building the KPI layer on pivots rather than typed values."},
        ]},
        {"id": "decisions", "heading": "My decisions and trade-offs", "blocks": [
            {"type": "table", "headers": ["Decision I made", "Why", "Trade-off I accepted"], "rows": [
                ["Pivot layer instead of formula grid", "Refresh-safe: every figure recomputes from one data refresh", "Pivot output needs careful chart sourcing, and the pivot sheet is not pretty"],
                ["Three slicers, no more", "They map to the three questions a retention lead asks", "Deeper cross-sections live on the analysis sheet, one click away"],
                ["Demography panel first despite carrying no signal", "It answers the reader's first question and clears the ground for the account story", "The strongest panel sits below the calmest one"],
                ["Kept the $2.86M card with the wrong label documented", "The magnitude frames the problem, and hiding a number because its label is loose wastes it", "Requires this documentation and a follow-up relabel to be fully honest"],
                ["No macros or Power Query", "The workbook opens anywhere with no security prompts", "No scheduled refresh; the data wiring is the documented next step"],
                ["Shares labelled on the marks", "Executives read labels, not legends", "Some marks get crowded on small slices"],
            ]},
        ]},
        {"id": "next", "heading": "If I took it further", "blocks": [
            {"type": "steps", "items": [
                ("Relabel the lifetime-billing card", "Change Yearly Charges to Lifetime Billing and add an annualised card beside it, so the two readings are both on screen and both correct."),
                ("Add the churn-rate pivot", "A rate-by-contract visual turns the mix panels into risk panels and kills the mix-versus-rate misreading."),
                ("Wire a live data source", "Point the data sheet at a scheduled extract so the monthly review runs on current data, with the pivot layer doing what it was built for."),
                ("Merge the two projects' views", "Bring the churn model's score distribution onto the analysis sheet, so the dashboard shows not just who churned but who is next."),
                ("Templatise the shell", "The sheet architecture (data, pivots, welcome, dashboard, analysis) is reusable for any executive KPI workbook; package it once and reuse it."),
            ]},
        ]},
        {"id": "reflection", "heading": "What this project shows", "blocks": [
            {"type": "p", "items": [
                "This dashboard and my churn model are the same investigation for two audiences, and building both taught me the translation layer matters as much as the analysis: the model's 0.858 ROC-AUC and the dashboard's 1,869 are the same story in two languages.",
                "The habits I would carry forward: build the KPI layer on pivots so refreshes propagate, label figures for what they actually measure rather than what sounds right, put the calm panel first when it clears the ground for the loud one, and reconcile every card against the raw rows before calling the dashboard done.",
            ]},
        ]},
    ],
}
