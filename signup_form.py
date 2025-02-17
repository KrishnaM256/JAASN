import streamlit as st

st.title("Signup Form")

with st.form("signup_form"):
    st.write("Please fill in the details below:")
    
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    submitted = st.form_submit_button("Sign Up")
    
    if submitted:
        if name and email and password:
            st.success("Signup successful!")
            st.write(f"Name: {name}")
            st.write(f"Email: {email}")
            st.write(f"Password: {password}")  
        else:
            st.error("Please fill in all the fields.")