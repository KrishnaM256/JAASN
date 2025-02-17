import streamlit as st

st.title("Login Form")

with st.form("login_form"):
    st.write("Please enter your credentials:")
    
    # Input fields
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    submitted = st.form_submit_button("Login")
    
    # If the form is submitted
    if submitted:
        if email and password:
            if email == "user@example.com" and password == "password123":
                st.success("Login successful!")
            else:
                st.error("Invalid email or password.")
        else:
            st.error("Please fill in all the fields.")