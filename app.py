import streamlit as stimport streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="🥦 AI Wellness Coach", layout="wide")

st.title("🥦 AI Wellness Coach")
st.write("Your personalized nutrition assistant 🍽️")

# Load dataset
try:
    food_data = pd.read_csv("food_nutrition_dataset_500.csv")
except FileNotFoundError:
    st.error("❌ food_nutrition_dataset_500.csv not found. Please upload it.")
    uploaded_file = st.file_uploader("Upload your food_nutrition_dataset_500.csv", type=["csv"])
    if uploaded_file:
        food_data = pd.read_csv(uploaded_file)
    else:
        food_data = None

if food_data is not None:
    # -------------------------
    # User Inputs
    # -------------------------
    st.sidebar.header("👤 Your Profile")

    age = st.sidebar.number_input("Age", min_value=10, max_value=100, value=25)
    gender = st.sidebar.radio("Gender", ["Male", "Female"])
    weight = st.sidebar.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
    height = st.sidebar.number_input("Height (cm)", min_value=120, max_value=220, value=170)
    diet_pref = st.sidebar.radio("Diet Preference", ["Veg", "Non-Veg"])

    # -------------------------
    # BMR Calculation
    # -------------------------
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    daily_calories = round(bmr * 1.2, 0)  # sedentary lifestyle
    st.sidebar.markdown(f"### 🔥 Estimated Daily Calorie Needs: **{daily_calories} kcal**")

    # -------------------------
    # Personalized Diet Plan
    # -------------------------
    st.subheader("🥗 Generate Personalized Diet Plan")

    if st.button("Generate Diet Plan"):
        # Filter by diet preference
        if diet_pref == "Veg":
            filtered_foods = food_data[food_data["Type"] == "Veg"]
        else:
            filtered_foods = food_data.copy()  # Veg + Non-Veg

        # Simple random sampling for meals
        breakfast = filtered_foods.sample(1)
        lunch = filtered_foods.sample(2)
        dinner = filtered_foods.sample(2)

        st.write(f"### 🍳 Breakfast")
        st.dataframe(breakfast[["Food Name", "Calories", "Protein (g)", "Carbs (g)", "Fat (g)", "Preparation Style"]])

        st.write(f"### 🍲 Lunch")
        st.dataframe(lunch[["Food Name", "Calories", "Protein (g)", "Carbs (g)", "Fat (g)", "Preparation Style"]])

        st.write(f"### 🍛 Dinner")
        st.dataframe(dinner[["Food Name", "Calories", "Protein (g)", "Carbs (g)", "Fat (g)", "Preparation Style"]])

        # Total calories
        total_calories = breakfast["Calories"].sum() + lunch["Calories"].sum() + dinner["Calories"].sum()
        st.markdown(f"### 📊 Total Calories in Plan: **{total_calories} kcal**")
        st.markdown(f"💡 Your target is around **{daily_calories} kcal/day**.")


import pandas as pd

st.set_page_config(page_title="🥦 AI Wellness Coach", layout="wide")

st.title("🥦 AI Wellness Coach")
st.write("Your personalized nutrition assistant powered by food data 🍽️")

# Load food dataset
try:
    food_data = pd.read_csv("food_nutrition_dataset_500.csv")
    st.success("✅ Food dataset loaded successfully!")
except FileNotFoundError:
    st.error("❌ food_nutrition_dataset_500.csv not found in repo. Please upload it.")
    uploaded_file = st.file_uploader("Upload your food_nutrition_dataset_500.csv", type=["csv"])
    if uploaded_file:
        food_data = pd.read_csv(uploaded_file)
    else:
        food_data = None

if food_data is not None:
    # Show preview
    st.subheader("📋 Food Database Preview")
    st.dataframe(food_data.head(10))

    # Search bar
    st.subheader("🔍 Search for Food")
    query = st.text_input("Enter a food name (e.g., Paneer Curry, Brown Rice, Dal Tadka):")
    
    if query:
        results = food_data[food_data["Food Name"].str.contains(query, case=False, na=False)]
        if not results.empty:
            st.write(f"### Results for '{query}'")
            st.dataframe(results)
        else:
            st.warning("⚠️ No matching food found.")

    # Simple Meal Plan Suggestion
    st.subheader("🥗 Generate a Simple Meal Plan")
    if st.button("Suggest Meal Plan"):
        sample_meal = food_data.sample(3)  # pick 3 random foods
        st.write("Here’s a suggested balanced meal plan:")
        st.dataframe(sample_meal[["Food Name", "Calories", "Protein (g)", "Carbs (g)", "Fat (g)", "Preparation Style"]])



