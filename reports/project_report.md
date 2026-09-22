# E-Commerce Sales & Customer Analytics

## 1. Project Overview

This project analyzes e-commerce transaction data to understand sales performance, customer behavior, product performance, geographic markets, and sales trends over time.

The goal is to transform raw transaction data into meaningful business insights.

---

## 2. Dataset

The project uses the `Online Retail II` dataset containing e-commerce transaction records.

The dataset contains the following fields:

- Invoice
- StockCode
- Description
- Quantity
- InvoiceDate
- Price
- Customer ID
- Country

---

## 3. Data Cleaning

The raw dataset was inspected for missing values, duplicate records, invalid prices, unusual quantities, and cancellation-related transactions.

The following cleaning steps were performed:

- Converted `InvoiceDate` to datetime format.
- Identified missing values in `Description` and `Customer ID`.
- Retained transactions with missing customer IDs for overall sales analysis.
- Removed exact duplicate records.
- Investigated negative quantities and cancellation transactions.
- Removed records with negative prices.
- Created a separate `sales_data` dataset containing positive quantities and positive prices for sales analysis.

---

## 4. Feature Engineering

Several derived features were created to support analysis:

### Transaction Features

- `Revenue = Quantity × Price`

### Date Features

- Year
- Month
- Month Name
- Day
- Hour

### Customer Features

- Total Revenue
- Total Orders
- Total Quantity

### Product Features

- Total Revenue
- Total Orders
- Total Quantity

---

## 5. Exploratory Data Analysis

The analysis focused on:

- Overall sales performance
- Monthly sales trends
- Product performance
- Customer behavior
- Country-level performance
- Relationship between product quantity and revenue

### Key Metrics

- Total Revenue: approximately 20.48 million
- Total Orders: approximately 40,078
- Total Quantity Sold: approximately 11.21 million
- Average Order Value: approximately 510.92

---

## 6. Visualizations

The following visualizations were created using Matplotlib and Seaborn:

- Monthly Revenue Trend
- Monthly Orders Trend
- Top 10 Products by Revenue
- Top 10 Products by Quantity Sold
- Top 10 Customers by Revenue
- Top 10 Customers by Number of Orders
- Top 10 Countries by Revenue
- Revenue Distribution by Country
- Revenue vs Quantity by Product

---

## 7. Key Business Findings

- Product `M` generated the highest revenue among the top products, with approximately 339.6K in revenue.
- Product `84077` had the highest quantity sold, with 106,139 units, but generated approximately 24.4K in revenue.
- Customer `18102` generated the highest revenue among the analyzed customers, with approximately 581.0K.
- Customer `14646` purchased the highest quantity among the displayed top customers, with 367,193 units.
- Customer `14911` placed the highest number of orders, with 398 orders.
- The United Kingdom generated substantially more revenue than the other countries in the top-10 comparison.
- Monthly revenue and order trends showed variation in sales activity across different periods.
- Higher product sales volume did not necessarily result in higher revenue.

---

## 8. Business Recommendations 
- Monitor high-revenue products and ensure their availability is maintained.
- Investigate high-volume products to understand their pricing and revenue contribution.
- Analyze high-value customers to understand their purchasing patterns.
- Develop strategies to encourage repeat purchases.
- Monitor the United Kingdom market because of its substantial revenue contribution.
- Use monthly sales trends to support inventory planning and identify periods of higher sales activity.

---

## 9. Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git & GitHub

---

## 10. Conclusion

This project demonstrates an end-to-end data analytics workflow, starting with raw e-commerce transaction data and progressing through data understanding, cleaning, feature engineering, exploratory analysis, visualization, and business insight generation.

The analysis provides a structured view of sales, products, customers, countries, and time-based performance.