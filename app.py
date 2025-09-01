import streamlit as st
import random

# Food options based on preference
food_options = {
    "veg": ["Paneer", "Dal", "Rice", "Roti", "Salad", "Vegetable Curry", "Fruits", "Daliya", "Poha", "Upma"],
    "non-veg": ["Chicken", "Eggs", "Fish", "Rice", "Roti", "Salad", "Vegetable Curry", "Fruits", "Paneer", "Dal"],
    "vegan": ["Tofu", "Dal", "Rice", "Roti", "Salad", "Vegetable Curry", "Fruits", "Oats", "Quinoa", "Sprouts"]
}

def calculate_calories(age, gender, weight, height):
    # Mifflin St Jeor Formula for BMR
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return round(bmr * 1.2)  # sedentary activity multiplier

def generate_diet(preference, daily_calories):
    foods = food_options.get(preference, [])
    if not foods:
        return {"Error": "Invalid diet preference"}

    plan = {
        "Breakfast": random.sample(foods, 2),
        "Lunch": random.sample(foods, 3),
        "Dinner": random.sample(foods, 3)
    }
    return plan

# Streamlit UI
st.title("🥗 Personalized Diet Plan Generator")

age = st.number_input("Enter your age:", min_value=10, max_value=100, step=1)
gender = st.radio("Select your gender:", ["Male", "Female"])
weight = st.number_input("Enter your weight (kg):", min_value=20, max_value=200, step=1)
height = st.number_input("Enter your height (cm):", min_value=100, max_value=250, step=1)
preference = st.selectbox("Select diet preference:", ["veg", "non-veg", "vegan"])

if st.button("Generate My Diet Plan"):
    daily_calories = calculate_calories(age, gender, weight, height)
    diet_plan = generate_diet(preference, daily_calories)
    
    st.subheader("Your Personalized Diet Plan")
    st.write(f"Recommended Daily Calories: **{daily_calories} kcal**")
    for meal, items in diet_plan.items():
        st.write(f"**{meal}**: {', '.join(items)}")
