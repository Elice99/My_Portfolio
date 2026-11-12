"""
GlowMart documentation content. Source: Elice's GlowMart README on GitHub.
Two pages are generated from this file: a business-insights page and a
technical-documentation page. Every number below comes from that README.

Writing rules for this file (so future edits stay consistent):
- First person, plain language, short sentences.
- No em dashes. No bullet lists inside body copy.
- Only state things the README actually supports.

One deliberate difference from the README: it says Abuja was the ONLY
city to decline in 2024, but its own city table also shows Kano at -2.9%.
The table has specific numbers, so these pages follow the table. Check
the workbook and edit here if the table is the part that's wrong.

Image names used (put these files in /images/):
  GlowMart_1  Executive overview page
  GlowMart_2  Brand and city deep dive page
  GlowMart_3  Customer and efficiency page
  GlowMart_Model, GlowMart_Table_Sales, GlowMart_Table_Customer,
  GlowMart_Table_Product, GlowMart_Table_Date
"""

BUSINESS = {
    "title": "GlowMart: what the data said",
    "lede": "GlowMart's Sales and Inventory managers disagreed about stock. The Managing Director asked me to settle it with evidence, not opinions. This page covers what I found and what I would do next.",
    "note": "GlowMart Nigeria Ltd is a realistic business scenario from the SkillAhead Data Analytics Challenge. The figures here come from that challenge dataset, not from a real company's accounts.",

    "scenario": {
        "heading": "The disagreement",
        "paragraphs": [
            "GlowMart Nigeria Ltd is a nationwide FMCG retailer selling across five cities: Abuja, Ibadan, Kano, Lagos and Port Harcourt.",
            "Emeka, the Sales Manager, believed Port Harcourt and Kano sold strongly because demand was higher than the stock they received. He wanted more inventory sent there.",
            "Tunde, the Inventory Manager, said stock was already shared equally across the five cities. In his view the gap came from customer demand, not from allocation.",
            "The Managing Director could not tell who was right, so three questions came to me. Is stock shared fairly? What is really driving revenue? What should management do next?",
        ],
    },

    "verdict": {
        "label": "The short answer",
        "text": "Stock was never the problem. Revenue share and customer share matched in every city, with the biggest gap about 0.3%. The real issues were flat growth, discounts that did not lift order value, and two cities that shrank in 2024, Abuja most of all.",
    },

    "kpis": [
        ("₦652.6M", "Total revenue, 2022 to 2024"),
        ("₦180.4M", "Gross profit"),
        ("27.6%", "Gross profit margin"),
        ("15,000", "Transactions"),
        ("500", "Customers"),
        ("₦72.4M", "Discounts given (11.1% of revenue)"),
    ],

    "findings": [
        {
            "id": "f-stock",
            "title": "Stock was shared fairly",
            "question": "Are some cities getting less stock than they should?",
            "table": {
                "headers": ["City", "Revenue share", "Customer share", "Gap (points)"],
                "rows": [
                    ["Abuja", "20.5%", "20.2%", "0.3"],
                    ["Ibadan", "19.2%", "19.2%", "0.0"],
                    ["Kano", "20.2%", "20.4%", "0.2"],
                    ["Lagos", "18.5%", "18.6%", "0.1"],
                    ["Port Harcourt", "21.6%", "21.6%", "0.0"],
                ],
            },
            "meaning": "Emeka's worry would show up as a gap between a city's share of revenue and its share of customers. There is no gap. Port Harcourt holds 21.6% of revenue and 21.6% of customers. Kano holds 20.2% and 20.4%. The largest difference anywhere is about 0.3 points.",
            "conclusion": "Leave stock allocation as it is. Put the attention on growth.",
        },
        {
            "id": "f-growth",
            "title": "Growth has stalled",
            "question": "Is the business actually growing?",
            "table": {
                "headers": ["Year", "Revenue", "Change on previous year"],
                "rows": [
                    ["2022", "₦217.1M", "n/a"],
                    ["2023", "₦216.0M", "-0.5%"],
                    ["2024", "₦219.5M", "+1.6%"],
                ],
            },
            "meaning": "The brief set a growth target of 5% a year. GlowMart missed it both years. Customers keep buying and the transaction count is high, but revenue is flat.",
            "conclusion": "The main challenge is sustainable growth, not stock.",
            "figure": ("GlowMart_1", "Executive overview page: revenue share against customer share, plus the monthly revenue trend."),
        },
        {
            "id": "f-brands",
            "title": "Brands are not equal",
            "question": "Which brands make money, not just sales?",
            "table": {
                "headers": ["Brand", "Revenue", "Gross margin"],
                "rows": [
                    ["Brand A", "₦200.3M", "31.3%"],
                    ["Brand D", "₦179.7M", "27.6%"],
                    ["Brand C", "₦146.4M", "22.1%"],
                    ["Brand B", "₦126.2M", "28.4%"],
                ],
            },
            "meaning": "Brand A is the strongest on both revenue and margin. Brand C sells well but earns the least from each naira of sales. Brand B has the smallest revenue but a healthy margin, so it looks like a brand that needs more exposure, not a price change.",
            "conclusion": "Each brand needs its own plan. One national approach would hide these differences.",
        },
        {
            "id": "f-cities",
            "title": "Abuja needs attention first",
            "question": "Which cities are growing and which are not?",
            "table": {
                "headers": ["City", "2024 growth"],
                "rows": [
                    ["Ibadan", "+10.6%"],
                    ["Lagos", "+5.0%"],
                    ["Port Harcourt", "+2.7%"],
                    ["Kano", "-2.9%"],
                    ["Abuja", "-5.7%"],
                ],
            },
            "meaning": "Abuja fell the most, and Kano also slipped. Because stock is already shared fairly, the cause is more likely commercial than about supply. The data cannot tell me what the cause is. Competitors, pricing, product range, customer retention and local demand are all worth checking.",
            "conclusion": "Look at Abuja first and keep an eye on Kano.",
            "figure": ("GlowMart_2", "Brand and city deep dive page: brand revenue and margin, the brand by city heatmap, and growth by city."),
        },
        {
            "id": "f-discounts",
            "title": "Discounts cost money and did not lift order value",
            "question": "Are discounts making customers spend more?",
            "paragraphs": [
                "GlowMart gave away about ₦72.4M in discounts, which is 11.1% of revenue. If discounts work, higher discounts should come with bigger orders.",
                "I compared discount rate against average order value across the cities. Cities with slightly higher discounts did not have noticeably larger orders. Average order value across all sales was about ₦43,507.",
            ],
            "meaning": "The business is giving up revenue without getting bigger baskets in return. This is the clearest efficiency problem in the whole project.",
            "conclusion": "Review the discount strategy. Judge each campaign by the return it brings, not by how big the discount is.",
        },
        {
            "id": "f-customers",
            "title": "Customers are spread evenly",
            "question": "Who is the core customer?",
            "paragraphs": [
                "Spending is spread fairly evenly across age groups and between men and women. No single group carries the business.",
            ],
            "meaning": "GlowMart serves a broad customer base instead of depending on one segment.",
            "conclusion": "Keep marketing broad, and add more personal offers for the highest-value groups.",
            "figure": ("GlowMart_3", "Customer and efficiency page: customer demographics, discount effectiveness and recommendations."),
        },
        {
            "id": "f-seasonal",
            "title": "No festive peak",
            "question": "Is there a seasonal pattern?",
            "paragraphs": [
                "Quarterly revenue moves only a little across the three years. There is no regular fourth quarter spike, which retailers in this sector often see.",
            ],
            "meaning": "That may mean festive season chances are being missed.",
            "conclusion": "Plan promotions around the festive period and measure what they add.",
        },
    ],

    "recommendations": [
        {
            "title": "Focus on growth, not stock",
            "evidence": "Revenue share matched customer share within 0.3%, and growth was -0.5% then +1.6% against a 5% target.",
            "action": "Run customer acquisition campaigns, improve the loyalty programme, cross-sell related products, reach new customer groups, and back it with sales-led marketing.",
            "impact": "Raising demand should do more for revenue than moving stock that is already balanced.",
        },
        {
            "title": "Review the discount strategy",
            "evidence": "₦72.4M in discounts with no clear lift in average order value.",
            "action": "Swap blanket discounts for targeted ones: offers by customer group, product bundles, loyalty rewards and time-limited campaigns. Measure every campaign by its return on spend.",
            "impact": "Cutting discounts that do nothing should lift gross profit while keeping customers engaged.",
        },
        {
            "title": "Review Abuja, and watch Kano",
            "evidence": "Abuja fell 5.7% in 2024 and Kano fell 2.9%, while Ibadan grew 10.6%.",
            "action": "Look at local competitors, pricing, product range, customer retention and marketing results in both cities, starting with Abuja.",
            "impact": "Acting early may stop further decline and lift the national total.",
        },
        {
            "title": "Give each brand its own plan",
            "evidence": "Brand A leads on revenue and margin. Brand B has a healthy margin but the least revenue. Brand C sells well but earns the least.",
            "action": "Brand A: more visibility and stock support. Brand B: more marketing exposure. Brand C: review pricing and buying costs.",
            "impact": "Brand level plans should beat one national approach.",
        },
        {
            "title": "Use the dashboard every month",
            "evidence": "The dashboard tracks the same KPIs in every period, so changes are easy to spot.",
            "action": "Put it into the monthly management review instead of treating it as a one-off report.",
            "impact": "Problems show up early, before they turn into operating issues.",
        },
    ],

    "limits": [
        "This covers three years and one dataset of 15,000 transactions and 500 customers. It is a case study, so it should not be read as the accounts of a real company.",
        "I measured gross profit only, which is revenue minus the direct cost of goods. Running costs such as staff, rent and marketing are not part of this analysis.",
        "The discount check compares cities, so it rests on a small number of points. It shows no clear link between discounts and order value. It does not prove that discounts never work.",
        "For Abuja and Kano, I can show that they declined. I cannot show why. The list of possible causes is where to start looking, not a finding.",
    ],
}


