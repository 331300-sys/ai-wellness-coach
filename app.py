import streamlit as st
import random
from fpdf import FPDF

# ------------------ Food Options ------------------ #
food_options = {
    "veg": {
        "breakfast": ["Oats with fruits", "Poha", "Upma", "Paneer sandwich", "Daliya", "Idli-Sambar"],
        "lunch": ["Dal", "Rice", "Roti", "Vegetable curry", "Paneer bhurji", "Curd", "Salad"],
        "dinner": ["Vegetable pulao", "Mixed veg curry", "Chapati", "Moong dal", "Soup", "Salad"],
        "snacks": ["Sprouts", "Fruit salad", "Dry fruits", "Green tea with nuts"]
    },
    "non-veg": {
        "breakfast": ["Egg omelette", "Boiled eggs", "Chicken sandwich", "Oats with milk", "Idli-Sambar"],
        "lunch": ["Chicken curry", "Fish fry", "Egg curry", "Rice", "Chapati", "Dal", "Salad"],
        "dinner": ["Grilled chicken", "Fish curry", "Vegetable curry", "Chapati", "Soup", "Salad"],
        "snacks": ["Boiled eggs", "Fruit salad", "Dry fruits", "Yogurt with seeds"]
    },
    "vegan": {
        "breakfast": ["Tofu scramble", "Oats with almond milk", "Smoothie bowl", "Quinoa porridge"],
        "lunch": ["Dal", "Brown rice", "Chapati", "Veg curry", "Tofu stir fry", "Salad"],
        "dinner": ["Quinoa pulao", "Vegetable curry", "Soup", "Chapati", "Sprouts salad"],
        "snacks": ["Roasted chickpeas", "Fruit salad", "Dry fruits", "Herbal tea"]
    }
}

# ------------------ Calorie Calculator ------------------ #
def calculate_calories(age, gender, weight, height):
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return round(bmr * 1.2)  # sedentary activity multiplier

# ------------------ Diet Generator ------------------ #
def generate_diet(preference, daily_calories):
    foods = food_options.get(preference, {})
    if not foods:
        return {"Error": "Invalid diet preference"}

    plan = {
        "Breakfast": random.sample(foods["breakfast"], 2),
        "Lunch": random.sample(foods["lunch"], 3),
        "Snacks": random.sample(foods["snacks"], 2),
        "Dinner": random.sample(foods["dinner"], 3),
        "Hydration": "Drink at least 2.5 – 3 litres of water daily 💧"
    }

    return plan

# ------------------ PDF Export ------------------ #
def create_pdf(diet_plan, daily_calories):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Personalized Diet Plan", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Recommended Daily Calories: {daily_calories} kcal", ln=True)

    for meal, items in diet_plan.items():
        pdf.ln(5)
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(200, 10, txt=meal, ln=True)
        pdf.set_font("Arial", size=12)
        if isinstance(items, list):
            for i in items:
                pdf.cell(200, 10, txt=f"- {i}", ln=True)
        else:
            pdf.cell(200, 10, txt=items, ln=True)

    return pdf

# ------------------ Streamlit App ------------------ #
st.title("🥗 AI Wellness Coach - Personalized Diet Plan")

with st.sidebar:
    st.header("Enter Your Details")
    age = st.number_input("Age:", min_value=10, max_value=100, step=1)
    gender = st.radio("Gender:", ["Male", "Female"])
    weight = st.number_input("Weight (kg):", min_value=20, max_value=200, step=1)
    height = st.number_input("Height (cm):", min_value=100, max_value=250, step=1)
    preference = st.selectbox("Diet Preference:", ["veg", "non-veg", "vegan"])
    generate_btn = st.button("Generate Diet Plan")

if generate_btn:
    daily_calories = calculate_calories(age, gender, weight, height)
    diet_plan = generate_diet(preference, daily_calories)

    st.subheader("Your Personalized Diet Plan")
    st.write(f"**Recommended Daily Calories:** {daily_calories} kcal")
    st.progress(70)  # Just a fun visual

    for meal, items in diet_plan.items():
        st.write(f"**{meal}**: {', '.join(items) if isinstance(items, list) else items}")

    # PDF Download
    pdf = create_pdf(diet_plan, daily_calories)
    pdf.output("diet_plan.pdf")
    with open("diet_plan.pdf", "rb") as f:
        st.download_button("📥 Download Diet Plan as PDF", f, file_name="diet_plan.pdf")
