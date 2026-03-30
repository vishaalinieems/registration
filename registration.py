import streamlit as st

st.title("User Registration Form")

# 1. Name
name = st.text_input("Enter your name")

# 2. Email
email = st.text_input("Enter your email")

# 3. Password
password = st.text_input("Enter your password", type="password")

# 4. Dropdown
role = st.selectbox("Select your role", ["Student", "Teacher", "Admin"])

# 5. Checkbox
agree = st.checkbox("I agree to the terms and conditions")

# Submit button
if st.button("Register"):
    if name and email and password and agree:
        st.success(f"Registration successful for {name} as {role}")
    else:
        st.error("Please fill all fields and accept terms")