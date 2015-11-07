

```python
from __future__ import print_function
```

#Data Analysis with Pandas

##Dataframe Basics

###1: Read in a CSV file

The first step, as always, is reading in a csv file.

With pandas, we'll need to use the read_csv method.

With pandas, the equivalent of a two-dimensional numpy array, or matrix, is called a dataframe.

####Instructions

Read "food_info.csv" info food_info.


```python
import pandas

food_info = pandas.read_csv("data/food_info.csv", encoding = "latin-1")
food_info[:5]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>NDB_No</th>
      <th>Shrt_Desc</th>
      <th>Water_(g)</th>
      <th>Energ_Kcal</th>
      <th>Protein_(g)</th>
      <th>Lipid_Tot_(g)</th>
      <th>Ash_(g)</th>
      <th>Carbohydrt_(g)</th>
      <th>Fiber_TD_(g)</th>
      <th>Sugar_Tot_(g)</th>
      <th>...</th>
      <th>Vit_K_(µg)</th>
      <th>FA_Sat_(g)</th>
      <th>FA_Mono_(g)</th>
      <th>FA_Poly_(g)</th>
      <th>Cholestrl_(mg)</th>
      <th>GmWt_1</th>
      <th>GmWt_Desc1</th>
      <th>GmWt_2</th>
      <th>GmWt_Desc2</th>
      <th>Refuse_Pct</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1001</td>
      <td>BUTTER,WITH SALT</td>
      <td>15.87</td>
      <td>717</td>
      <td>0.85</td>
      <td>81.11</td>
      <td>2.11</td>
      <td>0.06</td>
      <td>0</td>
      <td>0.06</td>
      <td>...</td>
      <td>7.0</td>
      <td>51.368</td>
      <td>21.021</td>
      <td>3.043</td>
      <td>215</td>
      <td>5.00</td>
      <td>1 pat,  (1" sq, 1/3" high)</td>
      <td>14.2</td>
      <td>1 tbsp</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002</td>
      <td>BUTTER,WHIPPED,W/ SALT</td>
      <td>16.72</td>
      <td>718</td>
      <td>0.49</td>
      <td>78.30</td>
      <td>1.62</td>
      <td>2.87</td>
      <td>0</td>
      <td>0.06</td>
      <td>...</td>
      <td>4.6</td>
      <td>45.390</td>
      <td>19.874</td>
      <td>3.331</td>
      <td>225</td>
      <td>3.80</td>
      <td>1 pat,  (1" sq, 1/3" high)</td>
      <td>9.4</td>
      <td>1 tbsp</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1003</td>
      <td>BUTTER OIL,ANHYDROUS</td>
      <td>0.24</td>
      <td>876</td>
      <td>0.28</td>
      <td>99.48</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0</td>
      <td>0.00</td>
      <td>...</td>
      <td>8.6</td>
      <td>61.924</td>
      <td>28.732</td>
      <td>3.694</td>
      <td>256</td>
      <td>12.80</td>
      <td>1 tbsp</td>
      <td>205.0</td>
      <td>1 cup</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1004</td>
      <td>CHEESE,BLUE</td>
      <td>42.41</td>
      <td>353</td>
      <td>21.40</td>
      <td>28.74</td>
      <td>5.11</td>
      <td>2.34</td>
      <td>0</td>
      <td>0.50</td>
      <td>...</td>
      <td>2.4</td>
      <td>18.669</td>
      <td>7.778</td>
      <td>0.800</td>
      <td>75</td>
      <td>28.35</td>
      <td>1 oz</td>
      <td>17.0</td>
      <td>1 cubic inch</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1005</td>
      <td>CHEESE,BRICK</td>
      <td>41.11</td>
      <td>371</td>
      <td>23.24</td>
      <td>29.68</td>
      <td>3.18</td>
      <td>2.79</td>
      <td>0</td>
      <td>0.51</td>
      <td>...</td>
      <td>2.5</td>
      <td>18.764</td>
      <td>8.598</td>
      <td>0.784</td>
      <td>94</td>
      <td>132.00</td>
      <td>1 cup, diced</td>
      <td>113.0</td>
      <td>1 cup, shredded</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 53 columns</p>
</div>



###2: Indexing data with pandas

Indexing in pandas is slightly different from in numpy.

We need to use the .iloc[] method (note how it uses square brackets instead of parentheses).

- numpy_array[0,0]
- numpy_array[:,0]
- numpy_array[0,:]

The above lines of code will get the first element of the first row, the whole first column, and the whole first row from a numpy array, respectively.

- pandas_dataframe.iloc[0,0]
- pandas_dataframe.iloc[:,0]
- pandas_dataframe.iloc[0,:]  

The above is the equivalent indexing in a pandas dataframe.

####Instructions

Assign the second row of food_info to the variable second_row.

Assign the tenth row of food_info to the variable tenth_row.


```python
# Print first row of data.
print("food_info.iloc[0,:10]:\n", food_info.iloc[0,:10])

