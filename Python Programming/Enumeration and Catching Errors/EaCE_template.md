

```python
from __future__ import print_function
```

#Python Programming

##Enumeration and Catching Errors

###1: Find the different genders

There's an invalid value in the gender column that isn't "M" or "F".

Our first task is going to be getting rid of the invalid values and assigning the right gender.

In order to do that, we first need to figure out what all of the unique values in the "gender" column are.

The value that isn't "M" or "F" will be the invalid value, and we need to replace it.


```python
import yaml
import io

#with open('data/legislators.yaml', 'r') as f:
#    doc = yaml.load(f)
with io.open("data/legislators.yaml", encoding="mac_roman") as f:
    legislate_raw = yaml.load(f)

print("legislate_raw[0]:", legislate_raw[0])
```

    legislate_raw[0]: {'name': {'last': 'Bassett', 'first': 'Richard'}, 'id': {'bioguide': 'B000226', 'govtrack': 401222, 'icpsr': 507}, 'terms': [{'party': 'Anti-Administration', 'type': 'sen', 'state': 'DE', 'end': '1793-03-03', 'start': '1789-03-04', 'class': 2}], 'bio': {'gender': 'M', 'birthday': '1745-04-02'}}
    


```python
legislators = []
count = 0
for row in legislate_raw:
    first = legislate_raw[count]["name"]["first"]
    last = legislate_raw[count]["name"]["last"]
    term = legislate_raw[count]["terms"][0]["start"]
    gender = legislate_raw[count]["bio"]["gender"]
    ttype = legislate_raw[count]["terms"][0]["type"]
    state = legislate_raw[count]["terms"][0]["state"]
    try:
        party = legislate_raw[count]["terms"][0]["party"]
    except KeyError:
        party = ""
    legislators.append([first, last, term, gender, ttype, state, party])
    count += 1
    
print("legislators[0]:", legislators[0])
```

    legislators[0]: ['Richard', 'Bassett', '1789-03-04', 'M', 'sen', 'DE', 'Anti-Administration']
    

####Instructions

Loop through the rows in legislators, and extract the gender column (fourth column)

Append the genders to genders_list.

Then turn genders_list into a set, and assign it to unique_genders

Finally, convert unique_genders back into a list, and assign it to unique_genders_list.


```python
# We can use the set() function to convert lists into sets.
# A set is a data type, just like a list, but it only contains each value once.
car_makers = ["Ford", "Volvo", "Audi", "Ford", "Volvo"]

# Volvo and ford are duplicates
#print(car_makers)

# Converting to a set
unique_car_makers = set(car_makers)
#print(unique_car_makers)

# We can't index sets, so we need to convert back into a list first.
unique_cars_list = list(unique_car_makers)
#print(unique_cars_list[0])

genders_list = []
unique_genders = set()
unique_genders_list = []
for row in legislators:
    genders_list.append(row[3])
    
unique_genders = set(genders_list)
unique_genders_list = list(unique_genders)

print("unique_genders:", unique_genders)
print("unique_genders_list:", unique_genders_list)
```

    unique_genders: {'F', 'M'}
    unique_genders_list: ['F', 'M']
    

###2: Replacing genders

Now we know that the invalid gender value is and empty string -- "".

Sadly, most US Congresspeople (and all prior to 1917) have been male.

Because it's going to make this exercise easier, we'll just assume that anyone with a missing gender is Male.

At some point later on, we'll be able to predict whether a name is male or female, and we'll revisit this exercise.

####Instructions

Loop through the rows in legislators and replace any gender values of "" with "M".


```python
# We can replace values in a list with a for loop.
# All of the 0 values in the first column here will be replaced with a 5.
lolists = [[0,5,10], [5,20,30], [0,70,80]]
for row in lolists:
    if row[0] == 0:
        row[0] = 5

# We can see the new list.
print("lolists:", lolists)

for row in legislators:
    if row[3] == "":
        row[3] = "M"
```

    lolists: [[5, 5, 10], [5, 20, 30], [5, 70, 80]]
    

###3: Parsing birth years

We want to find out what names are most common for senators, but we also want to be able to filter on date if we want to.

Naming someone Effingham was somewhat popular in the 1820's, but may not fly in the modern era.

So we need some way to determine if a Senator was born recently, and we need a way to only select those names if we want to.

We have a birthday column, so we should just be able to parse them out.

Birthdays are stored in the "year-month-day" format, such as "1820-05-02".

We should be able to split the birthday on "-", and grab the first part (the year).

####Instructions

Loop through the rows in legislators

Inside the loop, get the birthday column from the row, and split the birthday.

After splitting the birthday, get the birth year, and append it to birth_years

