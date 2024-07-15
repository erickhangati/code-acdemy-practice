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