# Assign second row.
second_row = food_info.iloc[1,:]

# Assign tenth row.
tenth_row = food_info.iloc[9,:]
```

    food_info.iloc[0,:10]:
     NDB_No                        1001
    Shrt_Desc         BUTTER,WITH SALT
    Water_(g)                    15.87
    Energ_Kcal                     717
    Protein_(g)                   0.85
    Lipid_Tot_(g)                81.11
    Ash_(g)                       2.11
    Carbohydrt_(g)                0.06
    Fiber_TD_(g)                     0
    Sugar_Tot_(g)                 0.06
    Name: 0, dtype: object
    

###3: Index a series

What we call a vector or a one-dimensional array is called a series in pandas.

We index a series without using .iloc[].

####Instructions

Assign the first 20 items in the second row to first_20_items_in_second_row.

Assign the first 10 items in the first column to first_10_items_in_first_column.


```python
# Assin a series.
first_row = food_info.iloc[0,:]

# Assign first 10 items from first row.
first_ten_items_in_first_row = first_row[0:10]
first_ten_items_in_first_row = food_info.iloc[0,:][0:10]

# Assign first 20 items from second row.
first_20_items_in_second_row = food_info.iloc[1,:][0:20]

# Assign first 10 items from first column.
first_10_items_in_first_column = food_info.iloc[:,0][0:10]
```

###4: Get column by name

One cool thing about pandas is that we can get columns with their names, instead of only by number.

####Instructions

Assign the FA_Sat_(g) column to the variable saturated_fat.

Assign the Cholestrl_(mg) to the variable cholesterol.


```python
# Print names of all the columns (in order).
print("list(food_info.columns.values):\n", list(food_info.columns.values))

# Print a particular column.
print("food_info['Protein_(g)'][0:10]:\n", food_info["Protein_(g)"][0:10])

