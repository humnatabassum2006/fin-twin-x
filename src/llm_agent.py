import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError

load_dotenv()

# Streamlit Cloud secrets se key read karein, agar local ho toh .env se
api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


def build_ai_prompt(
    question,
    retrieved_knowledge,
    health_score,
    savings_rate,
    debt_to_income,
    emergency_fund
):

    prompt = f"""
You are FinTwin-X, an AI financial assistant.

Answer the user's question in simple, clear language.

User question:
{question}

Relevant financial knowledge:
{retrieved_knowledge}

User's current financial information:
- Financial Health Score: {health_score:.2f}
- Savings Rate: {savings_rate:.2f}%
- Debt-to-Income Ratio: {debt_to_income:.2f}%
- Emergency Fund: {emergency_fund:.2f} months

Instructions:
- Give a personalized answer based on the user's financial situation.
- Use the relevant financial knowledge provided above.
- Explain the reasoning clearly.
- Give practical recommendations.
- Do not invent financial information.
- Keep the answer concise and easy to understand.
"""

    return prompt


def generate_ai_answer(prompt):

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except RateLimitError:

        return (
            "⚠️ FinTwin-X AI is temporarily unavailable because "
            "the OpenAI API has no remaining credits. "
            "Your financial data and RAG knowledge base are working correctly. "
            "Please add API credits later to enable the live AI response."
        )
