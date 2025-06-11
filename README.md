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
* **step 4:** Machine Learning using Random Forest to predict 2025 and 2030 access and emissions.
* **step 5:** Evaluation of model (R², MAE, RMSE) and export predictions
* **step 6:** Dashboard creation (In progress).

## The rationale to map the business requirements to the Data Visualisations
* Choropleth maps: global visualisation of electricity access by year.
* Violin plots: distribution of GDP per capita by access groups.
* Correlation matrix: reveal underlying relationships.
* Scatter plots: support hypotheses with trendlines.
* Time series line charts: progress over decades.

## Analysis techniques used
* Data cleaning (Pandas)
* Descriptive Statistics (mean, median, std dev)
* Hypothesis testing (Correlation)
* visualisation (Seaborn, Plotly, Matplotlib)
* Predictive modelling (Random Forest Regressor)
* Model evaluation (R²,Mae, RMSE)
* The data has its problems, i have spend a lot of time cleaning and thinking what was the most optimate methot to clean the nan values, also i have a lot of problems with the creation of the random forest, it required much time online to see how i could do it
* ChatGPT was used for ideation, code debugging, Markdwon generation and phrasing.

## Ethical considerations
* The dataset is public and anonymised.
* Bias may arise from lack of regional granularity (Rural vs urban).
* The model reflects historical trends and may not capture conflict or policy changes.
* Predictions should not be used for critical planning without expert review.

## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).
* How were data insights communicated to technical and non-technical audiences?
* Explain how the dashboard was designed to communicate complex data insights to different audiences. 

## Unfixed Bugs
* None affecting core functionality.
* Some outiliers in CO2 emissions skew model variance. Considered normal due to economic disparity.

## Development Roadmap
* Large gaps in raw dataset (Handled via interpolation).
* Correlations were weaker than expected, requiring broader feature engineering.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
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


## Credits 

* Dataset source: https://www.kaggle.com/datasets/anshtanwar/global-data-on-sustainable-energy
* Code snippets inspired by Code Institute templates and online threads

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements
* Thank to Code Institute mentors for iterative feedback, explanations and support