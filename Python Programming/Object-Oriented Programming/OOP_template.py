
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Python Programming

# ##Object-Oriented Programming

# ###1: Solving Problems with Code

# Computer programming is an engineering discipline. A successful engineer must be able to think through complex problems and choose an optimal solution. This involves careful planning, some trial and error, and above all else experience. It's important to practice programming in order to build an intuition for what tools best fit a situation, and how to approach particular problems.

# ###2: Defining custom classes

# Let's now explore how to use custom classes to explore data on NBA players from the 2013-2014 season. We need a way to easily represent both the players and teams in the league. Let's focus on how we can use custom classes to compare the average ages of the players on each team.
# 
# You can see below that we have defined a Player class and we have defined the default __init__ method to take in a data row as an argument. We made a deliberate choice to split up the logic of players and teams so that our code is easy to read and maintain. We also made the convenient choice to initialize our Player instances using a data row, since all of the information is present in a row, and it will make it easier later on to create Player objects from the dataset.

# ####Instructions

# Create a Team class that is initialized with a team name. Store that team name in the instance property team_name.
# 
# Create an instance of the Team class with the team name "San Antonio Spurs". Call this instance spurs.

# In[2]:

import csv
with open("data/nba_2013.csv", "r") as f:
    reader = csv.reader(f, delimiter=',')
    nba = list(reader)

# Implement the Player class
class Player():
    # The special __init__ function is run whenever a class is instantiated.
    # The init function can take arguments, but self is always the first one.
    # Self is just a reference to the instance of the class. It is automatically
    #     passed in when you instantiate an instance of the class.
    def __init__(self, data_row):
        self.player_name = data_row[0]
        self.position = data_row[1]
        self.age = int(data_row[2])
        self.team = data_row[3]

# Initialize a player using the first row of our dataset
first_player = Player(nba[1])

print("first_player.player_name:", first_player.player_name)
print("first_player.position:", first_player.position)
print("first_player.age:", first_player.age)
print("first_player.team:", first_player.team)

# Implement the Team class
class Team():
    def __init__(self, team_name):
        self.team_name = team_name
        
spurs = Team("San Antonio Spurs")
print("spurs.team_name:", spurs.team_name)


# ###3: More interesting instance properties

# Now that we have a Team class with a team name, we can also store a team roster within each Team instance.
# 
# We'll represent a roster as a list of Player instances. We can write code inside the __init__ method to run some initialization logic.
# 
# Our dataset of NBA players has been loaded into the nba variable.

# ####Instructions

# Modify the __init__ method of the Team class to loop through our dataset and add a player to the roster every time the row's team name matches the instance's team_name. You can add an item to a list using .append(item).
# 
# Store the "San Antonio Spurs" team in spurs.

# In[3]:

class Team():
    def __init__(self, team_name):
        self.team_name = team_name
        self.roster = []
        for row in nba:
            if row[3] == self.team_name:
                self.roster.append(Player(row))
                
spurs = Team("San Antonio Spurs")
print("spurs.team_name:", spurs.team_name)


# ###4: Instance Methods

# The Player and Team classes we have defined serve as blueprints that we can use to create instances of these classes. Fundamental to object oriented programming are the classes and the instances of those classes, known collectively as objects.
# 
# We can define some methods on a class. For example, if we want to compute the average age of the players on a team, we would write a method for the Team class that does so. However, since this number can be different for each team, we want to make sure the method acts individually on specific instances of the Team class. We call these methods instance methods.
# 
# For method declarations, the first argument to the method is always self, even though we don't explicitly pass in self when we call the method. self is a reference to the current object we are working with, and is useful when we want to access properties of that object within the method we are defining.

# ####Instructions

# Write an average_age method for the Team class that computes the average age of the Team instance. We have provided a method to find the total number of players on a Team instance.
# 
# Store the result of calling average_age on the "TOT" team in TOT_avg_age.

# In[4]:

class Team():
    def __init__(self, team_name):
        self.team_name = team_name
        self.roster = []
        for row in nba:
            if row[3] == self.team_name:
                self.roster.append(Player(row))
    
    def num_players(self):
        count = 0
        for player in self.roster:
            count += 1
        return count
    
    def average_age(self):
        total_age = 0
        for player in self.roster:
            total_age += player.age
        return total_age / self.num_players()


# Initialize the TOT team
TOT = Team("TOT")

TOT_avg_age = TOT.average_age()
print("TOT_avg_age:", TOT_avg_age)


# ###5: Class Methods

