"""
Sunrise Coffee performance review documentation content.

Source: the supplied DataDNA challenge extract and the analysis I rebuilt from
the five raw CSVs in the project folder. Every number here comes from
scripts/analyse.py and outputs/summary.json. The original workbook is left
untouched and is documented as a source artefact with known label problems.

Image names (in /images/):
  SunriseReview_1  regional net profit margin
  SunriseReview_2  loss-making store-months by region
  SunriseReview_3  loyalty adoption vs member revenue share
  SunriseReview_4  revenue mix 2023 vs 2024
  SunriseReview_5  bank holiday revenue by format
  SunriseReview_6  biggest store profit movements
"""

BUSINESS = {
    "title": "Sunrise Coffee: the margin story behind 60 shops",
    "lede": "Two years of trading data across 60 UK stores. The estate looks healthy at an 18.8 percent net margin, but that average hides a London problem, a loyalty programme that changes who pays rather than how much they spend, and a revenue mix that barely moved.",
    "sections": [
        {"id": "question", "heading": "The question", "blocks": [
            {"type": "note", "text": "This is a supplied challenge extract, not audited company accounts. It covers 2023 and 2024 trading and uses GBP throughout. I rebuilt every figure from the raw CSVs because several dashboard KPIs in the supplied workbook did not agree with each other."},
            {"type": "p", "items": [
                "The commercial team wanted to know which stores and formats actually drive profit, whether loyalty members spend more, how the revenue mix is shifting, and what seasonality does to trading.",
                "I used five tables: 60 stores, 40 products, 730 calendar days, 10,000 recorded store-days of sales, and 1,440 store-month P&L rows.",
            ]},
        ]},
        {"id": "answer", "heading": "The short answer", "blocks": [
            {"type": "verdict", "text": "The estate made £16.88M net profit on £89.69M revenue over two years, an 18.8 percent margin. That average hides London at 8.5 percent margin with a quarter of its store-months loss-making. Loyalty members provide a third of revenue, but adoption has no useful relationship with transaction value. Food share did not grow. Bank holidays are quieter, not busier."},
        ]},
        {"id": "numbers", "heading": "Numbers at a glance", "blocks": [
            {"type": "stat_grid", "items": [
                ("£89.69M", "Revenue over 2023 and 2024"),
                ("£16.88M", "Net profit"),
                ("18.8%", "Net profit margin"),
                ("33.2%", "Revenue from loyalty members"),
                ("8", "Loss-making stores in Dec 2024"),
                ("12", "UK regions in the estate"),
            ]},
        ]},
        {"id": "findings", "heading": "What I found", "blocks": [
            {"type": "findings", "items": [
                {
                    "id": "london",
                    "title": "The headline margin hides a London problem",
                    "question": "Where does the profit actually come from?",
                    "paragraphs": [
                        "Northern-Ireland leads on 28.4 percent net margin, then West-Midlands on 24.5 percent and Wales on 22.8 percent. London sits last on 8.5 percent despite carrying £10.46M of the two-year revenue.",
                        "25.6 percent of London store-months are classed Loss-Making or Structural-Loss, the highest share of any region. Profit per store over the two years is about £126k in London against £421k in Northern-Ireland.",
                    ],
                    "figure": ("SunriseReview_1", "Net profit margin by region. London is the clear outlier at the bottom."),
                    "meaning": "Estate averages make London look like just another region. The store-level cut shows where margin is being lost.",
                    "conclusion": "Prioritise a London store review before adding more London sites to the 2025 plan.",
                },
                {
                    "id": "losses",
                    "title": "Eight stores were losing money at the end of 2024",
                    "question": "How wide is the immediate problem?",
                    "paragraphs": [
                        "In December 2024, 8 of 60 stores were Loss-Making or Structural-Loss. East-Midlands had 3 of them. One store, Dundee Station, was Structural-Loss at minus £16,932 for that month.",
                        "South London Corner is the sharpest deterioration I found. It went from £28,649 profit in 2023 to a £79,144 loss in 2024, a fall of £107,793.",
                    ],
                    "figure": ("SunriseReview_2", "Loss-making store-months by region. London's rate is the highest in the estate."),
                    "meaning": "A small set of stores carries the downside. This is a triage list, not a reason to close sites without looking at the leases.",
                    "conclusion": "Run store-level P&L reviews on the eight loss-makers first, with South London Corner at the top.",
                },
                {
                    "id": "loyalty",
                    "title": "Loyalty changes who pays, not how much they spend",
                    "question": "Is the loyalty programme worth more investment?",
                    "paragraphs": [
                        "Stores with higher adoption also report a higher share of revenue from loyalty members. The correlation is 0.998, which is so tight that I treat it as close to mechanical in this data rather than proof of behaviour change.",
                        "Against recomputed transaction value, adoption has a correlation of minus 0.063. In plain terms, higher loyalty adoption does not come with larger baskets here.",
                        "Members account for £29.77M of revenue, or 33.2 percent of the total. Redemption cost £1.73M, 1.9 percent of revenue. The contribution after redemption is £28.04M. That is useful context, but it is not incremental revenue because the data has no member and non-member transaction counts to compare like for like.",
                    ],
                    "figure": ("SunriseReview_3", "Adoption and member revenue share sit almost on the same line. That is a data property, not a causal result."),
                    "meaning": "The programme is collecting a large share of spend, but I cannot show that it creates extra spend.",
                    "conclusion": "Keep the scheme running and test it properly with a holdout group before increasing the budget.",
                },
                {
                    "id": "mix",
                    "title": "Food share did not grow",
                    "question": "Is the revenue mix shifting towards food?",
                    "paragraphs": [
                        "Across the recorded store-days, espresso supplies 45.7 percent of revenue, food 26.1 percent, filter 19.2 percent and retail beans 9.0 percent.",
                        "From 2023 to 2024, food moved from 26.24 percent to 25.90 percent, down 0.34 points. Retail beans moved from 8.90 percent to 9.20 percent, up 0.30 points. The mix is close to flat.",
                    ],
                    "figure": ("SunriseReview_4", "Revenue mix by year. The bars barely move, so there is no food-led shift to chase."),
                    "meaning": "The brief's food growth idea is not supported by this extract.",
                    "conclusion": "Do not build a 2025 plan around a food growth story that the data does not show.",
                },
                {
                    "id": "calendar",
                    "title": "Bank holidays are quieter, not busier",
                    "question": "Should staffing rise for holidays and weekends?",
                    "paragraphs": [
                        "Average revenue per recorded store-day is £1,347 on bank holidays against £2,054 on standard trading days, about 34 percent lower. High-Street stores show the same pattern at £1,365 against £2,046.",
                        "Weekends are also lower in this extract at £1,661 per recorded store-day against £2,195 on weekdays. That runs against normal coffee shop intuition, so I treat it as a feature of which store-days were recorded rather than a staffing rule.",
                    ],
                    "figure": ("SunriseReview_5", "Bank holiday revenue by format. Both formats are below normal trading days."),
                    "meaning": "A blanket holiday staffing uplift is not supported here.",
                    "conclusion": "Use store-level trading history for staffing decisions, and fix the daily table coverage before drawing a weekday rule.",
                },
                {
                    "id": "movement",
                    "title": "Profit swings are store-specific, not seasonal",
                    "question": "Which stores moved, and does the calendar explain it?",
                    "paragraphs": [
                        "Belfast Yard improved by £116,790 and Liverpool Collective by £116,497. At the other end, Bristol Station fell by £141,297.",
                        "The monthly pattern does not repeat cleanly. November 2023 was the worst month at £564,015 profit, while November 2024 was the best at £816,898. That is a warning against planning from month-of-year alone.",
                    ],
                    "figure": ("SunriseReview_6", "The largest store profit movements between 2023 and 2024."),
                    "meaning": "Individual store management matters more here than a single seasonal playbook.",
                    "conclusion": "Investigate the movers store by store before changing promotional calendars.",
                },
            ]},
        ]},
        {"id": "recommendations", "heading": "What I would do first", "blocks": [
            {"type": "recs", "items": [
                {"priority": "High", "title": "Review London store economics",
                 "evidence": "8.5 percent margin, 25.6 percent of store-months loss-making, and about £126k profit per store over two years.",
                 "action": "Pull rent, staffing and footfall for the seven London stores and separate lease problems from trading problems.",
                 "impact": "Targets the weakest margin pool before the next expansion round."},
                {"priority": "High", "title": "Triage the eight December loss-makers",
                 "evidence": "8 stores were loss-making in Dec 2024 and Dundee Station was Structural-Loss at minus £16,932.",
                 "action": "Start with South London Corner and Bristol Station, then work through the rest with store managers.",
                 "impact": "Stops the clearest cash drain, with a visible owner for each site."},
                {"priority": "Medium", "title": "Test loyalty incrementality before scaling it",
                 "evidence": "33.2 percent of revenue comes from members, but adoption has no link to transaction value and the data has no member transaction counts.",
                 "action": "Run a holdout test in a matched set of stores and measure spend per customer, not just member revenue share.",
                 "impact": "Turns a large contribution number into an actual investment decision."},
                {"priority": "Medium", "title": "Stop using format labels as an expansion rule",
                 "evidence": "The data has 58 High-Street stores and 2 Transport-Hub stores. Retail-Park appears in the brief but not in the data.",
                 "action": "Rank sites by regional margin and rent burden instead of format name, and fix the source labels.",
                 "impact": "Avoids pretending a two-store comparison is a strategy."},
                {"priority": "Medium", "title": "Rebuild the dashboard KPI layer",
                 "evidence": "The supplied workbook shows 59 profitable and 41 loss-making stores from a 60-store estate, and 27 of 28 charts have no title.",
                 "action": "Use the raw-data definitions in this analysis as the single KPI source and label every chart.",
                 "impact": "Gives the commercial team one set of numbers they can defend."},
            ]},
        ]},
        {"id": "limits", "heading": "What this cannot tell you", "blocks": [
            {"type": "p", "items": [
                "The daily sales table holds 10,000 store-days out of 43,800 possible store-days. Day-of-week and holiday cuts describe recorded rows, not a full estate census.",
                "There are no member and non-member transaction counts, so I cannot measure incremental spend. The loyalty figures are contribution, not causality.",
                "The date dimension stops at 30 December 2024 even though the brief says 31 December 2024.",
                "The brief describes three store formats, but the store table contains only High-Street and Transport-Hub. The format comparison is deliberately narrow.",
                "The supplied workbook has conflicting KPI counts and mostly untitled charts. I did not use its cached values as source figures.",
                "This is a supplied challenge extract. It is not audited company accounts.",
            ]},
        ]},
    ],
}


