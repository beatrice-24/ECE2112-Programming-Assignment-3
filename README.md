# PROGRAMMING ASSIGNMENT 3

This repository contains my Jupyter Notebook submission for **ECE 2112: Advanced Computer Programming and Algorithms – Experiment 3**, covering two Python problems.

> Source of problems: *EXPERIMENT 3 - Python Data Analysis.pdf*

---

## Implementation and Explanation

### 1. Import the pandas library
We begin by importing the `pandas` library

```
import pandas as pd
```

### 2. Load the dataset
We use `pd.read_csv()` to read the CSV file named `'cars.csv'`. The data from the file is loaded into a DataFrame named `cars`. This allows us to easily manipulate and explore the tabular data.

```
cars = pd.read_csv('cars.csv')              
```

### 3. Display the full DataFrame
Typing the DataFrame name (`cars`) will output the entire contents of the DataFrame in most interactive environments like Jupyter Notebooks or IPython.

```
cars               
```

### 4. Dispaly the first 5 rows
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


