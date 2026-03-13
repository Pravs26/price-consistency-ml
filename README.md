## Real-Time Product Price Consistency System

# Problem Statement

Users report that product prices on the website appear to change while they browse, whereas other users observe stable pricing for the same products at the same time. These inconsistencies occur without any manual intervention from administrators, leading to confusion and trust issues during the purchasing process.
The challenge is to understand and manage the unseen factors influencing price variation while ensuring price consistency during checkout. A reliable system is required to monitor pricing behaviour, detect anomalies, and maintain deterministic pricing for users interacting with the platform.

3 Project Overview

The Real-Time Product Price Consistency System is designed to address pricing inconsistencies in e-commerce platforms.
The system integrates machine learning models, anomaly detection mechanisms, and price locking techniques to ensure stable and reliable pricing for users browsing the same product.

The application predicts product prices based on factors such as:

Demand level
Available stock
Time of day

It then verifies the price using a determinism checker and detects unusual price patterns using anomaly detection algorithms.
The system also locks the price once it is generated to ensure consistent pricing during a user's browsing session.

# Solution

This project solves the pricing inconsistency issue using the following mechanisms:

1. Machine Learning Price Prediction
A Random Forest Regression model predicts product prices based on market factors such as demand, stock levels, and time.

2. Anomaly Detection
An Isolation Forest algorithm detects abnormal pricing behaviour that may arise due to hidden system triggers or data irregularities.

3. Determinism Checker
A price consistency validator ensures that a product maintains a stable price across multiple views for the same user session.

4. Price Locking Mechanism
Once a price is generated for a user-product pair, it is locked in memory so the user always sees the same price while browsing.

5. Real-Time Dashboard
A Streamlit-based interface allows users to simulate product pricing scenarios and observe price predictions, alerts, and consistency behaviour.

# How the Project Works

The user inputs product parameters:

User ID
Product ID
Demand Level
Available Stock
Time of Day

The system processes the inputs through the machine learning price prediction model.
The predicted price is checked using the determinism checker to ensure stability.
The anomaly detection model evaluates whether the predicted price is abnormal.
The system locks the generated price for the user session to ensure consistent viewing during browsing.

Alerts are displayed if:

Stock is very low
Demand is extremely high
Pricing anomalies are detected

# Implementation

The project is implemented using a modular architecture consisting of multiple components:

1. Data Processing
Training data is stored in CSV format and used to train machine learning models.

2. Machine Learning Module
Two models are trained:
RandomForestRegressor for price prediction
IsolationForest for anomaly detection

3. Services Layer

Handles the business logic including:
Price prediction
Anomaly detection
Determinism validation
Price Cache

Implements a session-based price locking mechanism.

# Tech Stack Used

1. Python	Core programming language
2. Scikit-learn	Machine learning models
3. Pandas-	Data handling
4. NumPy-Numerical operations
5. Streamlit-Web dashboard interface
6. Joblib-Model serialization


# Conclusion

The Real-Time Product Price Consistency System demonstrates how machine learning and system design can work together to maintain stable and trustworthy pricing in e-commerce environments.
By integrating price prediction, anomaly detection, and deterministic price locking, the system ensures users experience consistent product pricing while browsing, thereby improving trust and transparency in the purchasing process.
This prototype provides a strong foundation for implementing scalable price consistency mechanisms in real-world online marketplaces.

# Project Links

GitHub Repository
https://github.com/Pravs26/price-consistency-ml.git

Deployment Link


Author
K. SAI PRAVALLIKA

LinkedIn:
https://www.linkedin.com/in/sai-pravallika-kovvuri-9b289b376