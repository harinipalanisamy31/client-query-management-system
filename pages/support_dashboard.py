
import streamlit as st
import pandas as pd
from database.db_connection import get_connection

def app():
    st.title("Support Dashboard")
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM queries", conn)

    st.dataframe(df)

    if not df.empty:
        qid = st.selectbox("Close Query ID", df[df['status']=="Open"]['query_id'])
        if st.button("Close Query"):
            cur = conn.cursor()
            cur.execute(
                "UPDATE queries SET status='Closed', query_closed_time=GETDATE() WHERE query_id=?",
                qid
            )
            conn.commit()
            st.success("Query closed")
