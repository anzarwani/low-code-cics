import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('loan.db')
c = conn.cursor()

# Read the text file and update the database
with open('daily_update_file.txt', 'r') as file:
    for line in file:
        loan_id = line[:3].strip()  # Extract loan_id
        loan_left = int(line[17:29])  # Extract loan_left
        debt_cleared = line[-2]  # Extract debt_cleared

        # Update the database for the given loan_id
        c.execute('''UPDATE loan
                     SET loan_left = ?,
                         debt_cleared = ?
                     WHERE loan_id = ?''', (loan_left, debt_cleared, loan_id))

# Commit changes and close connection
conn.commit()
conn.close()