TECHNICAL = {
    "title": "GlowMart: how it was built",
    "lede": "The data model, the measures and formulas, the visual choices and the reasons behind each one. I built the whole thing in Microsoft Excel.",

    "stack": {
        "intro": "I used Excel like a BI tool: prepare the data, model it, measure it, visualise it, then report it. Keeping data preparation separate from reporting makes the workbook easier to maintain and extend.",
        "flow": [
            ("Raw data", "15,000 transactions"),
            ("Power Query", "Clean and shape"),
            ("Power Pivot", "Model and relationships"),
            ("PivotTables", "Measures and summaries"),
            ("PivotCharts", "Dashboard design"),
            ("Insights", "Findings and advice"),
        ],
    },

    "dataset": {
        "headers": ["Attribute", "Value"],
        "rows": [
            ["Analysis period", "2022 to 2024"],
            ["Transactions", "15,000"],
            ["Customers", "500"],
            ["Cities", "5"],
            ["Product brands", "4"],
            ["Units sold", "45,226"],
            ["Total revenue", "₦652.6M"],
            ["Gross profit", "₦180.4M"],
            ["Total discount given", "₦72.4M"],
        ],
    },

    "model": {
        "intro": "Instead of one large spreadsheet, I used a small relational model: one fact table in the middle and three lookup tables around it. It is easier to scale, simpler to report from, and it is how BI tools expect data to be organised.",
        "figure": ("GlowMart_Model", "The data model in Power Pivot: Sales in the middle, joined to Customer, Product and Date."),
        "tables": [
            {
                "name": "Sales (fact table)",
                "purpose": "Holds every transaction. All the measures are calculated from this table.",
                "fields": "Sales ID, Customer ID, Product ID, Date, City, Quantity sold, Total sales, Cost of goods sold, Gross profit, Discount",
                "figure": ("GlowMart_Table_Sales", "The Sales table."),
            },
            {
                "name": "Customer",
                "purpose": "Used for customer segmentation and behaviour analysis.",
                "fields": "Customer ID, Gender, Age group, City",
                "figure": ("GlowMart_Table_Customer", "The Customer table."),
            },
            {
                "name": "Product",
                "purpose": "Used for brand level reporting and profitability.",
                "fields": "Product ID, Brand, Category",
                "figure": ("GlowMart_Table_Product", "The Product table."),
            },
            {
                "name": "Date",
                "purpose": "A dedicated calendar table, so time comparisons such as year over year, quarterly and monthly trends work properly.",
                "fields": "Date, plus derived Year, Quarter, Month and Month name",
                "figure": ("GlowMart_Table_Date", "The Date table."),
            },
        ],
    },

    "prep": {
        "intro": "I cleaned and shaped the data in Power Query before any analysis. Doing it first keeps PivotTables, PivotCharts and the dashboard calculations accurate and fast.",
        "steps": [
            ("Review data quality", "Check the raw data for problems before building anything on top of it."),
            ("Correct data types", "Make sure dates are dates and numbers are numbers, so calculations behave."),
            ("Create calculated fields", "Add the fields the analysis needs, such as gross profit."),
            ("Build the calendar table", "Create the Date table and derive Year, Quarter, Month and Month name."),
            ("Prepare lookup relationships", "Set up the keys that connect Sales to Customer, Product and Date."),
            ("Load to the Data Model", "Send the cleaned tables into Power Pivot, ready for reporting."),
        ],
    },

    "approach": {
        "intro": "I did not start by choosing charts. I started with the decision management needed to make.",
        "steps": [
            ("Understand the problem", "Ask what decision management needs to make, not which charts to build."),
            ("Pick the KPIs", "Choose the measures that answer that decision: revenue, profit, growth, customer behaviour and stock fairness."),
            ("Test the assumption", "The Sales Manager said stock was the problem. I compared revenue share with customer share to test it instead of accepting it."),
            ("Look for other explanations", "Once stock was ruled out, I looked at brands, customers, city growth, discounts and trends."),
            ("Turn it into advice", "The final dashboard explains what happened, why, and what management should do next."),
        ],
    },

    "kpis": {
        "intro": "Each KPI is there because it helps answer a specific business question, not just to fill a card.",
        "items": [
            {"name": "Total revenue", "formula": "SUM(Sales[Total_sale])", "result": "₦652.6M",
             "why": "The highest level view of performance and the base for every other money measure."},
            {"name": "Total transactions", "formula": "COUNTA(Sales[SalesID])", "result": "15,000",
             "why": "Revenue alone hides activity. Transactions give context and are needed to work out average order value."},
            {"name": "Total customers", "formula": "DISTINCTCOUNT(Sales[Customer ID])", "result": "500",
             "why": "A customer should count once however often they buy. A distinct count stops repeat purchases from inflating the number."},
            {"name": "Average order value", "formula": "Total revenue ÷ Total transactions", "result": "₦43,506.92",
             "why": "Shows the typical purchase size. It is also the test for discounts: if discounts work, higher discounts should come with higher order values. They did not."},
            {"name": "Total units sold", "formula": "SUM(Sales[Quantity])", "result": "45,226",
             "why": "Separates growth from higher prices and growth from more product actually moving."},
            {"name": "Gross profit", "formula": "Revenue − Cost of goods sold", "result": "₦180.4M",
             "why": "Revenue shows what comes in. Gross profit shows what is left after direct product costs."},
            {"name": "Gross profit margin", "formula": "Gross profit ÷ Revenue", "result": "27.6%",
             "why": "I divide total gross profit by total revenue on purpose. Averaging each transaction's margin would give small sales the same weight as big ones and give a misleading answer. The ratio of totals is the true business margin, and it lets me compare brands, cities and periods fairly."},
            {"name": "Revenue per customer", "formula": "Total revenue ÷ Total customers", "result": "₦1.31M",
             "why": "A high level measure of customer value over the three years, useful for acquisition and retention decisions."},
            {"name": "Transactions per customer", "formula": "Total transactions ÷ Total customers", "result": "30",
             "why": "A business grows by finding more customers or by getting existing ones to buy more often. This measures the second."},
            {"name": "Total discount given", "formula": "SUM(Sales[Discount Amount])", "result": "₦72.4M",
             "why": "Discounts are revenue given away. Tracking the total shows whether the spend is earning enough back."},
            {"name": "Discount rate", "formula": "Total discount ÷ Total revenue", "result": "11.1%",
             "why": "A percentage says more than a naira figure. It shows how much of total sales is being given up through promotions."},
        ],
    },

    "visuals": {
        "intro": "I picked every chart by the question it had to answer. The aim was never attractive charts. It was to show evidence clearly.",
        "items": [
            {"name": "Revenue share vs customer share", "type": "Clustered bar chart",
             "question": "Is stock shared fairly across cities?",
             "why": "Cities differ in size, so raw revenue cannot answer that. Putting revenue share and customer share side by side makes even small gaps easy to see.",
             "insight": "The biggest gap was about 0.3%.",
             "not_chosen": "A pie chart. Small percentage differences are hard to compare in slices."},
            {"name": "Revenue by city", "type": "Horizontal bar chart",
             "question": "Which cities earn the most?",
             "why": "Ranked bars show relative performance at a glance, and horizontal bars keep the city names fully readable.",
             "insight": "Port Harcourt earned the most, but all five cities sit in a narrow range."},
            {"name": "Monthly revenue trend", "type": "Line chart with markers",
             "question": "Is the business growing steadily?",
             "why": "Trends show what single numbers hide. Thirty-six months on one line shows rises, dips and flat stretches, and the markers keep each month readable.",
             "insight": "Revenue stayed roughly flat with small swings."},
            {"name": "Brand revenue and gross margin", "type": "Combo chart",
             "question": "Which brands earn both sales and profit?",
             "why": "A brand can sell a lot and still earn little. Bars for revenue with margin on the same chart show both without needing a second chart.",
             "insight": "Brand A led on both. Brand C sold well but earned the least."},
            {"name": "Brand by city heatmap", "type": "Conditional formatting on a PivotTable",
             "question": "Do preferences differ across cities?",
             "why": "Colour intensity lets you spot patterns faster than reading a grid of numbers. Green marks stronger performance and red marks weaker.",
             "insight": "Brand A did well in every city. No city looked very different, so a standard national stocking approach still fits, with small local changes."},
            {"name": "Quarterly revenue trend", "type": "Line chart",
             "question": "Is there a seasonal pattern?",
             "why": "Quarters smooth out monthly noise but still show more detail than yearly totals.",
             "insight": "There was no regular fourth quarter peak."},
            {"name": "City performance by year", "type": "Clustered column chart",
             "question": "Which cities are improving and which need help?",
             "why": "Grouping the years for each city puts every city's change side by side.",
             "insight": "Ibadan recovered the most in 2024. Abuja fell the most."},
            {"name": "Discount vs average order value", "type": "Scatter plot",
             "question": "Do discounts make customers spend more?",
             "why": "A scatter plot is built for checking whether two numbers move together. If discounts worked, higher discounts would sit alongside higher order values.",
             "insight": "The link was weak."},
            {"name": "Customer demographics", "type": "Donut chart and bar chart",
             "question": "Who is the core customer?",
             "why": "The donut shows each age group's share of revenue. The bar compares male and female revenue. Two small visuals finish the customer story without clutter.",
             "insight": "Spending is spread evenly across groups."},
        ],
    },

    "pages": {
        "intro": "The dashboard has three pages, one for each stage of the decision. An executive should understand the business situation from the first page in under a minute, so the layout follows reading order: business health, the verdict, revenue performance, then supporting detail.",
        "headers": ["Page", "Question it answers", "What is on it"],
        "rows": [
            ["Executive overview", "Is there actually an inventory problem?", "KPI cards, revenue share vs customer share, revenue by city, monthly trend, insight panel"],
            ["Brand and city deep dive", "If stock is not the problem, what is?", "Brand revenue and margin, brand by city heatmap, quarterly trend, city growth by year, insight panel"],
            ["Customer and efficiency", "What should management do next?", "Demographics, gender split, discount effectiveness, discount vs order value, recommendations"],
        ],
    },

    "features": {
        "headers": ["Feature", "What I used it for"],
        "rows": [
            ["Power Query", "Cleaning and preparing the raw data before analysis"],
            ["Power Pivot", "Building the data model and managing relationships between tables"],
            ["PivotTables", "Turning transactions into business-ready summaries"],
            ["PivotCharts", "Dynamic charts connected to the slicers"],
            ["Slicers", "Interactive filtering across the dashboard pages"],
            ["Conditional formatting", "The brand by city heatmap"],
            ["IFERROR()", "Keeping calculation errors off the dashboard"],
            ["SUM(), AVERAGE()", "Totals such as revenue and gross profit, and averages such as order value"],
            ["COUNT / DISTINCT COUNT", "Counting transactions and unique customers"],
            ["Shapes and icons", "KPI cards and navigation panels"],
            ["Custom number formatting", "Showing ₦652.6M instead of a long number"],
            ["Sparklines", "Small revenue trends inside KPI cards"],
        ],
    },

    "principles": [
        ("Simplicity", "Every visual exists to answer a business question. I added nothing just to fill space."),
        ("Consistency", "Colours, type, spacing and formatting stay the same across all three pages, so users spend less effort figuring out each one."),
        ("Executive focus", "The most important information comes first. The KPIs and the verdict sit at the top."),
        ("Interactivity", "Slicers let people filter the dashboards without touching the underlying data model."),
        ("Storytelling", "The pages follow one story: is there a stock problem, if not what is going on, and what should be done. They are not a pile of separate charts."),
    ],

    "challenges": [
        ("Preparing the data", "Raw transactions needed shaping in Power Query before anything useful could be built."),
        ("Choosing KPIs", "It would have been easy to show every metric. I kept only the ones that helped answer the Managing Director's questions."),
        ("Fitting the story into three pages", "I tested every visual against one question: does this help answer the brief? If not, it came out."),
        ("Testing an assumption", "The easy path was to accept that stock was the problem. Checking it with data pointed somewhere else entirely."),
    ],

    "lessons": [
        ("A dashboard should answer questions", "The most useful one helps someone decide with confidence."),
        ("Good analysis challenges assumptions", "The story everyone started with was about stock. The data said otherwise."),
        ("KPIs should support decisions", "Every KPI here earned its place. Metrics with no business value were left out."),
        ("Storytelling is part of analytics", "Without a clear narrative, accurate analysis can still fail to change anything."),
    ],

    "next": [
        "Move the dashboard to Power BI for enterprise reporting.",
        "Connect it to a SQL database so it refreshes automatically.",
        "Build demand forecasting models.",
        "Add inventory optimisation analysis.",
        "Add customer lifetime value.",
        "Forecast sales with Python.",
    ],
}