# In traditional object-oriented programming, everything (yes, everything) is an object. Integers are objects, booleans are objects. Python is not quite this object-oriented, but objects are nonetheless abundant in the Python language. For example, the math.floor function is really just a class method for the math class. Class methods act on a whole class rather than a particular instance of a class, and are often used as utility functions.
# 
# Notice in the code below that we've rewritten our average_age method to use the math class along with a list comprehension. This is somewhat advanced Python code, but you've seen all of it before. The math.fsum method is a method that acts on the math class, and takes an iterable (i.e. list or list-like) argument, and sums the values in the list to produce a result.
# 
# Notice also that we have begun writing a class method for you. The @classmethod line above the method tells the Python interpretter that the method is a class method. You'll have to follow this example whenever you declare class methods.

# ####Instructions

# Modify the older_team method to return the team with the greatest average age.
# 
# Store the result of calling older_team on the "TOT" team and the "UTA" team in old_team.
# 
# Read through all of the code we've written so far for our Team class. It's full of advanced Python concepts that will be very useful to you.

# In[5]:

import math

class Player():
    def __init__(self, data_row):
        self.player_name = data_row[0]
        self.position = data_row[1]
        self.age = int(data_row[2])
        self.team = data_row[3]

class Team():
    def __init__(self, team_name):
        self.team_name = team_name
        self.roster = []
        for row in nba:
            if row[3] == self.team_name:
                self.roster.append(Player(row))
    
    def num_players(self):
        count = 0
        for player in self.roster:
            count += 1
        return count
   
    def average_age(self):
        return math.fsum([player.age for player in self.roster]) / self.num_players()
    
    @classmethod
    def older_team(self, team1, team2):
        if team1.average_age() > team2.average_age():
            return team1
        else:
            return team2
        
        
old_team = Team.older_team(Team("TOT"), Team("UTA"))

older_team = old_team.team_name
print("older_team:", older_team)


# ###6: Inheritance

# In object oriented programming, the concept of inheritance enables you to organize classes in a tree-like hierarchy, where the parent class has some traits that are passed onto its descendants. When we define a class, we specify a parent class from which it inherits. Inheriting from a class means that the behavior of the parent also exists in the child, but that the child can still define its own additional behavior.
# 
# Consider a Player class with generic information about NBA players. This is very useful, and there are a lot of things players have in common, but we may want specific behavior for different positions. We can define classes like Center, Forward, or Point Guard, each with behavior that is specific to that position. These classes would each specify Player as its parent class. They would all be siblings, and would each inherit the same behaviors from the Player class, while also containing special behaviors of their own.
# 
# In Python 3, every class is a subclass of a generic object class. This is done automatically when an ancestor is not specified, but it's sometimes good practice to be explicit. When we define classes for the remainder of this mission, we will explicitly specify when a class has object as its parent. This is a good programming practice because if we get in the habit of specifying a class's ancestry, we won't forget to specify a parent when the parent class is something other than object. It's simply a way to form good habits.

# ###7: Overloading

# When a class inherits from a parent class, it acquires all of the behavior from that parent class. However, sometimes we don't want all of that behavior, or we want to modify it slightly for our custom class. To do so, we use a tool known as overloading.
# 
# Overloading inherited behavior means we assign new behavior to our custom class. It's simply done by redefining the method on our new class.
# 
# We will be altering our Player class to support comparisons using >, <, ==, !=, >=, and <=. The object class has these methods built in, and we've seen these operators used to compare integers, floating point numbers (decimals), and strings. The operators work because classes like string have implemented them specifically. However, it's a little difficult to understand why the object class would need to have these methods. The best way to understand is through example.
# 
# Let's imagine the + operator. The object class defines a method for addition. The sum() function is defined using the addition method, but the object class doesn't really know how to add integers or floating points specifically. However, the integer and float classes define their own addition method (thus overloading the object's addition method), and the sum() function will add the values together properly. This is very powerful, since sum() only had to be defined once, can be called on a multitude of classes, and results in proper behavior. This is the power of inheritance and overloading.

# ####Instructions

# Read the implementation of the __lt__ (less than, or <) method of our Player class. In this exercise, we will use comparisons to compare players by age.
# 
# Implement __gt__ (greater than, or >), __le__ (<=), __ge__ (>=), __eq__ (==), and __ne__ (!=).
# 
# Store the result of evaluating carmelo != kobe in result.

# In[6]:

class Player(object):
    def __init__(self, data_row):
        self.player_name = data_row[0]
        self.position = data_row[1]
        self.age = int(data_row[2])
        self.team = data_row[3]
        
    def __lt__(self, other):
        return self.age < other.age
    def __gt__(self, other):
        return self.age > other.age
    def __le__(self, other):
        return self.age <= other.age
    def __ge__(self, other):
        return self.age >= other.age
    def __eq__(self, other):
        return self.age == other.age
    def __ne__(self, other):
        return self.age != other.age


