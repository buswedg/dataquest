

```python
from __future__ import print_function
```

#Python Programming

##Dictionaries

###1: Parsing the file

Our data is in a CSV file, so we'll need to parse it before we can get started.

####Instructions

Open "la_weather.csv", parse it, and assign the result to weather_data.


```python
weather_data = []
f = open("data/la_weather.csv", "r")
data = f.read()
rows = data.split("\n")
for row in rows:
    split_row = row.split(",")
    weather_data.append(split_row)
weather_data[:10]
```




    [['Day', 'Type\xa0of\xa0Weather'],
     ['1', 'Sunny'],
     ['2', 'Sunny'],
     ['3', 'Sunny'],
     ['4', 'Sunny'],
     ['5', 'Sunny'],
     ['6', 'Rain'],
     ['7', 'Sunny'],
     ['8', 'Sunny'],
     ['9', 'Fog']]



###2: Getting a single column from the data

The first column of the data isn't very useful to what we're doing, so let's get rid of it and only work with the second column.

####Instructions

Get all of the values in the second column and append them to weather_column.


```python
weather_column = []
for row in weather_data:
    if row:
        weather_column.append(row[1])
weather_column[:10]
```




    ['Type\xa0of\xa0Weather',
     'Sunny',
     'Sunny',
     'Sunny',
     'Sunny',
     'Sunny',
     'Rain',
     'Sunny',
     'Sunny',
     'Fog']



###3: Pre-defined variables

Loop over the weather variable, and set count equal to the number of items in weather.

####Instructions

Loop over the weather variable, and set count equal to the number of items in weather.


```python
weather = weather_data
with open("data/la_weather.csv", "r") as f:
    # weather_data = [row.rstrip().split(',') for row in f]
    weather = [row.rstrip().split(',')[1] for row in f][1:]
print("weather[0]:", weather[0])

# Loop over the weather variable, and set count equal to the number of items in weather.
count = 0
for item in weather:
    count = count + 1
print("count:", count)
```

    weather[0]: Sunny
    count: 365
    

###4: Practice slicing a list

Now that we know how to slice lists, let's practice.

####Instructions

Assign a slice containing index 2 and 3 from slice_me to slice1. Assign a slice containing index 1 from slice_me to slice2. Assign a slice containing index 3 and 4 from slice_me to slice3.


```python
a = [4,5,6,7,8]
print("a:", a)
# New list containing index 2 and 3.
print("a[2:4]:", a[2:4])
# New list with no elements.
print("a[2:2]:", a[2:2])
# New list containing only index 2.
print("a[2:3]:", a[2:3])

slice_me = [7,6,4,5,6]
print("slice_me:", slice_me)

slice1 = slice_me[2:4]
print("slice1:", slice1)

slice2 = slice_me[1:2]
print("slice2:", slice2)

slice3 = slice_me[3:5]
print("slice3:", slice3)
```

    a: [4, 5, 6, 7, 8]
    a[2:4]: [6, 7]
    a[2:2]: []
    a[2:3]: [6]
    slice_me: [7, 6, 4, 5, 6]
    slice1: [4, 5]
    slice2: [6]
    slice3: [5, 6]
    

###5: Removing our header

Now that we can slice lists, let's remove the header from the weather data.

####Instructions

The weather data is in the weather variable. Slice the data and remove the header. The slice can end at 367. Assign the result to new_weather.


```python
new_weather = weather[1:367]
new_weather[:10]
```




    ['Sunny',
     'Sunny',
     'Sunny',
     'Sunny',
     'Rain',
     'Sunny',
     'Sunny',
     'Fog',
     'Rain',
     'Sunny']



###6: Making a dictionary

Use curly braces to define a dictionary -- {} -- and then you add keys.

####Instructions

Assign the value 5 to the key "test" in dictionary_two. Assign the value "hello" to the key 10 in dictionary_two.


```python
# Make dictionary.
dictionary_one = {}

# Add keys and values.
dictionary_one["key_one"] = 2
print("dictionary_one:", dictionary_one)

# Dictionaries can have multiple keys.
dictionary_one[10] = 5
dictionary_one[5.2] = "hello"
print("dictionary_one:", dictionary_one)

# Make dictionary.
dictionary_two = {}

# Add keys and values.
dictionary_two["test"] = 5
dictionary_two[10] = "hello"
print("dictionary_two:", dictionary_two)
```

    dictionary_one: {'key_one': 2}
    dictionary_one: {10: 5, 'key_one': 2, 5.2: 'hello'}
    dictionary_two: {'test': 5, 10: 'hello'}
    

