# Project SDG7 Tracking Global Energy Access and Sustainability

**Project SDG7** is a comprehensive data analysis tool designed to streamline data exploration, analysis, and visualisation. The tool supports multiple data formats and provides an intuitive interface for both novice and expert data scientists.

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


## Dataset Content
* This project uses a public dataset on global energy indicators, covering multiple countries over the past decades. The data includes:
- Access to electricity (% of population)
- Access to clean fuels for cooking
- Renewable electricity capacity per capita
- Share of renewables in final energy consumption
- CO2 emissions, energy intensity, and more.

The dataset has been cleaned and preprocessed using Python (Pandas) and exported to structured CSVs.

## Business Requirements
* The dashboard aims to:
1. Identify countries and regions lagging behind in access to sustainable energy.
2. Visualise progress over time toward the UN's SDG 7 targets.
3. Provide actionable insights for policymakers and NGOs focused on energy access.
4. Allow comparisons between regions using interactive elements and clear data storytelling.


## Hypothesis and how to validate?
- **Hypothesis 1:** Regions with lower GDP per capita tend to have lower access to clean energy.
   *Validation:* Scatter plots and correlation analysis confirm this with moderate positive correlation.

- **Hypothesis 2:** Countries with higher renewable electricity capacity per capita improve electricity access faster.
   *Validation:* Time series trends and growth rates show weak correlation; not strongly supported.

- **Hypothesis** 3: Higher renewable energy share is linked to lower energy intensity.
   *Validation:* Scatter plots reveal weak positive correlation; structural inefficiencies play a stronger role.

- **Hypothesis 4:** Increases in renewable capacity reduce CO2 emissions.
   *Validation:* Data does not support this uniformly; economic growth can offset renewable benefits.

## Project Plan
* **step 1:** Dataset Acquisition and exploratory data analysis. 
* **step 2:** Data cleaning, formatting, renaming colums and dropping unused variables. 
* **step 3:** Hypotheses testing and visual analytics (Correlation, growth rates, violinplots, choropleths)
* **step 4:** Model Switch to linear Regression due to interpretability and scope
* **step 5:** Evaluation of model (R², MAE, RMSE) and export predictions
* **step 6:** Dashboard creation with streamlit (Interactive plots, filters etc)
* **Step 7:** Deployment via Heroku

## The rationale to map the business requirements to the Data Visualisations
* Choropleth maps: global visualisation of electricity access by year.
* Violin plots: distribution of GDP per capita by access groups.
* Correlation matrix: reveal underlying relationships.
* Scatter plots: support hypotheses with trendlines.
* Time series line charts: progress over decades.
* Box plots: Highlight variation across indicators and countries.

# Modeling decision: Linear Regression vs Random Forest
* Originally, a Random Forest Regressor was used for predictive modeling. However, the project pivoted to linear regression due to: 
* - Simpler interpretability for non technical audiences
* - Easier extraction of feature importance
* - Absence of important parts of the data that justified a Random Forest

# Limitations
* - Linear Regression assumes linearity, wich may not hold for all indicators.
* - It is sensitive to outliers (Especially in CO2 emissions).
* - Some countries lacked historical data, reducing reliability of predictions.

# Model Evaluation
The models were evaluated using:
* - R² Coefficient of determination
* - Mean absolute error (MAE)
* - Root mean squared error (RMSE)
these metrics were displayed alongside predicted vs actual charts for interpretability and in the EDA and visualization parts

## Analysis techniques used
* Data cleaning (Pandas)
* Descriptive Statistics (mean, median, std dev)
* Hypothesis testing (Correlation)
* visualisation (Seaborn, Plotly, Matplotlib)
* Predictive modelling (Random Forest Regressor)
* Model evaluation (R²,Mae, RMSE)
* The data has its problems, i have spend a lot of time cleaning and thinking what was the most optimate methot to clean the nan values, also i have a lot of problems with the creation of the random forest, it required much time online to see how i could do it. Also the use of streamlit was time consuming
* ChatGPT was used for ideation, code debugging, Markdwon generation and phrasing.

