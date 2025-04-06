import streamlit as st
import pandas as pd
from agents.soil_agent import SoilAgent
from agents.weather_agent import WeatherAgent
from agents.market_agent import MarketAgent
from agents.sustainability_agent import SustainabilityAgent
from agents.advisor_agent import AdvisorAgent
from models.yield_predictor import load_model

st.title("AgriGuard - Smart Farming Advisor")

crop_type = st.selectbox("Crop Type", ["Wheat", "Rice", "Maize", "Barley"])
soil_type = st.selectbox("Soil Type", ["Clay", "Sandy", "Loam"])
soil_pH = st.slider("Soil pH", 3.0, 9.0, 6.5)
moisture = st.slider("Soil Moisture (%)", 0, 100, 30)
temperature = st.slider("Temperature (°C)", 0, 50, 25)
rainfall = st.slider("Rainfall (mm)", 0, 300, 100)
fertilizer_used = st.slider("Fertilizer Used (kg/acre)", 0, 200, 80)
pesticide_used = st.slider("Pesticide Used (kg/acre)", 0, 100, 20)

if st.button("Get Recommendation"):
    input_data = {
        'Crop_Type': crop_type,
        'Soil_Type': soil_type,
        'Soil_pH': soil_pH,
        'Moisture': moisture,
        'Temperature': temperature,
        'Rainfall': rainfall,
        'Fertilizer_Used': fertilizer_used,
        'Pesticide_Used': pesticide_used
    }

    model = load_model("models/yield_predictor.pkl")
    market_data = pd.read_csv("data/market_researcher_dataset.csv")

    soil_agent = SoilAgent()
    weather_agent = WeatherAgent()
    market_agent = MarketAgent(market_data)
    sustainability_agent = SustainabilityAgent()
    advisor_agent = AdvisorAgent(model, soil_agent, weather_agent, market_agent, sustainability_agent)

    result = advisor_agent.recommend(input_data)

    st.subheader("Recommendation")
    st.json(result)
