class AdvisorAgent:
    def __init__(self, model, soil_agent, weather_agent, market_agent, sustainability_agent):
        self.model = model
        self.soil_agent = soil_agent
        self.weather_agent = weather_agent
        self.market_agent = market_agent
        self.sustainability_agent = sustainability_agent

    def recommend(self, input_data):
        features = [
            input_data['Soil_pH'],
            input_data['Moisture'],
            input_data['Temperature'],
            input_data['Rainfall'],
            input_data['Fertilizer_Used'],
            input_data['Pesticide_Used']
        ]
        predicted_yield = self.model.predict([features])[0]
        price = self.market_agent.get_price(input_data['Crop_Type'])
        profit = predicted_yield * price
        sustainability = self.sustainability_agent.score(
            input_data['Fertilizer_Used'],
            input_data['Pesticide_Used'],
            input_data['Rainfall']
        )

        return {
            "Recommended Crop": input_data['Crop_Type'],
            "Predicted Yield (tons)": round(predicted_yield, 2),
            "Estimated Profit": round(profit, 2),
            "Soil Advice": self.soil_agent.analyze(input_data['Soil_pH'], input_data['Moisture']),
            "Weather Advice": self.weather_agent.analyze(input_data['Temperature'], input_data['Rainfall']),
            "Sustainability Score": sustainability
        }