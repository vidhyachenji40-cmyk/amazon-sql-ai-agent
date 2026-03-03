# AI-Powered Retail Sentiment Analyzer (2026)

## Overview
This project is an automated data pipeline that processes customer retail reviews using the Anthropic Claude API. It reads raw feedback from a CSV, performs sentiment analysis using the latest 2026 AI models, and exports the results into a structured report.

## Tech Stack
* **Language:** Python 3.12
* **AI Model:** Claude Haiku 4.5 (`claude-haiku-4-5-20251001`)
* **Environment:** Google Cloud Shell
* **Libraries:** `anthropic`, `csv`, `os`

## How It Works
1. **Data Input:** The script loads `ai_analysis_report.csv` containing raw customer review text.
2. **AI Processing:** Each review is sent to the Haiku 4.5 model with a specific prompt to categorize sentiment (Positive, Negative, Mixed) and provide a concise reason.
3. **Data Output:** The final results are saved to `final_sentiment_results.csv` for business reporting.

## Key Challenges Overcome
* Resolved API model deprecation (404 errors) by implementing 2026-specific model IDs.
* Optimized API costs by utilizing the high-speed, low-cost Haiku model.

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