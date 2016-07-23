
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Data Analysis with Pandas

# ##Pandas Internals: DataFrames

# ###1: Shared index

# DataFrame objects were designed to easily query and interact with many columns, each of which is represented as a Series object. We discussed how Series objects work in the previous mission and in this mission we'll learn about how DataFrames build on Series objects to provide a powerful data analysis toolkit. 
# 
# Series objects maintain data alignment between the index labels and the data values. Since DataFrame objects are, at the core, a collection of columns where each column is a Series, they also maintain alignment along both the columns and the rows. Pandas DataFrames utilize a shared row index across columns, which is an integer index by default. By default, Pandas enforces this shared row index by throwing an error if you read in a CSV where the columns don't contain exactly the same number of elements.
# 
# Whenever you call a method that returns or prints a DataFrame, the left-most column contains the values for the index. You can use the index attribute to access the values in the index directly as well. For this mission, we're going to continue working with the dataset containing average user and critic ratings from the major film review sites. FiveThirtyEight has compiled the dataset and made it available on their <a href = "https://github.com/fivethirtyeight/data/tree/master/fandango">Github repo</a>.

# ####Instructions

# Read in fandango_score_comparison.csv into a DataFrame object named fandango. Then print the first 2 rows of the dataset using the head() method. Finally, print the index of the DataFrame use the index attribute.

# In[2]:

import pandas as pd
fandango = pd.read_csv('data/fandango_score_comparison.csv')

fandango.head(2)


# In[3]:

print("fandango.index:\n", fandango.index)


# ###2: Selecting using integer index

# In the previous cell, we observed the default integer index that Pandas uses for the DataFrame. In Series, each unique index value refers to a data value but in DataFrames, each index refers to an entire row. We can use the integer index to select rows a few different ways:
# 
#     # First 5 rows
#     fandango[0:5]
#     # From row at 140 and higher
#     fandango[140:]
#     # Just row at index 150
#     fandango.iloc[50]
#     # Just row at index 45 and 90
#     fandango.iloc[[45,90]]
# 
# 
# To select a slice, or a continuous sequence, of rows, use bracket notation, similar to when working with lists. To select an individual row, however, you need to use the <a href = "http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.iloc.html">iloc[] method</a>. The iloc[] method accepts a few different objects for selection:
# 
# - an integer
# - list of integers
# - slice object
# - Boolean array
# 
# When selecting an individual row, Pandas will return a Series object but when selecting multiple rows, a DataFrame, representing a subset of the original DataFrame, will be returned.

# ####Instructions

# Return a DataFrame containing just the first and the last row and assign to first_last.

# In[4]:

first_row = 0
last_row = fandango.shape[0] - 1

first_last = fandango.iloc[[first_row, last_row]]
first_last


# ###3: Custom Index

# The DataFrame object contains a set_index() method that allow you to pass in the column name you'd like Pandas to use as the index for the DataFrame. Pandas by default will return a new DataFrame with the custom index and will drop the specified column from the DataFrame, but the set_index() method contains a few parameters to tweak this behavior:
# 
# - inplace: if set to True, will set the index to the current DataFrame instead of returning a new one
# - drop: if set to False, will keep the column you specified for the index in the DataFrame

# ####Instructions

# Use the Pandas DataFrame method set_index to assign the FILM column as the custom index for the DataFrame without the FILM column dropped from the DataFrame. We want to keep the original DataFrame so assign the new DataFrame to fandango_films. 
# 
# Then print the index of fandango_films, which you access using the index attribute.

# In[5]:

fandango = pd.read_csv("data/fandango_score_comparison.csv")
fandango_films = fandango.set_index('FILM', drop=False)
print("fandango_films.index:\n", fandango_films.index)


# ###4: Selection using custom index

