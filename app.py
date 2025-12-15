
import streamlit as st

st.set_page_config(page_title="Client Query Management System", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Login", "Client Page", "Support Dashboard"])

if page == "Login":
    from pages.login_page import app
    app()
elif page == "Client Page":
    from pages.client_page import app
    app()
else:
    from pages.support_dashboard import app
    app()
