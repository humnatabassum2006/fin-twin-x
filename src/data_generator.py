import pandas as pd
import numpy as np

np.random.seed(42)

users = []

for i in range(1000):

    # Monthly income
    monthly_income = np.random.randint(40000, 300000)

    # Different spending patterns
    expense_ratio = np.random.uniform(0.40, 0.90)

    monthly_expenses = int(
        monthly_income * expense_ratio
    )

    # Monthly savings
    monthly_savings = max(
        monthly_income - monthly_expenses,
        0
    )

    # Emergency fund balance
    # Different users have different levels of preparedness
    emergency_fund_multiplier = np.random.uniform(0, 8)

    emergency_fund_savings = (
        monthly_expenses * emergency_fund_multiplier
    )

    # Debt
    debt = np.random.randint(0, 200000)

    users.append({
        "user_id": i + 1,
        "monthly_income": monthly_income,
        "monthly_expenses": monthly_expenses,
        "monthly_savings": monthly_savings,
        "emergency_fund_savings": emergency_fund_savings,
        "debt": debt
    })


df = pd.DataFrame(users)

# Save raw financial dataset
df.to_csv(
    "data/users.csv",
    index=False
)

print("Dataset created successfully!")
print(df.head())

print(f"Total users: {len(df)}")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())

print(
    "Average income:",
    round(df["monthly_income"].mean(), 2)
)