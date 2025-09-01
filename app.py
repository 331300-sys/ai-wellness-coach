import streamlit as st
import pandas as pd

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="AI Wellness Coach", page_icon="🥗", layout="centered")

st.title("🥗 AI Wellness Coach")
st.write("Get a personalized meal plan based on your health goals 🚀")

# ----------------------------
# User Input
# ----------------------------
goal = st.selectbox(
    "Select your health goal:",
    ["Weight Loss", "Muscle Gain", "General Wellness"]
)

age = st.number_input("Enter your age:", min_value=10, max_value=100, value=25)
weight = st.number_input("Enter your weight (kg):", min_value=30, max_value=200, value=70)
activity = st.selectbox("Select your activity level:", ["Low", "Medium", "High"])

# ----------------------------
# Sample Meal Plan Data
# ----------------------------
meal_data = [
    {"Food": "Oatmeal with Fruits", "Calories": 300, "Protein": 10, "Carbs": 50, "Fat": 5, "Preparation Time": "10 mins"},
    {"Food": "Grilled Chicken Salad", "Calories": 400, "Protein": 35, "Carbs": 20, "Fat": 10, "Preparation Time": "15 mins"},
    {"Food": "Brown Rice with Veggies", "Calories": 450, "Protein": 12, "Carbs": 60, "Fat": 8, "Preparation Time": "20 mins"},
    {"Food": "Protein Smoothie", "Calories": 250, "Protein": 20, "Carbs": 30, "Fat": 5, "Preparation Time": "5 mins"},
]

plan = pd.DataFrame(meal_data)

# ----------------------------
# Meal Plan Recommendation
# ----------------------------
st.subheader("🥦 Suggested Meal Plan")

# Display dataframe safely (avoid KeyError)
if not plan.empty:
    st.dataframe(plan)
else:
    st.warning("⚠️ No meal plan available. Please try again later.")

# ----------------------------
# Summary Recommendation
# ----------------------------
st.subheader("📋 Wellness Recommendation")

if goal == "Weight Loss":
    st.info("👉 Focus on high-protein, low-carb meals. Include cardio exercises 4-5 times/week.")
elif goal == "Muscle Gain":
    st.info("👉 Increase protein intake and strength training. Ensure calorie surplus with balanced macros.")
else:
    st.info("👉 Maintain a balanced diet with moderate portions. Stay active and hydrated.")

st.success("✅ Your personalized wellness plan has been generated!")
