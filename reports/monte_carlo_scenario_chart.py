import numpy as np
import matplotlib.pyplot as plt

# Starting financial values
monthly_income = 150000
monthly_expenses = 90000

# Number of simulations
simulations = 10000

# Reproducible results
np.random.seed(42)

# -----------------------------
# NORMAL SCENARIO
# -----------------------------

normal_income = np.random.normal(
    monthly_income,
    monthly_income * 0.05,
    simulations
)

normal_savings = np.maximum(
    normal_income - monthly_expenses,
    0
)


# -----------------------------
# INCOME STRESS
# Income decreases by 20%
# -----------------------------

stress_income = np.random.normal(
    monthly_income * 0.80,
    monthly_income * 0.10,
    simulations
)

stress_savings = np.maximum(
    stress_income - monthly_expenses,
    0
)


# -----------------------------
# COMBINED STRESS
# Income -20%
# Expenses +20%
# -----------------------------

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


# -----------------------------
# Calculate average savings
# -----------------------------

average_savings = [
    normal_savings.mean(),
    stress_savings.mean(),
    combined_savings.mean()
]

scenario_names = [
    "Normal",
    "Income Stress",
    "Combined Stress"
]


# -----------------------------
# Create comparison chart
# -----------------------------

plt.figure(figsize=(9, 6))

plt.bar(
    scenario_names,
    average_savings
)

plt.title("Monte Carlo Scenario Comparison")
plt.xlabel("Scenario")
plt.ylabel("Average Monthly Savings")

plt.savefig(
    "reports/monte_carlo_scenario_comparison.png"
)

print("Scenario comparison chart created successfully!")
print("Chart saved in reports folder.")