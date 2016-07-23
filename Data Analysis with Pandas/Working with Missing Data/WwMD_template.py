
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Data Analysis with Pandas

# ##Working with Missing Data

# ###1: Finding the missing data

# Missing data can be presented a few different ways.
# 
# In python, we have the None keyword and type, which indicates no value.
# 
# pandas uses NaN, which stands for "not a number", to indicate a missing value.
# 
# We can also call NaN a null value.

# ####Instructions

# Count the number of null values in the "Age" column.
# 
# Assign the result to age_null_count.

# In[2]:

import pandas as pd

f = "data/titanic.csv"
titanic_survival = pd.read_csv(f)

titanic_survival.head(5)


# In[3]:

# Print age column.
#print titanic_survival["age"]

# Use the isnull function to find which values in a column are missing
age_null = pd.isnull(titanic_survival["age"])

age_null_true = age_null[age_null == True]
age_null_count = len(age_null_true)
print("age_null_count:", age_null_count)


# ###2: Whats the big deal with missing data?

# So, we know that quite a few values are missing in the "age" column, and other columns are missing data, too, but why is this a problem?
# 
# Let's try to compute the average age of passengers on the Titanic.

# ####Instructions

# Use age_null to create a vector that only contains values from the "age" column that aren't "NaN".
# 
# Compute the mean of the new vector, and assign the result to correct_mean_age.

# In[4]:

import pandas as pd

mean_age = sum(titanic_survival["age"]) / len(titanic_survival["age"])

# 'mean_age' is NaN.  This is because any calculations we do with a null value also result in a null value.
print("mean_age:", mean_age)

# Filter the missing values out before we compute the mean.
age_null = pd.isnull(titanic_survival["age"])
good_ages = titanic_survival["age"][age_null == False]
correct_mean_age = sum(good_ages) / len(good_ages)

print("correct_mean_age:", correct_mean_age)


# ###3: Easier ways to do math

# Luckily, missing data is so common that pandas automatically filters for it with some methods.
# 
# We can use the .mean() method to compute the mean, and it will automatically remove missing values.

# ####Instructions

# Assign the mean of the "fare" column to 'correct_mean_fare'.

# In[5]:

import pandas as pd

# This is the same value that we computed in the last screen, but it's much simpler.
correct_mean_age = titanic_survival["age"].mean()
print("correct_mean_age:", correct_mean_age)

correct_mean_fare = titanic_survival["fare"].mean()
print("correct_mean_fare:", correct_mean_fare)


# ###4: Computing summary statistics

# Let's compute some more advanced statistics about the data.

# ####Instructions

# Fill in the missing code to compute fare_for_class for the given pclass.
# 
# When the loop is done, fares_by_class should have 1, 2, and 3 as keys, with the average fares as the corresponding values.

# In[6]:

# Passengers are divided into classes based on the "pclass" column
passenger_classes = [1, 2, 3]

# Create dictionary.
fares_by_class = {}
for pclass in passenger_classes:
    # Return fares for pclass.
    pclass_fares = titanic_survival["fare"][titanic_survival["pclass"] == pclass]
    # Calculate pclass mean fare.
    fare_for_class = pclass_fares.mean()
    # Store in 'fares_by_class' dictionary.
    fares_by_class[pclass] = fare_for_class

print("fares_by_class[1]:", fares_by_class[1])
print("fares_by_class[2]:", fares_by_class[2])
print("fares_by_class[3]:", fares_by_class[3])


# ###5: Making pivot tables

# Let's compute the survival probability for each passenger class in the Titanic.
# 
# In order to help us out, we'll use the pivot_table method on dataframes -- it makes doing analysis like what we did in the last screen much simpler.
# 
# If you're familiar with pivot tables in excel, this will look familiar.

# ####Instructions

# Use the pivot_table method to compute the mean "age" for each passenger class ("pclass").
# 
# Assign the result to passenger_age.

# In[7]:

import pandas as pd
import numpy as np