## Ethical considerations
* The dataset is public and anonymised.
* Bias may arise from lack of regional granularity (Rural vs urban).
* The model reflects historical trends and may not capture conflict or policy changes.
* Predictions should not be used for critical planning without expert review.

## Dashboard Design
This interactive dashboard was developed to suport Sustainable Development Goal 7 (SDG7), which aims to ensure access to affordable, reliable, sustainable, and modern energy for all by 2030. It uses historical data and linear predictions to analyze energy trends across more than 170 countries since the 2000s

* **Quick summary** Overview of SDG7 and project goals
* **Dashboard** An overview of global trends in nergy access and emissions with.
* - Line chart: Evolution of electricity access for selected countries
* - Choropleth map: Geographic distribution of electricity access by decade
* - Scatter plot: Correlation between renewable capacity and electricity access.
* - Box & Histogram: Distribution of CO₂ in 2020.
* - Regional Box plot: Compares CO₂, emissions by continent.
* - Quartile Box plot: Categorizes emisiions into quartiles for analysis.
* **Country Overview** An overview of metrics by country
* - 2000 vs 2020 metrics for key indicators.
* - % Change with conditional coloring (Red = negative, green = positive).
* - Regional context for the country.
* - Useful for indentifying individual progress.
* **Predictions (2030)** Merges actual 2020 data with model predictions for 2030
* - Focus on access to clean fuels: 
   - Top 10 countries with highest and lowest growth.
   - Bar charts for comparison.
   - Option to select custom countries for targeted analysis.
* **Hypotheses and Validation**  Provides five interactive tabs to validate analytical hypotheses using viusal and statistical methods:
- * Correlation Heatmap: Shows relationships among numerical variables in 2020.

- * Hypothesis 1: GDP per capita vs Access to clean fuels.

- * Hypothesis 2: Renewable capacity per capita vs Access to electricity.

- * Hypothesis 3: Renewable energy share vs Energy intensity (efficiency).

- *Hypothesis 4: Growth in renewable capacity vs Growth in CO₂ emissions (2000–2020).

Each test includes:

- * Scatter plots with trendlines.

- * Statistical metrics (Pearson r, p-value).

- * Violin/box/histogram charts for grouped distribution.

* The dashboard was designed with both data experts and general audiences in mind. To achieve this.
- * I used plain langueage and describe hypotheses, objectives and variable meanings.
- * Use Tooltips, caption and section headers to offer quick explanation on charts, allowing non thecnical users to grasp key ideas.
- * Key statistics, such as correlation coefficients and p-values are accompanied by interpretative text to make them meaningful to non experts.
For technical users, data transformations and analytical logic are traceable in the codebase or visualized.

* The visual desing and content strategy follow the next principles:
* - User friendly layaout with sidebar navigation.
* - Data storytelling through tabs and visuals.
* - Visual diversity including line graphs, scatter plots, choropleths etc... To suit different data types and user preferences.
* - color coded to help users intuitively understand directional trends.
* - interactive controls like multiselect and sliders wich let users customize outputs.

## Unfixed Bugs
* None affecting core functionality.
* Some outiliers in CO2 emissions skew model variance. Considered normal due to economic disparity.

## Development Roadmap
* Large gaps in raw dataset (Handled via interpolation).
* Correlations were weaker than expected, requiring broader feature engineering.

## Deployment
### Heroku

* The App live link is: https://sdg7-4e4a2bdd3507.herokuapp.com/
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. From the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis Libraries
* **Pandas** - for data handling and cleaning.
* **Numpy** - numerical operations
* **Matplotlib, Seaborn** - visualisation
* **Plotly.express** - interactive charts
* **Sklearn** - Random Forest, metrics
* **Heroku** - App deployment

## Credits 

* Dataset source: https://www.kaggle.com/datasets/anshtanwar/global-data-on-sustainable-energy
* Code snippets inspired by Code Institute templates and online threads
* Icons: Font Awesome

## Acknowledgements
* Thank to Code Institute mentors (Vasi) for iterative feedback, explanations and support