import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []

    common_passwords = ["password", "123456", "qwerty", "abc123", "letmein", "admin", "welcome"]
    if password.lower() in common_passwords:
        feedback.append("This password is commonly used and vulnerable")
        return 0, feedback

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    if len(password) >= 12:
        score += 1

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Use both uppercase and lowercase letters")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add at least one number")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$% etc.)")

    if score < 3:
        strength = "Weak 😟"
    elif score == 3:
        strength = "Medium 😐"
    elif score == 4:
        strength = "Strong 🙂"
    else:
        strength = "Very Strong 😎"

    return strength, feedback

st.title("Password Strength Checker")

password = st.text_input("Enter password", type="password", placeholder="Type your password here...")

if st.button("Check Strength"):
    if password:
        strength, feedback = check_password_strength(password)
        
        st.subheader("Result:")
        if strength == "Weak 😟":
            st.error(f"Strength: {strength}")
        elif strength == "Medium 😐":
            st.warning(f"Strength: {strength}")
        else:
            st.success(f"Strength: {strength}")
        
       
        if len(feedback) > 0:
            st.subheader("Improvement Suggestions:")
            for item in feedback:
                st.write(item)
    else:
        st.warning("Please enter a password")

st.markdown("---")
st.markdown("### Password Requirements:")
st.markdown("""
- Minimum 8 characters long (12+ recommended)
- Mix of uppercase and lowercase letters
- At least one number
- At least one special character (!@#$%^&* etc.)
""")