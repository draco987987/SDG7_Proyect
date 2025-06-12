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

# map the region to each country
region_map = {
    'Afghanistan': 'Asia', 'Albania': 'Europe', 'Algeria': 'Africa', 'Angola': 'Africa',
    'Antigua and Barbuda': 'North America', 'Argentina': 'South America', 'Armenia': 'Asia',
    'Australia': 'Oceania', 'Austria': 'Europe', 'Azerbaijan': 'Asia', 'Bahamas': 'North America',
    'Bahrain': 'Asia', 'Bangladesh': 'Asia', 'Barbados': 'North America', 'Belarus': 'Europe',
    'Belgium': 'Europe', 'Belize': 'North America', 'Benin': 'Africa', 'Bhutan': 'Asia',
    'Bolivia': 'South America', 'Bosnia and Herzegovina': 'Europe', 'Botswana': 'Africa',
    'Brazil': 'South America', 'Brunei': 'Asia', 'Bulgaria': 'Europe', 'Burkina Faso': 'Africa',
    'Burundi': 'Africa', 'Cambodia': 'Asia', 'Cameroon': 'Africa', 'Canada': 'North America',
    'Cape Verde': 'Africa', 'Central African Republic': 'Africa', 'Chad': 'Africa',
    'Chile': 'South America', 'China': 'Asia', 'Colombia': 'South America', 'Comoros': 'Africa',
    'Congo': 'Africa', 'Costa Rica': 'North America', 'Croatia': 'Europe', 'Cuba': 'North America',
    'Cyprus': 'Europe', 'Czechia': 'Europe', 'Denmark': 'Europe', 'Djibouti': 'Africa',
    'Dominican Republic': 'North America', 'Ecuador': 'South America', 'Egypt': 'Africa',
    'El Salvador': 'North America', 'Estonia': 'Europe', 'Eswatini': 'Africa', 'Ethiopia': 'Africa',
    'Fiji': 'Oceania', 'Finland': 'Europe', 'France': 'Europe', 'Gabon': 'Africa',
    'Gambia': 'Africa', 'Georgia': 'Asia', 'Germany': 'Europe', 'Ghana': 'Africa',
    'Greece': 'Europe', 'Guatemala': 'North America', 'Guinea': 'Africa', 'Guyana': 'South America',
    'Haiti': 'North America', 'Honduras': 'North America', 'Hungary': 'Europe', 'Iceland': 'Europe',
    'India': 'Asia', 'Indonesia': 'Asia', 'Iran': 'Asia', 'Iraq': 'Asia', 'Ireland': 'Europe',
    'Israel': 'Asia', 'Italy': 'Europe', 'Jamaica': 'North America', 'Japan': 'Asia',
    'Jordan': 'Asia', 'Kazakhstan': 'Asia', 'Kenya': 'Africa', 'Kuwait': 'Asia',
    'Kyrgyzstan': 'Asia', 'Laos': 'Asia', 'Latvia': 'Europe', 'Lebanon': 'Asia',
    'Lesotho': 'Africa', 'Liberia': 'Africa', 'Libya': 'Africa', 'Lithuania': 'Europe',
    'Luxembourg': 'Europe', 'Madagascar': 'Africa', 'Malawi': 'Africa', 'Malaysia': 'Asia',
    'Maldives': 'Asia', 'Mali': 'Africa', 'Malta': 'Europe', 'Mauritania': 'Africa',
    'Mauritius': 'Africa', 'Mexico': 'North America', 'Moldova': 'Europe', 'Mongolia': 'Asia',
    'Montenegro': 'Europe', 'Morocco': 'Africa', 'Mozambique': 'Africa', 'Myanmar': 'Asia',
    'Namibia': 'Africa', 'Nepal': 'Asia', 'Netherlands': 'Europe', 'New Zealand': 'Oceania',
    'Nicaragua': 'North America', 'Niger': 'Africa', 'Nigeria': 'Africa', 'North Macedonia': 'Europe',
    'Norway': 'Europe', 'Oman': 'Asia', 'Pakistan': 'Asia', 'Panama': 'North America',
    'Papua New Guinea': 'Oceania', 'Paraguay': 'South America', 'Peru': 'South America',
    'Philippines': 'Asia', 'Poland': 'Europe', 'Portugal': 'Europe', 'Qatar': 'Asia',
    'Romania': 'Europe', 'Rwanda': 'Africa', 'Saint Lucia': 'North America',
    'Saudi Arabia': 'Asia', 'Senegal': 'Africa', 'Serbia': 'Europe', 'Seychelles': 'Africa',
    'Sierra Leone': 'Africa', 'Singapore': 'Asia', 'Slovakia': 'Europe', 'Slovenia': 'Europe',
    'Solomon Islands': 'Oceania', 'Somalia': 'Africa', 'South Africa': 'Africa', 'South Sudan': 'Africa',
    'Spain': 'Europe', 'Sri Lanka': 'Asia', 'Sudan': 'Africa', 'Suriname': 'South America',
    'Sweden': 'Europe', 'Switzerland': 'Europe', 'Syria': 'Asia', 'Tajikistan': 'Asia',
    'Tanzania': 'Africa', 'Thailand': 'Asia', 'Togo': 'Africa', 'Trinidad and Tobago': 'North America',
    'Tunisia': 'Africa', 'Turkey': 'Asia', 'Turkmenistan': 'Asia', 'Uganda': 'Africa',
    'Ukraine': 'Europe', 'United Arab Emirates': 'Asia', 'United Kingdom': 'Europe',
    'United States': 'North America', 'Uruguay': 'South America', 'Uzbekistan': 'Asia',
    'Vanuatu': 'Oceania', 'Venezuela': 'South America', 'Vietnam': 'Asia', 'Yemen': 'Asia',
    'Zambia': 'Africa', 'Zimbabwe': 'Africa'
}
df_cleaned["region"] = df_cleaned["country"].map(region_map)



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
    df_2020_features = df_cleaned[df_cleaned["year"] == 2020]

    fig4 = px.box(df_2020_features, y="co2_emissions_kt", title="Distribution of CO₂ Emissions")
    st.plotly_chart(fig4, use_container_width=True, key="chart_emissions")

    # Histogram of CO₂ emissions
    fig_hist_co2 = px.histogram(df_2020_features, x="co2_emissions_kt", nbins=50, title="Histogram of CO₂ Emissions (2020)")
    st.plotly_chart(fig_hist_co2, use_container_width=True)

    # Box plot of CO₂ emissions by region
    fig_box_region = px.box(df_2020_features, x="region", y="co2_emissions_kt", color="region",
                             title="CO₂ Emissions by Region (2020)", points="all", hover_name="country")
    st.plotly_chart(fig_box_region, use_container_width=True)

    # Divide CO₂ emissions into quartiles
    df_2020_features["co2_quartile"] = pd.qcut(df_2020_features["co2_emissions_kt"], q=4, labels=["Q1 (Low)", "Q2", "Q3", "Q4 (High)"])
    fig_quartile = px.box(df_2020_features, x="co2_quartile", y="co2_emissions_kt",
                          title="CO₂ Emissions by Quartile (2020)", color="co2_quartile", points="all", hover_name="country")
    st.plotly_chart(fig_quartile, use_container_width=True)

