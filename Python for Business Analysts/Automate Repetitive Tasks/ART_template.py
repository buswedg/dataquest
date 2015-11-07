
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Python for Business Analysts

# ##Automate Repetitive Tasks

# ###1: Introduction

# In this mission, we will explore how we can use Python to automate tasks for us.

# ####Instructions

# Create 2 variables, housing_2007 and housing_2005, that contain the DataFrame objects associated with Hud_2007.csv and Hud_2005.csv, respectively.

# In[2]:

import pandas

housing_2007 = pandas.read_csv("data/Hud_2007.csv")
print("housing_2007:\n", housing_2007.head(3))

housing_2005 = pandas.read_csv("data/Hud_2005.csv")
print("housing_2005:\n", housing_2005.head(3))


# ###2: Lists

# Now that we have read in both datasets into DataFrame objects, let's add them to a List. A List is type of object (just like a DataFrame, Integer, or String) that contains an ordered group of objects. Just like how a grocery list contains a group of "ingredient" objects to buy, is a List object in Python houses a group of the objects we add to it. Instead of writing code to manipulate each object separately (in our case the objects are DataFrames), we can group a few objects into a List object, write the logic once, and apply it to every object in that List. This saves us a lot of time and energy, and will be important when we deal with much larger datasets with tens, hundreds or even thousands of DataFrames.
# 
# In the following code block, we will create an empty List called data_frames_list by assigning it empty brackets: []
# 
# Then, we will add a year column for each DataFrame to keep track of which DataFrame is which:
# 
#     housing_2005['year'] = '2005'
#     housing_2007['year'] = '2007'
# 
# Each row now has a value for year, either 2005 or 2007, identifying which dataset that row originated from. Finally, we will use .append() to first add housing_2005 then housing_2007 to the end of data_frames_list. The List object preserves the order by which the DataFrames were added:
# 
#     data_frames_list.append(housing_2005)
#     data_frames_list.append(housing_2007)
# 
# The list now contains these two DataFrames in the order we added them.

# In[3]:

# Create list.
data_frames_list = []

# Add a year column to each dataframe.
housing_2005['year'] = '2005'
housing_2007['year'] = '2007'

# .append() adds the specified object to the end of the list.
data_frames_list.append(housing_2005)
data_frames_list.append(housing_2007)

# List now contains 2 objects, the respective dataframes for 2005 and 2007.
print("data_frames_list:", len(data_frames_list))


# ###3: Column Filtering

# After appending both DataFrames, we ran print() on len(data_frames_list) to display the number of elements, or length, of the list to verify that we added two DataFrame objects to the list.
# 
# Let's now practice Pandas' column filtering feature that we learned in the previous lesson. Create a new DataFrame, filtered_housing_2007, that contains the column filtered version of housing_2007, with just the columns we are interested in. The columns we want are: ['AGE1', 'FMR', 'TOTSAL', 'year'].

# ####Instructions

# First, create a List variable, columns, that contains the names of all of the columns we are interested in. When specifying the elements we want in the list, we need to surround each column name we want with quotes (either single or double quotes), add a comma between each column name, and then surround the whole thing with a starting [ and closing bracket ]. Then, we use bracket notation on the DataFrame object to specify a filter. We want the filter to just contain the columns list.

# In[4]:

columns = []
filtered_housing_2007 = []

# Create list of column names to filter by.
columns = ['AGE1', 'FMR', 'TOTSAL', 'year']

# Filter dataframe.
filtered_housing_2007 = housing_2007[columns]

print("filtered_housing_2007:\n", filtered_housing_2007[:5])


# ###4: Functions

# Now, we will learn how to write our own functions. Functions are core to every programming language and are a powerful way to package logic and apply it wherever we see fit. They can take an object as an input, apply pre-written logic on the input, and then return a modified object. Functions are like factories that take in raw materials, add other materials and processes to them, and then crank out finished products. In the next code block, we define a function filter_columns, that takes in an input, data_frames_list, and returns a new list new_df_list.
# 
# We want the function to filter each DataFrame down to only the columns we want. Let's use the same columns from the last code block: * 'AGE1', 'FMR', 'TOTSAL', year

# In[5]:

def filter_columns(data_frames_list):
    # Create list.
    new_df_list = list()
    
    # Look through each dataframe.
    for df in data_frames_list:
        # Create list of column names to filter by.
        columns = ['AGE1', 'FMR', 'TOTSAL', 'year']
        # Filter dataframe.
        filtered_df = df[columns]
        # Append filtered dataframe to 'new_df_list'.
        new_df_list.append(filtered_df)

    return new_df_list

filtered_data_frames_list = filter_columns(data_frames_list)


# ###5: Explanation

# Let's walk through what we wrote, step by step.
# 
# In the function above, we used a for loop:
# 
# for df in data_frames_list:
# 
# to iterate over all of the object in data_frames_list (which contained our twp DataFrames we added earlier) and applied our column filtering logic. We iterated over a list object by object, referring to the current object we were applying the logic to as df.
# 
# Instead of hard coding the columns we want at the filter level like we did in the last lesson:
# 
#     filtered_housing_2013 = housing_2013[[ 'AGE1', 'FMR',  'TOTSAL', 'year' ]]
# 
# we assigned the column names to a list object, called columns:
# 
#     columns = ['AGE1', 'FMR', 'TOTSAL', 'year']
# 
# and passed it into the filter criteria:
# 
#     filtered_df = df[columns]
# 
# Instead of creating two different DataFrame objects (like filtered_housing_2005, filtered_housing_2007, etc), we created an empty list called new_df_list:
# 
#     new_df_list = list()
# 
# and appended each of the filtered_df objects to it:
# 
#     new_df_list.append(filtered_df)
# 
# As you can see, we placed a heavy emphasis on abstracting, or generalizing, our logic so we can detail the logic once, and apply it in many cases. The filter_columns function that we wrote is essentially a piece of software that will filter any list of DataFrame objects into the 4 columns we want. Whether the list of DataFrame objects has 1 DataFrame object or 25, the same function can be applied to get the result we want. Another abstraction we could implement would be to modify the function and specify the columns we want filtered every time by adding it as an input to the function (alongside data_frames_list). This way, instead of always using a specific set of columns within the function, the user can now specify in the input which columns they prefer to filter their DataFrames.
# 
# This is the power of abstraction. It allows us to automate repetitive work incredibly easily.

