import streamlit as st
import pandas as pd
import sqlite3

def load_data():
    conn = sqlite3.connect('loan.db')
    df = pd.read_sql_query("SELECT * FROM loan", conn)
    conn.close()
    return df

def admin():
    st.title('Admin Dashboard')
    st.subheader('Loan Details')

    df = load_data()
    
    st.dataframe(df)

if __name__ == '__main__':
    admin()
