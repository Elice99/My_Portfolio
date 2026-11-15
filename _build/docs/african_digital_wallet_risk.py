"""
PayPesa Wallet Risk Intelligence documentation content, written in
Elisha's voice: he ran the investigation, so the pages say "I did".

Basis for this rewrite: the DataDNA August 2026 challenge brief and its
six hypothesis bullets, his README and PayPesa_Project_Documentation.docx,
the five dashboard screenshots (copied into this site as
DigitalWallet_1..5), and a direct profile he can reproduce from the
shipped CSV files (chi-square, Cramer's V, point-biserial, concentration
and correlation checks re-run at the row level).

Rules: first person, plain words, no em dashes, only claims the data
supports. The dataset is a generated challenge dataset and every page
says so. Where a number differs from his earlier writeup, the verified
row-level number is used and the correction is stated.
"""


# ---------------------------------------------------------------- business
BUSINESS = {
    "title": "PayPesa Wallet Risk Intelligence: what survived the audit",
    "lede": "A five-page Excel dashboard built for the DataDNA August 2026 challenge, with 50,000 wallet transactions from gig workers in four African markets. The brief handed me six risk claims. I tested every one formally. None survived as stated. This page covers what the brief asked, what the data actually said, and what a risk team should do about it.",
    "sections": [
        {"id": "problem", "heading": "The problem the brief set", "blocks": [
            {"type": "note", "text": "I built this for the Onyx Data #DataDNA monthly challenge (August 2026). The PayPesa scenario is fictional and the dataset is synthetic: 50,000 transactions from 5,000 gig workers across Nigeria, Kenya, Ghana and South Africa, in USD, spanning 2023-01-01 to 2024-12-31. I say that everywhere on these pages, because the honest reading of any generated dataset is patterns within the data, not claims about real African fintech fraud."},
            {"type": "p", "items": [
                "My first look at this data was alarming. Fraud, dispute and reversal flags all sat at about 50%, across 50,000 transactions. On its face that is a platform in full fraud crisis, and the natural move is to start hunting for the pocket where it comes from.",
                "The brief pushed in the same direction with six specific claims: USSD carries 2.3 times the app fraud rate, Nigeria and Kenya drive 70% of fraud volume, accounts under 90 days defraud three times as often, market traders dispute most, velocity scores predict fraud, and month-ends spike cash-outs and reversals.",
                "Before trusting any of it, I did something that changed the whole project: I checked the data against its own documentation. It did not match, in at least five places. So instead of a fraud-hunt, this became a validation-first investigation: prove what the data actually is, test every claim formally, and only report what survives.",
            ]},
        ]},
        {"id": "hypotheses", "heading": "Testing the brief's six claims", "blocks": [
            {"type": "p", "text": "This is the table I would want to read first: each claim from the brief, what I found when I tested it, and my verdict. I ran descriptive cuts first, then chi-square with Cramér's V for the categorical ones and point-biserial correlation for the continuous ones. The honest headline is that all six came back flat or mis-stated, and proving that carefully is the most useful thing this project did."},
            {"type": "table", "headers": ["The brief claimed", "What I found in the data", "My verdict"], "rows": [
                ["USSD shows 2.3x higher fraud rate than the app channel",
                 "USSD runs 51.19% fraud against Mobile App at 50.33%. A 0.9 point gap, not 2.3 times. USSD does lead one ranking that matters: fraud loss per dollar processed, at 51.46 cents.",
                 "Does not hold on frequency. USSD's real distinction is exposure per dollar, which is a different risk conversation."],
                ["Nigeria and Kenya drive 70% of fraud volume",
                 "The four markets hold 12.4K to 12.6K transactions each; Nigeria and Kenya together are 49.7% of volume, fraud included. There is no 70%.",
                 "Does not hold. Volume is almost perfectly balanced across the four markets."],
                ["Accounts under 90 days defraud three times as often",
                 "Under-90-day accounts run 51.06% fraud against 50.25% for the rest. Under one percentage point.",
                 "Does not hold. New-account risk in this data is noise, not a signal."],
                ["Market traders have the highest dispute rate",
                 "Informal Vendor is highest at 53.34%, Delivery Rider lowest at 49.02%. Market Trader sits mid-pack. The overall effect size stays negligible (Cramér's V 0.016).",
                 "Does not hold as stated, though the 4.3 point top-to-bottom segment spread is the widest single-dimension gap I found and worth a closer look."],
                ["High velocity scores correlate with fraud",
                 "Point-biserial correlation between velocity score and the fraud flag: -0.001. Processing time: -0.002.",
                 "Does not hold. The behavioural scores carry no fraud signal at all in this data."],
                ["Month-ends spike cash-out and reversal rates",
                 "Month-end transactions run 51.24% fraud against 50.26% otherwise, on 1,575 month-end rows. Inside sampling noise.",
                 "Does not hold. The spike the brief promised is about one point, which is what chance produces."],
            ]},
            {"type": "p", "text": "And one finding from the same exercise that sits above all of it: the shipped data dictionary does not describe the shipped data. It documents fraud flags at 7% (observed 50.29%), disputes at 5% (observed 50.07%), reversals at 8% (observed 49.90%), four outcome categories (observed eight, all near 12.5%), four gig segments (the worker table carries 15), and lowercase channel labels (the data uses Agent, API/Third-Party, Mobile App, POS, USSD). I profiled the CSVs directly and worked from what is actually in them."},
        ]},
        {"id": "answer", "heading": "The short answer", "blocks": [
            {"type": "verdict", "text": "With the brief's claims settled, here is what the data does say. Fraud frequency is genuinely flat: every one of the ten categorical dimensions I tested returns a Cramér's V below 0.04, deep in negligible territory, and the two continuous risk scores correlate with the fraud flag at essentially zero. The only places the pattern moves at all are two-way combinations: Ghana with Mobile App runs 52.72% fraud on 2,094 transactions and Nigeria with USSD runs 52.23% on 1,030, roughly two points above the 50.29% baseline, which is the strongest relative signal in the dataset while still being modest in absolute terms. Financial exposure tells its own story: POS, API/Third-Party and Agent carry the largest absolute losses ($3.08M to $3.13M each) purely because they carry the volume, while USSD has the worst loss rate per dollar. And the platform's own risk scores fail their audit: South Africa carries the highest Market Fraud Index (797.51) despite the lowest observed fraud rate (49.75%), and the worker risk score correlates with actual fraud losses at r = -0.003. My conclusion for a risk team: on this data, frequency-based targeting has nothing to grab, exposure and the two-way lens are where the signal lives, and the stated risk indicators need independent validation before anyone steers by them."},
            {"type": "figure", "spec": ("DigitalWallet_1", "Page one, the Fraud Exposure Executive Overview: the 50K transactions and $24.98M volume cards, the three ~50% doughnut rates, the near-uniform eight-outcome distribution, monthly rate trend, fraud loss by channel, and the channel risk and exposure table.")},
        ]},
        {"id": "numbers", "heading": "Numbers at a glance", "blocks": [
            {"type": "stat_grid", "items": [
                ("50,000", "transactions analysed"),
                ("$24.98M", "total volume processed"),
                ("50.29%", "overall fraud rate"),
                ("$12.56M", "recorded fraud loss"),
                ("<0.04", "max Cramér's V across 10 dimensions"),
                ("20.4%", "of losses held by the top 10% of workers"),
            ]},
            {"type": "p", "text": "Where they come from: the headline KPIs, channel table and market cards are read off my dashboard pages, and the statistical results (Cramér's V values, correlations, concentration and tenure cuts) come from my own re-run of the tests on the shipped CSV files, which is the same thing my dashboard page two visualises."},
        ]},
        {"id": "meaning", "heading": "How to read each number", "blocks": [
            {"type": "table", "headers": ["Number", "How I got it", "How to read it"], "rows": [
                ["50.29% fraud rate", "Fraud-flagged transactions over all 50,000", "Documented at 7%. The flags behave like coin flips in this data, which is itself the first finding."],
                ["$12.56M fraud loss", "Fraud loss summed over flagged transactions", "An average of $499.47 per fraud event, generated from a heavy-tailed distribution, so per-event severity varies widely."],
                ["Cramér's V below 0.04, ten times", "Chi-square test of independence for each categorical dimension against the fraud flag, converted to an effect size", "On a scale where 0.10 is the floor for even a weak effect, this is a formally proven null. No single category explains who gets flagged."],
                ["52.72% at Ghana x Mobile App", "Fraud rate inside that channel-by-market cell, 2,094 transactions", "The largest cell deviation, about 2.4 points above baseline. Suggestive, not conclusive; with twenty cells tested some elevation is expected by chance."],
                ["51.46% USSD loss rate", "USSD fraud loss over USSD volume", "The worst exposure per dollar despite the smallest absolute loss ($1.08M), because USSD carries a fifth of the transaction volume."],
                ["r = -0.003", "Pearson correlation between each worker's risk score and that worker's actual fraud loss", "The platform's worker-level risk score has no relationship with observed fraud behaviour."],
                ["20.4% of losses from the top 10% of workers", "Workers ranked by total fraud loss, share of the $12.56M total", "About twice their fair share, but far from the 80/20 concentration a watchlist strategy assumes."],
                ["797.51 South Africa Fraud Index", "The market table's own stated index, read off my page-three card", "The highest of four markets, attached to the lowest observed fraud rate (49.75%). The label does not track the data."],
            ]},
        ]},
        {"id": "findings", "heading": "What I found", "blocks": [
            {"type": "findings", "items": [
                {
                    "id": "f-audit",
                    "title": "The 50% crisis was a documentation failure before it was a fraud finding",
                    "question": "Can the headline numbers be trusted at all?",
                    "paragraphs": [
                        "Fraud, dispute and reversal flags all sit at 49.9% to 50.3%. The dictionary documents 7%, 5% and 8%. The eight transaction outcomes each hold 12.2% to 12.6% of the file, which is what a near-uniform random draw produces, not what a risk process produces.",
                        "I could have reported the crisis. Instead I audited: flag rates against the dictionary, outcome categories against the four the dictionary promised, channel labels against the documented list, gig segments against four (the worker table carries 15), and the risk score scale against its own generator spec. At least five fields do not match their documentation.",
                        "That audit reframed everything downstream. The ~50% rates are structurally consistent with coin-flip generation, and the brief's six risk claims were tested against the data as it is, not the data as documented. Several of the claims, like the 2.3x USSD rate and 3x new-account risk, probably came from the same documentation the data ignores.",
                    ],
                    "meaning": "An audit of the data against its own documentation is not overhead. Here it redirected the entire analysis before a single finding was published.",
                    "conclusion": "Audit any new data source against its own documentation before building on it, and report the mismatches as findings.",
                    "figure": ("DigitalWallet_1", "Page one carries the claim at face value, 50K transactions, $24.98M volume, three ~50% doughnut rates and eight near-uniform outcomes, so a reviewer sees exactly what I chose not to take at face value."),
                },
                {
                    "id": "f-null",
                    "title": "The formally proven null: no single dimension explains the flags",
                    "question": "Does any category the platform tracks predict fraud?",
                    "paragraphs": [
                        "I tested ten dimensions against the fraud flag: channel, country, gig segment, KYC tier, age band, gender, transaction type, channel subtype, transaction outcome and day of week. My page-two leaderboard shows every Cramér's V, from Age Band at 0.036 down to Country at 0.007. All of them are deep inside the negligible band on a scale where 0.10 is the floor even for a weak effect.",
                        "I applied the caveat that matters at this sample size: with n = 50,000, chi-square returns a significant p-value for almost any non-zero difference, so significance alone proves nothing. Every result was paired with its effect size, and every effect size is negligible. My own re-run of the tests on the raw CSVs lands in the same place, with even smaller values.",
                        "The continuous candidates failed too. Velocity score against the fraud flag correlates at -0.001 and processing time at -0.002. The behavioural scores the platform records carry no fraud signal whatsoever in this data.",
                    ],
                    "meaning": "A null result, proven with effect sizes rather than impressions, is a real finding. It tells a risk team that frequency-based targeting has nothing to grab here.",
                    "conclusion": "Stop looking for a single fraud pocket in this data. The search has been done formally and it came back empty.",
                    "figure": ("DigitalWallet_2", "Page two, Transaction and Risk Intelligence: the Cramér's V leaderboard with all ten dimensions negligible, the transaction-lifecycle bars (25.15K flagged, 25.04K disputed, 24.95K reversed), and the processing-time and transaction-type cuts."),
                },
                {
                    "id": "f-interaction",
                    "title": "When one dimension says nothing, two dimensions whisper",
                    "question": "Can a pattern hide from every single-dimension test?",
                    "paragraphs": [
                        "A flat result on every marginal test does not rule out a pattern living in a combination, because no one-dimensional cut can see it. So I crossed channel with market and read the twenty cells against the 50.29% baseline.",
                        "Two cells stand above the rest: Ghana with Mobile App at 52.72% on 2,094 transactions and Nigeria with USSD at 52.23% on 1,030. A few others sit about a point high, Ghana with USSD at 51.91% and Nigeria with POS at 51.37%, while the lowest cell, South Africa with Mobile App, sits at 48.10%. Every one-dimension test returned nothing, and the two-way cut is where the only movement in this dataset lives.",
                        "I want to be precise about the strength here. A two-point deviation on a couple of thousand rows is suggestive, not conclusive, and with twenty cells tested some elevation is expected from chance alone. What makes it worth reporting is not its size but its exclusivity: it is the only relative signal anywhere in the frequency data, which is exactly why a risk review should look at channel-by-market intersections rather than either dimension alone.",
                    ],
                    "meaning": "Interaction analysis earns its place when marginals are flat. Here it is the only lens that moves at all, even though the movement is modest.",
                    "conclusion": "Review channel controls at the channel-by-market intersection, and treat the elevated cells as candidates for a targeted look, not proven hotspots.",
                    "figure": ("DigitalWallet_3", "Page three, Market and Channel Intelligence: the country-by-channel fraud risk matrix with its dual-encoded heat map, the highest-risk market and channel cards, and the country exposure table."),
                },
                {
                    "id": "f-exposure",
                    "title": "Frequency and exposure rank differently, and only one of them should set priorities",
                    "question": "Where does the money actually go?",
                    "paragraphs": [
                        "USSD has the highest fraud rate of any channel at 51.19% and the highest loss rate per dollar at 51.46 cents. It also has the smallest absolute loss, $1.08M, because it carries 4,229 transactions while Agent, POS and API/Third-Party each carry 12,300 or more.",
                        "The absolute-loss ranking inverts that: POS $3.13M, API/Third-Party $3.12M, Agent $3.08M, Mobile App $2.16M, USSD $1.08M. Those three big channels lead the absolute table mostly by being big, which is why I computed fraud loss rate (loss over total volume) throughout, so a channel is not punished or pardoned for its size.",
                        "The same discipline settles the worker question. The top 10% of workers by loss hold 20.35% of the $12.56M, about twice their fair share but nowhere near the concentration a watchlist strategy assumes. Fraud loss per event is drawn from a heavy-tailed distribution, so a few big single events are expected from randomness alone; the honest read is that exposure is broad, and controls have to operate across the transaction base rather than chase a small group.",
                    ],
                    "meaning": "Frequency, severity and concentration are three different questions. Ranking by the wrong one sends the control budget to the wrong place.",
                    "conclusion": "Prioritise controls by financial exposure per dollar, and design them for a dispersed risk base, not a fraud pocket.",
                    "figure": ("DigitalWallet_1", "Page one pairs the two readings in one table: fraud rate and fraud loss side by side for every channel, which is where the USSD inversion becomes visible."),
                },
                {
                    "id": "f-scores",
                    "title": "The platform's own risk scores fail their audit",
                    "question": "Can the stated risk indicators be trusted to find risk?",
                    "paragraphs": [
                        "South Africa carries the highest Market Fraud Index of the four markets, 797.51, and the lowest observed fraud rate, 49.75%, against Ghana's 50.68% with an index of 421.60. The label ranks the markets almost opposite to what the transactions show.",
                        "At worker level I checked it directly: the correlation between each worker's risk score and that worker's actual fraud loss is r = -0.003, and against fraud count r = -0.009. Whatever the score measures, it is not what the transaction data shows.",
                        "The channel table fails the same audit: its reference fraud-rate field is documented as a 0.02 to 0.15 rate, but the shipped values read 484 to 675, which is not a rate on any scale. Three stated risk indicators, market index, worker score and channel reference rate, and none of them tracks observed behaviour in this data.",
                    ],
                    "meaning": "A risk score that does not correlate with outcomes is decoration. Before steering controls by any stated indicator, check it against the outcomes it claims to predict.",
                    "conclusion": "Treat the Market Fraud Index, worker risk scores and channel reference rates as unverified until they are re-derived from observed outcomes.",
                    "figure": ("DigitalWallet_3", "Page three carries the sharpest version of this: the Market Risk Index card reading 797.51 for South Africa directly above a country table showing it with the lowest observed fraud rate."),
                },
            ]},
        ]},
        {"id": "recommendations", "heading": "What I would do next", "blocks": [
            {"type": "recs", "items": [
                {"priority": "High", "title": "Set controls by financial exposure, not fraud frequency",
                 "evidence": "USSD leads fraud rate (51.19%) and loss rate (51.46 cents per dollar) but holds the smallest absolute loss ($1.08M); POS, API/Third-Party and Agent hold $3.1M each on volume alone.",
                 "action": "Rank control investments by fraud loss rate per dollar and absolute exposure together, and stop ranking by event frequency alone.",
                 "impact": "Puts the control budget where the dollars are, not where the percentages are."},
                {"priority": "High", "title": "Review channel controls at the channel-by-market intersection",
                 "evidence": "Every one-dimensional test is negligible, while Ghana x Mobile App (52.72%, n=2,094) and Nigeria x USSD (52.23%, n=1,030) sit about two points above baseline.",
                 "action": "Make the channel-plus-market pair the unit of review, and validate the elevated cells against a held-out time window before acting.",
                 "impact": "Aims the only frequency signal that exists in this data at the exact place it lives."},
                {"priority": "High", "title": "Re-derive the stated risk indicators from observed outcomes",
                 "evidence": "South Africa's Fraud Index is the highest of four against the lowest observed rate; worker risk score vs actual loss correlates at r = -0.003; channel reference rates read 484 to 675 on a field documented as 0.02 to 0.15.",
                 "action": "Rebuild the market index, worker score and channel reference rates from transaction outcomes, or publish them as unvalidated until they are.",
                 "impact": "Stops decisions being steered by labels that do not track the data."},
                {"priority": "Medium", "title": "Do not build a worker watchlist from loss concentration",
                 "evidence": "The top 10% of workers hold 20.35% of losses, twice their fair share but far from 80/20, and per-event loss is heavy-tailed by construction.",
                 "action": "Design controls for broad coverage across the worker base, and use persistence across multiple fraud events (not single large losses) to flag individuals.",
                 "impact": "Avoids a small-population strategy that misses most of the exposure."},
                {"priority": "Medium", "title": "Investigate the segment spread before trusting it",
                 "evidence": "Dispute rates run 49.02% (Delivery Rider) to 53.34% (Informal Vendor), the widest single-dimension gap in the data, though the overall effect size stays negligible (V = 0.016).",
                 "action": "Re-test the segment spread on fresh data with a multiple-comparisons correction before acting on it.",
                 "impact": "Either confirms the one marginal signal worth having, or retires it cleanly."},
                {"priority": "Low", "title": "Run the documentation audit as a standing step",
                 "evidence": "At least five fields in this dataset do not match their own documentation, including the three flag rates the whole crisis narrative rested on.",
                 "action": "Add a documentation-versus-observed audit to the intake checklist for any new dataset.",
                 "impact": "Catches story-corrupting mismatches before they reach a dashboard."},
            ]},
        ]},
        {"id": "limits", "heading": "What this can't tell you", "blocks": [
            {"type": "p", "items": [
                "The dataset is synthetic, built for the challenge. Every finding describes patterns in this specific file, not real African digital-wallet fraud.",
                "The ~50% flag rates and near-uniform outcomes are consistent with the generator having applied no correlations at all. A platform with genuinely random flags cannot yield fraud drivers, no matter how hard anyone tests.",
                "Cramér's V thresholds (0.10 / 0.30 / 0.50) are conventions, applied here alongside percentage-point differences and sample size, not as a rigid cutoff.",
                "The elevated channel-by-market cells are two points above baseline on one to two thousand rows. Suggestive, not conclusive, and not cross-validated on a held-out window. I say that on the page rather than dressing it up.",
                "One honest note on my own dashboard: the page-four worker table lists workers by name, and this dataset reuses common names across different worker ids, so each row there pools several distinct people. I treat that table as name groups, and I ran the worker-level checks in these pages on worker ids instead.",
                "My earlier project writeup quoted the three channel-by-market spikes as roughly ten points above baseline (60.79%, 60.71%, 60.61%). Checking the raw data directly, those cells read 50.79%, 50.71% and 50.61%, about half a point above baseline, and the largest genuine deviations are the Ghana x Mobile App and Nigeria x USSD cells at one to two points. These pages use the corrected numbers.",
            ]},
        ]},
    ],
}


