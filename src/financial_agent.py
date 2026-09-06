import pandas as pd

from src.agent_tools import TOOLS


# =========================================================
# LOAD FINANCIAL DATA
# =========================================================

df = pd.read_csv("data/financial_dna_profiles.csv")


# =========================================================
# SELECT USER
# =========================================================

selected_user = df.iloc[0]


# =========================================================
# FINANCIAL AGENT
# =========================================================

def financial_agent(user):

    health_score = TOOLS["calculate_financial_health_score"](
        user["savings_score"],
        user["debt_score"],
        user["emergency_fund_score"]
    )

    savings_rate = TOOLS["calculate_savings_rate"](
        user["monthly_income"],
        user["monthly_savings"]
    )

    debt_to_income = TOOLS["calculate_debt_to_income"](
        user["monthly_income"],
        user["debt"]
    )

    emergency_fund = TOOLS["calculate_emergency_fund_months"](
        user["monthly_savings"],
        user["monthly_expenses"]
    )

    print("========================================")
    print("          FINANCIAL AI AGENT")
    print("========================================")

    print("User ID:", user["user_id"])
    print("Financial Health Score:", round(health_score, 2))

    print("\nAgent Analysis:")

    if health_score >= 70:
        print("Overall financial health is strong.")

    elif health_score >= 40:
        print("Overall financial health is moderate.")

    else:
        print("Overall financial health needs improvement.")


    # =====================================================
    # RECOMMENDATIONS
    # =====================================================

    recommendations = []

    if savings_rate < 20:
        recommendations.append(
            "Increase your savings rate."
        )

    if debt_to_income > 40:
        recommendations.append(
            "Focus on reducing debt."
        )

    if emergency_fund < 3:
        recommendations.append(
            "Build an emergency fund."
        )

    if (
        savings_rate >= 20
        and debt_to_income <= 40
        and emergency_fund >= 3
    ):
        recommendations.append(
            "Continue maintaining good financial habits."
        )


    # =====================================================
    # STRUCTURED AGENT OUTPUT
    # =====================================================

    return {
        "user_id": user["user_id"],
        "health_score": round(health_score, 2),
        "savings_rate": round(savings_rate, 2),
        "debt_to_income": round(debt_to_income, 2),
        "emergency_fund": round(emergency_fund, 2),
        "status": (
            "Healthy"
            if health_score >= 70
            else "Moderate"
            if health_score >= 40
            else "Financially Stressed"
        ),
        "recommendations": recommendations
    }


# =========================================================
# RUN AGENT
# =========================================================

if __name__ == "__main__":
    result = financial_agent(selected_user)

    print("\nReturned Agent Result:")

    print(result)

    print("\nFinancial AI Agent analysis completed successfully!")