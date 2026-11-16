"""
Customer Churn Prediction documentation content, written in Elisha's
voice: he trained and served the model, so the pages say "I did".

Basis: his BUSINESS_README.md, TECHNICAL_README.md, QUICK_REFERENCE.md
and LINKEDIN_POST.md in the Elisha-ML-Journey repo, the Churn.py and
predict.py source, the Swagger UI screenshot (CustomerChurn_2), and a
direct profile of Telco-Customer-Churn.csv plus an exact re-run of his
pipeline (5-fold CV and the held-out test score) that reproduced every
metric.

Rules: first person, plain words, no em dashes, only claims the data
supports. Where an earlier writeup used a loose label (accuracy for
AUC, "yearly revenue" for lifetime billing), the precise version is
used here and the correction is stated.
"""


# ---------------------------------------------------------------- business
BUSINESS = {
    "title": "Customer Churn Prediction: the risk model and the money behind it",
    "lede": "A logistic regression that ranks telecom customers by their probability of leaving, validated with cross-validation and served through an API. This page covers the business case: what the data says about who leaves, what that is worth, and what a retention team should do with the score.",
    "sections": [
        {"id": "problem", "heading": "The problem I set out to solve", "blocks": [
            {"type": "p", "items": [
                "Retention teams in telecom mostly work reactively: a customer calls to cancel, and only then does anyone try to keep them. The dataset I worked with describes 7,043 customers of a telecom provider across 21 attributes: who they are, what services they take, how long they have stayed, what they pay, and whether they left.",
                "The question I wanted the data to answer is the one a retention budget depends on: who is most likely to churn next, and are they even worth the outreach cost? Not every departing customer is equal. A month-to-month customer paying $74 a month for four months is a different problem from a two-year customer paying $118 a month for six years.",
                "So I split the work in two. A prediction model that scores every customer's churn probability, and an executive dashboard that shows where the risk lives in the business. The dashboard has its own case study on this site; this page is the model and the money.",
            ]},
        ]},
        {"id": "answer", "heading": "The short answer", "blocks": [
            {"type": "verdict", "text": "The churn in this data is not a mystery: it concentrates in a handful of segments that are visible long before anyone needs a model. Month-to-month customers churn at 42.7% against 2.8% for two-year contracts, a 15-fold difference. Fiber optic customers churn at 41.9% against 19.0% on DSL. Electronic-check payers churn at 45.3% against 15.2% on automatic credit card. The 1,869 customers who churned carry $2.86M of lifetime billing, and the churned segment bills $74.44 a month on average against $64.76 for everyone else, so the people leaving are the ones paying the most. The model's job is to turn those segment facts into an individual score: my logistic regression reaches a test ROC-AUC of 0.858, meaning it ranks a random churner above a random non-churner about 86 times out of 100, and a retention team can work the ranked list top-down."},
            {"type": "figure", "spec": ("CustomerChurn_1", "The executive dashboard I built alongside the model: the 1,869 at-risk customers, their ticket load, monthly and lifetime billing, and the demographic and service panels that show where the risk concentrates.")},
        ]},
        {"id": "numbers", "heading": "Numbers at a glance", "blocks": [
            {"type": "stat_grid", "items": [
                ("7,043", "customers in the dataset"),
                ("26.5%", "churn rate (1,869 customers)"),
                ("0.858", "test ROC-AUC"),
                ("0.842", "cross-validation AUC (+/- 0.007)"),
                ("15x", "contract-type churn spread (42.7% vs 2.8%)"),
                ("$2.86M", "lifetime billing in the churned segment"),
            ]},
            {"type": "p", "text": "Where they come from: the dataset figures are from my direct profile of the CSV, and the model scores are from an exact re-run of my training pipeline, the same code as my Churn.py, which reproduced the cross-validation and test results my README reports. Both pages of this case study only carry numbers I can regenerate on demand."},
        ]},
        {"id": "meaning", "heading": "How to read each number", "blocks": [
            {"type": "table", "headers": ["Number", "How I got it", "How to read it"], "rows": [
                ["0.858 test ROC-AUC", "Scoring my final model on the 1,409-customer hold-out", "A ranking quality, not an accuracy. It says a random churner gets a higher score than a random retained customer 85.8% of the time. My README sometimes calls this 85.8% accuracy; the precise claim is the ranking one."],
                ["0.842 +/- 0.007", "Five-fold cross-validation on the 5,634-customer training set", "The tight spread across folds matters more than the level: the model is not riding one lucky split."],
                ["42.7% vs 2.8%", "Churn rate by contract type, computed on the raw data", "The single strongest pattern in the dataset. Contract type is the closest thing this problem has to a ground truth."],
                ["45.3% e-check churn", "Churn rate within the electronic-check payment segment", "Process friction behaves like a churn driver in its own right, at nearly three times the automatic-payment rate."],
                ["$74.44 vs $64.76", "Average monthly bill, churned group versus the full base", "The customers who leave are above-average payers, which is why churn here is a revenue problem and not just a count."],
                ["$2.86M", "Total lifetime charges billed to the 1,869 churned customers", "What those customers were worth across their whole stay. My dashboard labels this Yearly Charges; the precise reading is cumulative lifetime billing, and their monthly run-rate is $139,131."],
            ]},
        ]},
        {"id": "findings", "heading": "What I found", "blocks": [
            {"type": "findings", "items": [
                {
                    "id": "f-contract",
                    "title": "Contract type is the ground truth of this problem",
                    "question": "What separates the customers who leave from the ones who stay?",
                    "paragraphs": [
                        "I cut the churn rate by every dimension in the dataset, and nothing comes close to contract type. Month-to-month customers churn at 42.7%, one-year customers at 11.3%, two-year customers at 2.8%. That is a 15-fold spread between the extremes, and it dwarfs every demographic effect in the data.",
                        "It also makes business sense rather than just statistical sense: a customer with no term commitment can leave in any billing cycle, so the observed rate is the natural consequence of the contract structure. Two-year customers churn at 2.8% not because they are loyal by temperament but because leaving costs them something.",
                        "The practical translation is uncomfortable but useful: the biggest retention lever in this data is not a model, it is moving customers onto term commitments. The model's value is telling you which month-to-month customers to convert first.",
                    ],
                    "meaning": "When one variable dominates this hard, the intervention design should start from it rather than from a blended risk score.",
                    "conclusion": "Treat month-to-month contracts as the primary targeting criterion, and use the model score to rank within that segment.",
                    "figure": ("CustomerChurn_1", "The contract-type slicer sits in the middle of my dashboard for exactly this reason: it is the cut that reorganises every other number."),
                },
                {
                    "id": "f-services",
                    "title": "The services customers do not take are the ones that predict leaving",
                    "question": "Does service adoption mark the at-risk segment?",
                    "paragraphs": [
                        "Add-on service adoption runs 29% for online security, 34% for online backup, 34% for device protection and 29% for tech support, against 90% phone-service uptake. The protective add-ons are the least-adopted services in the base.",
                        "Internet type cuts the same way: fiber optic customers churn at 41.9% while DSL customers churn at 19.0%, and customers with no internet service at all are the most stable of all at 7.4%. The premium, high-expectation product churns hardest; the plain, reliable one holds.",
                        "My reading is that the low-adoption numbers are an engagement signal, not a service-quality finding. A customer who buys only the core product has fewer ties to the provider and fewer moments of perceived value, and the fiber pattern says expectations outran delivery at the premium tier.",
                    ],
                    "meaning": "Service adoption and internet type behave like leading indicators you can read from billing data alone, months before a cancellation.",
                    "conclusion": "Use low add-on adoption plus fiber as the profile to prioritise, and test bundling as the retention offer.",
                    "figure": ("CustomerChurn_1", "The services panel on my dashboard lists the adoption share for every add-on, which is where the 29% support and security gaps stand out against the 90% phone baseline."),
                },
                {
                    "id": "f-payment",
                    "title": "Payment friction is a churn signal hiding in a billing field",
                    "question": "Can a mundane account field carry risk information?",
                    "paragraphs": [
                        "Payment method looks like the dullest field in the dataset, and it produces one of the sharpest splits: electronic-check payers churn at 45.3%, while automatic bank-transfer and credit-card payers churn at 16.7% and 15.2%. Mailed checks sit at 19.1%.",
                        "That is nearly a three-fold difference inside an account attribute nobody would call strategic. One plausible mechanism: automatic payment removes a monthly moment where cancelling is easy, while a manual e-check keeps the customer doing effortful billing work every cycle.",
                        "I verified the mix too: electronic check is 34% of the payment field while every automatic method is about 22%, so the high-risk group is also the largest single payment segment, not a fringe.",
                    ],
                    "meaning": "Operational friction fields can carry as much signal as satisfaction scores, and they are free to collect.",
                    "conclusion": "Move e-check customers to automatic payments as a low-cost retention play, and watch whether churn follows.",
                    "figure": ("CustomerChurn_1", "The payment-methods bars on my dashboard, which is where the e-check share and its churn association sit side by side."),
                },
                {
                    "id": "f-value",
                    "title": "The customers who leave are the ones paying the most",
                    "question": "Is churn here a volume problem or a revenue problem?",
                    "paragraphs": [
                        "The churned segment bills $74.44 per month on average against $64.76 across the full base, so the leavers are about 15% above-average payers. Their cumulative lifetime billing totals $2.86M across the 1,869 customers, an average of $1,532 each.",
                        "On a monthly basis the churned segment was a $139,131 run-rate, roughly $1.67M a year if it had held. That is the honest revenue-at-stake number; the $2.86M figure is what those customers had already paid over their whole stay, which is why my dashboard's Yearly Charges label needed this clarification.",
                        "The tenure side completes the picture: 29.4% of all customers are inside their first 12 months, and my dashboard's subscription-time panel shows the risk window is front-loaded, before contracts and habits settle.",
                    ],
                    "meaning": "Churn concentrated among above-average payers inside the first year makes the revenue exposure much larger than the customer count suggests.",
                    "conclusion": "Weight retention priority by monthly billing as well as churn probability, and front-load interventions into the first year.",
                    "figure": ("CustomerChurn_1", "The monthly and lifetime billing cards on my dashboard, with the average-charge card showing the $74.44 churned-group figure."),
                },
                {
                    "id": "f-model",
                    "title": "The model turns segment facts into an individual score",
                    "question": "Is a model actually needed when the segments are this visible?",
                    "paragraphs": [
                        "Fair challenge: with contract type and payment method this predictive, a simple segment table gets a team most of the way. What the model adds is the individual ranking inside the noisy middle, where a customer has a mix of signals: month-to-month but two years of tenure, fiber but automatic payment, low add-ons but a partner on file.",
                        "My logistic regression uses 19 features: three numeric (tenure, monthly and total charges) and sixteen one-hot encoded categoricals, trained with 5-fold cross-validation on ROC-AUC. Cross-validation lands at 0.842 with a standard deviation of 0.007, and the held-out test set scores 0.858, so generalisation is real rather than a split artefact.",
                        "I chose logistic regression deliberately over a flashier classifier: every coefficient is inspectable, the probability is calibrated enough to threshold, and the whole pipeline trains in seconds, which matters when a retention team wants monthly rescoring, not a research project.",
                    ],
                    "meaning": "The model is the ranking layer on top of segment knowledge, and a simple, inspectable one is a feature for a business process, not a compromise.",
                    "conclusion": "Deploy the score as a ranked worklist for the retention team, led by month-to-month customers.",
                    "figure": ("CustomerChurn_2", "The served API's Swagger page: the /predict endpoint a real system would call, with the input schema visible."),
                },
            ]},
        ]},
        {"id": "recommendations", "heading": "What I would do next", "blocks": [
            {"type": "recs", "items": [
                {"priority": "High", "title": "Work the ranked list top-down, not the whole base",
                 "evidence": "1,869 churned-profile customers at $139,131 monthly billing, and contract type separating churn risk by 15-fold.",
                 "action": "Score the base monthly, start outreach at the top of the ranked list among month-to-month customers, and stop treating the 26.5% at-risk share as one undifferentiated pool.",
                 "impact": "Puts limited retention budget where the contract structure and the score both say the risk is."},
                {"priority": "High", "title": "Make contract conversion the primary offer",
                 "evidence": "42.7% month-to-month churn versus 2.8% on two-year terms, the strongest pattern in the data.",
                 "action": "Lead with term-conversion incentives for high-scoring month-to-month customers before discounting or upgrades.",
                 "impact": "Attacks the mechanism the data actually shows, instead of the symptoms around it."},
                {"priority": "Medium", "title": "Migrate e-check payers to automatic payments",
                 "evidence": "45.3% churn among electronic-check payers against 15.2% to 16.7% for automatic methods, on a 34% share of the base.",
                 "action": "Run a migration campaign for e-check customers with a small incentive, and measure churn in the migrated cohort against a hold-out.",
                 "impact": "A cheap, testable intervention on the single most friction-heavy segment."},
                {"priority": "Medium", "title": "Bundle the low-adoption protective services",
                 "evidence": "Tech support and online security adoption both at 29% against 90% phone-service uptake, with fiber churn at 41.9%.",
                 "action": "Package security and support add-ons into the fiber pitch for new and at-risk customers, and track adoption as the leading indicator it behaves like.",
                 "impact": "Raises the engagement signals that precede churn, on the tier that churns hardest."},
                {"priority": "Low", "title": "Rebuild the API's input contract to match the model",
                 "evidence": "My served /predict endpoint accepts 4 fields while the model was trained on 19, so missing features silently default to zero.",
                 "action": "Expand the CustomerInput schema to the full 19-feature contract before any real integration leans on the API.",
                 "impact": "Removes a silent-accuracy gap between the validated model and the served one."},
                {"priority": "Low", "title": "Improve the model's weakest records honestly",
                 "evidence": "The 11 blank totalcharges rows were filled with 0, which distorts brand-new customers the model most needs to score well.",
                 "action": "Impute from tenure-based expectations rather than zero, and re-validate; also tune the 0.5 threshold against the actual cost of a wasted offer versus a lost customer.",
                 "impact": "Tightens exactly the low-tenure edge of the score where the money concentrates."},
            ]},
        ]},
        {"id": "limits", "heading": "What this can't tell you", "blocks": [
            {"type": "p", "items": [
                "The dataset is the public Kaggle telco churn table. It is real-world-shaped and widely benchmarked, but it describes one provider at one snapshot, so the coefficients belong to this table rather than to telecom in general.",
                "ROC-AUC 0.858 is a ranking quality. It does not say the model is right about any individual customer, and the classes are imbalanced 74/26, so a raw accuracy number would flatter it. Ranking is the honest metric here.",
                "The churn causes are inferred, not observed. The dataset has no cancellation interviews, so e-check friction and fiber expectation gaps are readings of patterns, not documented reasons.",
                "The revenue projections in my README ($420K to $1.26M saved, ROI scenarios) are business-case modelling with stated assumptions, not measurements. They assume retention offers convert at 40 to 50% and each save is worth about $1,400 a year. Treat them as a frame for the decision, not as results.",
                "The served API currently scores on 4 of the 19 features the model trained on; predictions through it are not the validated model's output. I say that plainly rather than letting the Swagger page imply otherwise.",
            ]},
        ]},
    ],
}


