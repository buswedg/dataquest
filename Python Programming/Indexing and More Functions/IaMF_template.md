

```python
from __future__ import print_function
```

#Python Programming

##Indexing and More Functions

###1: Writing a while loop

Before we dive into analyzing the data, we need to learn a few more things about loops.

A for loop isn't the only kind of loop.

One other type of loop is called a while loop.

It will keep running the loop as long as the condition specified is True.

    x = 2
    while x == 2:
        print(x)

The code above will run forever, because the loop will keep testing to see if x equals 2, and it will always return True.

You have to be careful not to get into an infinite loop, or a loop that runs forever, when you use a while loop.

    x = 2
    while x == 3:
        print(x)

The code above won't run at all, because x will never equal three.

####Instructions

Create a while loop that tests if b is greater than 5. If it is, the loop body should print b out, then subtract one from it.


```python
x = 3
# The loop body will execute three times.  Once when x == 3, once when x == 4, and once when x == 5.
# Then x < 6 will evaluate to False, and it will stop.
# 3, 4, and 5 will be printed out.
while x < 6:
    print("x:", x)
    # Using += is a shorter way of saying x = x + 1.  It will add one to x.
    x += 1

b = 10
while b > 5:
    print("b:", b)
    b -= 1
```

    x: 3
    x: 4
    x: 5
    b: 10
    b: 9
    b: 8
    b: 7
    b: 6
    

###2: Using the break keyword

The break keyword can be used to stop a loop early.

This can be useful in for loops when something happens inside the loop that makes us need to end it early.

    dog_available = False
    desired_dog = "Great Dane"
    available_dogs = ["Labrador", "Poodle", "Sheepdog", "Great Dane", "Pomeranian"]
    for dog in available_dogs:
        if dog == desired_dog:
            dog_available = True
            break

The code above will check to see if the desired_dog is available, and stop looping if it is found.

####Instructions

Let's say we want two "Bengal" tigers from available_tigers for our nature reserve.

Write a for loop that breaks after finding two, and increments tiger_count when it finds one.


```python
available_count = 0
desired_dog = "Great Dane"
available_dogs = ["Labrador", "Poodle", "Sheepdog", "Great Dane", "Pomeranian", "Great Dane", "Collie"]

# Let's say we are searching for two dogs of the same breed to adopt.
# We'll loop through the dogs.
for dog in available_dogs:
    # If our desired dog is found.
    if dog == desired_dog:
        # Increment the counter.
        available_count += 1
        # We only want two dogs, so we can stop searching after we find them.
        if available_count == 2:
            break

tiger_count = 0
desired_tiger = "Bengal"
available_tigers = ["Bengal", "Dressed up poodle", "Siberian", "Sumatran", "Bengal", "Housecat", "Hobbes"]
for tiger in available_tigers:
    if tiger == desired_tiger:
        tiger_count += 1
        if tiger_count == 2:
            break
```

###3: Finding a column number from a name

The data is in the flight_delays variable, and the column names are in the column_names variable.

So far, we've been numbering columns and selecting them using numbers, but it can get pretty painful to do this when there are more than 10 columns.

One fix for this is to refer to the columns by name, and write a function that returns a column number for a given column name.

####Instructions

Write a function that will get the column number from the column name.

Use it to get the column number for the "arr_delay" column and assign it to the arr_delay variable.

Use it to get the column number for the "weather_delay" column and assign it to the weather_delay variable.


