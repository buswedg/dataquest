
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Data Structures and Algorithms

# ##Algorithms

# ###1: What is an algorithm?

# An algorithm is a well-defined series of steps that are taken to perform a task. An algorithm usually has an input, and an output. It may sound familiar, and really any code you write performs an algorithm, whether it be simple or complicated.
# 
# In real life, we perform algorithms daily. Following a cookie recipe is an example of a series of steps that takes an input (sugar, milk, flour, etc.) and produces an output (the cookies). 
# 
# You may have seen machine learning algorithms previously on Dataquest. These are a special, specific type of algorithm, but many more categories of algorithms exist. In this mission, we'll show you a few examples of what an algorithm looks like, and introduce some methods for evaluating the efficiency of those algorithms.

# ###2: Implementing an algorithm

# Let's start with a simple algorithm that searches for a value in a list. One algorithm we could use is a linear search. Remember that an algorithm is a particular method for performing a task, and linear search is only one example of an algorithm that can solve this problem.
# 
# Linear search checks a list of items for a particular value by checking each item in the list until it finds the item it is looking for. If a matching item is not found, we can determine that no matching item exists in the list.

# ####Instructions

# Write a linear search algorithm to find "Kobe Bryant" in the nba dataset. The first column (index 0) of the dataset contains each player's name.
# 
# When "Kobe Bryant" is found, store his position (the second column of the dataset) in the variable kobe_position.

# In[2]:

