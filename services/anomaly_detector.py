import joblib
model = joblib.load("models/anomaly_model.pkl")
def detect_anomaly(demand, stock, time_of_day, price):
    result = model.predict([[demand, stock, time_of_day, price]])
    if result[0] == -1:
        return True
    return False