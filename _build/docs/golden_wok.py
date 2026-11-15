"""
Golden Wok Delivery Intelligence documentation content, written in
Elisha's voice: he built the report, so the pages say "I did".

Sources: his two project READMEs (business and technical), the DataDNA
September 2026 challenge brief, the dashboard screenshots (copied into
this site as GoldenWok_1..5), the DAX measures as documented in the
technical README, and a direct profile of the CSV files.

Rules: first person, plain words, no em dashes, only claims his saved
outputs support. The dataset is a generated challenge dataset and every
page says so.
"""


# ---------------------------------------------------------------- business
BUSINESS = {
    "title": "Golden Wok Delivery Intelligence: where the delivery network is breaking",
    "lede": "A five-page Power BI report that follows one operational chain: operating conditions, delivery friction, SLA performance, profitability, customer experience, and the corridors that need attention first. This page covers what the report says, how I read each number, and what I would do about it.",
    "sections": [
        {"id": "problem", "heading": "The problem", "blocks": [
            {"type": "note", "text": "I built this for the DataDNA September 2026 dataset challenge. The Golden Wok scenario is fictional and the dataset is generated: 5,000 orders across 4 kitchens, 15 destination zones and 24 active riders, in Lagos, in naira, spanning 2023 to 2024. I say that everywhere on these pages, because the honest reading of any generated dataset is patterns within the data, not claims about a real business."},
            {"type": "p", "items": [
                "A typical delivery dashboard reports what happened: orders, revenue, average delivery time. That is a scorecard, and it answers nothing about what to do next. The challenge brief pushed for more: which routes are under pressure, what does that pressure cost, and which kitchen-to-zone combinations deserve attention first.",
                "So I built the report around an operational chain instead of a chart pile: operating conditions shape delivery friction, friction shows up as SLA performance, SLA lands in the money, and the money and the delays both land on the customer. Each of my five pages owns one link of that chain, so management can move from what happened to where the pressure is.",
                "The report answers one question per page: how healthy is the operation, where is delivery time lost, where are we making or losing money, how healthy is the customer experience, and how does the network itself perform.",
            ]},
        ]},
        {"id": "answer", "heading": "The short answer", "blocks": [
            {"type": "verdict", "text": "The headline is uncomfortable and that is the point. Half of all orders (49.9%) miss their promised delivery window, the average promise gap is -4.97 minutes, and the whole operation runs on a 0.65% profit margin: ₦380.56M of revenue returns just ₦2.49M of profit while delivery cost eats ₦30.50M, about 8% of order value. The pressure is not spread evenly. SLA breach rates sit near 50% in every zone tier and every vehicle group, but they climb to 53.28% in the 6 to 8 km distance band, and one corridor, Ikeja GRA to Alimosho, stands at 64.52% on 62 orders. My reading: this is not a slow-rider problem, it is a promise-calibration and distance-economics problem, and the fix order is promises first, distance economics second, one corridor third. Every number here comes off my own dashboard and my two project READMEs."},
            {"type": "figure", "spec": ("GoldenWok_1", "Page one, the Executive Command Center: the 5K orders, ₦380.56M revenue and ₦2.49M profit cards, the 50.1% SLA health gauge with its 5-minutes-behind-promise note, the monthly revenue and profit trend, and the zone-tier and rider-vehicle breakdowns.")},
        ]},
        {"id": "numbers", "heading": "Numbers at a glance", "blocks": [
            {"type": "stat_grid", "items": [
                ("5,000", "orders, 2023 to 2024"),
                ("₦380.56M", "revenue across the network"),
                ("₦2.49M", "profit, a 0.65% margin"),
                ("49.9%", "SLA breach rate"),
                ("-4.97 min", "average promise gap"),
                ("64.52%", "breach rate on the worst corridor"),
            ]},
            {"type": "p", "text": "Where they come from: the headline KPIs, the corridor and distance figures, and the zone and vehicle breakdowns are all read off my dashboard pages, and the row counts come from a direct profile of the CSV files I loaded into the model."},
        ]},
        {"id": "meaning", "heading": "How to read each number", "blocks": [
            {"type": "table", "headers": ["Number", "How I got it", "How to read it"], "rows": [
                ["49.9% SLA breach rate", "Orders whose actual delivery time exceeded the promise, over all orders", "Half the network misses its promise. My severity breakdown shows the misses are extreme: about 2.2K of the 2.5K breached orders arrived more than 60 minutes late."],
                ["-4.97 minute promise gap", "Average of actual minus promised delivery time, per order", "Deliveries run late on average, but only by five minutes against promises of roughly 505 minutes. The average hides how many orders are severely late."],
                ["0.65% profit margin", "₦2.49M profit over ₦380.56M revenue", "Almost no cushion. An 8% delivery cost against a 0.65% margin means small cost movements flip zones between profit and loss."],
                ["8.01% delivery cost share", "₦30.50M delivery cost over order value", "Delivery is the biggest controllable cost, and it rises sharply with distance."],
                ["53.28% breach at 6 to 8 km", "The distance band with the highest breach rate, 259 orders, with a minimum-volume rule applied", "Distance is where the pressure concentrates. Shorter bands sit at or below the network average."],
                ["64.52% on the worst corridor", "Ikeja GRA to Alimosho, 62 orders, ranked with a minimum-order threshold", "One kitchen-to-zone pairing is the clearest single point of failure in the network."],
            ]},
        ]},
        {"id": "findings", "heading": "What I found", "blocks": [
            {"type": "findings", "items": [
                {
                    "id": "f-sla",
                    "title": "Half the orders miss the promise, and the promise itself is half the problem",
                    "question": "Are we delivering within our promises?",
                    "paragraphs": [
                        "My SLA page shows a 50.1% success rate, a -4.97 minute average promise gap and a 43.6% delay rate. Those three numbers together tell a specific story: promises average about 505 minutes and actuals about 500, so on average the operation is nearly on promise. Yet half of all orders breach.",
                        "The severity distribution explains why. It is bimodal: roughly 2.5K orders arrive early while roughly 2.2K arrive more than 60 minutes late, with almost nothing in the middle bands. When an operation this split, the promise is mis-calibrated in both directions at once: too generous for the orders that run early, too tight for the orders that run severely late.",
                        "That is why my first recommendation is to fix the promises before fixing the riders. Recalibrating promise times by distance band attacks both tails at once, and it costs nothing operationally.",
                    ],
                    "meaning": "A breach rate of 50% with a nearly balanced promise-to-actual average is a promise-shape problem, not only a speed problem.",
                    "conclusion": "Recalibrate promised times by distance band before investing in speed.",
                    "figure": ("GoldenWok_2", "Page two, Delivery Friction and SLA Control: the SLA cards, the monthly promise-versus-actual bars, the SLA severity distribution with its early and severe clusters, the vehicle exposure ranking, and the kitchen-to-zone corridor pressure matrix."),
                },
                {
                    "id": "f-distance",
                    "title": "Distance is the pressure line, and the cost curve bends at 6 km",
                    "question": "Where is delivery friction concentrated?",
                    "paragraphs": [
                        "I banded every order by delivery distance, and the pattern is steep. Breach rates sit near the network average in the short bands, then reach 53.28% in the 6 to 8 km band on 259 orders. Delivery cost per kilometre tells the sharper story: about ₦0.65K per km on the shortest runs, ₦0.93K and ₦1.2K through the middle bands, then ₦5.44K per km at 6 to 8 km. The cost curve does not climb gently, it bends.",
                        "The zone tiers do not explain this on their own. My page-one tier breakdown shows breach rates of 48.87% in Core, 50.28% in Adjacent, 50.27% in Extended and 49.64% in Outer zones, all within two points of each other. Distance, not zone label, is what separates the healthy orders from the broken ones.",
                        "The challenge brief hypothesised that orders beyond 8 km would show structurally negative profit. My dashboard shows the pressure building earlier, from 6 km up, which matters for where a cutoff or a re-pricing rule should sit.",
                    ],
                    "meaning": "Distance is the variable that moves both service and cost at the same time, which makes it the natural first split for any operating rule.",
                    "conclusion": "Draw the operating line at 6 km, not 8: price, route and promise differently above it.",
                },
                {
                    "id": "f-economics",
                    "title": "The margin math leaves no room for surprises",
                    "question": "Where is the operation creating or consuming value?",
                    "paragraphs": [
                        "₦380.56M of revenue returns ₦2.49M of profit. That is a 0.65% margin, and delivery cost alone is ₦30.50M, 8.01% of order value. My profitability page breaks that down by zone, and the spread is thin everywhere: the top zone by margin, Shomolu, sits at 0.72% against a network average of 0.65%. Nobody is printing money; the whole network is one cost shock away from loss.",
                        "The vehicle view adds the shape. My scatter of average order profit against delivery cost share puts Tricycle (Keke) in the at-risk corner, high cost share and weak profit, while Motorcycle (Okada) sits in the healthy corner. The distance-cost curve explains why: vehicles assigned to long runs pay the steepest part of the cost curve.",
                        "That is also why the vehicle exposure ranking matters: Electric Motorcycle riders show 66.7% breach rates in the worst distance bands and Bicycle riders 57.6%, both well above Cargo Motorcycle at 53.2%. Assigning those vehicles to long routes is not a neutral choice.",
                    ],
                    "meaning": "At a 0.65% margin, operational decisions are existential. Vehicle-to-route assignment is the lever with the clearest mechanism behind it.",
                    "conclusion": "Treat vehicle assignment as a profitability decision, not a scheduling detail.",
                    "figure": ("GoldenWok_3", "Page three, Profitability and Cost Intelligence: the revenue, profit, margin and delivery cost cards, the cost-versus-profit trend, the top zone by margin, the delivery cost efficiency donut by distance band, the vehicle profitability scatter, and the zone economics table."),
                },
                {
                    "id": "f-customers",
                    "title": "Ratings barely move, and that flatness is itself a finding",
                    "question": "Is customer experience aligned with operational performance?",
                    "paragraphs": [
                        "Overall experience health sits at 3.0 out of 5, which my dashboard flags as Watch, and low-rating exposure varies sharply by destination: Isolo at 41.09% and Lekki Phase 2 at 40.48% carry the most low-rating pressure, against Maryland at 32.05% at the other end.",
                        "But when I lined customer rating up against SLA severity, the line stayed flat. Ratings sit in a narrow 2.9 to 3.3 band across every severity level, and the On Time group actually reads lowest at 2.9. In this dataset, a severely late order is rated almost the same as an on-time one.",
                        "I will not over-read that. It may mean ratings in the generated data are close to noise, or that with delivery times this long and this uniform, severity stops differentiating. Either way, the operational conclusion is the same: on this data I cannot claim that fixing delays will lift ratings, so I would sell SLA fixes on cost and retention risk, not on a promised rating lift.",
                    ],
                    "meaning": "A flat rating curve is as informative as a steep one. Here it says the customer-experience story lives in the low-rating exposure by zone, not in the delay-to-rating link.",
                    "conclusion": "Fix zones with high low-rating exposure, and do not promise rating gains from speed alone.",
                    "figure": ("GoldenWok_4", "Page four, Customer Experience Control: the 3.0/5 health card with its 37.50% low-rating rate, low-rating exposure ranked by destination zone, delivery time against rating, and rating across SLA severity sitting flat between 2.9 and 3.3."),
                },
                {
                    "id": "f-corridor",
                    "title": "One corridor is the clearest starting point",
                    "question": "Which parts of the network require attention first?",
                    "paragraphs": [
                        "My network page ranks kitchen-to-zone corridors by SLA pressure, with a minimum-order threshold so a tiny sample with an extreme rate cannot dominate the ranking. The current view puts Ikeja GRA to Alimosho at the top: 64.52% breach on 62 orders, about fifteen points above the network average.",
                        "The threshold is doing real work there. Without it, a corridor with five orders and a 100% breach rate would top the list and send management to a rounding error. With it, the ranking points at a corridor with enough volume that fixing it would be visible in the network numbers.",
                        "I pair the corridor finding with the capacity read: peak observed hourly demand of 3 orders against kitchen capacity puts highest utilisation at 6.67%. Capacity is not the constraint in this dataset. The constraint is what happens on the road, which keeps the focus on corridors and distance rather than kitchen throughput.",
                    ],
                    "meaning": "A prioritised list is only as good as its sample-size discipline. The corridor ranking earns trust because it refuses thin slices.",
                    "conclusion": "Start the operational review at Ikeja GRA to Alimosho, and re-run the ranking whenever the underlying data changes.",
                    "figure": ("GoldenWok_5", "Page five, Corridor and Network Intelligence: the network profile cards, the highest-pressure corridor callout with its breach rate, volume and distance exposure, the kitchen network performance scatter, and the corridor table with SLA, orders, profit and customer rating."),
                },
            ]},
        ]},
        {"id": "recommendations", "heading": "What I would do next", "blocks": [
            {"type": "recs", "items": [
                {"priority": "High", "title": "Fix the promises before fixing the speed",
                 "evidence": "A 50.1% success rate with promises of roughly 505 minutes and a bimodal severity distribution: 2.5K orders early, 2.2K severely late.",
                 "action": "Recalibrate promised delivery times by distance band so each band's promise reflects what that band actually delivers.",
                 "impact": "Attacks both tails at once and costs nothing operationally."},
                {"priority": "High", "title": "Draw the operating line at 6 km",
                 "evidence": "Breach rate reaches 53.28% at 6 to 8 km, and delivery cost per kilometre jumps from ₦1.2K to ₦5.44K entering that band.",
                 "action": "Above 6 km, apply a different delivery fee structure, a different vehicle assignment, or a hard cutoff.",
                 "impact": "Stops the orders that are structurally unprofitable and badly served."},
                {"priority": "High", "title": "Review the Ikeja GRA to Alimosho corridor first",
                 "evidence": "64.52% SLA breach on 62 orders, the highest of any corridor past the minimum-volume threshold.",
                 "action": "Run an operational review of that specific kitchen-to-zone pairing: routing, rider allocation and promise time.",
                 "impact": "The clearest single point of failure, and the fastest measurable improvement."},
                {"priority": "Medium", "title": "Match vehicles to routes deliberately",
                 "evidence": "Electric Motorcycle (66.7%) and Bicycle (57.6%) carry the highest distance-band breach exposure; the vehicle profitability scatter puts Keke in the at-risk corner.",
                 "action": "Assign long-distance and adverse-weather routes to the vehicle types with the best distance economics, not by availability.",
                 "impact": "Fewer breaches on the routes where the cost curve is steepest."},
                {"priority": "Medium", "title": "Build a rain-day promise adjustment",
                 "evidence": "The challenge brief flags rain conditions, and my time-slot model distinguishes rush hours; both are built into the model's slicers.",
                 "action": "Trigger a promise adjustment when weather or rush-hour conditions apply, rather than holding riders to the clear-day promise.",
                 "impact": "Removes predictable breaches from the count and protects the riders held to impossible promises."},
                {"priority": "Medium", "title": "Track low-rating zones separately from speed",
                 "evidence": "Ratings sit flat at 2.9 to 3.3 across every SLA severity level, while low-rating exposure varies by zone from 32.05% to 41.09%.",
                 "action": "Investigate what drives low ratings in Isolo and Lekki Phase 2 specifically, since delivery delay does not explain them on this data.",
                 "impact": "Puts customer-experience effort where the exposure actually is."},
            ]},
        ]},
        {"id": "limits", "heading": "What this can't tell you", "blocks": [
            {"type": "p", "items": [
                "The dataset is generated for the DataDNA challenge and the Golden Wok scenario is fictional. Profitability conclusions describe this dataset, not a real business's economics.",
                "Delivery times in this data are far longer than real-world food delivery: promises average about 505 minutes. I read relative patterns between groups, not absolute times.",
                "I excluded the food-temperature field from the customer-experience analysis entirely: its recorded values could not be validated, and I would rather report that than transform it silently.",
                "My traffic-friction bands are analytical buckets I defined for display. They are not official traffic classifications and they do not establish causal thresholds.",
                "Nothing here proves causation. A traffic group with a higher breach rate is an association worth investigating, not proof that traffic caused the delay.",
            ]},
        ]},
    ],
}