import csv
with open("data/nba_2013.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    nba = list(reader)

# When Kobe is found in the dataset, store his position in Kobe_position.
kobe_position = ""

# Find Kobe in the dataset.
kobe_position = ""
for row in nba:
    if row[0] == "Kobe Bryant":
        kobe_position = row[1]

print("kobe_position:", kobe_position)


# ###3: Importance of modularity and abstraction

# As algorithms get more complex, it's important to keep code modular.
# 
# Modular code is split into smaller chunks of code that can be reused easily and often. This is most typically done using functions.
# 
# Abstraction is the idea that someone can use code to perform an operation without having to worry about how that code is implemented.
# 
# An easy example of modularity and abstraction is the sum() function. We don't know how exactly the function is implemented, we only need to know what it does. That makes it abstract. It also saves us the work of having to manually compute sums in many parts of our code. That makes it modular.

# ###4: Linear search revisited

# Now let's try writing a modular search function that can easily find the age of any player in our dataset without having to repeat code.

# ####Instructions

# Write a function called player_age that takes in a name parameter. The function should return the age of the player with name name, according to our nba dataset (which we have loaded in for you). If the player is not found, the function should return -1.
# 
# The third row (index 2) of nba contains players' ages.
# 
# Store the age of "Ray Allen" in the variable allen_age.
# 
# Store the age of "Kevin Durant" in the variable durant_age.
# 
# Store the age of "Shaquille O'Neal" in the variable shaq_age.
# 
# If the for loop finishes execution without returning, it's safe to return -1 since no matching player was found.

# In[3]:

# player_age returns the age of a player in our nba dataset
def player_age(name):
    for row in nba:
        if row[0] == name:
            return row[2]
    return -1
    
allen_age = player_age("Ray Allen")
print("allen_age:", allen_age)

durant_age = player_age("Kevin Durant")
print("durant_age:", durant_age)

shaq_age = player_age("Shaquille O'Neal")
print("shaq_age:", shaq_age)


# ###5: What makes an algorithm smart?

# So far, we've been working with a simple algorithm: linear search. However, when we need to perform more complicated tasks, algorithms become much more involved, and often many algorithms exist that achieve the same result.
# 
# With multiple algorithms to choose from, trade-offs must be made, and a programmer has to choose which algorithm best suits his/her needs. The most common factor to consider is time complexity.
# 
# Time complexity is a measurement of how much time an algorithm takes with respect to its input size. Algorithms that have a smaller time complexity generally take less time and are more desirable.

# ###6: Constant time algorithms

# Let's consider an algorithm that returns the first element of a list:
# 
#     def first(ls):
#         return ls[0]
# 
# Regardless of the size of the list, returning the first element is done in constant time. It only takes one operation to retrieve this element, no matter how large the list.
# 
# We tend to think of algorithms in terms of steps. Any primitive operation like setting a variable or performing arithmetic is considered a step. Algorithms that take a constant number of steps are always constant time, even if that constant number is not 1. 
# 
# Most complicated algorithms are not constant time. However, many operations within larger algorithms are constant time. Since we don't particularly care about what the constant is, we don't need to tediously count steps as long as we are certain we will get a constant.
# 
# An example of an operation that is not constant-time is a loop that touches every element in an input list. Since a larger input would cause more steps to be necessary, we cannot treat this operation as a constant. We'll look closely at examples like this soon.

# ###7: Example constant time algorithms

# It's important to recognize the time complexity of your algorithms.

# ####Instructions

# Read the function implementations below. Of A, B, and C, one implementation is not constant time. Indicate which by setting not_constant to the value "A", "B", or "C".

# In[4]:

# Implementation A: Convert degrees Celcius to degrees Fahrenheit
def celcius_to_fahrenheit(degrees):
    step_1 = degrees * 1.8
    step_2 = step_1 + 32
    return step_2

# Implementation B: Reverse a list
def reverse(ls):
    length = len(ls)
    new_list = []
    for i in range(length):
        new_list[i] = ls[length - i]
    return new_list

# Implementation C: Print a blastoff message after a countdown
def blastoff(message):
    count = 10
    for i in range(count):
        print(count - i)
    print(message)

not_constant = ""
not_constant = "B"


# ###8: Common pitfall

# We said earlier that small steps in an algorithm can often be considered constant time. However, be careful not to expect that every small operation is constant time. For instance, function calls and built-in Python operations are often not constant time because the function/operator itself is not constant time.
# 
#     def has_milk(fridge_items):
#         if "milk" in fridge_items:
#             return True
#         else:
#             return False
# 
# 
# It's easy to mistake the above function for a constant time algorithm. However, the python in operator has to search through the given list to see if the element "milk" exists, which can take more or less time depending on the size of the list. This algorithm, therefore, is not constant time.

# ###9: Linear time algorithms

# Now let's consider the linear search we wrote earlier. It looked something like this:
# 
#     def player_age(name):
#         for row in nba:
#             if row[0] == name:
#                 return row[2]
#         return -1
# 
# 
# The above code stops executing and returns immediately when the nba player is found, so it doesn't waste steps checking the rest of the list.
# 
# If a linear search is performed, and the element we are looking for happens to be first in the list, then the search is very quick. However, that case isn't very interesting, and it doesn't tell us very much about what trade-offs we are really making by choosing an algorithm.
# 
# The worst case of a linear search happens when the element does not exist in the list, or is found late in the list. This is the case we care about, since we need to account for the worst case so that our algorithm is more robust.
# 
# For a list of size n, in the worst case n elements have to be checked. We refer to this time complexity as linear time, since the time the algorithm takes to run grows at a constant rate with respect to its input size.
# 
# Algorithms that take constant multiples of n steps (where n is the input size) are still linear time. For instance, an algorithm that takes 5n steps, or even 0.5n steps, is linear time. For example, if we have an algorithm that prints the first half of a list (and we know the length of the list ahead of time), the algorithm would take 0.5n time. Even though it takes less than n time, we still consider it linear.
# 
# It's also worth noting that we only care about performance at a large scale. At a small scale, most algorithms will run pretty quickly, and it's only when n gets large that we worry about time complexity. Consequently, only the highest order of n is considered for time complexity. So, an algorithm that runs in 9n + 20 time is linear, because the constant component is negligable for large values of n.

# ###10: Some other algorithms

# We have seen only two types of algorithms so far: linear time and constant time algorithms. There are infinitely many categories of algorithms and time complexities, but just these two cover a large variety of different algorithms.

# ####Instructions

# Read the implementations of algorithms, and indicate their time complexities by setting the variables below to "linear" or "constant", as appropriate for their corresponding algorithms.
# 
# Remember that function calls also take time. So, if an internal function costs n operations, we must be sure to factor that into our time complexity analysis.

# In[5]:

# Find the length of a list.
def length(ls):
    count = 0
    for elem in ls:
        count = count + 1
length_time_complexity = ""

# Check if a list is empty -- Implementation 1.
def is_empty_1(ls):
    if length(ls) == 0:
        return True
    else:
        return False
is_empty_1_complexity = ""

# Check if a list is empty -- Implementation 2.
def is_empty_2(ls):
    for element in ls:
        return False
    return True

is_empty_2_complexity = ""
print("is_empty_2_complexity:", is_empty_2_complexity)

length_time_complexity = "linear"
print("length_time_complexity:", length_time_complexity)

is_empty_1_complexity = "linear"
print("is_empty_1_complexity:", is_empty_1_complexity)

is_empty_2_complexity = "constant"
print("is_empty_2_complexity:", is_empty_2_complexity)


# ###11: A brief note about notation

# When discussing time complexity, we should use the proper notation. Most commonly, we use Big-O Notation. The notation is rather simple. 
# 
# To denote constant time, we would write O(1), since 1 is a constant (and a simple constant).
# 
# To denote linear time, we would write O(n), since n is the simplest example of linearity.
# 
# For other time complexities, Big-O Notation follows a similar pattern. O(n^2), O(2^n), O(log(n)), etc. are all valid time complexities. The algorithms with these complexities are probably rather complicated, and we don't need to worry about them right now. Just know how to recognize Big-O Notation so that we can use it to describe time complexities in future missions.

# ###12: Why time complexity matters

# When we are analyzing real-world data, time complexity is an important consideration. Since datasets can get quite large, an inefficient algorithm will perform very slowly.
# 
# Algorithms with lower-order time complexities are more efficient. Constant time algorithms, denoted O(1), are more efficient than linear time algorithms, denoted O(n). Similarly, an algorithm with complexity O(n^2) is more efficient than one with complexity O(n^3).
# 
# When we try to choose an algorithm, we always want to find the one with the lowest time complexity. It may not always be the easiest to implement, but the extra effort is usually worth the resulting efficiency.
