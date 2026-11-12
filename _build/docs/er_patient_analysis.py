"""
ER Patient Analysis documentation content.
Sources: the Business and Technical documentation .docx files, plus the
dashboard screenshot. Uses the generic `sections` format (see build_docs.py).

Where the written documentation and the dashboard screenshot disagree, these
pages follow the screenshot (it is what a visitor sees) and say so openly:
  - satisfaction: report shows 5.47 average and 75.10% not rated; a direct CSV
    count gave 4.99 and 72.7% blank. About 222 scores of 0 would explain both.
  - referral: a CSV profile counted 5,400 blanks; the report shows a 'None'
    category of exactly 5,400 and 58.59% unreferred.
The 222 figure is arithmetic (6,921 not rated in the report minus 6,699 blank),
not a count from the file. It is presented as a hypothesis to confirm.

Rules: first person, plain words, no em dashes, only supported claims.
The dataset is synthetic and every page says so.

Image names (in /images/):
  ERPatient_1   the report page (clean crop or export)
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
         'aria-label="Architecture: CSV, Power Query, two patient tables, a date table, a measures table, a field parameter and the report">'
         '<defs><marker id="dgA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
         'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="dg-head"/></marker></defs>']
    # tables and sources
    s.append(_box(6, 30, 195, 84, "Hospital ER - Copy.csv", ["9,216 rows, 11 columns"]))
    s.append(_box(226, 30, 180, 84, "Power Query (M)", ["types, Moment, Full_Name"]))
    s.append(_box(450, 20, 210, 100, "Patients Dataset", ["Main reporting table", "+ 3 calculated columns"], "dg-model"))
    s.append(_box(710, 20, 200, 100, "Date", ["Calculated, CALENDARAUTO", "Year, Month, Weektype"], "dg-model"))
    s.append(_box(450, 190, 210, 92, "Hospital ER - Copy", ["Second imported table", "same columns"], "dg-model"))
    s.append(_box(710, 190, 200, 92, "LocalDateTable", ["Auto date/time table"], "dg-model"))
    s.append(_box(226, 350, 180, 84, "Parameter", ["Field parameter", "switches the heatmap"], "dg-measure"))
    s.append(_box(450, 350, 210, 84, "Calculation", ["Measures table", "reads Patients Dataset"], "dg-measure"))
    s.append(_box(710, 350, 200, 84, "Report", ["1 page, 1280 x 720"]))
    # connectors
    line = lambda d, extra="": s.append(f'<path class="dg-line {extra}" d="{d}" marker-end="url(#dgA)"/>')
    line("M201,72 L226,72")
    line("M406,72 L450,72")
    line("M316,114 L316,236 L450,236", "dg-dash")
    line("M660,70 L710,70")
    line("M660,236 L710,236")
    line("M406,392 L450,392")
    line("M660,392 L710,392")
    s.append('<path class="dg-line" d="M555,120 L555,190" marker-start="url(#dgA)" marker-end="url(#dgA)"/>')
    # connector labels
    lbl = lambda x, y, t, a="middle": s.append(f'<text class="dg-l" x="{x}" y="{y}" text-anchor="{a}">{t}</text>')
    lbl(685, 60, "date")
    lbl(685, 226, "date")
    lbl(326, 176, "second import", "start")
    lbl(567, 150, "patient_id", "start")
    lbl(567, 164, "both directions", "start")
    # legend
    s.append('<rect class="dg-box dg-model" x="8" y="458" width="14" height="14" rx="3"/>')
    lbl(30, 469, "Model table", "start")
    s.append('<rect class="dg-box dg-measure" x="130" y="458" width="14" height="14" rx="3"/>')
    lbl(152, 469, "Measures and parameter", "start")
    s.append("</svg>")
    return "".join(s)


ARCH_SVG = _arch_svg()


# ---------------------------------------------------------------- business
BUSINESS = {
    "title": "ER Patient Analysis: what the report shows",
    "lede": "A one-page Power BI report on emergency room visits: volume, waiting time, satisfaction, referrals and who comes in. This page covers what it shows, what to be careful with, and what I would fix next.",
    "sections": [
        {"id": "problem", "heading": "The problem", "blocks": [
            {"type": "note", "text": "This project uses a synthetic demonstration dataset. Nothing here describes a real hospital, and none of it should be used for real patient-care decisions."},
            {"type": "p", "items": [
                "Emergency departments keep an eye on patient volume, waiting time, patient experience, referrals and admin processes. Those usually sit in separate reports, so it is hard to see how they move together across dates, weekdays and weekends, age groups, gender and referral destinations.",
                "I built a one-page Power BI report that puts them in a single view. It is a monitoring and exploration tool. It helps you ask the first questions. It does not explain why anything happens.",
            ]},
        ]},
        {"id": "answer", "heading": "The short answer", "blocks": [
            {"type": "verdict", "text": "This is a monitoring report, not an investigation with a verdict. The most useful things it taught me were about the data itself: most visits have no satisfaction rating, the ages look randomly generated, and the monthly trend is shaped partly by which months the data covers."},
        ]},
        {"id": "numbers", "heading": "Numbers at a glance", "blocks": [
            {"type": "stat_grid", "items": [
                ("9,216", "ER visit records"),
                ("35.26", "Average wait time (unit not documented)"),
                ("5.47", "Average satisfaction, rated visits only"),
                ("75.10%", "Visits with no satisfaction rating"),
                ("58.59%", "Visits where the referral is None"),
                ("50.04%", "Visits with the administrative flag set"),
            ]},
            {"type": "p", "text": "These are the numbers as the report displays them. Where they differ from a direct count of the source file, the findings below say so."},
        ]},
        {"id": "meaning", "heading": "What each number means", "blocks": [
            {"type": "table", "headers": ["Number", "How it is worked out", "How to read it"], "rows": [
                ["Total visits", "Count of rows in the main patient table", "Treated as visits because every patient_id is unique in the file. A real source should confirm whether an ID means a visit or a person."],
                ["Average satisfaction", "Average of the satisfaction scores that are not blank", "Covers only visits that have a score. Always read it with the not-rated share."],
                ["Not rated %", "Visits with a blank score, divided by all visits", "A data completeness measure, not a satisfaction result."],
                ["Average wait time", "Average of the wait time field", "The unit is not stated in the file. Confirm it before calling this minutes."],
                ["Administrative %", "Visits where the admin flag is TRUE, divided by all visits", "Do not read it as appointment adherence until someone defines the flag."],
                ["Referred and unreferred %", "Visits where the referral is not, or is, the text none", "Check with the data owner what None means."],
                ["Gender mix", "Share of the codes M, F and NC", "Shown as coded in the source. NC is displayed as Unknown."],
                ["Monthly and yearly visits", "Visit count by the date table's year and month", "The data covers part of 2019 and part of 2020."],
            ]},
        ]},
        {"id": "findings", "heading": "What I found", "blocks": [
            {"type": "findings", "items": [
                {
                    "id": "f-satisfaction",
                    "title": "Most visits have no satisfaction rating",
                    "question": "How far can I trust the satisfaction average?",
                    "paragraphs": [
                        "The report shows 75.10% of visits as not rated. The 5.47 average therefore describes only about a quarter of visits.",
                        "A direct count of the source file gives different figures: 72.7% blank and an average of 4.99 on the scores present. One explanation fits both gaps. If some visits carry a score of 0, DAX drops them from the average and counts them as not rated, because a comparison to BLANK() is also true for 0. About 222 zero scores would explain both numbers. Counting the zeros in the file is the first thing to check.",
                    ],
                    "meaning": "Either way, the average describes a minority of visits. It should not appear without the share of visits that were not rated next to it.",
                    "conclusion": "Show the response rate beside the average, and settle what a score of 0 means.",
                },
                {
                    "id": "f-referral",
                    "title": "Most visits show no referral",
                    "question": "Where do patients get referred?",
                    "paragraphs": [
                        "The report shows None as the referral for 5,400 of 9,216 visits (58.59%). The other 3,816 visits (41.41%) have a referral department.",
                    ],
                    "table": {"headers": ["Referral", "Visits"], "rows": [
                        ["None", "5,400"], ["General Practice", "1,840"], ["Orthopedics", "995"],
                        ["Physiotherapy", "276"], ["Cardiology", "248"], ["Neurology", "193"],
                        ["Gastroenterology", "178"], ["Renal", "86"],
                    ]},
                    "meaning": "General Practice and Orthopedics make up about 74% of the referrals that do exist. None is a real value in the data. Whether it means no referral was needed or nothing was recorded is a question for the data owner. A direct profile of the file read those same 5,400 rows as blank, so it is also worth checking whether None is literal text in the CSV.",
                    "conclusion": "Confirm what None means before calling 58.59% unreferred.",
                },
                {
                    "id": "f-age",
                    "title": "The ages look randomly generated",
                    "question": "Who comes to this ER?",
                    "paragraphs": [
                        "Adults account for 7,106 of the 9,216 visits (77%). That sounds like a finding, but the Adult group covers ages 19 to 79 while Infancy covers only ages 1 and 2, so the bars are not comparable.",
                        "Divide each group by the number of years of age it covers and the picture changes.",
                    ],
                    "table": {"headers": ["Age group", "Ages covered", "Visits", "Visits per year of age"], "rows": [
                        ["Infancy", "1 to 2", "226", "113"],
                        ["Early Childhood", "3 to 6", "468", "117"],
                        ["Middle Childhood", "7 to 12", "719", "120"],
                        ["Teenager", "13 to 18", "697", "116"],
                        ["Adult", "19 to 79", "7,106", "116"],
                    ]},
                    "meaning": "Every group gets about 113 to 120 visits per year of age. Real ER data is usually not that flat, because very young children and older adults tend to stand out. This looks like randomly generated ages, which fits a synthetic dataset.",
                    "conclusion": "Compare age groups per year of age, not by bar height. Done that way, there is no age effect at all.",
                },
                {
                    "id": "f-weektype",
                    "title": "Weekdays and weekends look the same per day",
                    "question": "Is the ER busier on weekdays?",
                    "paragraphs": [
                        "The report shows about 6.6K visits on weekdays and 2.6K on weekends, which looks like a big gap.",
                        "Weekdays are five days and weekends are two. 6.6K over five days is about 1.3K a day, and 2.6K over two days is also about 1.3K a day.",
                    ],
                    "meaning": "The totals compare unequal numbers of days, so they suggest a pattern that is not there. It is another sign of evenly spread, generated dates. These figures come from the chart's rounded labels, so treat the per-day numbers as approximate.",
                    "conclusion": "Compare day types per day, not in total.",
                },
                {
                    "id": "f-monthly",
                    "title": "The monthly line mostly reflects which months are in the data",
                    "question": "Is there a seasonal pattern?",
                    "paragraphs": [
                        "The monthly chart peaks at 1,024 visits in August and bottoms out at 431 in February. It rises steeply between February and April and drops after October.",
                        "The data runs from 1 April 2019 to 30 October 2020. April to October appear in both years. January to March appear only in 2020, and November and December only in 2019. Months covered twice naturally add up to more visits.",
                    ],
                    "meaning": "So most of that shape is coverage, not seasonality. The yearly totals have the same problem: 2019 has 4,338 visits and 2020 has 4,878, and both are partial years, so the gap is not a full-year comparison.",
                    "conclusion": "Compare like with like: use year and month together, or only the months both years cover.",
                },
                {
                    "id": "f-admin",
                    "title": "The administrative flag splits almost evenly",
                    "question": "What share of visits carry the administrative flag?",
                    "paragraphs": [
                        "4,612 visits are flagged TRUE (50.04%) and 4,604 are FALSE (49.96%). Together they add up to all 9,216 visits, so no visit has a missing flag.",
                    ],
                    "meaning": "Nobody has written down what the flag means, so I cannot say whether it relates to scheduled or unscheduled care.",
                    "conclusion": "Define the flag before reporting it as administrative appointments.",
                },
            ]},
        ]},
        {"id": "reading", "heading": "How to read the report", "blocks": [
            {"type": "figure", "spec": ("ERPatient_1", "The report page: KPI cards, referral and age charts, yearly and monthly trends, gender panel and the satisfaction and wait time heatmap.")},
            {"type": "table", "headers": ["Report area", "Question it supports", "Reading guidance"], "rows": [
                ["KPI cards", "How many visits, and what are the average wait and satisfaction?", "Check the current filters, and note how many visits are not rated."],
                ["Administrative split", "What share of visits carry each flag?", "A flag distribution until the flag is defined."],
                ["Weekday and weekend chart", "How does volume differ by day type?", "Saturday and Sunday count as weekend. Totals are not adjusted for the number of days."],
                ["Age group chart", "Which age groups account for the most visits?", "Groups cover very different age spans. Compare per year of age."],
                ["Year and month trends", "How does volume change over time?", "Both years are partial. Months are combined across years."],
                ["Referral bar chart", "Which referral categories appear most often?", "The largest bar is None, at 5,400 visits."],
                ["Demographic heatmap", "How do satisfaction or wait time vary by race and age?", "A field parameter switches the metric. Cell colour is relative, and a dark cell is not proof of cause."],
                ["Gender breakdown", "What share of visits fall into M, F and NC?", "Coded values in the source."],
            ]},
        ]},
        {"id": "recommendations", "heading": "What I would do next", "blocks": [
            {"type": "recs", "items": [
                {"priority": "High", "title": "Confirm what None means for referrals",
                 "evidence": "The report shows 58.59% of visits with a referral of None, and a direct file profile read those rows as blank.",
                 "action": "Ask the data owner what None means, write it in the data dictionary, and show Not recorded separately if blanks and None ever appear together.",
                 "impact": "Stops 58.59% being read as unreferred when it might mean something else."},
                {"priority": "High", "title": "Reconcile the satisfaction numbers and show the response rate",
                 "evidence": "The report shows 5.47 and 75.10% not rated. A direct count gives 4.99 and 72.7% blank.",
                 "action": "Count the zero scores in the file, decide whether 0 is a real rating, and put the response rate on the report next to the average.",
                 "impact": "The average becomes honest about the quarter of visits it describes."},
                {"priority": "High", "title": "Confirm the wait time unit",
                 "evidence": "The average is 35.26 on a range of 10 to 60, with no unit stated.",
                 "action": "Ask the data owner and label the card.",
                 "impact": "The KPI becomes something a manager can act on."},
                {"priority": "Medium", "title": "Clarify whether patient_id is a visit or a person",
                 "evidence": "There are 9,216 unique IDs in 9,216 rows.",
                 "action": "Confirm the grain, and rename the measure Total Visits if each row is a visit.",
                 "impact": "Avoids reporting a row count as a patient count if repeat visits exist."},
                {"priority": "Medium", "title": "Fix the date handling and month sorting",
                 "evidence": "Month-only summaries mix the same month across years, and the data covers partial years.",
                 "action": "Mark the Date table, switch off the automatic date tables, and use a year and month field.",
                 "impact": "Time comparisons stop being shaped by coverage."},
                {"priority": "Medium", "title": "Simplify the model to one patient table",
                 "evidence": "Two similarly shaped patient tables are joined by patient_id with filtering in both directions, and the reason is not documented.",
                 "action": "Confirm what the second table is for, and remove it if there is no reason.",
                 "impact": "Less duplicated data and fewer ambiguous filters."},
                {"priority": "Medium", "title": "Add definitions, visible filters and clear labels",
                 "evidence": "The report carries no metric definitions, and gender is shown as coded values.",
                 "action": "Add a short definitions panel, show which filters are active, and label coded values in plain words.",
                 "impact": "More trust and easier use for a management audience."},
            ]},
        ]},
        {"id": "limits", "heading": "What this can't tell you", "blocks": [
            {"type": "p", "items": [
                "Every record is synthetic, so no conclusion here describes real hospital performance.",
                "The satisfaction and referral fields have large gaps or unclear values, as covered above.",
                "The meaning of the administrative flag and the unit of the wait time are not specified in the source file.",
                "The data covers part of 2019 and part of 2020, so year and month comparisons are not like for like.",
                "The model contains two similarly shaped patient tables, and the reason for that design is not documented.",
                "The formulas come from the project files, and the figures come from the report screenshot and a profile of the source CSV. Report interactions were not re-run in Power BI Desktop for this write-up, and the refresh schedule, row-level security and published settings were not checked.",
            ]},
        ]},
    ],
}


# --------------------------------------------------------------- technical
TECHNICAL = {
    "title": "ER Patient Analysis: how it was built",
    "lede": "The data model, the Power Query steps, every DAX column and measure with the reasoning behind it, and the problems I found in my own model.",
    "sections": [
        {"id": "solution", "heading": "The solution", "blocks": [
            {"type": "note", "text": "Synthetic demonstration data. The formulas and metadata on this page come from the Power BI project files. Code is copied as stored and only re-indented. My local folder path in the M query is shortened."},
            {"type": "p", "text": "The solution is a Power BI Project (PBIP) with a report definition and a semantic model in Import mode. M expressions read the CSV, a Date table is calculated in DAX, and a dedicated Calculation table holds the measures. A Parameter table defines a field parameter that switches the heatmap between Average Satisfaction Score and Average wait Time."},
            {"type": "svg", "svg": ARCH_SVG, "caption": "How the pieces connect. The patient_id relationship runs between the two patient tables, and the Calculation table is not joined to anything, it only holds measures."},
            {"type": "table", "headers": ["Component", "Where it lives", "Role"], "rows": [
                ["Power BI Project (PBIP)", "PatientsAnalysis - Copy.pbip", "Project based source form of the report and model"],
                ["Report definition", "Report/definition/pages and visuals", "Page layout, visual types, fields and report objects"],
                ["Semantic model", "SemanticModel/definition/*.tmdl", "Tables, columns, measures, partitions and relationships"],
                ["Power Query / M", "Patients Dataset partition", "CSV ingestion and shaping"],
                ["DAX", "Calculated columns, Calculation table, Date table", "Derived categories, KPI calculations and calendar attributes"],
                ["Source data", "Hospital ER - Copy.csv", "A synthetic 11 column dataset"],
            ]},
        ]},
        {"id": "data", "heading": "The data and profiling", "blocks": [
            {"type": "p", "text": "The source file has 9,216 rows and 11 columns, covering 1 April 2019 to 30 October 2020. Every patient_id is unique in this file, but nothing says whether an ID means a person or a visit."},
            {"type": "table", "headers": ["Check", "Result", "What it means"], "rows": [
                ["Row count", "9,216", "The baseline for reconciling everything else. The report's Total Patients card also shows 9,216."],
                ["Column count", "11", "The M source step explicitly expects 11 columns."],
                ["Unique patient_id", "9,216", "Unique in this file. The true grain needs confirming."],
                ["Blank patient_sat_score", "6,699 (72.7%) in a direct count", "The report shows 75.10% not rated. See the note below."],
                ["Blank department_referral", "5,400 (58.6%) in a direct count", "The report shows a None category of exactly 5,400. See the note below."],
                ["Blanks in other columns", "None observed", "Does not remove the need for schema and domain checks."],
                ["Age range", "1 to 79", "The age group formulas cover every observed age."],
                ["Wait time range", "10 to 60", "Unit and sensible limits are not specified."],
            ]},
            {"type": "note", "text": "Two numbers do not match between the direct file profile and the report. Satisfaction: the report says 75.10% not rated and an average of 5.47, the profile says 72.7% blank and 4.99. Referral: the profile counted 5,400 blanks, while the report shows 5,400 rows with the value None. The satisfaction gap fits about 222 scores of exactly 0, which DAX drops. The referral gap fits None being literal text in the file that the profiling tool read as blank. Both are hypotheses to confirm in the CSV."},
        ]},
        {"id": "dictionary", "heading": "Data dictionary", "blocks": [
            {"type": "table", "headers": ["Column", "Type and role", "Transform and notes"], "rows": [
                ["date", "Date-time in the CSV", "Converted to a date after the time is extracted."],
                ["patient_id", "Text identifier", "Imported as text. Used in the relationship between the patient tables."],
                ["patient_gender", "Text category", "Values M, F and NC."],
                ["patient_age", "Integer", "Used by Age Buckets and Age Group."],
                ["patient_sat_score", "Integer, nullable", "The average measure excludes blank scores. % No Rating counts blanks."],
                ["patient_first_inital", "Text", "Source spelling kept. Combined with the surname."],
                ["patient_last_name", "Text", "Combined with the first initial into Full_Name."],
                ["patient_race", "Text category", "The heatmap row field."],
                ["patient_admin_flag", "Boolean", "Used for the TRUE and FALSE administrative percentages."],
                ["patient_waittime", "Integer", "Used by the average wait measure and the heatmap parameter."],
                ["department_referral", "Text", "Shown in the report with a None category of 5,400 rows and seven departments for the other 3,816."],
                ["Moment", "Derived in M", "The last 8 characters of the date text. The model metadata says it is a time."],
                ["Full_Name", "Derived in M", "First initial and last name joined with a space."],
                ["Age Buckets", "DAX calculated column", "Ten year bands. The last label says 70+ although the logic means 71+."],
                ["Age Group", "DAX calculated column", "Infancy, Early Childhood, Middle Childhood, Teenager, Adult."],
                ["AM_PM", "DAX calculated column", "Uses HOUR(Moment) < 12."],
            ]},
        ]},
        {"id": "powerquery", "heading": "Power Query steps", "blocks": [
            {"type": "p", "text": "The M query for Patients Dataset runs these steps in order. They are documented as built. Improvements are listed after the code."},
            {"type": "table", "headers": ["Step", "What it does", "Why, and what to watch"], "rows": [
                ["Source", "Reads the CSV with Csv.Document, expecting 11 columns, Windows-1252 encoding and QuoteStyle.None", "Reads a local file. The fixed column count makes schema changes fail loudly, which is useful but unplanned."],
                ["Promoted Headers", "Uses the first row as column names", "Needed because the CSV has a header row."],
                ["Changed Type", "Sets date, text, integer and logical types", "Gives every column the type the model expects."],
                ["Inserted Last Characters", "Takes the last 8 characters of the date as text", "An attempt to capture the time of day. It depends on the locale."],
                ["Changed Type1", "Changes date to date only", "Done after the time text is taken out."],
                ["Renamed Columns", "Renames the new column to Moment", "A clearer name."],
                ["Changed Type2", "Keeps Moment as text", "Conflicts with the model, which treats Moment as a time."],
                ["Merged Columns", "Joins first initial and last name into Full_Name", "Only for display. The dashboard KPIs do not use names."],
            ]},
            {"type": "code", "title": "Patients Dataset (source query)", "lang": "m", "code": r'''
let
    Source = Csv.Document(
        File.Contents("C:\...\Hospital ER - Copy.csv"),
        [Delimiter=",", Columns=11, Encoding=1252, QuoteStyle=QuoteStyle.None]
    ),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers", {
        {"date", type datetime}, {"patient_id", type text}, {"patient_gender", type text},
        {"patient_age", Int64.Type}, {"patient_sat_score", Int64.Type},
        {"patient_first_inital", type text}, {"patient_last_name", type text},
        {"patient_race", type text}, {"patient_admin_flag", type logical},
        {"patient_waittime", Int64.Type}, {"department_referral", type text}
    }),
    #"Inserted Last Characters" = Table.AddColumn(
        #"Changed Type", "Last Characters",
        each Text.End(Text.From([date], "en-GB"), 8), type text
    ),
    #"Changed Type1" = Table.TransformColumnTypes(#"Inserted Last Characters", {{"date", type date}}),
    #"Renamed Columns" = Table.RenameColumns(#"Changed Type1", {{"Last Characters", "Moment"}}),
    #"Changed Type2" = Table.TransformColumnTypes(#"Renamed Columns", {{"Moment", type text}}),
    #"Merged Columns" = Table.CombineColumns(
        #"Changed Type2", {"patient_first_inital", "patient_last_name"},
        Combiner.CombineTextByDelimiter(" ", QuoteStyle.None), "Full_Name"
    )
in
    #"Merged Columns"
'''},
            {"type": "sub", "text": "What I would change"},
            {"type": "pairs", "items": [
                ("Hard coded file path", "The query points at a folder on my machine. Replace it with a parameter or a governed location before handover."),
                ("Time from text", "Taking the last 8 characters of a date as text depends on the locale and breaks easily. Time.From([date]) gives a typed time first."),
                ("Moment type", "The query makes Moment text while the model treats it as a time. Pick one type and test the AM_PM column against it."),
                ("Quote style", "QuoteStyle.None can mishandle values with quoted commas. Use the quote style the CSV actually follows."),
                ("Fixed column count", "Columns=11 hides schema changes. Add an explicit schema check with a clear failure."),
                ("Full_Name", "Built for display, but no KPI needs it. Remove it from the model if the report never shows names."),
                ("Misspelt field", "patient_first_inital is spelt wrongly in the source. Keep it for lineage, but rename it in a cleaned layer."),
            ]},
        ]},
        {"id": "model", "heading": "Data model and relationships", "blocks": [
            {"type": "table", "headers": ["Relationship", "How it is stored", "Review"], "rows": [
                ["Patients Dataset[patient_id] to Hospital ER - Copy[patient_id]", "Patients Dataset is the one side. Filtering runs in both directions.", "The two tables have almost identical fields. Find out why a second table exists. Two way filtering adds ambiguity."],
                ["Patients Dataset[date] to Date[Date]", "A relationship exists. Cardinality is not shown in the stored snippet.", "Confirm it is active and one to many, and mark Date as the date table."],
                ["Hospital ER - Copy[date] to LocalDateTable[Date]", "Links to an auto generated date table.", "Probably redundant next to the Date table. Review the automatic date setting so two date paths do not compete."],
            ]},
            {"type": "p", "text": "The relationships confirm two patient tables and a separate Date table. The intended star schema is not fully there, because the second patient table is joined by patient_id with filtering in both directions. For this dataset the better target is one visit level fact table, related one to many from a Date dimension, with measures in their own table."},
            {"type": "sub", "text": "Date table"},
            {"type": "code", "title": "Date (calculated table)", "lang": "dax", "code": r'''
ADDCOLUMNS(
    CALENDARAUTO(),
    "Year", YEAR([Date]),
    "Month", FORMAT([Date], "mmm"),
    "Weektype", if (WEEKDAY([Date]) = 1, "Weekend", IF(WEEKDAY([Date]) = 7, "Weekend", "Weekday")),
    "Weekday", FORMAT([Date], "ddd"),
    "MonthNum", MONTH([Date])
)
'''},
            {"type": "p", "text": "CALENDARAUTO() builds the calendar from the date columns in the model, then I add year, short month, weektype, short weekday and a month number. Month is sorted by that number. Sunday and Saturday are labelled Weekend. Because CALENDARAUTO() can stretch the calendar based on other date columns, the real date range should be checked, and the table marked as a date table in Power BI."},
        ]},
        {"id": "columns", "heading": "Calculated columns", "blocks": [
            {"type": "code_cards", "items": [
                {"name": "Age Buckets", "kind": "Calculated column", "lang": "dax",
                 "text": ["Technique: SWITCH(TRUE()) checks the conditions in order and returns the label for the first one that is true. That gives bands of 0 to 10, 11 to 20, and so on up to 61 to 70, then a catch-all."],
                 "code": r'''
SWITCH(
    TRUE(),
    'Patients Dataset'[patient_age] <= 10, "0-10",
    'Patients Dataset'[patient_age] <= 20, "11-20",
    'Patients Dataset'[patient_age] <= 30, "21-30",
    'Patients Dataset'[patient_age] <= 40, "31-40",
    'Patients Dataset'[patient_age] <= 50, "41-50",
    'Patients Dataset'[patient_age] <= 60, "51-60",
    'Patients Dataset'[patient_age] <= 70, "61-70",
    "70+"
)
''',
                 "note": "Ages 71 and above reach the last branch, so the label should say 71+, not 70+. A negative age would also land in the first band, so the age range should be checked if this is reused on new data."},
                {"name": "Age Group", "kind": "Calculated column", "lang": "dax",
                 "text": ["Technique: a variable holds the row's age, then nested IFs assign a life stage. Boundaries are inclusive: 2 or under is Infancy, up to 6 Early Childhood, up to 12 Middle Childhood, up to 18 Teenager, and anything higher is Adult."],
                 "code": r'''
var _patientAge = 'Patients Dataset'[patient_age]
return
IF(
    _patientAge <= 2, "Infancy",
    IF(_patientAge <= 6, "Early Childhood",
        IF(_patientAge <= 12, "Middle Childhood",
            IF(_patientAge <= 18, "Teenager",
                "Adult"
            )
        )
    )
)
''',
                 "note": "These are my own groupings, not a clinical or standard life stage list. A SWITCH(TRUE()) would be easier to maintain as the categories grow. Adult covers 61 years of age, which is why the age chart needs reading per year of age."},
                {"name": "AM_PM", "kind": "Calculated column", "lang": "dax",
                 "text": ["Technique: HOUR() pulls the hour out of Moment. Hours before 12 are AM and 12 to 23 are PM."],
                 "code": r'''
IF(HOUR('Patients Dataset'[Moment]) < 12, "AM", "PM")
''',
                 "note": "This is only right if Moment is a real time value. The query creates it as text, so the conversion needs testing. A typed Time.From([date]) in Power Query would be safer."},
            ]},
        ]},
        {"id": "measures", "heading": "DAX measures", "blocks": [
            {"type": "p", "text": "Measures are worked out on the fly in the current filter context. Calculated columns are stored per row at refresh. Each measure below is copied from the model and only re-indented. I have grouped them by job, and the order is mine."},
            {"type": "code_cards", "items": [
                {"name": "Total Patients", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: the base visit count that most other measures divide by.", "Logic: COUNTROWS counts the rows left after filters."],
                 "code": r'''
COUNTROWS('Patients Dataset')
''',
                 "note": "Because patient_id is unique in this file, the row count equals the unique ID count. For production, call it Total Visits unless the business confirms one row per person."},
                {"name": "Average wait Time", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: the mean waiting time.", "Logic: AVERAGE ignores blanks and averages patient_waittime in the current context."],
                 "code": r'''
AVERAGE('Patients Dataset'[patient_waittime])
''',
                 "note": "The report shows 35.26, which matches the source mean of 35.2599, so this one reconciles. The unit is still not specified, so confirm it is minutes before labelling the card."},
                {"name": "Average Satisfaction Score", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: the mean of the satisfaction scores that were recorded.", "Logic: CALCULATE applies a not-blank filter, then AVERAGE takes the mean of what is left."],
                 "code": r'''
CALCULATE(
    AVERAGE('Patients Dataset'[patient_sat_score]),
    'Patients Dataset'[patient_sat_score] <> BLANK()
)
''',
                 "note": "The report shows 5.47, but the mean of the non-blank scores in the file is 4.9921, so this does not reconcile. In DAX, comparing a number to BLANK() is also true for 0, so any scores of 0 would be dropped here. Dropping about 222 zeros would give exactly 5.47. Count the zeros. If a 0 is a real rating, test for blank with ISBLANK() instead."},
                {"name": "% No Rating", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: a completeness indicator for the satisfaction survey.", "Logic: a variable counts the rows whose score equals BLANK(), and DIVIDE returns that over Total Patients."],
                 "code": r'''
VAR _NoRatings =
    CALCULATE(
        [Total Patients],
        'Patients Dataset'[patient_sat_score] = BLANK()
    )
return
DIVIDE(
    _NoRatings,
    [Total Patients]
)
''',
                 "note": "This is a data completeness measure, not a negative rating. The report shows 75.10%, against 72.7% blank in a direct count. The same zero-versus-blank behaviour would explain the difference."},
                {"name": "% Administrative Schedule", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: the share of visits with the administrative flag set.", "Logic: FILTER keeps the visible rows where the flag is TRUE, COUNTROWS counts them, and DIVIDE protects against a zero denominator."],
                 "code": r'''
DIVIDE(
    COUNTROWS(
        FILTER(
            'Patients Dataset',
            'Patients Dataset'[patient_admin_flag] = TRUE())
    ),
    [Total Patients]
)
''',
                 "note": "This assumes TRUE means an administrative appointment. The flag still needs a written definition. The report shows 50.04%, which matches 4,612 of 9,216."},
                {"name": "% None Administrative Schedule", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: the share without the flag.", "Logic: the same pattern, counting rows where the flag is FALSE."],
                 "code": r'''
DIVIDE(
    COUNTROWS(
        FILTER(
            'Patients Dataset',
            'Patients Dataset'[patient_admin_flag] = FALSE())
    ),
    [Total Patients]
)
''',
                 "note": "It only mirrors the TRUE share if every row has a non-blank flag. Here the two counts add up to all 9,216 rows, and the report shows 49.96%."},
                {"name": "% Unreferred Patients", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: the share of visits with no referral.", "Logic: CALCULATE counts rows where department_referral equals the text none, and DIVIDE returns that over Total Patients."],
                 "code": r'''
Var _FilterPatients =
    CALCULATE(
        [Total Patients],
        'Patients Dataset'[department_referral] = "none"
    )
RETURN
DIVIDE(
    _FilterPatients,
    [Total Patients]
)
''',
                 "note": "The report shows 58.59%, which is exactly 5,400 of 9,216, and the bar chart has a None category of 5,400. So the measure works as written. A direct file profile read the same rows as blank, which suggests None is literal text in the CSV. What None means still needs confirming."},
                {"name": "% Referred Patients", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: the share of visits with a referral department.", "Logic: the same pattern, counting rows that are not equal to none."],
                 "code": r'''
Var _FilterPatients =
    CALCULATE(
        [Total Patients],
        'Patients Dataset'[department_referral] <> "none"
    )
RETURN
DIVIDE(
    _FilterPatients,
    [Total Patients]
)
''',
                 "note": "The report shows 41.41%, which matches 3,816 of 9,216. The business definition should separate a real referral destination, a true no-referral, and a missing value."},
                {"name": "% Male Visit", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: the share of visits coded M.", "Logic: CALCULATE narrows Total Patients to gender M, and DIVIDE returns that over all rows in the current context."],
                 "code": r'''
DIVIDE(
    CALCULATE(
        [Total Patients], 'Patients Dataset'[patient_gender] = "M"
    ),
    [Total Patients]
)
''',
                 "note": "The category codes should be written down in a data dictionary."},
                {"name": "% Female Visit", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: the share of visits coded F.", "Logic: the same pattern with gender F."],
                 "code": r'''
DIVIDE(
    CALCULATE(
        [Total Patients], 'Patients Dataset'[patient_gender] = "F"
    ),
    [Total Patients]
)
''',
                 "note": "The category codes should be written down in a data dictionary."},
                {"name": "% Unknown", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: the share of visits coded NC, shown as Unknown on the report.", "Logic: the same pattern with gender NC."],
                 "code": r'''
DIVIDE(
    CALCULATE(
        [Total Patients], 'Patients Dataset'[patient_gender] = "NC"
    ),
    [Total Patients]
)
''',
                 "note": "NC should be explained in the data dictionary, not assumed to mean one particular phrase."},
                {"name": "CF Max Point (Month)", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: a conditional formatting marker for the lowest and highest months.", "Logic: SUMMARIZE builds a month level table, ADDCOLUMNS adds Total Patients, ALLSELECTED keeps the outside selections, and MINX and MAXX find the extremes. SWITCH returns 0 for the minimum and 1 for the maximum."],
                 "code": r'''
VAR _PatientTable =
    CALCULATETABLE(
        ADDCOLUMNS(
            SUMMARIZE('Date', 'Date'[Month]),
            "@Total_Patients", [Total Patients]
        ),
        ALLSELECTED()
    )
VAR _MinValu = MINX(_PatientTable, [@Total_Patients])
VAR _Maxvalu = MAXX(_PatientTable, [@Total_Patients])
VAR _TotalPatients = [Total Patients]
RETURN
SWITCH(
    TRUE(),
    _TotalPatients = _MinValu, 0,
    _TotalPatients = _Maxvalu, 1
)
''',
                 "note": "A month name is not unique across years, so this groups the same month from different years together. That is what shapes the monthly chart. A year and month field or a month start date would fix it. Ties can mark more than one point, and other points return BLANK."},
                {"name": "Values Max Point (Month)", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: the data label shown on the lowest and highest months, which is where 431 and 1,024 come from.", "Logic: the same month summary, returning Total Patients when the current value matches the minimum or maximum."],
                 "code": r'''
VAR _PatientTable =
    CALCULATETABLE(
        ADDCOLUMNS(
            SUMMARIZE('Date', 'Date'[Month]),
            "@Total_Patients", [Total Patients]
        ),
        ALLSELECTED()
    )
VAR _MinValu = MINX(_PatientTable, [@Total_Patients])
VAR _Maxvalu = MAXX(_PatientTable, [@Total_Patients])
VAR _TotalPatients = [Total Patients]
RETURN
SWITCH(
    TRUE(),
    _TotalPatients = _MinValu, [Total Patients],
    _TotalPatients = _Maxvalu, [Total Patients]
)
''',
                 "note": "Returns BLANK for every other month. The same month-across-years caveat applies."},
                {"name": "CF Max Point (Year)", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: the same marker idea for the yearly chart.", "Logic: summarises Total Patients by year, finds the minimum and maximum, and returns 0 or 1."],
                 "code": r'''
VAR _PatientTable =
    CALCULATETABLE(
        ADDCOLUMNS(
            SUMMARIZE('Date', 'Date'[Year]),
            "@Total_Patients", [Total Patients]
        ),
        ALLSELECTED()
    )
VAR _MinValu = MINX(_PatientTable, [@Total_Patients])
VAR _Maxvalu = MAXX(_PatientTable, [@Total_Patients])
VAR _TotalPatients = [Total Patients]
RETURN
SWITCH(
    TRUE(),
    _TotalPatients = _MinValu, 0,
    _TotalPatients = _Maxvalu, 1
)
''',
                 "note": "A tie can mark more than one year. ALLSELECTED depends on the report's slicers and visual filters."},
                {"name": "Values Max Point (Year)", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: the data label on the lowest and highest years, which shows 4,338 and 4,878.", "Logic: returns Total Patients for the years that match the minimum or maximum."],
                 "code": r'''
VAR _PatientTable =
    CALCULATETABLE(
        ADDCOLUMNS(
            SUMMARIZE('Date', 'Date'[Year]),
            "@Total_Patients", [Total Patients]
        ),
        ALLSELECTED()
    )
VAR _MinValu = MINX(_PatientTable, [@Total_Patients])
VAR _Maxvalu = MAXX(_PatientTable, [@Total_Patients])
VAR _TotalPatients = [Total Patients]
RETURN
SWITCH(
    TRUE(),
    _TotalPatients = _MinValu, [Total Patients],
    _TotalPatients = _Maxvalu, [Total Patients]
)
''',
                 "note": "Returns BLANK for every other year."},
                {"name": "HeatMap Caption", "kind": "Measure", "lang": "dax",
                 "text": ["Purpose: a caption that changes with the metric chosen for the heatmap.", "Logic: SELECTEDVALUE reads the parameter order. If it is 0 the satisfaction caption shows, otherwise the wait time caption shows."],
                 "code": r'''
var _selectedMeasure =
    SELECTEDVALUE(Parameter[Parameter Order])
RETURN
IF(_selectedMeasure = 0,
    " Patients are most SATISFIED when the SCALE shows the Darkest GREEN on the Age-Group",
    "The Darkest Green on the scale denotes LOW wait Time on the Age-Group"
)
''',
                 "note": "The second caption also shows when nothing is selected or more than one item is, so the parameter should stay single select."},
            ]},
        ]},
        {"id": "parameter", "heading": "Field parameter and heatmap", "blocks": [
            {"type": "code", "title": "Parameter (field parameter)", "lang": "dax", "code": r'''
{
    ("Avg Satisfaction", NAMEOF('Calculation'[Average Satisfaction Score]), 0),
    ("Avg wait Time", NAMEOF('Calculation'[Average wait Time]), 1)
}
'''},
            {"type": "p", "text": "The Parameter table holds two selectable metrics. Order 0 points at Average Satisfaction Score and order 1 at Average wait Time. The heatmap reads whichever is chosen, and the HeatMap Caption measure reads the order to show the matching explanation. A field parameter lets one visual show different measures without building the visual twice."},
        ]},
        {"id": "report", "heading": "The report page", "blocks": [
            {"type": "p", "text": "The report has one page, FitToPage at 1280 by 720. The visual files show cards, clustered bar and column charts, a line chart, an area chart, a pivot style heatmap, a slicer, a text box and one custom visual."},
            {"type": "figure", "spec": ("ERPatient_1", "The report page.")},
            {"type": "table", "headers": ["Visual group", "Fields and measures", "Purpose"], "rows": [
                ["KPI cards", "Total Patients, Average Satisfaction Score, % No Rating, Average wait Time", "Headline summary"],
                ["Administrative split", "% Administrative Schedule, % None Administrative Schedule", "Split of the boolean flag"],
                ["Referral bar chart", "department_referral by row count", "Referral categories, including None"],
                ["Age group bar chart", "Age Group and Total Patients", "Visits across life stage bands"],
                ["Weekday and weekend chart", "Date[Weektype] and Total Patients", "Volume by day type"],
                ["Yearly trend", "Date[Year], Total Patients, the year marker measures", "Yearly counts with the extremes marked"],
                ["Monthly trend", "Date[Month], Total Patients, the month marker measures", "The monthly shape. Combines years."],
                ["Gender panel", "% Male Visit, % Female Visit, % Unknown", "Share by gender code"],
                ["Heatmap", "patient_race by Age Buckets, with the selectable metric", "Compares the chosen metric across groups"],
                ["AM and PM selector", "AM_PM", "Probably filters time of day. Interaction settings need checking in Desktop."],
            ]},
        ]},
        {"id": "validation", "heading": "Validation plan", "blocks": [
            {"type": "p", "text": "I wrote the checks first and then compared them with the report screenshot. Some now reconcile, and two do not."},
            {"type": "table", "headers": ["Test", "Check", "Expected", "Status"], "rows": [
                ["DQ-01", "Source row count", "9,216 rows reconcile to the model", "Reconciles. The report card shows 9,216."],
                ["DQ-02", "Identifier uniqueness", "patient_id matches the agreed grain", "9,216 unique IDs. The business grain still needs confirming."],
                ["DQ-03", "Satisfaction completeness", "Blank and rated counts add up", "Direct count: 6,699 blank, 2,517 rated. The report shows 75.10% not rated, so it does not match yet."],
                ["DQ-04", "Referral completeness", "Blank, none and destinations profiled separately", "Profile: 5,400 blank, 3,816 filled. The report shows None for the same 5,400 rows, so the file may hold literal None text."],
                ["DQ-05", "Average satisfaction", "DAX equals the source mean of the non-blank scores", "Source mean 4.9921. The report shows 5.47. Does not reconcile. Zero scores are the leading suspect."],
                ["DQ-06", "Average wait", "DAX equals the source average", "Source mean 35.2599. The report shows 35.26. Reconciles. Unit still to confirm."],
                ["DQ-07", "Administrative split", "TRUE plus FALSE equals the total", "4,612 + 4,604 = 9,216. The report shows 50.04% and 49.96%. Reconciles."],
                ["DQ-08", "Age bucket edges", "Test 0, 10, 11, 70, 71 and the maximum age", "The last label should be 71+, not 70+."],
                ["DQ-09", "AM and PM boundary", "Test 00:00, 11:59, 12:00 and 23:59", "Needs a typed time check in Desktop."],
                ["DQ-10", "Date relationships", "Active relationships filter every visual as expected", "Model inspection only. Runtime not verified."],
                ["DQ-11", "Referral measures", "Blanks, none and real destinations checked separately", "The measures work as written, since 58.59% matches 5,400 of 9,216. The meaning of None is still to confirm."],
                ["DQ-12", "Extreme point measures", "Test ties, one period, multi year months and slicers", "Open. The monthly shape matches the date coverage, which points the same way."],
            ]},
        ]},
        {"id": "issues", "heading": "Known issues and what I would fix", "blocks": [
            {"type": "table", "headers": ["Severity", "What I found", "What I would do"], "rows": [
                ["High", "The report does not reconcile to the source for satisfaction. It shows 5.47 and 75.10%, the file gives 4.99 and 72.7%. Scores of 0 are the likely cause, because DAX treats 0 as BLANK() in comparisons.", "Count the zero scores. If a 0 is a real rating, test with ISBLANK(). If it means not rated, write that in the data dictionary."],
                ["High", "Two similarly shaped patient tables joined by patient_id, with filtering in both directions.", "Confirm the purpose, and prefer one fact table unless there is a documented reason."],
                ["High", "Satisfaction is missing for most visits.", "Show completeness prominently and never present the average as describing all visits."],
                ["High", "An absolute local file path in Power Query.", "Use a parameter, and document the refresh credentials and environment."],
                ["Medium", "The meaning of None in the referral field is unconfirmed. The measures work as written, but a file profile read those rows as blank.", "Check the CSV for literal None text, and document the meaning."],
                ["Medium", "Moment is taken from locale dependent text, while the model says it is a time.", "Use a typed Time.From transformation and check the result."],
                ["Medium", "The Age Buckets last label says 70+ but means 71+.", "Change the label or the conditions."],
                ["Medium", "Month only summaries combine the same month across years.", "Use a year and month field or a month start date."],
                ["Medium", "The Date table uses CALENDARAUTO, and the model also has an automatic date table.", "Turn off the automatic tables, mark the explicit Date table and check the relationships."],
                ["Medium", "Names with spaces, abbreviations and a source typo.", "Keep lineage but use consistent names, with descriptions and display folders."],
                ["Low", "Unused tables such as Table and a blank Calculation.Column1.", "Remove them after checking dependencies."],
            ]},
        ]},
        {"id": "maintainability", "heading": "Deployment and upkeep", "blocks": [
            {"type": "steps", "items": [
                ("Stable source", "Move the files somewhere governed and replace the hard coded local path."),
                ("Document the setup", "Record the Power BI Desktop version, source credentials, refresh steps and who owns it."),
                ("Version control", "Keep the PBIP in source control with meaningful commits, so report and model changes can be reviewed."),
                ("Own the KPIs", "Write down each measure's definition and who owns it in the business."),
                ("Refresh checklist", "Check row counts, missing values, schema changes and KPI reconciliation after every refresh."),
                ("Before publishing", "Check workspace permissions, sensitivity labels, row-level security and export settings. None of these were verified."),
                ("Clean exports", "Use a clean export of the report page, not a Desktop screenshot, in anything public."),
            ]},
        ]},
        {"id": "reflection", "heading": "What this project shows", "blocks": [
            {"type": "p", "items": [
                "This project is an end to end Power BI workflow. I took a synthetic ER visit dataset, profiled how complete it was, shaped it in Power Query, wrote reusable DAX measures, built age and time categories and a date table, and designed a one page report for exploring the data.",
                "It is also a record of what went wrong. Satisfaction and referral values are mostly missing or unclear, the model has a duplicate table, the time conversion is shaky, the KPI definitions are loose, and two of the report's numbers do not match the source. I would rather show those problems and what I would do about them than hide them.",
            ]},
        ]},
    ],
}
