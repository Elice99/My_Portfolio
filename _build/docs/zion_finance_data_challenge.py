"""
Zion Tech Hub Finance Data Challenge documentation content.

Source: the completed analysis project in
C:\\Users\\Hp\\Desktop\\GitHub\\Portfolio\\Zion Tech Hub Finance Data Challenge - Nov 2025
(README, docs/01-05, outputs/summary.json, outputs/validation.csv and the
15-sheet analysis workbook). Every number here reconciles to the brief.

Rules: first person, plain words, short sentences, no invented claims. The
technical-vs-behavioural split and the recovery targets are labelled as
inference and assumptions. Uses the generic `sections` format in build_docs.py.

Image names (in /images/):
  ZionFinance_1  monthly leak chart
  ZionFinance_2  channel paradox chart
  ZionFinance_3  concentration chart
  ZionFinance_4  ticket-band chart
  ZionFinance_5  January 2024 drivers chart
  ZionFinance_6  recovery scenarios chart
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
    s = ['<svg viewBox="0 0 960 500" role="img" class="dg" '
         'aria-label="Architecture: raw extracts flow through preparation, analysis, validation, charts, an Excel workbook and a PDF export">'
         '<defs><marker id="dgZ" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
         'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="dg-head"/></marker></defs>']

    # Row 1: raw data to analysis
    s.append(_box(10, 30, 190, 92, "Raw extracts", ["transactions.csv", "customer_details.csv", "exchange_rates.csv"]))
    s.append(_box(250, 30, 170, 92, "prepare_data.py", ["parse period", "join customers", "map sector"]))
    s.append(_box(470, 30, 170, 92, "prepared/", ["tx_prepared.csv", "customers_prepared.csv", "fx_monthly.csv"], "dg-model"))
    s.append(_box(690, 30, 200, 92, "analyse.py", ["28 monthly rows", "8 cut tables", "summary.json"], "dg-measure"))

    # Row 2: outputs to validation, charts and workbook
    s.append(_box(690, 190, 200, 92, "outputs/", ["tables and CSVs", "validation.csv", "summary.json"], "dg-model"))
    s.append(_box(470, 190, 170, 92, "qa_check.py", ["64 checks", "12 brief reconciliations"], "dg-measure"))
    s.append(_box(250, 190, 170, 92, "make_charts.py", ["6 report charts", "PNG figures"], "dg-measure"))
    s.append(_box(10, 190, 190, 92, "build_workbook.py", ["15 sheets", "8 native charts"], "dg-measure"))

    # Row 3: delivery artifacts and the brief
    s.append(_box(10, 350, 190, 92, "Workbook", ["static values", "no live formulas"], "dg-model"))
    s.append(_box(250, 350, 170, 92, "Portfolio docs", ["business insights", "technical doc"], "dg-model"))
    s.append(_box(470, 350, 170, 92, "PDF export", ["22 pages", "print scaling"]))
    s.append(_box(690, 350, 200, 92, "Challenge brief", ["definitions", "headline targets"]))

    line = lambda d, extra="": s.append(f'<path class="dg-line {extra}" d="{d}" marker-end="url(#dgZ)"/>')
    lbl = lambda x, y, t, a="middle": s.append(f'<text class="dg-l" x="{x}" y="{y}" text-anchor="{a}">{t}</text>')

    # Main left-to-right flow
    line("M200,76 L250,76")
    line("M420,76 L470,76")
    line("M640,76 L690,76")
    line("M790,122 L790,190")

    # Outputs fan out to validation, charts and workbook build
    line("M690,236 L640,236")
    line("M690,248 L690,316 L335,316 L335,282", "dg-dash")
    line("M700,258 L700,330 L105,330 L105,282", "dg-dash")

    # Remaining row flow and the brief feeding validation
    line("M470,236 L420,236")
    line("M250,236 L200,236")
    line("M105,282 L105,350")
    line("M200,396 L250,396")
    line("M420,396 L470,396")
    line("M690,396 L580,396 L580,282", "dg-dash")

    lbl(720, 182, "tables")
    lbl(520, 230, "checks")
    lbl(330, 306, "charts")
    lbl(120, 322, "workbook")
    lbl(610, 386, "brief targets", "start")

    # Legend
    s.append('<rect class="dg-box dg-model" x="10" y="470" width="14" height="14" rx="3"/>')
    lbl(32, 481, "Prepared data and outputs", "start")
    s.append('<rect class="dg-box dg-measure" x="250" y="470" width="14" height="14" rx="3"/>')
    lbl(272, 481, "Python pipeline step", "start")
    s.append('<rect class="dg-box" x="470" y="470" width="14" height="14" rx="3"/>')
    lbl(492, 481, "Delivered artifact", "start")
    s.append("</svg>")
    return "".join(s)


ARCH_SVG = _arch_svg()


# ---------------------------------------------------------------- business
BUSINESS = {
    "title": "The cost of failed transactions: what the data says",
    "lede": "Across 28 months of East African payment data, 9 of every 10 dollars of fee revenue sat in failed transactions. This page covers where that money sat, what happened in January 2024, and what I think can realistically be recovered.",
    "sections": [
        {"id": "question", "heading": "The question", "blocks": [
            {"type": "note", "text": "This is a supplied challenge extract, not an audited production ledger. Failed fee revenue is a counterfactual: what the fee would have been if the transaction had succeeded. It is not a confirmed accounting loss."},
            {"type": "p", "items": [
                "The brief gave me three questions. Where do payment failures concentrate? What happened in January 2024, when the revenue failure rate reached 97 percent? What could a fix realistically recover?",
                "I used 62,684 monthly aggregate rows from January 2022 to April 2024, covering Kenya, Uganda, Tanzania, Ghana and Zambia. The rows are customer by month by currency by payment type by status.",
            ]},
        ]},
        {"id": "answer", "heading": "The short answer", "blocks": [
            {"type": "verdict", "text": "The leak is concentrated, not diffuse. Ten accounts hold 49.3 percent of it. Card carries 79.7 percent of the failed fee revenue. January 2024 was a volume and mix shock from a few accounts, not a broad change in customer behaviour. A credible fix recovers about $0.32M to $0.40M over the 28 months, not the full $2.84M."},
        ]},
        {"id": "numbers", "heading": "Numbers at a glance", "blocks": [
            {"type": "stat_grid", "items": [
                ("1,645,892", "Payment attempts"),
                ("1,019,793", "Failed attempts (62.0 percent)"),
                ("$3,148,892", "Total fee revenue"),
                ("$2,842,676", "Failed fee revenue (90.3 percent)"),
                ("49.3%", "Leak held by the top 10 accounts"),
                ("$319,853", "Stacked recovery scenario"),
            ]},
        ]},
        {"id": "findings", "heading": "What I found", "blocks": [
            {"type": "findings", "items": [
                {
                    "id": "two-rates",
                    "title": "Two failure rates tell two different stories",
                    "question": "Is the failure rate 62 percent or 90 percent?",
                    "paragraphs": [
                        "Both figures are correct, but they answer different questions. Count failure rate divides failed attempts by all attempts. Revenue failure rate divides failed fee revenue by all fee revenue.",
                        "62.0 percent of attempts failed. 90.3 percent of fee dollars failed. A failed attempt carries about 5.7 times the fee of a successful one, so the money skews heavily towards failures.",
                    ],
                    "table": {"headers": ["Lens", "Value", "What it answers"], "rows": [
                        ["Count failure rate", "62.0 percent", "How often a payment fails"],
                        ["Revenue failure rate", "90.3 percent", "Where the fee money sits"],
                        ["Average failed fee", "5.7 times a success", "Why the two rates diverge"],
                        ["Lowest revenue month", "78.7 percent, Oct 2023", "The brief's never below 78 percent claim holds"],
                        ["Lowest count month", "50.4 percent, Jul 2022", "The same claim fails on the count lens"],
                    ]},
                    "meaning": "The brief mixes both lenses. Reporting only one of them makes the problem look either too soft or too absolute.",
                    "conclusion": "Keep both rates on every dashboard, with the question each one answers written next to it.",
                },
                {
                    "id": "concentration",
                    "title": "A small set of accounts holds the leak",
                    "question": "Is this a broad customer problem or a few broken flows?",
                    "paragraphs": [
                        "The top 10 accounts by failed fee revenue hold $1,400,986, which is 49.3 percent of the leak. The top 3 hold 30.3 percent. The top 100 hold 78.4 percent.",
                        "957 accounts fail at least 99 percent of their fee value and carry 54.7 percent of the leak. Account 49957 alone runs 54,539 attempts with 100 percent card and USD exposure and a 100 percent revenue failure rate. That pattern looks like a broken integration or a routing rule, not customer behaviour.",
                    ],
                    "figure": ("ZionFinance_3", "Failed fee revenue by account. The first ten bars are almost half the leak."),
                    "meaning": "Account-level triage reaches more money than a broad awareness campaign.",
                    "conclusion": "Start with the top three accounts, then work down the ranked account list.",
                },
                {
                    "id": "card",
                    "title": "Card is the single biggest lever",
                    "question": "Which payment type carries the problem?",
                    "paragraphs": [
                        "Card is 23 percent of attempts but 77 percent of fee revenue. 93.8 percent of card fee value fails, and card holds 79.7 percent of the total leak, or $2,266,220.",
                        "Bank transfer tells a useful contrast. Only 3.3 percent of its fee value fails. Failure is technically avoidable in this dataset, but bank transfer carries almost no volume, so it cannot simply replace card.",
                    ],
                    "figure": ("ZionFinance_2", "Fee revenue and failed fee revenue by payment type. Card dominates both bars."),
                    "meaning": "Any serious fix has to address card acceptance, scheme routing or account configuration.",
                    "conclusion": "Treat card as the priority channel, with bank transfer as a benchmark rather than a scale solution.",
                },
                {
                    "id": "ticket",
                    "title": "Larger tickets fail more often",
                    "question": "Do small or large payments carry the leak?",
                    "paragraphs": [
                        "Sub-1 dollar payments fail 47 percent by fee value. The 100 to 500 dollar band fails 95.4 percent and carries $1.22M of the leak. Every band above 50 dollars fails above 85 percent by fee value.",
                    ],
                    "figure": ("ZionFinance_4", "Revenue failure rate rises sharply with average ticket size."),
                    "meaning": "The failure is not spread evenly across ticket sizes. High-value flows are the expensive ones.",
                    "conclusion": "Prioritise high-ticket account and channel combinations in any remediation wave.",
                },
                {
                    "id": "january",
                    "title": "January 2024 was a mix shock, not a rate shock",
                    "question": "Why did the rate jump to 97.3 percent?",
                    "paragraphs": [
                        "January 2024 recorded $683k more failed fee revenue than the 2023 monthly average. Ten accounts explain 99.9 percent of that increase. Three of them pushed card from 25 percent to 57 percent of attempts and USD from 15 percent to 53 percent.",
                        "The same mechanism appears again in April 2024 through account 47087 on mobilemoney. So the January spike is a visible peak in a recurring onboarding and routing problem, not a one-off event.",
                    ],
                    "figure": ("ZionFinance_5", "January 2024 decomposition against the 2023 monthly average."),
                    "meaning": "A monthly rate alone would have flagged the spike but not shown which accounts caused it.",
                    "conclusion": "Add account-level failed revenue monitoring so the next spike is visible before it becomes a headline.",
                },
                {
                    "id": "recovery",
                    "title": "The recoverable prize is much smaller than the headline",
                    "question": "Can the whole $2.84M be recovered?",
                    "paragraphs": [
                        "No. I built recovery scenarios as current failure rate minus an assumed target rate, multiplied by the revenue in scope. The stacked case fixes the top three accounts to the portfolio's own mobilemoney floor of 77.3 percent, then lifts the rest of card to 85 percent. That gives $319,853, or 11.3 percent of the leak.",
                        "The stretch case lifts all card to the same 77.3 percent floor and gives $399,575, or 14.1 percent. A best-in-class case that assumes card can match bank transfer would imply $2.28M, but that assumption is not credible at this volume.",
                    ],
                    "figure": ("ZionFinance_6", "Recovery scenarios. The credible range is the first two bars."),
                    "meaning": "The honest answer is a range, with targets clearly labelled as assumptions.",
                    "conclusion": "Commit to the stacked case, and treat the stretch case as upside rather than a forecast.",
                },
            ]},
        ]},
        {"id": "recommendations", "heading": "What I would do first", "blocks": [
            {"type": "recs", "items": [
                {"priority": "High", "title": "Fix the top three accounts",
                 "evidence": "The top three hold 30.3 percent of the leak. Account 49957 alone runs 54,539 attempts at 100 percent card and USD failure.",
                 "action": "Audit integration, scheme support and routing rules for those accounts. Lift them to the observed mobilemoney floor of 77.3 percent first.",
                 "impact": "About $196k of recovery in the stacked scenario."},
                {"priority": "High", "title": "Lift the rest of card to 85 percent",
                 "evidence": "Card fails 93.8 percent by fee value and holds 79.7 percent of the leak. Bank transfer fails only 3.3 percent.",
                 "action": "Review card acceptance and routing for the remaining card accounts. Use 85 percent as a staged target, not a guaranteed outcome.",
                 "impact": "About $124k on top of Wave 1."},
                {"priority": "High", "title": "Alert on account-level failed revenue",
                 "evidence": "The January 2024 spike was already visible in December 2023, but the monthly blended rate hid the cause.",
                 "action": "Track failed fee revenue by account weekly and alert when one account contributes a large month-on-month jump.",
                 "impact": "Catches the next concentration before it becomes a 97 percent month."},
                {"priority": "Medium", "title": "Report both failure lenses",
                 "evidence": "62.0 percent of attempts fail, but 90.3 percent of fee dollars fail. The brief mixes them.",
                 "action": "Put count and revenue failure rates side by side, with the formula and question each answers.",
                 "impact": "Stops stakeholders arguing about two correct numbers."},
                {"priority": "Medium", "title": "Triage the near-100 percent accounts as broken flows",
                 "evidence": "957 accounts fail at least 99 percent of fee value and hold 54.7 percent of the leak.",
                 "action": "Treat these as integration or configuration cases first, and churn cases second.",
                 "impact": "Focuses support effort where failure is persistent rather than occasional."},
            ]},
        ]},
        {"id": "limits", "heading": "What this cannot tell you", "blocks": [
            {"type": "p", "items": [
                "The extract has no failure reason, provider, retry flag or transaction timestamp. I cannot observe technical failure directly. The technical versus behavioural split in the workbook is an account-level persistence proxy and is labelled as inference.",
                "Rows are monthly aggregates. Day-of-month questions in the brief cannot be answered at this grain.",
                "The source does not say whether a failed fee was ever booked, reversed or refunded. Failed fee revenue is a counterfactual.",
                "42 percent of sector values are blank. Sector cuts are directional only.",
                "The recovery targets are assumptions. They are not forecasts and should be confirmed with payment Operations before they become commitments.",
                "This is a supplied challenge extract, not an audited production ledger.",
            ]},
        ]},
    ],
}


# --------------------------------------------------------------- technical
TECHNICAL = {
    "title": "The cost of failed transactions: how it was built",
    "lede": "A reproducible Python pipeline, a 15-sheet Excel workbook, eight native charts, six report figures and a 64-check QA suite. This page covers the data grain, cleaning rules, metric definitions, validation and the architecture.",
    "sections": [
        {"id": "solution", "heading": "The solution", "blocks": [
            {"type": "note", "text": "The original ZT_Finance_Challenge.xlsx was a pre-formatted skeleton with uncalculated formulas that displayed zeros. I left it untouched. The new workbook stores static computed values, so every number is correct on open in any spreadsheet engine."},
            {"type": "p", "text": "I built a deterministic pipeline in five Python scripts plus one optional PowerShell export. Raw CSVs feed a preparation step, the prepared tables feed analysis, analysis writes tables and a summary, and the workbook and charts are generated from those outputs. A QA script recomputes the headline numbers and inspects the workbook."},
            {"type": "svg", "svg": ARCH_SVG, "caption": "How the pieces connect. The challenge brief feeds validation only. Dashed arrows are secondary reads of the same output tables."},
            {"type": "table", "headers": ["Component", "Where it lives", "Role"], "rows": [
                ["prepare_data.py", "scripts/prepare_data.py", "Raw CSVs to prepared tables and a preparation manifest"],
                ["analyse.py", "scripts/analyse.py", "All cut tables, summary.json and validation.csv"],
                ["make_charts.py", "scripts/make_charts.py", "Six report PNG figures"],
                ["build_workbook.py", "scripts/build_workbook.py", "15-sheet workbook with eight native charts"],
                ["qa_check.py", "scripts/qa_check.py", "64 checks across data, workbook and report"],
                ["export_workbook_pdf.ps1", "scripts/export_workbook_pdf.ps1", "Optional print-ready PDF via Excel COM"],
            ]},
        ]},
        {"id": "data", "heading": "The source data and its grain", "blocks": [
            {"type": "table", "headers": ["File", "Rows", "Grain or role"], "rows": [
                ["transactions.csv", "62,684", "Customer by month by currency by status by payment type"],
                ["customer_details.csv", "64,343", "One row per customer account"],
                ["exchange_rates.csv", "46,490", "Currency by calendar day"],
                ["Challenge brief PDF", "Not a data table", "Headline targets and question framing"],
                ["ZT_Finance_Challenge.xlsx", "Skeleton", "Pre-existing artefact, left unmodified"],
            ]},
            {"type": "p", "text": "The transaction rows are aggregates. One row can represent many payment attempts, so total attempts are the sum of total_count, not a row count. This distinction is the foundation of every rate in the analysis."},
            {"type": "pairs", "items": [
                ("Currency", "All monetary values are converted to USD. Fee amounts are already USD in the extract."),
                ("Period", "The month label is parsed to the first day of the month. No daily or intra-month claim is possible."),
                ("Sector", "A controlled mapping cleans free-text sectors. Blank sectors remain 'Unknown' rather than being dropped."),
            ]},
        ]},
        {"id": "prep", "heading": "Preparation rules", "blocks": [
            {"type": "steps", "items": [
                ("Parse the month", "Convert the period label to a date at month start so monthly ordering is stable."),
                ("Join customers", "Attach country, sector, customer status and sign-up date by customer_id."),
                ("Clean sector", "Map free-text sector values into a controlled set and keep blanks as Unknown."),
                ("Derive failure flags", "is_failed is 1 when status is failed. FailedCount and FailedRev_USD are derived from it."),
                ("Convert currency", "Join a month-average daily FX rate by currency and month. Rows without a rate keep a missing USD value and are excluded from monetary sums."),
                ("Freeze the grain", "Write prepared tables once and build every analysis from them. Source files are never overwritten."),
            ]},
            {"type": "note", "text": "222 transaction rows have no matching month-average FX rate. I did not impute them. Count-based metrics use all rows; money-based metrics use only rows with a valid USD value. The exclusion is disclosed in the workbook and the data quality report."},
        ]},
        {"id": "metrics", "heading": "Metric definitions", "blocks": [
            {"type": "p", "text": "I kept the operational and financial lenses separate instead of forcing one headline rate."},
            {"type": "code_cards", "items": [
                {"name": "Headline KPIs", "kind": "scripts/analyse.py", "lang": "python",
                 "text": ["This function is the core of the analysis. Attempts and fee revenue are summed from the prepared grain. The two failure rates are deliberately separate."],
                 "code": '''def kpis(d: pd.DataFrame) -> dict:\n    att = float(d["total_count"].sum())\n    fatt = float(d["FailedCount"].sum())\n    rev = float(d["Rev_USD"].sum())\n    frev = float(d["FailedRev_USD"].sum())\n    succ_att = att - fatt\n    return {\n        "attempts": att,\n        "failed_attempts": fatt,\n        "count_fail_rate": fatt / att if att else np.nan,\n        "revenue_usd": rev,\n        "failed_revenue_usd": frev,\n        "revenue_fail_rate": frev / rev if rev else np.nan,\n        "avg_fee_failed_att": frev / fatt if fatt else np.nan,\n        "avg_fee_success_att": (rev - frev) / succ_att if succ_att else np.nan,\n    }''',
                 "note": "Count failure rate answers how often payments fail. Revenue failure rate answers where the fee money sits. Both are reported everywhere."},
                {"name": "Recovery", "kind": "scenario formula", "lang": "python",
                 "text": ["Recovery is a counterfactual. It assumes a segment can move from its current revenue failure rate to an explicit target."],
                 "code": '''current = df["FailedRev_USD"].sum() / df["Rev_USD"].sum()\nrecovery = max(0.0, current - target) * df["Rev_USD"].sum()''',
                 "note": "Targets are assumptions, not forecasts. The mobilemoney floor of 77.3 percent is the best observed floor in the extract. The 85 percent card target is a staged improvement assumption."},
            ]},
            {"type": "table", "headers": ["Term", "Definition", "Why it matters"], "rows": [
                ["Payment attempts", "Sum of total_count", "Rows are aggregates, so a row count would understate volume"],
                ["Count failure rate", "FailedCount divided by total_count", "Operational view of failure frequency"],
                ["Revenue failure rate", "FailedRev_USD divided by Rev_USD", "Financial view of where fee dollars sit"],
                ["Leak", "Total FailedRev_USD across the window", "A counterfactual pool of fee revenue, not a booked loss"],
                ["Concentration", "Accounts ranked by FailedRev_USD with cumulative share", "Shows whether action should be broad or account-level"],
                ["Severity proxy", "Accounts banded by their own revenue failure rate", "A labelled inference, because no failure reason field exists"],
            ]},
        ]},
        {"id": "fx", "heading": "FX method and missing rates", "blocks": [
            {"type": "p", "text": "Each transaction row is a monthly aggregate. I use the average of the available daily rates for that currency in that month. This matches the grain of the transaction data and avoids pretending that a single day's rate applies to a whole month."},
            {"type": "table", "headers": ["Choice", "Rule", "Effect"], "rows": [
                ["DEF-1", "Month-average daily rate by currency", "One consistent USD value for each monthly row"],
                ["Missing rates", "No imputation", "222 rows excluded from monetary sums only"],
                ["Fee revenue", "Already USD in the extract", "No conversion applied to fee columns"],
                ["Audit trail", "fx_monthly.csv and prepare_manifest.json", "The rate table and run metadata are reproducible"],
            ]},
        ]},
        {"id": "validation", "heading": "Validation", "blocks": [
            {"type": "p", "text": "I recomputed every headline from the prepared data rather than copying the brief. Twelve checks pass. The workbook's Validation sheet shows all of them with the computed value, brief value, status and note."},
            {"type": "table", "headers": ["Check", "Computed", "Brief"], "rows": [
                ["Transaction rows", "62,684", "62,684"],
                ["Payment attempts", "1,645,892", "1.65M"],
                ["Failed attempts", "1,019,793", "1.02M"],
                ["Count failure rate", "62.0 percent", "62 percent"],
                ["Total fee revenue", "$3,148,892", "$3.15M"],
                ["Failed fee revenue", "$2,842,676", "$2.85M"],
                ["Revenue failure rate", "90.3 percent", "90 percent"],
                ["Minimum monthly revenue failure", "78.7 percent, Oct 2023", "never below 78 percent"],
                ["January 2024 revenue failure", "97.3 percent", "spiked to 97 percent"],
                ["Card revenue failure", "93.8 percent", "94 percent"],
                ["Kenya revenue failure", "93.4 percent", "93 percent"],
                ["Bank transfer revenue failure", "3.3 percent", "3 percent"],
            ]},
            {"type": "note", "text": "One deliberate divergence is documented. The brief says bank transfer is 2 percent of volume, but the data shows 0.7 percent of attempts and 0.2 percent of fee revenue. The workbook keeps the computed value and explains the gap."},
            {"type": "p", "text": "qa_check.py runs 64 checks in total: required files, recomputed headline numbers, the 12 reconciliations, workbook structure, chart series and report quotes. All 64 pass after the final build."},
        ]},
        {"id": "workbook", "heading": "The workbook and charts", "blocks": [
            {"type": "p", "text": "The workbook has 15 sheets. It moves from reading guide and executive summary through the analytical cuts, January 2024, recovery, severity, data quality, dictionary, method log and validation. Eight native Excel charts sit beside the tables."},
            {"type": "table", "headers": ["Sheet group", "Sheets", "Purpose"], "rows": [
                ["Orientation", "Read Me, Executive Summary", "Headline answer and how to navigate"],
                ["Failure cuts", "Monthly, Channel, Country, Sector", "Where the leak sits over time and by dimension"],
                ["Concentration", "Concentration, Ticket Size", "Account ranking and ticket-band behaviour"],
                ["Diagnosis", "Jan 2024, Recovery, Severity Split", "Shock decomposition, scenarios and labelled proxy"],
                ["Trust", "Data Quality, Data Dictionary, Method Log, Validation", "Limitations, definitions, decisions and proof"],
            ]},
            {"type": "table", "headers": ["Figure", "Why I chose it"], "rows": [
                ["Monthly leak", "Bars show failed dollars; lines show both failure rates over 28 months"],
                ["Channel paradox", "High-value card and near-zero bank transfer failure side by side"],
                ["Concentration", "Ranked account bars make the 49.3 percent top-10 story visible"],
                ["Ticket bands", "Line makes the sharp rise above 50 dollars obvious"],
                ["January drivers", "Composition shift is easier to read as changes against a 2023 baseline"],
                ["Recovery", "Scenario bars keep assumptions and credible ranges in view"],
            ]},
        ]},
        {"id": "reproduce", "heading": "Reproduce it", "blocks": [
            {"type": "code", "title": "Full pipeline", "lang": "bash", "code": '''python scripts/prepare_data.py\npython scripts/analyse.py\npython scripts/make_charts.py\npython scripts/build_workbook.py\npython scripts/qa_check.py\n\n# Optional, Windows and Microsoft Excel only:\npowershell -ExecutionPolicy Bypass -File scripts/export_workbook_pdf.ps1''', "caption": "No randomness, no external calls and no manual workbook edits. Re-running reproduces the same values."},
            {"type": "pairs", "items": [
                ("Determinism", "No random seed is used because no step is random. Only timestamps in prepare_manifest.json change."),
                ("Dependencies", "Python 3.10+, pandas, numpy, openpyxl and matplotlib. The PDF export also needs Microsoft Excel."),
                ("Source safety", "Raw CSVs and the original skeleton workbook are read-only inputs."),
            ]},
        ]},
        {"id": "reflection", "heading": "What I would change with better data", "blocks": [
            {"type": "pairs", "items": [
                ("Failure reason", "A reason code, provider identifier and retry flag would replace the persistence proxy with observed causes."),
                ("Daily grain", "Daily rows would allow the brief's time-of-month question to be answered properly."),
                ("Fee lifecycle", "Booked, reversed and refunded fee flags would tell us whether failed fee revenue is recoverable money or only a pricing counterfactual."),
                ("Automated gates", "The QA script already runs 64 checks. In production I would wire it into CI so a failed reconciliation blocks publication."),
            ]},
            {"type": "note", "text": "The main judgement call was to report both failure lenses and to keep the recovery targets visibly assumed. It would have been easy to publish 90 percent as the failure rate and $2.84M as the prize. That would have been a cleaner story and a worse answer."},
        ]},
    ],
}
