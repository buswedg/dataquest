
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Python Programming

# ##Modules and Classes

# ###1: Importing and using modules

# A module is a piece of code that someone else has already written.
# 
# We can use modules to do common tasks -- they save us from having to write the code ourselves.
# 
# To get access to a module, we have to use the import statement to import it.
# 
# Once we import it, we can access the functions in a module using dot notation.

# ####Instructions

# Assign the square root of 16 to a.
# 
# Assign the ceiling of 111.3 to b.
# 
# Assign the floor of 89.9 to c.

# In[2]:

import math

# The sqrt function in the math module will take the square root of a number.
print("math.sqrt(9):", math.sqrt(9))

# The ceil function will round a number up.
print("math.ceil(8.1):", math.ceil(8.1))

# And the floor function will round a number down.
print("math.floor(11.9):", math.floor(11.9))

a = math.sqrt(16)
print("a:", a)

b = math.ceil(111.3)
print("b:", b)

c = math.floor(89.9)
print("c:", c)


# ###2: More about modules

# We can also access other properties in modules.
# 
# Some modules have variables defined inside them.
# 
# Just like with functions, we can access them with the dot notation.
# 
# Imagine a module as a street, with houses on that street being functions and variables.
# 
# If you wanted to tell someone how to get to a house, you would first tell them how to get to the street.
# 
# Then you would tell them to turn onto the street and stop at the house.
# 
# Python is the same way -- it has to know how to get to a a function or variable before it can find it.
# 
# If the function or variable is inside a module, Python needs directions to be told about the module first.

# ####Instructions

# Assign the square root of pi to a.
# 
# Assign the ceiling of pi to b.
# 
# Assign the floor of pi to c.

# In[3]:

import math

# Multiply pi by 2.
print("math.pi * 2:", math.pi * 2)

a = math.sqrt(math.pi)
print("a:", a)

b = math.ceil(math.pi)
print("b:", b)

c = math.floor(math.pi)
print("c:", c)


# ###3: An easier way to read in csv files!

# You may be happy to know that there is a much easier way to load csv files : the csv module!

# ####Instructions

# Read in all of the data from "nfl.csv" into a List variable named nfl using the csv module.

# In[4]:

import csv

f = open("data/nfl.csv", "r")
csvreader = csv.reader(f)
nfl = list(csvreader)

print("nfl[:5]:", nfl[:5])


# ###4: Counting how many times a team won

# Now that we can load in the .csv file, let's count up the wins for a team.
# 
# Each row is the result of a single game.
# 
# The first column is the year, the second column is the week (The NFL regular season is 17 weeks, and games are played each week), the third column is the winning team, and the last column is the losing team.

# ####Instructions

# Loop through the nfl data.
# 
# Count up how many games the "New England Patriots" won from 2009-2013.
# 
# Assign the count to patriots_wins. The count should be an integer.

# In[5]:

# The nfl data is loaded into the nfl variable.
patriots_wins = 0
for row in nfl:
    if row[2] == "New England Patriots":
        patriots_wins += 1


# ###5: Making a function to count wins

# Great, we can count up the wins for a single team.
# 
# Now let's make a function to count wins for any team we want.

# ####Instructions

# Write a function called nfl_wins that will take a team name, in the form of a string, as input.
# 
# The function should output the number of wins the team had from 2009-2013, as an integer.
# 
# Use the function to assign the number of wins by the "Dallas Cowboys" to cowboys_wins.
# 
# Use the function to assign the number of wins by the "Atlanta Falcons" to falcons_wins.

# In[6]:

# The nfl data is loaded into the nfl variable.
def nfl_wins(team):
    count = 0
    for row in nfl:
        if row[2] == team:
            count = count + 1
    return count

cowboys_wins = nfl_wins("Dallas Cowboys")
print("cowboys_wins:", cowboys_wins)

falcons_wins = nfl_wins("Atlanta Falcons")
print("falcons_wins:", falcons_wins)


# ###6: Using boolean statements with the and keyword

# We can use the and keyword in a boolean to check if multiple conditions are True.
# 
#     a = 5
#     b = 10
#     a == 5 and b == 10
# 
# will evaluate to True.
# 
# But
# 
#     a = 5
#     b = 10
#     a == 5 and b == 11
# 
# will evaluate to False. and statements only evaluate to True if all of their elements evaluate to True individually.

# ####Instructions

# Assign a boolean that uses the and keyword and evaluates to True to a.
# 
# Assign a boolean that uses the and keyword and evaluates to False to b.

# In[7]:

its_raining = "Yes"
its_snowing = "No"

# Each statement is evaluated separately.
# If either of them is False on its own, then the whole statement is False.
logic1 = its_raining == "Yes" and its_snowing == "Yes"
print("logic1:", logic1)

# If both evaluate to True, then the whole statement is True.
logic2 = its_raining == "Yes" and its_snowing == "No"
print("logic2:", logic2)

c = 10
d = 50
a = c == 10 and d == 50
b = c == 11 and d == 50


# ###7: Using boolean statements with the or keyword

