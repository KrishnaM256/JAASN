import streamlit as st

# Mock data for logged-in users and their roles
users = [
    {"name": "Alice", "email": "alice@example.com", "role": "User"},
    {"name": "Bob", "email": "bob@example.com", "role": "Editor"},
    {"name": "Charlie", "email": "charlie@example.com", "role": "Admin"},
]

# Initialize session state to store roles
if "roles" not in st.session_state:
    st.session_state.roles = ["User", "Editor", "Admin"]

# Title of the admin dashboard
st.title("Admin Dashboard")

# Section to add new roles
st.header("Add New Role")
new_role = st.text_input("Enter a new role name")
if st.button("Add Role"):
    if new_role and new_role not in st.session_state.roles:
        st.session_state.roles.append(new_role)
        st.success(f"Role '{new_role}' added successfully!")
    elif new_role in st.session_state.roles:
        st.error(f"Role '{new_role}' already exists.")

# Display logged-in users
st.header("Logged-in Users")
if users:
    for user in users:
        st.write(f"**Name:** {user['name']}, **Email:** {user['email']}, **Role:** {user['role']}")
        
        # Dropdown to assign roles (dynamic based on available roles)
        new_role = st.selectbox(
            f"Assign a new role to {user['name']}",
            st.session_state.roles,
            key=user["email"],  # Unique key for each user
        )
        
        # Button to update role
        if st.button(f"Update Role for {user['name']}", key=f"update_{user['email']}"):
            user["role"] = new_role
            st.success(f"Updated {user['name']}'s role to {new_role}.")
else:
    st.write("No users are currently logged in.")

# Optional: Add a logout button for the admin
if st.button("Logout"):
    st.write("Admin has been logged out.")