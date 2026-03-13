import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
data = pd.read_csv("data/training_data.csv")
X = data[['demand', 'stock', 'time_of_day', 'price']]
model = IsolationForest(contamination=0.05)
model.fit(X)
joblib.dump(model, "models/anomaly_model.pkl")
print("Anomaly detection model trained successfully")
