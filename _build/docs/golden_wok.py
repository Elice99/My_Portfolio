"""
Golden Wok Delivery Intelligence documentation content, written in
Elisha's voice: he built the report, so the pages say "I did".

Basis for this rewrite: the DataDNA September 2026 challenge brief and
its five hypothesis bullets, his two project READMEs, the actual model
definition (the PBIP SemanticModel TMDL files with the real DAX), the
Power Query steps, the five dashboard screenshots (copied into this
site as GoldenWok_1..5), and a direct profile he can reproduce from
the shipped CSV files.

Rules: first person, plain words, no em dashes, only claims the data
supports. The dataset is a generated challenge dataset and every page
says so.
"""


# ---------------------------------------------------------------- business
BUSINESS = {
    "title": "Golden Wok Delivery Intelligence: testing the brief against 5,000 orders",
    "lede": "A five-page Power BI report built for the DataDNA September 2026 challenge. The brief handed me five hypotheses about delivery friction. I built the model, tested every one of them, and several came back false. This page covers what the brief asked, what the data actually said, and what I would do about it.",
    "sections": [
        {"id": "problem", "heading": "The problem the brief set", "blocks": [
            {"type": "note", "text": "I built this for the DataDNA September 2026 dataset challenge. The Golden Wok scenario is fictional and the dataset is generated: 5,000 orders across 4 kitchens, 15 destination zones and 24 active riders, in Lagos, in naira, spanning 2023-01-01 to 2024-12-31. I say that everywhere on these pages, because the honest reading of any generated dataset is patterns within the data, not claims about a real business."},
            {"type": "p", "items": [
                "The brief put me in the role of an analyst investigating delivery radius and urban traffic friction, and it did something I appreciated: it did not just ask for charts, it made five specific claims about the data and expected me to check them. Rush-hour orders to outer zones would run past 90 minutes and lose money. Rain would push traffic friction up 1.8 times and add about 28 minutes. Orders beyond 8 km would be structurally unprofitable. Cold food would drive low ratings. And the Lekki kitchen serving Victoria Island and Ikoyi would be a loss-making corridor.",
                "So my report has two jobs at once. One: answer the standing questions any delivery operator has, how are we performing, where is time lost, where is money made, how do customers feel, and where in the network should we look first. Two: test the brief's five claims and report honestly which ones survive contact with the data. I organized my five dashboard pages along one chain, operating conditions, delivery friction, SLA performance, profitability, customer experience, and then named corridors, so each page owns one link.",
            ]},
        ]},
        {"id": "hypotheses", "heading": "Testing the brief's five hypotheses", "blocks": [
            {"type": "p", "text": "This is the table I would want to read first if I were judging this work: each claim from the brief, what I found when I tested it against all 5,000 orders, and my verdict. Two of the five hold in some form. Three do not, and saying so plainly matters more to me than agreeing with the brief."},
            {"type": "table", "headers": ["The brief claimed", "What I found in the data", "My verdict"], "rows": [
                ["Rush-hour orders to outer zones run past 90 minutes, triple the promise, and lose money (profit below -500)",
                 "Rush-hour breach rates run 47.3% to 50.8% by zone tier, slightly better than non-rush in two tiers. About 13% to 18% of orders miss their promise by more than double, but that share is flat across tiers. And not one of the 5,000 orders is loss-making at all.",
                 "Does not hold. Rush hour is not where the pressure is in this data."],
                ["Rain or Heavy Rain raises traffic friction 1.8x and adds about 28 minutes",
                 "The time effect is real: Heavy Rain runs +38.4 minutes against Sunny days, more than the brief's estimate. But the friction score barely moves, 1.02x to 1.05x. Weather shifts delivery time, not the recorded friction score.",
                 "Half holds. The delay effect is real and larger than claimed; the 1.8x friction effect is not."],
                ["Orders beyond 8 km are structurally unprofitable regardless of order value",
                 "Orders beyond 8 km average +\u20a6498 profit, and they stay positive at every order-value level I cut. Zero loss-making orders exist anywhere in the file. What is true: delivery cost is roughly \u20a66,000 whether the run is 2 km or 30 km, so cost per kilometre collapses from \u20a65,445 on short runs to \u20a6272 on long ones.",
                 "Does not hold. Profit does not flip negative with distance; the interesting cost pattern is the opposite of what I expected."],
                ["Food temperature below 45\u00b0C for deliveries past 60 minutes, dragging ratings below 2.5",
                 "Only 4.1% of rows are both cold and late, and cold orders rate 3.04 on average against 3.00 for warm ones. The field itself is implausible: temperatures read around 500\u00b0C with values up to 999.9, which is not food, that is an oven.",
                 "Does not hold, and the field is unusable. I excluded it from every conclusion."],
                ["The Lekki kitchen serving Victoria Island and Ikoyi records negative corridor profitability",
                 "No corridor anywhere is negative. Lekki's own corridors all run positive profit. The worst corridor by profit is Ikeja GRA to Ogudu at +\u20a6432 per order, and the worst by service is Ikeja GRA to Alimosho at a 64.52% breach rate.",
                 "Does not hold as stated. The real pressure corridor is a service problem, not a profit problem, and it is not Lekki's."],
            ]},
            {"type": "p", "text": "One more finding from the same exercise: the shipped data dictionary does not describe the shipped data. It promises promised times of 25 to 45 minutes and five weather values including Clear; the file has promises from 0 to 1,000 minutes and eight weather values with no Clear. I profiled the CSVs directly and worked from what is actually in them, and I flag this here because it is exactly the kind of thing that quietly corrupts an analysis if you trust the documentation over the data."},
        ]},
        {"id": "answer", "heading": "The short answer", "blocks": [
            {"type": "verdict", "text": "With the brief's hypotheses settled, here is what the data does say. Half of all orders (49.9%) miss their promised delivery window, the average promise gap is -4.97 minutes, and the whole operation runs on a 0.65% profit margin: \u20a6380.56M of revenue returns just \u20a62.49M of profit. The severity distribution is bimodal, roughly 2,499 orders arrive early while roughly 2,181 arrive more than 60 minutes late, with almost nothing in between, which points at promise calibration rather than rider speed. Pressure concentrates in specific corridors: Ikeja GRA to Alimosho breaches 64.52% of the time on 62 orders. And the one condition effect the data supports is weather: heavy rain adds about 38 minutes to delivery. My fix order is promises first, corridors second, weather third. Every number here comes off my own dashboard and my own profiling of the shipped files."},
            {"type": "figure", "spec": ("GoldenWok_1", "Page one, the Executive Command Center: the 5K orders, \u20a6380.56M revenue and \u20a62.49M profit cards, the 50.1% SLA health gauge with its 5-minutes-behind-promise note, the monthly revenue and profit trend, and the zone-tier and rider-vehicle breakdowns.")},
        ]},
        {"id": "numbers", "heading": "Numbers at a glance", "blocks": [
            {"type": "stat_grid", "items": [
                ("5,000", "orders, 2023 to 2024"),
                ("\u20a6380.56M", "revenue across the network"),
                ("\u20a62.49M", "profit, a 0.65% margin"),
                ("49.9%", "SLA breach rate"),
                ("-4.97 min", "average promise gap"),
                ("64.52%", "breach rate on the worst corridor"),
            ]},
            {"type": "p", "text": "Where they come from: the headline KPIs, the corridor figures and the zone breakdowns are read off my dashboard pages, and the row-level facts (severity counts, weather effects, distance economics) come from my own profile of the shipped CSV files, which I ran because the shipped dictionary did not match the data."},
        ]},
        {"id": "meaning", "heading": "How to read each number", "blocks": [
            {"type": "table", "headers": ["Number", "How I got it", "How to read it"], "rows": [
                ["49.9% SLA breach rate", "Orders whose actual delivery time exceeded the promise, over all 5,000 orders", "Half the network misses its promise. The severity split says most misses are extreme: 2,181 orders arrived more than 60 minutes late."],
                ["-4.97 minute promise gap", "Average of actual minus promised delivery time", "On average deliveries run almost on promise (500 vs 505 minutes). The average hides the two-tail story; the severity bands are where it lives."],
                ["0.65% profit margin", "\u20a62.49M profit over \u20a6380.56M revenue", "Almost no cushion. Delivery cost is 8.01% of order value, so small cost movements would flip zones between profit and loss."],
                ["Bimodal severity split", "Each order banded by how far past the promise it landed: Early, On Time, three mild-late bands, Severe >60 min", "2,499 early against 2,181 severely late, and only 316 orders in the mild bands. The promise is mis-calibrated in both directions at once."],
                ["53.28% breach at 6 to 8 km", "The distance band with the highest breach rate, 259 orders", "The band-level peak, but read with care: the 8 to 10 km band dips to 44.4% and 10+ km sits at 50.3%, so distance is not a clean gradient in this data."],
                ["64.52% on the worst corridor", "Ikeja GRA to Alimosho, 62 orders, ranked with a 20-order minimum built into my measure", "One kitchen-to-zone pairing is the clearest single point of failure in the network."],
                ["+38.4 minutes in Heavy Rain", "Heavy Rain average actual time minus Sunny average, all else free", "The one condition effect the data supports, and it is bigger than the brief's own estimate. Worth a promise adjustment."],
            ]},
        ]},
        {"id": "findings", "heading": "What I found", "blocks": [
            {"type": "findings", "items": [
                {
                    "id": "f-sla",
                    "title": "The promises are broken in both directions, and that is the first thing to fix",
                    "question": "Are we delivering within our promises?",
                    "paragraphs": [
                        "My SLA page shows a 50.1% success rate, a -4.97 minute average promise gap and a 43.6% delay rate. On averages alone this operation looks nearly on time: promises average about 505 minutes and actuals about 500.",
                        "The severity distribution is what tells the truth. It is bimodal: 2,499 orders arrive early, 2,181 arrive more than 60 minutes late, and just 316 land in the three mild-late bands combined. An operation this split does not have a speed problem at the middle, it has a promise that is simultaneously too generous and too tight. The P90 sits at 899 minutes, which means the worst tenth of orders are walking home.",
                        "This is also where the brief's first hypothesis fails usefully: rush-hour orders breach at 47.3% to 50.8% depending on tier, no worse than the rest, so the breaches are not coming from when orders are placed. They come from how promises are set.",
                    ],
                    "meaning": "A 50% breach rate with a near-zero average gap is a promise-shape problem, not a speed problem.",
                    "conclusion": "Recalibrate promised times by distance band and weather condition before investing in speed.",
                    "figure": ("GoldenWok_2", "Page two, Delivery Friction and SLA Control: the SLA cards, the monthly promise-versus-actual bars, the SLA severity distribution with its early and severe clusters, the vehicle exposure ranking, and the kitchen-to-zone corridor pressure matrix."),
                },
                {
                    "id": "f-distance",
                    "title": "Distance does not do what the brief expected, and the cost curve bends the other way",
                    "question": "Where is delivery friction concentrated, and what does distance cost?",
                    "paragraphs": [
                        "I banded every order by distance, and the honest headline is that distance is a weak signal here. Breach rates sit between 44.4% and 53.3% across all six bands: the 6 to 8 km band peaks at 53.28% on 259 orders, the 8 to 10 km band dips to 44.4%, and the 10+ km band, which carries 71.7% of all orders, sits right on the network average at 50.3%. There is no clean gradient, and I would not sell one.",
                        "The economics surprised me more. The brief expected orders beyond 8 km to be structurally unprofitable. They are not: zero loss-making orders exist in the entire file, and orders beyond 8 km average +\u20a6498 profit whether the order value is \u20a61,500 or \u20a6150,000. The reason is that delivery cost barely scales with distance, about \u20a66,000 per order whether the run is 2 km or 30 km. That makes cost per kilometre collapse from \u20a65,445 on the shortest runs to \u20a6272 past 10 km, so the expensive kilometres are the short ones, not the long ones.",
                        "The zone tiers tell the same flat story: breach rates of 48.9%, 50.3%, 50.3% and 49.6% across the four tiers, all within two points. Neither zone label nor distance band explains much on its own. What does move the needle is the specific kitchen-to-zone pairing, which is where my corridor finding comes from.",
                    ],
                    "meaning": "When a hypothesised driver does not survive the data, the remaining variation points somewhere else. Here it points at corridors and promises, not distance bands.",
                    "conclusion": "Do not draw an 8 km profit cliff that is not there. Treat distance bands as display buckets and act on corridors and promise calibration instead.",
                },
                {
                    "id": "f-economics",
                    "title": "The margin math leaves no room for surprises",
                    "question": "Where is the operation creating or consuming value?",
                    "paragraphs": [
                        "\u20a6380.56M of revenue returns \u20a62.49M of profit. That is a 0.65% margin, and delivery cost alone is \u20a630.50M, 8.01% of order value. My profitability page breaks that down by zone, and the spread is thin everywhere: Shomolu tops the table at about 0.7% against a network average of 0.65%, and the weakest zone sits at 0.62%. Nobody is printing money; the whole network is one cost shock away from loss.",
                        "The vehicle view adds texture. No vehicle type is dramatically worse overall, breach rates run 49.0% to 52.0% across the five types. But my exposure ranking, which crosses vehicle type with distance band, finds the concentrated pockets: Electric Motorcycle riders breach 66.7% of the time in the 6 to 8 km band, Bicycle riders 57.6% in the 8 to 10 km band, while Tricycle (Keke) riders carry the big long-haul volume, 451 orders past 10 km at 50.1%.",
                        "Because the margin is 0.65%, these are not statistical curiosities. A vehicle assignment rule that keeps the worst vehicle-band pairs out of the worst routes is one of the few levers that operates at the scale of the whole margin.",
                    ],
                    "meaning": "At a 0.65% margin, operational decisions are existential, and the levers that matter are the ones that shift cost or breach rates at network scale.",
                    "conclusion": "Treat vehicle-to-route assignment as a profitability decision, starting with the Electric Motorcycle and Bicycle exposure pockets.",
                    "figure": ("GoldenWok_3", "Page three, Profitability and Cost Intelligence: the revenue, profit, margin and delivery cost cards, the cost-versus-profit trend, the top zone by margin, the delivery cost efficiency donut by distance band, the vehicle profitability scatter, and the zone economics table."),
                },
                {
                    "id": "f-customers",
                    "title": "Ratings barely move, and the brief's cold-food chain does not exist here",
                    "question": "Is customer experience aligned with operational performance?",
                    "paragraphs": [
                        "Overall experience health sits at 3.0 out of 5, which my dashboard flags as Watch, and low-rating exposure varies sharply by destination: Isolo at 41.09% and Lekki Phase 2 at 40.48% carry the most low-rating pressure, against Maryland at 32.05% at the other end.",
                        "But when I lined customer rating up against SLA severity, the line stayed flat: ratings sit between 2.89 and 3.27 across every severity level, and the On Time group actually reads lowest. The brief's proposed chain, late delivery causes cold food causes bad ratings, fails at both links in this data. Cold orders (below 45\u00b0C) rate 3.04 on average, slightly better than warm ones at 3.00.",
                        "And the food-temperature field itself had to go. It reads around 500\u00b0C with a maximum of 999.9, which is not a plausible food temperature in any world, so I excluded it from every conclusion rather than transform it silently. On this data I cannot claim that fixing delays will lift ratings, so I would sell SLA fixes on cost and retention risk, not on a promised rating lift.",
                    ],
                    "meaning": "A flat rating curve is as informative as a steep one. Here it says the customer-experience story lives in low-rating exposure by zone, not in the delay-to-rating link.",
                    "conclusion": "Fix zones with high low-rating exposure, and do not promise rating gains from speed alone.",
                    "figure": ("GoldenWok_4", "Page four, Customer Experience Control: the 3.0/5 health card with its 37.50% low-rating rate, low-rating exposure ranked by destination zone, delivery time against rating, and rating across SLA severity sitting flat between 2.9 and 3.3."),
                },
                {
                    "id": "f-corridor",
                    "title": "One corridor is the clearest starting point, and my ranking measure refuses thin slices",
                    "question": "Which parts of the network require attention first?",
                    "paragraphs": [
                        "My network page ranks kitchen-to-zone corridors by SLA breach rate, and the ranking measure carries a 20-order minimum by construction, so a five-order corridor with a 100% breach rate cannot top the list. The current view puts Ikeja GRA to Alimosho first: 64.52% breach on 62 orders, about fifteen points above the network average. Two runners-up sit just behind it, Surulere Hub to Surulere at 61.4% on 70 orders and Ikeja GRA to Magodo at 61.3% on 62 orders.",
                        "The corridor lens beats the tier lens because tiers explain nothing (all within two points) while corridors swing fifteen. That is also why the brief's Lekki hypothesis misdirected: the model shows Lekki's corridors are profitable and mid-pack on service. The pressure lives at Ikeja GRA's long-haul pairings.",
                        "I pair the corridor finding with the capacity read: peak observed hourly demand is 3 orders against kitchen capacity, which puts highest utilisation at 6.67%. Capacity is not the constraint in this dataset. The constraint is what happens on the road, which keeps the focus on corridors and promises rather than kitchen throughput.",
                    ],
                    "meaning": "A prioritised list is only as good as its sample-size discipline. The corridor ranking earns trust because the threshold is inside the measure, not in my head.",
                    "conclusion": "Start the operational review at Ikeja GRA to Alimosho, and re-run the ranking whenever the underlying data changes.",
                    "figure": ("GoldenWok_5", "Page five, Corridor and Network Intelligence: the network profile cards, the highest-pressure corridor callout with its breach rate, volume and distance exposure, the kitchen network performance scatter, and the corridor table with SLA, orders, profit and customer rating."),
                },
            ]},
        ]},
        {"id": "recommendations", "heading": "What I would do next", "blocks": [
            {"type": "recs", "items": [
                {"priority": "High", "title": "Fix the promises before fixing the speed",
                 "evidence": "A 50.1% success rate with a -4.97 minute average gap, a bimodal severity split (2,499 early, 2,181 severely late), and P90 at 899 minutes.",
                 "action": "Recalibrate promised delivery times by distance band and weather condition so each promise reflects what that band actually delivers.",
                 "impact": "Attacks both tails at once and costs nothing operationally."},
                {"priority": "High", "title": "Build a weather-adjusted promise",
                 "evidence": "Heavy Rain adds +38.4 minutes against Sunny days, the one condition effect the data supports, and thunderstorms alone cover 1,057 orders.",
                 "action": "Trigger a promise adjustment when Heavy Rain or Thunderstorm conditions apply, rather than holding riders to the clear-day promise.",
                 "impact": "Removes predictable breaches from the count and protects riders held to impossible promises."},
                {"priority": "High", "title": "Review the Ikeja GRA to Alimosho corridor first",
                 "evidence": "64.52% SLA breach on 62 orders, the highest of any corridor past the 20-order threshold, with two more corridors just behind at 61%.",
                 "action": "Run an operational review of that pairing: routing, rider allocation and promise time, then re-check the runner-up corridors.",
                 "impact": "The clearest single point of failure, and the fastest measurable improvement."},
                {"priority": "Medium", "title": "Match vehicles to routes deliberately",
                 "evidence": "Electric Motorcycle breaches 66.7% in the 6 to 8 km band and Bicycle 57.6% in the 8 to 10 km band, while Keke carries 451 long-haul orders at 50.1%.",
                 "action": "Assign routes using the vehicle-band exposure ranking, not availability alone.",
                 "impact": "Fewer breaches on the exact vehicle-band pairs where they concentrate."},
                {"priority": "Medium", "title": "Track low-rating zones separately from speed",
                 "evidence": "Ratings sit flat at 2.9 to 3.3 across every SLA severity level, while low-rating exposure varies by zone from 32.05% to 41.09%.",
                 "action": "Investigate what drives low ratings in Isolo and Lekki Phase 2 specifically, since delivery delay does not explain them on this data.",
                 "impact": "Puts customer-experience effort where the exposure actually is."},
                {"priority": "Low", "title": "Re-test the brief's hypotheses on a dataset that matches its dictionary",
                 "evidence": "Three of five hypotheses fail on this data, and the shipped dictionary does not describe the shipped file.",
                 "action": "If the challenge re-runs with regenerated data, re-run my same model and measures; the thresholds and bands are the only constants to review.",
                 "impact": "The whole framework is reusable; only the conclusions would change."},
            ]},
        ]},
        {"id": "limits", "heading": "What this can't tell you", "blocks": [
            {"type": "p", "items": [
                "The dataset is generated for the DataDNA challenge and the Golden Wok scenario is fictional. Profitability conclusions describe this dataset, not a real business's economics.",
                "Delivery times in this data are far longer than real-world food delivery: promises average about 505 minutes and P90 sits at 899. I read relative patterns between groups, not absolute times.",
                "I excluded the food-temperature field from the analysis entirely: its values read around 500\u00b0C up to 999.9, which is implausible on its face, and I would rather report that than transform it silently.",
                "My traffic-friction and distance bands are analytical buckets I defined for display. They are not official classifications and they do not establish causal thresholds. The distance band story is deliberately weak here and I say so rather than selling a gradient the data does not show.",
                "Nothing here proves causation. Heavy Rain runs 38 minutes slower than Sunny, but weather is not randomly assigned in this data, so I treat it as a strong association worth acting on, not proof.",
                "The shipped data dictionary does not match the shipped CSVs on several fields (promised times, weather values, zone tier labels). My numbers come from the CSVs; anyone reproducing this from the dictionary alone will get different answers.",
            ]},
        ]},
    ],
}


