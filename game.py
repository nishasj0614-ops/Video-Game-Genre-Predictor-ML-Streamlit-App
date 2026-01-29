import streamlit as st
import pandas as pd
import joblib

# ---------------------------------
# Page Config
# ---------------------------------
st.set_page_config(
    page_title="🎮 Game Genre Predictor",
    page_icon="🎯",
    layout="centered"
)

# ---------------------------------
# DARK COLOR BACKGROUND + STYLING
# ---------------------------------
st.markdown(
    """
    <style>

    /* Remove white background */
    html, body, [data-testid="stAppViewContainer"], 
    [data-testid="stSidebar"], .stApp {
        background-color: #0f172a !important;
    }

    /* Main Card */
    .main-card {
        background: #020617;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 0 30px rgba(56,189,248,0.35);
        margin-top: 20px;
    }

    h1 {
        color: #38bdf8;
        text-align: center;
        text-shadow: 2px 2px 10px black;
    }

    h3, label {
        color: #e5e7eb !important;
    }

    /* Input boxes */
    input, select, textarea {
        background-color: #020617 !important;
        color: #38bdf8 !important;
        border-radius: 10px !important;
        border: 1px solid #38bdf8 !important;
    }

    /* Button */
    .stButton > button {
        background: linear-gradient(90deg, #22c55e, #16a34a);
        color: black;
        border-radius: 25px;
        font-size: 18px;
        padding: 12px 30px;
        border: none;
        font-weight: bold;
    }

    .stButton > button:hover {
        transform: scale(1.05);
        background: linear-gradient(90deg, #38bdf8, #0ea5e9);
        color: black;
    }

    /* Result box */
    .result-box {
        background: linear-gradient(135deg, #facc15, #fde047);
        color: black;
        padding: 20px;
        border-radius: 15px;
        font-size: 20px;
        text-align: center;
        margin-top: 20px;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------
# Title
# ---------------------------------
st.markdown("<h1>🎮 Video Game Genre Predictor</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#e5e7eb;'>"
    "Machine Learning based Game Analytics App 🚀"
    "</p>",
    unsafe_allow_html=True
)

# ---------------------------------
# Card Start
# ---------------------------------
st.markdown("<div class='main-card'>", unsafe_allow_html=True)

st.subheader("🕹️ Enter Game Details")

platform = st.selectbox("🎮 Platform", ["Wii", "NES", "DS", "PS4", "PS3", "X360"])
publisher = st.selectbox("🏢 Publisher", ["Nintendo", "Activision", "EA", "Sony", "Ubisoft"])
year = st.number_input("📅 Release Year", 1980, 2025, 2010)

na_sales = st.number_input("🇺🇸 NA Sales (Millions)", 0.0, step=0.1)
eu_sales = st.number_input("🇪🇺 EU Sales (Millions)", 0.0, step=0.1)
jp_sales = st.number_input("🇯🇵 JP Sales (Millions)", 0.0, step=0.1)
other_sales = st.number_input("🌍 Other Sales (Millions)", 0.0, step=0.1)

# ---------------------------------
# Prediction
# ---------------------------------
if st.button("🎯 Predict Genre"):
    model = joblib.load("best_vgsales_model.joblib")

    user_input = pd.DataFrame([{
        "Platform": platform,
        "Publisher": publisher,
        "Year": year,
        "NA_Sales": na_sales,
        "EU_Sales": eu_sales,
        "JP_Sales": jp_sales,
        "Other_Sales": other_sales
    }])

    prediction = model.predict(user_input)[0]

    st.markdown(
        f"<div class='result-box'>🎉 Predicted Game Genre: 🎮 {prediction}</div>",
        unsafe_allow_html=True
    )

# ---------------------------------
# Card End
# ---------------------------------
st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------
# Footer
# ---------------------------------
st.markdown(
    "<p style='text-align:center; color:#94a3b8;'>"
    "Built with ❤️ using Streamlit | ML Project"
    "</p>",
    unsafe_allow_html=True
)
