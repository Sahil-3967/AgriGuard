class WeatherAgent:
    def analyze(self, temperature, rainfall):
        if temperature < 15:
            return "Too cold, choose frost-resistant crops."
        elif temperature > 35:
            return "Too hot, choose heat-tolerant crops."
        if rainfall < 50:
            return "Drought-prone area, consider low-water crops."
        return "Weather suitable for most crops."
