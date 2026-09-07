import streamlit as st
import pandas as pd
import numpy as np
from src.financial_agent import financial_agent
from src.rag_retriever import retrieve_knowledge
from src.semantic_rag import semantic_search
from src.llm_agent import generate_ai_answer
from src.llm_agent import build_ai_prompt
from sklearn.ensemble import IsolationForest


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="FinTwin-X",
    page_icon="💰",
    layout="wide"
)


# =========================================================
# LOAD FINANCIAL DNA DATA
# =========================================================

df = pd.read_csv("data/financial_dna_profiles.csv")


# =========================================================
# DASHBOARD TITLE
# =========================================================

st.title("💰 FinTwin-X")

st.subheader(
    "AI Financial Digital Twin & Probabilistic Stress-Testing Engine"
)

st.caption(
    "AI-powered financial health, risk analysis, and stress testing."
)

st.divider()

# =========================================================
# KEY FINANCIAL METRICS
# =========================================================

st.write("### 📊 Key Financial Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Total Users",
        len(df)
    )

with col2:
    st.metric(
        "❤️ Average Health Score",
        round(df["financial_health_score"].mean(), 2)
    )

with col3:
    st.metric(
        "💰 Strong Savers",
        (df["savings_profile"] == "Strong Saver").sum()
    )

with col4:
    st.metric(
        "💳 High Debt Users",
        (df["debt_profile"] == "High Debt").sum()
    )

st.divider()


# =========================================================
# USER SELECTION
# =========================================================

st.header("👤 User Financial Profile")

st.write(
    "Select a simulated user to explore their financial profile, "
    "Financial DNA, health score, risk, and stress-test results."
)

selected_user_id = st.selectbox(
    "Choose User ID",
    df["user_id"].tolist()
)

selected_user = df[
    df["user_id"] == selected_user_id
].iloc[0]

# =========================================================
# SELECTED USER FINANCIAL INFORMATION
# =========================================================

st.write("### 💼 Selected User Financial Overview")

st.caption(
    "Monthly financial position of the selected simulated user."
)

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💵 Monthly Income",
        f"Rs. {selected_user['monthly_income']:,.0f}"
    )

with col2:
    st.metric(
        "💸 Monthly Expenses",
        f"Rs. {selected_user['monthly_expenses']:,.0f}"
    )

with col3:
    st.metric(
        "💰 Monthly Savings",
        f"Rs. {selected_user['monthly_savings']:,.0f}"
    )

with col4:
    st.metric(
        "💳 Debt",
        f"Rs. {selected_user['debt']:,.0f}"
    )


# =========================================================
# FINANCIAL DNA
# =========================================================

st.write("### 🧬 Financial DNA")

