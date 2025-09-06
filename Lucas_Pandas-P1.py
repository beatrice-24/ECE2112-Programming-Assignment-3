#!/usr/bin/env python
# coding: utf-8

# **PROBLEM 1**: Save your file as Surname_Pandas-P1.py
# 
# Using knowledge obtained from the experiment and demonstrations:
# 
# a. Load the corresponding .csv file into a data frame named cars using pandas

# In[7]:


import pandas as pd

cars = pd.read_csv('cars.csv')   # Loads 'cars.csv' into a DataFrame called cars
cars                             # Displays the entire DataFrame                           


# In[8]:


cars.head()   # Displays the first 5 rows of the DataFrame


# In[9]:


cars.tail()   # Displays the last 5 rows of the DataFrame

