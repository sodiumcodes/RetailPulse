# E-Commerce Sales & Customer Analytics

A data analytics project focused on understanding sales performance, product behavior, customer purchasing patterns, geographical trends, and time-based sales patterns using transactional e-commerce data.

## Project Overview

The goal of this project is to take raw transactional e-commerce data, clean and transform it, perform exploratory and business-oriented analysis, and present the findings through an interactive dashboard.

Rather than focusing only on visualization, the project aims to answer meaningful business questions and derive actionable insights from the data.

## Objectives

* Understand and clean the raw transactional data
* Identify and handle data-quality issues
* Analyze sales and revenue trends
* Identify top-performing products
* Analyze customer purchasing behavior
* Compare performance across countries
* Investigate seasonal and time-based patterns
* Create meaningful business metrics
* Build an interactive analytics dashboard
* Document the complete analytical process

## Dataset

The project uses the **Online Retail II** transactional dataset.

The dataset contains information such as:

* Invoice / transaction ID
* Product ID
* Product description
* Quantity purchased
* Invoice date
* Unit price
* Customer ID
* Country

The raw dataset is stored in:

```text
data/raw/
```

## Tech Stack

* **Python 3.12**
* **NumPy** — numerical computation
* **Pandas** — data cleaning and analysis
* **Matplotlib** — data visualization
* **Seaborn** — statistical visualization
* **Plotly / Cufflinks** — interactive visualizations
* **Streamlit** — interactive dashboard
* **Jupyter Notebook** — exploratory analysis
* **Git & GitHub** — version control

## Project Structure

```text
ecommerce-analytics/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_analysis.ipynb
│   └── 04_customer_product_analysis.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── analysis.py
│   └── utils.py
│
├── dashboard/
│   └── app.py
│
├── reports/
│   ├── figures/
│   └── project_report.md
│
├── tests/
│   └── test_data_pipeline.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── LICENSE
```

## Analytical Questions

The project will investigate questions such as:

1. How has revenue changed over time?
2. Which countries generate the most revenue?
3. Which products sell the most units?
4. Which products generate the most revenue?
5. Do the highest-volume products also generate the highest revenue?
6. What is the average order value?
7. How many customers are repeat customers?
8. Which customers contribute the most revenue?
9. How frequently do customers purchase?
10. Are there seasonal or weekday purchasing patterns?
11. Which markets or products appear to be underperforming?

These questions may evolve as we understand the dataset better.

## Project Workflow

```text
Raw Data
   ↓
Data Understanding
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Exploratory Data Analysis
   ↓
Business Analysis
   ↓
Visualization
   ↓
Interactive Dashboard
   ↓
Insights & Recommendations
```

## Key Metrics

Some of the metrics we plan to investigate include:

* Total Revenue
* Total Orders
* Units Sold
* Average Order Value
* Unique Customers
* Unique Products
* Revenue by Country
* Revenue by Product
* Customer Purchase Frequency
* Customer Revenue Contribution
* Repeat Customer Rate

The exact definitions of these metrics will be documented during the analysis.

## Dashboard

An interactive dashboard will be developed using Streamlit to allow users to explore:

* Overall sales performance
* Revenue trends
* Product performance
* Customer behavior
* Geographic performance
* Time-based purchasing patterns

> Dashboard screenshots and the deployed application link will be added after the dashboard is completed.

## Data Quality

The dataset will be inspected for issues such as:

* Missing values
* Duplicate records
* Cancelled transactions
* Invalid or zero prices
* Negative quantities
* Incorrect data types
* Date/time inconsistencies

All important cleaning decisions will be documented rather than silently removing data.

## Current Status

### Phase 0 — Project Setup

* [x] Repository created
* [x] Project folder structure created
* [x] Virtual environment configured
* [x] `requirements.txt` created
* [x] `.gitignore` created
* [x] Initial README created

### Phase 1 — Data Understanding

* [x]Load raw dataset
* [x]Inspect dataset dimensions
* [x]Inspect columns and data types
* [x] Analyze missing values
* [x] Analyze duplicates
* [x] Investigate unusual values
* [x]Understand transaction/cancellation structure
* [x]Document initial observations

### Phase 2 — Data Cleaning

* [ ] Define cleaning rules
* [ ] Clean transaction data
* [ ] Validate cleaned dataset
* [ ] Save processed dataset

### Phase 3 — Feature Engineering

* [ ] Create revenue metric
* [ ] Create time-based features
* [ ] Create order-level metrics
* [ ] Create customer-level metrics
* [ ] Create product-level metrics

### Phase 4 — Analysis

* [ ] Sales analysis
* [ ] Product analysis
* [ ] Customer analysis
* [ ] Geographic analysis
* [ ] Time-based analysis

### Phase 5 — Dashboard

* [ ] Build Streamlit dashboard
* [ ] Add KPIs
* [ ] Add filters
* [ ] Add interactive visualizations
* [ ] Test dashboard

### Phase 6 — Finalization

* [ ] Document key findings
* [ ] Add dashboard screenshots
* [ ] Improve README
* [ ] Add project report
* [ ] Prepare resume bullets
* [ ] Prepare interview explanation


## Author

Naina Dugar

This project was built as part of a hands-on data analytics portfolio to demonstrate practical skills in Python, data manipulation, exploratory analysis, visualization, and analytical storytelling.
