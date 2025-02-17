import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.name = ""
    st.session_state.is_admin = False

# Function to login user
def login_user(email, password):
    response = requests.post(f"{API_BASE_URL}/login", json={"email": email, "password": password})
    
    if response.status_code == 200:
        data = response.json()
        st.write(data)  # Debugging: Print the response structure

        # Handle response data safely
        st.session_state.logged_in = True
        st.session_state.name = data.get("name", "")  # Avoid KeyError
        st.session_state.is_admin = data.get("is_admin", False)  # Avoid KeyError
        st.rerun()  # Rerun to update UI
    else:
        st.error("Invalid Credentials")

# UI when logged in
if st.session_state.logged_in:
    st.title(f"Welcome, {st.session_state.name}")
    st.write("You have successfully logged in.")

    if st.session_state.is_admin:
        st.subheader("Admin Dashboard")
        st.write("You have admin privileges.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.name = ""
        st.session_state.is_admin = False
        st.rerun()

# UI when not logged in
else:
    st.title("Authentication System")
    
    # Tabs for different sections
    tab1, tab2, tab3 = st.tabs(["User Registration", "Admin Registration", "User/Admin Login"])

    # User Registration
    with tab1:
        st.subheader("Register as a User")
        new_name = st.text_input("Full Name")
        new_email = st.text_input("Email")
        new_password = st.text_input("Password", type="password")

        if st.button("Register"):
            if new_name and new_email and new_password:
                response = requests.post(f"{API_BASE_URL}/register", json={"name": new_name, "email": new_email, "password": new_password})
                if response.status_code == 200:
                    st.success("Registration Successful! You can now log in.")
                else:
                    st.error("Email already registered.")
            else:
                st.warning("Please fill in all fields.")

    # Admin Registration
    with tab2:
        st.subheader("Register as Admin")
        admin_name = st.text_input("Full Name", key="admin_name")
        admin_email = st.text_input("Email", key="admin_email")
        admin_password = st.text_input("Password", type="password", key="admin_password")

        if st.button("Register as Admin"):
            if admin_name and admin_email and admin_password:
                response = requests.post(f"{API_BASE_URL}/register-admin", json={"name": admin_name, "email": admin_email, "password": admin_password})
                if response.status_code == 200:
                    st.success("Admin Registered Successfully! Now log in.")
                else:
                    st.error("Email already registered.")
            else:
                st.warning("Please fill in all fields.")

    # Login (User/Admin)
    with tab3:
        st.subheader("Login as User or Admin")
        login_email = st.text_input("Email", key="login_email")
        login_password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login"):
            if login_email and login_password:
                login_user(login_email, login_password)
            else:
                st.warning("Please enter email and password!")
