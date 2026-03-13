import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
data = pd.read_csv("data/training_data.csv")
X = data[['demand', 'stock', 'time_of_day']]
y = data['price']
model = RandomForestRegressor()
model.fit(X, y)
joblib.dump(model, "models/price_model.pkl")
print("Price prediction model trained successfully")