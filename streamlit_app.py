import streamlit as st
import joblib

from services.price_predictor import predict_price
from services.anomaly_detector import detect_anomaly
from services.determinism_checker import check_price
from cache.price_cache import lock_price, get_locked_price

st.title("🛒 Real-Time Product Price Consistency System")
st.write("This prototype predicts product price using ML and checks for anomalies.")

user_id = st.number_input("User ID", min_value=1, step=1)
product_id = st.number_input("Product ID", min_value=1, step=1)
demand = st.slider("Demand Level", 0, 200, 50)
stock = st.slider("Stock Available", 0, 300, 150)
time_of_day = st.slider("Time of Day", 0, 23, 12)

if st.button("Predict Price"):
    locked_price = get_locked_price(user_id, product_id)

    if locked_price:
        st.success(f"Locked Price: ₹{locked_price}")
        st.info("Price already locked for this session")

    else:
        predicted_price = predict_price(demand, stock, time_of_day)
        valid, stable_price = check_price(product_id, predicted_price)
        anomaly = detect_anomaly(demand, stock, time_of_day, predicted_price)
        lock_price(user_id, product_id, stable_price)
        st.success(f"Predicted Price: ₹{stable_price}")

        if anomaly:
            st.error(" Anomaly detected in pricing!")
        else:
            st.info("Price behaviour normal")