```python
import csv

f = open("data/flight_delays.csv", "r")
reader = csv.reader(f)
flight_delays = list(reader)

column_names = flight_delays[0]
print("column_names:", column_names)
flight_delays = flight_delays[1:]
print("flight_delays[:3]:", flight_delays[:3])

# It's pretty easy to get a column name from a column number.
# The third column contains the carrier (same as the airline).
#print column_names[2]

def column_number_from_name(column_name):
    column_number = None
    for i, column in enumerate(column_names):
        if column == column_name:
            column_number = i
    return column_number

# Convert blank entries to zero.
for column in column_names:
    column_number = column_number_from_name(column)

    for row in flight_delays:
        if row[column_number] == "":
            row[column_number] = 0

arr_delay = column_number_from_name("arr_delay")
weather_delay = column_number_from_name("weather_delay")
```

    column_names: ['year', ' month', 'carrier', 'carrier_name', 'airport', 'airport_name', 'arr_flights', 'arr_del15', 'carrier_ct', ' weather_ct', 'nas_ct', 'security_ct', 'late_aircraft_ct', 'arr_cancelled', 'arr_diverted', 'arr_delay', ' carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay']
    flight_delays[:3]: [['2003', '6', 'AA', 'American Airlines Inc.', 'ATL', 'Atlanta, GA: Hartsfield-Jackson Atlanta International', '752', '186', '33.99', '27.82', '104.76', '1.9', '17.53', '5', '0', '8314', '1367', '1722', '3817', '139', '1269'], ['2003', '6', 'AA', 'American Airlines Inc.', 'BOS', 'Boston, MA: Logan International', '1266', '225', '69.43', '23.66', '83.93', '2.25', '45.73', '7', '0', '12139', '4201', '1783', '3067', '45', '3043'], ['2003', '6', 'AA', 'American Airlines Inc.', 'BWI', 'Baltimore, MD: Baltimore/Washington International Thurgood Marshall', '593', '101', '17.56', '20.49', '38.26', '0', '24.69', '1', '1', '5698', '1058', '1332', '1708', '0', '1600']]
    

###4: Using negative indexing

We can index lists with negative values.

Positive indexes start getting values from the beginning of a list, but negative indexes get values from the end of a list.

####Instructions

Use negative indexing to assign the third to last row in flight_delays to third_to_last.

Use negative slicing to assign the fourth, third, and second to last rows in flight_delays to end_slice.


```python
# Prints the last row in flight_delays.
print("flight_delays[-1]:", flight_delays[-1])

# Prints the second to last row in flight_delays.
print("flight_delays[-2]:", flight_delays[-2])

# Prints the third to last and second to last rows in flight_delays
# (remember that slicing only goes up to but not including the second number)
# This will get the rows at index -3 and -2.
print("flight_delays[-3:-1]", flight_delays[-3:-1])
third_to_last = flight_delays[-3]
end_slice = flight_delays[-4:-1]
```

    flight_delays[-1]: ['2015', '6', 'WN', 'Southwest Airlines Co.', 'PHL', 'Philadelphia, PA: Philadelphia International', '701', '221', '63.42', '18.38', '61.04', '0', '78.16', '11', '7', '14435', '3746', '1716', '3508', '0', '5465']
    flight_delays[-2]: ['2015', '6', 'WN', 'Southwest Airlines Co.', 'PDX', 'Portland, OR: Portland International', '1094', '295', '98.44', '2.38', '22.18', '0', '171.99', '3', '0', '14720', '4737', '164', '741', '0', '9078']
    flight_delays[-3:-1] [['2015', '6', 'WN', 'Southwest Airlines Co.', 'TPA', 'Tampa, FL: Tampa International', '2412', '571', '198.35', '16.23', '71.2', '1.13', '284.09', '33', '11', '34449', '12385', '1452', '2823', '50', '17739'], ['2015', '6', 'WN', 'Southwest Airlines Co.', 'PDX', 'Portland, OR: Portland International', '1094', '295', '98.44', '2.38', '22.18', '0', '171.99', '3', '0', '14720', '4737', '164', '741', '0', '9078']]
    

###5: Indexing up to the end or from the beginning

When we take a slice, we can leave one of the numbers blank.

####Instructions

Assign the first 10 rows of flight_delays to first_ten_rows.

Assign the last 10 rows of flight_delays to last_ten_rows.


```python
# This code will get the rows at index 0, 1, 2, 3, and 4.
first_five_rows = flight_delays[:5]

# This will get the rows at index -5, -4, -3, -2, and -1
last_five_rows = flight_delays[-5:]

first_ten_rows = flight_delays[:10]
last_ten_rows = flight_delays[-10:]
```

###6: Finding the percentage of delayed flights

We can now find the percentage of flights that are delayed.

####Instructions

Sum together the values in the "arr_del15" column. This is the total number of arriving flights in each airport that were delayed more than 15 minutes.

Then, divide the number of delayed flights by total_arriving_flights. Assign the result to delayed_percentage.


