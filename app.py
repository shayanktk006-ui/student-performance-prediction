import streamlit as st
import pandas as pd
import joblib

# Load trained ML model
model = joblib.load("student_pass_fail_model.pkl")

# App title
st.title("🎓 Student Performance Prediction")

st.write("Enter student information to predict Pass or Fail.")

# User inputs
study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

previous_marks = st.number_input(
    "Previous Marks",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

# Prediction button
if st.button("Predict"):
    
    new_student = pd.DataFrame(
        [[study_hours, attendance, previous_marks]],
        columns=["StudyHours", "Attendance", "PreviousMarks"]
    )

    prediction = model.predict(new_student)

    if prediction[0] == 1:
        st.success("🎉 Student will PASS")
    else:
        st.error("❌ Student will FAIL")