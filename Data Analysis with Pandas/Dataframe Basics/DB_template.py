
# coding: utf-8

# #Data Analysis with Pandas

# ##Dataframe Basics

# ###1: Read in a CSV file

# The first step, as always, is reading in a csv file.
# 
# With pandas, we'll need to use the read_csv method.
# 
# With pandas, the equivalent of a two-dimensional numpy array, or matrix, is called a dataframe.

# ####Instructions

# Read "food_info.csv" info food_info.

# In[1]:

import pandas

food_info = pandas.read_csv("data/food_info.csv")


# ###2: Indexing data with pandas

# Indexing in pandas is slightly different from in numpy.
# 
# We need to use the .iloc[] method (note how it uses square brackets instead of parentheses).
# 
# - numpy_array[0,0]
# - numpy_array[:,0]
# - numpy_array[0,:]
# 
# The above lines of code will get the first element of the first row, the whole first column, and the whole first row from a numpy array, respectively.
# 
# - pandas_dataframe.iloc[0,0]
# - pandas_dataframe.iloc[:,0]
# - pandas_dataframe.iloc[0,:]  
# 
# The above is the equivalent indexing in a pandas dataframe.

# ####Instructions

# Assign the second row of food_info to the variable second_row.
# 
# Assign the tenth row of food_info to the variable tenth_row.

# In[4]:

# Print first row of data.
print "First row of data:"
print food_info.iloc[0,:]

# Assign second row.
second_row = food_info.iloc[1,:]

# Assign tenth row.
tenth_row = food_info.iloc[9,:]


# ###3: Index a series

# What we call a vector or a one-dimensional array is called a series in pandas.
# 
# We index a series without using .iloc[].

# ####Instructions

# Assign the first 20 items in the second row to first_20_items_in_second_row.
# 
# Assign the first 10 items in the first column to first_10_items_in_first_column.

# In[3]:

# Assin a series.
first_row = food_info.iloc[0,:]

# Assign first 10 items from first row.
first_ten_items_in_first_row = first_row[0:10]
first_ten_items_in_first_row = food_info.iloc[0,:][0:10]

# Assign first 20 items from second row.
first_20_items_in_second_row = food_info.iloc[1,:][0:20]

# Assign first 10 items from first column.
first_10_items_in_first_column = food_info.iloc[:,0][0:10]


# ###4: Get column by name

# One cool thing about pandas is that we can get columns with their names, instead of only by number.

# ####Instructions

# Assign the FA_Sat_(g) column to the variable saturated_fat.
# 
# Assign the Cholestrl_(mg) to the variable cholesterol.

# In[5]:

# Print names of all the columns (in order).
print list(food_info.columns.values)

# Print a particular column.
print food_info["Protein_(g)"][0:10]

# Assign particular columns.
sodium_column = food_info["Sodium_(mg)"]
saturated_fat = food_info["FA_Sat_(g)"]
cholesterol = food_info["Cholestrl_(mg)"]


# ###5: Getting multiple columns by name

# We can get a single column by passing in a name, but we can also get multiple columns by passing in a list of names.

# ####Instructions

# Assign the 'Zinc_(mg)' and 'Copper_(mg)' columns to zinc_and_copper.
# 
# Assign the 'Selenium_(mcg)' and 'Thiamin_(mg)' columns to selenium_and_thiamin.
# 
# Make sure that you get the columns in order (zinc and selenium come first).

# In[6]:

#print list food_info.columns.values

# Rename copper and selenium columns.
food_info = food_info.rename(columns={'Copper_mg)': 'Copper_(mg)'})
food_info = food_info.rename(columns={'Selenium_(\xb5g)': 'Selenium_(mcg)'})

# Assign fiber and suger columns.
column_list = ['Fiber_TD_(g)', 'Sugar_Tot_(g)']
fiber_and_sugar = food_info[column_list]

# Assign zinc and copper columns.
zinc_and_copper = food_info[['Zinc_(mg)', 'Copper_(mg)']]

# Assign selenium and thiamin columns.
selenium_and_thiamin = food_info[['Selenium_(mcg)', 'Thiamin_(mg)']]


# ###6: Math with columns

