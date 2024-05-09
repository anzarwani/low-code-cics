import streamlit as st
import sqlite3

def load_data():
    conn = sqlite3.connect('loan.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(loan_id), SUM(loan_amount) FROM loan where loan_status = 'Approved'")
    result = cursor.fetchone()
    conn.close()
    return result

def info():

    
    total_loans, total_amount = load_data()
    
    formatted_amount = "₹" + str(total_amount)
    c1, c2 = st.columns(2)
    with c1:
        st.metric(f"Total Borrowers", total_loans)
    with c2:
        st.metric(f"Total Loan Disbursed", formatted_amount)

if __name__ == '__main__':
    info()
