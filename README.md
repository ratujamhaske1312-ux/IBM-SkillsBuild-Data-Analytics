# E-Commerce Customer Churn Analysis

## Project Description
This project focuses on conducting user behavior analytics to understand why customers stop shopping on an e-commerce platform (churn). By generating and assessing a mock dataset of 500 customers, this system isolates churn trends across device preferences, transaction payment models, product domains, and customer experience scores to provide proactive business intelligence updates.

## Technologies Used
* **Python 3**
* **Pandas** (Data Manipulation and Aggregation)
* **Numpy** (Statistical Data Distribution and Mocking)

## Dataset Structure
The system processes an `ecommerce_data.csv` matrix featuring:
* `Customer_ID`: Unique account indicator
* `Device`: Access vector (Mobile App, Desktop, Tablet)
* `Category`: Purchase focus area (Electronics, Clothing, Home, Grocery)
* `Payment_Method`: Billing path used (Credit Card, UPI, Debit Card, Cash)
* `Churn`: Binary retention marker (Yes / No)
* `Satisfaction_Score`: User metric scale (1-5 stars)

## Setup & Run Instructions
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute the single-file pipeline script to create data parameters and view execution summaries:
   ```bash
   python Ratuja_EcommerceChurn.py
   ```

## Key Findings Summary
* **Highest At-Risk Domain**: Electronics leads all target sectors with 51 customer dropouts.
* **Metric Signal**: Dropping satisfaction scores highly correlate to structural churn states, yielding lower operational averages (3.45 out of 5 stars).
