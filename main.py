from agents.soil_agent import SoilAgent
from agents.weather_agent import WeatherAgent
from agents.market_agent import MarketAgent
from agents.sustainability_agent import SustainabilityAgent
from agents.advisor_agent import AdvisorAgent
from models.yield_predictor import load_model
import pandas as pd

# Sample input (replace with user interface input or real-time data)
input_data = {
    'Crop_Type': 'Wheat',
    'Soil_Type': 'Clay',
    'Soil_pH': 6.5,
    'Moisture': 30,
    'Temperature': 25,
    'Rainfall': 100,
    'Fertilizer_Used': 80,
    'Pesticide_Used': 20
}

# Load model and market price data
model = load_model("models/yield_predictor.pkl")
market_data = pd.read_csv("data/market_researcher_dataset.csv")

# Initialize agents
soil_agent = SoilAgent()
weather_agent = WeatherAgent()
market_agent = MarketAgent(market_data)
sustainability_agent = SustainabilityAgent()
advisor_agent = AdvisorAgent(model, soil_agent, weather_agent, market_agent, sustainability_agent)

# Get recommendation
recommendation = advisor_agent.recommend(input_data)
print("Final Farming Recommendation:\n", recommendation)