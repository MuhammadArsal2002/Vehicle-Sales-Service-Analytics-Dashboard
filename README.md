# Vehicle-Sales-Service-Analytics-Dashboard

<img width="1485" height="835" alt="Screenshot 2025-10-17 044249" src="https://github.com/user-attachments/assets/373aeaf4-13c0-439d-b9be-7bfb122dc184" />

Overview

This project shows a complete data analysis process for a vehicle company, covering both car sales and car services. It includes everything from data cleaning to creating a final interactive dashboard in Power BI. The goal was to understand sales performance, service trends, and customer feedback using real-world data practices.

<img width="1486" height="837" alt="Screenshot 2025-10-17 044239" src="https://github.com/user-attachments/assets/fdce559f-bee4-4055-b2bd-74a9f2634db4" />

Project Steps:

1.	Data Preparation:
The raw datasets were created for car sales, service records, and customer feedback (each with over 10,000 rows).
I used Python for cleaning and combining the data. The cleaning process included removing duplicates, handling missing values, and converting data types for analysis.

2.	Data Storage and Analysis:
After cleaning, the data was stored and tested using MySQL for queries and validation.
Excel files were also used for manual review and to check the accuracy of results before visualization.

3.	Dashboard Creation:
    Finally, I built an interactive Power BI dashboard with two pages — one for Car Sales and one for Car Services.

Dashboard Pages:
1. Car Sales Dashboard

⦁	Shows total and average sales.
⦁	Highlights top-selling car models and brands.
⦁	Displays sales trends by month and year.
⦁	Lets the user filter data by region or model using slicers.

2. Car Services Dashboard

⦁	Focuses on service cost, type, and frequency.
⦁	Compares total service cost across different vehicle types.
⦁	Includes insights on customer feedback and repair trends.

Files Included

⦁	cleaned_vehicle_data.csv — cleaned data file created using Python.
⦁	sales_data.xlsx — dataset for car sales.
⦁	service_data.xlsx — dataset for service details.
⦁	customer_feedback.xlsx — dataset for customer responses.
⦁	data_cleaning.py — Python file used for cleaning and transforming the data.

Tools Used

⦁	Python: Data cleaning and preprocessing
⦁	MySQL: Querying and validation
⦁	Excel: Data checking and summaries
⦁	Power BI: Dashboard and visualization

Insights

⦁	Identified top-performing car models and high-revenue regions.
⦁	Found patterns in service costs and customer satisfaction.
⦁	Helped show how sales and service data can be combined to support business decisions.



You can view the full Power BI dashboard here: https://app.powerbi.com/view?r=eyJrIjoiYWQ3YWU4ZmYtZjYyNi00MWNkLThiYjgtYmRmOWU5MzRiYjg4IiwidCI6ImVkY2ZiMTUwLTMwOWEtNGIwOS04YzM4LWMyZmVhOGRjNzA4MSIsImMiOjl9



Python Script: data_cleaning.py

This Python script handles the data cleaning, transformation, and initial analysis steps for the Vehicle Sales and Service Dashboard project.
It combines data from multiple sources, removes errors, and prepares it for visualization in Power BI.

The main tasks performed in this file include:

<img width="933" height="758" alt="Screenshot 2025-10-17 050835" src="https://github.com/user-attachments/assets/c4b329d4-7d90-4881-9334-f96c954a9cb9" />


Loading Data:
⦁	The script imports three Excel files:
⦁	sales_data.xlsx
⦁	service_data.xlsx
⦁	customer_feedback.xlsx
⦁	These files contain raw data related to vehicle sales, service records, and customer ratings.

<img width="1008" height="335" alt="Screenshot 2025-10-17 050846" src="https://github.com/user-attachments/assets/5c543b28-fdb4-4e1e-a254-74e38ce9dd08" />

Data Cleaning

⦁	Removes duplicate entries from all datasets.
⦁	Handles missing values by replacing them with the average or median.
⦁	Ensures all numeric columns are clean and consistent.

<img width="992" height="588" alt="Screenshot 2025-10-17 050853" src="https://github.com/user-attachments/assets/027ed7d4-92be-4ca1-9dba-023060465e5c" />

Data Transformation

⦁	Converts date columns into proper datetime format.
⦁	Extracts year and month for trend analysis.
⦁	Merges sales and service data to calculate Customer Lifetime Value (total amount spent on purchases and services).


<img width="1078" height="716" alt="Screenshot 2025-10-17 050905" src="https://github.com/user-attachments/assets/0c9ed12f-f79b-4586-a247-2a668099993c" />

Exploratory Data Analysis (EDA)

⦁	Identifies the top 10 best-selling car models.
⦁	Calculates and visualizes the average service cost by model.
⦁	Analyzes customer satisfaction ratings using Seaborn charts.

<img width="941" height="336" alt="Screenshot 2025-10-17 050912" src="https://github.com/user-attachments/assets/4a68e6d1-a42c-4f3c-afb9-289eed134b9b" />

Exporting Cleaned Data
⦁	The final cleaned dataset is exported as cleaned_vehicle_data.csv, which is later used to build the Power BI dashboard.


Tools and Libraries Used
⦁	Pandas – For cleaning, merging, and managing data
⦁	NumPy – For handling numerical operations
⦁	Matplotlib & Seaborn – For data visualization and analysis

Output
After running the script:
⦁	A clean CSV file (cleaned_vehicle_data.csv) is generated
⦁	Multiple visualizations are displayed to understand key sales and service trends
⦁	The cleaned data is ready for use in SQL or Power BI



📬 Contact Name: Muhammad Arsal(Data Analyst) Email: arsal.khalid2002gmail.com LinkedIn: https://www.linkedin.com/in/muhammad-arsal-a57144385/







