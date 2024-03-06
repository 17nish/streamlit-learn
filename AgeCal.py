import streamlit as st
from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    full_year_passed = (today.month, today.day) < (birth_date.month, birth_date.day)
    if not full_year_passed:
        age -= 1
    return age

   

def get_zodiac_sign(birth_date):
    # Predefined list of zodiac signs and date ranges
    zodiac_signs = [
        ("Aries", (3, 21), (4, 19)),
        ("Taurus", (4, 20), (5, 20)),
        ("Gemini", (5, 21), (6, 20)),
        ("Cancer", (6, 21), (7, 22)),
        ("Leo", (7, 23), (8, 22)),
        ("Virgo", (8, 23), (9, 22)),
        ("Libra", (9, 23), (10, 22)),
        ("Scorpio", (10, 23), (11, 21)),
        ("Sagittarius", (11, 22), (12, 21)),
        ("Capricorn", (12, 22), (12, 31)),
        ("Capricorn", (1, 1), (1, 19)),
        ("Aquarius", (1, 20), (2, 18)),
        ("Pisces", (2, 19), (3, 20))
    ]

    for sign, (start_month, start_day), (end_month, end_day) in zodiac_signs:
        if (start_month, start_day) <= (birth_date.month, birth_date.day) <= (end_month, end_day):
            return sign

    return "Unknown"

def main():
    st.title("RCM Age Calculator")
    user_birth_date = st.date_input("Enter your date of birth:", min_value=date(1900, 1, 1))
    if user_birth_date:
        user_age = calculate_age(user_birth_date)
        zodiac_sign = get_zodiac_sign(user_birth_date)
       
        st.write(f"You are approximately **{user_age} years old**.")
        st.write(f"Your zodiac sign is **{zodiac_sign}**.")
    
        st.balloons()
        if 20 <= user_age <= 29:
            st.write("You are a **baby** :baby: in RCM!")
         
            st.balloons()
        if 30 <= user_age <= 39:
            st.write("You are **young** :boy: in RCM!")
           
            st.balloons()
        if 40 <= user_age <= 50:
            st.write("You are an **adult** :man: in RCM!")
        difference_age = 39-user_age         # calculating diffrence beetween the age.
       
        if difference_age > 0:
          st.write(f"Your **{difference_age}** years younger than Average Norwegian age.")
        elif difference_age < 0:
             difference_age =abs(difference_age)
             st.write(f"Your **{abs(difference_age)}** years older than Average Norwegian age.")
        else:
         st.write(f"Your age is same as Average Norwegian age.")
            
        st.balloons()
        

if __name__ == "__main__":
    main()
