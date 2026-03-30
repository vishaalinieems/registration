import streamlit as st

st.title("User Registration Form")
st.image("sunrise.jpg", caption="Sunrise by the mountains")

# 1. Name
name = st.text_input("Enter your name")

# 2. Email
email = st.text_input("Enter your email")

# 3. Gender (Radio Button)
gender = st.radio("Select your gender", ["Male", "Female"])

# 4. Dropdown
role = st.selectbox("Select your role", ["Student", "Teacher", "Admin"])

# 5. Checkbox
agree = st.checkbox("I agree to the terms and conditions")

# Submit button
if st.button("Register"):
    if name and email and gender and agree:
        st.success(f"Registration successful for {name} ({gender}) as {role}")
    else:
        st.error("Please fill all fields and accept terms")
