import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

# Load farmer dataset
farmer_data = pd.read_csv("data/farmer_advisor_dataset.csv")

# Feature columns and target
features = ['Soil_pH', 'Moisture', 'Temperature', 'Rainfall', 'Fertilizer_Used', 'Pesticide_Used']
target = 'Crop_Yield'

# Drop rows with missing values
farmer_data.dropna(subset=features + [target], inplace=True)

# Prepare X and y
X = farmer_data[features]
y = farmer_data[target]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Model Trained. MSE:", mse)

# Save model
joblib.dump(model, "models/yield_predictor.pkl")