# Streamlit Dashboard for SDG7
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns
from scipy.stats import pearsonr


# Page configuration
st.set_page_config(page_title="SDG7 Dashboard", page_icon="🌍", layout="wide")

@st.cache_data
def load_data():
    df_cleaned = pd.read_csv("Data/Processed/global-data-on-sustainable-energy-processed.csv")
    df_pred_2030 = pd.read_csv("Data/Predictions/predictions_linear_2030.csv")
    return df_cleaned, df_pred_2030

df_cleaned, df_pred_2030 = load_data()

page = st.sidebar.radio("Select Page", ["Quick Summary", "Dashboard", "Predictions", "Country Overview", "Hypotheses"])

if page == "Quick Summary":
    st.markdown("""
    <h1 style='text-align: center;'>Sustainable Development Goal 7: Affordable and Clean Energy 🌍</h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="display: flex; justify-content: center;">
    <div style="max-width: 900px; width: 100%;">
        <div style="background-color:#0c1c2c; padding: 20px; border-radius: 8px; color: white;">
        <h3> Project Context</h3>
        <p><strong>Sustainable Development Goal 7 (SDG 7)</strong> aims to ensure access to affordable, reliable, sustainable, and modern energy for all by 2030.
        This project uses data analytics and machine learning to analyse trends and make predictions for 175 countries.</p>
        <ul>
            <li> Covers data from 2000 to 2020, with forecasts for 2030.</li>
            <li> 13 key indicators including access to electricity, renewable energy, emissions, and GDP.</li>
            <li> Data Source: <a href="https://www.kaggle.com/datasets/anshtanwar/global-data-on-sustainable-energy" target="_blank" style="color:#2dcdd5;">Kaggle Dataset</a></li>
            <li> It includes more than 3,500 records of annual data per country from 2000 to 2020 with linear predictions for 2030</li>
        </ul>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div style="display: flex; justify-content: center;">
    <div style="max-width: 900px; width: 100%;">
        <div style="background-color:#073f24; padding: 20px; border-radius: 8px; color: #ccebd4; border-left: 6px solid #00cc66;">
        <h3> Project Objectives</h3>
        <ol>
            <li><strong>Understand key relationships:</strong> Explore how indicators such as renewable energy share and fossil electricity correlate with energy access and emissions.</li>
            <li><strong>Forecast for 2030:</strong> Predict access to electricity, access to clean fuels, and CO₂ emissions using linear regression models per country.</li>
            <li><strong>Support global analysis:</strong> Identify at-risk countries to help inform policy recommendations aligned with SDG 7.</li>
        </ol>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)



    st.markdown("""
    <div style="display: flex; justify-content: center;">
    <div style="max-width: 900px; width: 100%;">
        <div style="background-color:#132743; padding: 20px; border-radius: 8px; color: #d6ecf2;">
        <h3> Key Dataset Variables</h3>
        <table style="width:100%; border-collapse: collapse;">
            <tr style="background-color:#1c3d5a;">
            <th style="padding: 8px; border: 1px solid #395870;">Variable</th>
            <th style="padding: 8px; border: 1px solid #395870;">Meaning</th>
            <th style="padding: 8px; border: 1px solid #395870;">Units</th>
            </tr>
            <tr>
            <td style="padding: 8px;">access_to_electricity</td>
            <td style="padding: 8px;">Population with electricity access</td>
            <td style="padding: 8px;">% of total population</td>
            </tr>
            <tr>
            <td style="padding: 8px;">access_to_clean_fuels</td>
            <td style="padding: 8px;">Population with access to clean cooking fuels</td>
            <td style="padding: 8px;">% of total population</td>
            </tr>
            <tr>
            <td style="padding: 8px;">renewable_capacity_per_capita</td>
            <td style="padding: 8px;">Renewable capacity installed per person</td>
            <td style="padding: 8px;">Watts/person</td>
            </tr>
            <tr>
            <td style="padding: 8px;">fossil_electricity</td>
            <td style="padding: 8px;">Share of electricity from fossil sources</td>
            <td style="padding: 8px;">%</td>
            </tr>
            <tr>
            <td style="padding: 8px;">co2_emissions_kt</td>
            <td style="padding: 8px;">Annual CO₂ emissions</td>
            <td style="padding: 8px;">Kilotonnes</td>
            </tr>
            <tr>
            <td style="padding: 8px;">gdp_per_capita</td>
            <td style="padding: 8px;">Gross domestic product per person</td>
            <td style="padding: 8px;">USD</td>
            </tr>
        </table>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)



 # ------------------ Combine 2020 to 2030 ------------------
    df_2020 = df_cleaned[df_cleaned["year"] == 2020][["country", "access_to_electricity", "access_to_clean_fuels", "co2_emissions_kt"]]
    df_2020.columns = ["country", "access_to_electricity_2020", "access_to_clean_fuels_2020", "co2_emissions_kt_2020"]
    df_combined = pd.merge(df_2020, df_pred_2030, on="country")