###7: Indexing a dictionary

We can index dictionaries with square brackets. a = dictionary[10] will get the value stored in the dictionary for the key 10 and assign it to a.

####Instructions

Assign the value in "key1" in dictionary_two to a. Assign the value in "key2" in dictionary_two to b. Assign the value in "key3" in dictionary_two to c.


```python
# Make dictionary.
dictionary_one = {}

# Add keys and values.
dictionary_one["test"] = 10
dictionary_one["key"] = "fly"

print("dictionary_one:", dictionary_one)

# Retrieve values from dictionaries.
print("dictionary_one['test']:", dictionary_one["test"])
print("dictionary_one['key']:", dictionary_one["key"])

# Make dictionary.
dictionary_two = {}

# Add keys and values.
dictionary_two["key1"] = "high"
dictionary_two["key2"] = 10
dictionary_two["key3"] = 5.6

print("dictionary_two:", dictionary_two)

# Retrieve values from dictionaries.
a = dictionary_two["key1"]
print("a:", a)

b = dictionary_two["key2"]
print("b:", b)

c = dictionary_two["key3"]
print("c:", c)
```

    dictionary_one: {'test': 10, 'key': 'fly'}
    dictionary_one['test']: 10
    dictionary_one['key']: fly
    dictionary_two: {'key3': 5.6, 'key2': 10, 'key1': 'high'}
    a: high
    b: 10
    c: 5.6
    

###8: Defining a dictionary with values

We can define a dictionary that already contains values.

####Instructions

Make a dictionary c with the keys 7, 8, and 9 corresponding to the values "raven", "goose", and "duck". Make a dictionary d with the keys "morning", "afternoon", "evening", and "night" corresponding to the values 9, 14, 19, and 23.


```python
# Define dictionary that already contains values.
a = {"key1": 10, "key2": "indubitably", "key3": "dataquest", 3: 5.6}
print("a:", a)
print("a['key1']:", a["key1"])

# Define dictionary that already contains values.
b = {4: "robin", 5: "bluebird", 6: "sparrow"}
print("b:", b)
print("b[4]:", b[4])

# Define dictionary that already contains values.
c = {7: "raven", 8: "goose", 9: "duck"}
print("c:", c)
print("c[7]:", c[7])

# Define dictionary that already contains values.
d = {"morning": 9, "afternoon": 14, "evening": 19, "night": 23}
print("d:", d)
print("d['morning']:", d["morning"])
```

    a: {3: 5.6, 'key3': 'dataquest', 'key2': 'indubitably', 'key1': 10}
    a['key1']: 10
    b: {4: 'robin', 5: 'bluebird', 6: 'sparrow'}
    b[4]: robin
    c: {8: 'goose', 9: 'duck', 7: 'raven'}
    c[7]: raven
    d: {'evening': 19, 'night': 23, 'afternoon': 14, 'morning': 9}
    d['morning']: 9
    

###9: Testing if items are in a list

Let's practice testing if items are in a list.

####Instructions

Check if 9 is in list2, and assign the result to c. Check if 8 is in list2, and assign the result to d. Check if -1 is in list2, and assign the result to e.


```python
# Create list.
the_list = [10,60,-5,8]
print("the_list:", the_list)

# Print whether 10 is in 'the_list' using an 'in' statement.
print("10 in the_list:", 10 in the_list)

# Print whether -5 is in 'the_list' using an 'in' statement.
print("-5 in the_list:", -5 in the_list)

# Print whether 9 is in 'the_list' using an 'in' statement.
print("9 in the_list:", 9 in the_list)

# Assign the result of an in statement to a variable.
a = 7 in the_list
print("a:", a)

# Create list.
list2 = [8, 5.6, 70, 800]
print("list2:", list2)

c = 9 in list2
print("c:", c)

d = 8 in list2
print("d:", d)

e = -1 in list2
print("e:", e)
```

    the_list: [10, 60, -5, 8]
    10 in the_list: True
    -5 in the_list: True
    9 in the_list: False
    a: False
    list2: [8, 5.6, 70, 800]
    c: False
    d: True
    e: False
    

###10: More uses for the in statement

We can also use the in statement to check if a key is in a dictionary. We do this the same way we check if a value is in a list.

####Instructions

Check whether "jupiter" is in dict2 and assign the result to b. Check whether "earth" is in dict2 and assign the result to c.


