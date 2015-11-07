

```python
from __future__ import print_function
```

#Data Analysis with Pandas

##Getting Started with Matrices

###1: Reading data into NumPy

NumPy is a Python module that has a lot of functions for working with data.

If you want to do serious work with data in Python, you'll be using a lot of NumPy.

We'll work through importing NumPy and loading in a csv file.

####Instructions

Import the data in "world_alcohol.csv" into the variable world_alcohol.


```python
import numpy

f = "data/world_alcohol.csv"
world_alcohol = numpy.genfromtxt(f, delimiter=",")
print("world_alcohol:\n", world_alcohol)
```

    world_alcohol:
     [[  1.98600000e+03              nan              nan              nan
        0.00000000e+00]
     [  1.98600000e+03              nan              nan              nan
        5.00000000e-01]
     [  1.98500000e+03              nan              nan              nan
        1.62000000e+00]
     ..., 
     [  1.98600000e+03              nan              nan              nan
        2.54000000e+00]
     [  1.98700000e+03              nan              nan              nan
        0.00000000e+00]
     [  1.98600000e+03              nan              nan              nan
        5.15000000e+00]]
    

###3: Fixing the data types

If you looked at the data you read in last screen, you may have noticed that it looked very strange.

This is because genfromtxt reads the data into a NumPy array.

Every element in an array has to be the same data type.

So everything is a string, or everything is an integer, and so on.

NumPy tried to convert all of our data to floats, which caused the values to become strange.

We'll need to specify the data type when we read our data in so we can avoid that.

####Instructions

Read in the "world_alcohol.csv" data to world_alcohol, using the str datatype.

Be sure to skip the header row.


```python
import numpy

# Using the dtype keyword argument with the str type tells numpy that everything we are reading in is a string.
# "U75" tells numpy to load the file as strings.
# The "U" refers to unicode (a type of string), and the 75 is the maximum length of a string element in the data.
# While we're at it, let's also skip the header.
# We can add the optional skip_header keyword argument, and set it equal to the number of header rows to skip (1).
f = "data/world_alcohol.csv"
world_alcohol = numpy.genfromtxt(f, delimiter=",", dtype="U75", skip_header=0)
print("world_alcohol:\n", world_alcohol)
```

    world_alcohol:
     [['1986' 'Western Pacific' 'Viet Nam' 'Wine' '0']
     ['1986' 'Americas' 'Uruguay' 'Other' '0.5']
     ['1985' 'Africa' "Cte d'Ivoire" 'Wine' '1.62']
     ..., 
     ['1986' 'Europe' 'Switzerland' 'Spirits' '2.54']
     ['1987' 'Western Pacific' 'Papua New Guinea' 'Other' '0']
     ['1986' 'Africa' 'Swaziland' 'Other' '5.15']]
    

###3: Indexing the data

Now that we know how to read in a file, let's start pulling values out.

Remember how all elements in a matrix have an index?

We can print the item at row 1, column 2, by typing print world_alcohol[0,1]

####Instructions

Assign the amount of alcohol Uruguayans drank in other beverages per capita in 1986 to uruguay_other_1986. This is the second row in the data.

Assign the whole fourth row to row_four.

Assign the whole year column to years.


```python
# The columns are Year, Region, Country, Beverage type, and Number of liters of pure alcohol drunk per person
# The print function below prints the number of liters of pure alcohol vietnamese drank in wine in 1986.
print("world_alcohol[0,4]:", world_alcohol[0,4])

# The Beverage type can take the values "Beer", "Wine", "Spirits", and "Other".

# If we want to grab a whole row, we replace the column number with a colon, which means "get all of the columns".
print("world_alcohol[0,:]:", world_alcohol[0,:])

# If we want to grab a whole column, we do the same thing with the row number.
countries = world_alcohol[:,2]
print("countries:", countries)

uruguay_other_1986 = world_alcohol[1,4]
print("uruguay_other_1986:", uruguay_other_1986)

row_four = world_alcohol[3,:]
print("row_four:", row_four)

years = world_alcohol[:,0]
print("years:", years)
```

    world_alcohol[0,4]: 0
    world_alcohol[0,:]: ['1986' 'Western Pacific' 'Viet Nam' 'Wine' '0']
    countries: ['Viet Nam' 'Uruguay' "Cte d'Ivoire" ..., 'Switzerland' 'Papua New Guinea'
     'Swaziland']
    uruguay_other_1986: 0.5
    row_four: ['1986' 'Americas' 'Colombia' 'Beer' '4.27']
    years: ['1986' '1986' '1985' ..., '1986' '1987' '1986']
    

