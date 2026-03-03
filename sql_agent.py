import sqlite3
import anthropic
import os
from dotenv import load_dotenv

# 1. Setup Environment
load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

DB_NAME = "amazon_sales.db"
SQL_FILE = "AmazonSales.sql"

def setup_database():
    """Converts the .sql file into a live SQLite database if it doesn't exist"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Check if table already exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='mytable'")
    if not cursor.fetchone():
        print("🔧 Building database from SQL file...")
        try:
            with open(SQL_FILE, 'r') as f:
                sql_script = f.read()
            cursor.executescript(sql_script)
            conn.commit()
            print("✅ Database ready!")
        except FileNotFoundError:
            print(f"❌ Error: {SQL_FILE} not found. Please ensure it's in the folder.")
    return conn

def ask_claude_for_sql(question):
    """Sends the user question to Claude and gets back ONLY the SQL query"""
    system_prompt = (
        "You are a SQL expert. The database table is called 'mytable'. "
        "The columns are: product_name, actual_price, discounted_price, discount_percentage, rating, and review_content. "
        "Respond ONLY with the raw SQL code. No markdown, no backticks."
    )
    
    try:
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=300,
            system=system_prompt,
            messages=[{"role": "user", "content": question}]
        )
        # Extract and clean the SQL code
        sql_code = message.content[0].text.strip()
        # Fallback cleaning just in case Claude adds backticks anyway
        sql_code = sql_code.replace("```sql", "").replace("```", "").strip()
        return sql_code
    except Exception as e:
        print(f"❌ AI Error: {e}")
        return None

if __name__ == "__main__":
    connection = setup_database()
    
    print("\n--- Amazon Sales AI Agent ---")
    user_input = input("What would you like to know about the Amazon data? ")
    
    if user_input:
        generated_sql = ask_claude_for_sql(user_input)
        
        if generated_sql:
            print(f"\n🚀 Running SQL: {generated_sql}")
            try:
                cursor = connection.cursor()
                cursor.execute(generated_sql)
                results = cursor.fetchall()
                
                if results:
                    for row in results:
                        print(row)
                else:
                    print("No results found.")
            except Exception as e:
                print(f"❌ Database Error: {e}")
    
    connection.close()