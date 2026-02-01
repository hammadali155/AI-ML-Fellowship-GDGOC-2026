#module imports
import streamlit as st
import pandas as pd
from datetime import date
import os

#local imports
from logger_pkg import StudyLog, ExpenseLog, LogTracker, FileHandler


DATA_FILE = os.path.join("data", "logs.csv")

st.set_page_config(page_title="Fellowship Study & Expense Tracker", layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: block;}
            footer {visibility: block;}
            header {visibility: block;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("Fellowship Study & Expense Tracker")
st.markdown("---")

tracker = LogTracker()
saved_data = FileHandler.load_logs(DATA_FILE)

st.sidebar.header("Add New Entry")
category = st.sidebar.selectbox("Category", ["Study", "Expense"])

with st.sidebar.form("entry_form", clear_on_submit=True):
    entry_date = st.date_input("Date", date.today())
    description = st.text_input("Description", placeholder="e.g., Deep Learning Workshop or New Laptop")
    
    if category == "Study":
        value = st.number_input("Hours Spent", min_value=0.1, max_value=24.0, value=1.0, step=0.5)
        submit_btn = st.form_submit_button("Log Study Session")
    else:
        value = st.number_input("Amount ($)", min_value=0.01, value=10.0, step=1.0)
        submit_btn = st.form_submit_button("Log Expense")

    if submit_btn:
        if not description:
            st.error("Please provide a description.")
        else:
            try:
                if category == "Study":
                    new_entry = StudyLog(entry_date.strftime("%Y-%m-%d"), description, value)
                else:
                    new_entry = ExpenseLog(entry_date.strftime("%Y-%m-%d"), description, value)
                
                current_logs = saved_data + [new_entry.to_dict()]
                FileHandler.save_logs(DATA_FILE, current_logs)
                st.success(f"Added {category} entry successfully!")
                saved_data = FileHandler.load_logs(DATA_FILE)
            except Exception as e:
                st.error(f"Failed to save: {e}")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("All Logs")
    if saved_data:
        df = pd.DataFrame(saved_data)
        st.dataframe(df, use_container_width=True)
        
        if st.button("Clear All Data"):
            if os.path.exists(DATA_FILE):
                os.remove(DATA_FILE)
                st.warning("Data cleared. Please refresh the page.")
                st.rerun()
    else:
        st.info("No logs found. Add your first entry from the sidebar!")

with col2:
    st.subheader("Quick Stats")
    if saved_data:
        df = pd.DataFrame(saved_data)
        study_hours = df[df['Category'] == 'Study']['Hours/Amount'].sum()
        total_expense = df[df['Category'] == 'Expense']['Hours/Amount'].sum()
        
        st.metric("Total Study Hours", f"{study_hours} hrs")
        st.metric("Total Expenses", f"${total_expense:,.2f}")
    else:
        st.write("Complete your first task to see stats!")

st.markdown("---")
