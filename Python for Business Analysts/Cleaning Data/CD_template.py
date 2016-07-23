
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Python for Business Analysts

# ##Cleaning Data

# ###1: Introduction

# Art is a messy business. Over centuries, artists have created everything from simple paintings to complex sculptures, and art historians have been cataloging everything they can along the way. The Museum of Modern Art, or MoMA for short, is considered one of the most influential museums in the world and recently released a dataset of all the artworks they’ve cataloged in their collection. This dataset contains basic information on metadata for each artwork and is part of MoMA's push to make art more accessible to everyone.
# 
# The museum has put out a disclaimer however that the dataset is still a work in progress - an evolving artwork in its own right perhaps. Because it's still in progress, the dataset has data quality issues and needs some cleanup before we can analyze it.

# ###2: Show me the Data!

# For this post, we'll be working with just the first 100 rows of the dataset. We will first need to import the Pandas library into our environment and then read in the dataset into a DataFrame called artworks. Then, let's preview the first 5 rows using artworks.head(5).

# In[2]:

import pandas

artworks = pandas.read_csv("data/Artworks.csv")
artworks.head(5)


# ###3: Dating Artists

# As you can see, the dataset comes with details on every artwork ranging from the author, his / her's short bio, the artwork's dimensions, date acquired, and even the URL to the artwork's page. While some columns, like DateAcquired, are formatted in the right way for us to plot as a time series, other columns like Date contain a mix of values that make it hard to explore. We ideally want this column to just have the year the artwork was published so that we can plot them.
# 
# Let's use a Pandas feature called value_counts(), which returns a list of all the values in that column in addition to their frequency of appearance, similar to a histogram. We want to make sure we have a good sense of all the different formats the values in the Date column take on.

# In[3]:

# Returns list of all values in 'Date' column, and their frequency
artworks['Date'].value_counts()


# ###4: Patterns

# Looks like there are a few patterns in the Date column that we need to account for:
# - Pattern 1: "1976-77" (year ranges)
# - Pattern 2: "c. 1917"
# - Pattern 3: "Unknown"
# - Pattern 4: "n.d."
# 
# Now we need to come up Python logic to specify how we want these values to be handled.
# 
# For the first one, let's go ahead and just pick the lower of the 2 years provided in the range (e.g. "1976-77" becomes "1976"). For the second pattern, let's just get rid of the "c. " in front of "c. 1917". Finally, let's leave the third pattern alone, "Unknown", and actually convert the values where we see the fourth pattern, "n.d.", into the same value as the third pattern, "Unknown". This way, when we are calculating or plotting using the Date column, we can just filter out all of the artworks that have "Unknown" as their value and proceed without any issues.
# 
# Let's step through how we can write a function for dealing with each pattern and transforming the values based on the rules we described above.

# ###5: Pattern 1

# Since all of the rows with pattern 1 are year ranges spanning only two years (e.g. 1980-81), we can select a year and have it replace the range. To keep things simple, let's select the first year in the range since it contains all four digits of the year (1980) while the second year in the range has only the last two digits (81).
# 
# We also need a reliable way to identify which rows actually exhibit pattern 1 so we only update those rows and leave the others intact. We need to leave the others intact either because they are already in the proper date format or because they will need to be modified later using the logic we write for handling the other patterns.
# 
# Since year ranges contain a hyphen - separating the two years, we can look for the - in each row's Date value and split it into two separate years. The core Python library contains a function named .split() which in this situation will return a list of the two years if a hyphen is found or the original value if it isn't. Since we are looking for just the first year, we can call .split("-") on every row's Date, check to see if the resulting list contains two elements, and if it does, return the first element. Let's write a function clean_split_dates(row) which will do exactly that:

# In[4]:

def clean_split_dates(row):
    # Return current value for the 'Date' column for that row.
    initial_date = str(row['Date'])
    final_date = initial_date
    
    # Split string by the dash and create a list with the values surrounding the dash, called `split_date`.
    split_date = initial_date.split('-') 

    # If no dash found, 'split_date' will just contain one item, the initial_date.
    # If dash is found, 'split_date' will contain a list of at least 2 elements, return first element.
    if len(split_date) > 1:
        final_date = split_date[0]
    
    return final_date

# Assign the results of 'clean_split_dates' to the 'Date' column. Since we want Pandas to go
# row by row, we set "axis=1". If we wanted to go by columns, we would use "axis=0".
artworks['Date'] = artworks.apply(lambda row: clean_split_dates(row), axis=1)
artworks['Date'].value_counts()


# ###6: Pattern 2

# As you can see, there are no values in Date that are year ranges and contain a "-" separator. Let's now write a function to handle Pattern 2, called clean_c_dates.
# 
# This function needs to look for the characters, "c. ", at the beginning of each date and chop that sequence off if it finds it. Let's take advantage of another function that Strings have, called lstrip(chars). The lstrip(chars) function starts from the left side of the String and compares each letter of the String with the chars we passed in. If it finds the full chars phrase, it will remove it from the String. If it doesn't, it keeps it the same!

