# 🏥 AI Medical Prediction System (Task 4 - CodeAlpha Internship)

## 📌 Overview
This project is an AI-powered medical diagnosis system that predicts:

- 🩸 Diabetes
- ❤️ Heart Disease
- 🧠 Stroke Risk

It is developed using Machine Learning and deployed using Streamlit with a user-friendly interface.

---

## 🚀 Features
- Multi-Disease Prediction System
- Interactive Streamlit Web App
- Data Preprocessing & Cleaning
- Handling Missing Values
- Class Imbalance Handling (SMOTE)
- Feature Scaling (StandardScaler)
- Model Training & Evaluation
- Probability-Based Risk Output (Stroke)

---

## 🧠 Machine Learning Models Used

### 🩸 Diabetes Prediction
- Random Forest Classifier
- Feature Scaling (StandardScaler)
- Evaluation using Accuracy & Confusion Matrix

### ❤️ Heart Disease Prediction
- Random Forest Classifier
- Train-Test Split
- Accuracy Evaluation (~98%+)

### 🧠 Stroke Prediction
- XGBoost Classifier
- SMOTE for class balancing
- Label Encoding
- Probability threshold tuning
- ROC-AUC evaluation

---

## ⚙️ Tech Stack
- Python 🐍
- Pandas & NumPy
- Scikit-learn
- XGBoost
- Imbalanced-learn (SMOTE)
- Streamlit (Frontend)
- Matplotlib & Seaborn

---
# 🏥 AI Medical Prediction System (Task 4 - CodeAlpha Internship)

## 📌 Overview
This project is an AI-powered medical diagnosis system that predicts:

- 🩸 Diabetes
- ❤️ Heart Disease
- 🧠 Stroke Risk

It is developed using Machine Learning and deployed using Streamlit with a user-friendly interface.

---

## 🚀 Features
- Multi-Disease Prediction System
- Interactive Streamlit Web App
- Data Preprocessing & Cleaning
- Handling Missing Values
- Class Imbalance Handling (SMOTE)
- Feature Scaling (StandardScaler)
- Model Training & Evaluation
- Probability-Based Risk Output (Stroke)

---

## 🧠 Machine Learning Models Used

### 🩸 Diabetes Prediction
- Random Forest Classifier
- Feature Scaling (StandardScaler)
- Evaluation using Accuracy & Confusion Matrix

### ❤️ Heart Disease Prediction
- Random Forest Classifier
- Train-Test Split
- Accuracy Evaluation (~98%+)

### 🧠 Stroke Prediction
- XGBoost Classifier
- SMOTE for class balancing
- Label Encoding
- Probability threshold tuning
- ROC-AUC evaluation

---

## ⚙️ Tech Stack
- Python 🐍
- Pandas & NumPy
- Scikit-learn
- XGBoost
- Imbalanced-learn (SMOTE)
- Streamlit (Frontend)
- Matplotlib & Seaborn

---

## 📁 Project Structure
CodeAlpha_Medical_AI_System_Task4/
│
├── app.py
├── model.pkl
├── model_heart.pkl
├── stroke_model_v2.pkl
├── stroke_scaler_v2.pkl
├── stroke_encoders_v2.pkl
│
├── data/
│ ├── diabetes.csv
│ ├── heart.csv
│ └── healthcare-dataset-stroke-data.csv
│
├── images/
│ ├── company.png
│ └── profile.jpg
│
├── requirements.txt
└── README.md

---

## ▶️ How to Run

### 1️⃣ Clone Repository
```bash
git clone https://github.com/1122334455-eng/CodeAlpha_Machine_Learning_Internship.git
cd CodeAlpha_Medical_AI_Task4
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Streamlit App
streamlit run app.py
📊 Model Performance
🩸 Diabetes Model
Accuracy: ~81%
❤️ Heart Disease Model
Accuracy: ~98%
🧠 Stroke Model
Accuracy: ~87%
ROC-AUC: ~0.84
🎯 Key Techniques Used
Data Cleaning
Feature Engineering
Standard Scaling
Label Encoding
SMOTE (Oversampling)
Ensemble Learning
XGBoost Optimization
Probability Threshold Tuning
Model Serialization (Pickle)
🏢 Internship

This project is part of:

CodeAlpha Machine Learning Internship

👨‍💻 Author

Sharif Ullah
📧 Email: sharifullah7087@gmail.com

🎓 BS Artificial Intelligence
📍 Hazara University Mansehra

⭐ Future Improvements
Add Deep Learning models
Deploy on Cloud (AWS/Heroku)
Improve UI/UX
Add more diseases
