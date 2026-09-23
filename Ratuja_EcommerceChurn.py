import pandas as pd
import numpy as np

# Set random seed for consistent results
np.random.seed(42)

# Generate realistic data for 500 customers
data = {
    'Customer_ID': [f'CUST_{1000 + i}' for i in range(500)],
    'Device': np.random.choice(['Mobile App', 'Desktop', 'Tablet'], size=500, p=[0.5, 0.4, 0.1]),
    'Category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Grocery'], size=500, p=[0.4, 0.3, 0.2, 0.1]),
    'Payment_Method': np.random.choice(['Credit Card', 'UPI', 'Debit Card', 'Cash'], size=500, p=[0.45, 0.35, 0.15, 0.05]),
    'Churn': np.random.choice(['Yes', 'No'], size=500, p=[0.25, 0.75]),
    'Satisfaction_Score': np.random.choice([1, 2, 3, 4, 5], size=500, p=[0.1, 0.15, 0.2, 0.3, 0.25])
}

df = pd.DataFrame(data)
df.to_csv('ecommerce_data.csv', index=False)
print("Successfully created 'ecommerce_data.csv' with 500 rows!")

print("\n--- E-COMMERCE CHURN PROJECT ANALYSIS ---")
total_customers = len(df)
print(f"Total Customers in Dataset: {total_customers}")

churn_counts = df['Churn'].value_counts()
churn_yes = churn_counts.get('Yes', 0)
churn_rate = (churn_yes / total_customers) * 100
print(f"Overall Churn Rate: {churn_rate:.1f}%")

print("\n--- Churn Count by Login Device ---")
print(df[df['Churn'] == 'Yes']['Device'].value_counts())

print("\n--- Churn Count by Product Category ---")
print(df[df['Churn'] == 'Yes']['Category'].value_counts())

print("\n--- Average Satisfaction Score (Out of 5) ---")
print(df.groupby('Churn')['Satisfaction_Score'].mean())
