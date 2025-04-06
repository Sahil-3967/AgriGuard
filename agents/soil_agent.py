class SoilAgent:
    def analyze(self, pH, moisture):
        advice = []
        if pH < 5.5:
            advice.append("Add lime to improve pH.")
        elif pH > 7.5:
            advice.append("Add sulfur to lower pH.")
        else:
            advice.append("pH is optimal.")

        if moisture < 20:
            advice.append("Irrigation needed.")
        elif moisture > 40:
            advice.append("Soil too moist, improve drainage.")
        else:
            advice.append("Moisture is ideal.")

        return advice