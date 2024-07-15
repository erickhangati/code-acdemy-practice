# A/B Testing for ShoeFly.com

## Overview

This project analyzes A/B testing data for ShoeFly.com, an online shoe store. ShoeFly.com conducted an A/B test with two different versions of an ad, which were placed in emails and banner ads on Facebook, Twitter, and Google. The goal is to determine how the two ads performed across different platforms and days of the week using aggregate measures.

## Project Structure

The project is structured as follows:

1. **Introduction**: Provides an overview of the project.
2. **Importing the Dataset**: Imports the dataset from `ad_clicks.csv`.
3. **Analyzing Ad Sources**: Examines the ad sources and their performance.
4. **Analyzing an A/B Test**: Analyzes the performance of the two ads (A and B).

## Steps

### 1. Introduction
Provides an overview of the project and the goal of the analysis.

### 2. Importing the Dataset
Imports the dataset from the `ad_clicks.csv` file using Pandas.

```python
import pandas as pd
ad_clicks = pd.read_csv('ad_clicks.csv')
```

### 3. Analyzing Ad Sources
- Examines the first few rows of the dataset.
- Counts the number of views from each utm_source.
- Creates a new column `is_click` to indicate whether the ad was clicked.

```python
ad_clicks['is_click'] = ad_clicks.ad_click_timestamp.apply(lambda timestamp: False if pd.isna(timestamp) else True)
```

- Groups by `utm_source` and `is_click` to count the number of users in each group.

```python
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
```

- Pivots the data to show the number of clicks and non-clicks for each source.

```python
clicks_pivot = clicks_by_source.pivot(index='utm_source', columns='is_click', values='user_id')
clicks_pivot['percent_clicked'] = (clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])) * 100
```

### 4. Analyzing an A/B Test
- Checks if the same number of users were shown both ads.

```python
both_ads = ad_clicks.groupby('experimental_group').user_id.count()
```

- Groups by experimental_group and is_click to count the number of users in each group.

```python
percentage_clicked = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
```

- Pivots the data to show the number of clicks and non-clicks for each ad.

```python
pivot_percentage = percentage_clicked.pivot(index='experimental_group', columns='is_click', values='user_id')
pivot_percentage['percentage clicked'] = (pivot_percentage[True] / (pivot_percentage[True] + pivot_percentage[False])) * 100
```

- Analyzes click percentages for each day of the week.

```python
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

a_clicks_pivot = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index().pivot(index='day', columns='is_click', values='user_id')
a_clicks_pivot['percent_clicked'] = (a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False])) * 100

b_clicks_pivot = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index().pivot(index='day', columns='is_click', values='user_id')
b_clicks_pivot['percent_clicked'] = (b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False])) * 100
```

## Conclusion
This project provides insights into the performance of two different ads across various platforms and days of the week. The analysis helps ShoeFly.com understand user engagement with their ads and make informed decisions for future marketing strategies.

## Dependencies
- Python 3.x
- Jupyter Notebook
- Pandas

## Usage
To run this project, open the Jupyter Notebook and execute the cells step-by-step.