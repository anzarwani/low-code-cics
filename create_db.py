import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('loan.db')
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS loan
             (loan_id INTEGER PRIMARY KEY,
             no_of_dependents INTEGER,
             education TEXT,
             self_employed TEXT,
             income_annum INTEGER,
             loan_amount INTEGER,
             loan_term INTEGER,
             cibil_score INTEGER,
             residential_assets_value INTEGER,
             commercial_assets_value INTEGER,
             luxury_assets_value INTEGER,
             bank_asset_value INTEGER,
             loan_status TEXT,
             loan_left INTEGER,
             debt_cleared TEXT)''')

# Commit changes and close connection
conn.commit()
conn.close()