# Assign particular columns.
sodium_column = food_info["Sodium_(mg)"]
saturated_fat = food_info["FA_Sat_(g)"]
cholesterol = food_info["Cholestrl_(mg)"]
```

    list(food_info.columns.values):
     ['NDB_No', 'Shrt_Desc', 'Water_(g)', 'Energ_Kcal', 'Protein_(g)', 'Lipid_Tot_(g)', 'Ash_(g)', 'Carbohydrt_(g)', 'Fiber_TD_(g)', 'Sugar_Tot_(g)', 'Calcium_(mg)', 'Iron_(mg)', 'Magnesium_(mg)', 'Phosphorus_(mg)', 'Potassium_(mg)', 'Sodium_(mg)', 'Zinc_(mg)', 'Copper_mg)', 'Manganese_(mg)', 'Selenium_(µg)', 'Vit_C_(mg)', 'Thiamin_(mg)', 'Riboflavin_(mg)', 'Niacin_(mg)', 'Panto_Acid_mg)', 'Vit_B6_(mg)', 'Folate_Tot_(µg)', 'Folic_Acid_(µg)', 'Food_Folate_(µg)', 'Folate_DFE_(µg)', 'Choline_Tot_ (mg)', 'Vit_B12_(µg)', 'Vit_A_IU', 'Vit_A_RAE', 'Retinol_(µg)', 'Alpha_Carot_(µg)', 'Beta_Carot_(µg)', 'Beta_Crypt_(µg)', 'Lycopene_(µg)', 'Lut+Zea_ (µg)', 'Vit_E_(mg)', 'Vit_D_µg', 'Vit_D_IU', 'Vit_K_(µg)', 'FA_Sat_(g)', 'FA_Mono_(g)', 'FA_Poly_(g)', 'Cholestrl_(mg)', 'GmWt_1', 'GmWt_Desc1', 'GmWt_2', 'GmWt_Desc2', 'Refuse_Pct']
    food_info['Protein_(g)'][0:10]:
     0     0.85
    1     0.49
    2     0.28
    3    21.40
    4    23.24
    5    20.75
    6    19.80
    7    25.18
    8    22.87
    9    23.37
    Name: Protein_(g), dtype: float64
    

###5: Getting multiple columns by name

We can get a single column by passing in a name, but we can also get multiple columns by passing in a list of names.

####Instructions

Assign the 'Zinc_(mg)' and 'Copper_(mg)' columns to zinc_and_copper.

Assign the 'Selenium_(mcg)' and 'Thiamin_(mg)' columns to selenium_and_thiamin.

Make sure that you get the columns in order (zinc and selenium come first).


```python
#print(food_info.columns.values)

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
```

###6: Math with columns

We can do math with vectors (or, as we are more familiar with them as, columns).

Adding two columns will go through and add each value at each position to the corresponding value in the same position.

First, the values at index 0 will be added, then the values at index 1, and so on.

At the end, you'll have a new vector with all of the sums.

In order to do this kind of math, the vectors all need to be the same length (have the same number of elements).

####Instructions

Assign the number of grams of protein per gram of water ("Protein_(g)" column divided by "Water_(g)" column) to grams_of_protein_per_gram_of_water.

Assign the total amount of calcium and iron("Calcium_(mg)" column plus "Iron_(mg)" column) to milligrams_of_calcium_and_iron.


```python
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
```

###7: Math with scalars

We can also do math with a vector (column) and a scalar (single numbers).

food_info["Iron_(mg)"] / 1000  

The statement above will divide each item in the "Iron_(mg)" column by 1000, converting the values from milligrams to grams.

Multiplying by scalars can be a good way to manipulate values in columns.

####Instructions

Assign the number of grams of "Sodium_(mg)" to the variable sodium_grams (divide the column by 1000).

Assign the number of milligrams of "Sugar_Tot_(g)" to the variable sugar_milligrams (multiply the column by 1000).


```python
# Divide the protein column by a scalar to get kilograms.
protein_kilograms = food_info["Protein_(g)"] / 1000

# Subtract 5 grams from carbohydrates.
lowered_carbs = food_info["Carbohydrt_(g)"] - 5

# Assign the number of grams of "Sodium_(mg)" to the variable sodium_grams.
sodium_grams = food_info["Sodium_(mg)"] / 1000

# Assign the number of milligrams of "Sugar_Tot_(g)" to the variable sugar_milligrams.
sugar_milligrams = food_info["Sugar_Tot_(g)"] * 1000
```

###8: Sorting columns

We can also sort the dataframe by the values in a column.

To do this, we use the .sort method, which returns a new dataframe sorted according to the specified criteria.

####Instructions

Sort by the amount of "Sodium_(mg)", with the largest value on top (descending sort). Assign the result to descending_sodium.

Sort by the amount of "Vit_C_(mg)", with the smallest value on top (ascending sort). Assign the result to ascending_vitamin_c.


```python
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