elif page == "Country Overview":
    st.title(" Country Overview - 2020 Summary")

    st.markdown("""
    This section provides a country-by-country summary of key sustainable energy indicators for the year 2020. 
    Use the selector below to choose a country and explore its performance in terms of electricity access, clean fuels, emissions, and more.
    """)

    df_2020_summary = df_cleaned[df_cleaned["year"] == 2020].copy()

    selected_country = st.selectbox("Select a country:", df_2020_summary["country"].unique())

    if selected_country:
        country_data_2020 = df_2020_summary[df_2020_summary["country"] == selected_country]
        country_data_2000 = df_cleaned[(df_cleaned["country"] == selected_country) & (df_cleaned["year"] == 2000)]

        st.markdown(f"### General Results for {selected_country} (2020 vs 2000)")

        metrics = [
            "access_to_electricity",
            "access_to_clean_fuels",
            "renewable_capacity_per_capita",
            "renewable_energy_share",
            "fossil_electricity",
            "energy_intensity",
            "co2_emissions_kt",
            "gdp_per_capita"
        ]

        df_2020_vals = country_data_2020[metrics].transpose().rename(columns={country_data_2020.index[0]: "2020"})
        df_2000_vals = country_data_2000[metrics].transpose().rename(columns={country_data_2000.index[0]: "2000"}) if not country_data_2000.empty else pd.DataFrame(index=metrics, columns=["2000"])

        df_summary = df_2000_vals.join(df_2020_vals)
        df_summary["% Change"] = ((df_summary["2020"] - df_summary["2000"]) / df_summary["2000"] * 100).round(2)

        def highlight_change(val):
            try:
                val = float(val)
                if val > 0:
                    return 'color: green;'
                elif val < 0:
                    return 'color: red;'
                else:
                    return ''
            except:
                return ''
            
        styled_df = df_summary.style.applymap(highlight_change, subset=["% Change"])
        st.dataframe(styled_df, use_container_width=True)

        st.markdown("---")
        st.markdown("**Additional context:**")
        st.write("Region:", country_data_2020["region"].values[0])
        st.write("Income classification or further metrics could be added here.")
        
        
        


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
        st.markdown("""
        This heatmap shows how numerical variables correlate in 2020.  
        Red = strong positive correlation, blue = strong negative.  
        Look for variables that move together (strong correlation) or in opposite directions (negative correlation).
        """)

        df_2020_corr = df_2020.select_dtypes(include="number").corr()

        fig, ax = plt.subplots(figsize=(8, 4))  # Aumentamos tamaño
        sns.heatmap(df_2020_corr,
                    annot=True,
                    fmt=".2f",
                    cmap="coolwarm",
                    cbar=True,
                    square=True,
                    linewidths=0.5,
                    annot_kws={"size": 6})  

        plt.xticks(rotation=45, ha="right", fontsize=6)
        plt.yticks(rotation=0, fontsize=6)
        st.pyplot(fig)
        plt.clf()

    with tab2:
        st.subheader("Hypothesis 1: GDP per Capita vs Access to Clean Fuels")
        st.markdown(""" 
        This hypothesis explores if richer countries (higher GDP per capita) also provide more access to clean cooking fuels.  
        We expect a positive correlation if economic development supports energy access.
        """)
        fig_h1 = px.scatter(df_2020, x="gdp_per_capita", y="access_to_clean_fuels", color="country",
                           trendline="ols", title="GDP per Capita vs Access to Clean Fuels")
        st.plotly_chart(fig_h1, use_container_width=True, key="h1_scatter")
        r, p = pearsonr(df_2020["gdp_per_capita"], df_2020["access_to_clean_fuels"])
        st.markdown(f"**Correlation coefficient (r):** {r:.2f} | **p-value:** {p:.4f}")
        st.info("This hypothesis suggests that economic prosperity improves energy access. A significant positive correlation would support this assumption.")

        df_2020["gdp_quartile"] = pd.qcut(df_2020["gdp_per_capita"], q=4)
        df_2020["gdp_quartile_str"] = df_2020["gdp_quartile"].astype(str)
        fig_violin = px.violin(df_2020, y="access_to_clean_fuels", x="gdp_quartile_str", box=True,
                               title="Distribution of Clean Fuel Access by GDP Quartiles")
        st.plotly_chart(fig_violin, use_container_width=True, key="h1_violin")
        st.markdown("Higher GDP quartiles should ideally show higher access levels. This violin plot groups countries by income level to visually assess disparities.")

    with tab3:
        st.subheader("Hypothesis 2: Renewable Growth vs Access to Electricity")
        st.markdown("""
        This test checks whether countries that invest more in renewable energy per person also have higher access to electricity.  
        This helps understand if renewable capacity supports electrification.
        """)
        fig_h2 = px.scatter(df_2020, x="renewable_capacity_per_capita", y="access_to_electricity", color="country",
                           trendline="ols", title="Renewable Capacity per Capita vs Access to Electricity")
        st.plotly_chart(fig_h2, use_container_width=True, key="h2_scatter")
        r, p = pearsonr(df_2020["renewable_capacity_per_capita"], df_2020["access_to_electricity"])
        st.markdown(f"**Correlation coefficient (r):** {r:.2f} | **p-value:** {p:.4f}")

        df_2020["difference"] = df_2020["access_to_electricity"] - df_2020["renewable_capacity_per_capita"]
        fig_diff = px.histogram(df_2020, x="difference", nbins=30, title="Difference between Access to Electricity and Renewable Capacity per Capita")
        st.plotly_chart(fig_diff, use_container_width=True, key="h2_hist")
        st.markdown("This histogram shows if high renewable capacity aligns well with electricity access. Smaller differences suggest better alignment.")

    with tab4:
        st.subheader("Hypothesis 3: Renewable Energy Share vs Energy Intensity")
        st.markdown("""
          
        This hypothesis tests whether a higher share of renewable energy in total consumption leads to more efficient energy usage (lower energy intensity).
        """)
        fig_h3 = px.scatter(df_2020, x="renewable_energy_share", y="energy_intensity", color="country",
                           trendline="ols", title="Renewable Energy Share vs Energy Intensity")
        st.plotly_chart(fig_h3, use_container_width=True, key="h3_scatter")
        
        st.markdown("""
                This chart displays the distribution of energy intensity across world regions in 2020. 
                Lower energy intensity indicates better efficiency. Outliers represent countries with unusually high or low energy consumption relative to GDP.
                """)
        fig_box = px.box(df_2020, 
                 x="region", 
                 y="energy_intensity", 
                 color="region", 
                 title="Energy Intensity by Region (2020)",
                 points="all")  # Muestra puntos además del boxplot
        st.plotly_chart(fig_box, use_container_width=True)
        st.info("""
            This visualization compares the energy intensity of countries grouped by region. 
            Lower energy intensity indicates greater energy efficiency. The boxplot helps us observe whether regions 
            with higher renewable energy share tend to have lower energy intensity, supporting the hypothesis that renewables improve efficiency.
            """)
        r, p = pearsonr(df_2020["renewable_energy_share"], df_2020["energy_intensity"])
        st.markdown(f"**Correlation coefficient (r):** {r:.2f} | **p-value:** {p:.4f}")


    with tab5:
        st.subheader("Hypothesis 4: Renewable Capacity Growth vs CO₂ Emission Growth")
        st.markdown(""" 
        This chart compares the change in renewable energy capacity with the change in CO₂ emissions between 2000 and 2020.  
        If renewable capacity increases and emissions decrease, we expect a **negative correlation**, suggesting that renewables help reduce emissions.
        """)
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
            st.plotly_chart(fig_h4, use_container_width=True, key="h4_scatter", hover_name="country")

            fig_arrow = px.line(df_growth.sort_values(by=["country", "year"]), x="year", y="co2_emissions_kt", color="country",
                                title="CO₂ Emission Change per Country (2000–2020)", markers=True)
            st.plotly_chart(fig_arrow, use_container_width=True, key="h4_arrow", hover_name="country")

            r, p = pearsonr(df_pivot["renewable_growth"], df_pivot["co2_growth"])
            st.markdown(f"**Correlation coefficient (r):** {r:.2f} | **p-value:** {p:.4f}")
            st.info("This hypothesis assumes that expanding renewables leads to emission reductions. A strong negative correlation would support this. The arrow chart visualizes emission evolution per country.")
        else:
            st.warning("Not enough data to evaluate Hypothesis 4. Please check the dataset.")
# ------------------ Créditos ------------------
st.markdown("""
---
**Developed by:** Bruno Organai 
**Dataset:** [Global Data on Sustainable Energy](https://www.kaggle.com/datasets/anshtanwar/global-data-on-sustainable-energy)  
**Note:** All predictions are generated using a linear regression model per country. Interpret with caution.
""")