# ###6: Column Filtering Verification

# Let's quickly verify that each of the DataFrame objects in filtered_data_frames_list only contains the 4 columns we specified in columns. Here we will write a print() statement within a for loop to print all of the columns in each DataFrame housed in filtered_data_frames_list.

# In[6]:

# For every dataframe in the list 'filtered_data_frames_list'.
for df in filtered_data_frames_list:
    # Print dataframe columns.
    print("df.columns:", df.columns)


# ###7: Summary

# As you can see, our column filter was applied to every DataFrame in the list, filtered_data_frames_list, and each DataFrame now contains only the 4 columns we are interested in.

# ###8: Multiple Dataset Analysis

# Now let's write a function that counts the number of rows in each DataFrame that have negative values for the AGE1 column. We will also use Python's ability to custom print values.
# 
# In the following code block:
# 
#     print( str(year) + " - " + str(len( negative_age_count ) ) + " rows")
# 
# we use the function str() to convert Integer objects, like year and len(negative_age_count), into String objects. The print function can only print String objects, so we must convert other objects to String objects. While not all objects can be converted to String objects for displaying, most can and we will cover in a later lesson how we can tell.

# In[7]:

# For every dataframe in the list 'filtered_data_frames_list'.
for df in filtered_data_frames_list:
    # Get the dataframe year.
    year = df['year'][0]
    # Return rows with negative age values.
    negative_age_count = df[df['AGE1']<0]
    # Print row count.
    print(str(year) + " - " + str(len( negative_age_count ) ) + " rows")


# ###9: Explanation

# As we loop through filtered_data_frames_list, we print that DataFrame's year, add (using +) a "-", add the len(negative_age_count) , and then finally add the text "rows".
# 
# Looks like both 2005 and 2007 have several thousand rows with negative ages. Its our job to clean this up now.

# ###10: Multiple Dataset Cleanup

# If you recall from the previous mission, the 2013 dataset had 4438 rows with negative ages. The 2005 and 2007 datasets are not as bad, but now we have to clean up two years’ data at the same time. Let's write a function that automates the clean up we did in the last mission so that we are left only with the rows that contain positive values for the AGE1 column.
# 
# Now let's write a function clean_rows() that takes a List of DataFrames and returns a List of cleaned DataFrames with just rows containing positive AGE1 values.
# 
# Inside the function, we will first instantiate, or create, an empty list with no elements:
# 
#     cleaned_list = list()
# 
# Then, we will iterate through each DataFrame in filtered_data_frames_list, create a temporary DataFrame cleaned_df containing just the positive AGE1 rows for each DataFrame:
# 
#     cleaned_df = df[ df ['AGE1'] > 0 ]
# 
# And then we will append cleaned_df to cleaned_list for each iteration:
# 
#     cleaned_list.append(cleaned_df)
# 
# Let's run this function clean_rows on data_frames_list and assign the results to cleaned_data_frames_list.

# In[8]:

def clean_rows(filtered_data_frames_list):
    # Create list.
    cleaned_list = list()
    
    # For every dataframe in the list 'filtered_data_frames_list'.
    for df in filtered_data_frames_list:
        # Return rows with positive age values.
        cleaned_df = df[df['AGE1']>0] 
        # Append filtered dataframe to 'cleaned_list'.
        cleaned_list.append(cleaned_df)
    return cleaned_list

cleaned_data_frames_list = clean_rows(filtered_data_frames_list)

print("cleaned_data_frames_list[0]:\n", cleaned_data_frames_list[0][:5])
print("cleaned_data_frames_list[1]:\n", cleaned_data_frames_list[1][:5])


# ###11: Verify Cleanup

# Let's write a quick function to verify that cleaned_data_frames_list doesn't contain any DataFrame objects that have negative values for the AGE1 column.

# ####Instructions

# Run the function verify_cleanup on cleaned_data_frames_list and assign the result to a new variable, verification_count.

# In[9]:

def verify_cleanup(data_frames_list):
    # Create count.
    negative_rows_count = 0
    
    # For every dataframe in the list 'data_frames_list'.
    for df in data_frames_list:
        # Add the number of negative rows to 'negative_rows_count'.
        negative_rows_count += len(df[df['AGE1']<0])
    return negative_rows_count

verification_count = -1
verification_count = verify_cleanup(cleaned_data_frames_list)

print("verification_count:", verification_count)


# ###12: Summary

# There are zero 0 rows in all of the DataFrame objects in data_frames_list with negative values for the AGE1 column. Just like with the filter_columns function that we wrote before, clean_rows can now be applied to any future HUD datasets that we want without having to rewrite all of the logic we just wrote.

# ###13: Conclusion

# In this mission, you learned the power of automation by using lists, functions, filters and for loops. The process of writing code once that you can then apply in many situations is an underlying concept and principle in programming called Don’t Repeat Yourself, or DRY. By writing abstracted, or generalized, code that is versatile, you not only save yourself precious time, but ensure that your programs run efficiently and without bugs.