print("ascending_vitamin_c.iloc[0,:10]:\n", ascending_vitamin_c.iloc[0,:10])
```

    ascending_vitamin_c.iloc[0,:10]:
     NDB_No                        1001
    Shrt_Desc         BUTTER,WITH SALT
    Water_(g)                    15.87
    Energ_Kcal                     717
    Protein_(g)                   0.85
    Lipid_Tot_(g)                81.11
    Ash_(g)                       2.11
    Carbohydrt_(g)                0.06
    Fiber_TD_(g)                     0
    Sugar_Tot_(g)                 0.06
    Name: 0, dtype: object
    

###9: Multicolumn sort

We only sorted on the value of a single column before, but we can also sort based on multiple columns.

The first column in the list will be sorted on first. Any rows that have the same value for the first column will be sorted based on the second column, and so on until all of the given columns are used.

We can specify different sort orders for each column using the ascending argument.

####Instructions

Perform a multicolumn sort on food_info, with the first column being "Sugar_Tot_(g)" ascending, and the second being "Zinc_(mg)" descending. Assign the result to ascending_sugar_then_descending_zinc.

Perform a multicolumn sort on food_info, with the first column being "Cholestrl_(mg)" descending, and the second being "Protein_(g)" ascending. Assign the result to descending_cholesterol_then_ascending_protein.


```python
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

print("descending_cholesterol_then_ascending_protein.iloc[0,:10]:\n", descending_cholesterol_then_ascending_protein.iloc[0,:10])
```

    descending_cholesterol_then_ascending_protein.iloc[0,:10]:
     NDB_No                                                17189
    Shrt_Desc         VEAL,VAR MEATS&BY-PRODUCTS,BRAIN,CKD,BRSD
    Water_(g)                                             76.89
    Energ_Kcal                                              136
    Protein_(g)                                           11.48
    Lipid_Tot_(g)                                          9.63
    Ash_(g)                                                 1.4
    Carbohydrt_(g)                                            0
    Fiber_TD_(g)                                              0
    Sugar_Tot_(g)                                           NaN
    Name: 5287, dtype: object
    

###10: Creating a rating

Let's say that we have a friend, Superman, who's trying to gain muscle, and so he wants to eat foods that have a lot of protein.

But he's also very health conscious, so he wants to avoid fat.

We could sort based on those two columns and give him an answer, but what if he cares more about a food having a lot of protein than it being too fatty?

What we need to do is construct a rating for each food based on Superman's criteria.

Then we can recommend the food that scores the highest.

####Instructions

Let's say Superman now decides that the food having a lot of protein is only twice as important as the food not being too fatty.

Construct the new rating, and assign it to new_rating


```python
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

print("descending_new_rating.iloc[0,:10]:\n", descending_new_rating.iloc[0,:10])
```

    descending_new_rating.iloc[0,:10]:
     NDB_No                              16422
    Shrt_Desc         SOY PROT ISOLATE,K TYPE
    Water_(g)                            4.98
    Energ_Kcal                            321
    Protein_(g)                         88.32
    Lipid_Tot_(g)                        0.53
    Ash_(g)                              3.58
    Carbohydrt_(g)                       2.59
    Fiber_TD_(g)                            0
    Sugar_Tot_(g)                           0
    Name: 5009, dtype: object
    

###11: Normalizing columns

One of the simplest ways to normalize a column is to divide all of the values by the maximum value in the column.

It will change all of the values to be between 0 and 1.

It doesn't work so well with negative values, but we don't have any (you can't have negative amounts of protein, fat, etc).

This isn't necessarily the best way to normalize, and we'll learn some better methods soon.

####Instructions

Normalize the values in the "Vit_C_(mg)" column, and assign the result to normalized_vitamin_c

Normalize the values in the "Zinc_(mg)" column, and assign the result to normalized_zinc


```python
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
print("descending_normalized_vitamin_c.iloc[0,:10]:\n", descending_normalized_vitamin_c.iloc[0,:10])

