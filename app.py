import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("food_nutrition_dataset_500.csv")

st.title("🥗 AI Wellness Coach")
st.write("Get personalized diet, calorie, and macronutrient recommendations")

# User input
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", 10, 100)
weight = st.number_input("Enter your weight (kg)", 30, 200)
height = st.number_input("Enter your height (cm)", 100, 250)
goal = st.selectbox("Select your goal", ["Lose Weight", "Maintain Weight", "Gain Muscle"])
diet_type = st.selectbox("Select diet type", ["Vegetarian", "Non-Vegetarian", "Vegan"])

if st.button("Get My Plan"):
    bmi = weight / ((height/100)**2)
    st.write(f"Hello {name}, your BMI is **{bmi:.2f}**")

    # Filter dataset
    if diet_type == "Vegetarian":
        plan = df[df["Type"]=="Veg"].sample(5)
    elif diet_type == "Non-Vegetarian":
        plan = df[df["Type"]=="Non-Veg"].sample(5)
    else:
        plan = df[df["Type"]=="Vegan"].sample(5)

    st.subheader("🍴 Suggested Meal Plan")
    st.dataframe(plan[["Food", "Calories", "Protein", "Carbs", "Fat", "Preparation"]])