###4: Vectors

When we grab a whole row or column from the matrix, we actually end up with a vector.

Just like a matrix is a 2-dimensional array because it has rows and columns, a vector is a 1-dimensional array.

Vectors are similar to Python lists in that they can be indexed with only one number.

Think of a vector as just a single row, or a single column.

####Instructions

Assign index 30 in the years column to years_30.

Assign from index 80 to index 200, inclusive, in the years columns to years_80_200.

Assign from index 100 to index 103, inclusive, in the years columns to years_100_103.


```python
# Countries is a vector.
countries = world_alcohol[:,2]

# We can index a vector with only one number.
print("countries[0]:", countries[0])
print("countries[10]:", countries[10])

# We can also slice vectors to get some of the values in the vector.
# The result is a new, smaller, vector.
# Slicing gets values from the first index up to but not including the second index.
print("countries[1:10]:", countries[1:10])
print("countries[50:70]:", countries[50:70])

years = world_alcohol[:,0]
years_30 = years[30]
years_80_200 = years[80:201]
years_100_103 = years[100:104]
```

    countries[0]: Viet Nam
    countries[10]: Botswana
    countries[1:10]: ['Uruguay' "Cte d'Ivoire" 'Colombia' 'Saint Kitts and Nevis' 'Guatemala'
     'Mauritius' 'Angola' 'Antigua and Barbuda' 'Nigeria']
    countries[50:70]: ['Switzerland' 'Finland' 'Saudi Arabia' 'Kuwait' 'El Salvador' 'Suriname'
     'Viet Nam' 'Croatia' 'Somalia' 'Syrian Arab Republic'
     'Iran (Islamic Republic of)' 'Papua New Guinea' 'Suriname' 'Libya'
     'Bolivia (Plurinational State of)' 'Somalia' 'Iraq' 'Namibia' 'Uganda'
     'Togo']
    

###5: Array shape

All arrays, whether they are 1-dimensional (vectors), two dimensional (matrices), or even larger, have a number of elements in each dimension.

For example, a matrix may have 200 rows and 10 columns.

We can use the shape method to find these dimensions.

####Instructions

Assign the shape of the first column in world_alcohol to column_one_shape. The first column has index 0.

Assign the shape of the tenth row in world_alcohol to row_ten_shape. The tenth row has index 9.


```python
# Print the shape of the world alcohol matrix.
# The first number is the number of rows, and the second is the number of columns.
print("world_alcohol.shape:", world_alcohol.shape)

# We can do the same with a vector, but they only have one dimension, so only one number is printed.
print("world_alcohol[1,:].shape:", world_alcohol[1,:].shape)
column_one_shape = world_alcohol[:,0].shape
row_ten_shape = world_alcohol[9,:].shape
```

    world_alcohol.shape: (3257, 5)
    world_alcohol[1,:].shape: (5,)
    

###6: Boolean elements

We can also use boolean statements on arrays to get truth values.

The interesting part about this is that the booleans are computed elementwise.

    world_alcohol[:,3] == "Beer"

The above code will actually compare each element of the fourth column of world_alcohol, check if it equals "Beer", and create a new vector with the True/False values.

####Instructions

Create a vector that checks if the values in column one equal "1984". Assign the vector to years_1984.

Create a vector that checks if the values in column three equal "Canada". Assign the vector to countries_canada.


```python
# This will get the first 10 items in the fourth column of world alcohol.
# This is the type column.
selected_types = world_alcohol[:,3][0:10]

# This will create a vector that contains True if the item at that position equal "Beer", and False if not.
# The vector is then printed.
# Note how the first three values are False, because the element in the position does not equal "Beer".
# The fourth and fifth are "True".
print("selected_types == 'Beer':", selected_types == "Beer")
years_1984 = world_alcohol[:,0] == "1984"
countries_canada = world_alcohol[:,2] == "Canada"
```

    selected_types == 'Beer': [False False False  True  True False False False False False]
    

###7: Subsets of vectors

We can subset vectors based on boolean vectors like the ones we generated in the last screen.

    beer = world_alcohol[:,3] == "Beer"
    print world_alcohol[:,3][beer]

The code above will select and print only the elements in the fourth column whose value is "Beer".

world_alcohol[:,3][beer] goes through each position in the fourth column vector (from 0 to the last index), and checks if the beer vector is True at the same position. If the beer vector is True, it assigns the element of the fourth column at that position to the subset. If the beer vector is False, the element is skipped.

####Instructions

Subset the third column of world_alcohol on whether the value is "Algeria". Assign the result to country_algeria.