# Create normalized zinc value.
normalized_zinc = food_info["Zinc_(mg)"] / food_info["Zinc_(mg)"].max()
```

    descending_normalized_vitamin_c.iloc[0,:10]:
     NDB_No                                                         3022
    Shrt_Desc         BABYFOOD,GERBER,2ND FOODS,APPL,CARROT & SQUASH...
    Water_(g)                                                     83.83
    Energ_Kcal                                                       64
    Protein_(g)                                                     1.1
    Lipid_Tot_(g)                                                     0
    Ash_(g)                                                        0.26
    Carbohydrt_(g)                                                14.82
    Fiber_TD_(g)                                                    1.2
    Sugar_Tot_(g)                                                  9.09
    Name: 332, dtype: object
    

###12: Making a better rating

We now know enough to construct a better rating for our friend Superman.

We just have to normalize the columns that we are interested in before we create the rating.

####Instructions

Superman is twice as interested in a food having a lot of protein than he is in it having too much fat.

Construct a rating with these new criteria, and assign it to better_protein_rating.

Make sure to normalize the protein ("Protein_(g)") and fat ("Lipid_Tot_(g)") columns first.


```python
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
print("descending_better_protein_rating.iloc[0,:10]:\n", descending_better_protein_rating.iloc[0,:10])
```

    descending_better_protein_rating.iloc[0,:10]:
     NDB_No                              16422
    Shrt_Desc         SOY PROT ISOLATE,K TYPE
    Water_(g)                            4.98
    Energ_Kcal                            321
    Protein_(g)                         88.32
    Lipid_Tot_(g)                        0.53
    Ash_(g)                              3.58
    Carbohydrt_(g)                       2.59
    Fiber_TD_(g)                            0
    Sugar_Tot_(g)                           0
    Name: 5009, dtype: object
    

###13: Normalizing multiple columns

Now, let's say we want to construct a total nutrition rating that takes all the columns into account.

In order to do this, we would have to normalize each of the columns, which is a huge pain.

An easier way is to use a for loop to normalize each column.

The "NDB_No" and "Shrt_Desc" columns (first two) can't be normalized, because they aren't nutritional values. The first one is the ID number of the food, and the second is the name.

####Instructions

Remove the "NDB_No" and "Shrt_Desc" columns from all_columns

Then, use a for loop to normalize all the other columns.


```python
column_list = ["Energ_Kcal", "Protein_(g)"]

# Loop through column_list, and normalize each of the columns in it.
for column in column_list:
    food_info[column] = food_info[column] / food_info[column].max()

# All columns is a list of all the columns in the food_info dataframe.
all_columns = list(food_info.columns.values)
#print "All columns: ", all_columns

