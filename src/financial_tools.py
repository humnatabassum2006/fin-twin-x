# =========================================================
# FINANCIAL CALCULATION TOOLS
# =========================================================


def calculate_savings_rate(income, savings):
    """
    Calculate savings rate as a percentage.
    """

    if income <= 0:
        return 0

    savings_rate = (savings / income) * 100

    return savings_rate

def calculate_debt_to_income(income, debt):
    """
    Calculate debt-to-income ratio as a percentage.
    """

    if income <= 0:
        return 0

    debt_to_income = (debt / income) * 100

    return debt_to_income

def calculate_emergency_fund_months(savings, expenses):
    """
    Calculate how many months of expenses
    can be covered by current savings.
    """

    if expenses <= 0:
        return 0

    emergency_fund_months = savings / expenses

    return emergency_fund_months

def calculate_financial_health_score(
    savings_score,
    debt_score,
    emergency_fund_score
):
    """
    Calculate overall financial health score.
    """

    financial_health_score = (
        savings_score * 0.4
        + debt_score * 0.3
        + emergency_fund_score * 0.3
    )

    return financial_health_score

# =========================================================
# TEST THE TOOL
# =========================================================

if __name__ == "__main__":

    income = 150000
    savings = 60000

    result = calculate_savings_rate(
        income,
        savings
    )

    print("Income:", income)
    print("Savings:", savings)
    print("Savings Rate:", round(result, 2), "%")
