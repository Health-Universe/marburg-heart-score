import streamlit as st

def calculate_mhs(age, gender, number_of_coronary_risk_factors, known_not_coronary_heart_disease, pain_character):
    # Assuming each input is correctly validated and transformed to the score's requirements
    # Add logic to calculate the Marburg Heart Score based on the inputs
    score = 0
    # Example calculation, replace with actual logic
    score += age
    score += 1 if gender == 'Male' else 0
    score += number_of_coronary_risk_factors
    score += 2 if known_not_coronary_heart_disease else 0
    score += 3 if pain_character == 'Non-anginal' else 0
    return score


st.title("Marburg Heart Score Calculator")

with st.form("mhs_form"):
    age = st.number_input("Age", min_value=18, max_value=100)
    gender = st.selectbox("Gender", ["Male", "Female"])
    number_of_coronary_risk_factors = st.number_input("Number of Coronary Risk Factors", min_value=0, max_value=10)
    known_not_coronary_heart_disease = st.checkbox("Known Non-Coronary Heart Disease")
    pain_character = st.selectbox("Pain Character", ["Anginal", "Atypical Anginal", "Non-anginal"])

    submitted = st.form_submit_button("Calculate MHS")
    if submitted:
        score = calculate_mhs(age, gender, number_of_coronary_risk_factors, known_not_coronary_heart_disease, pain_character)
        st.write("Marburg Heart Score:", score)
        # Here you can add interpretation of the score