# Now that we have a custom index, we can select rows using film names instead of by the row number (integer index). To select rows using the custom index, you can use the loc[] method, which mirrors the iloc[] method in usage, or slice using bracket notation:
# 
#     # Slice using either bracket notation or loc[]
#     fandango_films["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]
#     fandango_films.loc["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]
# 
#     # Specific movie
#     fandango_films.loc['Kumiko, The Treasure Hunter (2015)']
# 
#     # Selecting list of movies
#     movies = ['Kumiko, The Treasure Hunter (2015)', 'Do You Believe? (2015)', 'Ant-Man (2015)']
#     fandango_films.loc[movies]
# 
# When selecting multiple rows, a DataFrame is returned, but when selecting an individual row, a Series object is returned instead. Similar to with Series objects, Pandas will maintain the original integer index even if you specify a custom index so you can still take advantage of selection by row number.

# ####Instructions

# Select just these movies in the following order from fandango_films:
# 
# - "The Lazarus Effect (2015)"
# - "Gett: The Trial of Viviane Amsalem (2015)"
# - "Mr. Holmes (2015)"
# 
# and assign to best_movies_ever.

# In[6]:

movies = ["The Lazarus Effect (2015)", "Gett: The Trial of Viviane Amsalem (2015)", "Mr. Holmes (2015)"]

best_movies_ever = fandango_films.loc[movies]
best_movies_ever


# ###5: Apply() over columns

# The apply() method in Pandas allows us to specify Python logic that we want evaluated over Series objects in a DataFrame. Recall that rows and columns are both represented as Series objects in a DataFrame. Here are some of the things we can accomplish using the apply() method:
# 
# - calculate the standard deviations for each numeric column
# - lower-case all film names in the FILM column
# 
# The apply() method requires you to pass in a vectorized operation that can be applied over each Series object. By default, the method runs over the DataFrame's columns but you can use the axis parameter to change this (which we'll dive into later). If the vectorized operation usually returns a single value (e.g. the NumPy std() function), a Series object will be returned containing the computed value for each column. If it instead usually returns a value for each element (e.g. multiplying or dividing by 2), a DataFrame will be returned instead with the transformation made over all the values.
# 
# In the following code cell, we filter to just the float columns and use the the apply() method calculate the standard deviation using the <a href = "http://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html">NumPy std() function</a>. Under the hood, Pandas takes advantage of Series objects' vectorized operations to apply the NumPy function for each iteration of the apply() method and return a final Series object.

# In[7]:

import numpy as np

# returns the data types as a Series
types = fandango_films.dtypes
# filter data types to just floats, index attributes returns just column names
float_columns = types[types.values == 'float64'].index
# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]

# `x` is a Series object representing a column
deviations = float_df.apply(lambda x: np.std(x))

print("deviations:\n", deviations)


# ###6: Apply() over columns, practice

# Since the NumPy std() method returns a single computed value when applied over a Series, in the previous code cell, the apply() method returned a single value for each column. If you instead used a NumPy function that returns a value for each element in a list (instead of just a single computed value), you can transform all of the values in each column and return a DataFrame with the new values instead. The following code will double all of the values in the float columns:
# 
#     float_df.apply(lambda x: x*2)
# 
# This will return a new DataFrame, with each of the values in the float columns doubled, instead of modifying the object inplace.

# ####Instructions

# Transform float_df using the apply() method to halve each value and assign to halved_df. Then print the first row.

# In[8]:

double_df = float_df.apply(lambda x: x*2)
double_df.head(1)


# In[9]:

halved_df = float_df.apply(lambda x: x/2)
halved_df.head(1)


# ###7: Apply() over rows

# So far we've used the default behavior of the apply() method, which operates over the columns in a DataFrame. To apply a function the rows (each row will be treated as a Series object) in a DataFrame, we need to set the axis parameter to 1 after we specify the function we want applied. Applying over the rows allows us to, for example, calculate the standard deviation of multiple column values for each movie:
# 
# - rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
# - rt_mt_user.apply(lambda x: np.std(x), axis=1)
# 
# This code filters the DataFrame to the two we want and then returns a Series object (since std() returns a value for each iteration) containing the standard deviation of each movie's values for RT_user_norm and Metacritic_user_norm.

# ####Instructions

# Use the apply() method to calculate the average of each movie's values for RT_user_norm and Metacritic_user_norm and assign to the variable rt_mt_means. Then print the first 5 values.

# In[10]:

rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_means = rt_mt_user.apply(lambda x: np.mean(x), axis=1)
print("rt_mt_means[0:5]:\n", rt_mt_means[0:5])