# We can do math with vectors (or, as we are more familiar with them as, columns).
# 
# Adding two columns will go through and add each value at each position to the corresponding value in the same position.
# 
# First, the values at index 0 will be added, then the values at index 1, and so on.
# 
# At the end, you'll have a new vector with all of the sums.
# 
# In order to do this kind of math, the vectors all need to be the same length (have the same number of elements).

# ####Instructions

# Assign the number of grams of protein per gram of water ("Protein_(g)" column divided by "Water_(g)" column) to grams_of_protein_per_gram_of_water.
# 
# Assign the total amount of calcium and iron("Calcium_(mg)" column plus "Iron_(mg)" column) to milligrams_of_calcium_and_iron.

# In[7]:

# Sum fat columns.
total_fat = food_info["FA_Sat_(g)"] + food_info["FA_Mono_(g)"] + food_info["FA_Poly_(g)"]

# Protein per calorie.
grams_of_protein_per_calorie = food_info["Protein_(g)"] / food_info["Energ_Kcal"]

# Protein squared.
grams_of_protein_squared = food_info["Protein_(g)"] * food_info["Protein_(g)"]

# Non-sugar carbohydrates.
non_sugar_carbs = food_info["Carbohydrt_(g)"] - food_info["Sugar_Tot_(g)"]

# Protein per water.
grams_of_protein_per_gram_of_water = food_info["Protein_(g)"] / food_info["Water_(g)"]

# Sum calcium and iron.
milligrams_of_calcium_and_iron = food_info["Calcium_(mg)"] + food_info["Iron_(mg)"]


# ###7: Math with scalars

# We can also do math with a vector (column) and a scalar (single numbers).
# 
# food_info["Iron_(mg)"] / 1000  
# 
# The statement above will divide each item in the "Iron_(mg)" column by 1000, converting the values from milligrams to grams.
# 
# Multiplying by scalars can be a good way to manipulate values in columns.

# ####Instructions

# Assign the number of grams of "Sodium_(mg)" to the variable sodium_grams (divide the column by 1000).
# 
# Assign the number of milligrams of "Sugar_Tot_(g)" to the variable sugar_milligrams (multiply the column by 1000).

# In[8]:

# Divide the protein column by a scalar to get kilograms.
protein_kilograms = food_info["Protein_(g)"] / 1000

# Subtract 5 grams from carbohydrates.
lowered_carbs = food_info["Carbohydrt_(g)"] - 5

# Assign the number of grams of "Sodium_(mg)" to the variable sodium_grams.
sodium_grams = food_info["Sodium_(mg)"] / 1000

# Assign the number of milligrams of "Sugar_Tot_(g)" to the variable sugar_milligrams.
sugar_milligrams = food_info["Sugar_Tot_(g)"] * 1000


# ###8: Sorting columns

# We can also sort the dataframe by the values in a column.
# 
# To do this, we use the .sort method, which returns a new dataframe sorted according to the specified criteria.

# ####Instructions

# Sort by the amount of "Sodium_(mg)", with the largest value on top (descending sort). Assign the result to descending_sodium.
# 
# Sort by the amount of "Vit_C_(mg)", with the smallest value on top (ascending sort). Assign the result to ascending_vitamin_c.

# In[9]:

# Sort foods by amount of fat.
descending_fat = food_info.sort(["Lipid_Tot_(g)"], ascending=[False])

# Print the most fatty food in the data.
#print(descending_fat.iloc[0,:])

# Reverse the sort order.
ascending_fat = food_info.sort(["Lipid_Tot_(g)"], ascending=[True])

# The least fatty food has no fat at all.
#print(ascending_fat.iloc[0,:])

# Sort by the amount of sodium.
descending_sodium = food_info.sort(["Sodium_(mg)"], ascending=[False])

# Sort by the amount of vitamin C.
ascending_vitamin_c = food_info.sort(["Vit_C_(mg)"], ascending=[True])

print "Food with least vitamin C:"
print(ascending_vitamin_c.iloc[0,:])


# ###9: Multicolumn sort

# We only sorted on the value of a single column before, but we can also sort based on multiple columns.
# 
# The first column in the list will be sorted on first. Any rows that have the same value for the first column will be sorted based on the second column, and so on until all of the given columns are used.
# 
# We can specify different sort orders for each column using the ascending argument.

# ####Instructions

