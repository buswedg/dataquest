

```python
from IPython.display import HTML

HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>''')
```




<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>



#Python Programming

##Dictionaries

###1: Parsing the file

Our data is in a CSV file, so we'll need to parse it before we can get started.

Open "la_weather.csv", parse it, and assign the result to weather_data.


```python
weather_data = []
f = open("data/la_weather.csv", 'r')
data = f.read()
rows = data.split('\n')
for row in rows:
    split_row = row.split(",")
    weather_data.append(split_row)
```

###2: Getting a single column from the data

The first column of the data isn't very useful to what we're doing, so let's get rid of it and only work with the second column.

Get all of the values in the second column and append them to weather_column.


```python
weather_column = []
for row in weather_data:
    weather_column.append(row[1])
```

###3: Pre-defined variables

Loop over the weather variable, and set count equal to the number of items in weather.


```python
weather = weather_data
with open('data/la_weather.csv', 'r') as f:
    # weather_data = [row.rstrip().split(',') for row in f]
    weather = [row.rstrip().split(',')[1] for row in f][1:]


print(weather[0])

count = 0
for item in weather:
    count = count + 1
```

    Sunny
    

###4: Practice slicing a list

Assign a slice containing index 2 and 3 from slice_me to slice1. Assign a slice containing index 1 from slice_me to slice2. Assign a slice containing index 3 and 4 from slice_me to slice3.


```python
# Let's practice with some list slicing.
a = [4,5,6,7,8]
# New list containing index 2 and 3.
print(a[2:4])
# New list with no elements.
print(a[2:2])
# New list containing only index 2.
print(a[2:3])

slice_me = [7,6,4,5,6]
slice1 = slice_me[2:4]
slice2 = slice_me[1:2]
slice3 = slice_me[3:5]
```

    [6, 7]
    []
    [6]
    

###5: Removing our header

The weather data is in the weather variable. Slice the data and remove the header. The slice can end at 367. Assign the result to new_weather.


```python
new_weather = weather[1:367]
```

###6: Making a dictionary

Assign the value 5 to the key "test" in dictionary_two. Assign the value "hello" to the key 10 in dictionary_two.


```python
# We can make a dictionary with curly braces.
dictionary_one = {}

# The we can add keys and values.
dictionary_one["key_one"] = 2
print(dictionary_one)

# Keys and values can be anything.
# And dictionaries can have multiple keys
dictionary_one[10] = 5
dictionary_one[5.2] = "hello"
print(dictionary_one)

dictionary_two = {}
dictionary_two["test"] = 5
dictionary_two[10] = "hello"
```

    {'key_one': 2}
    {5.2: 'hello', 10: 5, 'key_one': 2}
    

###7: Indexing a dictionary

We can index dictionaries with square brackets. a = dictionary[10] will get the value stored in the dictionary for the key 10 and assign it to a.

Assign the value in "key1" in dictionary_two to a. Assign the value in "key2" in dictionary_two to b. Assign the value in "key3" in dictionary_two to c.


```python
dictionary_one = {}
dictionary_one["test"] = 10
dictionary_one["key"] = "fly"
# We can retrieve values from dictionaries with square brackets.
print(dictionary_one["test"])
print(dictionary_one["key"])

dictionary_two = {}
dictionary_two["key1"] = "high"
dictionary_two["key2"] = 10
dictionary_two["key3"] = 5.6
a = dictionary_two["key1"]
b = dictionary_two["key2"]
c = dictionary_two["key3"]
```

    10
    fly
    

###8: Defining a dictionary with values

We can define a dictionary that already contains values.

Make a dictionary c with the keys 7, 8, and 9 corresponding to the values "raven", "goose", and "duck". Make a dictionary d with the keys "morning", "afternoon", "evening", and "night" corresponding to the values 9, 14, 19, and 23.


```python
# We can define dictionaries that already contain values.
# All we do is add in keys and values separated by colons.
# We have to separate pairs of keys and values with commas.
a = {"key1": 10, "key2": "indubitably", "key3": "dataquest", 3: 5.6}

# a is initialized with those keys and values, so we can access them.
print(a["key1"])

# Another example
b = {4: "robin", 5: "bluebird", 6: "sparrow"}
print(b[4])
c = {7: "raven", 8: "goose", 9: "duck"}
d = {"morning": 9, "afternoon": 14, "evening": 19, "night": 23}
```

    10
    robin
    

