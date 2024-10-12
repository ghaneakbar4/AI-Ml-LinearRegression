# macOS/Linux

# You may need to run `sudo apt-get install python3-venv` first on Debian-based OSs

```
python3 -m venv .venv
```

# Windows

```
python -m venv .venv
.venv\scripts\activate
pip install numpy matplotlib scikit-learn

python main.py
```

## Introduction

This repository contains python code that analyzes the relationship between GDP per capita and life satsisfaction across a wide range of countries using Machine Learning, linear regression.

## Data Sources

- `oecd_bli_2015.csv`: Contains a wide range of BLI (Better Life Index) data.
- `gdp_per_capita.csv`: Contains GDP per capita for various countries.

## Code Structure

Main components of the code:

1. Data Preparation function (`prepare_country_stats`)
   This function accepts to data as parameters, one the BLI data and the other gpd for countries that we have.
   and it uses these data and manipulates it to the desired structure by doing these steps:

   - Filtering bli data for total inequality.
   - Pivoting the data to create a country indexed data.
   - Renaming gdp data.
   - Indexing gdp data by country.
   - Merging both gdp and bli data.
   - Sorting data based on gpd value.
   - Removing unnecassary data(indexes that we don't want to use to train our model).
   - Returning relevant data for GDP per capita and life satisfaction.

2. Data loading and processing:
   GDP and BLI data will be read from our data sources using `pandas` library and will be process using `prepare_country_stats` function.

3. Linear regression model training.
   We use sklearn to levrage linear regression training methods to train our model

4. Visualization of the data and regression line.
   We use the data we have and `matplotlib` library to show a chart showcasing the data we used to train our model and the line that represents the f(x) of the outcome of the training.
   Also there is a `*` in the chart showing the test we gave to the model to predict, and as you can see it is on the line.