# Perform a multicolumn sort on food_info, with the first column being "Sugar_Tot_(g)" ascending, and the second being "Zinc_(mg)" descending. Assign the result to ascending_sugar_then_descending_zinc.
# 
# Perform a multicolumn sort on food_info, with the first column being "Cholestrl_(mg)" descending, and the second being "Protein_(g)" ascending. Assign the result to descending_cholesterol_then_ascending_protein.

# In[10]:

# Perform a multicolumn sort, with first column "Lipid_Tot_(g)" ascending, and the second "Sodium_(mg)" ascending
ascending_fat_then_ascending_sodium = food_info.sort(["Lipid_Tot_(g)", "Sodium_(mg)"], ascending=[True, True])

# Print the multicolumn sort
#print ascending_fat_then_ascending_sodium.iloc[0,:]

# Perform a multicolumn sort, with first column "Lipid_Tot_(g)" ascending, and the second "Sodium_(mg)" descending
ascending_fat_then_descending_sodium = food_info.sort(["Lipid_Tot_(g)", "Sodium_(mg)"], ascending=[True, False])

# Print the multicolumn sort
#print(ascending_fat_then_descending_sodium.iloc[0,:])

# Perform a multicolumn sort, with first column "Sugar_Tot_(g)" ascending, and the second "Zinc_(mg)" descending
ascending_sugar_then_descending_zinc = food_info.sort(["Sugar_Tot_(g)", "Zinc_(mg)"], ascending=[True, False])

# Perform a multicolumn sort, with first column "Cholestrl_(mg)" descending, and the second "Protein_(g)" ascending
descending_cholesterol_then_ascending_protein = food_info.sort(["Cholestrl_(mg)", "Protein_(g)"], ascending=[False, True])

print "Food with greatest cholesterol and least protein:"
print descending_cholesterol_then_ascending_protein.iloc[0,:]


# ###10: Creating a rating

# Let's say that we have a friend, Superman, who's trying to gain muscle, and so he wants to eat foods that have a lot of protein.
# 
# But he's also very health conscious, so he wants to avoid fat.
# 
# We could sort based on those two columns and give him an answer, but what if he cares more about a food having a lot of protein than it being too fatty?
# 
# What we need to do is construct a rating for each food based on Superman's criteria.
# 
# Then we can recommend the food that scores the highest.

# ####Instructions

# Let's say Superman now decides that the food having a lot of protein is only twice as important as the food not being too fatty.
# 
# Construct the new rating, and assign it to new_rating

# In[11]:

# Calculate the weighted value for protein.
weighted_protein = food_info["Protein_(g)"] * 3

# Calculate the weighted value for fat.
weighted_fat = -1 * food_info["Lipid_Tot_(g)"]

# Construct the final rating by adding the weighted values.
initial_rating = weighted_protein + weighted_fat
new_rating = (food_info["Protein_(g)"] * 2) - food_info["Lipid_Tot_(g)"]
food_info["new_rating"] = new_rating

# Sort by the new rating.
descending_new_rating = food_info.sort(["new_rating"], ascending=[False])

print "Food with greatest new weighting:"
print descending_new_rating.iloc[0,:]


# ###11: Normalizing columns

# One of the simplest ways to normalize a column is to divide all of the values by the maximum value in the column.
# 
# It will change all of the values to be between 0 and 1.
# 
# It doesn't work so well with negative values, but we don't have any (you can't have negative amounts of protein, fat, etc).
# 
# This isn't necessarily the best way to normalize, and we'll learn some better methods soon.

# ####Instructions

# Normalize the values in the "Vit_C_(mg)" column, and assign the result to normalized_vitamin_c
# 
# Normalize the values in the "Zinc_(mg)" column, and assign the result to normalized_zinc

# In[12]:

# Use the max() method to find the maximum value in a column.
max_protein = food_info["Protein_(g)"].max()

# Divide the column by the scalar.
normalized_protein = food_info["Protein_(g)"] / max_protein

# Print normalized protein values.
#print(normalized_protein[0:20])

# Create normalized vitamin C value.
normalized_vitamin_c = food_info["Vit_C_(mg)"] / food_info["Vit_C_(mg)"].max()
food_info["normalized_vitamin_c"] = normalized_vitamin_c