# index specifies which column to subset data based on 
# values specifies which column to subset based on the index
# The aggfunc specifies what to do with the subsets
# In this case, we split survived into 3 vectors, one for each passenger class, and take the mean of each
passenger_survival = titanic_survival.pivot_table(index="pclass", values="survived", aggfunc=np.mean)
print("passenger_survival:", passenger_survival)

passenger_age = titanic_survival.pivot_table(index="pclass", values="age", aggfunc=np.mean)
print("passenger_age", passenger_age)

passenger_fare = titanic_survival.pivot_table(index="pclass", values="fare", aggfunc=np.mean)
print("passenger_fare:", passenger_fare)


# ###6: More complex pivot tables

# We can use the pivot_table method to do more advanced things than we just did.
# 
# For starters, we can make more complex pivot tables that show multiple values at once.

# ####Instructions

# Make a pivot table that computes the mean "age", survival chance("survived"), and "fare" for each embarkation port ("embarked").
# 
# Assign the result to 'port_stats'.
# 
# Make sure to put the values list in the same order that the columns are given here.

# In[8]:

import numpy as np

# Compute the mean survival chance and the mean age for each passenger class.
passenger_survival = titanic_survival.pivot_table(index="pclass", values=["age", "survived"], aggfunc=np.mean)
print("passenger_survival:\n", passenger_survival)

port_stats = titanic_survival.pivot_table(index="embarked", values=["age", "survived", "fare"], aggfunc=np.mean)
print("port_stats:\n", port_stats)


# ###7: Drop missing values

# We looked at how to remove missing values in a vector of data, but how about in a matrix?
# 
# We can use the dropna method on pandas dataframes to do this.
# 
# Using the method will drop any rows that contain missing values.

# ####Instructions

# Drop all rows in titanic_survival where the columns "age", "body", or "home.dest" have missing values.
# 
# Assign the result to new_titanic_survival.

# In[9]:

import pandas as pd

# Drop all rows that have missing values.
new_titanic_survival = titanic_survival.dropna()

# We have an empty dataframe now because every row has at least one missing value.
#print(new_titanic_survival)

# We can also use the axis argument to drop columns that have missing values
new_titanic_survival = titanic_survival.dropna(axis=1)
#print(new_titanic_survival)

# We can use the subset argument to only drop rows if certain columns have missing values.
# This drops all rows where "age" or "sex" is missing.
new_titanic_survival = titanic_survival.dropna(subset=["age", "sex"])
#print(new_titanic_survival)

new_titanic_survival = titanic_survival.dropna(subset=["age", "body", "home.dest"])
new_titanic_survival.head(5)


# ###8: Row indices

# In pandas, dataframes and series have row indexes.
# 
# These work just like column indexes, and can take values like numbers, characters, and strings.

# ####Instructions

# Assign the row with index 25 to row_index_25.
# 
# Assign the fifth row to row_position_fifth.

# In[10]:

# Print out the first 5 rows in 'titanic_survival'.
#print(titanic_survival.iloc[:5,:])

new_titanic_survival = titanic_survival.dropna(subset=["body"])

# Print out the first 5 rows in 'new_titanic_survival'.
#print(new_titanic_survival.iloc[:5,:])

# Print out 4th row in 'new_titanic_survival'.
row_index_4 = new_titanic_survival.iloc[4,:]
print("row_index_4:\n", row_index_4)

# .loc instead addresses rows and columns by index, not position
# This actually prints the first row, because it has index 3
#print(new_titanic_survival.loc[3,:])

row_index_25 = new_titanic_survival.loc[25,:]
print("row_index_25:\n", row_index_25)

row_position_fifth = new_titanic_survival.iloc[4,:]
print("row_position_fifth:\n", row_position_fifth)


# ###9: Column indices

# We can also index columns using the .loc[] method.

# ####Instructions

# Assign the value at row index 1100, column index "age" to row_1100_age.
# 
# Assign the value at row index 25, column index "survived" to row_25_survived.

# In[11]:

new_titanic_survival = titanic_survival.dropna(subset=["body"])
print("new_titanic_survival[:5]:\n", new_titanic_survival[:5])