```python
def column_number_from_name(column_name):
    column_number = None
    for i, column in enumerate(column_names):
        if column == column_name:
            column_number = i
    return column_number

# Get the column number of the arr_flight column.
# This column counts the total number of arriving flights for a carrier in a given airport.
arr_flights_column = column_number_from_name("arr_flights")
delayed_flights_column = column_number_from_name("arr_del15")

# Extract all of the values in the column using a list comprehension.
# We need to convert the values to float because they are strings initially.
arr_flights = [float(row[arr_flights_column]) for row in flight_delays]

# Now we can use the sum() function to add together all of the values.
total_arriving_flights = sum(arr_flights)
delayed_flights = [float(row[delayed_flights_column]) for row in flight_delays]
delayed_percentage = sum(delayed_flights) / total_arriving_flights

print("total_arriving_flights:", total_arriving_flights)
print("delayed_percentage:", delayed_percentage)
```

    total_arriving_flights: 50196030.0
    delayed_percentage: 0.20345150801766593
    

###7: Finding the average delay time

The total amount of time (in minutes) that planes for a given carrier were delayed at a given airport is in "arr_delay" column.

####Instructions

Find the sum of the "arr_delay" column.

Then, divide it by the sum of the "arr_del15" column to get the average number of minutes a plane was delayed.

Assign the result to average_delay_time.


```python
def column_number_from_name(column_name):
    column_number = None
    for i, column in enumerate(column_names):
        if column == column_name:
            column_number = i
    return column_number

delayed_flights_column = column_number_from_name("arr_del15")
delay_time_column = column_number_from_name("arr_delay")

average_delay_time = None
delayed_flights_column = column_number_from_name("arr_del15")
delayed_flights = [float(row[delayed_flights_column]) for row in flight_delays]

delay_time_column = column_number_from_name("arr_delay")
delay_time = [float(row[delay_time_column]) for row in flight_delays]
average_delay_time = sum(delay_time) / sum(delayed_flights)

print("average_delay_time:", average_delay_time)
```

    average_delay_time: 56.47049515405596
    

###8: Making a function to calculate the delay

There are a few more columns that we'll need to calculate the sum of, and its getting a bit tedious to keep typing the same few commands.

Let's make a function to save ourselves time.

####Instructions

Make a function that takes a column name as input, and returns the column sum.

Then use the function to take the sum of the "weather_delay" column, and divide it by the sum of the "arr_del15" column.

Assign the result to average_weather_delay_time.


```python
def column_number_from_name(column_name):
    column_number = None
    for i, column in enumerate(column_names):
        if column == column_name:
            column_number = i
    return column_number

def calculate_column_sum(column_name):
    column_number = column_number_from_name(column_name)
    column = [float(row[column_number]) for row in flight_delays]
    column_total = sum(column)
    return column_total

weather_delay_column = column_number_from_name("weather_delay")

average_weather_delay_time = calculate_column_sum("weather_delay") / calculate_column_sum("arr_del15")
print("average_weather_delay_time:", average_weather_delay_time)
```

    average_weather_delay_time: 2.6141094533754754
    

###9: Named arguments to functions

We can use named keyword arguments to pass input to a function.

####Instructions

Fix the statements above so the code runs properly.

The first statement should divide 5 by 20, and the second should divide 100 by 30.


```python
def divide(x, y):
    return float(x)/y

# Use positional arguments, which will implicitly pass 10 to x and 5 to y.
print("divide(10,5):", divide(10,5))

# Use named arguments, which will pass the values to the named variable.
print("divide(y=10, x=5):", divide(y=10, x=5))

# If we use named arguments, the order doesn't matter
print("divide(x=5, y=10):", divide(x=5, y=10))

# But we can't have any positional arguments after we use a named argument
print("divide(y=20, x=5):", divide(y=20, x=5))
print("divide(x=100, y=30):", divide(x=100, y=30))
```

    divide(10,5): 2.0
    divide(y=10, x=5): 0.5
    divide(x=5, y=10): 0.5
    divide(y=20, x=5): 0.25
    divide(x=100, y=30): 3.3333333333333335
    

###10: Optional arguments to a function

We can also specify default values in a function definition that make the arguments optional.

You can't have an optional argument before a non-optional argument, just like named keywords.

####Instructions

Fix the last two statements so that they work properly.

The first statement should multiply 4 * 3 * 1

The second statement should multiply 3 * 2 * 3