# Sort by normalized vitamin C values.
descending_normalized_vitamin_c = food_info.sort(["normalized_vitamin_c"], ascending=[False])
print "Food with greatest normalized vitamin C:"
print descending_normalized_vitamin_c.iloc[0,:]

# Create normalized zinc value.
normalized_zinc = food_info["Zinc_(mg)"] / food_info["Zinc_(mg)"].max()


# ###12: Making a better rating

# In[ ]:

We now know enough to construct a better rating for our friend Superman.

We just have to normalize the columns that we are interested in before we create the rating.


# ####Instructions

# Superman is twice as interested in a food having a lot of protein than he is in it having too much fat.
# 
# Construct a rating with these new criteria, and assign it to better_protein_rating.
# 
# Make sure to normalize the protein ("Protein_(g)") and fat ("Lipid_Tot_(g)") columns first.

# In[13]:

# Create better protein rating.
better_protein_rating = None

# Create normalized protein values.
normalized_protein = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()

# Create normalized fat values.
normalized_fat = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()

# Create new protein rating.
better_protein_rating = (normalized_protein * 2) - normalized_fat
food_info["better_protein_rating"] = better_protein_rating

# Sort by new protein rating.
descending_better_protein_rating = food_info.sort(["better_protein_rating"], ascending=[False])
print "Food with greatest better protein rating:"
print descending_better_protein_rating.iloc[0,:]


# ###13: Normalizing multiple columns

# Now, let's say we want to construct a total nutrition rating that takes all the columns into account.
# 
# In order to do this, we would have to normalize each of the columns, which is a huge pain.
# 
# An easier way is to use a for loop to normalize each column.
# 
# The "NDB_No" and "Shrt_Desc" columns (first two) can't be normalized, because they aren't nutritional values. The first one is the ID number of the food, and the second is the name.

# ####Instructions

# Remove the "NDB_No" and "Shrt_Desc" columns from all_columns
# 
# Then, use a for loop to normalize all the other columns.

# In[15]:

column_list = ["Energ_Kcal", "Protein_(g)"]

# Loop through column_list, and normalize each of the columns in it.
for column in column_list:
    food_info[column] = food_info[column] / food_info[column].max()

# All columns is a list of all the columns in the food_info dataframe.
all_columns = list(food_info.columns.values)
#print "All columns: ", all_columns

column_count = len(all_columns)
all_columns = all_columns[2:column_count]
print "Removed 'NDB_No' and 'Shrt_Desc': ", all_columns


# ###14: Finding the amount of vitamins

# Now that we normalized all of the columns, we're well on our way to making a nutritional rating.
# 
# In order to get there, let's create a sum of all the vitamin columns.
# 
# Most methods on pandas dataframes can operate on series, or on dataframes.
# 
# Let's take the .sum() method as an example.
# 
# On a series, it gives you the total of all the values in the series.
# 
# When used on a dataframe, it takes the optional axis keyword argument.
# 
# When axis is 0, it gives you a new series with the sums of all of the columns in the dataframe.
# 
# When axis is 1, it gives you a new series with sums of all of the rows in the dataframe.

# ####Instructions

# Sum up the amount of vitamins in each food (using the vitamin_columns list to get columns from the dataframe), and assign the result to vitamin_totals.
# 
# You'll need to sum the total in each row.

# In[16]:

column_list = ['Fiber_TD_(g)', 'Sugar_Tot_(g)']

# Sum the amount of fiber and sugar in each of the foods.
row_total = food_info[column_list].sum(axis=1)
#print row_total

# Sum the total amount of fiber and sugar across all the foods.
column_total = food_info[column_list].sum(axis=0)
#print column_total

# Rename 'Vit_B12_(mcg)', 'Vit_D_mcg', 'Vit_K_(mcg)' columns.
food_info = food_info.rename(columns={'Vit_B12_(\xb5g)': 'Vit_B12_(mcg)'})
food_info = food_info.rename(columns={'Vit_D_\xb5g': 'Vit_D_mcg'})
food_info = food_info.rename(columns={'Vit_K_(\xb5g)': 'Vit_K_(mcg)'})

