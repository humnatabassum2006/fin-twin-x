import numpy as np

# Starting financial values
monthly_income = 150000
monthly_expenses = 90000

# Number of simulations
simulations = 10000

# Random seed for reproducible results
np.random.seed(42)

# Generate possible income changes
income_changes = np.random.normal(
    loc=0,
    scale=0.10,
    size=simulations
)

# Simulated future incomes
simulated_income = (
    monthly_income * (1 + income_changes)
)

# Calculate simulated savings
simulated_savings = (
    simulated_income - monthly_expenses
)

# Savings cannot be negative
simulated_savings = np.maximum(
    simulated_savings,
    0
)

# Calculate average simulated savings
average_savings = simulated_savings.mean()

# Calculate probability of having zero savings
zero_savings_probability = (
    (simulated_savings == 0).mean() * 100
)

print("===== MONTE CARLO SIMULATION =====")

print("Number of Simulations:", simulations)

print(
    "Average Simulated Monthly Savings:",
    round(average_savings, 2)
)

print(
    "Probability of Zero Savings:",
    round(zero_savings_probability, 2),
    "%"
)