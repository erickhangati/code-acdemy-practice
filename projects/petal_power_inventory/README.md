# Petal Power Inventory

You’re the lead data analyst for a chain of gardening stores called Petal Power. This project aims to help them analyze their inventory data.

## Table of Contents

- [Overview](#overview)
- [Data Loading](#data-loading)
- [Inspecting Data](#inspecting-data)
- [Data Manipulation](#data-manipulation)
- [Customer Requests](#customer-requests)
- [Inventory Analysis](#inventory-analysis)
- [Product Descriptions](#product-descriptions)

## Overview

The `Petal Power Inventory` notebook demonstrates various data analysis tasks including loading data, inspecting data, data manipulation, and responding to customer requests using the `pandas` library in Python.

## Data Loading

We start by loading the inventory data from the `inventory.csv` file into a pandas DataFrame.

```python
import pandas as pd

# Load the data into a DataFrame called inventory
with open('inventory.csv') as csvfile:
    inventory = pd.read_csv(csvfile)
```

## Inspecting Data
Inspect the first 10 rows of the inventory data to understand its structure.

```python
# Inspect the first 10 rows of inventory
inventory.head(10)
```

## Data Manipulation
### Selecting Staten Island Data
Select the first 10 rows representing data from the Staten Island location.

```python
# Select the first 10 rows and save them to staten_island
staten_island = inventory.loc[:10]
staten_island
```

## Adding In-Stock Information
Add a column to the inventory called `in_stock` which indicates if the quantity is greater than 0.

```python
# Add in_stock column
inventory['in_stock'] = inventory.apply(lambda row: True if row.quantity > 0 else False, axis=1)
inventory
```

## Calculating Total Value
Create a column called `total_value` that is equal to price multiplied by quantity.

```python
# Add total_value column
inventory['total_value'] = inventory.apply(lambda row: row.quantity * row.price, axis=1)
inventory
```

## Customer Requests
### Products Sold at Staten Island
Select the column `product_description` from `staten_island` for a customer inquiry.

```python
# Select product_description column for Staten Island
product_request = staten_island.product_description
product_request
```

## Types of Seeds Sold at Brooklyn
Select all rows where `location` is equal to `Brooklyn` and `product_type` is equal to seeds.

```python
# Select seeds from Brooklyn location
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
seed_request
```

## Inventory Analysis
### Complete Description
Combine `product_type` and `product_description` into a single string for a complete product description.

```python
# Define lambda function to combine product_type and product_description
combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)

# Add full_description column
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
inventory
```

## Conclusion
This notebook demonstrates how to load, inspect, manipulate, and analyze inventory data using pandas. It also shows how to respond to customer requests by filtering and transforming the data accordingly.

## Running the Notebook
1. Make sure you have pandas installed in your Python environment.
2. Download or clone this repository.
3. Open the Jupyter Notebook and run the cells to see the analysis in action.