elif page == "Dashboard":
    st.title(" Global Trends Dashboard")
# ------------------ visual 1 ------------------
    st.subheader("Access to Electricity Over Time")
    countries_to_plot = st.multiselect("Select countries", df_cleaned["country"].unique(), default=["India", "Kenya", "Germany"], key="electricity_countries")
    df_filtered = df_cleaned[df_cleaned["country"].isin(countries_to_plot)]
    fig1 = px.line(df_filtered, x="year", y="access_to_electricity", color="country", title="Access to Electricity Over Time")
    st.plotly_chart(fig1, use_container_width=True, key="chart_electricity")

    st.subheader("Access to Electricity Change by Year")
    year_map = st.selectbox("Select a year", [2000, 2010, 2020, 2030])
    
    if year_map == 2030:
        map_df = df_pred_2030.copy()
        map_df["access_to_electricity"] = df_pred_2030["access_to_electricity"]
    else:
        map_df = df_cleaned[df_cleaned["year"] == year_map]

    fig_map = px.choropleth(map_df, locations="country", locationmode="country names",
                            color="access_to_electricity",
                            title=f"Access to Electricity in {year_map}",
                            color_continuous_scale="YlGnBu")
    st.plotly_chart(fig_map, use_container_width=True)

    st.subheader("Renewable Capacity vs Access to Electricity")
    df_2020_features = df_cleaned[df_cleaned["year"] == 2020]
    fig3 = px.scatter(df_2020_features, x="renewable_capacity_per_capita", y="access_to_electricity",
                     color="country", trendline="ols", title="Renewable Capacity vs Electricity Access (2020)")
    st.plotly_chart(fig3, use_container_width=True, key="chart_scatter")

    st.subheader("CO₂ Emissions Distribution in 2020")
    fig4 = px.box(df_2020_features, y="co2_emissions_kt", title="Distribution of CO₂ Emissions")
    st.plotly_chart(fig4, use_container_width=True, key="chart_emissions")

