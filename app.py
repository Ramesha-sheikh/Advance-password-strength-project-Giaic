import streamlit as st
import re  

# ✅ Move `st.set_page_config()` to the first Streamlit command
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")

# Function to check password strength
def check_password_strength(password):
    strength = 0  
    missing_criteria = []  

    if len(password) >= 8:
        strength += 1  
    else:
        missing_criteria.append("🔴 At least 8 characters required")

    if re.search(r"[a-z]", password):
        strength += 1  
    else:
        missing_criteria.append("🟡 At least one lowercase letter (a-z) required")

    if re.search(r"[A-Z]", password):
        strength += 1  
    else:
        missing_criteria.append("🟡 At least one uppercase letter (A-Z) required")

    if re.search(r"\d", password):
        strength += 1  
    else:
        missing_criteria.append("🟡 At least one number (0-9) required")

    if re.search(r"[@$!%*?&#]", password):
        strength += 1  
    else:
        missing_criteria.append("🟡 At least one special character (@$!%*?&#) required")

    # Remarks & Color Coding
    if strength == 5:
        remarks = "🟢 Strong Password 💪"
        color = "green"
    elif strength >= 3:
        remarks = "🟡 Moderate Password 🙂"
        color = "orange"
    else:
        remarks = "🔴 Weak Password 😓"
        color = "red"

    return remarks, strength, missing_criteria, color

# Streamlit UI
st.markdown("""
    <style>
        .big-font { font-size:25px !important; font-weight: bold; }
        .stTextInput { border: 2px solid #4CAF50 !important; border-radius: 10px; padding: 10px; }
        .stButton>button { background-color: #4CAF50; color: white; font-size: 18px; padding: 10px; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

st.title("🔒 Password Strength Checker")

# Toggle password visibility
show_password = st.checkbox("👁 Show Password")

# Password input field
password = st.text_input("Enter your password:", type="default" if show_password else "password")

# Analyze button
if st.button("Analyze Password"):
    if password:
        strength_result, score, missing_criteria, color = check_password_strength(password)
        
        # Password strength result
        st.markdown(f"<p class='big-font' style='color:{color};'>{strength_result}</p>", unsafe_allow_html=True)

        # Progress bar for visual feedback
        st.progress(score / 5)

        # Display missing criteria (if any)
        if missing_criteria:
            st.warning("🔽 Improve your password by adding:")
            for criteria in missing_criteria:
                st.write(criteria)
        else:
            st.success("✅ Your password meets all security standards!")

# Sidebar for password guidelines
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2867/2867423.png", width=100)
st.sidebar.subheader("🔹 Password Guidelines:")
st.sidebar.markdown("""
- ✅ Minimum **8 characters**
- ✅ At least **one lowercase letter (a-z)**
- ✅ At least **one uppercase letter (A-Z)**
- ✅ At least **one number (0-9)**
- ✅ At least **one special character** (@$!%*?&#)
""")

# Footer
st.markdown("---")
st.markdown("📌 *A secure password helps protect your online accounts. Use a strong password!*")
