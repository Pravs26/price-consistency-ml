import joblib
model = joblib.load("models/price_model.pkl")
def predict_price(demand, stock, time_of_day):
    price = model.predict([[demand, stock, time_of_day]])
    return float(price[0])