# --------------------------------------------------------------- technical
TECHNICAL = {
    "title": "Golden Wok Delivery Intelligence: how I built it",
    "lede": "The model behind the report: the Power BI project structure, the star schema and its relationships, the Power Query preparation, the DAX measures with the decisions inside them, the dynamic pressure analysis, and the data-quality calls I made on the way.",
    "sections": [
        {"id": "solution", "heading": "The solution", "blocks": [
            {"type": "note", "text": "The DAX and Power Query on this page come from my model definition files, as I wrote them. Every number traces to my dashboard pages, my two project READMEs, and a direct profile of the shipped CSV files."},
            {"type": "p", "text": "I built this as a Power BI project: CSV source data prepared in Power Query, loaded into a star-schema model, and surfaced through a five-page report. My project folder is a PBIP workspace, with the semantic model and report definition in separate folders and the PBIX as the shipped artifact. Inside the model I organized measures into five display folders that mirror the report's chain, Core KPIs, Delivery & SLA, Profitability, Operations, Customer Experience, plus an Analysis folder for the dynamic callouts, so anyone opening the model sees the same structure the report walks."},
            {"type": "table", "headers": ["Component", "What I built it from", "Role"], "rows": [
                ["fact_orders", "5,000 rows, 15 fields", "One row per delivery: kitchen, zone, rider, time slot, promise and actual times, distance, traffic score, costs, profit, rating"],
                ["dim_kitchen", "4 rows", "Kitchen name, LGA, hourly capacity, opening date, active status"],
                ["dim_delivery_zone", "20 rows", "Zone name, LGA, tier, traffic index, population density, baseline delivery time, restricted-zone flag"],
                ["dim_rider", "60 rows", "Assigned kitchen, vehicle type, experience, average speed, rating, active status"],
                ["dim_time_slot", "48 rows, source", "Original slot labels with hour, day, rush flag, meal period and weather"],
                ["dim_time_slot_clean", "My Power Query derivation", "Slot start and end times, numeric hour, my own rush-hour windows, cleaned meal periods, time bands and sort keys"],
                ["dim_date", "Built in the model", "Time intelligence for the monthly trends"],
                ["The report", "5 pages in Power BI Desktop", "Executive, SLA control, profitability, customer experience, network intelligence"],
            ]},
            {"type": "p", "text": "A direct profile of the orders shows the model touches 15 of the 20 zones and 24 of the 60 riders; the rest exist in the dimensions without orders in this dataset. I mention that so the dimension row counts and the dashboard counts do not look contradictory."},
            {"type": "figure", "spec": ("GoldenWok_5", "Page five, the network view: 4 kitchens, 15 zones and 24 riders observed in the orders, with the highest-pressure corridor callout and the corridor-level table.")},
        ]},
        {"id": "prep", "heading": "The Power Query preparation", "blocks": [
            {"type": "p", "text": "The source tables needed two kinds of cleaning, and both happened in Power Query rather than in DAX, because preparation belongs in the loading layer."},
            {"type": "p", "text": "First, the kitchen names. The CSV ships them as \"Golden Wok Yaba Central\" and friends, which is redundant next to a report that already says Golden Wok everywhere, so I strip the prefix on load. What is left keeps a leading space, and my DAX measures match that exactly. It looks odd in the code and it is deliberate."},
            {"type": "code", "title": "Kitchen name cleanup (dim_kitchen query)", "lang": "python", "code": r'''
#"Replaced Value" = Table.ReplaceValue(
    #"Changed column type", "Golden Wok", "",
    Replacer.ReplaceText, {"kitchen_name"})
'''},
            {"type": "p", "text": "Second, and more involved: the time-slot table. The raw slot_label reads like \"07:30-08:00\", which no visual can sort or slice properly. I derived a clean reference table that parses the label into start and end times, pulls the numeric hour, and then rebuilds the analytical attributes I actually needed. The rush-hour definition matters most: I hard-coded the brief's own windows, 07:00 to 09:00 and 16:30 to 19:30, so my rush-hour analysis tests exactly what the brief claimed."},
            {"type": "code", "title": "Rush-hour windows, straight from the brief (dim_time_slot_clean query)", "lang": "python", "code": r'''
#"Added Custom3" = Table.AddColumn(PreviousStep, "is_rush_hour_clean",
    each if ([slot_start_time] >= #time(7,0,0) and [slot_start_time] < #time(9,0,0))
         or ([slot_start_time] >= #time(16,30,0) and [slot_start_time] < #time(19,30,0))
    then "Yes" else "No")
'''},
            {"type": "p", "text": "The same query derives cleaned meal periods (Breakfast 6 to 11, Lunch 11 to 15, Dinner 15 to 22, Late Night after), Morning/Afternoon/Evening/Night time bands, and a numeric sort key so every time visual sorts by actual time instead of alphabetically. Building these once in the dimension kept the DAX simple and the slicers consistent across all five pages."},
        ]},
        {"id": "model", "heading": "The data model", "blocks": [
            {"type": "p", "text": "The relationships are the classic star: the fact table filters its four dimensions, and the rider dimension is conformed to kitchens through its assigned-kitchen column, so kitchen analysis can see rider attributes without a second fact path."},
            {"type": "code", "title": "Model relationships", "lang": "text", "code": r'''
fact_orders[kitchen_id]        -> dim_kitchen[kitchen_id]
fact_orders[zone_id]           -> dim_delivery_zone[zone_id]
fact_orders[rider_id]          -> dim_rider[rider_id]
fact_orders[time_slot_id]      -> dim_time_slot_clean[time_slot_id]
dim_rider[assigned_kitchen_id] -> dim_kitchen[kitchen_id]
fact_orders[order_date]        -> dim_date[Date]
'''},
            {"type": "p", "text": "Inside fact_orders I added the banding columns the whole report shares: an SLA severity column with a matching sort column, a distance band with its sort column, and month helpers for the trend visuals. I built them as model columns rather than measures on purpose, so every page, card and matrix bands the same way, and the sort columns keep Early through Severe and 0-2 km through 10+ km from ever alphabetising."},
            {"type": "code", "title": "SLA severity and its sort", "lang": "python", "code": r'''
column 'SLA Severity' =
    VAR Gap = fact_orders[actual_delivery_min]
              - fact_orders[promised_delivery_min]
    RETURN SWITCH ( TRUE (),
        Gap < 0,  "Early",
        Gap = 0,  "On Time",
        Gap <= 15, "Late 1-15 min",
        Gap <= 30, "Late 16-30 min",
        Gap <= 60, "Late 31-60 min",
        "Severe >60 min" )

column 'SLA Severity Sort' =
    SWITCH ( fact_orders[SLA Severity],
        "Early", 1, "On Time", 2, "Late 1-15 min", 3,
        "Late 16-30 min", 4, "Late 31-60 min", 5,
        "Severe >60 min", 6, 99 )
'''},
            {"type": "code", "title": "Distance band and its sort", "lang": "python", "code": r'''
column 'Distance Band' =
    VAR Distance = fact_orders[delivery_distance_km]
    RETURN SWITCH ( TRUE (),
        Distance <= 2,  "0-2 km",
        Distance <= 4,  "2-4 km",
        Distance <= 6,  "4-6 km",
        Distance <= 8,  "6-8 km",
        Distance <= 10, "8-10 km",
        "10+ km" )
'''},
        ]},
        {"id": "measures", "heading": "The measures and the decisions inside them", "blocks": [
            {"type": "p", "text": "The KPI layer is deliberately plain. I wanted every headline number to be auditable from its definition."},
            {"type": "code", "title": "Executive KPIs (Core KPIs table)", "lang": "dax", "code": r'''
Total Orders = DISTINCTCOUNT ( fact_orders[order_id] )

Total Revenue = SUM ( fact_orders[order_value_ngn] )

Total Profit = SUM ( fact_orders[order_profit_ngn] )

Profit Margin = DIVIDE ( [Total Profit], [Total Revenue] )

Avg Order Value = DIVIDE ( [Total Revenue], [Total Orders] )

P90 Actual Delivery =
PERCENTILEX.INC ( fact_orders,
    fact_orders[actual_delivery_min], 0.90 )
'''},
            {"type": "p", "text": "The trend layer uses month-over-month measures on the date intelligence, so the executive page can show orders, revenue and profit movement without me rebuilding anything on refresh."},
            {"type": "code", "title": "Month-over-month pattern", "lang": "dax", "code": r'''
Total Revenue MoM % =
VAR CurrentRev = [Total Revenue]
VAR PreviousRev =
    CALCULATE ( [Total Revenue],
        DATEADD ( fact_orders[order_date].[Date], -1, MONTH ) )
RETURN DIVIDE ( CurrentRev - PreviousRev, PreviousRev )
'''},
            {"type": "sub", "text": "The SLA layer"},
            {"type": "code", "title": "SLA measures (Delivery & SLA table)", "lang": "dax", "code": r'''
SLA Breaches =
CALCULATE ( [Total Orders],
    fact_orders[actual_delivery_min]
        > fact_orders[promised_delivery_min] )

SLA Breach Rate = DIVIDE ( [SLA Breaches], [Total Orders] )

SLA Compliance rate = 1 - [SLA Breach Rate]

Avg Delivery Variance =
[Avg Actual Delivery] - [Avg Promised Delivery]

Severe Delay Orders =
CALCULATE ( [Total Orders],
    FILTER ( fact_orders,
        fact_orders[actual_delivery_min]
            > fact_orders[promised_delivery_min] + 60 ) )
'''},
            {"type": "p", "text": "One measure on this page I am particularly happy with writes its own sentence. The executive card does not show a naked number, it reads the variance, picks a direction word and an icon, and composes the takeaway. When the data refreshes, the sentence rewrites itself, which is the whole point of a dynamic report."},
            {"type": "code", "title": "The self-writing delivery summary", "lang": "dax", "code": r'''
Delivery Exec Summary =
VAR promise = [Avg Promised Delivery]
VAR actual  = [Avg Actual Delivery]
VAR varianc = [Avg Delivery Variance]
VAR stat = IF ( varianc >= 0, "ahead of", "behind" )
VAR icon = IF ( varianc >= 0, UNICHAR ( 9679 ), UNICHAR ( 9660 ) )
RETURN
    "We are delivering " & icon
        & FORMAT ( ABS ( varianc ), "#,0" )
        & " minutes " & stat & " promise." & UNICHAR ( 10 )
    & "Promise: " & FORMAT ( promise, "#,0" )
        & " min | Actual: " & FORMAT ( actual, "#,0" ) & " min"
'''},
            {"type": "sub", "text": "The economics layer"},
            {"type": "code", "title": "Cost and profitability", "lang": "dax", "code": r'''
Delivery Cost per KM =
DIVIDE ( SUM ( fact_orders[delivery_cost_ngn] ),
         SUM ( fact_orders[delivery_distance_km] ) )

Delivery Cost % of Order Value =
DIVIDE ( SUM ( fact_orders[delivery_cost_ngn] ),
         SUM ( fact_orders[order_value_ngn] ) )

Loss-Making Orders =
CALCULATE ( [Total Orders],
    fact_orders[order_profit_ngn] < 0 )

Loss-Making Order Rate =
DIVIDE ( [Loss-Making Orders], [Total Orders] )
'''},
            {"type": "p", "text": "The Loss-Making Orders measure is the one that answers the brief's distance hypothesis directly. On this dataset it returns zero, which is itself the finding: there is no loss-making population to segment, so the corridor and promise stories take over."},
            {"type": "sub", "text": "The rider and customer layers"},
            {"type": "code", "title": "Rider benchmarking (Operations table)", "lang": "dax", "code": r'''
Rider Status =
VAR SLA = [SLA Breach Rate]
RETURN SWITCH ( TRUE (),
    SLA < 0.25, "STRONG",
    SLA < 0.50, "WATCH",
    "CONCERNING" )

Rider SLA Position =
VAR RiderSLA   = [SLA Breach Rate]
VAR NetworkSLA =
    CALCULATE ( [SLA Breach Rate], REMOVEFILTERS ( dim_rider ) )
RETURN SWITCH ( TRUE (),
    RiderSLA < NetworkSLA - 0.05, "BELOW NETWORK",
    RiderSLA > NetworkSLA + 0.05, "ABOVE NETWORK",
    "NEAR NETWORK" )
'''},
            {"type": "p", "text": "The rider page benchmarks each rider against the network, not against a fixed number, so the flag survives a data refresh. The customer layer carries the star display I am fond of: the stars and the numeric label compute from the same rounded value, so they can never disagree."},
            {"type": "code", "title": "Customer experience", "lang": "dax", "code": r'''
Low Rating Orders =
CALCULATE ( [Total Orders],
    fact_orders[customer_rating] < 2.5 )

Low Rating Rate =
DIVIDE ( [Low Rating Orders], [Total Orders] )

Customer Rating Stars =
VAR Rating = ROUND ( [Avg Customer Rating], 1 )
VAR FullStars = INT ( Rating )
VAR EmptyStars = 5 - FullStars
RETURN REPT ( "\u2605", FullStars ) & REPT ( "\u2606", EmptyStars )
'''},
        ]},
        {"id": "dynamic", "heading": "The dynamic pressure analysis", "blocks": [
            {"type": "p", "text": "Three outputs on the network page compute themselves from the current filter context, and each one has a sample-size or definition decision baked in. This is where the Analysis measure folder earns its keep."},
            {"type": "p", "text": "The highest-pressure corridor ranks kitchen-to-zone pairings by SLA breach rate. I build the full cross join, compute orders and breach rate per pair, keep only corridors with at least 20 orders, then take the top row with a tie-break on volume. The 20-order minimum is the decision: without it, a five-order corridor with a 100% breach rate would top the list. With it, the callout points at Ikeja GRA to Alimosho, 64.52% on 62 orders, which is a finding someone can act on."},
            {"type": "code", "title": "Highest Pressure Corridor (the real measure, condensed)", "lang": "dax", "code": r'''
VAR CorridorTable =
    ADDCOLUMNS (
        CROSSJOIN ( ALLSELECTED ( dim_kitchen[kitchen_id] ),
                    ALLSELECTED ( dim_delivery_zone[zone_id] ) ),
        "@Orders", CALCULATE ( [Total Orders] ),
        "@SLA",    CALCULATE ( [SLA Breach Rate] ) )

VAR ValidCorridors =
    FILTER ( CorridorTable,
        [@Orders] >= 20 && NOT ISBLANK ( [@SLA] ) )

VAR TopCorridor =
    TOPN ( 1, ValidCorridors, [@SLA], DESC, [@Orders], DESC )
-- then LOOKUPVALUE the kitchen and zone names and
-- return KitchenName & " -> " & ZoneName
'''},
            {"type": "p", "text": "The highest distance exposure reuses the same pattern over distance bands instead of corridors, same 20-order floor, currently pointing at the 6 to 8 km band at 53.28% on 259 orders. A companion measure writes the sentence into a card so the page explains itself."},
            {"type": "code", "title": "The distance insight card", "lang": "dax", "code": r'''
Distance Pressure Insight =
"Highest SLA pressure occurs in " & [Highest Risk Distance Band]
    & " at " & FORMAT ( [Highest Risk Distance SLA], "0.0%" )
    & " breach rate."
'''},
            {"type": "p", "text": "The capacity comparison is the one I had to define carefully. The kitchen capacity field is stated as orders per hour, so dividing total daily orders by it would be meaningless. I aggregate demand to the operating hour first with a SUMMARIZE over date and hour, take the peak observed hour, and compare it with capacity. That puts peak hourly demand at 3 orders and highest utilisation at 6.67% in this dataset, which is itself a finding: capacity is nowhere near the constraint."},
            {"type": "code", "title": "Capacity utilisation", "lang": "dax", "code": r'''
Peak Hourly Orders =
MAXX (
    SUMMARIZE ( fact_orders,
        fact_orders[order_date].[Date],
        dim_time_slot_clean[hour],
        "@Hourly Orders", [Total Orders] ),
    [@Hourly Orders] )

Peak Capacity Utilization =
DIVIDE ( [Peak Hourly Orders],
         MAX ( dim_kitchen[kitchen_capacity_orders_hr] ) )
'''},
        ]},
        {"id": "quality", "heading": "Data quality calls I made", "blocks": [
            {"type": "p", "text": "I treated data quality as part of the analysis rather than something to clean quietly. Four calls define what the report can and cannot claim, and the first two are the ones I would highlight in a review."},
            {"type": "table", "headers": ["What I found", "What I did"], "rows": [
                ["The food-temperature field reads around 500\u00b0C with values up to 999.9. No food is an oven. It also fails the brief's own hypothesis: cold orders rate 3.04, warm ones 3.00.",
                 "Excluded it from every conclusion, and said so on the page rather than transforming it silently."],
                ["The shipped data dictionary does not describe the shipped CSVs: it promises 25 to 45 minute deliveries and five weather values including Clear, while the file carries promises of 0 to 1,000 minutes and eight weather values with no Clear.",
                 "Profiled the CSVs directly and worked from the actual data. The dictionary mismatch is documented in my README so nobody reproduces this from the dictionary alone."],
                ["Delivery times stretch to operationally implausible durations (P90 at 899 minutes, promises averaging 505).",
                 "Reported as observed, and labelled P90 and the averages as dataset observations, not real-world delivery benchmarks."],
                ["The traffic friction score is a generated 0 to 10 number with no external standard.",
                 "Banded it for display and labelled the bands as analytical categories in my README."],
            ]},
            {"type": "p", "text": "The generated validation report that shipped with the challenge data passed 10 of 10 checks, which covers structural integrity, not plausibility. The plausibility judgement was mine, and the food-temperature exclusion is the honest example: the field exists, the values do not earn trust, so the field does not appear in my conclusions."},
            {"type": "figure", "spec": ("GoldenWok_2", "Page two is where the quality caveat matters most: the P90 delivery card reads 899 minutes, which is why every delivery-time number on my pages is framed as a dataset observation.")},
        ]},
        {"id": "validation", "heading": "Where my numbers come from", "blocks": [
            {"type": "p", "text": "Every figure on both pages is one I can trace:"},
            {"type": "table", "headers": ["Number", "Where I got it", "Cross-check"], "rows": [
                ["Headline KPIs (\u20a6380.56M, \u20a62.49M, 0.65%, 49.9%, -4.97 min)", "My dashboard pages one to three", "My business README, written from the same report"],
                ["Corridor 64.52% on 62 orders; 6 to 8 km at 53.28% on 259", "My page-five callouts", "Same figures documented in my technical README"],
                ["Severity split 2,499 early / 4 on time / 316 mild-late / 2,181 severe", "My page-two distribution", "Direct profile of fact_orders.csv"],
                ["Weather effect (+38.4 min Heavy Rain vs Sunny)", "Direct profile of the weather groups", "The brief's own claim (+28 min), which the data exceeds"],
                ["Zone low-rating exposure (Isolo 41.09%, Lekki Phase 2 40.48%)", "My page-four ranking", "Read directly off the dashboard screenshot"],
                ["Vehicle exposure (Electric Motorcycle 66.7%, Bicycle 57.6%)", "My page-two ranking", "Same figures in my business README"],
                ["Row counts 5,000 / 4 / 20 / 60 / 48", "Direct profile of the CSVs", "The challenge brief's dataset description"],
                ["Scope 2023-01-01 to 2024-12-31, NGN", "The challenge brief", "The report's date range and currency formatting"],
                ["Validation 10 of 10 passed", "The challenge's VALIDATION_REPORT.json", "Generated alongside the dataset"],
            ]},
            {"type": "note", "text": "One reading note I keep making: the dashboard's zone-tier breach rates sit between 48.87% and 50.28%, so tier alone explains almost nothing. That is why my findings lead with corridors, promises and weather rather than zone labels."},
        ]},
        {"id": "decisions", "heading": "My decisions and trade-offs", "blocks": [
            {"type": "table", "headers": ["Decision I made", "Why", "Trade-off I accepted"], "rows": [
                ["Excluded food temperature rather than transform it", "The values read around 500\u00b0C and fail the brief's own hypothesis; a silent transform would invent signal", "The customer page loses a field the brief hypothesised about"],
                ["Profiled the CSVs instead of trusting the dictionary", "The dictionary and the data disagree on several fields", "Anyone reproducing from the dictionary alone will get different answers, so I documented the mismatch"],
                ["Minimum-order thresholds (20) inside the corridor and distance ranking measures", "An extreme rate on a tiny sample would misdirect management", "A genuinely failing low-volume corridor waits longer for attention"],
                ["Hard-coded the brief's rush-hour windows in Power Query", "My rush-hour test answers exactly what the brief claimed, 07:00-09:00 and 16:30-19:30", "If the challenge's definition changed, the window needs a one-line edit"],
                ["Hourly capacity comparison instead of daily totals", "Capacity is defined per hour; daily division would be meaningless", "More complex measure logic than a simple ratio"],
                ["Reported order profit as supplied", "The profit field is the challenge's own definition", "My profitability conclusions inherit whatever assumptions the generator made"],
                ["Kept delivery-time outliers visible with a caveat", "Trimming them would flatter the averages and hide the severe-delay problem", "P90 and averages look alarming until you read the framing"],
                ["Built severity and distance bands as model columns with sort columns", "Every page, card and matrix bands the same way, and bands never alphabetise", "Changing a boundary means touching the model, not just a visual"],
            ]},
        ]},
        {"id": "upkeep", "heading": "Publication and next steps", "blocks": [
            {"type": "steps", "items": [
                ("Publish the repository", "The READMEs, the PBIX, the PBIP model definition and the dataset profile are ready; the repo is the next deliverable so everything here is reproducible."),
                ("Surface the loss-making order cut", "The measure exists; on this data it reads zero, which is worth showing as its own card so the brief's profit-cliff claim is answered on the page, not just in the docs."),
                ("Add a weather-adjusted promise scenario", "Heavy Rain adds 38 minutes; a measure-side scenario that extends promises under rain would quantify how much of the breach rate is weather-predictable."),
                ("Re-run the corridor ranking on any refresh", "The dynamic callouts are filter-context driven, so a new dataset recomputes them; the 20-order threshold is the only constant to review."),
                ("Benchmark against real delivery times", "Before reusing the framework on live data, promise and actual distributions need real-world calibration."),
            ]},
        ]},
        {"id": "reflection", "heading": "What this project shows", "blocks": [
            {"type": "p", "items": [
                "This project is my attempt at the difference between agreeing with a brief and testing one. The brief handed me five confident claims; I built the model that could check all of them, found three of them false, and built the report around what the data actually supports: promise calibration, corridor pressure and a weather effect larger than the one the brief predicted.",
                "The habits I would carry forward: put sample-size discipline inside the ranking logic so the insight survives without me in the room, write measures that explain themselves so the report stays current on refresh, profile the data instead of trusting its documentation, and when a field or a hypothesis does not earn trust, say so out loud.",
            ]},
        ]},
    ],
}
