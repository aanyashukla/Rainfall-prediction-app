import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import os

# Load model
model_path = os.path.join(os.path.dirname(__file__), "rainfall_prediction_model.pkl")
model_data = joblib.load(model_path)
model = model_data["model"]
features = model_data["feature_names"]

st.set_page_config(page_title="Rainfall Prediction App", layout="wide")
st.title("🌧️ Rainfall Prediction using Random Forest")
st.markdown("Enter weather parameters to predict if it will rain today.")

# Sidebar for inputs
st.sidebar.header("🔧 Input Weather Parameters")
user_input = {}
for feature in features:
    user_input[feature] = st.sidebar.number_input(f"{feature.title()}", value=0.0)

input_df = pd.DataFrame(user_input, index=[0])

# Visualize input summary
st.subheader("📊 Input Feature Summary")
fig_input = px.bar(input_df.T, labels={"value": "Value", "index": "Feature"}, title="Entered Weather Data")
st.plotly_chart(fig_input, use_container_width=True)

# Make prediction
if st.button("🔍 Predict"):
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0]

    st.subheader("🧠 Model Prediction")
    if prediction == 1:
        st.success("🌧️ Yes, Rain is Expected Today!")
    else:
        st.info("🌤️ No Rain is Expected Today!")

    # Show prediction confidence
    st.subheader("📈 Prediction Confidence")
    fig_proba = px.pie(names=["No Rain 🌤️", "Rain ☔"], values=proba, title="Model Confidence")
    st.plotly_chart(fig_proba, use_container_width=True)

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit & Random Forest")
