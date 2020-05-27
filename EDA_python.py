"""
Author: Thinh Mai
Date: 3/17/2020
Purpose: Final Exam - Question 3

"""

#load packages
import pandas as pd
import numpy as np
import os

os.chdir(r"C:\Users\Mai\Downloads\SalesData_Final\Output_File")
master = pd.read_csv("Consolidated.csv",sep=',',header = 0)
print("Overview the data")
print(master.head())
print(master.describe())
print(master.info)
print("===================================================\n\n")

#dropping unnecessary columns: [Unnamed 0] from the original file
master = master.drop(columns = ['Unnamed: 0'], axis = 1)

#check if there is any missing values
#zero missing values
print(master.isnull().sum(axis = 0))
print("===================================================\n\n")

#drop duplicates if there are any
master_dups = master[master.duplicated()]
print("Number of duplicates rows: {}".format(master_dups.shape[0]))
print("===================================================\n\n")

#total count
print("Records count for the data set")
print(master.count())
print("===================================================\n\n")

#create profit column:
master['Profit'] = (master['Units Sold'])*(master['Unit Price'] - master['Unit Cost'])

#Sales Chanel with most Profit
sales_p = master.groupby(['Sales Channel'],as_index=False)['Profit'].sum()
most_profit = sales_p.loc[sales_p['Profit'].idxmax()]['Sales Channel']
print("Sales Channel with the Most Profit: {}".format(most_profit))
print("===================================================\n\n")

#Sales Channel with the Most Revenue
#create revenue column
master['Revenue'] = master['Units Sold']  * master['Unit Price']

sales_r = master.groupby(['Sales Channel'],as_index=False)['Revenue'].sum()
most_revenue = sales_r.loc[sales_r['Revenue'].idxmax()]['Sales Channel']
print("Sales Channel with the Most Revenue: {}".format(most_revenue))
print("===================================================\n\n")

# Item Type with the Least Profit
items_p = master.groupby(['Item Type'],as_index=False)['Profit'].sum()
least_profit = items_p.loc[items_p['Profit'].idxmin()]['Item Type']
print("Item Type with the Least Profit: {}".format(least_profit))
print("===================================================\n\n")

# Item Type with the Least Revenue
items_r = master.groupby(['Item Type'],as_index=False)['Revenue'].sum()
least_revenue = items_r.loc[items_r['Revenue'].idxmin()]['Item Type']
print("Item Type with the Least Revenue: {}".format(least_revenue))
print("===================================================\n\n")

# Per Country, Per Month, Per Item Units Sold, Revenue, Cost & Profit
#create month column for grouping purpose
master['Month'] = pd.DatetimeIndex(master['OrderDate']).month
summary = master.groupby(['Country','Month','Item Type'])['Units Sold','Revenue','Unit Cost','Profit'].sum()
print("Per Country, Per Month, Per Item Units Sold, Revenue, Cost & Profit")
print(summary)
print("===================================================\n\n")

# World Wide Monthly top revenue generating channel with the revenue
master['Month'] = pd.DatetimeIndex(master['OrderDate']).month

# monthly_revenue_channel = pd.pivot_table(master,index = ['Month'],columns='Sales Channel', values = 'Revenue',aggfunc=np.sum)
monthly_revenue_channel = master.groupby(['Month','Sales Channel'])['Revenue'].sum().sort_values(ascending=True)
print("World Wide Monthly top revenue generating channel with the revenue")
print(monthly_revenue_channel.tail(1))
print("===================================================\n\n")

# Lifetime Top 10 Items with most units sold
top_10 = master[["Item Type","Units Sold"]].groupby("Item Type").sum().sort_values("Units Sold",ascending=False)
print("Lifetime Top 10 Items with most units sold")
print(top_10.head(10))
print("===================================================\n\n")

# Lifetime Bottom 10 Items with the least units sold
bottom_10 = master[["Item Type","Units Sold"]].groupby("Item Type").sum().sort_values("Units Sold",ascending=False)
print("Lifetime Bottom 10 Items with the least units sold")
print(bottom_10.tail(10))
print("===================================================\n\n")



