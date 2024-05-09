import sqlite3

def create_cobol_batch_file():
    conn = sqlite3.connect('loan.db')
    c = conn.cursor()
    
    # Fetch approved loans with only required fields
    c.execute("SELECT loan_id, loan_amount, loan_left, loan_term, 'N' FROM loan WHERE loan_status=?", ('Approved',))
    approved_loans = c.fetchall()

    # Create COBOL copybook
    with open('daily_file.txt', 'w') as file:
        for loan in approved_loans:
            # Convert each field to specified length and separate with space
            loan_id = str(loan[0]).rjust(3, '0')  # 3 bytes
            loan_amount = str(loan[1]).rjust(12, '0')[:12]  # 12 bytes
            loan_left = str(loan[2]).rjust(12, '0')[:12]  # 12 bytes
            #loan_term = str(loan[3]).rjust(2, '0')  # 2 bytes
            loan_term = str(loan[3]).rstrip().ljust(2)  # 2 bytes,

            loan_completed = str(loan[4])  # 1 byte
            # Write loan data to file with spaces between each field
            file.write(f"{loan_id} {loan_amount} {loan_left} {loan_term} {loan_completed}\n")

    conn.close()

if __name__ == '__main__':
    create_cobol_batch_file()