elif page == "Predictions":
    st.title(" Predictions for 2030")

    df_2020 = df_cleaned[df_cleaned["year"] == 2020][["country", "access_to_electricity", "access_to_clean_fuels", "co2_emissions_kt"]]
    df_2020.columns = ["country", "access_to_electricity_2020", "access_to_clean_fuels_2020", "co2_emissions_kt_2020"]
    df_combined = pd.merge(df_2020, df_pred_2030, on="country")

    tab1, tab2, tab3, tab4 = st.tabs(["Clean Fuels", "Electricity Access", "CO₂ Emissions", "Custom Country View"])

    with tab1:
        st.subheader("Access to Clean Fuels in 2020 vs 2030")
        df_combined["clean_growth"] = df_combined["access_to_clean_fuels"] - df_combined["access_to_clean_fuels_2020"]

        top_clean = df_combined.sort_values("clean_growth", ascending=False).head(10)
        bottom_clean = df_combined.sort_values("clean_growth", ascending=True).head(10)

        st.markdown("### Top 10 Countries with Highest Growth in Clean Fuels")
        fig_top_clean = px.bar(top_clean, x="country", y=["access_to_clean_fuels_2020", "access_to_clean_fuels"],
                               barmode="group", title="Top 10 Countries - Clean Fuels Access Growth (2020-2030)",
                               color_discrete_sequence=["#66c2a5", "#fc8d62"])
        st.plotly_chart(fig_top_clean, use_container_width=True)

        st.markdown("### Top 10 Countries with Lowest Growth in Clean Fuels")
        fig_bottom_clean = px.bar(bottom_clean, x="country", y=["access_to_clean_fuels_2020", "access_to_clean_fuels"],
                                  barmode="group", title="Bottom 10 Countries - Clean Fuels Access Growth (2020-2030)",
                                  color_discrete_sequence=["#66c2a5", "#fc8d62"])
        st.plotly_chart(fig_bottom_clean, use_container_width=True)

    with tab2:
        st.subheader("Access to Electricity in 2020 vs 2030")
        df_combined["elec_growth"] = df_combined["access_to_electricity"] - df_combined["access_to_electricity_2020"]
        top_elec = df_combined.sort_values("elec_growth", ascending=False).head(10)
        bottom_elec = df_combined.sort_values("elec_growth", ascending=True).head(10)

        st.markdown("### Top 10 Countries with Highest Growth in Electricity Access")
        fig_top_elec = px.bar(top_elec, x="country", y=["access_to_electricity_2020", "access_to_electricity"],
                              barmode="group", title="Electricity Access Growth (2020 vs 2030)",
                              color_discrete_sequence=["#8da0cb", "#e78ac3"])
        st.plotly_chart(fig_top_elec, use_container_width=True)


    with tab3:
        st.subheader("CO₂ Emissions in 2020 vs 2030")
        df_combined["co2_change"] = df_combined["co2_emissions_kt"] - df_combined["co2_emissions_kt_2020"]

        top_co2_increase = df_combined.sort_values("co2_change", ascending=False).head(10)
        top_co2_decrease = df_combined.sort_values("co2_change", ascending=True).head(10)

        st.markdown("### Top 10 Countries with Highest CO₂ Emission Increase")
        fig_co2_inc = px.bar(top_co2_increase, x="country", y=["co2_emissions_kt_2020", "co2_emissions_kt"],
                             barmode="group", title="CO₂ Emissions Increase (2020 vs 2030)",
                             color_discrete_sequence=["#a6cee3", "#fb9a99"])
        st.plotly_chart(fig_co2_inc, use_container_width=True)

        st.markdown("### Top 10 Countries with Highest CO₂ Emission Decrease")
        fig_co2_dec = px.bar(top_co2_decrease, x="country", y=["co2_emissions_kt_2020", "co2_emissions_kt"],
                             barmode="group", title="CO₂ Emissions Decrease (2020 vs 2030)",
                             color_discrete_sequence=["#a6cee3", "#fb9a99"])
        st.plotly_chart(fig_co2_dec, use_container_width=True)

    with tab4:
        st.subheader("Compare Countries Manually")
        custom_countries = st.multiselect("Select countries to compare:", df_combined["country"].unique())
        if custom_countries:
            df_selected = df_combined[df_combined["country"].isin(custom_countries)]
            st.dataframe(df_selected[["country", "access_to_electricity_2020", "access_to_electricity",
                                     "access_to_clean_fuels_2020", "access_to_clean_fuels",
                                     "co2_emissions_kt_2020", "co2_emissions_kt"]].sort_values("country"))
        


