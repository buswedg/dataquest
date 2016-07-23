
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Data Structures and Algorithms

# ##Binary Search

# ###1: Let's play a game

# Imagine you and I are playing a game. You have to guess a number between 1 and 100, and after each guess I will tell you whether the answer is higher or lower than your guess.
# 
# Perhaps your strategy is to start at 1. If 1 is not the answer, you guess 2, then 3, and so on. This strategy resembles the linear search we learned in our last mission. However, since I'm giving you helpful hints, a linear search is a naive approach to this game.

# ###2: A better strategy

# Instead, imagine first guessing 50. I tell you the answer is higher. Suddenly, you've removed half of the original possibilities for consideration. You then guess 75, and I tell you the answer is lower. In only two guesses, you've narrowed down your possibilities to only a fourth of the original size, and you now know that the answer lies between 50 and 75. That's a significant reduction, and your strategy is very efficient.
# 
# This strategy illustrates a binary search. The idea of a binary search is that we can efficiently find an item in a list if we know the list is ordered. We can check the middle element of the list, compare it to the item we are looking for, and continue narrowing down our search in this manner.

# ###3: When can we binary search?

# So if binary search is more efficient than linear search, why ever bother with linear search at all?
# 
# The answer is simple. We can only perform a binary search on ordered data. When we think back to our game, the key to our strategy is that we knew exactly how our guess compared to the correct number. To order elements, we must be able to compare two elements and determine which is greater, or if they are equal.
# 
# We will be using a dataset of nba players from 2012. The dataset is ordered alphabetically by last name, then first name. We can compare two strings the same way we compare integers. For instance, "A" is less than "Z", and "A" < "Z" would evaluate to True.
# 
# We have a small challenge to overcome because the names in the dataset are stored as
# 
#     "first_name last_name"
# 
# but the dataset is ordered differently. So, we cannot directly compare the names in their raw format. Instead, we will format them as
# 
#     "last_name, first_name"
# 
# Before moving on, be sure you're convinced why this format is important, and why it will allow us to compare names properly.

# ###4: Implementing binary search -- Part 1

# We'll now begin implementing a binary search on our list of nba players.
# 
# Some division by 2 will need to be done in order to perform binary search. In order to ensure we get a sensible index, we will cast the result of this division to an integer using the math.floor() function, which rounds down to the nearest integer.
# 
# This is necessary because if we are splitting an interval with an odd length, we will get an index that has a fraction. Since a fraction is nonsense in the context of indexing a dataset, we will cast it to an integer. The choice to round down rather than up is arbitrary, but we will use it for our implementation.
# 
# Since this is a pretty involved algorithm, we'll implement it piece by piece. The first important piece is that we understand what step to take after each guess. We have provided the format_name function to you to save you from tedious string manipulation.

# ####Instructions

# Write the function player_age, which takes in name as a parameter. 
# 
# For now, start your guess at the middle of the list, and return "later" if the queried name is later in the list, "earlier" if the queried name is earlier in the list, and "found" if you have found the queried name.
# 
# Store the result of calling player_age on "Darius Johnson-Odom" in johnson_odom_age.
# 
# Store the result of calling player_age on "Nick Young" in young_age.
# 
# Store the result of calling player_age on "Jeff Adrien" in adrien_age.
# 
# We have loaded the nba dataset for you.

# In[2]:

import csv
import math