st.caption(
    "A quick profile of the selected user's financial behavior "
    "across savings, debt, emergency preparedness, and overall health."
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("**💰 Savings Profile**")
    st.info(selected_user["savings_profile"])

with col2:
    st.write("**💳 Debt Profile**")
    st.info(selected_user["debt_profile"])

with col3:
    st.write("**🛡️ Emergency Fund**")
    st.info(selected_user["emergency_fund_profile"])

with col4:
    st.write("**❤️ Overall Health**")
    st.info(selected_user["health_profile"])


# =========================================================
# FINANCIAL HEALTH SCORE
# =========================================================

health_score = selected_user["financial_health_score"]

st.write("### 📊 Financial Health")

st.caption(
    "Overall financial health score based on savings, debt management, "
    "and emergency fund strength."
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "❤️ Financial Health Score",
        f"{health_score:.2f} / 100"
    )

with col2:
    if health_score >= 70:
        health_status = "Healthy 🟢"
    elif health_score >= 40:
        health_status = "Moderate 🟡"
    else:
        health_status = "Needs Improvement 🔴"

    st.metric(
        "Health Status",
        health_status
    )

st.progress(
    min(int(health_score), 100)
)


# =========================================================
# RISK CATEGORY
# =========================================================

if health_score >= 70:
    risk_category = "Low Risk 🟢"

elif health_score >= 40:
    risk_category = "Medium Risk 🟡"

else:
    risk_category = "High Risk 🔴"

st.write("### ⚠️ Risk Status")

st.caption(
    "Current risk classification based on the user's financial health score."
)

st.info(
    f"⚠️ **Current Risk Category:** {risk_category}"
)

st.divider()

# =========================================================
# EXPLAINABLE AI (XAI)
# =========================================================

st.write("### 🧠 Explainable AI — Why This Score?")

st.caption(
    "Understand which financial factors contribute most to "
    "the selected user's Financial Health Score."
)

savings_contribution = (
    selected_user["savings_score"] * 0.4
)

debt_contribution = (
    selected_user["debt_score"] * 0.3
)

emergency_contribution = (
    selected_user["emergency_fund_score"] * 0.3
)

contributions = {
    "Savings": savings_contribution,
    "Debt": debt_contribution,
    "Emergency Fund": emergency_contribution
}

most_important_factor = max(
    contributions,
    key=contributions.get
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💰 Savings Contribution",
        f"{savings_contribution:.2f}"
    )

with col2:
    st.metric(
        "💳 Debt Contribution",
        f"{debt_contribution:.2f}"
    )

with col3:
    st.metric(
        "🛡️ Emergency Fund Contribution",
        f"{emergency_contribution:.2f}"
    )

st.info(
    f"🔎 **Most Important Factor:** {most_important_factor}\n\n"
    "This factor has the largest contribution to the user's "
    "current Financial Health Score."
)

st.divider()

# =========================================================
# FINANCIAL RECOMMENDATION
# =========================================================

st.write("### 💡 Personalized Financial Recommendation")

st.caption(
    "A personalized recommendation based on the selected "
    "user's savings, debt, and emergency-fund position."
)

if selected_user["emergency_fund_months"] < 3:
    st.warning(
        "🛡️ **Priority: Build Your Emergency Fund**\n\n"
        "Your emergency fund is below 3 months of expenses. "
        "Prioritize building a financial safety buffer before "
        "taking unnecessary financial risks."
    )

elif selected_user["debt_to_income"] > 40:
    st.warning(
        "💳 **Priority: Reduce Debt**\n\n"
        "Your debt-to-income ratio is high. Focus on reducing "
        "existing debt and avoid unnecessary borrowing."
    )

elif selected_user["savings_rate"] < 20:
    st.info(
        "💰 **Priority: Increase Savings**\n\n"
        "Your savings rate is below 20%. Try to gradually "
        "increase your monthly savings and control unnecessary spending."
    )

else:
    st.success(
        "🌟 **Your Financial Position Looks Healthy**\n\n"
        "Your main financial indicators are in a healthy range. "
        "Continue maintaining good savings, manageable debt, "
        "and sufficient emergency savings."
    )

st.divider()

# =========================================================
# AI FINANCIAL AGENT
# =========================================================

st.write("### 🤖 AI Financial Agent")

st.caption(
    "AI-powered analysis of the selected user's financial health, "
    "risk indicators, and personalized recommendations."
)

agent_result = financial_agent(selected_user)

st.write("#### 📊 AI Agent Financial Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "❤️ Health Score",
        f"{agent_result['health_score']:.2f}"
    )

with col2:
    st.metric(
        "💰 Savings Rate",
        f"{agent_result['savings_rate']:.2f}%"
    )

with col3:
    st.metric(
        "💳 Debt-to-Income",
        f"{agent_result['debt_to_income']:.2f}%"
    )

with col4:
    st.metric(
        "🛡️ Emergency Fund",
        f"{agent_result['emergency_fund']:.2f} months"
    )


st.write("#### 💡 Personalized Agent Recommendations")

if agent_result["recommendations"]:

    for recommendation in agent_result["recommendations"]:
        st.info(f"💡 {recommendation}")

else:

    st.info(
        "No specific recommendation was generated."
    )


st.write("### 🎯 Overall AI Agent Recommendation")

if agent_result["status"] == "Healthy":

    st.success(
        "🌟 **Healthy Financial Position**\n\n"
        "Continue maintaining strong savings, manageable debt, "
        "and a sufficient emergency fund."
    )

elif agent_result["status"] == "Moderate":

    st.warning(
        "⚠️ **Moderate Financial Position**\n\n"
        "Focus on increasing savings, controlling debt, "
        "and strengthening your emergency fund."
    )

else:

    st.error(
        "🚨 **Financial Position Needs Improvement**\n\n"
        "Prioritize building emergency savings, reducing debt, "
        "and improving your monthly savings rate."
    )

    st.divider()

# =========================================================
# AI FINANCIAL Q&A
# =========================================================

st.write("### 💬 Ask FinTwin-X")

user_question = st.text_input(
    "Ask a question about your financial health"
)

if user_question:

    question = user_question.lower()
    answer = None

    # =====================================================
    # DIRECT PERSONAL FINANCIAL QUESTIONS
    # =====================================================

    if (
        ("how much debt" in question or "my debt" in question)
        and "safely" not in question
        and "safe debt" not in question
    ):

        st.info(
            f"🤖 FinTwin-X: Your current debt is "
            f"**Rs. {selected_user['debt']:,.0f}**."
        )

    elif "what is my savings rate" in question or "my savings rate" in question:

        st.info(
            f"🤖 FinTwin-X: Your current savings rate is "
            f"**{agent_result['savings_rate']:.2f}%**."
        )

    elif (
        "emergency fund" in question
        or "emergency savings" in question
        or "months of emergency" in question
    ) and "how long will it take" not in question:

        st.info(
            f"🤖 FinTwin-X: Your emergency fund currently covers "
            f"**{agent_result['emergency_fund']:.2f} months** of expenses."
        )

    elif (
        "monthly income" in question
        or "my income" in question
        or "how much do i earn" in question
    ):

        st.info(
            f"🤖 FinTwin-X: Your monthly income is "
            f"**Rs. {selected_user['monthly_income']:,.0f}**."
        )

    elif (
        "monthly expenses" in question
        or "my expenses" in question
        or "how much do i spend" in question
    ):

        st.info(
            f"🤖 FinTwin-X: Your monthly expenses are "
            f"**Rs. {selected_user['monthly_expenses']:,.0f}**."
        )

    elif (
        "monthly savings" in question
        or "my savings" in question
        or "how much do i save" in question
    ):

        st.info(
            f"🤖 FinTwin-X: Your monthly savings are "
            f"**Rs. {selected_user['monthly_savings']:,.0f}** per month."
        )

    elif (
        "financial health score" in question
        or "my health score" in question
        or "what is my score" in question
    ):

        st.info(
            f"🤖 FinTwin-X: Your Financial Health Score is "
            f"**{agent_result['health_score']:.2f}/100**."
        )

    elif (
        "risk status" in question
        or "my risk" in question
        or "what is my risk" in question
    ):

        health_score = agent_result["health_score"]

        if health_score >= 70:
            risk_status = "Low Risk"
        elif health_score >= 40:
            risk_status = "Moderate Risk"
        else:
            risk_status = "High Risk"

        st.info(
            f"🤖 FinTwin-X: Your current Risk Status is "
            f"**{risk_status}**."
        )

    elif (
        "what should i improve first" in question
        or "what should i improve" in question
        or "where should i improve" in question
    ):

        if agent_result["debt_to_income"] > 40:
            priority = (
                "💳 **Debt Management** — Your debt-to-income ratio "
                "is high, so reducing debt should be your first priority."
            )

        elif agent_result["emergency_fund"] < 3:
            priority = (
                "🛡️ **Emergency Fund** — Your emergency fund is below "
                "3 months, so building your emergency savings should "
                "be your first priority."
            )

        elif agent_result["savings_rate"] < 20:
            priority = (
                "💰 **Savings** — Try to gradually increase your "
                "savings rate toward 20% or more."
            )

        else:
            priority = (
                "🌟 Your main financial indicators are in a healthy "
                "range. Continue maintaining your current habits."
            )

        st.info(
            f"🤖 FinTwin-X: Based on your current financial profile, "
            f"your first priority should be:\n\n{priority}"
        )

    elif (
        "how can i improve my emergency fund" in question
        or "improve my emergency fund" in question
        or "build my emergency fund" in question
    ):

        emergency_months = agent_result["emergency_fund"]

        if emergency_months < 1:
            advice = (
                "🛡️ Your emergency fund is very low. "
                "Start by saving a small amount every month "
                "until you build at least 1 month of expenses."
            )

        elif emergency_months < 3:
            advice = (
                "🛡️ Your emergency fund is below the recommended "
                "3 months. Try to gradually increase your emergency "
                "savings until you reach at least 3 months of expenses."
            )

        elif emergency_months < 6:
            advice = (
                "🛡️ Your emergency fund is in a good range. "
                "Keep saving until you reach around 6 months of expenses "
                "for stronger financial protection."
            )

        else:
            advice = (
                "🌟 Excellent! Your emergency fund covers 6 or more "
                "months of expenses. Keep maintaining it."
            )

        st.info(
            f"🤖 FinTwin-X: You currently have "
            f"**{emergency_months:.2f} months** of emergency-fund coverage.\n\n"
            f"{advice}"
        )

    elif (
        "how can i improve my savings" in question
        or "improve my savings" in question
        or "increase my savings" in question
        or "how can i save more" in question
    ):

        savings_rate = agent_result["savings_rate"]

        if savings_rate < 10:
            advice = (
                "💰 Your savings rate is quite low. "
                "Start by tracking your expenses and try to save "
                "at least 10% of your monthly income."
            )

        elif savings_rate < 20:
            advice = (
                "💰 Your savings rate is below the recommended 20%. "
                "Try reducing unnecessary expenses and gradually "
                "increase your monthly savings."
            )

        elif savings_rate < 30:
            advice = (
                "🌟 Your savings rate is good. "
                "Try to increase it toward 30% by controlling "
                "non-essential spending."
            )

        else:
            advice = (
                "🌟 Excellent! Your savings rate is strong. "
                "Keep maintaining your current saving habits."
            )

        st.info(
            f"🤖 FinTwin-X: Your current savings rate is "
            f"**{savings_rate:.2f}%**.\n\n"
            f"{advice}"
        )

    elif (
        "how can i reduce my debt" in question
        or "reduce my debt" in question
        or "pay off my debt" in question
        or "how can i manage my debt" in question
    ):

        debt_to_income = agent_result["debt_to_income"]

        if debt_to_income > 40:
            advice = (
                "💳 Your debt-to-income ratio is high. "
                "Prioritize paying down high-cost debt, avoid taking "
                "new unnecessary debt, and try to increase your "
                "monthly debt payments gradually."
            )

        elif debt_to_income > 20:
            advice = (
                "💳 Your debt-to-income ratio is moderate. "
                "Continue making regular debt payments and avoid "
                "taking on unnecessary new debt."
            )

        else:
            advice = (
                "🌟 Your debt-to-income ratio is relatively low. "
                "Keep your debt under control and continue making "
                "regular payments."
            )

        st.info(
            f"🤖 FinTwin-X: Your current debt-to-income ratio is "
            f"**{debt_to_income:.2f}%**.\n\n"
            f"{advice}"
        )

    elif (
        "why is my financial health low" in question
        or "why is my health score low" in question
        or "why is my financial health bad" in question
    ):

        reasons = []

        if agent_result["debt_to_income"] > 40:
            reasons.append(
                f"💳 Your debt-to-income ratio is high "
                f"({agent_result['debt_to_income']:.2f}%)."
            )

        if agent_result["savings_rate"] < 20:
            reasons.append(
                f"💰 Your savings rate is below 20% "
                f"({agent_result['savings_rate']:.2f}%)."
            )

        if agent_result["emergency_fund"] < 3:
            reasons.append(
                f"🛡️ Your emergency fund covers only "
                f"{agent_result['emergency_fund']:.2f} months."
            )

        if not reasons:
            reasons.append(
                "🌟 Your main financial indicators are in a healthy range."
            )

        st.info(
            f"🤖 FinTwin-X: Your Financial Health Score is "
            f"**{agent_result['health_score']:.2f}/100**.\n\n"
            "The main factors affecting your score are:\n\n"
            + "\n".join(reasons)
        )

    elif (
        "what is my financial status" in question
        or "what is my financial position" in question
        or "tell me my financial status" in question
    ):

        health_score = agent_result["health_score"]

        if health_score >= 70:
            status_message = (
                "🌟 Your financial position is healthy. "
                "Keep maintaining your current financial habits."
            )

        elif health_score >= 40:
            status_message = (
                "⚠️ Your financial position is moderate. "
                "There are some areas that you should improve."
            )

        else:
            status_message = (
                "🚨 Your financial position needs improvement. "
                "Focus on reducing debt, building your emergency fund, "
                "and maintaining healthy savings."
            )

        st.info(
            f"🤖 FinTwin-X: Your Financial Health Score is "
            f"**{health_score:.2f}/100**.\n\n"
            f"{status_message}"
        )                

    elif (
        "how much should i save each month" in question
        or "how much should i save" in question
        or "monthly saving target" in question
        or "saving target" in question
    ):

        monthly_income = selected_user["monthly_income"]
        current_savings = selected_user["monthly_savings"]

        recommended_savings = monthly_income * 0.20
        extra_savings_needed = max(
            recommended_savings - current_savings,
            0
        )

        st.info(
            f"🤖 FinTwin-X: Based on your monthly income of "
            f"**Rs. {monthly_income:,.0f}**, a recommended savings "
            f"target is around **Rs. {recommended_savings:,.0f} per month** "
            f"(20% of income).\n\n"
            f"💰 You currently save **Rs. {current_savings:,.0f}** per month.\n\n"
            f"🎯 You would need to save approximately "
            f"**Rs. {extra_savings_needed:,.0f} more per month** "
            f"to reach the 20% target."
        )

    elif (
        "how much debt can i safely have" in question
        or "safe debt limit" in question
        or "how much debt is safe" in question
        or "safe debt" in question
    ):

        monthly_income = selected_user["monthly_income"]
        current_debt = selected_user["debt"]

        safe_debt_limit = monthly_income * 0.40

        if current_debt <= safe_debt_limit:
            debt_message = (
                "🌟 Your current debt is within this estimated safe limit. "
                "Continue managing your debt responsibly."
            )
        else:
            debt_message = (
                "⚠️ Your current debt is above this estimated limit. "
                "Focus on reducing your debt and avoid unnecessary borrowing."
            )

        st.info(
            f"🤖 FinTwin-X: Based on your monthly income of "
            f"**Rs. {monthly_income:,.0f}**, an estimated debt limit "
            f"using 40% of monthly income is "
            f"**Rs. {safe_debt_limit:,.0f}**.\n\n"
            f"💳 Your current debt is **Rs. {current_debt:,.0f}**.\n\n"
            f"{debt_message}"
        )


    elif "debt" in question:

        answer = (
            f"Your debt-to-income ratio is "
            f"{agent_result['debt_to_income']:.2f}%. "
            "Reducing debt can improve your financial health."
        )
    
    elif (
        "how long will it take" in question
        and "emergency fund" in question
    ):

        monthly_expenses = selected_user["monthly_expenses"]
        current_emergency_fund = (
            selected_user["emergency_fund_savings"]
        )
        monthly_savings = selected_user["monthly_savings"]

        target_emergency_fund = monthly_expenses * 3
        remaining_amount = max(
            target_emergency_fund - current_emergency_fund,
            0
        )

        if remaining_amount == 0:
            months_needed = 0
            message = (
                "🌟 You already have enough savings to cover "
                "3 months of expenses."
            )

        elif monthly_savings > 0:
            months_needed = (
                remaining_amount / monthly_savings
            )
            message = (
                f"🛡️ If you continue saving around "
                f"Rs. {monthly_savings:,.0f} per month, "
                f"you could reach your 3-month emergency-fund "
                f"target in approximately **{months_needed:.1f} months**."
            )

        else:
            months_needed = None
            message = (
                "⚠️ You currently have no monthly savings available "
                "to build your emergency fund. Try to create a small "
                "monthly saving amount first."
            )

        st.info(
            f"🤖 FinTwin-X: Your 3-month emergency-fund target is "
            f"**Rs. {target_emergency_fund:,.0f}**.\n\n"
            f"💰 Your current emergency-fund savings are "
            f"**Rs. {current_emergency_fund:,.0f}**.\n\n"
            f"{message}"
        )

    # =====================================================
    # COMBINED STRESS TEST
    # =====================================================

    elif (
        "income decreases by 20%" in question
        and "expenses increase by 20%" in question
    ):

        stress_income = selected_user["monthly_income"] * 0.80
        stress_expenses = selected_user["monthly_expenses"] * 1.20

        stress_savings = max(
            stress_income - stress_expenses,
            0
        )

        stress_savings_rate = (
            stress_savings / stress_income
        ) * 100

        stress_savings_score = min(
            stress_savings_rate,
            50
        ) * 2

        stress_emergency_fund = (
            stress_savings / stress_expenses
        )

        stress_emergency_fund_score = (
            min(stress_emergency_fund, 6) / 6
        ) * 100

        stress_debt_score = max(
            min(
                100 - selected_user["debt_to_income"],
                100
            ),
            0
        )

        stress_health_score = (
            stress_savings_score * 0.4
            + stress_debt_score * 0.3
            + stress_emergency_fund_score * 0.3
        )

        answer = (
            "⚠️ **Combined Stress Test**\n\n"
            f"Your monthly income would decrease from "
            f"Rs. {selected_user['monthly_income']:,.0f} "
            f"to Rs. {stress_income:,.0f}.\n\n"
            f"Your monthly expenses would increase from "
            f"Rs. {selected_user['monthly_expenses']:,.0f} "
            f"to Rs. {stress_expenses:,.0f}.\n\n"
            f"Your estimated monthly savings would become "
            f"Rs. {stress_savings:,.0f}.\n\n"
            f"Your new savings rate would be "
            f"{stress_savings_rate:.2f}%.\n\n"
            f"Your estimated Financial Health Score would become "
            f"{stress_health_score:.2f}.\n\n"
            "💡 Recommendation: This combined scenario creates "
            "significant financial pressure. Prioritize your "
            "emergency fund, reduce unnecessary expenses, and "
            "avoid taking on additional debt."
        )

    # =====================================================
    # INCOME -20% STRESS TEST
    # =====================================================

    elif (
        "income decreases by 20%" in question
        or "income decrease by 20%" in question
    ):

        stress_income = selected_user["monthly_income"] * 0.80
        stress_expenses = selected_user["monthly_expenses"]

        stress_savings = max(
            stress_income - stress_expenses,
            0
        )

        stress_savings_rate = (
            stress_savings / stress_income
        ) * 100

        stress_savings_score = min(
            stress_savings_rate,
            50
        ) * 2

        stress_emergency_fund = (
            stress_savings / stress_expenses
        )

        stress_emergency_fund_score = (
            min(stress_emergency_fund, 6) / 6
        ) * 100

        stress_debt_score = max(
            min(
                100 - selected_user["debt_to_income"],
                100
            ),
            0
        )

        stress_health_score = (
            stress_savings_score * 0.4
            + stress_debt_score * 0.3
            + stress_emergency_fund_score * 0.3
        )

        answer = (
            "📉 **Income -20% Stress Test**\n\n"
            f"Your monthly income would decrease from "
            f"Rs. {selected_user['monthly_income']:,.0f} "
            f"to Rs. {stress_income:,.0f}.\n\n"
            f"Your estimated savings would become "
            f"Rs. {stress_savings:,.0f} per month.\n\n"
            f"Your new savings rate would be "
            f"{stress_savings_rate:.2f}%.\n\n"
            f"Your estimated Financial Health Score would become "
            f"{stress_health_score:.2f}.\n\n"
            "💡 Recommendation: A 20% income reduction would put "
            "additional pressure on your financial position. "
            "Maintain an emergency fund and control unnecessary expenses."
        )

    # =====================================================
    # EXPENSES +20% STRESS TEST
    # =====================================================

    elif (
        "expenses increase by 20%" in question
        or "expenses increase" in question
    ):

        stress_income = selected_user["monthly_income"]
        stress_expenses = selected_user["monthly_expenses"] * 1.20

        stress_savings = max(
            stress_income - stress_expenses,
            0
        )

        stress_savings_rate = (
            stress_savings / stress_income
        ) * 100

        stress_savings_score = min(
            stress_savings_rate,
            50
        ) * 2

        stress_emergency_fund = (
            stress_savings / stress_expenses
        )

        stress_emergency_fund_score = (
            min(stress_emergency_fund, 6) / 6
        ) * 100

        stress_debt_score = max(
            min(
                100 - selected_user["debt_to_income"],
                100
            ),
            0
        )

        stress_health_score = (
            stress_savings_score * 0.4
            + stress_debt_score * 0.3
            + stress_emergency_fund_score * 0.3
        )

        answer = (
            "📈 **Expenses +20% Stress Test**\n\n"
            f"Your monthly expenses would increase from "
            f"Rs. {selected_user['monthly_expenses']:,.0f} "
            f"to Rs. {stress_expenses:,.0f}.\n\n"
            f"Your estimated savings would become "
            f"Rs. {stress_savings:,.0f} per month.\n\n"
            f"Your new savings rate would be "
            f"{stress_savings_rate:.2f}%.\n\n"
            f"Your estimated Financial Health Score would become "
            f"{stress_health_score:.2f}.\n\n"
            "💡 Recommendation: Higher expenses can reduce your "
            "monthly savings. Review unnecessary spending and "
            "maintain an adequate emergency fund."
        )

    # =====================================================
    # SAVINGS QUESTION
    # =====================================================

    elif (
        "my savings" in question
        or "current savings" in question
    ):

        answer = (
            f"Your current savings rate is "
            f"{agent_result['savings_rate']:.2f}%. "
            "Try to increase your savings rate gradually."
        )

    # =====================================================
    # DEBT QUESTION
    # =====================================================

    elif "debt" in question:

        answer = (
            f"Your debt-to-income ratio is "
            f"{agent_result['debt_to_income']:.2f}%. "
            "Reducing debt can improve your financial health."
        )

    # =====================================================
    # EMERGENCY FUND QUESTION
    # =====================================================

    elif "emergency" in question:

        answer = (
            f"Your emergency fund currently covers approximately "
            f"{agent_result['emergency_fund']:.2f} months of expenses."
        )

    # =====================================================
    # FINANCIAL HEALTH QUESTION
    # =====================================================

    elif (
        "health" in question
        or "score" in question
        or "improve" in question
        or "better" in question
    ):

        recommendations = []

        if agent_result["debt_to_income"] > 40:
            recommendations.append(
                "💳 Reduce your debt-to-income ratio by prioritizing debt repayment and avoiding unnecessary borrowing."
            )

        if agent_result["emergency_fund"] < 3:
            recommendations.append(
                "🛡️ Build an emergency fund covering at least 3 months of expenses."
            )

        if agent_result["savings_rate"] < 20:
            recommendations.append(
                "💰 Gradually increase your savings rate toward 20% or more."
            )

        if not recommendations:
            recommendations.append(
                "🌟 Your main financial indicators are already in a healthy range. Continue maintaining your current financial habits."
            )

        answer = (
            f"❤️ Your Financial Health Score is "
            f"{agent_result['health_score']:.2f}/100, "
            f"which is classified as {agent_result['status']}.\n\n"
            "💡 **How You Can Improve:**\n\n"
            + "\n".join(recommendations)
        )


    else:
   
        retrieved_knowledge = semantic_search(user_question)
   
        prompt = build_ai_prompt(
            user_question,
            retrieved_knowledge,
            agent_result["health_score"],
            agent_result["savings_rate"],
            agent_result["debt_to_income"],
            agent_result["emergency_fund"]
        )
   
        answer = generate_ai_answer(prompt)
        
    if answer:
        st.info(f"🤖 FinTwin-X: {answer}")


# =========================================================
# STRESS SCENARIO SELECTION
# =========================================================

st.write("### 🧪 Financial Stress Test")

st.caption(
    "Select a stress scenario to estimate its impact on "
    "the selected user's financial health."
)

stress_scenario = st.selectbox(
    "Choose Stress Scenario",
    [
        "Income -20%",
        "Expenses +20%",
        "Combined Stress"
    ]
)

normal_income = selected_user["monthly_income"]
normal_expenses = selected_user["monthly_expenses"]
normal_health = selected_user["financial_health_score"]


# =========================================================
# SELECTED STRESS SCENARIO CALCULATION
# =========================================================

if stress_scenario == "Income -20%":

    stress_income = normal_income * 0.80
    stress_expenses = normal_expenses


elif stress_scenario == "Expenses +20%":

    stress_income = normal_income
    stress_expenses = normal_expenses * 1.20


else:

    stress_income = normal_income * 0.80
    stress_expenses = normal_expenses * 1.20


# =========================================================
# STRESS FINANCIAL CALCULATIONS
# =========================================================

stress_savings = max(
    stress_income - stress_expenses,
    0
)

stress_savings_rate = (
    stress_savings / stress_income
) * 100

stress_savings_score = (
    min(stress_savings_rate, 50) * 2
)

stress_emergency_fund = (
    stress_savings / stress_expenses
)

stress_emergency_fund_score = (
    min(stress_emergency_fund, 6) / 6
) * 100

stress_debt_score = (
    100 - selected_user["debt_to_income"]
)

stress_debt_score = max(
    min(stress_debt_score, 100),
    0
)

stress_health_score = (
    stress_savings_score * 0.4
    + stress_debt_score * 0.3
    + stress_emergency_fund_score * 0.3
)


# =========================================================
# STRESS SCENARIO RESULTS
# =========================================================

st.write("### 📊 Stress Scenario Impact")
st.caption(
    "Estimated financial impact of the selected stress scenario."
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💵 Stress Income",
        f"Rs. {stress_income:,.0f}"
    )

with col2:
    st.metric(
        "💰 Stress Savings",
        f"Rs. {stress_savings:,.0f}"
    )

with col3:
    st.metric(
        "📈 Savings Rate",
        f"{stress_savings_rate:.2f}%"
    )

with col4:
    st.metric(
        "❤️ Health Score",
        f"{stress_health_score:.2f}"
    )


# =========================================================
# HEALTH SCORE IMPACT
# =========================================================

health_change = (
    normal_health - stress_health_score
)

st.write("### 🎯 Financial Health Impact")

st.caption(
    f"Estimated change in financial health under the selected "
    f"**{stress_scenario}** scenario."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "❤️ Normal Health Score",
        f"{normal_health:.2f}"
    )

with col2:
    st.metric(
        "📉 Stress Health Score",
        f"{stress_health_score:.2f}"
    )

with col3:
    if health_change > 0:
        st.metric(
            "⚠️ Health Score Change",
            f"-{health_change:.2f}"
        )
    else:
        st.metric(
            "✅ Health Score Change",
            f"+{abs(health_change):.2f}"
        )
        st.divider()
        st.write("### 📊 Normal vs Stress Health Score")

st.bar_chart(
    {
        "Normal": normal_health,
        "Stress": stress_health_score
    }
)

st.divider()

st.write("### ⚠️ Stress Test Interpretation")

health_difference = stress_health_score - normal_health

if health_difference >= 0:
    st.success(
        "This stress scenario does not reduce the user's "
        "financial health score."
    )
elif health_difference > -10:
    st.warning(
        "This stress scenario causes a small decline in "
        "financial health."
    )
elif health_difference > -25:
    st.warning(
        "This stress scenario causes a significant decline "
        "in financial health."
    )
else:
    st.error(
        "🚨 This stress scenario creates severe financial pressure "
        "and significantly reduces financial health."
    )

st.divider()


# =========================================================
# AI STRESS INSIGHT
# =========================================================

st.write("### 🤖 AI Stress Insight")

if stress_health_score >= normal_health:

    stress_message = (
        "Your financial health remains stable under this "
        "stress scenario."
    )

elif stress_health_score >= 40:

    stress_message = (
        "Your financial health decreases under this stress "
        "scenario. Consider increasing savings and controlling expenses."
    )

else:

    stress_message = (
        "🚨 This stress scenario significantly affects your "
        "financial health. Focus on building emergency savings "
        "and reducing unnecessary expenses."
    )

st.info(
    f"🤖 **AI Agent Insight**\n\n{stress_message}"
)


# =========================================================
# AI RECOMMENDATION
# =========================================================

st.write("### 💡 AI Agent Recommendation")

if health_change > 0:

    st.warning(
        f"🤖 Under the **{stress_scenario}** scenario, your "
        f"Financial Health Score decreases by "
        f"**{health_change:.2f} points**."
    )

else:

    st.success(
        f"🤖 Your financial health remains stable under the "
        f"**{stress_scenario}** scenario."
    )


if "Income" in stress_scenario:

    st.write(
        "💰 **Recommendation:** Focus on maintaining your "
        "savings and reduce unnecessary expenses during an income reduction."
    )

elif "Expenses" in stress_scenario:

    st.write(
        "💳 **Recommendation:** Control discretionary spending "
        "and review your monthly expenses."
    )

elif "Combined" in stress_scenario:

    st.write(
        "🚨 **Recommendation:** Build a stronger emergency fund, "
        "reduce unnecessary expenses, and maintain a higher savings buffer."
    )


st.divider()

# =========================================================
# MULTIPLE STRESS SCENARIOS
# =========================================================

st.write("### 🔬 Multiple Stress Scenarios")

st.caption(
    "Compare how different financial stress conditions affect "
    "the selected user's Financial Health Score."
)


# =========================================================
# NORMAL SCENARIO
# =========================================================

normal_score = normal_health


# =========================================================
# INCOME -20%
# =========================================================

income_stress_income = normal_income * 0.80

income_stress_savings = max(
    income_stress_income - normal_expenses,
    0
)

income_stress_savings_rate = (
    income_stress_savings / income_stress_income
) * 100

income_stress_savings_score = (
    min(income_stress_savings_rate, 50) * 2
)

income_stress_emergency = (
    income_stress_savings / normal_expenses
)

income_stress_emergency_score = (
    min(income_stress_emergency, 6) / 6
) * 100

income_stress_score = (
    income_stress_savings_score * 0.4
    + stress_debt_score * 0.3
    + income_stress_emergency_score * 0.3
)


# =========================================================
# EXPENSES +20%
# =========================================================

expense_stress_expenses = normal_expenses * 1.20

expense_stress_savings = max(
    normal_income - expense_stress_expenses,
    0
)

expense_stress_savings_rate = (
    expense_stress_savings / normal_income
) * 100

expense_stress_savings_score = (
    min(expense_stress_savings_rate, 50) * 2
)

expense_stress_emergency = (
    expense_stress_savings / expense_stress_expenses
)

expense_stress_emergency_score = (
    min(expense_stress_emergency, 6) / 6
) * 100

expense_stress_score = (
    expense_stress_savings_score * 0.4
    + stress_debt_score * 0.3
    + expense_stress_emergency_score * 0.3
)


# =========================================================
# COMBINED STRESS
# =========================================================

combined_income = normal_income * 0.80

combined_expenses = normal_expenses * 1.20

combined_savings = max(
    combined_income - combined_expenses,
    0
)

combined_savings_rate = (
    combined_savings / combined_income
) * 100

combined_savings_score = (
    min(combined_savings_rate, 50) * 2
)

combined_emergency = (
    combined_savings / combined_expenses
)

combined_emergency_score = (
    min(combined_emergency, 6) / 6
) * 100

combined_stress_score = (
    combined_savings_score * 0.4
    + stress_debt_score * 0.3
    + combined_emergency_score * 0.3
)


# =========================================================
# SCENARIO COMPARISON
# =========================================================

scenario_data = pd.DataFrame({
    "Scenario": [
        "Normal",
        "Income -20%",
        "Expenses +20%",
        "Combined Stress"
    ],
    "Financial Health Score": [
        normal_score,
        income_stress_score,
        expense_stress_score,
        combined_stress_score
    ]
})


st.write("### 📊 Scenario Comparison")

st.caption(
    "A higher score indicates stronger financial health "
    "under the given scenario."
)

st.dataframe(
    scenario_data,
    width="stretch",
    hide_index=True
)

st.bar_chart(
    scenario_data.set_index("Scenario")[
        "Financial Health Score"
    ]
)

st.divider()


# =========================================================
# MONTE CARLO SIMULATION
# =========================================================

st.write("### 🎲 Monte Carlo Savings Simulation")

st.caption(
    "Simulating 10,000 possible monthly income outcomes "
    "to estimate potential savings."
)

simulations = 10000

np.random.seed(42)

simulation_income = selected_user["monthly_income"]
simulation_expenses = selected_user["monthly_expenses"]

income_changes = np.random.normal(
    loc=0,
    scale=0.10,
    size=simulations
)

simulated_income = (
    simulation_income * (1 + income_changes)
)

simulated_savings = (
    simulated_income - simulation_expenses
)

simulated_savings = np.maximum(
    simulated_savings,
    0
)

average_simulated_savings = (
    simulated_savings.mean()
)

zero_savings_probability = (
    (simulated_savings == 0).mean() * 100
)


col1, col2 = st.columns(2)

with col1:
    st.metric(
        "💰 Average Simulated Savings",
        f"Rs. {average_simulated_savings:,.0f}"
    )

with col2:
    st.metric(
        "⚠️ Probability of Zero Savings",
        f"{zero_savings_probability:.2f}%"
    )

st.divider()

# =========================================================
# MONTE CARLO DISTRIBUTION
# =========================================================

st.write("### 📊 Possible Savings Distribution")

st.caption(
    "This chart shows the distribution of possible monthly "
    "savings across 10,000 simulated outcomes."
)

hist_counts, bin_edges = np.histogram(
    simulated_savings,
    bins=30
)

hist_df = pd.DataFrame({
    "Savings Range": [
        f"Rs. {int(bin_edges[i]):,}"
        for i in range(len(hist_counts))
    ],
    "Simulations": hist_counts
})

st.bar_chart(
    hist_df.set_index("Savings Range")
)

st.divider()

# =========================================================
# VALUE AT RISK (VaR)
# =========================================================

st.write("### 📉 Value at Risk (VaR)")

st.caption(
    "VaR estimates the potential monthly savings loss "
    "under adverse simulated income outcomes."
)

normal_savings = (
    simulation_income - simulation_expenses
)

savings_loss = (
    normal_savings - simulated_savings
)

var_95 = np.percentile(
    savings_loss,
    95
)

var_99 = np.percentile(
    savings_loss,
    99
)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "📉 95% VaR",
        f"Rs. {var_95:,.0f}"
    )