column_count = len(all_columns)
all_columns = all_columns[2:column_count]
print("all_columns:", all_columns)
```

    all_columns: ['Water_(g)', 'Energ_Kcal', 'Protein_(g)', 'Lipid_Tot_(g)', 'Ash_(g)', 'Carbohydrt_(g)', 'Fiber_TD_(g)', 'Sugar_Tot_(g)', 'Calcium_(mg)', 'Iron_(mg)', 'Magnesium_(mg)', 'Phosphorus_(mg)', 'Potassium_(mg)', 'Sodium_(mg)', 'Zinc_(mg)', 'Copper_(mg)', 'Manganese_(mg)', 'Selenium_(mcg)', 'Vit_C_(mg)', 'Thiamin_(mg)', 'Riboflavin_(mg)', 'Niacin_(mg)', 'Panto_Acid_mg)', 'Vit_B6_(mg)', 'Folate_Tot_(µg)', 'Folic_Acid_(µg)', 'Food_Folate_(µg)', 'Folate_DFE_(µg)', 'Choline_Tot_ (mg)', 'Vit_B12_(µg)', 'Vit_A_IU', 'Vit_A_RAE', 'Retinol_(µg)', 'Alpha_Carot_(µg)', 'Beta_Carot_(µg)', 'Beta_Crypt_(µg)', 'Lycopene_(µg)', 'Lut+Zea_ (µg)', 'Vit_E_(mg)', 'Vit_D_µg', 'Vit_D_IU', 'Vit_K_(µg)', 'FA_Sat_(g)', 'FA_Mono_(g)', 'FA_Poly_(g)', 'Cholestrl_(mg)', 'GmWt_1', 'GmWt_Desc1', 'GmWt_2', 'GmWt_Desc2', 'Refuse_Pct', 'new_rating', 'normalized_vitamin_c', 'better_protein_rating']
    

###14: Finding the amount of vitamins

Now that we normalized all of the columns, we're well on our way to making a nutritional rating.

In order to get there, let's create a sum of all the vitamin columns.

Most methods on pandas dataframes can operate on series, or on dataframes.

Let's take the .sum() method as an example.

On a series, it gives you the total of all the values in the series.

When used on a dataframe, it takes the optional axis keyword argument.

When axis is 0, it gives you a new series with the sums of all of the columns in the dataframe.

When axis is 1, it gives you a new series with sums of all of the rows in the dataframe.

####Instructions

Sum up the amount of vitamins in each food (using the vitamin_columns list to get columns from the dataframe), and assign the result to vitamin_totals.

You'll need to sum the total in each row.


```python
column_list = ["Fiber_TD_(g)", "Sugar_Tot_(g)"]

# Sum the amount of fiber and sugar in each of the foods.
row_total = food_info[column_list].sum(axis=1)
#print(row_total)

# Sum the total amount of fiber and sugar across all the foods.
column_total = food_info[column_list].sum(axis=0)
#print(column_total)

# Rename 'Vit_B12_(mcg)', 'Vit_D_mcg', 'Vit_K_(mcg)' columns.
food_info = food_info.rename(columns={"Vit_B12_(\xb5g)": "Vit_B12_(mcg)"})
food_info = food_info.rename(columns={"Vit_D_\xb5g": "Vit_D_mcg"})
food_info = food_info.rename(columns={"Vit_K_(\xb5g)": "Vit_K_(mcg)"})

# Sum the total amount of vitamins in each foods.
vitamin_columns = ["Calcium_(mg)", "Iron_(mg)", "Magnesium_(mg)", "Phosphorus_(mg)", 
                   "Potassium_(mg)", "Sodium_(mg)", "Zinc_(mg)", "Copper_(mg)", 
                   "Manganese_(mg)", "Selenium_(mcg)", "Vit_C_(mg)", "Thiamin_(mg)", 
                   "Riboflavin_(mg)", "Niacin_(mg)", "Vit_B6_(mg)", "Vit_B12_(mcg)", 
                   "Vit_A_IU", "Vit_A_RAE", "Vit_E_(mg)", "Vit_D_mcg", "Vit_D_IU", 
                   "Vit_K_(mcg)"]
vitamins = food_info[vitamin_columns]
vitamin_totals = vitamins.sum(axis=1)
print("vitamin_totals.head(10):\n", vitamin_totals.head(10))
```

    vitamin_totals.head(10):
     0    3910.684
    1    3829.252
    2    3934.431
    3    3303.482
    4    3261.634
    5    1982.328
    6    2885.552
    7    3312.130
    8    3554.729
    9    3159.877
    dtype: float64
    

###15: Adding a new column

We can add a column to a dataframe by assigning to it.

food_info["double_fat"] = food_info["Lipid_Tot_(g)"] * 2  

The above code assigns double the amount of lipids to the "double_fat" column in food_info.

####Instructions

We've read the vitamin_totals variable from the last screen in.

Assign vitamin_totals to the "vitamin_totals" column in food_info.


```python
# Assign double protein values.
food_info["double_protein"] = food_info["Protein_(g)"] * 2