At the end, birth_years will contain the birth years of all the Congresspeople in the data.


```python
birth_years = []
for row in legislators:
    split_birthday = row[2].split("-")
    birth_year = split_birthday[0]
    birth_years.append(birth_year)

print("birth_years[:5]:", birth_years[:5])
```

    birth_years[:5]: ['1789', '1789', '1789', '1789', '1789']
    

###4: Practice with enumerate

Let's apply the enumerate function a bit before moving forward.

####Instructions

Use a for loop to enumerate the ships list.

In the body of the loop, print the ship at the current index, then the car at the current index.

Make sure you have two separate print statements.


```python
dogs = ["labrador", "poodle", "collie"]
cats = ["siamese", "persian", "somali"]
# Enumerate the dogs list, and print the values.
for i, dog in enumerate(dogs):
    # Will print the dog at the current loop iteration.
    print("dog:", dog)
    # This will equal dog.  Prints the dog at index i.
    print("dogs[i]:", dogs[i])
    # Print the cat at index i.
    print("cats[i]:", cats[i])

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]
for i, ship in enumerate(ships):
    print("ship:", ship)
    print("cars[i]:", cars[i])
```

    dog: labrador
    dogs[i]: labrador
    cats[i]: siamese
    dog: poodle
    dogs[i]: poodle
    cats[i]: persian
    dog: collie
    dogs[i]: collie
    cats[i]: somali
    ship: Andrea Doria
    cars[i]: Ford Edsel
    ship: Titanic
    cars[i]: Ford Pinto
    ship: Lusitania
    cars[i]: Yugo
    


```python
lolists = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]
for i, row in enumerate(lolists):
    row.append(trees[i])

# Our list now has a new column containing the values from trees.
print("lolists:", lolists)

# Legislators and birth_years have both been loaded in.
for i, row in enumerate(legislators):
    row.append(birth_years[i])
```

    lolists: [['apple', 'monkey', 'cedar'], ['orange', 'dog', 'maple'], ['banana', 'cat', 'fig']]
    

###5: Practice with list comprehensions

Let's practice a bit with list comprehensions.

####Instructions

Double all of the prices in apple_price, and assign the resulting list to apple_price_doubled.

Subtract 100 from all of the prices in apple_price, and assign the resulting list to apple_price_lowered.


```python
# Define a list of lists
data = [["tiger", "lion"], ["duck", "goose"], ["cardinal", "bluebird"]]

# Extract the first column from the list
first_column = [row[0] for row in data]

apple_price = [100, 101, 102, 105]
apple_price_doubled = [price*2 for price in apple_price]
apple_price_lowered = [price-100 for price in apple_price]
```

###6: Convert birth years to integers

We want to find the most common Senator names after a certain date -- let's say 1940.

Remember that the birth years are now the last column in the legislators data.

There's one problem -- the birth years are stored as strings, but we need them to be integers so we can use booleans to pick only the ones that are greater than 1940.

We can't use booleans to compare a string value to the integer 1940 -- the comparison wouldn't make any sense.

Luckily, we can convert strings to ints using the int() function.

####Instructions

We're stuck for now, but we'll learn a concept next that will help us out.

Just hit "Next" to move on for now.


```python
for row in legislators:
    row[7] = int(row[7])

# Hmm, but the above code fails.
# It fails because there is a value in the column that can't be converted to an int.
# Remember how some genders were missing?  It also looks like some birthdays were missing, which is giving us invalid values in the birth years column.
```

###7: Practice with try/except

Let's practice with try/except blocks a bit to get a better handle on them.

####Instructions

Use try/except statements to parse another_invalid_int and another_valid_int.

Assign 0 to another_invalid_int in the except block.

At the end, another_valid_int will be parsed properly, and another_invalid_int will be 0.


```python
# Cannot be parsed into an int with the int() function.
invalid_int = ""

# Can be parsed into an int.
valid_int = "10"

# Parse the valid int.
try:
    valid_int = int(valid_int)
except Exception:
    # This code is never run, because there is no error parsing valid_int into an integer.
    valid_int = 0

# Try to parse the invalid int.
try:
    invalid_int = int(invalid_int)
except Exception:
    # The parsing fails, so we end up here.
    # The code here will be run, and will assign 0 to invalid_int.
    invalid_int = 0

print("valid_int:", valid_int)
print("invalid_int:", invalid_int)

another_invalid_int = "Oregon"
another_valid_int = "1000"
try:
    another_invalid_int = int(another_invalid_int)
except Exception:
    another_invalid_int = 0

try:
    another_valid_int = int(another_valid_int)
except Exception:
    another_valid_int = 0
```

    valid_int: 10
    invalid_int: 0
    