with col2:
    st.metric(
        "📉 99% VaR",
        f"Rs. {var_99:,.0f}"
    )

st.info(
    "VaR estimates the potential savings loss under "
    "adverse simulated income outcomes."
)

st.divider()

# =========================================================
# VaR INTERPRETATION
# =========================================================

st.write("### 🧠 VaR Interpretation")

if var_95 <= 0:
    st.success(
        "Your simulated savings show low downside risk under "
        "the current assumptions."
    )
else:
    st.warning(
        f"Under the simulation assumptions, a 95% VaR of "
        f"Rs. {var_95:,.0f} means the estimated monthly "
        "savings loss should not exceed this amount in about "
        "95% of simulated outcomes."
    )

st.info(
    f"At the more severe 99% confidence level, the estimated "
    f"potential savings loss is Rs. {var_99:,.0f}."
)

st.divider()


# =========================================================
# FINANCIAL ANOMALY DETECTION
# =========================================================

st.write("### 🚨 Financial Anomaly Detection")

st.caption(
    "Identifying unusual financial patterns across simulated users."
)

anomaly_features = [
    "monthly_income",
    "monthly_expenses",
    "monthly_savings",
    "debt",
    "savings_rate",
    "debt_to_income",
    "emergency_fund_months"
]

anomaly_model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