```python
# Define dictionary that already contains values.
the_dict = {"robin": "red", "cardinal": "red", "oriole": "orange", "lark": "blue"}
print("the_dict:", the_dict)

# Print whether robin is in 'the_dict' using an 'in' statement.
print("'robin' in the_dict:", "robin" in the_dict)

# Print whether crow is in 'the_dict' using an 'in' statement.
print("'crow' in the_dict:", "crow" in the_dict)

# Assign the result of an in statement to a variable.
a = "cardinal" in the_dict
print("a:", a)

# Define dictionary that already contains values.
dict2 = {"mercury": 1, "venus": 2, "earth": 3, "mars": 4}
print("dict2", dict2)

b = "jupiter" in dict2
print("b:", b)

c = "earth" in dict2
print("c:", c)
```

    the_dict: {'cardinal': 'red', 'lark': 'blue', 'robin': 'red', 'oriole': 'orange'}
    'robin' in the_dict: True
    'crow' in the_dict: False
    a: True
    dict2 {'earth': 3, 'mercury': 1, 'venus': 2, 'mars': 4}
    b: False
    c: True
    

###11: Practicing with the else statement

The else statement is a powerful way to extend a basic if statement.

####Instructions

Write an if statement that prints "It's hot!" when the season is "Summer" Add an else statement to the if that prints "It might be hot!".


```python
# Code in an else statement will be executed if the if statement boolean is False.
a = 6
if a == 7:
    print(a)
else:
    print("Not 7!")

video_game = "Mario"
if video_game == "Mario":
    print("Nintendo is the best!")
else:
    print("Sony is the best!")

season = "Spring"
if season == "Summer":
    print("It's hot!")
else:
    print("It might be hot!")
```

    Not 7!
    Nintendo is the best!
    It might be hot!
    

###12: Counting with dictionaries

We can combine some of the concepts we've already learned to count how many times items appear in a list using dictionaries. We'll loop over the list, and create a key for each item we want to count. We then increment the key whenever we see the element again. At the end, we have the count.

####Instructions

Count how many times each presidential last name appears in us_presidents. Assign the counts to us_president_counts.


```python
# Create list.
pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]
print("pantry:", pantry)

# Create an empty dictionary.
pantry_counts = {}
# Loop through the list.
for item in pantry:
    if item in pantry_counts:
        # If the list item is already a key in the dictionary, then add 1 to the value of that key.
        pantry_counts[item] = pantry_counts[item] + 1
    else:
        # If the item isn't already a key in the count dictionary, then add the key, and set the value to 1.
        pantry_counts[item] = 1 
print("pantry_counts:", pantry_counts)

# Create list.
us_presidents = ["Adams", "Bush", "Clinton", "Obama", "Harrison", "Taft", "Bush", "Adams", "Wilson", "Roosevelt", "Roosevelt"]
print("us_presidents:", us_presidents)

# Create an empty dictionary.
us_president_counts = {}
# Loop through the list.
for president in us_presidents:
    if president in us_president_counts:
        # If the list item is already a key in the dictionary, then add 1 to the value of that key.
        us_president_counts[president] = us_president_counts[president] + 1
    else:
        # If the item isn't already a key in the count dictionary, then add the key, and set the value to 1.
        us_president_counts[president] = 1
print("us_president_counts:", us_president_counts)
```

    pantry: ['apple', 'orange', 'grape', 'apple', 'orange', 'apple', 'tomato', 'potato', 'grape']
    pantry_counts: {'tomato': 1, 'apple': 3, 'potato': 1, 'orange': 2, 'grape': 2}
    us_presidents: ['Adams', 'Bush', 'Clinton', 'Obama', 'Harrison', 'Taft', 'Bush', 'Adams', 'Wilson', 'Roosevelt', 'Roosevelt']
    us_president_counts: {'Harrison': 1, 'Roosevelt': 2, 'Clinton': 1, 'Adams': 2, 'Taft': 1, 'Bush': 2, 'Obama': 1, 'Wilson': 1}
    

###13: Counting the weather!

We now know how to count up how many times each type of weather occurs in the data!

####Instructions

The weather column, minus the header, has been loaded into the weather variable. Count up how many times each type of weather occurs. Store the counts in weather_counts.


```python
# Create an empty dictionary.
weather_counts = {}
# Loop through the list.
for item in weather:
    if item in weather_counts:
        weather_counts[item] = weather_counts[item] + 1
    else:
        weather_counts[item] = 1
print("weather_counts:", weather_counts)
```

    weather_counts: {'Rain': 25, 'Sunny': 210, 'Fog-Rain': 4, 'Thunderstorm': 1, 'Fog': 125}
    