# --------------------------------------------------------------- technical
TECHNICAL = {
    "title": "Golden Wok Delivery Intelligence: how I built it",
    "lede": "The model behind the report: the star schema and its relationships, the Power Query preparation, the DAX measures with the decisions inside them, the dynamic pressure analysis, and the data-quality calls I made on the way.",
    "sections": [
        {"id": "solution", "heading": "The solution", "blocks": [
            {"type": "note", "text": "The code on this page is the DAX and model logic from my project files, as I wrote it. Every number traces to my dashboard pages, my two project READMEs, and a direct profile of the CSVs I loaded."},
            {"type": "p", "text": "I built this as a Power BI project: CSV source data prepared in Power Query, loaded into a star-schema model, and surfaced through a five-page report. The model separates transactional facts from descriptive dimensions so every page can slice delivery performance by kitchen, zone, rider, time and operating conditions. The five pages follow the operational chain I wanted management to walk: executive state, delivery friction and SLA, profitability, customer experience, then corridor and network intelligence."},
            {"type": "table", "headers": ["Component", "What I built it from", "Role"], "rows": [
                ["fact_orders", "5,000 rows, 15 fields", "One row per delivery: kitchen, zone, rider, time slot, promise and actual times, distance, traffic score, costs, profit, rating"],
                ["dim_kitchen", "4 rows", "Kitchen name, LGA, hourly capacity, opening date, active status"],
                ["dim_delivery_zone", "20 rows", "Zone name, LGA, tier, traffic index, population density, baseline delivery time, restricted-zone flag"],
                ["dim_rider", "60 rows", "Assigned kitchen, vehicle type, experience, average speed, rating, active status"],
                ["dim_time_slot", "48 rows, plus a cleaned reference table", "Original slots, then my derived hour, day of week, rush-hour flag and meal period"],
                ["dim_date", "Calculated in DAX", "Time intelligence for the trends"],
                ["The report", "5 pages in Power BI Desktop", "Executive, SLA control, profitability, customer experience, network intelligence"],
            ]},
            {"type": "p", "text": "A direct profile of the orders shows the model touches 15 of the 20 zones and 24 of the 60 riders; the rest exist in the dimensions without orders in this dataset. I mention that so the dimension row counts and the dashboard counts do not look contradictory."},
            {"type": "figure", "spec": ("GoldenWok_5", "Page five, the network view: 4 kitchens, 15 zones and 24 riders observed in the orders, with the highest-pressure corridor callout and the corridor-level table.")},
        ]},
        {"id": "model", "heading": "The data model", "blocks": [
            {"type": "p", "text": "The relationships are the classic star: the fact table filters its dimensions, one rider dimension is conformed to kitchens, and the date table carries the trends."},
            {"type": "code", "title": "Model relationships", "lang": "text", "code": r'''
fact_orders[kitchen_id]        -> dim_kitchen[kitchen_id]
fact_orders[zone_id]           -> dim_delivery_zone[zone_id]
fact_orders[rider_id]          -> dim_rider[rider_id]
fact_orders[time_slot_id]      -> dim_time_slot[time_slot_id]
dim_rider[assigned_kitchen_id] -> dim_kitchen[kitchen_id]
fact_orders[order_date]        -> dim_date[Date]
'''},
            {"type": "p", "text": "One modelling decision worth calling out: the supplied time-slot table carried the raw slot information, but I derived a cleaned reference table for the analytical attributes I actually needed, hour of day, day of week, rush-hour classification and meal period. Building those once in the dimension kept the DAX simpler and the slicers consistent across pages."},
        ]},
        {"id": "measures", "heading": "The measures and the decisions inside them", "blocks": [
            {"type": "p", "text": "The KPI layer is deliberately plain. I wanted every headline number to be auditable from its definition."},
            {"type": "code", "title": "Executive KPIs", "lang": "dax", "code": r'''
Total Orders =
DISTINCTCOUNT ( fact_orders[order_id] )

Total Revenue =
SUM ( fact_orders[order_value_ngn] )

Total Profit =
SUM ( fact_orders[order_profit_ngn] )

Profit Margin =
DIVIDE ( [Total Profit], [Total Revenue] )
'''},
            {"type": "sub", "text": "The SLA layer"},
            {"type": "code", "title": "SLA measures", "lang": "dax", "code": r'''
SLA Breaches =
CALCULATE (
    [Total Orders],
    fact_orders[actual_delivery_min] > fact_orders[promised_delivery_min]
)

SLA Breach Rate =
DIVIDE ( [SLA Breaches], [Total Orders] )

Avg Promise Gap =
AVERAGEX (
    fact_orders,
    fact_orders[actual_delivery_min]
        - fact_orders[promised_delivery_min]
)

Severe Delay Orders =
CALCULATE (
    [Total Orders],
    FILTER (
        fact_orders,
        fact_orders[actual_delivery_min]
            > fact_orders[promised_delivery_min] + 60
    )
)
'''},
            {"type": "p", "text": "The severity banding is where the report earns its diagnostic value. Rather than treating every breach the same, I classify each order by how far past the promise it landed, which is what exposed the bimodal early-versus-severe split on page two."},
            {"type": "code", "title": "SLA severity", "lang": "dax", "code": r'''
SLA Severity =
VAR Gap =
    fact_orders[actual_delivery_min]
        - fact_orders[promised_delivery_min]
RETURN
    SWITCH (
        TRUE (),
        Gap < 0, "Early",
        Gap = 0, "On Time",
        Gap <= 15, "Late 1-15 min",
        Gap <= 30, "Late 16-30 min",
        Gap <= 60, "Late 31-60 min",
        "Severe >60 min"
    )
'''},
            {"type": "sub", "text": "The banding features"},
            {"type": "code", "title": "Distance and traffic bands", "lang": "dax", "code": r'''
Distance Band =
VAR Distance = fact_orders[delivery_distance_km]
RETURN
    SWITCH (
        TRUE (),
        Distance <= 2, "0-2 km",
        Distance <= 4, "2-4 km",
        Distance <= 6, "4-6 km",
        Distance <= 8, "6-8 km",
        Distance <= 10, "8-10 km",
        "10+ km"
    )

Traffic Friction Band =
VAR Traffic = fact_orders[traffic_friction_score]
RETURN
    SWITCH (
        TRUE (),
        Traffic < 3, "Low",
        Traffic < 5, "Moderate",
        Traffic < 7, "High",
        "Very High"
    )
'''},
            {"type": "pairs", "items": [
                ("Distance bands drive the cost story", "The 6 to 8 km band carries ₦5.44K per kilometre against ₦1.2K at 4 to 6 km. One band boundary carries most of the insight, which is why I built the band as a column the whole report shares."),
                ("Traffic bands are mine, not the data's", "I defined the Low to Very High thresholds for display. I say so on the page, because presenting an analytical bucket as an external standard would be dishonest."),
                ("Severe means one hour late", "The 60-minute severe threshold matches the severity bands, so the severe-delay card and the severity distribution reconcile by construction."),
                ("Sort columns keep bands honest", "The traffic band has a numeric sort column so Low, Moderate, High and Very High never alphabetise."),
            ]},
            {"type": "p", "text": "The customer-experience layer carries a small detail I am fond of: the star display and the numeric label are computed from the same rounded value, so the stars and the text can never disagree."},
            {"type": "code", "title": "Customer experience", "lang": "dax", "code": r'''
Low Rating Orders =
CALCULATE (
    [Total Orders],
    fact_orders[customer_rating] < 2.5
)

Customer Rating Stars =
VAR Rating =
    ROUND ( [Avg Customer Rating], 1 )
VAR FullStars =
    INT ( Rating )
VAR EmptyStars =
    5 - FullStars
RETURN
    REPT ( "★", FullStars )
        & REPT ( "☆", EmptyStars )
'''},
            {"type": "sub", "text": "The economics layer"},
            {"type": "code", "title": "Cost and profitability", "lang": "dax", "code": r'''
Delivery Cost per KM =
DIVIDE (
    SUM ( fact_orders[delivery_cost_ngn] ),
    SUM ( fact_orders[delivery_distance_km] )
)

Delivery Cost % of Order Value =
DIVIDE (
    SUM ( fact_orders[delivery_cost_ngn] ),
    SUM ( fact_orders[order_value_ngn] )
)

Loss-Making Orders =
CALCULATE (
    [Total Orders],
    fact_orders[order_profit_ngn] < 0
)
'''},
        ]},
        {"id": "dynamic", "heading": "The dynamic pressure analysis", "blocks": [
            {"type": "p", "text": "Three outputs on the network page compute themselves from the current filter context, and each one has a sample-size or definition decision baked in."},
            {"type": "p", "text": "The highest-pressure corridor ranks kitchen-to-zone pairings by SLA breach rate, but only past a minimum-order threshold. Without it, a five-order corridor with a 100% breach rate would top the list. With it, the callout points at Ikeja GRA to Alimosho, 64.52% on 62 orders, which is a finding someone can act on."},
            {"type": "code", "title": "Corridor ranking logic", "lang": "text", "code": r'''
Kitchen x Zone
      |
Calculate Orders
      |
Calculate SLA Breach Rate
      |
Keep corridors with sufficient volume
      |
Rank by SLA pressure
      |
Return highest-pressure corridor
'''},
            {"type": "p", "text": "The highest distance exposure works the same way: distance bands ranked by breach rate past a volume threshold, currently 6 to 8 km at 53.28% on 259 orders."},
            {"type": "p", "text": "The capacity comparison is the one I had to define carefully. The kitchen capacity field is stated as orders per hour, so dividing total daily orders by it would be meaningless. I aggregate demand to the operating hour first, take the peak observed hour, and compare that with capacity, which puts highest utilisation at 6.67% in this dataset."},
            {"type": "code", "title": "Capacity utilisation logic", "lang": "text", "code": r'''
Daily transaction data
        |
Date + operating hour
        |
Hourly order volume
        |
Peak observed hourly demand
        |
Compare with kitchen capacity
        |
Capacity utilisation
'''},
        ]},
        {"id": "quality", "heading": "Data quality calls I made", "blocks": [
            {"type": "p", "text": "I treated data quality as part of the analysis rather than something to clean quietly. Three calls define what the report can and cannot claim."},
            {"type": "table", "headers": ["Field", "What I found", "What I did"], "rows": [
                ["food_temp_on_arrival_c", "Values I could not validate as plausible", "Excluded it from the customer-experience analysis entirely, and said so on the page rather than transforming it silently"],
                ["actual_delivery_min", "Values stretching to operationally implausible durations (P90 reads 899 minutes)", "Reported it as observed, and labelled P90 and the averages as dataset observations, not real-world delivery benchmarks"],
                ["traffic_friction_score", "A generated score with no external standard", "Banded it for display and labelled the bands as analytical categories"],
            ]},
            {"type": "p", "text": "The generated validation report that shipped with the challenge data passed 10 of 10 checks, which covers structural integrity, not plausibility. The plausibility judgement was mine, and the food-temperature exclusion is the honest example: the field exists, the values do not earn trust, so the field does not appear in my conclusions."},
            {"type": "figure", "spec": ("GoldenWok_2", "Page two is where the quality caveat matters most: the P90 delivery card reads 899 minutes, which is why every delivery-time number on my pages is framed as a dataset observation.")},
        ]},
        {"id": "validation", "heading": "Where my numbers come from", "blocks": [
            {"type": "p", "text": "Every figure on both pages is one I can trace:"},
            {"type": "table", "headers": ["Number", "Where I got it", "Cross-check"], "rows": [
                ["Headline KPIs (₦380.56M, ₦2.49M, 0.65%, 49.9%, -4.97 min)", "My dashboard pages one to three", "My business README, written from the same report"],
                ["Corridor 64.52% on 62 orders, 6 to 8 km at 53.28% on 259", "My page-five callouts", "Same figures documented in my technical README"],
                ["Zone low-rating exposure (Isolo 41.09%, Lekki Phase 2 40.48%)", "My page-four ranking", "Read directly off the dashboard screenshot"],
                ["Vehicle exposure (Electric Motorcycle 66.7%, Bicycle 57.6%)", "My page-two ranking", "Same figures in my business README"],
                ["Row counts 5,000 / 4 / 20 / 60 / 48", "Direct profile of the CSVs", "The challenge brief's dataset description"],
                ["Scope 2023-01-01 to 2024-12-31, NGN", "The challenge brief", "The report's date range and currency formatting"],
                ["Validation 10 of 10 passed", "The challenge's VALIDATION_REPORT.json", "Generated alongside the dataset"],
            ]},
            {"type": "note", "text": "One reading note I keep making: the dashboard's zone-tier breach rates sit between 48.87% and 50.28%, so tier alone explains almost nothing. That is why my findings lead with distance bands and corridors rather than zone labels."},
        ]},
        {"id": "decisions", "heading": "My decisions and trade-offs", "blocks": [
            {"type": "table", "headers": ["Decision I made", "Why", "Trade-off I accepted"], "rows": [
                ["Excluded food temperature rather than transform it", "The values could not be validated, and a silent transform would invent signal", "The customer page loses a field the brief hypothesised about"],
                ["Minimum-volume thresholds on corridor and distance rankings", "An extreme rate on a tiny sample would misdirect management", "A genuinely failing low-volume corridor waits longer for attention"],
                ["Hourly capacity comparison instead of daily totals", "Capacity is defined per hour; daily division would be meaningless", "More complex measure logic than a simple ratio"],
                ["Analytical traffic bands with visible labelling", "Display buckets make the friction matrix readable", "A reader could mistake my thresholds for official standards, so I label them"],
                ["Reported order profit as supplied", "The profit field is the challenge's own definition", "My profitability conclusions inherit whatever assumptions the generator made"],
                ["Kept delivery-time outliers visible with a caveat", "Trimming them would flatter the averages and hide the severe-delay problem", "P90 and averages look alarming until you read the framing"],
                ["Built severity and distance bands as model columns", "Every page, card and matrix bands the same way", "Changing a boundary means touching the model, not just a visual"],
            ]},
        ]},
        {"id": "upkeep", "heading": "Publication and next steps", "blocks": [
            {"type": "steps", "items": [
                ("Publish the repository", "The READMEs, the PBIX and the dataset profile are ready; the repo is the next deliverable so everything here is reproducible."),
                ("Test the brief's hypotheses directly", "The brief proposes rain effects, rush-hour-to-outer-zone failures and the Lekki corridor question; my model has the slices, the segment-level measures are the next build."),
                ("Add the loss-making order cut", "The Loss-Making Orders measure exists; surfacing its rate by zone would quantify exactly which corridors price below their cost."),
                ("Re-run the corridor ranking on any refresh", "The dynamic callouts are filter-context driven, so a new dataset recomputes them; the thresholds are the only constants to review."),
                ("Benchmark against real delivery times", "Before reusing the framework on live data, promise and actual distributions need real-world calibration."),
            ]},
        ]},
        {"id": "reflection", "heading": "What this project shows", "blocks": [
            {"type": "p", "items": [
                "This is my attempt at the difference between a scorecard and a diagnosis. The same 5,000 orders could have produced five pages of totals; instead the report connects operating conditions to friction, friction to SLA, SLA to money, and both to the customer, and it lands on named corridors rather than vague pressure.",
                "The habits I would carry forward: put sample-size discipline inside the ranking logic so the insight survives without me in the room, label analytical bands as analytical, and when a field does not earn trust, exclude it out loud.",
            ]},
        ]},
    ],
}
