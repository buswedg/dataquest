
# coding: utf-8

# #Python Programming

# ##Python Basics

# ###1: Variables

# Variables are used in our code to store values that we want to use later. For example, we can store the value 10 in the variable b. The equals sign assigns the value on the right to the variable on the left.
# 
# You can overwrite a variable with a new value whenever you want. The variable will take on the new value.

# ####Instructions

# Assign 5 to the variable a.

# In[1]:

# Here is an example of assigning the value 10 to the variable b.
b = 10
# We can then assign a new value to the variable b.
b = 20

# a has the value 0.
a = 0
a = 5


# ###2: Printing values

# The print function in Python will print out values so we can look at them. We'll get more into what a function is later, but you can use the print function to print 10 by typing print(10).
# 
# Anything that is printed will appear in an output box underneath the code area.

# ####Instructions

# Use the print function to print the number 5.

# In[2]:

# The line below will print out the number 10.
# Look in the output area underneath to see it.
print(10)
print(5)


# ###3: Exploring the dataset

# We saw the raw dataset in the video. For the purposes of this lesson, we've preloaded an excerpt from the raw scripts into the star_wars variable. We can explore it by printing it out. You can print a variable the same way you print a number -- if you want to print the variable a, just type print(a).

# ####Instructions

# Print the star_wars variable.

# In[3]:

star_wars = []
f = open("data/star_wars.txt", 'r')
star_wars = f.read()
rows = star_wars.split('\n')

print(star_wars[:500])


# ###4: Types of variables

# We saw numbers before, like 5, and 10. These are known as integers. We also just printed an excerpt from the raw movie script data, which looked like STAR WARS - EPISODE 4: STAR WARS. This is known as a string.
# 
# Both strings and integers are different types of values that we can store in variables. When a string is stored in a variable, we call the whole variable a string.
# 
# There are many other kinds of variables, but another important one is a float. A float is a number with a decimal point. It is more precise than an integer, because it can store fractions.

# ####Instructions

# Assign an integer to h, a string to i, and a float to j.

# In[4]:

# A number without decimals is an integer type.
# An integer can hold negative and positive values.
# We can do do math with integers.
a = 5
b = -1

# Print a multiplied by b.
print(a * b)

# Anything enclosed in single or double quotes is a string.
# Strings hold text.
# We can't do math with strings like we can with integers.
# But there are some operations we can do (that we will learn later on).
c = "I'm a string.  I do string-like things."
d = 'Let me in on this string party!  PS I dont like math.'

# Floats are numbers with decimal points.
e = 5.1
f = 10.2
# g equals e times f.
g = e * f

# There are other types that we will learn about later on.
h = 1
i = "Strings are great."
j = 5.1


# ###5: Checking the type of a variable

# We can check what type a variable is by using the type function. If you wanted to find the type of the variable a, you would use type(a) to find it.
# 
# A function is a named chunk of code that takes certain inputs and gives you an output.
# 
# You can use functions by typing their name, and passing in the inputs. Some functions can have multiple input values.

# ####Instructions

# Assign the type of 10 to c, the type of "racecar" to d, and the type of 10.6 to e.

# In[5]:

# The type function has only one input value.
a = type(5)

# The above code invokes the type function on the input 5, and as the output, we get the type of 5.
# The type is assigned to a.

# We can also invoke functions on variables.
b = "Dataquest is the best thing ever"
# Note how when the type for b is printed, it is abbreviated to str.
print(type(b))

c = type(10)
print(c)

d = type("racecar")
print(d)

e = type(10.6)
print(e)


# ###6: So, which character speaks the most?

# You now have enough basic building blocks to figure out what character speaks the most across all three original star wars movies.
# 
# We mentioned in the video that we won't ask you to parse the data just yet -- that requires a few bits of knowledge that we'll get to in the next mission.
# 
# So what we'll give you instead is a preprocessed version of the data. This version of the data contains an entry for each character, and an entry for how many times they spoke.
# 
# The records will show the name of each character, then a :, then the number of lines they spoke. Here's an excerpt:
# 
#     {'leia': 113, 'boushh': 7, 'tarkin': 28,
# 
# leia speaks 113 lines, boushh speaks 7, and tarkin speaks 28.

# ####Instructions

# There's an easy automatic way to find who speaks the most lines that we'll learn later. For now, look through the printout of lines, and figure out who spoke the most lines. Assign the name of that character to most_lines.

# In[6]:

# The preprocessed data is loaded into the lines variable.
# Lines is a dictionary (dict), a type that we'll learn about in the next mission.
#print(type(lines))

# We can print out the lines variable and look at it.
#print(lines)
most_lines = "luke"