```python
def multiply(a, b=2, c=1):
    return a * b * c

# This will multiply 5 * 2 * 1
print("multiply(5):", multiply(5))

# This will multiply 6 * 4 * 1
print("multiply(5, 4):", multiply(5, 4))

# This will multiply 5 * 2 * 1
print("multiply(a=5):", multiply(a=5))

# This will multiply 6 * 2 * 4
print("multiply(a=6, c=4):", multiply(a=6, c=4))

# Invalid, because we didn't fill the a variable, which doesn't have a default.
print("multiply(a=4, b=3):", multiply(a=4, b=3))

# Invalid, because we didn't fill the a variable.
print("multiply(a=3, c=3):", multiply(a=3, c=3))
```

    multiply(5): 10
    multiply(5, 4): 20
    multiply(a=5): 10
    multiply(a=6, c=4): 48
    multiply(a=4, b=3): 12
    multiply(a=3, c=3): 18
    

###11: Finding delay by carrier

Now that we know about optional and keyword arguments, let's make a function that can find the average delay for a given airport.

####Instructions

Fill in the rest of the find_average_delay function.

You can calculate average delay time by dividing the "arr_delay" column by the "arr_del15" column.

The "carrier" column can be used to subset by carrier.

Then use the function to assign the average delay time to average_delay_time.

Use the function again to assign the average delay time on carrier "AA" to american_airlines_average_delay_time.


```python
def column_number_from_name(column_name):
    column_number = None
    for i, column in enumerate(column_names):
        if column == column_name:
            column_number = i
    return column_number

def find_average_delay(carrier_name=None):
    total_delayed_flights = 0
    total_delay_time = 0
    delay_time_column = column_number_from_name("arr_delay")
    delay_number_column = column_number_from_name("arr_del15")
    carrier_column = column_number_from_name("carrier")
    for row in flight_delays:
        if carrier_name is None or row[carrier_column] == carrier_name:
            total_delayed_flights += float(row[delay_number_column])
            total_delay_time += float(row[delay_time_column])
    return total_delay_time / total_delayed_flights

average_delay_time = find_average_delay()
american_airlines_average_delay_time = find_average_delay("AA")

print("average_delay_time:", average_delay_time)
print("american_airlines_average_delay_time:", american_airlines_average_delay_time)
```

    average_delay_time: 56.47049515405596
    american_airlines_average_delay_time: 59.362134469731
    

###12: Finding average delay for each carrier

Now that we have a function to find the delay for a given carrier, we can find the delays for each carrier.

####Instructions

Create a list of the unique carrier names.

Then call the find_average_delay function for each carrier.

Set the carriers as keys in the delays_by_carrier dictionary, with the values being the average delay times.


```python
def column_number_from_name(column_name):
    column_number = None
    for i, column in enumerate(column_names):
        if column == column_name:
            column_number = i
    return column_number

def find_average_delay(carrier_name=None):
    total_delayed_flights = 0
    total_delay_time = 0
    delay_time_column = column_number_from_name("arr_delay")
    delay_number_column = column_number_from_name("arr_del15")
    carrier_column = column_number_from_name("carrier")
    for row in flight_delays:
        if carrier_name is None or row[carrier_column] == carrier_name:
            total_delayed_flights += float(row[delay_number_column])
            total_delay_time += float(row[delay_time_column])
    return total_delay_time / total_delayed_flights

delays_by_carrier = {}
carrier_column = column_number_from_name("carrier")
carriers = [row[carrier_column] for row in flight_delays]
unique_carriers = list(set(carriers))

for carrier in unique_carriers:
    delays_by_carrier[carrier] = find_average_delay(carrier)

print("delays_by_carrier:", delays_by_carrier)
```

    delays_by_carrier: {'US': 48.78565400843882, 'DL': 53.76891443330582, 'HP': 45.270835956980584, 'F9': 50.097403085159414, 'B6': 62.84498670040223, 'RU': 58.148919452958474, 'FL': 57.38075660630524, 'AA': 59.362134469731, '9E': 61.099084755164306, 'UA': 59.37946761830199, 'OH': 56.831616212878096, 'MQ': 61.785425161954315, 'YV': 65.34052644059759, 'XE': 66.81241586890181, 'HA': 50.89347014925373, 'AQ': 50.468879668049794, 'NK': 67.34425011817139, 'WN': 48.97373921973743, 'TZ': 58.65738720958416, 'VX': 66.96449918493026, 'DH': 63.23939241165086, 'AS': 50.16532318760089, 'EV': 65.13085231843156, 'CO': 56.87818765091253, 'OO': 57.48481293103578, 'NW': 49.824358059491665}
    
