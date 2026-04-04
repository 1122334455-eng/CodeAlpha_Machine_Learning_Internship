:

🏥 CodeAlpha Medical AI System (Task 4)
🚀 AI-Powered Disease Prediction System

This project is a Machine Learning-based Medical Prediction System built using Streamlit.
It predicts the risk of:

🩸 Diabetes
❤️ Heart Disease
🧠 Stroke

The goal is early disease detection using AI to assist in medical decision-making.

📌 Features

✔ User Authentication (Login/Signup)
✔ Diabetes Prediction Model
✔ Heart Disease Prediction Model
✔ Stroke Risk Prediction Model
✔ Interactive Web UI (Streamlit)
✔ Real-time Prediction Results
✔ Risk Level Indicator (Low / Medium / High)
✔ Beautiful Dark Medical UI

Machine Learning Models Used
Logistic Regression / Classification Models
StandardScaler for preprocessing
Trained using Scikit-learn
📁 Project Structure
CodeAlpha_Medical_AI_Task4/
│
├── app.py                      # Main Streamlit Application
├── model.pkl                   # Diabetes Prediction Model
├── model_heart.pkl            # Heart Disease Model
├── stroke_model_v2.pkl        # Stroke Prediction Model
├── stroke_scaler_v2.pkl       # Stroke Data Scaler
│
├── profile.jpg                # Developer Profile Image
├── company.png                # Sidebar Logo/Image
│
├── requirements.txt           # Required Libraries
├── README.md                  # Project Documentation
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/CodeAlpha_Medical_AI_Task4.git
cd CodeAlpha_Medical_AI_Task4
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Application
streamlit run app.py
🌐 Requirements

Make sure you have:

Python 3.8+
pip installed
Streamlit installed
📦 requirements.txt
streamlit
numpy
scikit-learn
pillow
🖥️ How It Works
User logs in / signs up
Select disease from sidebar:
Diabetes
Heart Disease
Stroke
Enter medical inputs
Click Predict
System shows risk level:
🟢 Low Risk
🟡 Medium Risk
🔴 High Risk
🧠 Stroke Prediction Logic
Uses 10 input medical features
Data is scaled using StandardScaler
Model predicts probability of stroke
Risk percentage displayed using progress bar
🎯 Objective

To build an AI-based medical assistant that helps in:

Early disease detection
Risk assessment
Supporting healthcare decisions
👨‍💻 Developer

Sharif Ullah
🎓 BS Artificial Intelligence
🏫 Hazara University Mansehra
📧 sharifullah7087@gmail.com

🏆 Project Status

✔ Completed for CodeAlpha Internship Task 4
✔ Fully Functional
✔ Ready for Deployment

🚀 Future Improvements
Add hospital database (SQLite)
PDF medical report generation
Deploy on Streamlit Cloud
Add more diseases
Improve model accuracy with deep learning
⭐ If you like this project

Give a ⭐ on the repository and connect with me!