df["anomaly"] = anomaly_model.fit_predict(
    df[anomaly_features]
)

df["anomaly_status"] = df["anomaly"].map({
    1: "Normal",
    -1: "Anomaly"
})

anomaly_count = (
    df["anomaly_status"] == "Anomaly"
).sum()

normal_count = (
    df["anomaly_status"] == "Normal"
).sum()

anomaly_rate = (
    anomaly_count / len(df)
) * 100

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "✅ Normal Users",
        normal_count
    )

with col2:
    st.metric(
        "🚨 Anomalous Users",
        anomaly_count
    )

    st.metric(
    "📊 Anomaly Rate",
    f"{anomaly_rate:.2f}%"
)

st.caption(
    "Percentage of simulated users identified as having "
    "unusual financial patterns."
)

st.divider()

selected_anomaly_status = df.loc[
    df["user_id"] == selected_user_id,
    "anomaly_status"
].iloc[0]

st.write("### Selected User Anomaly Status")

if selected_anomaly_status == "Anomaly":

    st.error(
        "🚨 This user's financial pattern has been "
        "detected as unusual."
    )

else:

    st.success(
        "✅ This user's financial pattern appears normal."
    )

# =========================================================
# ANOMALY INTERPRETATION
# =========================================================

if anomaly_rate <= 5:
    st.info(
        "🧠 The anomaly detection model identified a relatively "
        "small portion of users as unusual financial patterns."
    )
