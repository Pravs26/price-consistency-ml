import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from datetime import time

from services.price_predictor import predict_price
from services.anomaly_detector import detect_anomaly
from services.determinism_checker import check_price
from cache.price_cache import lock_price, get_locked_price

st.set_page_config(page_title="Price Consistency System", layout="centered")
st.title(" Real-Time Product Price Consistency System")
st.write("Predict product price and monitor demand and stock behaviour.")
st.divider()


user_id = st.number_input("User ID", min_value=1, step=1)
product_id = st.number_input("Product ID", min_value=1, step=1)
demand = st.number_input(
    "Demand Level",
    min_value=0,
    step=1,
    help="Higher demand can increase product price."
)

stock = st.number_input(
    "Stock Available",
    min_value=0,
    step=1,
    help="Lower stock may trigger urgency."
)

time_input = st.time_input("Time of Day")
time_of_day = time_input.hour

st.divider()

if stock > 0 and stock <= 20:
    st.warning(" Purchase soon, only few left in stock!")

if demand >= 100:
    st.warning(" This product is highly in demand right now!")


if st.button("Predict Price"):
    locked_price = get_locked_price(user_id, product_id)

    if locked_price:
        st.success(f"Locked Price: ₹{locked_price:.2f}")
        st.info("Price already locked for this session")

    else:

        predicted_price = predict_price(demand, stock, time_of_day)
        valid, stable_price = check_price(product_id, predicted_price)
        anomaly = detect_anomaly(demand, stock, time_of_day, predicted_price)

        lock_price(user_id, product_id, stable_price)

        st.success(f"Predicted Price: ₹{stable_price:.2f}")
        if anomaly:
            st.error("⚠ Pricing anomaly detected")
        else:
            st.info("Price behaviour normal")