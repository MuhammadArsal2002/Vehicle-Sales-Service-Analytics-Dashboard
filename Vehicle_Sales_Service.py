# ==============================================================
# Project: Vehicle Sales and Service Data Cleaning & Analysis
# Author: Arsal Khalid
# Description: This script performs data cleaning, transformation,
# and basic analysis for car sales, services, and customer feedback.
# ==============================================================

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------------------
# Step 1: Load Datasets
# --------------------------------------------------------------
sales = pd.read_excel("sales_data.xlsx")
service = pd.read_excel("service_data.xlsx")
feedback = pd.read_excel("customer_feedback.xlsx")

# Display basic information and missing values
print("Sales Data Info:")
print(sales.info(), "\n")
print(sales.isnull().sum(), "\n")

print("Service Data Info:")
print(service.info(), "\n")
print(service.isnull().sum(), "\n")

print("Customer Feedback Info:")
print(feedback.info(), "\n")
print(feedback.isnull().sum(), "\n")

# --------------------------------------------------------------
# Step 2: Data Cleaning
# --------------------------------------------------------------

# Remove duplicate records
sales.drop_duplicates(inplace=True)
service.drop_duplicates(inplace=True)
feedback.drop_duplicates(inplace=True)

# Handle missing values
sales.fillna({'Price': sales['Price'].mean()}, inplace=True)
service.fillna({'Service_Cost': service['Service_Cost'].mean()}, inplace=True)
feedback.fillna({'Satisfaction_Rating': feedback['Satisfaction_Rating'].median()}, inplace=True)

# --------------------------------------------------------------
# Step 3: Data Transformation
# --------------------------------------------------------------

# Convert date columns to datetime format
sales['Sale_Date'] = pd.to_datetime(sales['Sale_Date'])
service['Service_Date'] = pd.to_datetime(service['Service_Date'])

# Extract year and month for trend analysis
sales['Sale_Year'] = sales['Sale_Date'].dt.year
sales['Sale_Month'] = sales['Sale_Date'].dt.month

service['Service_Year'] = service['Service_Date'].dt.year
service['Service_Month'] = service['Service_Date'].dt.month

# Merge sales and service data to calculate customer lifetime value
merged = pd.merge(
    sales, service,
    on='Customer_ID',
    how='outer',
    suffixes=('_sale', '_service')
)

merged['Customer_Lifetime_Value'] = merged['Price'] + merged['Service_Cost']

# --------------------------------------------------------------
# Step 4: Exploratory Data Analysis (EDA)
# --------------------------------------------------------------

# Top 10 best-selling car models
top_models = (
    sales.groupby('Vehicle_Model')['Price']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_models.plot(kind='bar', color='skyblue', title='Top 10 Best-Selling Car Models')
plt.ylabel("Total Sales (PKR)")
plt.xlabel("Vehicle Model")
plt.tight_layout()
plt.show()

# Average service cost by vehicle model
avg_service = (
    service.groupby('Vehicle_Model')['Service_Cost']
    .mean()
    .sort_values(ascending=False)
)

avg_service.plot(kind='barh', color='orange', title='Average Service Cost by Vehicle Model')
plt.xlabel("Average Service Cost (PKR)")
plt.ylabel("Vehicle Model")
plt.tight_layout()
plt.show()

# Customer satisfaction distribution
sns.countplot(x='Satisfaction_Rating', data=feedback, palette='coolwarm')
plt.title("Customer Satisfaction Distribution")
plt.xlabel("Satisfaction Rating")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# --------------------------------------------------------------
# Step 5: Export Cleaned Data
# --------------------------------------------------------------
merged.to_csv("cleaned_vehicle_data.csv", index=False)
print("Cleaned dataset exported successfully!")
