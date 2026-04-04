import streamlit as st
import numpy as np
import pickle
from PIL import Image

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="AI Medical System", layout="wide")

# =========================
# STYLE
# =========================
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #1b1f2a, #0e1117);
    color: white;
}
h1, h2, h3, label, p {
    color: white !important;
}
div.stButton > button {
    background: linear-gradient(135deg, #6c757d, #495057);
    color: white;
    border-radius: 10px;
}
section[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.06) !important;
    backdrop-filter: blur(18px);
}
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SESSION
# =========================
if "users" not in st.session_state:
    st.session_state.users = {"admin": "1234"}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = ""

# =========================
# LOGIN
# =========================
if not st.session_state.logged_in:

    st.title("🏥 AI Medical System")

    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")

        if st.button("Login"):
            if u in st.session_state.users and st.session_state.users[u] == p:
                st.session_state.logged_in = True
                st.session_state.user = u
                st.rerun()
            else:
                st.error("Invalid Credentials ❌")

    with tab2:
        nu = st.text_input("New Username")
        np = st.text_input("New Password", type="password")

        if st.button("Create Account"):
            st.session_state.users[nu] = np
            st.success("Account Created")

    st.stop()

# =========================
# SIDEBAR
# =========================
st.sidebar.image("company.png", width=120)
st.sidebar.markdown("## 🏥 MEDICAL AI SYSTEM")

st.sidebar.markdown(f"""
👤 Logged in: **{st.session_state.user}**
""")

menu = st.sidebar.selectbox(
    "📌 Navigation",
    [
        "Diabetes Prediction",
        "Heart Disease Prediction",
        "🧠 Stroke Prediction",
        "👨‍💻 About Me",
        "📘 About Project"
    ]
)

if st.sidebar.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.rerun()

# =========================
# LOAD MODELS
# =========================
diabetes_model = pickle.load(open("model.pkl", "rb"))
heart_model = pickle.load(open("model_heart.pkl", "rb"))
stroke_model = pickle.load(open("stroke_model_v2.pkl", "rb"))
stroke_scaler = pickle.load(open("stroke_scaler_v2.pkl", "rb"))

# =========================
# 🩸 DIABETES (FIXED 8 FEATURES)
# =========================
if menu == "Diabetes Prediction":

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.title("🩸 Diabetes Prediction")

    glucose = st.number_input("Glucose Level", 0, 300, 120)
    bp = st.number_input("Blood Pressure", 0, 200, 80)
    bmi = st.number_input("BMI", 0.0, 60.0, 25.0)
    age = st.number_input("Age", 1, 100, 30)
    insulin = st.number_input("Insulin", 0, 900, 80)

    # 🔥 ADD MISSING FEATURES (SAFE FIX)
    skin_thickness = st.number_input("Skin Thickness", 0, 100, 20)
    pregnancies = st.number_input("Pregnancies", 0, 10, 1)
    pedigree = st.number_input("Diabetes Pedigree", 0.0, 2.0, 0.5)

    if st.button("Predict Diabetes"):

        x = np.array([[glucose, bp, bmi, age, insulin,
                       skin_thickness, pregnancies, pedigree]])

        pred = diabetes_model.predict(x)[0]

        if pred == 1:
            st.error("🔴 High Risk of Diabetes")
        else:
            st.success("🟢 Low Risk of Diabetes")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# ❤️ HEART (FIXED 13 FEATURES)
# =========================
elif menu == "Heart Disease Prediction":

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.title("❤️ Heart Disease Prediction")

    features = []
    labels = [
        "age","sex","cp","trestbps","chol","fbs","restecg",
        "thalach","exang","oldpeak","slope","ca","thal"
    ]

    for l in labels:
        features.append(st.number_input(l, 0.0, 500.0, 1.0))

    if st.button("Predict Heart Disease"):

        x = np.array([features])

        pred = heart_model.predict(x)[0]

        if pred == 1:
            st.error("🔴 Heart Disease Risk")
        else:
            st.success("🟢 Normal Heart Condition")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# 🧠 STROKE (FIXED)
# =========================
elif menu == "🧠 Stroke Prediction":

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.title("🧠 Stroke Prediction")

    age = st.number_input("Age", 1, 100, 40)
    hypertension = st.number_input("Hypertension", 0, 1, 0)
    heart_disease = st.number_input("Heart Disease", 0, 1, 0)
    ever_married = st.number_input("Ever Married", 0, 1, 1)
    work_type = st.number_input("Work Type", 0, 4, 0)
    residence = st.number_input("Residence", 0, 1, 1)
    glucose = st.number_input("Glucose Level", 50.0, 300.0, 120.0)
    bmi = st.number_input("BMI", 10.0, 60.0, 25.0)
    gender = st.number_input("Gender", 0, 1, 1)
    smoking = st.number_input("Smoking", 0, 3, 0)

    if st.button("Predict Stroke"):

        x = np.array([[age, hypertension, heart_disease,
                       ever_married, work_type, residence,
                       glucose, bmi, gender, smoking]])

        x = stroke_scaler.transform(x)

        prob = stroke_model.predict_proba(x)[0][1]
        risk = prob * 100

        if risk < 40:
            st.success(f"🟢 Low Risk ({risk:.2f}%)")
        elif risk < 70:
            st.warning(f"🟡 Medium Risk ({risk:.2f}%)")
        else:
            st.error(f"🔴 High Risk ({risk:.2f}%)")

        st.progress(int(risk))

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# 👨‍💻 ABOUT ME (WITH IMAGE)
# =========================
elif menu == "👨‍💻 About Me":

    st.title("👨‍💻 About Me")

    img = Image.open("profile.jpg")  # <-- apni image file rakho
    st.image(img, width=200)

    st.markdown("""
    ## Sharif Ullah

    🎓 BS Artificial Intelligence  
    📍 Hazara University Mansehra  

    ### Skills:
    - Python
    - Machine Learning
    - Deep Learning
    - NLP
    - Computer Vision
    - Digital Image Processing

    ### Contact:
    📧 sharifullah7087@gmail.com
    """)

# =========================
# 📘 ABOUT PROJECT
# =========================
elif menu == "📘 About Project":

    st.title("📘 About Project")

    st.markdown("""
    ### 🏥 AI Medical Prediction System

    This project predicts:

    ✔ Diabetes  
    ✔ Heart Disease  
    ✔ Stroke  

    ### ⚡ Technologies:
    - Python
    - Streamlit
    - Machine Learning
    - Scikit-learn

    ### 🎯 Objective:
    Early disease detection using AI models to help medical decision making.

    ### ❤️ Purpose:
    For CODEALPHA AI Project
    """)