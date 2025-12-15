
import streamlit as st
from database.db_connection import get_connection

def app():
    st.title("Submit Query")
    email = st.text_input("Email")
    mobile = st.text_input("Mobile Number")
    heading = st.text_input("Query Heading")
    desc = st.text_area("Query Description")

    if st.button("Submit"):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO queries (mail_id, mobile_number, query_heading, query_description, status) VALUES (?, ?, ?, ?, ?)",
            email, mobile, heading, desc, "Open"
        )
        conn.commit()
        st.success("Query submitted successfully")