# --------------------------------------------------------------- technical
TECHNICAL = {
    "title": "PayPesa Wallet Risk Intelligence: how I built it",
    "lede": "The build behind the audit: the Excel stack and star schema, the Power Query preparation, the statistical test layer with the formulas as I ran them, the DAX measures with the denominator decisions inside them, and the data-quality calls that reframed the project.",
    "sections": [
        {"id": "solution", "heading": "The solution", "blocks": [
            {"type": "note", "text": "The formulas and measures on this page are from my project documentation and workbook, as I ran them. Every number traces to my dashboard pages, my README and documentation doc, and a direct profile of the shipped CSV files."},
            {"type": "p", "text": "I built this in Excel, deliberately: Power Query for the load and cleaning layer, Power Pivot for a proper star schema in the data model, and DAX for every KPI as a live measure. The result is a five-page dashboard where one slicer click filters every visual at once, which is what a model gives you and a pile of PivotTables does not. The five pages follow the investigation's order: the claim at face value, the formal frequency tests, the interaction lens, worker-level exposure, then the synthesis page with findings and priorities."},
            {"type": "table", "headers": ["Component", "What I built it from", "Role"], "rows": [
                ["fact_transactions", "50,000 rows, 15 fields", "One row per wallet transaction: worker, date, channel, market, type, amount, outcome, three flags, velocity, fraud loss, processing time"],
                ["dim_worker", "5,000 rows", "Gig segment, account tenure, KYC tier, gender, age band, risk score, active status, preferred channel"],
                ["dim_channel", "12 rows", "Channel type and subtype, digital flag, reference fraud rate, internet requirement"],
                ["dim_market", "4 rows", "Country, currency, dominant channel, regulatory tier, FX rate, market fraud index"],
                ["dim_date", "730 rows", "Month, quarter, day of week, weekend and month-end flags"],
                ["The report", "5 pages in Excel", "Executive overview, transaction and risk intelligence, market and channel intelligence, workers and behavioural risk, insights and risk action center"],
            ]},
            {"type": "p", "text": "The relationships are the standard star, all four dimensions joining the fact on their keys (worker_id, date_id, channel_id, market_id) as many-to-one in Power Pivot. Building the model first is what made the statistical pages possible: the same fraud rate measure slices by any dimension, so the leaderboard and the twenty-cell heat map read off one definition."},
        ]},
        {"id": "prep", "heading": "The Power Query preparation", "blocks": [
            {"type": "p", "text": "The load layer did four jobs before a single visual existed, and the fourth one changed the project."},
            {"type": "p", "items": [
                "Type correction: the flags and dates arrived as text in places, so I enforced proper types on load rather than trusting the CSV's apparent shapes.",
                "Bucketing: I derived tenure bands (0-30 days, 31-90, 91-180, 181-365, 2+ years), velocity bands and risk-score bands in Power Query, because the brief's claims were phrased in bands (accounts under 90 days) and the tests needed comparable groupings.",
                "Category validation: I compared every categorical column's observed values against the dictionary's documented list, which is how the mismatches surfaced: eight outcome categories against four documented, five channel labels against the documented lowercase set, fifteen gig segments against four, and a risk score running 0.002 to 99.96 against a generator spec that implies 0 to 1.",
                "Flag-rate validation: fraud documented at 7% true, disputes at 5%, reversals at 8%; observed 50.29%, 50.07% and 49.90%. That check came before anything else and set the tone for everything after it.",
            ]},
            {"type": "p", "text": "One channel-table detail worth recording: the reference fraud-rate field is documented as a 0.02 to 0.15 rate, but the shipped values read 484 to 675. It is not a rate on any scale, so I did not use it as one. That field is part of the audit finding, not part of the analysis."},
        ]},
        {"id": "stats", "heading": "The statistical test layer", "blocks": [
            {"type": "p", "text": "This is the part of the build I would defend in a review: every claim in the brief was tested formally, in Excel, with the formulas visible rather than buried in a script."},
            {"type": "p", "text": "The chi-square test of independence asks whether a category and the fraud flag are statistically independent. I built the contingency table of observed counts, computed the expected table as (row total x column total) / grand total, and summed the squared deviations."},
            {"type": "code", "title": "Chi-square, as I ran it", "lang": "text", "code": r'''
Chi-Square =
SUMPRODUCT((Observed_Range - Expected_Range)^2 / Expected_Range)

p-value =
CHISQ.DIST.RT(chi_square_stat, degrees_of_freedom)
'''},
            {"type": "p", "text": "Then the step most dashboards skip: the effect size. At n = 50,000, chi-square returns a significant p-value for almost any non-zero difference, so I paired every test with Cramér's V and read the V, not the p."},
            {"type": "code", "title": "Cramér's V", "lang": "text", "code": r'''
Cramer's V = SQRT(Chi-Square / (N * MIN(rows - 1, cols - 1)))

< 0.10     negligible  -> logged, not reported as a finding
0.10-0.30  weak        -> worth a mention
0.30-0.50  moderate    -> a real finding
> 0.50     strong      -> headline material
'''},
            {"type": "p", "text": "For the continuous candidates I coerced the boolean flag to 0/1 and used a direct Pearson correlation, which for a binary flag is the point-biserial correlation."},
            {"type": "code", "title": "Point-biserial for velocity and processing time", "lang": "text", "code": r'''
=CORREL(velocity_score_range, fraud_flag_as_0_1_range)

velocity score vs fraud flag:  r = -0.001
processing time vs fraud flag: r = -0.002
'''},
            {"type": "p", "text": "The concentration check got the same treatment. A standard Pareto of ranked fraud loss was extended with a persistence flag: workers appearing across multiple fraud events are real signal candidates, while a worker with one large loss event is statistically expected noise from the heavy-tailed loss distribution. That distinction is what keeps the dispersion finding honest, and it is also why I re-ran the concentration math directly: the top 10% of workers hold 20.35% of losses, which I would rather state exactly than round into a story."},
        ]},
        {"id": "measures", "heading": "The measures and the decisions inside them", "blocks": [
            {"type": "p", "text": "Every KPI is a live DAX measure in the data model, so every card updates when a slicer moves. The definitions are deliberately plain, with the decisions in the denominators."},
            {"type": "code", "title": "Core risk measures", "lang": "dax", "code": r'''
Total Transactions := COUNTROWS(fact_transactions)

Total Volume USD := SUM(fact_transactions[amount_usd])

Fraud Transactions :=
CALCULATE(COUNTROWS(fact_transactions),
    fact_transactions[is_fraud_flagged] = TRUE())

Fraud Rate := DIVIDE([Fraud Transactions], [Total Transactions], 0)

Fraud Loss USD :=
CALCULATE(SUM(fact_transactions[fraud_loss_usd]),
    fact_transactions[is_fraud_flagged] = TRUE())

Avg Fraud Loss per Fraud Txn :=
DIVIDE([Fraud Loss USD], [Fraud Transactions], 0)
'''},
            {"type": "p", "text": "The denominator decision I care most about: Fraud Loss Rate divides fraud loss by total transaction volume, not by fraud volume. It answers how many cents of every dollar processed are exposed to fraud, which is the exposure question, not the per-event severity question. That one choice is what makes the USSD story readable: highest loss rate per dollar, lowest absolute loss, because the volume is a fifth of the other channels."},
            {"type": "code", "title": "The exposure measure", "lang": "dax", "code": r'''
Fraud Loss Rate := DIVIDE([Fraud Loss USD], [Total Volume USD])
'''},
            {"type": "p", "text": "Dispute Rate and Reversal Rate follow the same pattern as Fraud Rate, filtered on is_disputed and is_reversed. The lifecycle view on page two composes them: 50.00K transactions, 25.15K flagged, 25.04K disputed, 24.95K reversed, which is the coin-flip structure made visible."},
            {"type": "pairs", "items": [
                ("DIVIDE with a zero fallback", "Fraud Rate and the per-event averages use DIVIDE's third argument so an empty slicer selection shows a blank, not a division error."),
                ("Measures, not typed numbers", "Every figure on the dashboard computes live. Nothing on those pages goes stale when a slicer or a refresh changes the context."),
                ("One fraud-rate definition everywhere", "The leaderboard, the twenty-cell heat map, the channel table and the market cards all read the same measure, so the pages cannot disagree with each other."),
            ]},
        ]},
        {"id": "visuals", "heading": "The dashboard architecture and visual grammar", "blocks": [
            {"type": "p", "text": "Five pages, one story, in the order the investigation actually ran:"},
            {"type": "table", "headers": ["Page", "What it carries", "The decision behind it"], "rows": [
                ["1. Executive Overview", "The claim at face value: KPI cards, three ~50% doughnuts, outcome mix, monthly trend, channel exposure table", "Show the alarming version honestly first, so the audit that follows has something concrete to test"],
                ["2. Transaction & Risk Intelligence", "The Cramér's V leaderboard across ten dimensions, lifecycle bars, processing-time and transaction-type cuts", "Put the null result on the record with the effect sizes visible, not just percentages"],
                ["3. Market & Channel Intelligence", "The country-by-channel dual-encoded heat map, market cards, country exposure table", "The interaction lens: where the only frequency movement in the data lives, next to the Fraud Index contradiction"],
                ["4. Workers & Behavioural Risk", "Worker-level exposure, segment and tenure risk bands, the risk-score columns", "Where the stated risk score meets observed behaviour, with the name-pooling caveat stated"],
                ["5. Insights & Risk Action Center", "Seven numbered findings, prioritised recommendations tied to evidence", "Synthesis with the priorities ordered by exposure, not frequency"],
            ]},
            {"type": "p", "text": "Two visual choices I would repeat: dual-encoded heat maps, where colour carries one metric and an embedded number carries a second, so one grid answers two questions without a legend hunt; and combo charts built with discipline, bars that share a currency unit on one axis and a rate as a line on a secondary axis, never two mismatched bar series competing for the same space."},
            {"type": "figure", "spec": ("DigitalWallet_5", "Page five, the Risk Action Center: seven numbered findings with the priorities and the distinction between frequency risk and severity risk stated explicitly.")},
        ]},
        {"id": "quality", "heading": "Data quality calls I made", "blocks": [
            {"type": "p", "text": "The audit trail is the heart of this build. Five documented-versus-observed mismatches, each checked directly against the raw data:"},
            {"type": "table", "headers": ["Field", "Documented", "Observed", "What I did"], "rows": [
                ["is_fraud_flagged", "7% true", "50.29% true", "Reported the mismatch as a finding; tested claims against the observed data"],
                ["is_disputed / is_reversed", "5% / 8% true", "50.07% / 49.90% true", "Same treatment; the three ~50% flags together suggest coin-flip generation"],
                ["transaction_outcome", "4 weighted categories", "8 categories, 12.2% to 12.6% each", "Worked from the eight; the near-uniform spread is itself diagnostic"],
                ["channel_type / gig_segment", "5 lowercase labels / 4 segments", "5 renamed labels / 15 segments", "Used observed labels; joined tests on the real categories"],
                ["risk_score", "Beta(2,5) implies a 0-1 scale", "0.002 to 99.96", "Treated as a 0-100 score per the field's own description; tested it against outcomes rather than trusting either spec"],
            ]},
            {"type": "p", "text": "The conclusion from this phase shaped everything: the documentation supplied with the challenge does not reliably describe the deployed data, so every number I published was checked against the raw file, never assumed from the dictionary. My own earlier writeup carried one error of its own, the channel-by-market spikes quoted as roughly ten points; re-checked against the raw rows they are about half a point, and the corrected figures are what these pages use. I would rather correct myself in public than leave a wrong number standing."},
        ]},
        {"id": "validation", "heading": "Where my numbers come from", "blocks": [
            {"type": "p", "text": "Every figure on both pages is one I can trace:"},
            {"type": "table", "headers": ["Number", "Where I got it", "Cross-check"], "rows": [
                ["50,000 transactions, $24.98M volume, 50.29% fraud rate", "My dashboard page one", "Direct profile of fact_transactions (25,145 flagged rows)"],
                ["$12.56M fraud loss, $499.47 per fraud event", "My dashboard pages one and two", "Direct sum over flagged rows"],
                ["Cramér's V leaderboard (0.036 down to 0.007)", "My dashboard page two", "My own re-run of all ten chi-square tests on the CSVs; same ranking, same negligible verdict"],
                ["Channel rates and losses (USSD 51.19% rate, $1.08M loss; POS $3.13M)", "My channel exposure table", "Direct group-by on the fact table"],
                ["Market cards (Ghana 50.68% highest rate, South Africa 49.75% lowest, index 797.51)", "My page-three cards", "Direct group-by plus the shipped dim_market index values"],
                ["Interaction cells (Ghana x Mobile App 52.72% on 2,094; Nigeria x USSD 52.23% on 1,030)", "My page-three matrix", "Direct cell-level computation; my earlier writeup's 60.79% figures corrected to these"],
                ["Concentration (top 10% of workers hold 20.35% of losses)", "My Pareto analysis", "Direct worker-level computation, both with and without zero-loss workers included"],
                ["Risk-score failure (r = -0.003 vs loss, r = -0.009 vs fraud count)", "My worker-level check", "Direct correlation of dim_worker risk scores against per-worker outcomes"],
                ["Row counts 50,000 / 5,000 / 12 / 4 / 730", "Direct profile of the CSVs", "The challenge brief's dataset description"],
            ]},
            {"type": "note", "text": "One figure I deliberately do not quote from my dashboard: the page-four table's per-worker loss amounts, because that visual groups by displayed name and the dataset reuses common names across worker ids. The worker-level claims on these pages are computed on worker ids."},
        ]},
        {"id": "decisions", "heading": "My decisions and trade-offs", "blocks": [
            {"type": "table", "headers": ["Decision I made", "Why", "Trade-off I accepted"], "rows": [
                ["Led with the data audit, not the fraud hunt", "The documentation mismatch corrupted the premise of every claim, including the brief's", "The dashboard's first page shows a crisis I then spend two pages deflating"],
                ["Reported effect sizes, not p-values", "At n = 50,000, significance is nearly free; Cramér's V is what separates signal from noise", "A reviewer used to p-value tables sees a column of tiny numbers and has to read the scale"],
                ["Computed fraud loss rate against total volume", "Exposure per dollar is the steering metric; per-event averages reward scary outliers", "A channel with a terrible rate but tiny volume (USSD) can look defensible until both readings are shown"],
                ["Tested the two-way cut only after the one-way nulls", "Interaction claims are strongest when the marginals are known to be flat", "The elevated cells are modest, so the finding needed careful, hedged wording"],
                ["Re-ran every headline statistic directly on the CSVs", "My own writeup had one mis-quoted figure; the data is the referee", "Some numbers on these pages are deliberately corrected from my earlier project documents"],
                ["Kept the name-pooling caveat on the record", "The page-four table groups by name and the data reuses names; hiding it would invite a reviewer to find it first", "One of my own visuals needs a footnote"],
                ["Flagged the channel reference-rate field as unusable", "Values of 484 to 675 on a field documented as a 0.02 to 0.15 rate cannot be used as a rate", "The channel table loses a documented column"],
            ]},
        ]},
        {"id": "upkeep", "heading": "Publication and next steps", "blocks": [
            {"type": "steps", "items": [
                ("Sync the repository writeup", "My README and documentation doc still carry the ten-point interaction claim and the 11.73% concentration figure; the verified numbers (about half a point on those cells, 20.35% concentration) should be corrected there so the repo and these pages agree."),
                ("Cross-validate the elevated cells", "Split the two years into a training and a hold-out window and check whether Ghana x Mobile App and Nigeria x USSD persist before anyone treats them as hotspots."),
                ("Systematise the two-way scan", "Ten dimensions give 45 pairs; I tested the most plausible one. A full scan with a multiple-comparisons correction would either find more structure or close the question properly."),
                ("Re-derive the risk indicators", "Rebuild the market fraud index and worker risk score from observed outcomes and measure how far they land from the shipped versions."),
                ("Re-run on a regenerated dataset", "If the challenge data is regenerated with correlations applied, the same workbook and tests re-run unchanged; only the verdicts would move."),
            ]},
        ]},
        {"id": "reflection", "heading": "What this project shows", "blocks": [
            {"type": "p", "items": [
                "This project is my argument that a null result, done properly, is a deliverable. Ten dimensions tested with visible formulas, effect sizes instead of p-value theatre, and the honesty to report that the platform's own risk scores correlate with nothing, that is a risk analysis a team can actually act on.",
                "The habits I would carry forward: audit a dataset against its own documentation before believing either, pair every significance test with an effect size, separate frequency from severity from concentration, and when my own earlier number turns out wrong, correct it in the open.",
            ]},
        ]},
    ],
}
