# PROGRAMMING ASSIGNMENT 3

This repository contains my Jupyter Notebook submission for **ECE 2112: Advanced Computer Programming and Algorithms – Experiment 3**, covering two Python problems.

> Source of problems: *EXPERIMENT 3 - Python Data Analysis.pdf*

---

## Project Structure

```
.
├─ Lucas_Pandas-P1.py      # Python script with Problem 1 solution
├─ Lucas_Pandas-P2.py      # Python script with Problem 2 solution
└─ README.md               # You're here
```

---

# PROBLEM 1

## Problem Description
**PROBLEM 1**: Save your file as Surname_Pandas-P1.py

Using knowledge obtained from the experiment and demonstrations:

  a. Load the corresponding .csv file into a data frame named cars using pandas

  b. Display the first five and last five rows of the resulting cars.

---

## Implementation and Explanation

### 1. Import the pandas library
We begin by importing the `pandas` library

```
import pandas as pd
```

### 2. Load the dataset
We use `pd.read_csv()` to read the CSV file named `'cars.csv'`. The data from the file is loaded into a DataFrame named `cars`. 

```
cars = pd.read_csv('cars.csv')              
```

### 3. Display the full DataFrame
Typing the DataFrame name (`cars`) outputs the full dataset so we can confirm it was loaded correctly.

```
cars               
```

### 4. Display the first 5 rows
The `.head()` method is used to view the first 5 rows of the DataFrame.

```
cars.head()    
```

### 5. Display the last 5 rows
Similarly, the .tail() method displays the last 5 rows of the DataFrame.

```
cars.tail()              
```

---

# PROBLEM 2

## PROBLEM DESCRIPTION
**PROBLEM 2**: Save your file as Surname_Pandas-P2.py

Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.

b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

--- 

## Implementation and Explanation

### 1. Import the pandas library
As before, we begin by importing the `pandas` library to work with tabular data.

```
import pandas as pd
```

### 2. Load the dataset
We use `pd.read_csv()` to read the CSV file named `'cars.csv'`. The data from the file is loaded into a DataFrame named `cars`. 

```
cars = pd.read_csv('cars.csv')              
```

### 3. Display the full DataFrame
Typing the DataFrame name (`cars`) outputs the full dataset so we can confirm it was loaded correctly.

```
cars               
```

### 4. Display the first 5 rows with odd-numbered columns
We use `.loc` to select rows and columns by index.

  - `:5` → first 5 rows
  - `1::2` → start from column index 1 and step by 2 (selecting every other column, i.e., columns 1, 3, 5, 7...)

```
cars.iloc[:5, 1::2] 
```

### 5. Display the row containing the 'Model' of Mazda RX4
We use `.loc` with a condition to filter rows where the `Model` column equals `"Mazda RX4"`.

```
cars.loc[cars['Model'] == 'Mazda RX4', ]           
```

### 6. Find how many cylinders ('cyl') the car model Camaro Z28 has
We again use `.loc` but specify the `['Model', 'cyl']` columns to only diplay the car's name and cylinder count.

```
cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]
```

### 7. Determine the cylinders ('cyl') and gear type ('gear') of specific car models
We filter multiple models using logical OR (`|`) conditions inside `.loc`. only the `['Model', 'cyl', 'gear']` columns are displayed for clarity.

```
cars. loc[
  (cars['Model'] == 'Mazda RX4 Wag') |
  (cars['Model'] == 'Ford Pantera L') |
  (cars['Model'] == 'Honda Civic') |
  ['Model', 'cyl', 'gear']
]
```

---

**Author:** LUCAS, Beatrice Sophia

**Section:** 2ECE-B

**Course:** ECE 2112 (Advanced Computer Programming and Algorithms)


