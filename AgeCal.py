import streamlit as st
from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    full_year_passed = (today.month, today.day) < (birth_date.month, birth_date.day)
    if not full_year_passed:
        age -= 1
    return age

def main():
    st.title("RCM Age Calculator")
    user_birth_date = st.date_input("Enter your date of birth:", min_value=date(1900, 1, 1))
    if user_birth_date:
        user_age = calculate_age(user_birth_date)
        st.write(f"You are approximately **{user_age} years old**.")
        st.balloons()
        if 20 <= user_age <= 29:
            st.write("You are a **baby** :baby: in RCM!")
            st.balloons()
        if 30 <= user_age <= 39:
            st.write("You are **young** :boy: in RCM!")
            st.balloons()
        if 40 <= user_age <= 50:
            st.write("You are an **adult** :man: in RCM!")
            st.balloons()
        

if __name__ == "__main__":
    main()