elif page == "Predictions":
    st.title(" Predictions for 2030")
    df_2020 = df_cleaned[df_cleaned["year"] == 2020][["country", "access_to_electricity", "access_to_clean_fuels", "co2_emissions_kt"]]
    df_2020.columns = ["country", "access_to_electricity_2020", "access_to_clean_fuels_2020", "co2_emissions_kt_2020"]
    df_combined = pd.merge(df_2020, df_pred_2030, on="country")

    st.subheader("Access to Clean Fuels in 2020 vs 2030")
    df_combined["clean_growth"] = df_combined["access_to_clean_fuels"] - df_combined["access_to_clean_fuels_2020"]

    top_clean = df_combined.sort_values("clean_growth", ascending=False).head(10)
    bottom_clean = df_combined.sort_values("clean_growth", ascending=True).head(10)

    st.markdown("### Top 10 Countries with Highest Growth in Clean Fuels")
    fig_top_clean = px.bar(top_clean, x="country", y=["access_to_clean_fuels_2020", "access_to_clean_fuels"],
                           barmode="group", title="Top 10 Countries - Clean Fuels Access Growth (2020-2030)")
    st.plotly_chart(fig_top_clean, use_container_width=True)

    st.markdown("### Top 10 Countries with Lowest Growth in Clean Fuels")
    fig_bottom_clean = px.bar(bottom_clean, x="country", y=["access_to_clean_fuels_2020", "access_to_clean_fuels"],
                              barmode="group", title="Bottom 10 Countries - Clean Fuels Access Growth (2020-2030)")
    st.plotly_chart(fig_bottom_clean, use_container_width=True)

    custom_clean = st.multiselect("Select additional countries to compare (Clean Fuels):", df_combined["country"].unique())
    if custom_clean:
        df_selected_clean = df_combined[df_combined["country"].isin(custom_clean)]
        fig_custom_clean = px.bar(df_selected_clean, x="country", y=["access_to_clean_fuels_2020", "access_to_clean_fuels"],
                                  barmode="group", title="Selected Countries - Clean Fuels Access (2020 vs 2030)")
        st.plotly_chart(fig_custom_clean, use_container_width=True)

