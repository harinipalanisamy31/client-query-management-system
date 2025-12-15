
import streamlit as st, bcrypt
from database.db_connection import get_connection

def app():
    st.title("Login / Register")

    action = st.radio("Action", ["Login", "Register"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["client", "support"])

    conn = get_connection()
    cursor = conn.cursor()

    if st.button(action):
        if action == "Register":
            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            cursor.execute(
                "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                username, hashed.decode(), role
            )
            conn.commit()
            st.success("User registered successfully")

        else:
            cursor.execute(
                "SELECT role FROM users WHERE username=? AND password_hash=?",
                username, password
            )
            user = cursor.fetchone()
            if user:
                st.session_state["role"] = user[0]
                st.success("Login successful")
            else:
                st.error("Invalid credentials")