Subset the first column of world_alcohol on whether the value is "1987". Assign the result to year_1987.


```python
# Select the first 10 values in the "type" column
types = world_alcohol[:,3][0:10]
print("types:", types)

# Create a boolean vector that contains True or False indicating whether each element in types == "Beer"
beer_boolean = types == "Beer"
print("beer_boolean:", beer_boolean)

# Subset the types vector using the beer_boolean
# We end up with only two entries, corresponding to the entries in the types vector that have the "Beer" value
print("types[beer_boolean]:", types[beer_boolean])
country_algeria = world_alcohol[:,2][world_alcohol[:,2] == "Algeria"]
year_1987 = world_alcohol[:,0][world_alcohol[:,0] == "1987"]
```

    types: ['Wine' 'Other' 'Wine' 'Beer' 'Beer' 'Other' 'Wine' 'Spirits' 'Spirits'
     'Other']
    beer_boolean: [False False False  True  True False False False False False]
    types[beer_boolean]: ['Beer' 'Beer']
    

###8: Subsets of matrices

We can subset a matrix in the same way that we can subset a vector.

    beer = world_alcohol[:,3] == "Beer"
    print world_alcohol[beer,:]

The above code will print all of the rows in world_alcohol where the "Type" column equals "Beer"

Note how because matrices are indexed using two numbers, we are substituting the boolean vector beer for the first number.

We can alter the second number to select different columns.

    beer = world_alcohol[:,3] == "Beer"
    print world_alcohol[beer,1]

The above code would select the second column where the "Type" column equals "Beer"

####Instructions

Assign all of the rows where the country equals "Turkey" to turkey_rows.

Assign the first 10 rows where the year equals "1985" to rows_1985.

Note that variable names in Python can't start with numbers, so we can't start our name with 1985.


```python
# wine_rows now contains only rows where the beverage type is wine.
wine = world_alcohol[:,3] == "Wine"
wine_rows = world_alcohol[wine,:]

# wine_rows is still a matrix, so we can index it as such.
# Just like we can slice vectors, we can slice matrix rows or columns.
# In the below statement, we print all of the columns in the first 10 rows of wine_rows.
print("wine_rows[0:10,:]:", wine_rows[0:10,:])
turkey = world_alcohol[:,2] == "Turkey"
turkey_rows = world_alcohol[turkey,:]

year_1985 = world_alcohol[:,0] == "1985"
rows_1985 = world_alcohol[year_1985,:][0:10,:]
```

    wine_rows[0:10,:]: [['1986' 'Western Pacific' 'Viet Nam' 'Wine' '0']
     ['1985' 'Africa' "Cte d'Ivoire" 'Wine' '1.62']
     ['1987' 'Africa' 'Mauritius' 'Wine' '0.13']
     ['1987' 'Africa' 'Botswana' 'Wine' '0.2']
     ['1987' 'Africa' 'Guinea-Bissau' 'Wine' '0.07']
     ['1984' 'Americas' 'Costa Rica' 'Wine' '0.06']
     ['1986' 'South-East Asia' 'Myanmar' 'Wine' '0']
     ['1985' 'Europe' 'United Kingdom of Great Britain and Northern Ireland'
      'Wine' '1.36']
     ['1986' 'Western Pacific' 'Micronesia (Federated States of)' 'Wine' '0']
     ['1986' 'Europe' 'Russian Federation' 'Wine' '0.8']]
    

###9: Subsets with multiple conditions

So now we can find all of the rows that correspond to "Algeria", for example.

But what if what we really want is to find all the rows for "Algeria" in "1985"?

We'll have to use multiple conditions to generate our vector.

    algeria_1985_boolean = (world_alcohol[:,2] == "Algeria") & (world_alcohol[:,0] == "1985")

The code above will generate a boolean that uses multiple conditions.

How it works is that the parentheses specify that the two component vectors should be generated first. (order of operations)

Then the two vectors will be compared index by index. If both vectors are True at index 1, then the resulting vector will be True at index 1.

If either vector is False at index 1, the result will be False at index 1.

Here's an expanded example:

    boolean_1985 = world_alcohol[:,0] == "1985"
    algeria_boolean = world_alcohol[:,2] == "Algeria"
    algeria_1985_boolean = boolean_1985 & algeria_boolean

We can add more than 2 conditions if we want -- we just have to put an & symbol between each one.

The resulting vector will contain True in the position corresponding to rows where all conditions are True, and False for rows where any condition is False.

####Instructions

Assign all rows where the country is "Yemen" and the year is "1987" to yemen_1987.

