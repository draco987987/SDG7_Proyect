# Streamlit Dashboard for SDG7
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Page configuration
st.set_page_config(page_title="SDG7 Dashboard", page_icon="🌍", layout="wide")

st.title("Sustainable Development Goal 7: Affordable and Clean Energy 🌍")
st.markdown("""
This dashboard provides insights into the progress of Sustainable Development Goal 7,
which aims to ensure access to affordable, reliable, sustainable, and modern energy for all.
""")

@st.cache_data
def load_data():
    df_cleaned = pd.read_csv("Data/Processed/global-data-on-sustainable-energy-processed.csv")
    df_pred_2030 = pd.read_csv("Data/Predictions/predictions_linear_2030.csv")
    return df_cleaned, df_pred_2030

df_cleaned, df_pred_2030 = load_data()

# ------------------ Combine 2020 to 2030 ------------------
df_2020 = df_cleaned[df_cleaned["year"] == 2020][["country", "access_to_electricity", "access_to_clean_fuels", "co2_emissions_kt"]]
df_2020.columns = ["country", "access_to_electricity_2020", "access_to_clean_fuels_2020", "co2_emissions_kt_2020"]
df_combined = pd.merge(df_2020, df_pred_2030, on="country")

# ------------------ Visualization 1 ------------------
st.subheader("1. Access to Electricity Over Time")
countries_to_plot = st.multiselect("Select countries", df_cleaned["country"].unique(), default=["India", "Kenya", "Germany"])
df_filtered = df_cleaned[df_cleaned["country"].isin(countries_to_plot)]
fig1 = px.line(df_filtered, x="year", y="access_to_electricity", color="country", title="Access to Electricity Over Time")
st.plotly_chart(fig1, use_container_width=True)

# ------------------ Visualization 2 ------------------
st.subheader("2. Access to Electricity in 2020 vs 2030")
fig2 = px.bar(df_combined, x="country", y=["access_to_electricity_2020", "access_to_electricity"],
              barmode="group", title="Access to Electricity: 2020 vs 2030 Prediction")
st.plotly_chart(fig2, use_container_width=True)

# ------------------ Visualization 3  ------------------
st.subheader("3. Renewable Capacity vs Access to Electricity")
df_2020_features = df_cleaned[df_cleaned["year"] == 2020]
fig3 = px.scatter(df_2020_features, x="renewable_capacity_per_capita", y="access_to_electricity",
                 color="country", trendline="ols", title="Renewable Capacity vs Electricity Access (2020)")
st.plotly_chart(fig3, use_container_width=True)

# ------------------ Visualization 4 ------------------
st.subheader("4. CO₂ Emissions Distribution in 2020")
fig4 = px.box(df_2020_features, y="co2_emissions_kt", title="Distribution of CO₂ Emissions")
st.plotly_chart(fig4, use_container_width=True)

# ------------------ Visualization 5 ------------------
st.subheader("5. Country Energy Summary")
selected_country = st.selectbox("Select a country", sorted(df_cleaned["country"].unique()))
latest_data = df_cleaned[(df_cleaned["country"] == selected_country) & (df_cleaned["year"] == 2020)]
pred_data = df_pred_2030[df_pred_2030["country"] == selected_country]

if not latest_data.empty and not pred_data.empty:
    st.metric("Access to Electricity (2020)", f"{latest_data['access_to_electricity'].values[0]:.2f}%")
    st.metric("Access to Electricity (2030 Predicted)", f"{pred_data['access_to_electricity'].values[0]:.2f}%")
    st.metric("CO₂ Emissions (2020)", f"{latest_data['co2_emissions_kt'].values[0]:,.0f} kt")
    st.metric("CO₂ Emissions (2030 Predicted)", f"{pred_data['co2_emissions_kt'].values[0]:,.0f} kt")

# ------------------ Créditos ------------------
st.markdown("""
---
**Developed by:** Bruno Organai 
**Dataset:** [Global Data on Sustainable Energy](https://www.kaggle.com/datasets/anshtanwar/global-data-on-sustainable-energy)  
**Note:** All predictions are generated using a linear regression model per country. Interpret with caution.
""")
