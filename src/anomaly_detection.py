import pandas as pd
from sklearn.ensemble import IsolationForest

# Load financial data
df = pd.read_csv("data/financial_dna.csv")

# Features for anomaly detection
features = [
    "monthly_income",
    "monthly_expenses",
    "monthly_savings",
    "debt",
    "savings_rate",
    "debt_to_income",
    "emergency_fund_months"
]

X = df[features]

# Create Isolation Forest model
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

# Detect anomalies
df["anomaly"] = model.fit_predict(X)

# Convert result into readable labels
df["anomaly_status"] = df["anomaly"].map({
    1: "Normal",
    -1: "Anomaly"
})

# Count results
anomaly_summary = df["anomaly_status"].value_counts()

print("===== FINANCIAL ANOMALY DETECTION =====")

print("\nAnomaly Summary:")
print(anomaly_summary)

# Show detected anomalies
anomalies = df[
    df["anomaly_status"] == "Anomaly"
]

print("\nDetected Anomalies:")
print(
    anomalies[[
        "user_id",
        "monthly_income",
        "monthly_expenses",
        "monthly_savings",
        "debt",
        "debt_to_income",
        "anomaly_status"
    ]].head(10)
)