Assign all rows where the country is "Latvia", the year is "1989", and the type of alcohol is "Wine" to latvia_1989_wine.


```python
# Boolean vector corresponding to Canada and 1986.
canada_1986 = (world_alcohol[:,2] == "Canada") & (world_alcohol[:,0] == "1986")

# We can then use canada_1986 to subset a matrix -- it's just a normal boolean vector
print("world_alcohol[canada_1986,:]:", world_alcohol[canada_1986,:])
yemen_1987_boolean = (world_alcohol[:,2] == "Yemen") & (world_alcohol[:,0] == "1987")
yemen_1987 = world_alcohol[yemen_1987_boolean,:]

latvia_1989_wine_boolean = (world_alcohol[:,2] == "Latvia") & (world_alcohol[:,0] == "1989") & (world_alcohol[:,3] == "Wine")
latvia_1989_wine = world_alcohol[latvia_1989_wine_boolean,:]
```

    world_alcohol[canada_1986,:]: [['1986' 'Americas' 'Canada' 'Other' '']
     ['1986' 'Americas' 'Canada' 'Spirits' '3.11']
     ['1986' 'Americas' 'Canada' 'Beer' '4.87']
     ['1986' 'Americas' 'Canada' 'Wine' '1.33']]
    

###10: Convert a column to floats

We now know almost everything we need to compute how much alcohol the people in a country drank in a given year!

But there are a couple of things we need to work through first.

First, we need to convert the "Liters of alcohol drunk" column (the fifth one) to floats.

We need to do this because they are strings now, and we can't take the sum of strings.

Because they aren't numeric, their sum wouldn't make much sense.

We can use the astype method on the array to do this.


```python
# Let's convert the column to floats.
#alcohol_numbers = world_alcohol[:,4].astype(float)

# Hmm, but the above code fails with an error!
# It looks like some of the values in the column can't be converted to floats.
# We'll find out how we can figure out if values are failing in the next screen.
```

###11: Replace values in an array

There are values in our alcohol consumption column that are preventing us from converting the column from floats to strings.

In order to fix this, we first have to learn how to replace values.

We can replace values in a NumPy array by just assigning to them with the equals sign.

    world_alcohol[:,4][world_alcohol[:,4]=='0'] = '10'

The code above will replace any item in the alcohol consumption column that contains '0' (remember that the world alcohol matrix is all string values) with '10'.

####Instructions

Replace all instances of '1986' in the year column (column 1) with '2014'.

Replace all the values in the type column (column 4) with 'Grog' (pirates have taken over the world).


```python
# Let's say the US invades Canada (not that they should)
# This will replace all instances of "Canada" in the country column with "United States of America"
world_alcohol[:,2][world_alcohol[:,2] == "Canada"] = "United States of America"

# We don't have to subset before we replace
# Trinidad and Tobago can invade the whole world, and replace all countries
world_alcohol[:,2] = "Trinidad and Tobago"
print("world_alcohol[:,2][0:10]:", world_alcohol[:,2][0:10])

world_alcohol[:,0][world_alcohol[:,0] == "1986"] = "2014"
world_alcohol[:,3] = "Grog"

f = "data/world_alcohol.csv"
world_alcohol = numpy.genfromtxt(f, delimiter=",", dtype="U75", skip_header=0)
```

    world_alcohol[:,2][0:10]: ['Trinidad and Tobago' 'Trinidad and Tobago' 'Trinidad and Tobago'
     'Trinidad and Tobago' 'Trinidad and Tobago' 'Trinidad and Tobago'
     'Trinidad and Tobago' 'Trinidad and Tobago' 'Trinidad and Tobago'
     'Trinidad and Tobago']
    

###12: Convert the alcohol consumption column to floats

Now that you know what the bad value is, we can replace it and then convert the column to floats.m

####Instructions

Replace all the values in the alcohol consumption column (column 5) that equal bad_value with '0'.

Then convert all of the values in the column to floats, and assign the result to alcohol_consumption_float_column.

At the end, alcohol_consumption_float_column should contain a column of floats.


```python
bad_value = ""
alcohol_consumption_float_column = None
alcohol_consumption = world_alcohol[:,4]
alcohol_consumption[alcohol_consumption == bad_value] = "0"
alcohol_consumption_float_column = alcohol_consumption.astype(float)
```

###13: Compute the total alcohol consumption

We can compute the total value of a column using the sum method.

####Instructions

Use the sum method to store the sum of the alcohol consumption column into the total_alcohol column.


