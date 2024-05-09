import streamlit as st
import pandas as pd
import sqlite3

def load_data():
    conn = sqlite3.connect('loan.db')
    df = pd.read_sql_query("SELECT * FROM loan", conn)
    conn.close()
    return df

def get_loan_details(loan_id):
    conn = sqlite3.connect('loan.db')
    query = f"SELECT loan_amount, loan_left, debt_cleared FROM loan WHERE loan_id = {loan_id}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def user_details():
    st.title('User Dashboard')
    st.subheader('Loan Details')

    loan_id = st.text_input("Enter Loan ID:")
    if loan_id:
        loan_id = int(loan_id)
        loan_details = get_loan_details(loan_id)
        if not loan_details.empty:
            st.write("Loan Details:")
            st.write(loan_details)
        else:
            st.write("No loan found with this ID.")

if __name__ == '__main__':
    user_details()
