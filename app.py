import streamlit as st
import pandas as pd
import random

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
# Load Food Database (CSV)
# ----------------------------
@st.cache_data
def load_food_data():
    try:
        df = pd.read_csv("foods.csv")  # <-- make sure your CSV file is named foods.csv in repo
        return df
    except Exception as e:
        st.error(f"Error loading food data: {e}")
        return pd.DataFrame()

food_df = load_food_data()

# ----------------------------
# Generate Meal Plan
# ----------------------------
st.subheader("🥦 Suggested Meal Plan")

if not food_df.empty:
    # Pick random 5 meals (for variety)
    sample_meals = food_df.sample(5, random_state=random.randint(1, 1000))

    st.dataframe(sample_meals)

    # ----------------------------
    # Wellness Recommendation
    # ----------------------------
    st.subheader("📋 Wellness Recommendation")

    if goal == "Weight Loss":
        st.info("👉 Focus on high-protein, low-carb meals. Include cardio exercises 4-5 times/week.")
    elif goal == "Muscle Gain":
        st.info("👉 Increase protein intake and strength training. Ensure calorie surplus with balanced macros.")
    else:
        st.info("👉 Maintain a balanced diet with moderate portions. Stay active and hydrated.")

    st.success("✅ Your personalized wellness plan has been generated!")
else:
    st.warning("⚠️ No food database found. Please upload a valid foods.csv file.")