###8: The pass keyword

The pass keyword enables us to skip adding code into the body of a statement when we don't want to.

    valid_int="5"
    try:
        valid_int=int(valid_int)
    except Exception:

The code above will fail, because whenever we have a colon in Python, we are saying that we will have a line or lines below it, indented 4 spaces.

We can't have zero lines inside the body of any statement ending with a colon (for loop, function definition, if statement, and so on). Comments don't count as lines for this purpose.

But sometimes, such as with the except statement above, we really don't want to do anything in the body.

This is where the pass keyword comes in handy.

    valid_int="5"
    try:
        valid_int=int(valid_int)
    except Exception:
        pass

The code above will work, because the pass keyword is a line in the body of the except statement.

However, pass is a special keyword that tells Python to do nothing and keep going.

####Instructions

Use a try/except block to parse valid_int into an integer.

Use the pass keyword inside the except block.


```python
invalid_int = ""
try:
    # This parsing will fail
    invalid_int = int(invalid_int)
except Exception:
    # Nothing will happen in the body of the except statement, because we are passing.
    pass

# invalid_int still has the same value.
print("invalid_int:", invalid_int)

# We can also use the pass statement with for loops.
# (although it's less useful in this example).
a = [1,4,5]
for i in a:
    pass

# And if statements.
if 10 > 5:
    pass

# We can use the pass keyword inside the body of any statement that ends with a colon.
valid_int = "10"
try:
    valid_int = int(valid_int)
except Exception:
    pass
```

    invalid_int: 
    

###9: Convert birth years to integers

Now that we know about the try/except statements, we can convert the birth year column (column 8) to integers.

####Instructions

Loop over the rows in legislators, and convert the values in the birth year column to integers.

In cases where parsing fails, assign 0 as the value.


```python
# The legislators variable has been loaded.
for row in legislators:
    try:
        row[7] = int(row[7])
    except Exception:
        row[7] = 0
```

###10: Fill in years without a value

Great, we're very close to being able to find the most common name!

The final hurdle is dealing with the cases where the birth years are 0

We'll need to fill these in to make our results more accurate.

The rows in legislators are listed in rough chronological order, so we can fill in birth years that are 0 with the birth year of the previous row.

This isn't perfect, but we don't have a much better way of going about this.

####Instructions

Loop through legislators, and replace any values in the birth_year column that are 0 with the previous value.


```python
data = [[1,1],[0,5],[10,7]]
last_value = 0

# There are some holes in this code -- it won't work properly if the first birth year is 0, for example, but its fine for now.
# It keeps track of the last value in the column in the last_value variable.
# If it finds an item that equals 0, it replaces the value with the last value.
for row in data:
    # Check if the item is 0.
    if row[0] == 0:
        # If it is, replace it with the last value.
        row[0] = last_value
    # Set last value equal to the item -- we need to do this in order to keep track of what the previous value was, so we can use it for replacement.
    last_value = row[0]

# The 0 value in the second row, first column has been replaced with a 1.
print("data:", data)

last_value = 1
for row in legislators:
    if row[7] == 0:
        row[7] = last_value
    last_value = row[7]
```

    data: [[1, 1], [1, 5], [10, 7]]
    

###11: Counting up the female names

We now know enough to count up the most popular names!

We'll start with female names, and then do male names next.

Only names from congresspeople born after 1940 will be counted.

We'll be counting using a dictionary -- we've done this before, but a quick refresher is below.

####Instructions

Count up how many times each female name occurs in legislators. First name is the second column.

You'll need to make sure that gender (fourth column) equals "F", and that birth year (eighth column) is greater than 1940.

Store the first name key and the counts in the female_name_counts dictionary.

You'll need to use nested if statements to first check if gender and birth year are valid, and then to check if the first name is in female_name_counts.


```python
names = ["Jim", "Bob", "Bob", "JimBob", "Joe", "Jim"]
name_counts = {}
for name in names:
    if name in name_counts:
        name_counts[name] = name_counts[name] + 1
    else:
        name_counts[name] = 1

female_name_counts = {}
for row in legislators:
    if row[3] == "F" and row[7] > 1940:
        if row[1] in female_name_counts:
            female_name_counts[row[1]] = female_name_counts[row[1]] + 1
        else:
            female_name_counts[row[1]] = 1
```

###12: Practicing with the None type

Now that we know about the None type, let's practice with it a bit.

####Instructions

Check whether c equals None, and assign the result to c_none.

Check whether d equals None, and assign the result to d_none.


