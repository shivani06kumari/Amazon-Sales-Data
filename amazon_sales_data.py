# -*- coding: utf-8 -*-
"""Amazon Sales Data

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QuHoaGx4AQ3-F9zs9JrWCvnAMnDzewp8

UNIFIED MENTOR DATA ANALYTICS INTERNSHIP

NAME: SHIVANI KUMARI

PROJECT1: AMAZON SALES DATA ANALYTICS

PROBLEM STATEMENT:  Sales management has gained importance to meet increasing competition and the
 need for improved methods of distribution to reduce cost and to increase profits. Sales
 management today is the most important function in a commercial and business
 enterprise.
 Do ETL: Extract-Transform-Load some Amazon dataset and find for me
 Sales-trend -> month-wise, year-wise, yearly_month-wise
 Find key metrics and factors and show the meaningful relationships between
 attributes. Do your own research and come up with your findings.
"""

pip install pandas numpy matplotlib seaborn plotly scikit-learn

#importing the necessary libraries
#for data manipulation and analysis
import pandas as pd
import numpy as np
#for data visualization
import matplotlib.pyplot as plt
import seaborn as sns
#for date and time manipulation
import datetime
#for interactive visualizations
import plotly.express as px
import plotly.graph_objects as go
#for advance data manipulations
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import os
print(os.getcwd())


#load the Dataset
df = pd.read_csv('/Amazon_Sales_data.csv')
df.head()
#data cleaning
missing_values=data.isnull().sum()
print("missing_vlaues :\n" ,missing_values)

"""there is no missing values or null values in the data, this means our data is already cleaned."""

#convert order date to datetime
data['Order Date'] = pd.to_datetime(data['Order Date'])
#extract year and month from order date
data['Year'] = data['Order Date'].dt.year
data['Month'] = data['Order Date'].dt.month
data.head()

"""Data Analysis"""

#calculate the number of regions
regions = data['Region'].nunique()
print('Number of regions:', regions)

"""There are 7 different regions in our dataset.

"""

#calculate the number of countries.
countries = data['Country'].nunique()
print('Number of countries:', countries)

"""There are 78 different countries in our datasets."""

#calculate the item Types
item_types = data['Item Type'].nunique()
print('Number of item types:', item_types)

"""There are 12 different item types in our dataset."""

#calculate total unit coast.
total_unit_cost = data['Unit Cost'].sum()
print('Total unit cost:', total_unit_cost)

#calculate the total cost
total_cost = data['Total Cost'].sum()
print('Total cost:', total_cost)

#calculate the total revenue
total_revenue = data['Total Revenue'].sum()
print('Total revenue:', total_revenue)

#calculate the total profit
total_profit = data['Total Profit'].sum()
print('Total profit:', total_profit)
data.groupby(['Region','Sales Channel'])['Total Profit'].sum()

# year wise Sales
year_sales = data.groupby('Year')['Total Revenue'].mean()
plt.figure(figsize=(10,5))
sns.barplot(x=year_sales.index, y=year_sales.values)
plt.xlabel('Year')
plt.ylabel('Total Revenue')
plt.title('Average Sales by Year')

#pie chart of tool profit in region wise
plt.figure(figsize=(10,5))
region_total_revenue = data.groupby('Region')['Total Profit'].mean()
plt.pie(region_total_revenue,startangle=99, labels=region_total_revenue.index, autopct='%1.1f%%')
plt.title('Average Profit in Region Wise')

#Group Total Revenue by Item type
total_revenue_item_types = data.groupby('Item Type')['Total Revenue'].sum()
#BAR chart for the total Revenue item type
plt.figure(figsize=(10,5))
total_revenue_item_types.plot(kind='bar')
plt.xlabel('Item Type')
plt.ylabel('Average Revenue by Product type')
plt.grid(axis='y')

#group total Revenue by sales channel
total_revenue_sales_channel = data.groupby('Sales Channel')['Total Revenue'].mean()
#BAR chart for the total Revenue by item type
plt.figure(figsize=(5,5))
plt.tight_layout()
total_revenue_sales_channel.plot(kind='pie', autopct='%1.1f%%', startangle=90)

plt.xlabel('Sales Channel')
plt.ylabel('Average Revenue')
plt.title('Total Revenue by Sales Channel')

#create a pie chart for a donut chart
region_unitsold = data.groupby('Region')['Units Sold'].sum()
plt.figure(figsize=(5,5))
region_unitsold.plot(kind='pie', startangle=90, labels=region_unitsold.index, autopct='%1.1f%%')

#draw a circle at the centre of the pie chart
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

#Equal aspects ration ensures that pie is drawn as a circle.
plt.title('Units Sold by Region')
plt.axis('equal')

import pandas as pd
#Read data from CSV
data = pd.read_csv('/Amazon_Sales_data.csv')

#Convert 'order date' to datetime
data['Order Date'] = pd.to_datetime(data['Order Date'])

#Extract year and month from 'order date'
data['Year'] = data['Order Date'].dt.year
data['Month'] = data['Order Date'].dt.month

#grouping the data by year and month and summing the units sold
yearmonthly_units_sold = data.groupby(['Year', 'Month'])['Units Sold'].sum()

#display the grouped data
print(yearmonthly_units_sold)

import matplotlib.pyplot as plt
#Reset the index to convert the grouped data into a dataframe
yearmonthly_units_sold_df = yearmonthly_units_sold.reset_index()

#convert year and month to a single datetime column
yearmonthly_units_sold_df['Date'] = pd.to_datetime(yearmonthly_units_sold_df[['Year', 'Month']].assign(day=1))

#sort by date for plotting
yearmonthly_units_sold_df = yearmonthly_units_sold_df.sort_values('Date')

#plotting the data
plt.figure(figsize=(10,5))
plt.plot(yearmonthly_units_sold_df['Date'], yearmonthly_units_sold_df['Units Sold'])
plt.xlabel('Date')
plt.ylabel('Units Sold')
plt.title('Units Sold Over Time')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
#assuming 'Yearmonth_unitsold' contains the grouped data you have shown
#Reset the index to convert the grouped data into a dataframe
yearmonthly_units_sold_df = yearmonthly_units_sold.reset_index()

#plotting the data
plt.figure(figsize=(10,5))
plt.bar(yearmonthly_units_sold_df['Year'], yearmonthly_units_sold_df['Units Sold'])
plt.xlabel('Year')
plt.ylabel('Units Sold')
plt.title('Units Sold Over Time')

plt.show()

#Group by Total sales channel
totalcost_saleschannel=data.groupby('Sales Channel')['Total Cost'].sum()
totalcost_saleschannel= data.groupby('Sales Channel')['Total Cost'].sum()

#Bar chart for total cost by sales channel
plt.figure(figsize=(6,6))
totalcost_saleschannel.plot(kind='pie', autopct='1.1%%',startangle=90)
plt.title('Total Cost by Sales Channel')