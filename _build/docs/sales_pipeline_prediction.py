"""
CRM Sales Analytics documentation content.
Sources: the project zip (notebook with saved outputs, models.py, main.py,
test.py, Dockerfile, both SQL scripts, the Power BI PBIP model files with
the DAX measure tables, the four CSVs and the test summary report).

Every number on these pages traces to metrics.json, the file the
canonical training run writes, plus the test summary report and the CSV
profiles. The tone is portfolio, not audit: the pages present what the
work is and the decisions behind it, framed forward. The saved
evaluation is quoted: ROC-AUC 0.6085, accuracy 62.8%, precision 63.8%,
recall 94.8% at the shipped 0.5 threshold.

Rules: first person, plain words, no em dashes, only supported claims.
Code is copied as stored and only re-indented; excerpts say what was cut.
The dataset is a public CRM practice dataset and every page says so.
"""


# ---------------------------------------------------------------- diagram
def _box(x, y, w, h, title, subs, cls=""):
    cx = x + w / 2
    out = f'<rect class="dg-box {cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="12"/>'
    top = y + (h - 14 * len(subs)) / 2 + 2 if subs else y + h / 2
    out += f'<text class="dg-t" x="{cx}" y="{top - 6}" text-anchor="middle">{title}</text>'
    for i, sub in enumerate(subs):
        out += f'<text class="dg-s" x="{cx}" y="{top + 14 + i * 14}" text-anchor="middle">{sub}</text>'
    return out


def _arch_svg():
    s = ['<svg viewBox="0 0 920 480" role="img" class="dg" '
         'aria-label="Architecture: CSV files, a SQL Server database cleaned by two scripts, '
         'a Power BI branch, and a Python branch that trains an XGBoost model, pickles it '
         'and serves it through FastAPI in Docker">'
         '<defs><marker id="dgA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
         'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="dg-head"/></marker></defs>']
    # data and descriptive branch
    s.append(_box(6, 30, 180, 84, "CSV files", ["4 tables + dictionary", "8,800 opportunities"]))
    s.append(_box(226, 30, 200, 84, "SQL Server", ["CRM_Sales_Opportunity", "cleaned by 2 scripts"]))
    s.append(_box(466, 30, 210, 84, "Power BI report", ["3 pages, DAX measures"], "dg-model"))
    # modelling branch
    s.append(_box(226, 190, 200, 92, "Python (pyodbc)", ["JOIN drops Prospecting", "8,300 rows in"], "dg-model"))
    s.append(_box(466, 190, 210, 92, "Feature engineering", ["28 features", "experiment-driven"], "dg-model"))
    s.append(_box(716, 190, 190, 92, "XGBoost", ["repeated CV, one test eval"], "dg-measure"))
    # serving branch
    s.append(_box(226, 350, 200, 84, "test.py summary", ["1,589 open deals scored"]))
    s.append(_box(466, 350, 210, 84, "Model artifact", ["pickled pipeline + metrics.json"], "dg-measure"))
    s.append(_box(716, 350, 190, 84, "FastAPI in Docker", ["port 9696, logged runs"], "dg-measure"))
    # connectors
    line = lambda d, extra="": s.append(f'<path class="dg-line {extra}" d="{d}" marker-end="url(#dgA)"/>')
    line("M186,72 L226,72")
    line("M426,72 L466,72")
    line("M326,114 L326,190")
    line("M426,236 L466,236")
    line("M676,236 L716,236")
    line("M811,282 L811,316 L571,316 L571,350")
    line("M676,392 L716,392")
    line("M811,434 L811,462 L326,462 L326,434")
    # connector labels
    lbl = lambda x, y, t, a="middle": s.append(f'<text class="dg-l" x="{x}" y="{y}" text-anchor="{a}">{t}</text>')
    lbl(334, 152, "pyodbc SELECT", "start")
    lbl(600, 310, "pickle", "start")
    lbl(560, 456, "scores open deals")
    # legend
    s.append('<rect class="dg-box dg-model" x="8" y="458" width="14" height="14" rx="3"/>')
    lbl(30, 469, "Model tables and code", "start")
    s.append('<rect class="dg-box dg-measure" x="180" y="458" width="14" height="14" rx="3"/>')
    lbl(202, 469, "Trained artefacts and measures", "start")
    s.append("</svg>")
    return "".join(s)


ARCH_SVG = _arch_svg()


