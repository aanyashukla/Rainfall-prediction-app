# 🌧️ Rainfall Prediction App

A web-based machine learning app that predicts whether it will rain today based on user-provided weather conditions.
Built using **Random Forest**, **Streamlit**, and **Plotly** for interactive data input and output visualization.

---

## 📌 Project Highlights

- 🧠 Trained Random Forest Classifier on historical rainfall data
- 📊 Input feature summary with interactive bar chart
- 🌀 Real-time prediction confidence shown as a pie chart

---

## 📂 Folder Structure
<pre> 📦 Rainfall-prediction-app/ ├── 📂 streamlit_app/ │ ├── 📄 app.py # Streamlit application │ └── 📄 rainfall_prediction_model.pkl # Trained model for deployment │ ├── 📂 Model/ │ ├── 📄 Rainfall_Prediction.ipynb # EDA, preprocessing, model training │ ├── 📄 Rainfall.csv # Dataset used for training │ └── 📄 rainfall_prediction_model.pkl # Trained model with feature info │ ├── 📄 requirements.txt # Required packages └── 📄 README.md # You're reading this! </pre>


---

## 🛠 Tech Stack

| Tool         | Purpose                           |
|--------------|------------------------------------|
| Streamlit    | Web interface                      |
| scikit-learn | Model training (Random Forest)     |
| joblib       | Model serialization                |
| Plotly       | Interactive visualizations         |
| Pandas       | Data handling                      |
| Jupyter      | Notebook-based EDA and modeling    |

---

## 🧠 How the App Works
- You enter weather parameters on the left sidebar.
- The app visualizes your input in a bar chart.
- When you click 🔍 Predict, it:
    - Loads the trained model
    - Makes a prediction (Yes/No for Rain)
    - Displays prediction confidence as a pie chart