TECHNICAL = {
    "title": "Sunrise Coffee: how the analysis was built",
    "lede": "A small reproducible Python pipeline over five CSV tables. It writes one summary JSON and six report charts. This page covers the grain, the metric definitions, the validation checks, and the problems I found in the supplied workbook.",
    "sections": [
        {"id": "solution", "heading": "The solution", "blocks": [
            {"type": "note", "text": "I left the supplied workbook untouched. Its cached dashboard KPIs disagree with the raw data, so the case study uses figures recomputed from the five CSV tables by scripts/analyse.py."},
            {"type": "p", "text": "The pipeline has two steps. analyse.py joins the dimensions to the facts and writes every figure to outputs/summary.json. make_charts.py reads that JSON plus the raw CSVs and writes six PNG figures. There is no randomness and no manual spreadsheet work."},
            {"type": "table", "headers": ["Component", "Path", "Role"], "rows": [
                ["Source CSVs", "data/", "Five supplied tables, read-only"],
                ["Analysis", "scripts/analyse.py", "Joins, cuts, metrics and data-quality checks"],
                ["Summary", "outputs/summary.json", "Single source for every published number"],
                ["Charts", "scripts/make_charts.py", "Six report figures from the summary and CSVs"],
                ["Original workbook", "workbook/Sunrise Coffee_.xlsx", "Supplied artefact, kept for reference, not used as a figure source"],
            ]},
        ]},
        {"id": "data", "heading": "The source data and its grain", "blocks": [
            {"type": "table", "headers": ["Table", "Rows", "Grain or role"], "rows": [
                ["dim_store.csv", "60", "One row per store, with cost structure and loyalty adoption"],
                ["dim_product.csv", "40", "One row per product, with price, cost and margin"],
                ["dim_date.csv", "730", "One row per calendar day, 1 Jan 2023 to 30 Dec 2024"],
                ["fact_daily_sales.csv", "10,000", "Store-day sales with top product and category revenue split"],
                ["fact_store_monthly_profitability.csv", "1,440", "Store-month P&L, 60 stores times 24 months"],
            ]},
            {"type": "pairs", "items": [
                ("Join keys", "store_id, date_id and product_id are unique in the dimensions and fully populated in both facts. There are zero orphan keys."),
                ("Daily coverage", "10,000 recorded store-days against 43,800 possible store-days. I never describe a daily cut as an estate-wide census."),
                ("Period", "The date table ends on 30 December 2024. The brief says 31 December 2024, but I follow the data."),
            ]},
        ]},
        {"id": "metrics", "heading": "Metric definitions", "blocks": [
            {"type": "p", "text": "I kept profitability, loyalty and revenue mix as separate lenses instead of forcing them into one headline."},
            {"type": "code_cards", "items": [
                {"name": "Estate KPIs", "kind": "scripts/analyse.py", "lang": "python",
                 "text": ["Revenue, profit and margin come from the 1,440 store-month P&L rows. Cost shares use the same denominator."],
                 "code": '''rev = float(m.total_monthly_revenue_gbp.sum())
profit = float(m.net_profit_gbp.sum())
return {
    "revenue_gbp": rev,
    "net_profit_gbp": profit,
    "net_profit_margin_pct": profit / rev * 100,
    "cogs_gbp": float(m.total_monthly_cogs_gbp.sum()),
    "rent_gbp": float(m.monthly_rent_gbp.sum()),
    "staffing_gbp": float(m.monthly_staffing_cost_gbp.sum()),
    "loyalty_redemption_gbp": float(m.loyalty_redemption_cost_gbp.sum()),
}''',
                 "note": "The 18.8 percent margin is profit divided by revenue, not an average of store margin percentages."},
                {"name": "Regional cut", "kind": "scripts/analyse.py", "lang": "python",
                 "text": ["Region is joined from dim_store. Margin uses summed revenue and summed profit so larger stores carry their proper weight."],
                 "code": '''g = m.groupby("region").agg(
    revenue=("total_monthly_revenue_gbp", "sum"),
    profit=("net_profit_gbp", "sum"),
)
g["margin_pct"] = g.profit / g.revenue * 100
loss = m.profitability_status.isin(["Loss-Making", "Structural-Loss"])
g["loss_month_share_pct"] = loss.groupby(m["region"]).mean() * 100''',
                 "note": "A simple mean of net_profit_margin_pct would give every store-month equal weight and would overstate small stores."},
                {"name": "Loyalty correlations", "kind": "scripts/analyse.py", "lang": "python",
                 "text": ["Store-level means are used for adoption and member revenue share. Transaction value is recomputed from revenue and transactions because the supplied ATV column is rounded."],
                 "code": '''adopt = m.groupby("store_id").loyalty_adoption_rate.mean()  # from dim_store
member = m.groupby("store_id").loyalty_member_revenue_pct.mean()
atv = d.groupby("store_id").apply(
    lambda x: x.total_revenue_gbp.sum() / x.total_transactions.sum(),
    include_groups=False,
)
r_member = adopt.corr(member)   # 0.998
r_atv = adopt.corr(atv)         # -0.063''',
                 "note": "The 0.998 result is reported as a near-mechanical relationship. It is not presented as proof that loyalty causes higher member revenue."},
            ]},
            {"type": "table", "headers": ["Term", "Definition", "Why it matters"], "rows": [
                ["Net profit margin", "Sum of net profit divided by sum of revenue", "Avoids giving tiny store-months the same weight as large ones"],
                ["Loss-making store-month", "profitability_status is Loss-Making or Structural-Loss", "A monthly flag, not a permanent store verdict"],
                ["Member revenue share", "loyalty_member_spend divided by monthly revenue", "Shows who pays, not whether spend was incremental"],
                ["Redemption cost share", "loyalty_redemption_cost divided by monthly revenue", "The direct cost side of the programme"],
                ["Revenue mix share", "Category revenue divided by the sum of four daily category columns", "Uses the recorded store-day sample only"],
            ]},
        ]},
        {"id": "validation", "heading": "Validation and data quality", "blocks": [
            {"type": "p", "text": "I recomputed the internal identities instead of trusting the dictionary. All four core checks pass."},
            {"type": "table", "headers": ["Check", "Result"], "rows": [
                ["Four category columns sum to daily revenue", "100 percent of rows"],
                ["Net profit equals revenue less COGS, rent, staffing and redemption", "100 percent of rows"],
                ["Published ATV matches revenue divided by transactions", "100 percent within rounding, maximum gap 0.12 percent"],
                ["Nulls in loyalty share, footfall and seating capacity", "0"],
                ["Orphan keys in both fact tables", "0"],
            ]},
            {"type": "note", "text": "Three dictionary claims are wrong for this extract. dim_date has 11 columns and no month_id. The daily fact has an extra column, avg_dwell_time_minutes. Product gross margin runs from 66.0 to 90.4 percent, not the 36 to 80 percent stated in the dictionary."},
        ]},
        {"id": "workbook", "heading": "What I found in the supplied workbook", "blocks": [
            {"type": "p", "text": "The workbook is a useful starting point for layout, but its cached KPI layer is not safe to publish. I kept it as a reference file and rebuilt the numbers from the CSVs."},
            {"type": "table", "headers": ["Issue", "What I saw", "What I did"], "rows": [
                ["Conflicting store counts", "59 Profitable plus 41 Loss-Making from a 60-store estate, and status categories summing to 221", "Ignored those KPI cells and recomputed status from the raw monthly file"],
                ["KPI scale", "2024-only revenue of £44.70M and profit of £8.41M shown as headline totals", "Reported the full 2023 and 2024 totals of £89.69M and £16.88M with the period stated"],
                ["Expansion count", "One KPI says 20 candidate stores while the visible pivot totals 1", "Left the field out of the case study until the definition is fixed"],
                ["Chart labelling", "27 of 28 charts have no title, and Product, Loyalty and Store tabs have no cell values", "Generated six titled report charts with explicit captions"],
                ["Field labels", "week_num holds day of week, IDs are text, and several labels have typos", "Used the CSV column names and documented the mismatch"],
                ["Duplicate block", "The loyalty-per-store range appears twice", "Charts use the analysis output, not the duplicated range"],
            ]},
        ]},
        {"id": "reproduce", "heading": "Reproduce it", "blocks": [
            {"type": "code", "title": "Full analysis", "lang": "bash",
             "code": '''python scripts/analyse.py
python scripts/make_charts.py

# Outputs:
# outputs/summary.json
# outputs/charts/01_region_margin.png ... 06_store_moves.png''',
             "caption": "No random steps, no network calls and no manual workbook edits. Re-running reproduces the same summary and charts."},
            {"type": "pairs", "items": [
                ("Dependencies", "Python 3.10+, pandas, numpy and matplotlib."),
                ("Source safety", "The five CSVs and the original workbook are read-only inputs."),
                ("Determinism", "No seed is needed because no step is random."),
            ]},
        ]},
        {"id": "reflection", "heading": "What I would change with better data", "blocks": [
            {"type": "pairs", "items": [
                ("Full daily census", "Complete store-day rows would let me answer the weekday and holiday questions without sample caveats."),
                ("Member transaction counts", "Member and non-member transactions would turn contribution into a real incrementality test."),
                ("Correct format labels", "A properly populated Retail-Park format would allow the comparison the brief asks for."),
                ("Clean KPI layer", "One agreed definition per card, with titles on every chart, would make the workbook safe for leadership."),
            ]},
            {"type": "note", "text": "The main judgement call was to treat the workbook as a source artefact rather than a source of truth. It would have been easier to quote its KPI cards. It would also have meant publishing contradictory store counts."},
        ]},
    ],
}
