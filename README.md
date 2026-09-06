# FinTwin-X 🧠💰

## AI Financial Digital Twin & Probabilistic Stress-Testing Engine

FinTwin-X is an AI-powered financial analytics dashboard designed to simulate user financial profiles, evaluate financial health, identify financial risks, and analyze how financial conditions may change under different stress scenarios.

The project combines financial analytics, machine learning, explainable AI, stress testing, Monte Carlo simulation, Value at Risk (VaR), anomaly detection, and an AI-powered financial assistant into one interactive Streamlit application.

---

## 🚀 Key Features

### 📊 Financial Health Analysis

* Financial Health Score
* Savings rate analysis
* Debt-to-income analysis
* Emergency fund analysis
* Financial risk classification

### 🧬 Financial DNA

FinTwin-X creates financial profiles based on:

* Savings behavior
* Debt levels
* Emergency-fund preparedness
* Overall financial health

### 🧪 Financial Stress Testing

Users can analyze the impact of scenarios such as:

* Income decreasing by 20%
* Expenses increasing by 20%
* Combined financial stress

### 🎲 Monte Carlo Simulation

Simulates thousands of possible financial outcomes to understand potential financial risk and uncertainty.

### 📉 Value at Risk (VaR)

Estimates potential financial losses under simulated conditions.

### 🚨 Anomaly Detection

Uses machine learning to identify unusual financial patterns among simulated users.

### 🤖 AI Financial Assistant

Ask FinTwin-X questions about your financial profile and receive personalized responses based on your financial data.

Examples:

* What is my financial health score?
* What is my risk status?
* How much should I save each month?
* How can I improve my emergency fund?
* How can I reduce my debt?
* What should I improve first?

### 🔍 Explainable AI

FinTwin-X highlights important factors influencing a user's financial health score, helping users understand why their financial position is classified as healthy, moderate, or financially stressed.

### 👥 Population-Level Analysis

The dashboard also analyzes financial patterns across simulated users, including:

* Savings profiles
* Debt profiles
* Emergency-fund profiles
* Financial health profiles

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Machine Learning
* Explainable AI
* Monte Carlo Simulation
* Value at Risk (VaR)
* Financial Risk Analytics

---

## 📁 Project Structure

```text
fin-twin-x/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── users.csv
│   ├── financial_dna.csv
│   ├── financial_dna_profiles.csv
│   ├── ml_dataset.csv
│   └── users_with_features.csv
│
└── src/
    ├── data_generator.py
    ├── features.py
    ├── financial_tools.py
    ├── financial_agent.py
    ├── financial_dna_all_users.py
    ├── rag_retriever.py
    ├── semantic_rag.py
    └── llm_agent.py
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project directory:

```bash
cd fin-twin-x
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit dashboard:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📊 Sample Dataset

The project uses simulated financial users rather than real personal financial data.

The dataset contains financial variables such as:

* Monthly income
* Monthly expenses
* Monthly savings
* Emergency-fund savings
* Debt
* Financial health metrics
* Financial profile classifications

---

## 🎯 Project Objective

The goal of FinTwin-X is to demonstrate how financial data, machine learning, simulation, and AI can be combined to create an intelligent financial decision-support system.

The system is designed to help users understand their financial position, identify major risk factors, and explore how their financial health could change under different economic conditions.

---

## 🔮 Future Improvements

Potential future developments include:

* Real-time financial data integration
* Advanced predictive financial models
* Personalized investment recommendations
* Portfolio risk analysis
* Interactive financial goal planning
* Real-world economic scenario simulation
* Advanced LLM-based financial conversations
* Automated financial reports

---

## 👩‍💻 Author

**Humna Tabassum**

BS FinTech Student
FAST-NUCES Karachi

---

## ⚠️ Disclaimer

FinTwin-X is an educational and research-oriented project using simulated financial data. It is not intended to provide professional financial, investment, tax, or legal advice.

```