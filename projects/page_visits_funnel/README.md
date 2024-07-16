# Page Visits Funnel

## Project Overview
Cool T-Shirts Inc. has asked you to analyze data on visits to their website. Your job is to build a funnel, which is a description of how many people continue to the next step of a multi-step process. In this case, our funnel describes the following process:
1. A user visits CoolTShirts.com
2. A user adds a t-shirt to their cart
3. A user clicks “checkout”
4. A user actually purchases a t-shirt

## Notebook Contents

### 1. Introduction
The introduction provides an overview of the project and the steps involved in creating the funnel.

### 2. Importing Libraries and Data
The necessary libraries (e.g., pandas) are imported, and the data files (`visits.csv`, `cart.csv`, `checkout.csv`, `purchase.csv`) are read into pandas DataFrames.

### 3. Inspecting the DataFrames
We inspect the first few rows of each DataFrame to understand their structure and contents.

### 4. Merging DataFrames
We perform a series of left merges to combine the `visits`, `cart`, `checkout`, and `purchase` DataFrames into a single DataFrame (`page_visit_df`).

### 5. Analysis Steps
- Calculate the length of the merged DataFrame `visits_cart`.
- Determine the number of null timestamps for `cart_time`.
- Calculate the percentage of users who only visited.
- Calculate the percentage of users who placed a t-shirt in their cart but did not checkout.
- Calculate the percentage of users who got to checkout but did not purchase.
- Identify the weakest part of the funnel and suggest improvements.
- Calculate the average time to purchase.

## Key Findings
- **Visit Percentage:** 100%
- **Non-checkout Times:** 35.06%
- **Non-purchase Times:** 24.55%

The weakest part of the funnel is getting a user to add a t-shirt to their cart. Once users add a t-shirt to their cart, it is fairly likely they will complete the purchase. A suggestion to improve the funnel is to make the add-to-cart button more prominent on the front page.

## Conclusion
The analysis helps identify the stages in the funnel where users drop off and provides insights on how to improve the conversion rate. The average time to purchase is also calculated to understand user behavior better.

## How to Run the Notebook
1. Ensure you have Python and Jupyter Notebook installed.
2. Clone the repository.
3. Navigate to the project directory.
4. Run `jupyter notebook` in your terminal.
5. Open the `page_visits_funnel.ipynb` notebook and run the cells sequentially.

## Files
- `visits.csv`: Data on user visits to the website.
- `cart.csv`: Data on users adding t-shirts to their cart.
- `checkout.csv`: Data on users proceeding to checkout.
- `purchase.csv`: Data on users completing a purchase.

## Libraries Used
- pandas