# ####Instructions

# While the logic for clean_c_dates is written out, we are going to ask you to apply the function to the artworks DataFrame and assign the results to the Date column.

# In[5]:

def clean_c_dates(row):
    # Return current value for the 'Date' column for that row.
    initial_date = row['Date']
    # Use .lstrip() to strip from the left side of "c. ".
    final_date = initial_date.lstrip("c. ")
    return final_date

# Assign the results of 'clean_c_dates' to the 'Date' column. Since we want Pandas to go
# row by row, we set "axis=1". If we wanted to go by columns, we would use "axis=0".
artworks['Date'] = artworks.apply(lambda row: clean_c_dates(row), axis=1)


# ###7: Verifying Pattern 2

# Let's run value_counts() on the Date column to verify that our logic worked as we expected. Look to make sure the row with Pattern 2 no longer exhibits that pattern.

# In[6]:

artworks['Date'].value_counts()


# ###8: Pattern 3

# The row with "c. 1917" is now just "1917", as expected! We don't have to write any specific code to handle Pattern 3 since we want those values to remain the same as the original. In the functions we use to clean the other 3 patterns, if a match wasn't found, the original Date value was returned. Since "Unknown" doesn't overlap in logic with our other patterns, all rows that had the initial value "Unknown" remained the same!

# ###9: Pattern 4

# For pattern 4, we just need to check if initial_date is equal to n.d., and modify that row's Date value to Unknown if it is. Let's call this function clean_nd_dates then run .value_counts() on the updated Date column as before.

# In[7]:

def clean_nd_dates(row):
    # Return current value for the 'Date' column for that row.
    initial_date = row['Date']
    final_date = initial_date
    
    # If equal to "n.d.", replace with "Unknown".
    if initial_date == "n.d.":
        final_date = "Unknown"

    return final_date

# Assign the results of 'clean_nd_dates' to the 'Date' column. Since we want Pandas to go
# row by row, we set "axis=1". If we wanted to go by columns, we would use "axis=0".
artworks['Date'] = artworks.apply(lambda row: clean_nd_dates(row), axis=1)
artworks['Date'].value_counts()


# ###10: Packaging Logic Into One Function

# We now only have specific year values or the value "Unknown" in our Date column. For the purposes of this lesson, we split up the pattern transformations into 3 different functions: clean_split_dates, clean_c_dates, and clean_nd_dates. As you become more familiar with Python and Pandas, you will become more comfortable reducing complexity by writing just one function to handle the patterns. Let's now see what that function could look like, by borrowing from the logic of the 3 functions we wrote above.

# In[8]:

# Single transformation function.
def clean_dates(row):
    initial_date = str(row['Date'])
    final_date = initial_date

    # Pattern 1
    split_date = initial_date.split("-")
    
    if len(split_date) > 1:
        final_date = split_date[0]
        return final_date
    
    # Pattern 4
    elif initial_date == "n.d.":
        final_date = "Unknown"
        return final_date
    
    # Pattern 2
    else:
        final_date = initial_date.lstrip("c. ")
    return final_date

# Assign the results of 'clean_dates' to the 'Date' column. Since we want Pandas to go
# row by row, we set "axis=1". If we wanted to go by columns, we would use "axis=0".
artworks = pandas.read_csv("data/Artworks.csv")
artworks['Date'] = artworks.apply(lambda row: clean_dates(row), axis=1)
artworks['Date'].value_counts()


# ###11: Challenge, Introduction

# We've left this next problem up to you as a challenge. If you run .value_counts() on the the ArtistBio column, you'll notice that every value is surrounded by parentheses.

# In[9]:

artworks['ArtistBio'].value_counts()[:10]


# ##12: Challenge, Go!

# ####Instructions

# Write a function clean_parentheses(row) that removes the trailing parentheses from both sides. Just like we used .lstrip() on each value to remove "c. " from values in the Date column, use the function .rstrip() to remove trailing characters from the right side.

# In[10]:

def clean_parentheses(row):
    initial_bio = str(row['ArtistBio'])
    left_stripped = initial_bio.lstrip("(")
    final_stripped = left_stripped.rstrip(")")
    final_bio = final_stripped
    return final_bio

artworks['ArtistBio'] = artworks.apply(lambda row: clean_parentheses(row), axis=1)
artworks['ArtistBio'].value_counts()[:10]


# ##13: Conclusion

# The ArtistBio column is now much cleaner without the starting and ending parentheses. You may have noticed that some of the values have parentheses in the middle of the String, instead of just at the edges. Usually in these kinds of situations, you go from exploring the values, coming up with patterns, writing code to deal with them, and then revising and repeating until the data is ready to go. Because our code persists even after we run it, it's easy to iterate through ideas.