# Assign vitamin totals.
food_info["vitamin_totals"] = vitamin_totals
```

###16: Making a nutritional index

We've normalized the values in vitamin_totals, and assigned it to the "vitamin_totals" column in food_info.

Let's construct a nutritional rating using the amount of vitamins, fats, protein, sugar, fiber, and cholesterol.

####Instructions

Give the "vitamin_totals" column a weight of 3, the "Lipid_Tot_(g)" column a weight of -2, the "Protein_(g)" column a weight of 3, the "Sugar_Tot_(g)" column a weight of -1, the "Fiber_TD_(g)" a weight of 1, and the "Cholestrl_(mg)" column a weight of -2.

Construct a rating using the above weights, and assign it to nutritional_rating.


```python
# Assign nutritional rating.
nutritional_rating = None
nutritional_rating = 3 * food_info["vitamin_totals"] + -2 * food_info["Lipid_Tot_(g)"] + 3 * food_info["Protein_(g)"] + -1 * food_info["Sugar_Tot_(g)"] + 1 * food_info["Fiber_TD_(g)"] + -2 * food_info["Cholestrl_(mg)"]
food_info["nutritional_rating"] = nutritional_rating

print("nutritional_rating.head(10):\n", nutritional_rating.head(10))
```

    nutritional_rating.head(10):
     0    11139.800872
    1    10881.112644
    2    11092.342511
    3     9703.192902
    4     9537.821402
    5     5691.878823
    6     8464.348554
    7             NaN
    8    10399.863834
    9             NaN
    dtype: float64
    

###17: Finding the most nutritious foods

We've read the nutritional rating series from the last screen to the "nutritional_rating" column in food_info.

Now, lets see if we can use it to find the most nutritious foods.

####Instructions

Find the three most nutritious foods by sorting food_info using the "nutritional_rating" column.

Get the name of those foods (the "Shrt_Desc" column), and assign the names to most_nutritious_foods.

If most_nutritious_foods isn't a list at the end, use the list() function to turn it into one.


```python
# Assign most nutritional foods.
most_nutritious_foods = []
sorted_food_info = food_info.sort(["nutritional_rating"], ascending=[False])
most_nutritious_foods = sorted_food_info["Shrt_Desc"].iloc[0:3]
most_nutritious_foods = list(most_nutritious_foods)

print("most_nutritious_foods:", most_nutritious_foods)
```

    most_nutritious_foods: ['BEEF,NZ,IMP,VAR MEATS & BY-PRODUCTS,LIVER,RAW', 'VEAL,VAR MEATS&BY-PRODUCTS,LIVER,CKD,BRSD', 'BEEF,NZ,IMP,VAR MEATS & BY-PRODUCTS LIVER,CKD,BLD']
    

###18: Finding the least nutritious foods

Let's do the same as in the last screen, but find the least nutritious foods.

####Instructions

Find the three least nutritious foods by sorting food_info using the "nutritional_rating" column.

Get the name of those foods (the "Shrt_Desc" column), and assign the names to least_nutritious_foods.

If least_nutritious_foods isn't a list at the end, use the list() function to turn it into one.


```python
# Assign least nutritional foods.
least_nutritious_foods = []
sorted_food_info = food_info.sort(["nutritional_rating"], ascending=[True])
least_nutritious_foods = sorted_food_info["Shrt_Desc"].iloc[0:3]
least_nutritious_foods = list(least_nutritious_foods)

print("least_nutritious_foods:", least_nutritious_foods)
```

    least_nutritious_foods: ['BEEF,VAR MEATS&BY-PRODUCTS,BRAIN,CKD,SIMMRD', 'BEEF,VAR MEATS&BY-PRODUCTS,BRAIN,RAW', 'LAMB,NZ,IMP,BRAINS,CKD,SOAKED & FRIED']
    
