# AI-Powered Natural Language SQL Agent (2026)

An intelligent interface that allows users to query an Amazon Sales database using plain English. Powered by **Claude 3.5 Sonnet**, this agent translates natural language into optimized SQLite queries.

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **AI Model:** Claude 3.5 Sonnet (Anthropic API)
* **Database:** SQLite3
* **Environment:** Google Cloud Shell

## 🚀 Features
* **Natural Language Processing:** No SQL knowledge required.
* **Schema-Aware:** The agent understands the specific columns in `AmazonSales.sql`.
* **Format-Optimized:** Custom system prompts ensure raw SQL generation.

## 📖 How to Use
1. Clone the repository.
2. Add your Anthropic API Key to a `.env` file.
3. Run the agent:
   ```bash
   python3 sql_agent.py