```python
# We've read the alcohol consumption column (converted to floats) into the alcohol_consumption variable.
total_alcohol = 0
total_alcohol = alcohol_consumption_float_column.sum()

print("total_alcohol:", total_alcohol)
```

    total_alcohol: 3908.96
    

###14: Finding how much alcohol a person in a country drank in a year

We can subset a vector with another vector, as we learned earlier.

This means that we can find the total alcohol consumed by any given country in any given year now.

####Instructions

Assign the total amount of alcohol an average person in "Canada" drank in "1986" to canada_1986_alcohol.

Assign the total amount of alcohol an average person in "Trinidad and Tobago" drank in "1987" to trinidad_1987_alcohol.


```python
# Create a boolean vector that contains True where year is 1985 and the country is Algeria.
algeria_1985 = (world_alcohol[:,2] == "Algeria") & (world_alcohol[:,0] == '1985')
print("algeria_1985:", algeria_1985)

# Subset the alcohol consumption vector with our boolean, and get the sum.
# The sum is the total amount of alcohol and average Algerian drank in 1985.
algeria_1985_alcohol = alcohol_consumption_float_column[algeria_1985].sum()
print("algeria_1985_alcohol:", algeria_1985_alcohol)

canada_1986 = (world_alcohol[:,2] == "Canada") & (world_alcohol[:,0] == '1986')
canada_1986_alcohol = alcohol_consumption_float_column[canada_1986].sum()
print("canada_1986_alcohol:", canada_1986_alcohol)

trinidad_1987 = (world_alcohol[:,2] == "Trinidad and Tobago") & (world_alcohol[:,0] == '1987')
trinidad_1987_alcohol = alcohol_consumption_float_column[trinidad_1987].sum()
print("trinidad_1987_alcohol:", trinidad_1987_alcohol)
```

    algeria_1985: [False False False ..., False False False]
    algeria_1985_alcohol: 0.31
    canada_1986_alcohol: 9.31
    trinidad_1987_alcohol: 4.35
    

###15: A function to sum yearly alcohol consumption

Now that we know how to find the total alcohol consumption of the average person in a country in a given year, we can make a function out of it.

A function will make it easier for us to calculate the alcohol consumption for all countries.

####Instructions

Fill in the rest of the calculate_consumption function.

Then use the function to calculate how much alcohol people in "India" drank in "1989" on average, and store the result in india_1989_alcohol.


```python
def calculate_consumption(country, year):
    country_year = (world_alcohol[:,2] == country) & (world_alcohol[:,0] == year)
    country_year_alcohol = alcohol_consumption_float_column[country_year].sum()
    return country_year_alcohol

india_1989_alcohol = calculate_consumption("India", "1989")
print("india_1989_alcohol:", india_1989_alcohol)
```

    india_1989_alcohol: 1.66
    

###17: Finding the country that drinks the least

We can now loop over our dictionary keys to find the country with the lowest amount of alcohol consumed per person in 1989.

####Instructions

Loop over the keys in country_consumption_1989 and find the country where the average person drank the least in 1989.

To do this, you'll need to use a for loop, and keep track of the lowest value and country.

Assign the lowest value to lowest_consumption, and the country with the lowest value to lowest_country.

Check the hint if you need help.


```python
country_consumption_1989 = world_alcohol[:][world_alcohol[:,0] == "1989"]
#print(country_consumption_1989)

# country_consumption_1989 has been loaded in for you.
lowest_country = None
lowest_consumption = None
for country in country_consumption_1989:
    consumption = float(country[4])
    if lowest_consumption is None or lowest_consumption > consumption:
        lowest_consumption = consumption
        lowest_country = country[2]
        
print("lowest_country:", lowest_country)
print("lowest_consumption:", lowest_consumption)
```

    lowest_country: Syrian Arab Republic
    lowest_consumption: 0.0
    

###17: Finding the country that drinks the most

Now we can find the country that drinks the most.

####Instructions

Loop over the keys in country_consumption_1989 and find the country where the average person drank the most in 1989.

To do this, you'll need to use a for loop, and keep track of the highest value and country.

Assign the highest value to highest_consumption, and the country with the highest value to highest_country.


```python
country_consumption_1989 = world_alcohol[:][world_alcohol[:,0] == "1989"]
#print(country_consumption_1989)

highest_country = None
highest_consumption = None
for country in country_consumption_1989:
    consumption = float(country[4])
    if highest_consumption is None or highest_consumption < consumption:
        highest_consumption = consumption
        highest_country = country[2]
        
print("highest_country:", highest_country)
print("highest_consumption:", highest_consumption)
```

    highest_country: France
    highest_consumption: 10.24
    