# ---------------------------------------------------------------- business
BUSINESS = {
    "title": "CRM Sales Analytics: what the model is worth",
    "lede": "A cleaned SQL layer, a Power BI dashboard for what happened, and an XGBoost model behind a FastAPI service for what might happen next. This page covers what each layer does, what the model says about the 1,589 open deals, and where every number comes from in my own saved outputs.",
    "sections": [
        {"id": "problem", "heading": "The problem", "blocks": [
            {"type": "note", "text": "The data is a public CRM practice dataset (a sales pipeline with accounts, products and sales teams). SPOTA, the company in the brief, is the fictional framing I wrote the project against. Nothing here measures a real company's revenue."},
            {"type": "p", "items": [
                "The brief describes a B2B company with the usual sales reporting problems: performance scattered across regions, products and agents; no shared view of the funnel; no way to know which open deals deserve attention; and coaching decisions made on gut feel.",
                "I built three things that answer it in layers. A SQL Server database with two cleaning scripts, so every consumer reads the same corrected tables. A three-page Power BI dashboard with DAX measures for the descriptive questions: revenue, win rates, agent rankings, month over month movement. And the predictive layer: an XGBoost model trained on closed deals, wrapped in a FastAPI service, containerised with Docker, and run against all 1,589 open deals in the data.",
                "The model answers one question per deal: given what similar agents, accounts, products and sectors have done before, is this open deal likely to be won?",
            ]},
        ]},
        {"id": "answer", "heading": "The short answer", "blocks": [
            {"type": "verdict", "text": "Three layers, one question per layer. A cleaned SQL layer gives everyone the same corrected tables, a Power BI dashboard answers what happened, and an XGBoost model behind a FastAPI service ranks the open pipeline for what might happen next. On the saved evaluation the tuned model separates winners from losers about 60% of the time (ROC-AUC 0.6085 on the held-out test set), and at the shipped threshold it catches 95% of the real winners while 64% of its win calls are right, so I position it as a ranking aid for working the top of the list, not a forecast. Every number on this page traces to one metrics file the training run wrote, and each one says where it comes from."},
            {"type": "figure", "spec": ("SalesPipeline_1", "The descriptive layer, live: page one of the Power BI dashboard. Four headline KPIs carry the month-over-month arrows from the DAX trio, and the drilldowns cover agents, revenue trend and geography.")},
        ]},
        {"id": "numbers", "heading": "Numbers at a glance", "blocks": [
            {"type": "stat_grid", "items": [
                ("8,800", "opportunities in the pipeline data"),
                ("6,711", "closed deals the model learned from"),
                ("63.2%", "historical win rate on closed deals"),
                ("1,589", "open deals scored through the API"),
                ("0.6085", "ROC-AUC on the held-out test set"),
                ("28", "features, after experiment-driven pruning"),
            ]},
            {"type": "p", "text": "Where they come from: I profiled the pipeline CSV directly for the stage counts and win rate, my test summary report holds the scoring counts, and metrics.json, the file my training run writes on every run, holds the model numbers."},
        ]},
        {"id": "meaning", "heading": "How to read each number", "blocks": [
            {"type": "table", "headers": ["Number", "How it is worked out", "How to read it"], "rows": [
                ["8,800 opportunities", "Row count of the pipeline table", "The whole book: 4,238 won, 2,473 lost, 1,589 engaging, 500 prospecting."],
                ["6,711 closed deals", "Won plus lost rows", "The only deals with a known outcome, so the only ones a model can learn from or be tested on."],
                ["63.2% historical win rate", "Won divided by closed deals", "The baseline the open pipeline gets compared against."],
                ["1,589 scored deals", "The engaging rows, run through the API", "Open deals with no outcome yet, so accuracy cannot be computed on them. The scoring run is a path test."],
                ["ROC-AUC 0.6085", "Tuned model, held-out test set", "Pick one won and one lost deal at random: the model ranks the winner first about 60% of the time. 0.5 is a coin flip."],
                ["63.8% precision, 94.8% recall", "Share of predicted wins that actually won, and share of real winners caught, at the shipped threshold", "It flags nearly every winner and calls some losers wins too. Read it when missing a winner is expensive; the probability is the real output."],
            ]},
        ]},
        {"id": "findings", "heading": "What I found", "blocks": [
            {"type": "findings", "items": [
                {
                    "id": "f-signal",
                    "title": "The model ranks deals, it does not predict them",
                    "question": "How good is the model, really?",
                    "paragraphs": [
                        "On the saved evaluation the tuned model reaches a ROC-AUC of 0.6085 on the held-out test set, with 62.8% accuracy. Naively calling every deal won would score 63.1% accuracy on the same set, so raw accuracy is not the story; the ranked win probabilities are.",
                        "The path is traceable in one metrics file: a slim-feature baseline cross-validated at 0.591, the search's best five-fold candidate at 0.612, the winner confirmed at 0.613 across three repeats of five folds, and one single evaluation on the untouched test set landing at 0.6085. The test set is scored exactly once, after selection is finished.",
                    ],
                    "meaning": "The useful output is a ranked list of open deals, not a predicted outcome. Ranking is exactly what a sales coach needs: work the top of the list first.",
                    "conclusion": "Quote ROC-AUC 0.6085 (tuned model, held-out test) and treat the model as a ranking aid.",
                },
                {
                    "id": "f-pipeline",
                    "title": "The scoring run was a path test, not a pipeline read",
                    "question": "What does the model say about the deals that are open right now?",
                    "paragraphs": [
                        "The deployed API scored all 1,589 open deals, and every one came back predicted to win, with probabilities from 0.65 to 0.87. The repo documents the run as illustrative, for a good reason: the deals are from 2016 and 2017, so at serve time each one is computed as roughly nine years old, far outside anything the model saw in training, where closed deals averaged about 48 days of age.",
                        "Feeding a nine-year-old deal into a model trained on weeks-old deals can only produce extreme outputs. The run proves the serve path works end to end; it does not describe a live pipeline, because this dataset is closed history rather than a working CRM.",
                    ],
                    "meaning": "A scoring service is only as current as the data feeding it. On fresh deals with recent engage dates, the same path would produce usable scores. On this vintage it can only show that the plumbing works.",
                    "conclusion": "Re-run the scoring on fresh engage dates before reading anything into predicted win shares.",
                },
                {
                    "id": "f-precision",
                    "title": "The threshold is a business decision, and the numbers move with it",
                    "question": "What do the numbers mean at the threshold the API actually uses?",
                    "paragraphs": [
                        "At the shipped 0.5 threshold, the test evaluation gives precision of 63.8% (of the deals called wins, 63.8% actually won) and recall of 94.8% (it caught nearly every real winner). Because 63.2% of closed deals were won anyway, calling everything a win would score 63.2% precision, so at this operating point the model's edge shows in the ranking, not in the flag.",
                        "The training run also tuned the threshold on out-of-fold training predictions and landed at 0.425, which pushes recall to 100% on the test set. The API ships 0.5 and reports both probabilities on every call, so a caller can apply any cutoff their use case needs.",
                    ],
                    "meaning": "A coaching tool that must not miss a likely winner wants the low threshold. A tool that acts on every flag wants a higher one and better precision. The shipped setup serves the first.",
                    "conclusion": "Publish the threshold next to every precision and recall number, and choose it per use case.",
                },
                {
                    "id": "f-data",
                    "title": "Most of the missing values were structural, not dirty",
                    "question": "How much cleaning did the data actually need?",
                    "paragraphs": [
                        "2,089 of the 8,800 rows have no close value and no close date. That is exactly the count of the open deals: 1,589 engaging plus 500 prospecting. Those blanks are the pipeline working as expected, not a quality problem.",
                        "The real catches were elsewhere. The sector field holds the spelling error 'technolgy' in 12 accounts, which the cleaning script's case normalization does not fix. 1,425 rows have no account at all. The subsidiary_of column was 82.4% blank and was dropped. There are no duplicate opportunity ids, so the SQL deduplication step is a safety net that found nothing to delete.",
                    ],
                    "meaning": "The cleaning script ends with an audit query that counts nulls per deal stage. That instinct, measure then decide, is what makes the structural nulls visible as a pattern instead of a panic.",
                    "conclusion": "Treat nulls as information. These ones reconciled exactly to the deal stages.",
                },
                {
                    "id": "f-spread",
                    "title": "Won deal values span three orders of magnitude",
                    "question": "What does the revenue data actually look like?",
                    "paragraphs": [
                        "Won deals run from $38 to $30,288, averaging $2,361, for a total of $10.0M in closed revenue. A spread that wide means the average describes very few real deals, and a quarter's revenue can hinge on a handful of them.",
                        "It also explains two modelling choices. Tree-based learners tolerate skew that would distort a linear model, and company size enters as a log transform, so a 34,000-employee account does not dominate every split.",
                    ],
                    "meaning": "Any revenue conversation should start from the distribution, not the average. The dashboard keeps deal size next to its own month-over-month movement for exactly this reason.",
                    "conclusion": "Report the spread alongside the mean, and treat aggregate forecasts as ranges.",
                },
            ]},
        ]},
        {"id": "recommendations", "heading": "What I would do next", "blocks": [
            {"type": "recs", "items": [
                {"priority": "High", "title": "Use the ranking, not the label",
                 "evidence": "At the shipped threshold the model flags nearly every deal as a win; the ranked probabilities, not the label, are the usable output.",
                 "action": "Work the scored list top down for coaching calls, and review the bottom of the list for pipeline hygiene, instead of treating WON or LOST as verdicts.",
                 "impact": "Coach time goes where the model actually sees signal."},
                {"priority": "High", "title": "Label the open deals when they close, then re-measure",
                 "evidence": "The 1,589 scored deals have no outcomes yet, so production accuracy is unmeasured.",
                 "action": "Join eventual outcomes back to the scored CSV and compute precision and recall on real future deals.",
                 "impact": "Replaces the held-out test estimate with a measured production number."},
                {"priority": "High", "title": "Score on fresh deals, not the 2016-17 vintage",
                 "evidence": "Serve-time deal age is computed from the engage date, so stale deals land years outside the training range and the scoring run came back all-wins.",
                 "action": "Bound-check engage_date at the API edge, and schedule scoring runs on current data.",
                 "impact": "Predicted win shares become readable as pipeline health."},
                {"priority": "Medium", "title": "Raise the threshold if win flags drive automation",
                 "evidence": "Precision is 63.8% at the shipped 0.5, with recall at 94.8%.",
                 "action": "If win flags feed automated actions, raise the cutoff and quote the precision and recall measured at the new point.",
                 "impact": "Fewer false alarms for anything downstream that acts on the flag."},
                {"priority": "Medium", "title": "Validate category spelling on entry",
                 "evidence": "The sector value 'technolgy' survives in 12 accounts because the cleaning only normalises case.",
                 "action": "Enforce a sector list in SQL or at data entry, and backfill the typo.",
                 "impact": "Group-bys and dashboards stop splitting technology into two buckets."},
                {"priority": "Medium", "title": "Pick the cutoff per use case at the caller",
                 "evidence": "The OOF-tuned 0.425 threshold is stored in the artifact; the API ships 0.5 with both probabilities on every response.",
                 "action": "Quote the metrics measured at whichever cutoff a use case applies, not just the shipped one.",
                 "impact": "Metrics and behaviour stay aligned as new use cases grow."},
            ]},
        ]},
        {"id": "limits", "heading": "What this can't tell you", "blocks": [
            {"type": "p", "items": [
                "The data is a public practice dataset, so no conclusion here describes a real company's pipeline or revenue.",
                "The 1,589 scored deals have no outcomes yet, so there is no production accuracy number, only the held-out test evaluation. The scoring run itself is illustrative: stale engage dates push deal age far outside the training range.",
                "A ROC-AUC of 0.6085 estimated from about 6,700 deals carries real uncertainty, and accuracy (62.8%) sits at the naive always-win baseline (63.1%); the value is in the ranking, not the flag.",
                "This project does not produce a revenue forecast. The forecast-accuracy numbers in the business brief are targets, not measurements.",
                "The Power BI dashboard and the model share the database but were evaluated separately; I did not re-run the report visuals for this write-up.",
            ]},
        ]},
    ],
}


