"""
Airbnb Market Intelligence documentation content, written in Elisha's
own voice: he built this, so the pages say "I did", not "the repo has".

Every number is one he produced: the run lines in reports/app.log, the
metrics saved to models/model_info.txt, the queries in sql/analytics.sql,
and the charts his pipelines generated (copied into this site as
AirbnbDoc_1..6). The screenshots on the project page capture a real
/predict run of his API.

Rules: first person, plain words, no em dashes, only claims his saved
outputs support.
"""


# ---------------------------------------------------------------- business
BUSINESS = {
    "title": "Airbnb Market Intelligence: what the data says and what the model is worth",
    "lede": "I built an ETL pipeline into PostgreSQL, wrote 16 SQL analytics queries for the market questions, trained an XGBoost price model behind a FastAPI endpoint, and put a Streamlit app on top. This page covers what my data says about NYC pricing, how good my price model actually is, and where I would take it next.",
    "sections": [
        {"id": "problem", "heading": "The problem", "blocks": [
            {"type": "note", "text": "I built this on the public Airbnb NYC 2019 open dataset: 48,895 listings with price, room type, borough and neighbourhood, host activity, availability and review counts. It is a 2019 snapshot, not a live market, and I say so everywhere on these pages."},
            {"type": "p", "items": [
                "Pricing is the biggest lever a short-term rental host has, and most hosts work it blind. Underprice against comparable listings and the revenue gap compounds every night. Overprice and bookings dry up. The usual methods are gut feel, scanning a few neighbour listings, or a static template, because there has been no structured way to answer: what should this listing, in this borough, in this room type, actually charge?",
                "So I built the missing layer in three pieces. An ETL pipeline that cleans the raw data and loads it into PostgreSQL. A SQL analytics layer, 16 queries, that answers the benchmark questions: prices by borough, room type and neighbourhood, host performance, availability patterns. And a prediction layer: an XGBoost model I trained on the cleaned listings, served through a FastAPI endpoint, with a Streamlit app so a host can enter their listing details and get a price estimate with a range.",
                "My model answers one question per listing: given what similar listings in similar locations have charged, what is a realistic nightly price?",
            ]},
        ]},
        {"id": "answer", "heading": "The short answer", "blocks": [
            {"type": "verdict", "text": "The market data is unambiguous about one thing: location and room type set the price band. Average prices run from $86 in the Bronx to $183 in Manhattan, and the median room types sit at $160 for an entire home, $70 for a private room and $45 for a shared one. My model turns that into a per-listing benchmark: on my saved evaluation it explains about 46% of price variance (R² 0.4553) with a typical error of $83.10, and five-fold cross-validation lands at $80.65 ± $1.31, so I know the number is not a lucky split. I position the output as a benchmark midpoint with a range, not a price oracle: my API returns a low and high estimate of about ±$47 around the prediction, and I am upfront that roughly half of price variation comes from things this data does not contain. Every number on this page comes out of my own run logs and saved metrics."},
            {"type": "figure", "spec": ("AirbnbDoc_1", "Average listing price by borough, from a chart my EDA pipeline generates from the cleaned data. The Manhattan-to-Bronx gap is the first benchmark any host should see: same city, more than double the average price.")},
        ]},
        {"id": "numbers", "heading": "Numbers at a glance", "blocks": [
            {"type": "stat_grid", "items": [
                ("48,895", "listings in the raw dataset"),
                ("48,884", "listings after my cleaning pass"),
                ("16", "SQL analytics queries I wrote"),
                ("38,833", "training rows, 16 features"),
                ("$83.10", "test RMSE of my price model"),
                ("R² 0.4553", "share of price variance explained"),
            ]},
            {"type": "p", "text": "Where they come from: I log every cleaning and training run as it happens, so the row counts and cleaning actions come straight from my pipeline log, the model numbers from the metrics file my training run saves, and the query count from my own SQL file."},
        ]},
        {"id": "meaning", "heading": "How to read each number", "blocks": [
            {"type": "table", "headers": ["Number", "How I got it", "How to read it"], "rows": [
                ["48,895 → 48,884 listings", "My cleaning pass dropped 11 listings priced at $0", "A $0 price is an invalid record, not a cheap listing. Everything else I capped or filled, I did not delete it."],
                ["$799 price cap", "I clipped prices above the 99th percentile to it", "The raw data tops out at $10,000 a night against a median of $106. Capping keeps those rows but stops them distorting my model."],
                ["38,833 training rows", "Rows with a value for every feature and the target", "Most of the difference from 48,884 is the 10,052 listings that never received a review, whose recency feature has no value."],
                ["RMSE $83.10", "My best model (XGBoost), on a held-out test set of 7,767 listings", "Typical prediction error in dollars. On a median price of around $106, that is a real but honest gap."],
                ["R² 0.4553", "Share of price variance my features explain", "Listing attributes and location explain about 46% of the variation. The rest is detail this dataset does not have."],
                ["$80.65 ± $1.31", "Mean and spread of RMSE across my 5 cross-validation folds", "My model performs consistently across different data splits, so the headline number is not a lucky split."],
            ]},
        ]},
        {"id": "findings", "heading": "What I found", "blocks": [
            {"type": "findings", "items": [
                {
                    "id": "f-market",
                    "title": "The spread across the city is the benchmark",
                    "question": "What does the market data actually tell a host?",
                    "paragraphs": [
                        "Average prices run from $183 in Manhattan down to $86 in the Bronx, with Brooklyn at $119, Staten Island at $102 and Queens at $96. Room type splits the same way: median prices sit at $160 for an entire home, $70 for a private room and $45 for a shared one.",
                        "The practical consequence I kept running into is that a city-wide average is useless as a reference. A host charging $80 a night in the Bronx is above their market; the same price in Manhattan is far below it. Any benchmark has to be borough plus room type first, neighbourhood second. That is why I wrote my SQL layer to build exactly those cuts: borough and room-type summaries, the top neighbourhoods by price with a minimum listing count, and a percentile rank that tells a host where their price sits inside their borough.",
                    ],
                    "meaning": "The most valuable output of my analytics layer is not a number, it is the right comparison group.",
                    "conclusion": "Benchmark every listing against its borough, room type and neighbourhood before anything else.",
                    "figure": ("AirbnbDoc_2", "Price distribution by room type, from my EDA pipeline. Medians sit at $160 for an entire home, $70 for a private room and $45 for a shared one, so room type sets the band before location even enters."),
                },
                {
                    "id": "f-signal",
                    "title": "My model is a benchmark with a range, not a price oracle",
                    "question": "How good is the price prediction, really?",
                    "paragraphs": [
                        "I trained three models on the same split. Linear regression reached an RMSE of $90.58 (R² 0.3529), random forest $83.83 (R² 0.4457), and XGBoost won at $83.10 with an MAE of $47.20 (R² 0.4553). Five-fold cross-validation on the winner gives a mean RMSE of $80.65 ± $1.31, so the held-out number matches the cross-validated one.",
                        "I turned that error into an honest output shape in the API. A real run of my service, which I captured in the screenshots on the project page, asked for an entire home in Williamsburg with a two-night minimum, and returned $243.58 with a range of $196.38 to $290.78. I build that range from the model's MAE, so it is a measured uncertainty, not a marketing buffer.",
                        "An R² of 0.4553 tells me my features explain about 46% of price variance: what a listing is, where it is, and how it operates. The remaining half lives in things this dataset does not carry: amenities, photos, listing quality, seasonality, the host's actual calendar. I would rather tell a host that than let them over-trust a number.",
                    ],
                    "meaning": "The prediction is a market reference point. A host should read the range and then weigh what they know that the data does not.",
                    "conclusion": "Quote the prediction with its range, and describe the model as a benchmark, not an appraiser.",
                },
                {
                    "id": "f-importance",
                    "title": "Room type and price-encoded location carry my model",
                    "question": "What actually drives the predictions?",
                    "paragraphs": [
                        "My feature importance chart is blunt: room_type accounts for about 37% of the model's split importance, more than the next two features combined. Those next two are the price-encoded geography I added: the median price of the listing's neighbourhood (about 11%) and of its borough (about 13%). After that come the long-term flag, the professional-host proxy and availability, all in single digits.",
                        "The encoding is my favourite decision in this build. Raw neighbourhood names mean nothing to a model, and 221 of them would blow up into 221 one-hot columns. Instead I gave each neighbourhood its median price as a numeric feature, so the model sees Tribeca at $295 and Fordham at $55 and can split on real price context.",
                    ],
                    "meaning": "The model confirms what my EDA showed: what you rent and where you rent it set the band, and everything else adjusts within it.",
                    "conclusion": "Lead any pricing guidance with room type and location tier, and treat the other attributes as fine-tuning.",
                    "figure": ("AirbnbDoc_3", "Feature importance from my trained XGBoost model, generated by my training pipeline. Room type carries about 37% of the split importance, more than the two price-encoded geography features behind it combined."),
                },
                {
                    "id": "f-demand",
                    "title": "Demand signals barely move price in this data",
                    "question": "Do reviews and availability explain pricing?",
                    "paragraphs": [
                        "When I built the correlation heatmap, it said no, not much. No feature I kept correlates with price above 0.12: host listing count and availability sit at 0.12, review counts at -0.06, and the recency of the last review at -0.01. The one strong correlation with price (0.37) is price_per_review, which I excluded from the model because I derived it from price itself.",
                        "That is a finding in itself. Reviews and availability describe activity and supply, not what a listing can charge. A listing can be fully booked all year and still be cheap, and a listing with no reviews can still sit in an expensive neighbourhood.",
                    ],
                    "meaning": "Any pricing advice built on review activity would be reading noise. The benchmark story has to come from location and room type, which is what my model and my SQL layer both do.",
                    "conclusion": "Do not sell review or availability metrics as pricing levers on this data.",
                },
            ]},
        ]},
        {"id": "recommendations", "heading": "What I would do next", "blocks": [
            {"type": "recs", "items": [
                {"priority": "High", "title": "Decide with the range, not the midpoint",
                 "evidence": "My API returns a low and high estimate built from the model's measured MAE ($47.20); my saved run shows $243.58 with a range of $196.38 to $290.78.",
                 "action": "Use the midpoint as the market reference and the range as the decision space: price near the bottom to fill calendar, near the top to test demand.",
                 "impact": "Hosts get a defensible pricing strategy instead of a single number to over-trust."},
                {"priority": "High", "title": "Refresh the data before hosting decisions",
                 "evidence": "I trained on the 2019 open snapshot, so my model only knows that market.",
                 "action": "Re-pull current listings, re-run my pipeline, and retrain before quoting benchmarks against today's market.",
                 "impact": "I built the whole system to be re-runnable, so freshness is a scheduled task, not a rebuild."},
                {"priority": "Medium", "title": "Add the signals that carry the missing half of price",
                 "evidence": "R² 0.4553 tells me about 54% of price variance is unexplained by listing attributes, location and activity.",
                 "action": "Join amenities, review quality scores and calendar seasonality onto the listings and re-run my feature experiments.",
                 "impact": "The benchmark range tightens where it matters most, the mid market."},
                {"priority": "Medium", "title": "Surface the neighbourhood benchmarks in my app",
                 "evidence": "My SQL layer already computes neighbourhood rankings and a per-borough percentile rank for every listing.",
                 "action": "Pipe those query results into my Streamlit neighbourhood explorer so a host sees their percentile, not just a prediction.",
                 "impact": "My analytics layer and my prediction layer reinforce each other on one screen."},
                {"priority": "Medium", "title": "Treat the top end as out of scope",
                 "evidence": "I capped prices at the 99th percentile ($799) during cleaning, and my actual-versus-predicted chart shows the model underpredicting at high actual prices.",
                 "action": "Say so in the product: my model benchmarks the everyday market, and luxury listings need a different approach.",
                 "impact": "The tool keeps its credibility by refusing predictions it cannot support."},
            ]},
        ]},
        {"id": "limits", "heading": "What this can't tell you", "blocks": [
            {"type": "p", "items": [
                "I trained on the public 2019 NYC open dataset, so nothing here measures today's market, and New York's short-term rental rules have changed since.",
                "R² 0.4553 is my documented baseline, not a claim of accurate appraisal. About 54% of price variance is not explained by my data.",
                "Because I capped training prices at $799 (the 99th percentile), my model has not seen true luxury pricing and should not be asked about it.",
                "The dataset has no amenities, review scores, photos or calendar detail, which is where much of my unexplained variance lives.",
                "These pages describe the 2019 build exactly as I saved it. I have not yet re-run the full stack on fresh data, which is why the refresh sits at the top of my recommendations.",
            ]},
        ]},
    ],
}


