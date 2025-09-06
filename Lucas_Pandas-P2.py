#!/usr/bin/env python
# coding: utf-8

# **PROBLEM 2**: Save your file as Surname_Pandas-P2.py
# 
# Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
# indexing operations.

# In[17]:


import pandas as pd

cars = pd.read_csv('cars.csv')   # Loads 'cars.csv' into a DataFrame called cars
cars                             # Displays the entire DataFrame   


# a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.

# In[19]:


cars.iloc[:5, 1::2]   # Selects first 5 rows and columns from index 1 onwards, stepping by 2 (every other column)


# b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

# In[21]:


cars.loc[cars['Model'] == 'Mazda RX4', ]   # Selects all columns for rows where 'Model' is 'Mazda RX4'


# c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

# In[23]:


cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]   # Selects 'Model' and 'cyl' columns for rows where 'Model' is 'Camaro Z28'


# d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
# Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have

# In[25]:


cars.loc[
    (cars['Model'] == 'Mazda RX4 Wag') | (cars['Model'] == 'Ford Pantera L') | (cars['Model'] == 'Honda Civic'), 
    ['Model', 'cyl', 'gear']]   
    # Selects 'Model', 'cyl', and 'gear' columns for rows where 'Model' matches any of the three specified models

