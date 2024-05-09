# THIS CODE SHOWS THE MAIN DASHBOARD FOR THE USER IN WHICH
# IT CAN CHECK IF LOAN CAN BE GIVEN OR NOT

import streamlit as st
import sqlite3
import pandas as pd
from ml_pipe import predict
def add_loan(no_of_dependents, education, self_employed, income_annum, loan_amount,
             loan_term, cibil_score, residential_assets_value, commercial_assets_value,
             luxury_assets_value, bank_asset_value, loan_status, loan_left, debt_cleared):
    conn = sqlite3.connect('loan.db')
    c = conn.cursor()
    
    c.execute("SELECT MAX(loan_id) FROM loan")
    max_id = c.fetchone()[0]
    
    # Increment the maximum loan_id by 1 to get a unique id
    if max_id is None:
        loan_id = 1
    else:
        loan_id = max_id + 1
    c.execute('''INSERT INTO loan VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (loan_id, no_of_dependents, education, self_employed, income_annum, loan_amount,
               loan_term, cibil_score, residential_assets_value, commercial_assets_value,
               luxury_assets_value, bank_asset_value, loan_status, loan_left, debt_cleared))
    conn.commit()
    conn.close()
    
    st.write("Your Loan ID is  ", loan_id)

def loan_app():
    st.title('Loan Details Input')
    st.write('Enter the details below:')

    #loan_id = loan_id
    #loan_id = st.number_input('Loan ID', min_value=1, step=1)
    no_of_dependents = st.number_input('Number of Dependents', min_value=0, step=1)
    education = st.selectbox('Education', ['Graduate', 'Undergraduate', 'Postgraduate'])
    self_employed = st.radio('Self Employed', ['Yes', 'No'])
    income_annum = st.number_input('Annual Income', min_value=0.0, step=1000.0, max_value = 9999999999.99)
    loan_amount = st.number_input('Loan Amount', min_value=0.0, step=1000.0, max_value = 9999999999.99)
    loan_term = st.number_input('Loan Term (months)', min_value=1, step=1, max_value = 99)
    cibil_score = st.number_input('CIBIL Score', min_value=300, max_value=900, step=1)
    residential_assets_value = st.number_input('Residential Assets Value', min_value=0.0, step=1000.0, max_value = 9999999999.99)
    commercial_assets_value = st.number_input('Commercial Assets Value', min_value=0.0, step=1000.0, max_value = 9999999999.99)
    luxury_assets_value = st.number_input('Luxury Assets Value', min_value=0.0, step=1000.0, max_value = 9999999999.99)
    bank_asset_value = st.number_input('Bank Asset Value', min_value=0.0, step=1000.0, max_value = 9999999999.99)
    
    if education == ' Graduate':
        education = 1
    else:
        education = 0
    
    if self_employed == ' Yes':
        self_employed = 1
    else:
        self_employed = 0
        
    #education =education.map({' Graduate': 1, ' Not Graduate': 0})
    #self_employed.map({' Yes':1, ' No': 0})
    
    user_data = list([no_of_dependents, education, self_employed, income_annum, loan_amount,
                     loan_term, cibil_score, residential_assets_value, commercial_assets_value, luxury_assets_value,
                     bank_asset_value])
    loan_data = pd.Series(user_data)
    
    loan_approve_or_not = predict(loan_data)
    
    if loan_approve_or_not == 1:
        loan_status = 'Approved'
        debt_cleared = 'N'
        loan_left = loan_amount
    else:
        loan_status = 'Rejected'
        debt_cleared = ' '
        loan_left = 0
    #loan_status = st.selectbox('Loan Status', ['Approved', 'Rejected'])

    if st.button('Submit'):
        add_loan(no_of_dependents, education, self_employed, income_annum, loan_amount,
                 loan_term, cibil_score, residential_assets_value, commercial_assets_value,
                 luxury_assets_value, bank_asset_value, loan_status, loan_left, debt_cleared)
        st.success('Loan details submitted successfully!')
        
        if loan_status == 'Approved':
            st.success("Congratulations, Loan Approved")
            
        else:
            st.warning("NOT APPROVED")

if __name__ == '__main__':
    loan_app()