# --------------------------------------------------------------- technical
TECHNICAL = {
    "title": "Customer Churn Prediction: how I built it",
    "lede": "The engineering behind the score: the pipeline from raw CSV to pickled artifact, the logistic regression and its cross-validation, the serving layer with the schema decision I would redo, and every number on these pages traced to a re-run.",
    "sections": [
        {"id": "solution", "heading": "The solution", "blocks": [
            {"type": "note", "text": "Every metric on this page comes from re-running my own pipeline against the shipped CSV, plus the source files themselves. The final model is a logistic regression, not the XGBoost an earlier description of this project mentioned; the shipped repository contains only the logistic regression path."},
            {"type": "table", "headers": ["Component", "What I built it from", "Role"], "rows": [
                ["Telco-Customer-Churn.csv", "7,043 rows, 21 columns", "One row per customer: demographics, services, contract, billing, churn flag"],
                ["Churn.py", "pandas + scikit-learn, 112 lines", "The full training pipeline: cleaning, splitting, cross-validation, final fit, pickle export"],
                ["model_C=1.0.bin", "pickled DictVectorizer + LogisticRegression", "One artifact carrying both the transformation and the model, so inference needs no retraining logic"],
                ["predict.py", "FastAPI", "The /predict endpoint with a Pydantic input schema and Swagger docs"],
                ["Retention dashboard", "Excel, separate case study", "The executive view of the same dataset, reconciled row-for-row"],
            ]},
            {"type": "p", "text": "The design principle I care about in this build is that preprocessing and model ship as one pickle. The DictVectorizer learned its vocabulary from training data; freezing them together is what stops the serving path from inventing its own idea of what a categorical value means."},
        ]},
        {"id": "prep", "heading": "Data preparation, as I ran it", "blocks": [
            {"type": "steps", "items": [
                ("Normalise columns", "All column names lowercased and underscored, then every categorical value lowercased and space-stripped, so one-hot encoding produces stable feature names."),
                ("Coerce and impute", "TotalCharges arrives with 11 whitespace-only values; I coerced to numeric and filled with 0. That choice is documented in my README as a known limitation: zero implies no billing history, which bends predictions for exactly the brand-new customers the model most needs to rank."),
                ("Encode the target", "Churn converted from yes/no strings to 1/0 integers."),
                ("Split before anything else", "An 80/20 train-test split with random_state 1 gives 5,634 training and 1,409 test rows. The test set is touched exactly once, at the end."),
            ]},
            {"type": "code", "title": "The preparation core", "lang": "python", "code": '''
df.columns = df.columns.str.lower().str.replace(' ', '_')
for col in cat_col:
    df[col] = df[col].str.lower().str.replace(' ', '_')
df.totalcharges = pd.to_numeric(df.totalcharges, errors='coerce')
df.totalcharges = df.totalcharges.fillna(0)
df.churn = (df.churn == 'yes').astype(int)
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
'''},
            {"type": "p", "text": "The feature set is 3 numerical columns (tenure, monthlycharges, totalcharges) and 16 categoricals covering demographics, services and account configuration. DictVectorizer one-hot encodes the categoricals and passes the numerics straight through, dense output."},
        ]},
        {"id": "model", "heading": "The model and its validation", "blocks": [
            {"type": "p", "text": "Logistic regression with C=1.0 and max_iter=5000. The iteration cap is not cosmetic: my notebook first ran with 1,000 and threw convergence warnings, so the production script raises it to 5,000, which my README records along with the honest note that feature scaling is the better fix."},
            {"type": "code", "title": "Training and validation", "lang": "python", "code": '''
def train(df_train, y_train, C=1.0):
    dicts = df_train[categorical + numerical].to_dict(orient='records')
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)
    model = LogisticRegression(C=C, max_iter=5000)
    model.fit(X_train, y_train)
    return dv, model

kfold = KFold(n_splits=5, shuffle=True, random_state=1)
scores = [roc_auc_score(y_val, predict(df_val, dv, model))
          for train_idx, val_idx in kfold.split(df_full_train)]
'''},
            {"type": "table", "headers": ["Metric", "Value", "Where it comes from"], "rows": [
                ["Fold AUCs", "0.8444 / 0.8452 / 0.8336 / 0.8348 / 0.8518", "My re-run, identical to the README's folds to rounding"],
                ["Cross-validation", "0.842 +/- 0.007", "Mean and standard deviation across the 5 folds"],
                ["Test AUC", "0.858", "Single scoring of the untouched 1,409-row hold-out"],
                ["Overfitting gap", "0.016", "Test minus CV mean; small, so I trust the generalisation"],
            ]},
            {"type": "p", "text": "I report ROC-AUC rather than accuracy throughout, and the class balance is why: 74/26 means a model predicting nobody churns scores 74% accuracy while being useless. AUC measures whether the model ranks churners above non-churners, which is the property a ranked worklist needs. My README's 85.8% accuracy phrasing is this same AUC wearing the wrong name."},
        ]},
        {"id": "serving", "heading": "Serving: the part I would partially redo", "blocks": [
            {"type": "p", "text": "The serving layer is FastAPI with a Pydantic schema, not the Flask my technical README describes; the code and the Swagger screenshot show FastAPI, and the README predates the rewrite. Swagger UI comes free with FastAPI, which is what my second screenshot shows."},
            {"type": "code", "title": "The endpoint", "lang": "python", "code": '''
class CustomerInput(BaseModel):
    tenure: int
    monthly_charges: float
    total_charges: float
    contract: str

@app.post("/predict")
def predict(customer: CustomerInput):
    X = dv.transform([customer.dict()])
    y_pred = model.predict_proba(X)[0, 1]
    return {"churn_probability": float(y_pred), "churn": y_pred >= 0.5}
'''},
            {"type": "p", "items": [
                "Now the honest engineering note, and it is the most instructive thing on this page: the CustomerInput schema accepts 4 fields, but the model trained on 19. DictVectorizer treats missing keys as absent features, which encode as zeros, so the API runs without error and silently scores each customer as if they had no gender, no services, no payment method and no internet type.",
                "That is not a crash, it is worse: it is a prediction that looks confident and is not the one the validated model would give. I built the 4-field schema to make the demo readable in Swagger, and the full-featured version is the first item on my redo list. Any production integration would need the 19-field contract with the same names the DictVectorizer was fitted on.",
                "The threshold is a flat 0.5. That is the right default for a demo and the wrong default for a retention budget, where the cost of a wasted offer and the cost of a lost customer are not symmetric, and the threshold should be tuned to that trade-off.",
            ]},
            {"type": "pairs", "items": [
                ("One pickle, two objects", "The vectorizer and model serialize together, so the serving path cannot desynchronise from the training path."),
                ("Validation before the final fit", "Cross-validation runs on the training split only; the test set is scored once, after the final model is trained on the full training split."),
                ("Fixed random_state", "Split and folds both seed at 1, so every number on these pages is reproducible bit-for-bit."),
            ]},
        ]},
        {"id": "quality", "heading": "Verification: my numbers versus my code", "blocks": [
            {"type": "p", "text": "I re-ran the whole pipeline independently and compared it against what my README claims. This is the table I wish every ML writeup shipped with:"},
            {"type": "table", "headers": ["Claim", "Re-run result", "Verdict"], "rows": [
                ["CV AUC 0.842 +/- 0.007", "0.842 +/- 0.007, folds matching to 4 decimals", "Reproduces exactly"],
                ["Test AUC 0.858", "0.8585", "Reproduces"],
                ["7,043 rows, 21 columns", "7,043 x 21", "Exact"],
                ["1,869 churners, 26.5%", "1,869 / 26.54%", "Exact"],
                ["5,634 / 1,409 split", "5,634 / 1,409", "Exact"],
                ["85.8% accuracy", "ROC-AUC 0.858, not accuracy", "Label corrected in these pages"],
                ["$2.86M yearly revenue at stake", "Cumulative lifetime charges of the churned segment; monthly run-rate $139,131", "Label corrected in these pages"],
            ]},
            {"type": "note", "text": "Two of my own labels needed correcting, and I would rather show the comparison than quietly fix them. The model numbers were always right; the names attached to two of them were loose."},
        ]},
        {"id": "decisions", "heading": "My decisions and trade-offs", "blocks": [
            {"type": "table", "headers": ["Decision I made", "Why", "Trade-off I accepted"], "rows": [
                ["Logistic regression over boosted trees", "Inspectability and retrain speed for a monthly business process", "Leaves AUC on the table; an XGBoost benchmark is the obvious next experiment"],
                ["AUC as the only reported metric", "Class imbalance makes raw accuracy misleading", "A stakeholder used to accuracy percentages needs the ranking framing explained"],
                ["fillna(0) for TotalCharges", "Simple, explicit, and only 11 rows", "Systematically under-states brand-new customers; median-by-tenure is the better imputation"],
                ["FastAPI over Flask for serving", "Pydantic validation and Swagger docs without extra code", "My README drifted from the code until this documentation; process lesson logged"],
                ["Shipped a 4-field demo schema", "Readable Swagger demo", "Silent feature truncation at inference; must be expanded before real use"],
                ["Threshold left at 0.5", "Neutral default while metrics are validated", "Not tuned to offer-cost economics, which is where the business value actually lands"],
            ]},
        ]},
        {"id": "next", "heading": "If I took it further", "blocks": [
            {"type": "steps", "items": [
                ("Fix the serving contract", "Expand CustomerInput to the full 19 features and add a contract test that scores a fixed customer record and compares against the offline model, so drift becomes loud instead of silent."),
                ("Tune the threshold to the economics", "Parameterise offer cost and customer value, then choose the probability cutoff that maximises expected savings rather than a default 0.5."),
                ("Fix the imputation", "Fill the 11 blank TotalCharges from a tenure-based expectation, and re-validate whether the low-tenure scores improve."),
                ("Benchmark tree models", "Run gradient boosting through the same CV harness as a benchmark, and keep logistic regression if the AUC gap does not buy its interpretability cost."),
                ("Explain individual scores", "Attach per-customer feature contributions (SHAP or coefficient inspection) to the ranked worklist, so an agent sees why a customer scored high before calling them."),
            ]},
        ]},
        {"id": "reflection", "heading": "What this project shows", "blocks": [
            {"type": "p", "items": [
                "The build is deliberately boring in the best way: a linear model, a frozen vectorizer, a single artifact, and a validation harness that any teammate can re-run in seconds. Boring is what makes a scoring process maintainable.",
                "The habits this project gave me: report the metric that matches the decision the model feeds, validate before the final fit and touch the test set once, re-run your own claims against your own code before publishing them, and when a serving schema drifts from a training schema, treat it as a defect rather than a demo convenience.",
            ]},
        ]},
    ],
}