# Sum the total amount of vitamins in each foods.
vitamin_columns = ['Calcium_(mg)', 'Iron_(mg)', 'Magnesium_(mg)', 'Phosphorus_(mg)', 'Potassium_(mg)', 'Sodium_(mg)', 'Zinc_(mg)', 'Copper_(mg)', 'Manganese_(mg)', 'Selenium_(mcg)', 'Vit_C_(mg)', 'Thiamin_(mg)', 'Riboflavin_(mg)', 'Niacin_(mg)', 'Vit_B6_(mg)', 'Vit_B12_(mcg)', 'Vit_A_IU', 'Vit_A_RAE', 'Vit_E_(mg)', 'Vit_D_mcg', 'Vit_D_IU', 'Vit_K_(mcg)']
vitamins = food_info[vitamin_columns]
vitamin_totals = vitamins.sum(axis=1)
print "Vitamin totals:"
print vitamin_totals.head(10)


# ###15: Adding a new column

# We can add a column to a dataframe by assigning to it.
# 
# food_info["double_fat"] = food_info["Lipid_Tot_(g)"] * 2  
# 
# The above code assigns double the amount of lipids to the "double_fat" column in food_info.

# ####Instructions

# We've read the vitamin_totals variable from the last screen in.
# 
# Assign vitamin_totals to the "vitamin_totals" column in food_info.

# In[17]:

# Assign double protein values.
food_info["double_protein"] = food_info["Protein_(g)"] * 2

# Assign vitamin totals.
food_info["vitamin_totals"] = vitamin_totals


# ###16: Making a nutritional index

# We've normalized the values in vitamin_totals, and assigned it to the "vitamin_totals" column in food_info.
# 
# Let's construct a nutritional rating using the amount of vitamins, fats, protein, sugar, fiber, and cholesterol.

# ####Instructions

# Give the "vitamin_totals" column a weight of 3, the "Lipid_Tot_(g)" column a weight of -2, the "Protein_(g)" column a weight of 3, the "Sugar_Tot_(g)" column a weight of -1, the "Fiber_TD_(g)" a weight of 1, and the "Cholestrl_(mg)" column a weight of -2.
# 
# Construct a rating using the above weights, and assign it to nutritional_rating.

# In[18]:

# Assign nutritional rating.
nutritional_rating = None
nutritional_rating = 3 * food_info["vitamin_totals"] + -2 * food_info["Lipid_Tot_(g)"] + 3 * food_info["Protein_(g)"] + -1 * food_info["Sugar_Tot_(g)"] + 1 * food_info["Fiber_TD_(g)"] + -2 * food_info["Cholestrl_(mg)"]
food_info["nutritional_rating"] = nutritional_rating

print "Nutritional rating:"
print nutritional_rating.head(10)


# ###17: Finding the most nutritious foods

# We've read the nutritional rating series from the last screen to the "nutritional_rating" column in food_info.
# 
# Now, lets see if we can use it to find the most nutritious foods.

# ####Instructions

# Find the three most nutritious foods by sorting food_info using the "nutritional_rating" column.
# 
# Get the name of those foods (the "Shrt_Desc" column), and assign the names to most_nutritious_foods.
# 
# If most_nutritious_foods isn't a list at the end, use the list() function to turn it into one.

# In[19]:

# Assign most nutritional foods.
most_nutritious_foods = []
sorted_food_info = food_info.sort(["nutritional_rating"], ascending=[False])
most_nutritious_foods = sorted_food_info["Shrt_Desc"].iloc[0:3]
most_nutritious_foods = list(most_nutritious_foods)

print "Most nutritional foods:"
print most_nutritious_foods


# ###18: Finding the least nutritious foods

# Let's do the same as in the last screen, but find the least nutritious foods.

# ####Instructions

# Find the three least nutritious foods by sorting food_info using the "nutritional_rating" column.
# 
# Get the name of those foods (the "Shrt_Desc" column), and assign the names to least_nutritious_foods.
# 
# If least_nutritious_foods isn't a list at the end, use the list() function to turn it into one.

# In[20]:

# Assign least nutritional foods.
least_nutritious_foods = []
sorted_food_info = food_info.sort(["nutritional_rating"], ascending=[True])
least_nutritious_foods = sorted_food_info["Shrt_Desc"].iloc[0:3]
least_nutritious_foods = list(least_nutritious_foods)

print "Least nutritional foods:"
print least_nutritious_foods

