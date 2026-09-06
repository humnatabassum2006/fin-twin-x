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


# Scenario 1: Income decreases by 20%
income_drop_score = calculate_stressed_health(
    df["monthly_income"] * 0.80,
    df["monthly_expenses"],
    df["debt_score"]
)


# Scenario 2: Expenses increase by 20%
expense_increase_score = calculate_stressed_health(
    df["monthly_income"],
    df["monthly_expenses"] * 1.20,
    df["debt_score"]
)


# Scenario 3: Income decreases by 20%
# and expenses increase by 20%
combined_stress_score = calculate_stressed_health(
    df["monthly_income"] * 0.80,
    df["monthly_expenses"] * 1.20,
    df["debt_score"]
)


# Calculate average scores
normal_average = df["financial_health_score"].mean()
income_drop_average = income_drop_score.mean()
expense_increase_average = expense_increase_score.mean()
combined_stress_average = combined_stress_score.mean()


# Display comparison
print("===== Scenario Comparison =====")

print(
    "Normal Average Health Score:",
    round(normal_average, 2)
)

print(
    "Income -20% Average Score:",
    round(income_drop_average, 2)
)

print(
    "Expenses +20% Average Score:",
    round(expense_increase_average, 2)
)

print(
    "Combined Stress Average Score:",
    round(combined_stress_average, 2)
)


# Find the most damaging scenario
scores = {
    "Income -20%": income_drop_average,
    "Expenses +20%": expense_increase_average,
    "Combined Stress": combined_stress_average
}

most_damaging_scenario = min(
    scores,
    key=scores.get
)

print(
    "\nMost Damaging Scenario:",
    most_damaging_scenario
)