# We can use the or keyword in a boolean to check if any condition is True.
# 
#     a = 5
#     b = 10
#     a == 5 or b == 5
# 
# will evaluate to True because a == 5.
# 
# But
# 
#     a = 5
#     b = 10
#     a == 6 or b == 11
# 
# will evaluate to False because both statements are False. or statements evaluate to True if any of their elements evaluate to True individually.

# ####Instructions

# Assign a boolean that uses the or keyword and evaluates to True to a.
# 
# Assign a boolean that uses the or keyword and evaluates to False to b.

# In[8]:

current_president = "Barack Obama"

# Each statement is evaluated separately.
# If either of them is True on its own, then the statement is True.
logic1 = current_president == "Barack Obama" or current_president == "George Bush"
print("logic1:", logic1)

# If all of the statements evaluate to False, then the statement is False.
logic2 = current_president == "Eminem" or current_president == "Kanye West"
print("logic2:", logic2)

c = 10
d = 50
a = c == 10 or d == 50
b = c == 11 or d == 55


# ###8: Counting wins in a given year

# Let's make a function to count up the wins for a team for a single year.

# ####Instructions

# Modify the nfl_wins function so it will take a team name, in the form of a string, and a year, in the form of an string, as input.
# 
# The only valid years are "2009", "2010", "2011", "2012", and "2013".
# 
# Remember that the years are stored as strings in the data, so we also have to use strings for consistency.
# 
# The function should output the number of wins the team had in the given year, as an integer.
# 
# Use the function to assign the number of wins by the "Cleveland Browns" in 2010 to browns_2010_wins.
# 
# Use the function to assign the number of wins by the "Philadelphia Eagles" in 2011 to eagles_2011_wins.

# In[9]:

# Modify this function to also take a year as input, and returns the wins by the team in the year.
def nfl_wins(team):
    count = 0
    for row in nfl:
        # We need to ensure that we only increment the count when the row pertains to the year we want.
        if row[2] == team:
            count = count + 1
    return count

def nfl_wins_in_a_year(team, year):
    count = 0
    for row in nfl:
        if row[2] == team and row[0] == year:
            count = count + 1
    return count

browns_2010_wins = nfl_wins_in_a_year("Cleveland Browns", "2010")
print("browns_2010_wins:", browns_2010_wins)

eagles_2011_wins = nfl_wins_in_a_year("Philadelphia Eagles", "2011")
print("eagles_2011_wins:", eagles_2011_wins)


# ###9: Counting wins by year

# Now that we can count wins for a single team in a given year, we can make a function that counts up wins for a team by year.
# 
# We'll use the function we worked with earlier to count wins by a team in a given year.

# ####Instructions

# Make a new function that calls on the nfl_wins_by_year function to compute wins for each year from 2009 - 2013.
# 
# Valid years are "2009", "2010", "2011", "2012", and "2013".
# 
# The function should return a dictionary with the years as keys, and the number of wins in each year as values.
# 
# Use the function to assign the number of wins by year by the "Miami Dolphins" to dolphins_wins_by_year.
# 
# Use the function to assign the number of wins by year by the "San Diego Chargers" to chargers_wins_by_year.

# In[10]:

# We'll need to create a new function to returns wins for each year.
# It will call nfl_wins_by_year as part of its computations.
def nfl_wins_in_a_year(team, year):
    count = 0
    for row in nfl:
        if row[2] == team and row[0] == year:
            count = count + 1
    return count

def nfl_wins_by_year(team):
    win_dict = {}
    for year in ["2009", "2010", "2011", "2012", "2013"]:
        win_dict[year] = nfl_wins_in_a_year(team, year)
    return win_dict

dolphins_wins_by_year = nfl_wins_by_year("Miami Dolphins")
print("dolphins_wins_by_year:", dolphins_wins_by_year)

chargers_wins_by_year = nfl_wins_by_year("San Diego Chargers")
print("chargers_wins_by_year:", chargers_wins_by_year)


# ###10: Intro to classes

# Classes are a way to organize and structure code.
# 
# We've already been using classes, they just haven't been presented as such.
# 
# Strings in python are classes, and we can access class methods on them, such as .lower().
# 
# Let's define a simple class.

# ####Instructions

# Make a class called Team.
# 
# Give it a class property called name, with the value "Tampa Bay Buccaneers".
# 
# Make an instance of the class, and assign it to the variable bucs.

# In[11]:

# Classes are defined with the class keyword.
# The parentheses are used to denote which class this class inherits from.
class NFLTeam():
    # Classes can have class properties.
    # These properties can then be accessed later on.
    # Properties are just variables that are contained in a class.
    name = "Pittsburgh Steelers"

# After we define a class, we create an instance of it.
steelers = NFLTeam()

# We can access the class property.
print("steelers.name:", steelers.name)

# The steelers variable is called an instance of the class.
# NFLTeam is the class.
# Because name is a class property, not an instance property, we can also access it directly.
print("NFLTeam.name:", NFLTeam.name)

class Team():
    name = "Tampa Bay Buccaneers"

bucs = Team()
print("bucs.name:", bucs.name)


# ###11: Initializing a class

