import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load ML dataset
df = pd.read_csv("data/ml_dataset.csv")

# Features
features = [
    "monthly_income",
    "monthly_expenses",
    "monthly_savings",
    "debt",
    "savings_rate",
    "debt_to_income",
    "emergency_fund_months",
    "savings_score",
    "debt_score",
    "emergency_fund_score"
]

# Input (X) and target (y)
X = df[features]
y = df["financial_health_score"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Machine Learning model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("===== Financial Health ML Model =====")
print("Training Users:", len(X_train))
print("Testing Users:", len(X_test))
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))
# Feature Importance
importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n===== Feature Importance =====")
print(importance)