```python
# Set a variable equal to the None type
a = None
# A normal variable
b = 1

# This is True
print("a is None:", a is None)
# And this is False
print("b is None:", b is None)

# a is of the None type
print("type(a):", type(a))

# Assigns whether a equals None to a_none
a_none = a is None
# Evaluates to True
print("a_none:", a_none)

c = None
d = "Bamboo"
c_none = c is None
d_none = d is None
```

    a is None: True
    b is None: False
    type(a): <class 'NoneType'>
    a_none: True
    

###13: Finding maximums with the None type

We know how to find the maximum value in a list or dictionary.

    max_val = 0
    data = [50,80,100,0,40]
    for i in data:
        if i > max_val:
            max_val = i
    print(max_val)

The code above will find the maximum value in the data.

But we have to initialize max_val first to a number.

    max_val = 0
    data = [-10, -20, -50, -100]
    for i in data:
        if i > max_val:
            max_val = i
    print(max_val)

In the above example, we would get an incorrect final value for max_val, because we didn't set the initial value well (0 is greater than any value in data, so it's never changed.)

Luckily, the None type to help us out.

####Instructions

Use a for loop to set min_val equal to the smallest value in income.


```python
max_val = None
data = [-10, -20, -50, -100]
for i in data:
    # If max_val equals None, or i is greater than max_val, then set max_val equal to i.
    # This ensures that no matter how small the values in data are, max_val will always get changed to a value in the list.
    # If you are checking if a value equals None and you are using it with and or or, then the None check always needs to come first.
    if max_val is None or i > max_val:
        max_val = i

min_val = None
income = [100,700,100,50,100,40,56,31,765,1200,1400,32,6412,987]
for i in income:
    if min_val is None or i < min_val:
        min_val = i
```

###14: Finding how many times the top female names occur

We now have a dictionary where the keys are first names, and the values are counts of how many times female congresspeople born after 1940 had that name.

We need to go from here to a name or names that are the most popular.

First, let's find out the highest value (how many times the most-occuring name occurred).

This will let us extract the name or names that occurred the most.

####Instructions

Loop through the keys in female_name_counts, and get the value associated with the key.

Assign the value to max_value if it is larger, or if max_value is None.

At the end of the loop, max_value will be the largest value in the dictionary.


```python
# female_name_counts has been loaded in.
max_value = None
for k in female_name_counts:
    if max_value is None or female_name_counts[k] > max_value:
        max_value = female_name_counts[k]
```

###15: Finding the female names that occur the most

So we now know that the names that occur the most occur 2 times.

All we have to do now is loop through the dictionary again and extract all the names that occur twice.

####Instructions

Loop through the keys in female_name_counts.

If any value equals 2, append the key to top_female_names.

At the end, top_female_names will be a list of the most occurring female congressperson names.


```python
# female_name_counts has been loaded in.
top_female_names = []
for k in female_name_counts:
    if female_name_counts[k] == 2:
        top_female_names.append(k)
```

###16: Practice with the items method

Let's practice a bit with the .items() method

####Instructions

Use the .items() method along with a for loop to loop through plant_types.

Inside the loop, print the key, and then the value.


```python
animal_types = {"robin": "bird", "pug": "dog", "osprey": "bird"}

# The .items method lets us access a dictionary key and value in a loop.
for key,value in animal_types.items():
    print("key:", key)
    print("value:", value)
    # This is equal to the value.
    print("animal_types[key]:", animal_types[key])

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for k,v in plant_types.items():
    print("k:", k)
    print("v:", v)
```

    key: pug
    value: dog
    animal_types[key]: dog
    key: osprey
    value: bird
    animal_types[key]: bird
    key: robin
    value: bird
    animal_types[key]: bird
    k: maple
    v: tree
    k: orchid
    v: flower
    k: cedar
    v: tree
    

###17: Finding the male names that occur the most

Let's follow the same process we did with the female names to find a list of the most common male names.

The .items() method may make the task quicker.

####Instructions

Loop through legislators, and count up how much each name where the gender column equals "M" and the birth year is after 1940 occurs. Store the results in a dictionary.

Then find the highest value in that dictionary.

Finally, loop through the dictionary and append any keys where the value equals the highest value to top_male_names.


```python
# legislators has been loaded in.
top_male_names = []
male_name_counts = {}
for row in legislators:
    if row[3] == "M" and row[7] > 1940:
        if row[1] in male_name_counts:
            male_name_counts[row[1]] = male_name_counts[row[1]] + 1
        else:
            male_name_counts[row[1]] = 1

highest_value = None
for k,v in male_name_counts.items():
    if highest_value is None or v > highest_value:
        highest_value = v

for k,v in male_name_counts.items():
    if v == highest_value:
        top_male_names.append(k)
```