# When we instantiate a class (create an instance of it), we have a chance to run a special function.
# 
# It's called the __init__ function, and it runs every time a class is instantiated.
# 
# We define functions inside our classes by indenting 4 spaces and then using the def keyword.

# ####Instructions

# Modify the Team class so that name is an instance property.
# 
# Make an instance of the class, passing in the value "Tampa Bay Buccaneers" to the __init__ function.
# 
# Assign the instance to the variable bucs.

# In[12]:

class Car():
    # The special __init__ function is run whenever a class is instantiated.
    # The init function can take arguments, but self is always the first one.
    # Self is a reference to the instance of the class.
    def __init__(self, car):
        # Using self before car means that car is an instance property.
        self.car = car

# When we instantiate the class, we pass in any arguments that the __init__ function needs.
# We skip the self argument.
accord = Car("Honda Accord")

# We set self.car in the __init__ function, but can print accord.car here.
# self is a reference to the instance of the class.
# It lets us interact with the class instance within the class.
print("accord.car:", accord.car)

# Instance properties are only available to instances, not to the classes.
# We couldn't print Car.car, for example.

class Team():
    def __init__(self, name):
        self.name = name

bucs = Team("Tampa Bay Buccaneers")
print("bucs.name:", bucs.name)


# ###12: Instance methods

# Classes can have methods. Once example is the .lower() method that turns a string into a lowercase version.
# 
# Methods are just functions that are contained within a class.
# 
# Here's an example of a method:
# 
#     class Car():
#         def __init__(self, miles_per_gallon):
#             self.mpg = miles_per_gallon
# 
#         def get_gas_cost(self, miles):
#             total_gas = self.mpg * miles
#             return total_gas * 3.00

# ####Instructions

# Add a method called count_total_wins to the Team class.
# 
# The method should take no arguments (except self), and should return the number of games the team won from 2009-2013.
# 
# Use the instance method to assign the number of wins by the "Denver Broncos" to broncos_wins.
# 
# Use the instance method to assign the number of wins by the "Kansas City Chiefs" to chiefs_wins.

# In[13]:

class Zoo():
    def __init__(self):
        self.animals = []

    # This is an instance method.
    # It can be invoked on any instance of this class.
    # Note that because it is an instance method, we still need to put in the self argument.
    def add_animal(self, animal):
        # This will add the animal to the list of animals that the instance is storing.
        self.animals.append(animal)

# We start with no animals.
san_diego_zoo = Zoo()
print("san_diego_zoo.animals:", san_diego_zoo.animals)

# Then we get a panda!
san_diego_zoo.add_animal("panda")
print("san_diego_zoo.animals:", san_diego_zoo.animals)

# The we get an orca!
san_diego_zoo.add_animal("orca")
print("san_diego_zoo.animals:", san_diego_zoo.animals)

# The nfl data is loaded into the nfl variable.
class Team():
    def __init__(self, name):
        self.name = name

    def count_total_wins(self):
        count = 0
        for row in nfl:
            if row[2] == self.name:
                count = count + 1
        return count

broncos = Team("Denver Broncos")
broncos_wins = broncos.count_total_wins()
print("broncos.name:", broncos.name)
print("broncos_wins:", broncos_wins)

chiefs = Team("Kansas City Chiefs")
chiefs_wins = chiefs.count_total_wins()
print("chiefs.name:", chiefs.name)
print("chiefs_wins:", chiefs_wins)


# ###13: Adding to the init function

# We read in the nfl data to the nfl variable automatically before, but we've removed it for this code cell.

# ####Instructions

# Add in code to read the csv nfl data to the __init__ method.
# 
# Store the nfl data in the self.nfl instance property.
# 
# Then convert the count_total_wins function to use the self.nfl property.
# 
# Use the instance method to assign the number of wins by the "Jacksonville Jaguars" to jaguars_wins.

# In[14]:

import csv
   
class Team():
    def __init__(self, name):
        self.name = name
        f = open("data/nfl.csv", "r")
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count

jaguars = Team("Jacksonville Jaguars")
jaguars_wins = jaguars.count_total_wins()

print("jaguars_wins:", jaguars_wins)


# ###14: Wins by year method

# Let's add the wins by year function that we created earlier to our class as a method.

# ####Instructions

# Add a method to the Team class that computes wins by year for the team.
# 
# The wins_by_year function should return a dictionary with each year from 2009-2013 as keys, and the number of wins in that year as values.
# 
# Valid years are "2009", "2010", "2011", "2012", and "2013".
# 
# Use the instance method to assign the number of wins by year by the "San Francisco 49ers" to niners_wins_by_year.

# In[15]:

import csv

class Team():
    def __init__(self, name):
        self.name = name
        f = open("data/nfl.csv", "r")
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count

    def wins_by_year(self):
        years = ["2009", "2010", "2011", "2012", "2013"]
        wins = {}
        for year in years:
            count = 0
            for row in self.nfl:
                if row[2] == self.name and row[0] == year:
                    count += 1
            wins[year] = count
        return wins

niners = Team("San Francisco 49ers")
niners_wins_by_year = niners.wins_by_year()

print("niners_wins_by_year:", niners_wins_by_year)