# --------------------------------------------------------------- technical
TECHNICAL = {
    "title": "Airbnb Market Intelligence: how I built it",
    "lede": "The full pipeline as I built it: the cleaning and feature engineering with their real logged numbers, the PostgreSQL layer, my 16 SQL analytics queries, the three-model comparison, the FastAPI service, and the Streamlit app.",
    "sections": [
        {"id": "solution", "heading": "The solution", "blocks": [
            {"type": "note", "text": "The code here is straight from my pipeline files, only re-indented. Long functions are excerpts and I say what I cut. Every number comes out of my own saved outputs: the metrics file my training run writes, the run lines in my log, my SQL file, and the charts my pipelines generate."},
            {"type": "p", "text": "I built the project as one pipeline with three consumers. My ETL layer (data_loader, data_cleaner, feature_engineer, db_loader) takes the raw CSV, cleans and enriches it, and loads it into PostgreSQL. My SQL analytics file answers the market questions against the loaded table. My ML branch trains and compares three models, cross-validates the winner, and saves the full sklearn pipeline (preprocessing included) as one artifact. My FastAPI backend loads that artifact and serves predictions, and my Streamlit frontend gives the four explorer pages. My pipelines also generate 15 charts that document the EDA and the model evaluation; I embedded six of them across these two pages."},
            {"type": "table", "headers": ["Component", "Where it lives", "What I built it to do"], "rows": [
                ["Raw data", "data/raw/AB_NYC_2019.csv", "The public Airbnb NYC 2019 open dataset, 48,895 listings"],
                ["ETL pipeline", "pipelines/data_cleaner.py, feature_engineer.py", "My cleaning steps, outlier caps, and 11 engineered feature functions"],
                ["Database layer", "pipelines/db_loader.py, db_connection.py", "SQLAlchemy load into PostgreSQL"],
                ["SQL analytics", "sql/analytics.sql", "My 16 business queries in 6 sections, including window functions"],
                ["Training code", "pipelines/ml_pipeline.py", "Three models, preprocessing, 5-fold CV, evaluation, 3 charts"],
                ["Model artifact", "models/best_model_xgboost.pkl + model_info.txt", "The full pipeline (preprocessor + XGBoost) I save with its metrics"],
                ["API", "app/backend/ (FastAPI)", "health, predict, model-info endpoints with Pydantic validation"],
                ["Frontend", "app/frontend/ (Streamlit)", "Market analytics, price prediction, neighbourhood explorer, model performance"],
                ["Generated evidence", "reports/charts/ (15 charts), app.log", "My EDA charts, evaluation charts, and the run lines every number here comes from"],
            ]},
            {"type": "p", "text": "One scoping note I want on the record: my README describes a Docker Compose deployment and cloud targets as the plan. I have not shipped the container files yet, so I treat deployment as documented intent, not something I claim as running."},
        ]},
        {"id": "data", "heading": "The data and my cleaning pass", "blocks": [
            {"type": "p", "text": "The raw file is the Airbnb NYC 2019 open dataset: 48,895 rows, 16 columns. I wrote each cleaning function to do one job and log what it did, so my run log preserves the counts. These are the actions it recorded:"},
            {"type": "table", "headers": ["Step I built", "What it did", "Why I did it"], "rows": [
                ["Drop zero prices", "11 rows removed", "A $0 listing is an invalid record that breaks averages and models"],
                ["Cap price outliers", "Prices above the 99th percentile ($799) clipped to it", "Raw max is $10,000 against a median of $106. Capping keeps real rows but limits their pull"],
                ["Cap minimum nights", "Values above the 99th percentile clipped", "Raw max is 1,250 nights, about 3.4 years, which would distort my model"],
                ["Fill review nulls", "10,052 rows: reviews_per_month set to 0, last_review flagged", "Those listings have never been reviewed. Zero is the true value, not a placeholder"],
                ["Fill text nulls", "16 listing names, 21 host names set to 'Unknown'", "The rows stay valid; the text is just missing"],
                ["Standardise text", "Whitespace stripped, neighbourhoods title-cased", "So 'Manhattan' and ' Manhattan' do not split into two categories"],
                ["Parse dates", "last_review converted to datetime, unparsable values kept as null", "My time-based features need a real date type"],
            ]},
            {"type": "code", "title": "My outlier handling (data_cleaner.py, excerpt)", "lang": "python", "code": r'''
def cap_price_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Why cap instead of drop?
    - Dropping removes real data (some listings ARE expensive).
    - Capping keeps the row but limits its influence on the model.
    - The 99th percentile is a standard industry threshold.
    """
    cap_value = df["price"].quantile(0.99)
    df["price"] = df["price"].clip(upper=cap_value)
    return df
'''},
            {"type": "p", "text": "My validation report at the end of the run confirms the result: 48,884 rows, 16 columns, no missing values left in the modelling columns, price max $799."},
        ]},
        {"id": "features", "heading": "My feature engineering and the leakage call", "blocks": [
            {"type": "p", "text": "I wrote eleven feature functions that run after cleaning. Some serve my dashboards, some serve my model. The ones my model actually uses are 16: three categoricals (borough, neighbourhood, room type), two price-encoded geography columns, and eleven numeric features."},
            {"type": "code", "title": "My model's feature list (ml_pipeline.py)", "lang": "python", "code": r'''
    FEATURES = [
        # Categorical
        "neighbourhood_group",
        "neighbourhood",
        "room_type",
         # Numeric - price-encoded geography
        "neighbourhood_median_price",
        "neighbourhood_group_median_price",
        # Numeric - original
        "minimum_nights",
        "number_of_reviews",
        "reviews_per_month",
        "calculated_host_listings_count",
        "availability_365",
        # Numeric - engineered
        "is_reviewed",
        "host_is_superhost_proxy",
        "availability_ratio",
        "is_long_term",
        "name_length",
        "days_since_last_review",
    ]
'''},
            {"type": "p", "text": "The geography encoding is the decision I am proudest of here. It replaces raw names with each area's median price, so my model gets numeric signal it can split on, and it stays compact where one-hot encoding 221 neighbourhoods would not."},
            {"type": "code", "title": "My neighbourhood target encoding (feature_engineer.py, excerpt)", "lang": "python", "code": r'''
    """
    Why this works better than ordinal encoding:
    OrdinalEncoder assigns arbitrary numbers - 'Tribeca'=187,
    'Bronx'=23. The model has no idea 187 means expensive.

    Median price encoding gives the model real signal:
    'Tribeca' -> $295, 'Fordham' -> $55.
    """
    neigh_median = (
        df.groupby("neighbourhood")["price"]
        .median()
        .rename("neighbourhood_median_price")
    )
    df["neighbourhood_median_price"] = df["neighbourhood"].map(neigh_median)
'''},
            {"type": "sub", "text": "Two features I built and then excluded"},
            {"type": "p", "text": "My engineering step also creates price_per_review (price divided by reviews) and price_category (budget to luxury buckets). Neither reaches my model. Both are derived from the target, so training on them would hand my model the answer. My code comment on the feature list says exactly that, and my correlation heatmap shows why the temptation exists: price_per_review is the only feature correlating with price at 0.37."},
            {"type": "figure", "spec": ("AirbnbDoc_6", "My feature correlation heatmap from the EDA pipeline. Price's strongest correlations with the features I kept are 0.12 (host listing count, availability); the visible 0.37 with price_per_review is the excluded, target-derived feature.")},
            {"type": "p", "text": "One preprocessing note on my choice: categoricals go through an OrdinalEncoder with an unknown-value fallback rather than one-hot encoding. With 221 unique neighbourhoods, one-hot would add 221 columns; the ordinal route keeps my matrix compact, and the tree models do the category work themselves."},
        ]},
        {"id": "model", "heading": "My model and its real numbers", "blocks": [
            {"type": "p", "text": "I kept training to one script. It loads my featured data, drops rows with any missing feature or target value (38,833 rows remain), splits 80/20 into 31,066 training and 7,767 test rows with a fixed random state so anyone can reproduce it, builds a preprocessing pipeline (encoding plus scaling), and trains three models on identical inputs."},
            {"type": "code", "title": "My candidate models (ml_pipeline.py, excerpt)", "lang": "python", "code": r'''
        "RandomForest": Pipeline([
            ("preprocessor", preprocessor),
            ("model", RandomForestRegressor(
                n_estimators=200, max_depth=15,
                min_samples_leaf=5, max_features=0.8,
                random_state=42, n_jobs=-1
            ))
        ]),

        "XGBoost": Pipeline([
            ("preprocessor", preprocessor),
            ("model", XGBRegressor(
                n_estimators=300, learning_rate=0.05,
                max_depth=6, subsample=0.8, colsample_bytree=0.8,
                random_state=42, n_jobs=-1, verbosity=0
            ))
        ]),
'''},
            {"type": "p", "text": "I also keep a fourth configuration in the script, an XGBoost with heavier regularisation, alongside these. My comparison picks the lowest test RMSE, cross-validates the winner, and saves the full pipeline so my API can accept raw inputs without repeating preprocessing."},
            {"type": "table", "headers": ["Model", "Test RMSE", "Test MAE", "R²"], "rows": [
                ["Linear regression", "$90.58", "$53.19", "0.3529"],
                ["Random forest", "$83.83", "$47.43", "0.4457"],
                ["XGBoost (my selection)", "$83.10", "$47.20", "0.4553"],
            ]},
            {"type": "stat_grid", "items": [
                ("$83.10", "Test RMSE, XGBoost"),
                ("$47.20", "Test MAE"),
                ("R² 0.4553", "Variance explained"),
                ("$80.65 ± $1.31", "5-fold cross-validated RMSE"),
                ("7,767", "Held-out test rows"),
                ("16", "Features"),
            ]},
            {"type": "p", "text": "These are the numbers my training run saves to models/model_info.txt at the end, and they match my README comparison table and the final run lines in my log."},
            {"type": "figure", "spec": ("AirbnbDoc_4", "Actual versus predicted price on my test set, with my saved metrics in the title. The cloud tracks the diagonal through the mid market; at high actual prices my predictions flatten below the line, which is exactly what my $799 training cap predicts it would do.")},
            {"type": "figure", "spec": ("AirbnbDoc_5", "My residual analysis from the same run: residuals against predicted price, and their distribution. The spread widens as predicted price rises, the usual shape for right-skewed price data, and the distribution stays centred on zero.")},
        ]},
        {"id": "serving", "heading": "How I serve the model", "blocks": [
            {"type": "p", "text": "My FastAPI backend loads the pickle once at startup and exposes three endpoints: GET /health, POST /predict and GET /model-info, with FastAPI's own docs page generated at /docs. The predict router is the part I would point a reviewer at, because it rebuilds every engineered feature from the raw request so the served input matches my training input exactly."},
            {"type": "code", "title": "Rebuilding my engineered features (routers/predict.py, excerpt)", "lang": "python", "code": r'''
    # Derived features - same logic as feature_engineer.py
    is_reviewed  = 1 if request.number_of_reviews > 0 else 0
    is_long_term = 1 if request.minimum_nights >= 30 else 0
    host_proxy   = 1 if request.calculated_host_listings_count >= 5 else 0
    avail_ratio  = round(request.availability_365 / 365, 4)

    # Neighbourhood price encoding
    neigh_median = NEIGHBOURHOOD_MEDIANS.get(
        request.neighbourhood,
        BOROUGH_MEDIANS.get(request.neighbourhood_group, 106.0)
    )
    group_median = BOROUGH_MEDIANS.get(request.neighbourhood_group, 106.0)

    # days_since_last_review - use training mean for new listings
    days_since = 277.95
'''},
            {"type": "p", "text": "Three serving decisions sit in this excerpt, all mine. Unknown neighbourhoods fall back to their borough median, and unrecognised boroughs to an overall median of $106, so my endpoint never crashes on a spelling difference. New listings with no review history get my training mean for review recency instead of a null. And I clip the output to a realistic band before it leaves my service."},
            {"type": "code", "title": "My response shape (routers/predict.py, excerpt)", "lang": "python", "code": r'''
    # Clip to realistic range - model can sometimes predict
    # negative or extremely high values for edge cases
    predicted_price = max(10.0, min(predicted_price, 799.0))
    predicted_price = round(predicted_price, 2)

    # Build price range using MAE as uncertainty estimate
    price_low  = round(max(10.0, predicted_price - MODEL_MAE), 2)
    price_high = round(min(799.0, predicted_price + MODEL_MAE), 2)

    return PredictionResponse(
        predicted_price=predicted_price,
        price_range_low=price_low,
        price_range_high=price_high,
        currency="USD",
        model_version="xgboost_v1",
        ...
    )
'''},
            {"type": "p", "text": "MODEL_MAE is my saved test MAE ($47.20), so my uncertainty band is measured, not decorative. I ran the service for real and captured it in the screenshots: a Manhattan entire home with a two-night minimum returned predicted_price 243.58 with a range of 196.38 to 290.78 and model_version xgboost_v1."},
            {"type": "table", "headers": ["Endpoint", "Method", "Purpose"], "rows": [
                ["/", "GET", "Service index"],
                ["/health", "GET", "Service and model status"],
                ["/predict", "POST", "Listing details in, price with low/high range out"],
                ["/model-info", "GET", "Model version, feature count, target and dataset"],
                ["/docs", "GET", "Auto-generated OpenAPI documentation"],
            ]},
        ]},
        {"id": "sql", "heading": "My SQL analytics layer", "blocks": [
            {"type": "p", "text": "I wrote 16 queries in analytics.sql across six sections, all against my featured_listings table in PostgreSQL: market overview, pricing intelligence, host analytics, availability and demand, review analytics, and window-function analytics. I structured the section headings to mirror the dashboard brief, so every query maps to a question a host or a platform team would ask."},
            {"type": "code", "title": "My percentile-rank query (analytics.sql, query 6.3)", "lang": "python", "code": r'''
-- Percentile rank of every listing within its borough
-- Useful for telling a host "your listing is in the top X%"
SELECT
    id,
    name,
    neighbourhood_group AS borough,
    room_type,
    price,
    ROUND(
        (
            PERCENT_RANK() OVER (
                PARTITION BY neighbourhood_group
                ORDER BY price
            ) * 100
        )::numeric,
        1
    ) AS price_percentile_in_borough
FROM featured_listings
ORDER BY neighbourhood_group, price_percentile_in_borough DESC
LIMIT 20;
'''},
            {"type": "p", "text": "That query is the bridge between my analytics layer and the product: it converts a price into a position, which is what a host actually needs to know. My other window queries rank neighbourhoods inside each borough (RANK), and build running totals and rolling three-row averages ordered by price (SUM and AVG with window frames)."},
            {"type": "table", "headers": ["Section", "Queries", "What I wrote them to answer"], "rows": [
                ["Market overview", "3", "Total listings, hosts, neighbourhoods, average and median price; per-borough and per-room-type shares"],
                ["Pricing intelligence", "3", "Top 15 neighbourhoods by price (min 30 listings), price-category mix per borough, room-type cross-tab"],
                ["Host analytics", "3", "Top hosts by listings, proxy-superhost comparison, hosts by average review volume"],
                ["Availability and demand", "2", "Availability category mix, availability by borough and room type"],
                ["Review analytics", "2", "Review activity by borough, review-score category breakdown"],
                ["Window functions", "3", "In-borough price ranks, running totals and rolling averages, per-listing percentile rank"],
            ]},
        ]},
        {"id": "app", "heading": "My Streamlit app", "blocks": [
            {"type": "p", "text": "I built the frontend as a multipage Streamlit app with a shared utils module. My goal was to make the two layers usable without SQL or Python: a host enters listing details and gets a price with a range; an analyst browses the market with filters."},
            {"type": "table", "headers": ["Page", "What it does"], "rows": [
                ["Market analytics", "Interactive charts and filters over my cleaned market data"],
                ["Price prediction", "Listing form, calls my /predict endpoint, shows the price with its range"],
                ["Neighbourhood explorer", "Compares areas by price, reviews and availability"],
                ["Model performance", "Shows my model metrics and my feature importance chart"],
            ]},
            {"type": "p", "text": "A walkthrough recording of my app is embedded on the project page above these documents."},
        ]},
        {"id": "validation", "heading": "Where my numbers come from", "blocks": [
            {"type": "p", "text": "I keep my pipeline honest by saving outputs as it runs, so every number on both pages can be traced to a file I produced. This is what each one sits on:"},
            {"type": "table", "headers": ["Number", "Where I saved it", "What confirms it"], "rows": [
                ["Final metrics $83.10 / $47.20 / R² 0.4553", "models/model_info.txt", "My README comparison table and the final training run line in my log"],
                ["Cross-validation $80.65 ± $1.31", "Final run line in reports/app.log", "My README cross-validation note"],
                ["Cleaning counts (11 dropped, $799 cap, 10,052 review fills, 48,884 final rows)", "Run lines in reports/app.log", "The cleaning code's own documented expectations"],
                ["Training shapes 38,833 / 31,066 / 7,767", "Run lines in reports/app.log", "An 80/20 split of my modelling rows"],
                ["16 SQL queries", "sql/analytics.sql", "Counted from the file I wrote"],
                ["Feature importance and market charts", "reports/charts/", "Generated by my ml_pipeline.py and my EDA pipeline; I copied them into this site as the figures on these pages"],
                ["Live prediction run", "Project screenshots", "My /predict returned $243.58 (range $196.38 to $290.78) for a Manhattan entire home, model_version xgboost_v1"],
            ]},
            {"type": "note", "text": "One thing my log keeps me honest about: the final run is where my headline metrics come from, and an earlier run of mine shows RMSE $83.55 at 14 features, before my price-encoded geography columns landed. The improvement from the encoding is small but real, which is why I describe the encoding as signal, not magic."},
        ]},
        {"id": "decisions", "heading": "My decisions and trade-offs", "blocks": [
            {"type": "table", "headers": ["Decision I made", "Why", "Trade-off I accepted"], "rows": [
                ["Cap outliers at the 99th percentile instead of dropping", "Keeps real expensive listings in my data", "My model never trains on true luxury prices, so it should not be asked about them"],
                ["Fill never-reviewed listings' review counts with 0", "Zero is the true value, not a missing one", "My recency features are null for them, which drops those rows from training"],
                ["Target-encode neighbourhoods with median price", "Gives my model real numeric geography signal, compact with 221 neighbourhoods", "My medians are computed on the full dataset before the split, justified as stable geographic facts, but it is a choice I want to re-test with fold-wise encoding"],
                ["Ordinal-encode the remaining categoricals", "Keeps my matrix compact", "Imposes an arbitrary order my trees must work around"],
                ["Exclude price_per_review and price_category from my model", "Both are derived from the target, so they leak", "Loses the single strongest correlate of price in my heatmap"],
                ["Build the response range from my test MAE", "The uncertainty is measured, not invented", "My band is uniform in dollars; it is wider than needed at the low end"],
                ["Save the whole pipeline, preprocessing included", "My API accepts raw inputs with no duplicate cleaning logic", "The pickle carries sklearn version coupling"],
                ["Clip my predictions to $10 to $799", "Serves plausible outputs on edge cases", "Hides model failure at the extremes rather than surfacing it"],
            ]},
        ]},
        {"id": "upkeep", "heading": "Deployment and next steps", "blocks": [
            {"type": "steps", "items": [
                ("Refresh the data", "My 2019 snapshot ages; I will re-pull, re-run my ETL, retrain, and quote new metrics."),
                ("Finish the container story", "My README plans Docker Compose for the API and database; I need to ship the Dockerfile and compose file so the one-command run is real."),
                ("Fold-wise target encoding", "I want to re-test my neighbourhood medians computed inside each fold to remove the before-split computation entirely."),
                ("Add the missing signals", "Amenities, review quality and seasonality are where my unexplained half of price variance lives."),
                ("Keep my validation report", "My cleaning pipeline's end-of-run report is the first thing I check after any data refresh."),
                ("Guard the endpoint", "Authentication and rate limits are not part of my demo service; they are my first requirement if it is exposed publicly."),
            ]},
        ]},
        {"id": "reflection", "heading": "What this project shows", "blocks": [
            {"type": "p", "items": [
                "This is my end-to-end analytics and ML build, not a notebook: a cleaning pipeline whose every action is logged and countable, a leakage call I made before it could flatter my metrics, a three-model comparison with cross-validation behind my headline number, an API that rebuilds its own features so serve-time inputs match training inputs, and a SQL layer that answers the benchmark questions my model alone cannot.",
                "The habits I built here are the part I would carry into any future project: cap rather than delete and say so, measure the uncertainty and ship it in the response, and let my saved log be the source of truth for every number I quote.",
            ]},
        ]},
    ],
}
