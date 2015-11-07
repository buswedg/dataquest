
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Data Analysis with Pandas

# ##Summarizing Data

# ###1: College majors and employment

# The American Community Survey is a survey run by the US Census Bureau that collects data on everything from the affordability of housing to employment rates for different industries. For this challenge, you'll be using the data derived from the American Community Survey for years 2010-2012.
# 
# Here's a quick overview of the files we'll be working with:
# 
# - all-ages.csv - employment data by major for all ages
# - recent-grads.csv - employment data by major for just recent college graduates

# In[2]:

import pandas as pd

all_ages = pd.read_csv("data/all-ages.csv")
all_ages.head(5)


# In[3]:

recent_grads = pd.read_csv("data/recent-grads.csv")
recent_grads.head(5)


# ###2: Summarizing major categories

# In both of these datasets, majors are grouped into categories. As you may have noticed, there are multiple rows with a common value for Major_category but different values for Major. We would like to know the total number of people in each Major_category for both datasets.

# ####Instructions

# Use the Total column to calculate the number of people who fall under each Major_category and store the result as a separate dictionary for each dataset. The key for the dictionary should be the Major_category and the value should be the total count. For the counts fromall_ages, store the results as a dictionary named all_ages_major_categories and for the counts from recent_grads, store the results as a dictionary named recent_grads_major_categories.
# 
# Format of dictionary:
# 
#     { 
#         "Engineering": 500,
#         "Business": 500
#         ...
#     }

# In[4]:

# All values for "Major_category"
all_ages_index = all_ages["Major_category"].value_counts().index
print("all_ages_index:\n", all_ages_index)

recent_grad_index = recent_grads['Major_category'].value_counts().index
print("recent_grad_index:\n", recent_grad_index)

all_ages_major_categories = dict()
recent_grads_major_categories = dict()
def calculate_major_cat_totals(df):
    cats = df["Major_category"].value_counts().index
    counts_dictionary = dict()

    for c in cats:
        major_df = df[df["Major_category"] == c]
        total = major_df["Total"].sum(axis=0)
        counts_dictionary[c] = total
    return counts_dictionary

all_ages_major_categories = calculate_major_cat_totals(all_ages)
recent_grads_major_categories = calculate_major_cat_totals(recent_grads)


# ###3: Low wage jobs rates

# The press likes to talk a lot about how many college grads are unable to get higher wage, skilled jobs and end up working lower wage, unskilled jobs instead. As a data person, it is your job to be skeptical of any broad claims and explore if you can acquire and analyze relevant data to obtain a more nuanced view. Let's run some basic calculations to explore that idea further.

# ####Instructions

# Use the "Low_wage_jobs" and "Total" columns to calculate the proportion of recent college graduates that worked low wage jobs. Store the resulting float object of the calculation as 'low_wage_percent'.

# In[5]:

low_wage_percent = 0.0

low_wage_percent = float(recent_grads['Low_wage_jobs'].sum(axis=0)) / (recent_grads['Total'].sum(axis=0))
print("low_wage_percent:", low_wage_percent)


# ###4: Comparing datasets

# Both all_ages and recent_grads datasets have 173 rows, corresponding to the 173 college major codes. This enables us to do some comparisons between the two datasets and perform some initial calculations to see how similar or different the statistics of recent college graduates are from those of the entire population.

# ####Instructions

# We want to know the number of majors where recent grads fare better than the overall population.
# 
# For each major:
# 
# - increment recent_grads_lower_emp_count if Unemployment_rate is lower for recent_grads
# - increment all_ages_lower_emp_count if Unemployment_rate is lowwer for all_ages
# - do nothing if Unemployment_rate is the same for both

# In[6]:

# All majors, common to both DataFrames
majors = recent_grads['Major'].value_counts().index

recent_grads_lower_emp_count = 0
all_ages_lower_emp_count = 0
for m in majors:
    recent_grads_row = recent_grads[recent_grads['Major'] == m]
    all_ages_row = all_ages[all_ages['Major'] == m]
    
    recent_grads_unemp_rate = recent_grads_row['Unemployment_rate'].values[0]
    all_ages_unemp_rate = all_ages_row['Unemployment_rate'].values[0]
    
    if recent_grads_unemp_rate < all_ages_unemp_rate:
        recent_grads_lower_emp_count += 1
    elif all_ages_unemp_rate < recent_grads_unemp_rate:
        all_ages_lower_emp_count += 1
        
print("recent_grads_lower_emp_count:", recent_grads_lower_emp_count)
print("all_ages_lower_emp_count:", all_ages_lower_emp_count)

