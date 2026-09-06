import numpy as np

# Starting financial values
monthly_income = 150000
monthly_expenses = 90000

# Number of simulations
simulations = 10000

# Same random results every time
np.random.seed(42)

# ---------------------------------
# SCENARIO 1: NORMAL
# ---------------------------------

normal_income = np.random.normal(
    monthly_income,
    monthly_income * 0.05,
    simulations
)

normal_savings = np.maximum(
    normal_income - monthly_expenses,
    0
)


# ---------------------------------
# SCENARIO 2: INCOME STRESS
# Income decreases by around 20%
# ---------------------------------

stress_income = np.random.normal(
    monthly_income * 0.80,
    monthly_income * 0.10,
    simulations
)

stress_savings = np.maximum(
    stress_income - monthly_expenses,
    0
)


# ---------------------------------
# SCENARIO 3: COMBINED STRESS
# Income -20%
# Expenses +20%
# ---------------------------------

combined_income = np.random.normal(
    monthly_income * 0.80,
    monthly_income * 0.10,
    simulations
)

combined_expenses = np.random.normal(
    monthly_expenses * 1.20,
    monthly_expenses * 0.05,
    simulations
)

combined_savings = np.maximum(
    combined_income - combined_expenses,
    0
)


# ---------------------------------
# RESULTS
# ---------------------------------

print("===== MONTE CARLO SCENARIO ANALYSIS =====")

print("\nNormal Scenario")
print(
    "Average Savings:",
    round(normal_savings.mean(), 2)
)

print("\nIncome Stress Scenario")
print(
    "Average Savings:",
    round(stress_savings.mean(), 2)
)

print("\nCombined Stress Scenario")
print(
    "Average Savings:",
    round(combined_savings.mean(), 2)
)

# Probability of zero savings
print("\n===== ZERO SAVINGS PROBABILITY =====")

print(
    "Normal:",
    round((normal_savings == 0).mean() * 100, 2),
    "%"
)

print(
    "Income Stress:",
    round((stress_savings == 0).mean() * 100, 2),
    "%"
)

print(
    "Combined Stress:",
    round((combined_savings == 0).mean() * 100, 2),
    "%"
)