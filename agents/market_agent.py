class MarketAgent:
    def __init__(self, market_data):
        self.market_data = market_data

    def get_price(self, crop_type):
        crop_info = self.market_data[self.market_data['Crop_Type'] == crop_type]
        if not crop_info.empty:
            return crop_info['Market_Price'].values[0]
        return 0.0