###9: Testing if items are in a list

Check if 9 is in list2, and assign the result to c. Check if 8 is in list2, and assign the result to d. Check if -1 is in list2, and assign the result to e.


```python
# We can check if values are in lists using the in statement.
the_list = [10,60,-5,8]

# This is True because 10 is in the_list
print(10 in the_list)

# This is True because -5 is in the_list
print(-5 in the_list)

# This is False because 9 isn't in the_list
print(9 in the_list)

# We can assign the results of an in statement to a variable.
# Just like any other boolean.
a = 7 in the_list

list2 = [8, 5.6, 70, 800]
c = 9 in list2
d = 8 in list2
e = -1 in list2
```

    True
    True
    False
    

###10: More uses for the in statement

We can also use the in statement to check if a key is in a dictionary. We do this the same way we check if a value is in a list.

Check whether "jupiter" is in dict2 and assign the result to b. Check whether "earth" is in dict2 and assign the result to c.


```python
# We can check if a key is in a dictionary with the in statement.
the_dict = {"robin": "red", "cardinal": "red", "oriole": "orange", "lark": "blue"}

# This is True
print("robin" in the_dict)

# This is False
print("crow" in the_dict)

# We can also assign the boolean to a variable
a = "cardinal" in the_dict
print(a)

dict2 = {"mercury": 1, "venus": 2, "earth": 3, "mars": 4}
b = "jupiter" in dict2
c = "earth" in dict2
```

###11: Practicing with the else statement

The else statement is a powerful way to extend a basic if statement.

Write an if statement that prints "It's hot!" when the season is "Summer" Add an else statement to the if that prints "It might be hot!".


```python
# The code in an else statement will be executed if the if statement boolean is False.
# This will print "Not 7!"
a = 6
# a doesn't equal 7, so this is False.
if a == 7:
    print(a)
else:
    print("Not 7!")

# This will print "Nintendo is the best!"
video_game = "Mario"
# video_game is "Mario", so this is True
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
    

##12: Practicing with the else statement

We can combine some of the concepts we've already learned to count how many times items appear in a list using dictionaries. We'll loop over the list, and create a key for each item we want to count. We then increment the key whenever we see the element again. At the end, we have the count.

Count how many times each presidential last name appears in us_presidents. Assign the counts to us_president_counts.


```python
# We can count how many times items appear in a list using dictionaries.
pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]

# Create an empty dictionary
pantry_counts = {}
# Loop through the whole list
for item in pantry:
    # If the list item is already a key in the dictionary, then add 1 to the value of that key.
    # This is because we've seen the item again, so our count goes up.
    if item in pantry_counts:
        pantry_counts[item] = pantry_counts[item] + 1
    else:
        # If the item isn't already a key in the count dictionary, then add the key, and set the value to 1.
        # We set the value to 1 because we are seeing the item, so it's occured once already in the list.
        pantry_counts[item] = 1
print(pantry_counts)

us_presidents = ["Adams", "Bush", "Clinton", "Obama", "Harrison", "Taft", "Bush", "Adams", "Wilson", "Roosevelt", "Roosevelt"]

us_president_counts = {}
for president in us_presidents:
    if president in us_president_counts:
        us_president_counts[president] = us_president_counts[president] + 1
    else:
        us_president_counts[president] = 1
```

    {'orange': 2, 'tomato': 1, 'grape': 2, 'apple': 3, 'potato': 1}
    

##13: Counting the weather!

We now know how to count up how many times each type of weather occurs in the data!

The weather column, minus the header, has been loaded into the weather variable. Count up how many times each type of weather occurs. Store the counts in weather_counts.


```python
# Our weather column, minus the header, is assigned to the weather variable.
weather_counts = {}
for item in weather:
    if item in weather_counts:
        weather_counts[item] = weather_counts[item] + 1
    else:
        weather_counts[item] = 1

print(weather_counts)
```

    {'Fog': 125, 'Sunny': 210, 'Thunderstorm': 1, 'Rain': 25, 'Fog-Rain': 4}
    


```python

```
