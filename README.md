# 🎓 Student Performance Prediction

A Machine Learning project that predicts whether a student will **PASS or FAIL** based on:

- Study Hours
- Attendance
- Previous Marks

## 🚀 Project Overview

In this project, multiple Machine Learning algorithms were trained and evaluated to predict student performance.

The models tested include:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- Naive Bayes

Cross-validation and hyperparameter tuning were also used to improve model selection.

## 🧠 Machine Learning

The final trained model is saved as:

`student_pass_fail_model.pkl`

The model takes three inputs:

1. Study Hours
2. Attendance
3. Previous Marks

and predicts:

- `1` → PASS
- `0` → FAIL

## 🌐 Streamlit Application

A Streamlit web application was created so users can enter student information and receive a prediction.

### Features

- Simple user interface
- Study Hours input
- Attendance input
- Previous Marks input
- PASS / FAIL prediction
- Trained ML model integration

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

## 📁 Project Structure

```text
ML Final Project/
│
├── Student Performance Prediction.ipynb
├── app.py
├── student_pass_fail_model.pkl
├── requirements.txt
└── README.md

## ▶️ How to Run

Install the required libraries:

```bash
pip install -r requirements.txt

Run the Streamlit application:

python -m streamlit run app.py

The application will open in the browser.

📊 Model Evaluation

The models were evaluated using cross-validation.

Hyperparameter tuning was also performed to find suitable model parameters.

🎯 Project Goal

The goal of this project is to demonstrate a complete Machine Learning workflow:

Data → Preprocessing → Model Training → Evaluation → Hyperparameter Tuning → Model Saving → Streamlit Deployment

👨‍💻 Author

Muhammad Shayan Khurshid

Machine Learning / AI Enthusiast