elif page == "Hypotheses":
    st.title(" Hypotheses and Validation")
    df_2020 = df_cleaned[df_cleaned["year"] == 2020].copy()
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Correlation Heatmap", "Hypotheses Tests 1", "Hypotheses Tests 2", "Hypotheses Tests 3", "Hypotheses Test 4"])

    with tab1:
        st.subheader("Heatmap of Correlation Between Variables (2020)")
        df_2020_corr = df_2020.select_dtypes(include="number").corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(df_2020_corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
        st.pyplot(fig)
        plt.clf()


    with tab2:
        st.subheader("Hypothesis 1: GDP per Capita vs Access to Clean Fuels")
        fig_h1 = px.scatter(df_2020, x="gdp_per_capita", y="access_to_clean_fuels", color="country",
                        trendline="ols", title="GDP per Capita vs Access to Clean Fuels")
        st.plotly_chart(fig_h1, use_container_width=True)
# box plot for GDP quartiles
        df_2020['gdp_quartile'] = pd.qcut(df_2020['gdp_per_capita'], 4, labels=["Q1", "Q2", "Q3", "Q4"])
        fig_box1 = px.box(df_2020, x='gdp_quartile', y='access_to_clean_fuels', title="Access to Clean Fuels by GDP Quartile")
        st.plotly_chart(fig_box1, use_container_width=True)


    with tab3:
        st.subheader("Hypothesis 2: Renewable Growth vs Access to Electricity")
        fig_h2 = px.scatter(df_2020, x="renewable_capacity_per_capita", y="access_to_electricity", color="country",
                        trendline="ols", title="Renewable Capacity per Capita vs Access to Electricity")
        st.plotly_chart(fig_h2, use_container_width=True)
# histogram of renewable capacity
        df_2020["difference"] = df_2020["access_to_electricity"] - df_2020["renewable_capacity_per_capita"]
        fig_diff = px.histogram(df_2020, x="difference", nbins=30, title="Difference between Access to Electricity and Renewable Capacity per Capita")
        st.plotly_chart(fig_diff, use_container_width=True)

        st.info("This hypothesis expects a strong positive relationship: more renewable capacity should enhance electricity availability. The histogram shows the distribution of difference between access and capacity.")
    
    with tab4:
        st.subheader("Hypothesis 3: Renewable Energy Share vs Energy Intensity")
        fig_h3 = px.scatter(df_2020, x="renewable_energy_share", y="energy_intensity", color="country",
                        trendline="ols", title="Renewable Energy Share vs Energy Intensity")
        st.plotly_chart(fig_h3, use_container_width=True)

# Lineplot of renewable energy share over time
        if "country" in df_2020.columns:
            fig_line = px.line(df_2020.sort_values(by="country"), x="renewable_energy_share", y="energy_intensity", color="country",
                               title="Energy Intensity by Renewable Share across Regions")
            st.plotly_chart(fig_line, use_container_width=True)
        else:
            st.warning("'region' column not found in dataset. Cannot display lineplot by region.")

        st.info("Lower energy intensity means more efficient energy use. A negative correlation supports that renewable energy improves efficiency. The lineplot helps observe regional trends if available.")
    
    with tab5:
         st.subheader("Hypothesis 4: Renewable Capacity Growth vs CO₂ Emission Growth")
         df_growth = df_cleaned[df_cleaned["year"].isin([2000, 2020])][
            ["country", "year", "renewable_capacity_per_capita", "co2_emissions_kt"]
        ].dropna()

         if not df_growth.empty and df_growth["year"].nunique() == 2:
            df_pivot = df_growth.pivot(index="country", columns="year", values=["renewable_capacity_per_capita", "co2_emissions_kt"])
            df_pivot.columns = ["_".join([str(c) for c in col]).strip() for col in df_pivot.columns.values]
            df_pivot = df_pivot.dropna()
            df_pivot["renewable_growth"] = df_pivot["renewable_capacity_per_capita_2020"] - df_pivot["renewable_capacity_per_capita_2000"]
            df_pivot["co2_growth"] = df_pivot["co2_emissions_kt_2020"] - df_pivot["co2_emissions_kt_2000"]
            df_pivot.reset_index(inplace=True)

            fig_h4 = px.scatter(df_pivot, x="renewable_growth", y="co2_growth", color="country",
                                trendline="ols", title="Renewable Capacity Growth vs CO₂ Emission Growth (2000–2020)")
            st.plotly_chart(fig_h4, use_container_width=True)

            fig_arrow = px.line(df_growth.sort_values(by=["country", "year"]), x="year", y="co2_emissions_kt", color="country",
                                title="CO₂ Emission Change per Country (2000–2020)", markers=True)
            st.plotly_chart(fig_arrow, use_container_width=True)

            r, p = pearsonr(df_pivot["renewable_growth"], df_pivot["co2_growth"])
            st.markdown(f"**Correlation coefficient (r):** {r:.2f} | **p-value:** {p:.4f}")
            st.info("This hypothesis assumes that expanding renewables leads to emission reductions. A strong negative correlation would support this. The arrow chart visualizes emission evolution per country.")
         else:
            st.warning("Not enough data to evaluate Hypothesis 4. Please check the dataset.")

elif page == "Country Overview":        
    st.title(" Country Overview")
    country = st.selectbox("Select a country", df_cleaned["country"].unique())
    df_country = df_cleaned[df_cleaned["country"] == country]

    if not df_country.empty:
        st.subheader(f"Data for {country}")
        st.dataframe(df_country)

        fig_country = px.line(df_country, x="year", y=["access_to_electricity", "access_to_clean_fuels", "co2_emissions_kt"],
                              title=f"Trends in {country} (2000-2020)", labels={"value": "Value", "variable": "Indicator"})
        st.plotly_chart(fig_country, use_container_width=True)
    else:
        st.warning(f"No data available for {country}.")
# ------------------ Créditos ------------------
st.markdown("""
---
**Developed by:** Bruno Organai 
**Dataset:** [Global Data on Sustainable Energy](https://www.kaggle.com/datasets/anshtanwar/global-data-on-sustainable-energy)  
**Note:** All predictions are generated using a linear regression model per country. Interpret with caution.
""")
