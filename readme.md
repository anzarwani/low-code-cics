# CobLoan - A Low Code CICS Interface Demonstration

## Story time

In the year 2300, after an apocalypse reshapes the world, two brilliant engineers, John Cob and John Py, stumble upon an ancient mainframe and a desktop computer. Seeing an opportunity to help in a world desperate for loans, they combine the COBOL with Python, SQL, and Streamlit to create a loan application system. 

They revamp the trivial CICS interface into a Low-code streamlit UI, moving past the black and green screens of the past. To ensure quick disbursement of loans, they integrate a machine learning loan approval model using CatBoost, boasting an impressive 97 percent accuracy rate. Since, the loan applications are too many, they rely on COBOL batch processing programs to process and do accounting for loan applications. 

Their creation becomes a beacon of hope in uncertain times, showcasing the resilience of human innovation in the face of adversity.

## Why Low-Code CICS approach?

- A shift from Java to create web interfaces which itself is essentially a 'legacy' approach.
- Modern clickable UI.
- No need of extra engineering talent, exisiting COBOL devs and DB Devs can do changes with very less effort.
- Easier to debug.
- Easy to integrate Machine Learning.
- Modern COBOL + Low Code CICS would reduce codebase.
- Make mainframes fun again.

## Workflow

Streamlit UI app which imitates a CICS interface -> Data Input -> ML Model determines loan approved or not -> sqlite3 DB populated -> a python script creates a batch processing file -> file processed through COBOL program -> updated file is created -> this file updates database.

## Demo

![Home](https://github.com/anzarwani/low-code-cics/blob/main/screenshots/home.png)
![Loan Approved](https://github.com/anzarwani/low-code-cics/blob/main/screenshots/loan_approved.png)
![Admin](https://github.com/anzarwani/low-code-cics/blob/main/screenshots/admin.png)
![Batch File for COBOL](https://github.com/anzarwani/low-code-cics/blob/main/screenshots/batch_file.png)

## Tools used

- Raincode for VS
- Visual Studio
- Streamlit
- sqlite3
- Python

## Steps

- pip install streamlit
- Run create_db.py (This creates sqlite3 DB)
- In cmd, enter 'streamlit run home.py'
- Apply for a loan (use high CIBIL score and low loan amount, and high asset values for loan approval)
- CTRL + C in terminal to terminate streamlit session.
- Run batch_file.py
- Run PROCESS.CBL in VS Code (or any COBOL environment you have)
- Run update_db.py
- In cmd, enter 'streamlit run home.py'
- Now, you can see admin as well as user functions as well.
- Admin Credentials are 'admin' and 'admin'

## Automation

I have yet to work on automation which will essentially eliminate manual running of python scripts therefore make it just 1 streamlit session.

## Enhancements

- Manual Approval of Loans
- Filtering and Sorting
- Ability to run COBOL code in a Streamlit session.

## Further Steps

Since, I am not really good at C programming language. COBOL allows us to create a DB connection to sqlite3 by incorporating a C code snippet, this will eliminate the 'update_db' step. I did try but failed. Contributions are welcome.