else:
    st.warning(
        "⚠️ A larger portion of users has been identified as "
        "having unusual financial patterns. Further investigation "
        "may be useful."
    )

st.divider()


# =========================================================
# FINANCIAL DNA POPULATION SUMMARY
# =========================================================

st.write("### 🧬 Financial DNA Population Summary")

st.caption(
    "Overview of financial behavior across all simulated users."
)

total_users = len(df)

average_health = (
    df["financial_health_score"].mean()
)

strong_savers = (
    df["savings_profile"] == "Strong Saver"
).sum()

high_debt_users = (
    df["debt_profile"] == "High Debt"
).sum()

weak_emergency_fund = (
    df["emergency_fund_profile"]
    == "Weak Emergency Fund"
).sum()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Total Users",
        total_users
    )

with col2:
    st.metric(
        "❤️ Average Health Score",
        round(average_health, 2)
    )

with col3:
    st.metric(
        "💰 Strong Savers",
        strong_savers
    )

with col4:
    st.metric(
        "💳 High Debt Users",
        high_debt_users
    )

st.write("#### 🛡️ Emergency Fund Risk")

st.metric(
    "Weak Emergency Fund Users",
    weak_emergency_fund
)

st.caption(
    "Users whose emergency savings are below the recommended level."
)

st.divider()


