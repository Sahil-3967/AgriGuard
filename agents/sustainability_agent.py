class SustainabilityAgent:
    def score(self, fertilizer, pesticide, water):
        score = 100
        if fertilizer > 100:
            score -= 20
        if pesticide > 50:
            score -= 20
        if water > 120:
            score -= 20
        return max(score, 0)