# Print the value in the first column of the first row.
#print(new_titanic_survival.iloc[0,0])

# Prints the value at row index 3 and column "pclass".
#print(new_titanic_survival.loc[3,"pclass"])

#row_1100_age = new_titanic_survival.loc[1100, "age"]
row_25_survived = new_titanic_survival.loc[25, "survived"]

#print(row_25_survived)


# ###10: Reindex rows

# Remember how new_titanic_survival didn't have sequential row indexes?
# 
# Each row retained its original index from titanic_survival.
# 
# Sometimes it is useful to reindex, and make new indexes starting from 0.
# 
# To do this, we can use the reset_index() method.

# ####Instructions

# Use the dropna method to remove rows that have missing values in the "age" or "boat" columns.
# 
# Then, reindex the resulting dataframe so the row indexes start from 0.
# 
# Assign the final result to titanic_reindexed.

# In[12]:

new_titanic_survival = new_titanic_survival.reset_index(drop=True)
print("new_titanic_survival[:5]:\n", new_titanic_survival[:5])

new_titanic_survival = titanic_survival.dropna(subset=["age", "boat"])
titanic_reindexed = new_titanic_survival.reset_index(drop=True)


# ###11: Use the apply function

# The first step we need to take to figure out the age breakdown is to learn about the .apply() method.
# 
# By default, .apply() will iterate through each column in a dataframe, and perform a function on it.
# 
# The column will be passed into the function.
# 
# The result from the function will be combined with all of the other results, and placed into a new series.
# 
# The function results will have the same position as the column they were generated from.

# ####Instructions

# Write a function to count up the number of non-null elements in a series.
# 
# Use the .apply() method, along with your function, to run across all the columns in titanic_survival.
# 
# Assign the result to column_not_null_count.

# In[13]:

import pandas as pd

# Function counts the number of null values in a series.
def null_count(column):
    # Make a vector that contains True if null, False if not.
    column_null = pd.isnull(column)
    # Create a new vector with only values where the series is null.
    null = column[column_null == True]
    # Return the count of null values.
    return len(null)

# Compute null counts for each column.
column_null_count = titanic_survival.apply(null_count)
print("column_null_count:\n", column_null_count)

def not_null_count(column):
    column_null = pd.isnull(column)
    null = column[column_null == False]
    return len(null)

column_not_null_count = titanic_survival.apply(not_null_count)


# ###12: Applying a function to a row

# By passing in the axis argument, we can use the .apply() method to iterate over rows, not columns.

# ####Instructions

# If someone is under 18, they are a "minor". If they are over 18, they are an "adult". If their age is missing (is null), their age is "unknown".
# 
# Make a function that returns the string "minor" if someone is under 18, "adult" if they are over 18, and "unknown" if their age is null.
# 
# Then, use the function along with .apply() to find the right label for everyone.
# 
# Assign the result to age_labels.
# 
# You can use isnull to check if a value is null or not.

# In[14]:

import pandas as pd

# Function will check if a row is an entry for a minor (under 18), or not.
def is_minor(row):
    if row["age"] < 18:
        return True
    else:
        return False

# This is a boolean series with the same length as the number of rows in titanic_survival
# Each entry is True if the row at the same position is a record for a minor
# The axis of 1 specifies that it will iterate over rows, not columns
minors = titanic_survival.apply(is_minor, axis=1)

def generate_age_label(row):
    age = row["age"]
    if pd.isnull(age):
        return "unknown"
    elif age < 18:
        return "minor"
    else:
        return "adult"

age_labels = titanic_survival.apply(generate_age_label, axis=1)

print("age_labels[:5]:\n", age_labels[:5])


# ###13: Computing survival percentage by age group

# Now that we have age labels for everyone, let's make a pivot table to find survival chance by age group.

# ####Instructions

# Make a pivot table that computes the mean survival chance("survived"), for each age group ("age_labels").
# 
# Assign the result to age_group_survival.

# In[15]:

import numpy as np

#age_group_survival = titanic_survival.pivot_table(index="age_labels", values=["survived"], aggfunc=np.mean)

