import pandas as pd

# Load Financial DNA dataset
df = pd.read_csv("data/financial_dna.csv")

# Function to calculate stressed health score
def calculate_stressed_health(income, expenses, debt_score):

    savings = (income - expenses).clip(lower=0)

    savings_rate = (savings / income) * 100

    savings_score = savings_rate.clip(0, 50) * 2

    emergency_fund_months = savings / expenses

    emergency_fund_score = (
        emergency_fund_months.clip(0, 6) / 6
    ) * 100

    health_score = (
        savings_score * 0.4
        + debt_score * 0.3
        + emergency_fund_score * 0.3
    )

    return health_score


# -----------------------------
# Scenario 1: Income -20%
# -----------------------------

scenario_1_income = df["monthly_income"] * 0.80
scenario_1_expenses = df["monthly_expenses"]

df["income_drop_score"] = calculate_stressed_health(
    scenario_1_income,
    scenario_1_expenses,
    df["debt_score"]
)


# -----------------------------
# Scenario 2: Expenses +20%
# -----------------------------

scenario_2_income = df["monthly_income"]
scenario_2_expenses = df["monthly_expenses"] * 1.20

df["expense_increase_score"] = calculate_stressed_health(
    scenario_2_income,
    scenario_2_expenses,
    df["debt_score"]
)


# -----------------------------
# Scenario 3: Income -20%
# AND Expenses +20%
# -----------------------------

scenario_3_income = df["monthly_income"] * 0.80
scenario_3_expenses = df["monthly_expenses"] * 1.20

df["combined_stress_score"] = calculate_stressed_health(
    scenario_3_income,
    scenario_3_expenses,
    df["debt_score"]
)


# -----------------------------
# Display Results
# -----------------------------

print("===== Multiple Stress Scenarios =====")

print(df[[
    "user_id",
    "financial_health_score",
    "income_drop_score",
    "expense_increase_score",
    "combined_stress_score"
]].head(10))