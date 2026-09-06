import numpy as np

# Starting financial values
monthly_income = 150000
monthly_expenses = 90000

# Number of simulations
simulations = 10000

# Reproducible results
np.random.seed(42)

# Income uncertainty
income_changes = np.random.normal(
    loc=0,
    scale=0.10,
    size=simulations
)

# Simulated future income
simulated_income = (
    monthly_income * (1 + income_changes)
)

# Simulated savings
simulated_savings = (
    simulated_income - monthly_expenses
)

# Savings cannot be negative
simulated_savings = np.maximum(
    simulated_savings,
    0
)

# -----------------------------
# Probability Analysis
# -----------------------------

# Probability of zero savings
zero_savings_probability = (
    (simulated_savings == 0).mean() * 100
)

# Probability of savings below 30,000
low_savings_probability = (
    (simulated_savings < 30000).mean() * 100
)

# Probability of savings above 50,000
healthy_savings_probability = (
    (simulated_savings >= 50000).mean() * 100
)

# -----------------------------
# Display Results
# -----------------------------

print("===== MONTE CARLO PROBABILITY ANALYSIS =====")

print(
    "Probability of Zero Savings:",
    round(zero_savings_probability, 2),
    "%"
)

print(
    "Probability of Savings Below 30,000:",
    round(low_savings_probability, 2),
    "%"
)

print(
    "Probability of Savings >= 50,000:",
    round(healthy_savings_probability, 2),
    "%"
)