# =========================================================
# FINANCIAL HEALTH OVERVIEW
# =========================================================

st.header("📊 Financial Health Overview")

st.caption(
    "Distribution of overall financial health profiles "
    "across all simulated users."
)

health_summary = (
    df["health_profile"].value_counts()
)

st.write("#### 👥 Health Profile Distribution")

st.caption(
    "Number of simulated users in each financial health category."
)

st.bar_chart(
    health_summary
)

st.divider()


# =========================================================
# SAVINGS PROFILE
# =========================================================

st.header("💰 Savings Profile")

st.caption(
    "Distribution of savings behavior across simulated users."
)

savings_summary = (
    df["savings_profile"].value_counts()
)

st.write("#### 👥 Savings Behavior Distribution")

st.caption(
    "Number of simulated users in each savings behavior category."
)

st.bar_chart(
    savings_summary
)

st.divider()


# =========================================================
# DEBT PROFILE
# =========================================================

st.header("📉 Debt Profile")

st.caption(
    "Distribution of debt-management profiles across simulated users."
)

debt_summary = (
    df["debt_profile"].value_counts()
)

st.write("#### 👥 Debt Management Distribution")

st.caption(
    "Number of simulated users in each debt-management category."
)

st.bar_chart(
    debt_summary
)

st.divider()


# =========================================================
# EMERGENCY FUND PROFILE
# =========================================================

st.header("🛡️ Emergency Fund Profile")

st.caption(
    "Distribution of emergency-fund preparedness across simulated users."
)

emergency_summary = (
    df["emergency_fund_profile"].value_counts()
)

st.write("#### 👥 Emergency Fund Distribution")

st.caption(
    "Number of simulated users in each emergency-fund preparedness category."
)

st.bar_chart(
    emergency_summary
)

st.divider()