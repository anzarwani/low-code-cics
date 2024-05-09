# THIS CODE BRINGS TOGETHER ALL THE FUNCTIONS TO 
# CREATE A MULTI-PAGE APP

import streamlit as st
from loan_screen import loan_app
from admin import admin
from user import user_details
from info import info

st.title("Modern CICS Loan Approval Screen")
#st.write("Please Choose Desired Function in the Sidebar")
st.divider()

info()

st.divider()

option = st.sidebar.radio(
    "Please Choose Desired Option",
    ("Loan Application", "Admin", "User")
)

if option == "Loan Application":
    loan_app()
    
if option == "Admin":
    user = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")

# Add css to hide item with title "Show password text"
    st.markdown(
        """
    <style>
        [title="Show password text"] {
            display: none;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
    if user == 'admin' and password == 'admin':
        admin()
    elif user == "" and password == "":
        st.warning("Please Enter Credentials to Access Admin")
    else:
        st.warning("You Don't Have Access")
        
    
if option == "User":
    user_details()

