import streamlit as st
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