# --------------------------------------------------------------- technical
TECHNICAL = {
    "title": "CRM Sales Analytics: how it was built",
    "lede": "The full pipeline: the SQL cleaning layer, the Python feature engineering and its leakage decisions, the model with its real evaluation numbers, the FastAPI service in Docker, and the DAX behind the Power BI dashboard.",
    "sections": [
        {"id": "solution", "heading": "The solution", "blocks": [
            {"type": "note", "text": "The code on this page is straight from my project files, only re-indented. Long functions are excerpts and say what I cut. Every number traces to metrics.json, the file my training run writes, plus my test summary report and my profiles of the raw CSVs."},
            {"type": "p", "text": "I built the project as one pipeline with three consumers. CSVs load into a SQL Server database, where two scripts clean and enrich the tables. The Power BI report reads those tables for the descriptive questions. The Python branch pulls a joined extract, engineers a compact 28-feature set, cross-validates and tunes on the training split only, evaluates once on the held-out test set, and pickles the model with a metrics file. A FastAPI service loads the pickle and serves predictions from Docker, and a test script scored the 1,589 open deals and wrote the summary report the business page discusses."},
            {"type": "svg", "svg": ARCH_SVG, "caption": "How the pieces connect. The Power BI branch answers what happened; the Python branch predicts which open deals will close. Both read the same cleaned SQL Server layer."},
            {"type": "table", "headers": ["Component", "Where it lives", "Role"], "rows": [
                ["SQL Server database", "CRM_Sales_Opportunity", "Cleaned fact and dimension tables"],
                ["SQL cleaning scripts", "SQL Scripts (2 files)", "Flags, imputations, deduplication, account tiers, audit query"],
                ["Power BI report", "CRM Recovered.pbip", "Three-page descriptive dashboard"],
                ["DAX measures", "4 measure tables in the model", "KPIs, month-over-month arrows, agent rankings, conditional formatting"],
                ["Training code", "models.py with experiments.py and tune.py", "Feature experiments, CV, tuning, single test evaluation, metrics file"],
                ["API", "main.py (FastAPI)", "predict, predict-batch, health and metrics endpoints"],
                ["Container", "Dockerfile", "Slim Python 3.13 image, pipenv dependencies, port 9696"],
                ["Scoring script", "test.py", "Scores the 1,589 open deals, writes the summary report"],
            ]},
        ]},
        {"id": "data", "heading": "The data and profiling", "blocks": [
            {"type": "p", "text": "Four tables carry the model and the report. When I profiled the CSVs directly, I got:"},
            {"type": "table", "headers": ["Table", "Rows", "What it holds"], "rows": [
                ["sales_pipeline", "8,800", "One row per opportunity: agent, product, account, deal stage, engage date, close date, close value"],
                ["accounts", "85", "Sector, year established, revenue, employees, office location"],
                ["products", "7", "The product catalogue"],
                ["sales_teams", "35", "Agent, manager, regional office"],
            ]},
            {"type": "table", "headers": ["Check", "Result", "What it means"], "rows": [
                ["Deal stages", "Won 4,238, Lost 2,473, Engaging 1,589, Prospecting 500", "6,711 closed deals for training; 1,589 open deals to score; 500 too early to judge"],
                ["Win rate on closed deals", "63.2%", "The baseline the open pipeline is compared against"],
                ["Dates", "Engagements Oct 2016 to Dec 2017; closings Mar to Dec 2017", "About 14 months of history"],
                ["Missing close value and close date", "2,089 rows each", "Exactly the engaging plus prospecting rows. Structural, not dirty"],
                ["Missing account", "1,425 rows", "Cleaned to 'Unknown' in SQL so joins survive"],
                ["Duplicate opportunity ids", "0", "The SQL deduplication is a safety net"],
                ["Won close values", "Sum $10.0M, mean $2,361, range $38 to $30,288", "Right-skewed, which is why the model uses a log-transformed employee count and tree-based learners"],
                ["Sector values", "Includes 'technolgy' in 12 accounts", "A spelling error that case normalization does not fix"],
            ]},
        ]},
        {"id": "sql", "heading": "The SQL cleaning layer", "blocks": [
            {"type": "p", "text": "Two scripts run against the raw tables before anything reads them. The pipeline script adds an active-deal flag, fixes structural nulls, standardises text, deduplicates, and ends with an audit query."},
            {"type": "code", "title": "Sales_pipeline cleaning.sql", "lang": "sql", "code": r'''
--Creating a new is_active column to track early stage deals
ALTER TABLE [dbo].[sales_pipeline]
ADD is_active BIT;

--Flag early stage deals as is_active (Engaging, lead, prospect)
UPDATE [dbo].[sales_pipeline]
SET is_active = CASE
                    WHEN deal_stage IN ('Engaging', 'Lead', 'Prospect') THEN 1
                    ELSE 0
                END;

-- Fix Null in close_value for deals not yet Won (set to 0)
UPDATE [dbo].[sales_pipeline]
SET [close_value] = 0
WHERE close_value IS NULL AND deal_stage != 'Won';

-- Fix Null close_date for closed deals either won or lost set as currrent date
UPDATE [dbo].[sales_pipeline]
SET [close_date] = GETDATE()
WHERE [close_date] IS NULL AND deal_stage IN ('Won', 'Lost');

--Handling Null account(Primary Key) set as Unknown
UPDATE [dbo].[sales_pipeline]
SET [account] = 'Unknown'
WHERE [account] IS NULL ;

--Capitalize deal_stage consistently
UPDATE [dbo].[sales_pipeline]
SET [deal_stage] = UPPER(LEFT([deal_stage],1)) + LOWER(SUBSTRING([deal_stage], 2, LEN([deal_stage])));

--Removing any duplicate opportunities(keep the earliest engaging_date) if any
WITH Duplicates_opp AS (
    SELECT [opportunity_id],
        ROW_NUMBER() OVER(PARTITION BY [opportunity_id] ORDER BY [engage_date] ASC) rn
    FROM [dbo].[sales_pipeline]
)
DELETE FROM [dbo].[sales_pipeline]
WHERE [opportunity_id] IN (
    SELECT [opportunity_id]
    FROM Duplicates_opp
    WHERE rn > 1
);

-- Audit summary by deal_stage
SELECT
    [deal_stage],
    COUNT(*) total_opportunities,
    SUM(CASE WHEN [account] IS NULL THEN 1 ELSE 0 END) null_acct,
    SUM(CASE WHEN [close_date] IS NULL THEN 1 ELSE 0 END) null_close_date,
    SUM(CASE WHEN [close_value] IS NULL THEN 1 ELSE 0 END) null_close_values
FROM [dbo].[sales_pipeline]
GROUP BY [deal_stage]
ORDER BY total_opportunities DESC
'''},
            {"type": "p", "text": "The account script standardises sector case, drops a column that is mostly blank, and buckets every account by size. The bucket boundaries then live in the database, so the dashboard, the model and any other consumer see the same tiers."},
            {"type": "code", "title": "account cleaning.sql", "lang": "sql", "code": r'''
--Capitalize sector consistently
UPDATE [dbo].[accounts]
SET [sector] = UPPER(LEFT([sector],1)) + LOWER(SUBSTRING([sector], 2, LEN([sector])));

--Drop subsidiary column since its have 80% Null
ALTER TABLE [dbo].[accounts]
DROP COLUMN [subsidiary_of];

--Creating a new account_tier column to categorize business account by employees
ALTER TABLE [dbo].[accounts]
ADD account_tier VARCHAR(20);

--Categorizing account into tiers based on employees
UPDATE [dbo].[accounts]
SET [account_tier] = CASE
                        WHEN [employees] BETWEEN 1 AND 9 THEN 'Micro_Enterprise'
                        WHEN [employees] BETWEEN 10 AND 49 THEN 'Small_Enterprise'
                        WHEN [employees] BETWEEN 50 AND 249 THEN 'Medium_Enterprise'
                        ELSE 'Large_Enterprise'
                     END;
'''},
            {"type": "sub", "text": "Design notes"},
            {"type": "pairs", "items": [
                ("GETDATE() invents close dates", "Writing today's date into deals that closed months ago corrupts any duration analysis. Keep the null and flag the row, or use a known audit date."),
                ("'Unknown' hides the gap", "1,425 deals with no account still exist, just under a label. Keep a flag column so the gap stays countable."),
                ("DELETE without an archive", "The deduplication deletes rows outright. In this dataset it found zero duplicates, but on real data it should write them to a quarantine table first."),
                ("The ELSE bucket catches nulls", "An account with a null employee count falls through to Large_Enterprise. Add an explicit null branch or a check constraint."),
                ("Case fixes are not spellcheck", "'technolgy' survives the capitalisation. Category fields need a domain list, not string functions."),
            ]},
        ]},
        {"id": "features", "heading": "The extract and feature engineering", "blocks": [
            {"type": "p", "text": "Python pulls one joined extract and leaves prospecting behind, since those deals are too early to have a knowable outcome."},
            {"type": "figure", "spec": ("SalesPipeline_9", "The raw sales_pipeline CSV before any cleaning: one row per opportunity with agent, product, account, stage, dates and value. The Engaging rows visible here are the 1,589 the model later scores; Prospecting rows are the ones the extract leaves behind.")},
            {"type": "code", "title": "The training extract (models.py)", "lang": "python", "code": r"""
query = '''
SELECT p.*,
    a.sector, a.year_established, a.account_tier, a.employees, a.office_location,
    s.manager, s.regional_office
FROM dbo.sales_pipeline p
LEFT JOIN accounts a ON a.account = p.account
LEFT JOIN sales_teams s ON p.sales_agent = s.sales_agent
WHERE deal_stage NOT IN ('Prospecting')
'''

df = pd.read_sql(query, conn)
conn.close()
"""},
            {"type": "p", "text": "That leaves 8,300 rows: 6,711 closed deals for training and evaluation, and 1,589 engaging deals held aside for scoring. Company size gets a log transform and six buckets, because employee counts run from 9 to 34,288 and the biggest companies would otherwise dominate every split."},
            {"type": "code", "title": "Company size features (notebook cells 9 and 10)", "lang": "python", "code": r'''
#since only few companies are this large, we capped the outliers
df["employees_log"] = np.log1p(df['employees'])

bins = [0, 50, 250, 1000, 5000, 15000, np.inf]
labels = ['micro', 'small', 'medium', 'large', 'enterprise', 'mega']
df["company_size"] = pd.cut(df['employees'], bins=bins, labels=labels).astype(str)
'''},
            {"type": "p", "text": "Deal age is the one duration feature that works for both closed and open deals: for closed deals it is the engage-to-close span, for open deals it is how long the deal has been alive as of the reference date."},
            {"type": "code", "title": "Deal age (notebook cell 28)", "lang": "python", "code": r'''
df['closed_duration'] = (df['close_date'] - df['engage_date']).dt.days
df['active_duration'] = (ref_date - df['engage_date']).dt.days
df['deal_age'] = df['closed_duration'].fillna(df['active_duration'])
'''},
            {"type": "p", "text": "The first version of this model carried 21 more features: hand-rolled win rates, deal counts and win counts per agent, account, sector, office, region, company size and product, always computed on the training split only so the encodings could not peek at held-out data. An experiment harness then measured whether they actually helped."},
            {"type": "code", "title": "The experiment harness and its honesty rule (experiments.py, excerpt)", "lang": "python", "code": r'''
for tr_idx, val_idx in skf.split(train_df, train_df['target']):
    fold_tr, fold_val = train_df.iloc[tr_idx], train_df.iloc[val_idx]
    # within each fold, the win-rate statistics are computed on the
    # FOLD-TRAIN rows only and mapped onto the fold-validation rows
    feat_tr = build_features(fold_tr, fold_tr, use_stats)
    feat_val = build_features(fold_tr, fold_val, use_stats)
    m = make_pipeline(kind, cv_params, num, cat)
    m.fit(feat_tr[num + cat], feat_tr['target'])
    aucs.append(roc_auc_score(feat_val['target'],
                              m.predict_proba(feat_val[num + cat])[:, 1]))
'''},
            {"type": "p", "text": "Five configs ran through it, with and without the hand-rolled statistics, plus a second round that searched XGBoost and LightGBM around the winner. The result was clear enough to act on: the statistics largely duplicate what the CatBoost target encoding already learns, and estimated from small, noisy groups they hurt out-of-sample discrimination, 0.57 cross-validated with them against 0.61 without. They were cut, and a proven winner from the tuning rounds stays locked into the final re-rank pool so a retrain can only match or improve on it."},
            {"type": "code", "title": "The slim feature set (models.py)", "lang": "python", "code": r'''
numerical = [
    'year_established', 'employees_log', 'deal_age',
    'agent_product_synergy', 'agent_win_efficiency', 'agent_vs_sector',
    'deal_complexity', 'office_load', 'product_sector_fit',
    'region_size_match', 'quarter_risk', 'is_quarter_end',
    'sales_velocity_ratio', 'pace_weighted_agent_score',
    'velocity_complexity_index',
    'month_engaged', 'quarter_engaged', 'day_of_week_engaged',
    'is_weekend', 'days_into_year',
]
categorical = ['sales_agent', 'product', 'account', 'sector',
               'office_location', 'manager', 'regional_office', 'company_size']
'''},
            {"type": "p", "text": "The interaction block survives from the earlier design. The features driven by deal age and company size still carry signal; the ones built on the removed statistics now collapse to constants that a tree either splits on or ignores. The experiments say the model does not miss the removed information, because the CatBoost encoding reconstructs the category effects from the categories themselves."},
            {"type": "sub", "text": "Dropping leakage"},
            {"type": "code", "title": "Leakage columns (notebook cell 16)", "lang": "python", "code": r'''
leakage_columns = ['close_date', 'close_value', 'is_active', 'deal_duration',
                   'opportunity_id', 'employees', 'account_tier']
df_training = df_training.drop(columns=leakage_columns, errors='ignore')
'''},
            {"type": "p", "text": "Only the first three are true leakage: close_date and close_value do not exist until a deal finishes, and is_active is derived from the stage the model is trying to predict. opportunity_id is an identifier, and employees and account_tier are dropped because their log and bucket versions replace them. Dropping close_value is the whole game here: a model that sees the deal's final value has read the answer off the row. That single decision is why the reported metrics can be believed at all."},
        ]},
        {"id": "model", "heading": "The model", "blocks": [
            {"type": "p", "text": "Training is one script (models.py). The pipeline is CatBoost encoding for the eight categorical columns and scaling for the 20 numerical ones, then XGBoost. Selection never touches the test set: a five-fold stratified baseline, a 30-combination randomized search, and a final re-rank of the top candidates scored with three repeats of five folds, with a proven winner from the tuning rounds locked into the pool."},
            {"type": "code", "title": "Candidate pipelines and the locked-in winner (models.py, excerpt)", "lang": "python", "code": r'''
def build_pipeline(**xgb_params):
    preprocessor = ColumnTransformer(
        transformers=[
            ('cb', CatBoostEncoder(cols=categorical, random_state=42), categorical),
            ('scaler', StandardScaler(), numerical),
        ],
        remainder='drop',
    )
    return Pipeline([
        ('preprocessor', preprocessor),
        ('xgb', XGBClassifier(random_state=42, eval_metric='logloss',
                              **xgb_params)),
    ])

# 'locked_search3' is the proven winner from tune.py - kept in the pool
# so the final selection can only match or improve on it.
LOCKED = dict(n_estimators=600, learning_rate=0.02, max_depth=3, subsample=0.7,
              colsample_bytree=0.9, min_child_weight=3, reg_lambda=3.0,
              reg_alpha=1.0)
'''},
            {"type": "code", "title": "Selection by repeated CV (models.py, excerpt)", "lang": "python", "code": r'''
repeats = RepeatedStratifiedKFold(n_splits=5, n_repeats=3, random_state=42)
results = search.cv_results_
top_idx = np.argsort(results['mean_test_score'])[::-1][:5]

candidates = [('baseline_300_lr05_d6', baseline),
              ('locked_search3', build_pipeline(**LOCKED))]
for rank, i in enumerate(top_idx, start=1):
    params = {k.replace('xgb__', ''): v for k, v in results['params'][i].items()}
    candidates.append((f'search_rank_{rank}', build_pipeline(**params)))

best_name, best_cv, model = None, -1, None
for name, pipe in candidates:
    scores = cross_val_score(pipe, X_train, y_train, cv=repeats,
                             scoring='roc_auc', n_jobs=-1)
    if scores.mean() > best_cv:
        best_name, best_cv = name, scores.mean()
'''},
            {"type": "p", "text": "The search settled on 500 estimators at depth 4 with a 0.01 learning rate, and the re-rank picked it over the baseline and the locked candidate. Class balance went into the search as a choice, scale_pos_weight 1.0 or the 0.58 lost-to-won ratio, and the cross-validation picked 1.0. The winner is refit on the full training split before the one test evaluation."},
        ]},
        {"id": "results", "heading": "Evaluation, with the real numbers", "blocks": [
            {"type": "p", "text": "These are the metrics exactly as metrics.json records them, from the single evaluation on the 1,343-row held-out test set."},
            {"type": "stat_grid", "items": [
                ("0.6085", "Test ROC-AUC"),
                ("0.6132", "Selected by 3x5 repeated CV"),
                ("62.8%", "Test accuracy at the 0.5 threshold"),
                ("63.8% / 94.8%", "Test precision / recall"),
                ("0.425", "OOF-tuned threshold (recall 100%)"),
                ("28", "Features: 20 numerical, 8 categorical"),
            ]},
            {"type": "table", "headers": ["Model", "Cross-validated ROC-AUC", "Test ROC-AUC"], "rows": [
                ["XGBoost (selected)", "0.6132 (3x5 repeated CV)", "0.6085"],
                ["Randomized search best (5-fold)", "0.6122", "-"],
                ["XGBoost baseline (slim features)", "0.5910 (5-fold)", "-"],
                ["Locked candidate (tune.py winner)", "-", "0.6027 (single evaluation)"],
            ]},
            {"type": "note", "text": "One reading note: accuracy 62.8% sits right at the naive always-win baseline of 63.1% on this test set, which is exactly why the docs lead with ROC-AUC and the ranked probabilities. The value of the model is the ordering it produces, not the flag at 0.5."},
            {"type": "p", "text": "The run also tuned the decision threshold on out-of-fold training predictions. It landed at 0.425, trading precision (63.1%) for total recall (100%) on the test set. The tuned number is stored in the artifact as metadata; the API ships 0.5 and reports both probabilities on every call, so the caller can apply the cutoff their use case needs."},
        ]},
        {"id": "api", "heading": "Serving the model", "blocks": [
            {"type": "p", "text": "main.py is a FastAPI service that loads the pickle once at startup and exposes five endpoints. The part worth reading is the contract: a Pydantic model defines the six required and four optional fields, so a malformed request fails validation with a useful message instead of a traceback."},
            {"type": "figure", "spec": ("SalesPipeline_5", "The API's OpenAPI page, generated by FastAPI: the five documented endpoints with their request schemas, including single and batch prediction.")},
            {"type": "code", "title": "Input contract and predict endpoint (main.py, excerpt)", "lang": "python", "code": r'''
class DealPredictionInput(BaseModel):
    # REQUIRED FIELDS (no default value)
    sales_agent: str = Field(..., description="Name of the sales agent")
    product: str = Field(..., description="Product name")
    account: str = Field(..., description="Customer account name")
    sector: str = Field(..., description="Industry sector")
    office_location: str = Field(..., description="Office location")
    engage_date: str = Field(..., description="Deal engagement date (YYYY-MM-DD format)")
    # OPTIONAL FIELDS (with defaults to fill any missing data)
    manager: Optional[str] = Field(default="unknown", description="Manager name")
    regional_office: Optional[str] = Field(default="central", description="Regional office")
    year_established: Optional[int] = Field(default=1995, description="Year company was established")
    employees: Optional[float] = Field(default=8.0, description="number of employees")


@app.post("/predict", response_model=PredictionOutput)
async def predict_single(deal: DealPredictionInput):
    if artifacts is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    result = make_prediction(deal)
    logger.info(f"Prediction result: {result['predicted_outcome']} "
                f"({result['confidence']:.2%} confidence)")
    return result
'''},
            {"type": "p", "text": "Inside make_prediction, the API rebuilds every engineered feature from the raw request using the statistics maps saved in the pickle, then applies the model. The response always carries both probabilities and a confidence score, which is what lets the caller distinguish a 0.71 from a 0.51."},
            {"type": "code", "title": "The prediction core (main.py, excerpt)", "lang": "python", "code": r'''
probabilities = artifacts['model'].predict_proba(X)[:, 1]
prob_won = float(probabilities[0])
prob_lost = 1 - prob_won

threshold = 0.5
if prob_won >= threshold:
    predicted_outcome = "WON"
else:
    predicted_outcome = "LOST"

# Calculate confidence (how sure is the model?)
confidence = max(prob_won, prob_lost)
'''},
            {"type": "table", "headers": ["Endpoint", "Method", "Purpose"], "rows": [
                ["/", "GET", "Welcome message and endpoint index"],
                ["/health", "GET", "Is the API alive and the model loaded"],
                ["/metrics", "GET", "Model type, stored ROC-AUC, feature counts"],
                ["/predict", "POST", "One deal in, outcome with probabilities out"],
                ["/predict-batch", "POST", "A list of deals, plus a summary of the results"],
            ]},
            {"type": "p", "text": "The Dockerfile keeps the image small (slim Python 3.13), installs dependencies from the pipenv lock file, and copies the pickle in with the code. The container exposes the same port uvicorn binds to."},
            {"type": "code", "title": "Dockerfile", "lang": "dockerfile", "code": r'''
#Use a slim Python image for a smaller container size
FROM python:3.13.9-slim

#Set working directory
WORKDIR /app

#Copy the pipfile install dependencies
COPY Pipfile Pipfile.lock ./

#FIX: Install pipenv globally in the container first, as it's not included in the slim image.
RUN pip install pipenv

#Now install project dependencies using pipenv
RUN pipenv install --system --deploy

#Copy model artifacts and application code
COPY sales_pipeline_model.pkl ./

#CRITICAL: Copy your application code
COPY main.py ./

#Expose the port that FastAPI will run on
EXPOSE 9696

#Command to run the application using Uvicorn
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9696"]
'''},
            {"type": "p", "text": "The folder ships api_logs.txt from real runs, and test.py re-scored the 1,589 open deals through the serve path and wrote the summary report (every deal predicted to win, probabilities from 0.6494 to 0.8686, mean 0.7413). As the business page explains, that run is a path test on stale 2016-17 dates, not a pipeline read. Predictions and logs, not slides, are the evidence this service works end to end."},
        ]},
        {"id": "dax", "heading": "The Power BI side", "blocks": [
            {"type": "p", "text": "The dashboard answers the descriptive half of the brief across three pages, about 150 visuals in total. Its roughly 45 measures live in 4 dedicated measure tables, grouped by job: deals, revenue, core KPIs and agent rankings. The signature pattern is a month-over-month trio per KPI: a percentage against last month with trend arrows, a green/red conditional-formatting measure, and a hex-colour variant for table rows. The ones worth showing are copied below; the model also holds quarterly top-agent measures that build a ranked table per quarter and return the agent at rank one."},
            {"type": "figure", "spec": ("SalesPipeline_11", "The semantic model behind the report: sales_pipeline as the fact table, four dimension tables feeding it one-to-many, a date table, and the dedicated measure tables that hold the DAX off the fact.")},
            {"type": "code_cards", "items": [
                {"name": "success_rate", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: the share of finished deals that were won.",
                          "Logic: DIVIDE protects against a zero denominator."],
                 "code": r'''
DIVIDE([deal_won],[deal_won] + [deal_lost])
''',
                 "note": "It sits next to conversion_rates = DIVIDE([deal_won],[opp_count]), where opp_count counts every non-prospecting deal including open ones. Keeping both definitions was deliberate: 'of everything engaged, what closed won' and 'of finished deals, what won' are different questions and a dashboard that conflates them misleads."},
                {"name": "opp_count", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: the pipeline size the funnel divides by.",
                          "Logic: CALCULATE with a filter that removes prospecting."],
                 "code": r'''
CALCULATE(COUNTROWS(sales_pipeline), sales_pipeline[deal_stage] <> "Prospecting")
''',
                 "note": "Same exclusion the training extract makes in SQL, so the report and the model describe the same population."},
                {"name": "vs Last Month %", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: the month-over-month arrow on every KPI card.",
                          "Logic: DATEADD shifts one month back, DIVIDE gets the change, and UNICHAR prints the up or down triangle with the formatted percentage."],
                 "code": r'''
VAR CM = [total_revenue_closed]
VAR PM_sales =
CALCULATE(
    [total_revenue_closed],
    DATEADD(DateTable[Date], -1,MONTH)
    )
VAR perc = DIVIDE(CM - PM_sales, PM_sales)
VAR _format =
SWITCH(
    TRUE(),
    perc > 0, UNICHAR(11165) & " " & FORMAT(perc, "0.0%"),
    perc < 0, UNICHAR(11167) & " " & FORMAT(perc*-1, "0.0%"),
    FORMAT(perc, "0.0%")
)
RETURN
_format
''',
                 "note": "The same pattern is replicated for deal_won, opp_count, success_rate and deal size, so every headline number carries its own movement. A month with nothing to compare against shows as a plain percentage."},
                {"name": "Rank_by_deal_won", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: rank agents by closed-won count across the whole model, regardless of the current visual's slice.",
                          "Logic: RANKX over ALL of the agent column, dense ranking."],
                 "code": r'''
RANKX(ALL(sales_pipeline[sales_agent]),
'deals measures'[deal_won], ,
DESC,Dense)
''',
                 "note": "A second measure, Previous_Rank, wraps this one in CALCULATE with PREVIOUSMONTH, and Rank_Chng compares the two to print the movement with last month's rank. Dense ranking keeps ties from skipping numbers."},
                {"name": "CF Last Month", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: a field-value conditional formatting measure.",
                          "Logic: same month-over-month calculation, returning a colour word instead of a number."],
                 "code": r'''
VAR CM = [total_revenue_closed]
VAR PM_sales =
CALCULATE(
    [total_revenue_closed],
    DATEADD(DateTable[Date], -1,MONTH)
    )
VAR perc = DIVIDE(CM - PM_sales, PM_sales)
VAR _format =
SWITCH(
    TRUE(),
    perc > 0, "Green",
    perc < 0, "Red",
    "Grey"
)
RETURN
_format
''',
                 "note": "A twin measure returns semi-transparent hex backgrounds for table cells. Encoding the colour rule once in DAX keeps the formatting consistent across visuals instead of hand-tuning each one."},
                {"name": "WelcomeMsg", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: a greeting card that names the manager whose view is active.",
                          "Logic: HOUR picks the greeting, SELECTEDVALUE reads the manager filter."],
                 "code": r'''
VAR CurrentHour = HOUR(NOW())
VAR Greetings =
    SWITCH(
        TRUE(),
        CurrentHour < 12, "Good Morning",
        CurrentHour < 17, "Good Afternoon",
        "Good Evening"
    )
VAR selectedManager = SELECTEDVALUE(sales_teams[manager], "Managers")
VAR Today = FORMAT(TODAY(), "dddd, mmmm dd, yyyy")
RETURN
Greetings &  " "  &  selectedManager & ", Welcome to your Dashboard. "
''',
                 "note": "Small touch, real function: the header always tells you whose numbers you are looking at. SELECTEDVALUE falls back to a generic greeting when nothing or several managers are selected."},
            ]},
            {"type": "sub", "text": "The report pages"},
            {"type": "figure", "spec": ("SalesPipeline_1", "Page one, the pipeline overview: four headline KPIs with their month-over-month arrows, the agents creating the most opportunities, the revenue trend at day, month and quarter grain, and the office-location map.")},
            {"type": "figure", "spec": ("SalesPipeline_2", "Page two, revenue contributions: top accounts, sectors and managers, each bar comparing last month's revenue against this month's, with the same geography drilldown on the right.")},
            {"type": "figure", "spec": ("SalesPipeline_3", "Page three, the agent performance summary: every agent ranked by success and conversion rate, with month-over-month deltas driven by the quarterly ranking measures.")},
            {"type": "figure", "spec": ("SalesPipeline_4", "The pipeline detail page: all 8,800 opportunities with stage, engagement date, deal duration and value, colour-flagged by outcome. The stage totals across the top are the same counts the SQL audit reconciles.")},
        ]},
        {"id": "validation", "heading": "How I verified the numbers", "blocks": [
            {"type": "p", "text": "Every number both pages quote comes from a saved output of my own. I profiled the key figures from the project files as I built these pages, and these are the checks:"},
            {"type": "table", "headers": ["Check", "Expected", "Result"], "rows": [
                ["Stage counts", "Won + Lost + Engaging + Prospecting = 8,800", "Reconciles: 4,238 + 2,473 + 1,589 + 500"],
                ["Structural nulls", "Missing close values = missing close dates = open deals", "Reconciles: 2,089 = 2,089 = 1,589 + 500"],
                ["Duplicates", "Deduplication is a safety net", "Reconciles: 0 duplicate opportunity ids"],
                ["Win rate", "Won / closed from the CSV", "Reconciles: 4,238 / 6,711 = 63.2%"],
                ["Test split size", "Classification report support = 20% of 6,711", "Reconciles: 1,343 rows"],
                ["Test class balance", "Report support matches the raw 63/37 split", "Reconciles: 848 won (63.1%), stratified split"],
                ["Open-deal scoring", "Summary report count = engaging rows", "Reconciles: 1,589 scored through the serve path"],
                ["Quoted numbers", "README, docs and the API /metrics quote the same figures", "Reconciles: all read metrics.json, written by the training run"],
            ]},
            {"type": "p", "text": "One deliberate non-check: the scoring run over the open deals is documented as illustrative rather than reconciled to any win share, because the stale 2016-17 dates put deal age far outside the training range. It proves the serve path, not the pipeline."},
        ]},
        {"id": "decisions", "heading": "Decisions and trade-offs", "blocks": [
            {"type": "table", "headers": ["Decision", "Why", "Trade-off I accepted"], "rows": [
                ["Excluded Prospecting from the training extract", "Those deals are too early to have a knowable outcome", "The model says nothing about brand-new leads yet"],
                ["Dropped close_date and close_value at training time", "Neither exists until a deal finishes, so keeping them is leakage", "The model cannot use deal size, one of the strongest signals in the data"],
                ["Cut the 21 hand-rolled group-statistic features", "Repeated CV showed they duplicate the CatBoost encoding and hurt out-of-sample AUC (0.57 with vs 0.61 without)", "Less hand-built signal; the encoding carries the category effects"],
                ["Selected by repeated CV with a locked candidate in the pool", "A single five-fold winner can be flattered by fold noise", "More compute on every training run"],
                ["Kept the API threshold at 0.5", "A fixed, explainable cutoff, with both probabilities on every response", "The OOF-tuned 0.425 trades precision for total recall; callers can apply their own cutoff"],
                ["Shipped one pickled pipeline plus metrics.json", "The API and every document quote the same file", "The pickle must be generated locally before the image build"],
                ["Scored the open deals as stored", "Proves the serve path works end to end", "Stale 2016-17 dates inflate deal age at serve time; the run is illustrative, not a pipeline read"],
            ]},
        ]},
        {"id": "upkeep", "heading": "Deployment and next steps", "blocks": [
            {"type": "steps", "items": [
                ("One training entry point", "models.py is the only way the artifact is produced; keep it that way as the code evolves."),
                ("Outcomes back into the loop", "When the scored deals close, join outcomes and recompute precision and recall on real production data."),
                ("Score on fresh data", "Bound-check engage dates at the API edge and schedule scoring runs on current deals, so predicted shares describe a live pipeline."),
                ("Retrain on a schedule", "The pipeline's win rates drift; the same re-rank protocol and metrics file keep the scores honest."),
                ("Keep the audit query", "The SQL audit summary by stage is the first thing to run after any refresh."),
                ("Guard the thresholds", "Any change to the cutoff ships with the precision and recall measured at that cutoff."),
                ("Lock down before exposure", "Authentication, restricted CORS and HTTPS are documented in the repo's deployment notes and remain undone, deliberately, for the demo."),
            ]},
        ]},
        {"id": "reflection", "heading": "What this project shows", "blocks": [
            {"type": "p", "items": [
                "This is an end-to-end machine learning workflow, not a notebook: SQL cleaning with an audit query, a leakage decision that removes the deal's final value from its own prediction, an experiment harness that decided the feature set on cross-validated evidence, a locked-in re-rank pool, a single test evaluation, a versioned artifact with a metrics file, a validated API contract, a container, and a scoring run over the full open pipeline.",
                "The habits around it matter as much as the code: features were cut because experiments said so, not because they looked cluttered; every quoted number traces to one metrics file; and the trade-offs sit next to the decisions. That is the part I would carry into the next project unchanged.",
            ]},
        ]},
    ],
}