#Compare ages between Carmelo and Kobe
carmelo = Player(nba[18])

print("carmelo.player_name:", carmelo.player_name)
print("carmelo.position:", carmelo.position)
print("carmelo.age:", carmelo.age)
print("carmelo.team:", carmelo.team)


kobe = Player(nba[69])

print("kobe.player_name:", kobe.player_name)
print("kobe.position:", kobe.position)
print("kobe.age:", kobe.age)
print("kobe.team:", kobe.team)


result = carmelo != kobe
print("result:", result)


# ###8: Comparing Average Ages

# We've seen that we can overload operators for custom classes. In the last screen, we were able to compare NBA players by age using >, <, ==, etc. This is extremely powerful, because a lot of built-in Python functions use these simple operators. If we implement them on a custom class, we can use functions like min and max on instances of our Person class.
# 
# Our original goal was to compare NBA teams based on average ages. We saw how we could overload operators in our Person class, and now it's time to do the same for our Team class.

# ####Instructions

# Overload the same 6 methods we wrote for the Person class on the Team class, this time comparing average ages for teams.
# 
# The methods are __lt__ (<), __gt__ (>), __le__ (<=), __ge__ (>=), __eq__ (==), and __ne__ (!=). Each should take a self parameter and an other parameter. self and other are 2 instances of the Team class, whose average ages should be compared.
# 
# Between the "TOT" and "ORL" teams, store the older team in older_team. Now that we've implemented comparison operators, we can use a few useful functions, including the max function, which takes a list of values and returns the maximum value, according to the comparisons that are defined.

# In[7]:

import math

class Team(object):
    def __init__(self, team_name):
        self.team_name = team_name
        self.roster = []
        for row in nba:
            if row[3] == self.team_name:
                self.roster.append(Player(row))
                
    def num_players(self):
        count = 0
        for player in self.roster:
            count += 1
        return count
    
    def average_age(self):
        return math.fsum([player.age for player in self.roster]) / self.num_players()
    def __lt__(self, other):
        return self.average_age() < other.average_age()
    def __gt__(self, other):
        return self.average_age() > other.average_age()
    def __le__(self, other):
        return self.average_age() <= other.average_age()
    def __ge__(self, other):
        return self.average_age() >= other.average_age()
    def __eq__(self, other):
        return self.average_age() == other.average_age()
    def __ne__(self, other):
        return self.average_age() != other.average_age()


#Compare max ages between TOT and ORL
TOT = Team("TOT")

TOT_team_name = TOT.team_name
TOT_num_players = TOT.num_players()
TOT_avg_age = TOT.average_age()

print("TOT_team_name:", TOT_team_name)
print("TOT_num_players:", TOT_num_players)
print("TOT_avg_age:", TOT_avg_age)


ORL = Team("ORL")

ORL_team_name = ORL.team_name
ORL_num_players = ORL.num_players()
ORL_avg_age = ORL.average_age()

print("ORL_team_name:", ORL_team_name)
print("ORL_num_players:", ORL_num_players)
print("ORL_avg_age:", ORL_avg_age)


older_team = max([TOT, ORL])
print("older_team.team_name:", older_team.team_name)


# ###9: Oldest NBA Team

# Now that we've implemented the comparison operations, a lot of interesting information is readily available to us. Python uses these comparisons to implement many utility functions, and we can now use those functions in a new setting to do analysis for us. Through overloading operators, we now have access to powerful functions without having to implement tedious logic.

# ####Instructions

# Alter the indicated list comprehension so that the teams variable contains a list of all the teams corresponding to the names in team_names.
# 
# Use max to store the oldest team in oldest_team.
# 
# Use min to store the youngest team in youngest_team.
# 
# Use sorted to store a youngest-to-oldest list of teams in sorted_teams.

# In[8]:

team_names = ["TOT", "ORL"]
teams = list([Team(name) for name in team_names])

oldest_team = max(teams)
youngest_team = min(teams)
sorted_teams = sorted(teams)

print("oldest_team.team_name:", oldest_team.team_name)
print("youngest_team.team_name:", youngest_team.team_name)
print("sorted_teams.team_name:", sorted_teams[0].team_name, sorted_teams[1].team_name)


# ###10: Conclusion

# To solve our problem, we chose an implementation that cleanly separated the ideas of a Player and a Team. By doing so, we wrote organized and sensible code that wasn't too difficult to keep track of. Most importantly, we chose an elegant solution that allowed us to easily analyze the data we were interested in.
# 
# By implementing comparison operators, we were able to very easily determine which team was the oldest and the youngest, and could even rank NBA teams based on age in just one line of code. This is the power of object oriented programming, and it highlights the importance of choosing our implementation wisely.