with open("data/nba_2013.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    nba = list(reader)

# A function to extract a player's last name.
def format_name(name):
    return name.split(" ")[1] + ", " + name.split(" ")[0]

# The length of the dataset.
length = len(nba)

# Implement the player_age function.    
def player_age(name):
    name = format_name(name)
    first_guess_index = math.floor(length/2)
    first_guess = format_name(nba[int(first_guess_index)][0])
    if name < first_guess:
        return "earlier"
    elif name > first_guess:
        return "later"
    else:
        return "found"
    
johnson_odom_age = player_age("Darius Johnson-Odom")
print("johnson_odom_age:", johnson_odom_age)

young_age = player_age("Nick Young")
print("young_age:", young_age)

adrien_age = player_age("Jeff Adrien")
print("adrien_age:", adrien_age)


# ###5: Implementing binary search -- Part 2

# We've now found our first guess and determined where to keep looking. The next step is to continue our binary search.
# 
# Let's imagine a round of our game from before. You guess 50, and I tell you the answer is higher. Now what do you do? Well, you guess 75, but how did you calculate that value? This is the step we will focus on for part 2 of our implementation.
# 
# There are a number of ways to calculate the index of the next split. Whichever method we use, we must keep track of the upper and lower bounds of our search. At the beginning of our game, the lower bound is 1, and the upper bound is 100. After I tell you the answer is greater than 50, the lower bound becomes 51 while the upper bound remains 100.
# 
# The bounds will look slightly different in our binary search implementation, but only because the dataset is indexed starting at 0 instead of 1. It's important to note that our bounds are inclusive.

# ####Instructions

# Edit our player_age function to change the bounds and make a second guess when needed. player_age should return the second guess, which will be the name of a player. Format this returned value using our "last_name, first_name" format.
# 
# Store the result of calling player_age on "Pau Gasol" in gasol_age.
# 
# Store the result of calling player_age on "Paul Pierce" in pierce_age.

# In[3]:

# A function to extract a player's last name.
def format_name(name):
    return name.split(" ")[1] + ", " + name.split(" ")[0]

# The length of the dataset.
length = len(nba)

# Implement the player_age function.
def player_age(name):
    # We need to appropriately format our name for successful comparison.
    name = format_name(name)
    upper_bound = length - 1
    lower_bound = 0
    first_guess_index = math.floor(length/2)
    first_guess = format_name(nba[int(first_guess_index)][0])
    if name < first_guess:
        upper_bound = first_guess_index - 1
    elif name > first_guess:
        lower_bound = first_guess_index + 1
    else:
        return first_guess
    second_guess_index = math.floor((lower_bound + upper_bound) / 2)
    second_guess = format_name(nba[int(second_guess_index)][0])
    return second_guess
    
gasol_age = player_age("Pau Gasol")
print("gasol_age:", gasol_age)

pierce_age = player_age("Paul Pierce")
print("pierce_age:", pierce_age)


# ###6: Pseudo-code

# Writing algorithms is less an exercise in coding, and more an exercise in reasoning. It's important to train your ability to develop and visualize algorithms. A strong tool that is easy to use is pseudo-code. You've already seen plenty of pseudo-code, even in this mission.
# 
# Pseudo-code comments reflect the code you want to write, but describe it in a high-level human language. In the last screen, we saw the following code snippet:
# 
#     # If the name comes before our guess
#         # Adjust the bounds as needed
#     # Else if the name comes after our guess
#         # Adjust the bounds as needed
#     # Else
#         # Player found, so return first guess
# 
# The comments in this snippet are easily replaced with code, but serve as placeholders for unwritten code. By writing pseudo-code like this, we can often plan and visualize an algorithm before worrying about syntactic details.
# 
# Pseudo-code is a good tool in all applications of programming, and we will use it in this mission to indicate where certain code needs to be written.

# ###7: Implementing binary search -- Part 3

# We've implemented a binary search function that runs for two iterations. It guesses twice, but if it doesn't find the answer in those two guesses, it gives up. This isn't robust, and we shouldn't stop until we've found our answer.
# 
# We've also seen that the guessing code is very repetitive. After each guess, we check if it's correct, adjust our bounds as needed, and then guess again. This is precisely the logic we need, and we can run that logic over and over again. The important step to take now is to translate it into a loop.
# 
# A while loop is perfect for this algorithm. It executes code as long as a condition is met. 
# 
#     count = 10
#     while count != 0:
#         print(count)
#         count = count - 1
#     print("blastoff!")
# 
# 
# The above while loop counts down from 10, and then prints "blastoff!". We will use a while loop to keep guessing until we've found the nba player we're searching for.

# ####Instructions

# Edit the player_age function to continue guessing until the desired name is found. Use a while loop with an appropriate condition to do so.
# 
# When the desired name is found, simply return "found".
# 
# Store the result of calling player_age on "Carmelo Anthony" in carmelo_age.

# In[4]:

# A function to extract a player's last name
def format_name(name):
    return name.split(" ")[1] + ", " + name.split(" ")[0]

# The length of the dataset
length = len(nba)

# Implement the player_age function.
def player_age(name):
    # We need to appropriately format our name for successful comparison.
    name = format_name(name)
    # Bounds of the search.
    upper_bound = length - 1
    lower_bound = 0
    # Index of first split.
    index = math.floor((lower_bound + upper_bound) / 2)
    # First guess halfways through the list.
    guess = format_name(nba[int(index)][0])
    # Search until the name is found
    while name != guess:
        if name < guess:
            upper_bound = index - 1
        else:
            lower_bound = index + 1
        index = math.floor((lower_bound + upper_bound) / 2)
        guess = format_name(nba[int(index)][0])
    return "found"
    
carmelo_age = player_age("Carmelo Anthony")
print("carmelo_age:", carmelo_age)


# ###8: Implementing binary search -- Part 4

# We're almost finished implementing our binary search. We still have to retrieve the player's age once we find him, and return -1 if he is not found. We can tell that a player is not found by adding a small condition to our search.
# 
# We should search until we've found the player, or until our list of possible answers is depleted. If we deplete all possible answers, the final step of our search, when upper_bound is equal to lower_bound (and also equal to index), will result in either upper_bound being decremented, or lower_bound being incremented. When this happens, lower_bound will be above upper_bound. We can easily check for this in our loop. It's very important to understand this nuance of our algorithm in order to take advantage of it.
# 
# Since these additions are short, we've also left it up to you to fill in the missing components of our algorithm.
# 
# In the code screen, we've provided pseudo-code for our algorithm, but have left it up to you to write the code.
# 

# ####Instructions

# Write the appropriate code that satisfies the tasks required by the pseudo-code.
# 
# Store the result of calling player_age on "Stephen Curry" in curry_age.
# 
# Store the result of calling player_age on "Blake Griffin" in griffin_age.
# 
# Store the result of calling player_age on "Michael Jordan" in jordan_age.
# 
# Looking back at the previous partial-implementations may help if you get stuck.

# In[5]:

# A function to extract a player's last name
def format_name(name):
    return name.split(" ")[1] + ", " + name.split(" ")[0]

# The length of the dataset
length = len(nba)

# Implement the player_age function.
def player_age(name):
    name = format_name(name)
    upper_bound = length - 1
    lower_bound = 0
    index = math.floor((lower_bound + upper_bound) / 2)
    guess = format_name(nba[int(index)][0])
    while name != guess and upper_bound >= lower_bound:
        if name < guess:
            upper_bound = index - 1
        else:
            lower_bound = index + 1
        index = math.floor((lower_bound + upper_bound) / 2)
        guess = format_name(nba[int(index)][0])
    if name == guess:
        return nba[int(index)][2]
    else:
        return -1
    
curry_age = player_age("Stephen Curry")
print("curry_age:", curry_age)

griffin_age = player_age("Blake Griffin")
print("griffin_age:", griffin_age)

jordan_age = player_age("Michael Jordan")
print("jordan_age:", jordan_age)


# ###9: Binary search time complexity analysis

# Now let's analyze the complexity of binary search.
# 
# We've established that the size of our problem is reduced by a factor of 2 with every iteration of the algorithm. The time complexity of the algorithm depends on the size of the input, and so we can conclude that it is not constant time. However, it's more efficient than a linear search, and thus is not linear time.
# 
# It turns out that binary search runs in logarithmic time, which we denote as O(log(n)). Logarithms are the mathematical counterpart to exponents, and thus it makes sense that an algorithm which cuts its problem size in half, or any fraction, with each iteration will be logarithmic.
