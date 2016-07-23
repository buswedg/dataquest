
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Python Programming

# ##Lambda Functions

# ###1: String Manipulation

# In this mission, we will dive into String manipulation, which is essential to working with data that's represented as text. String objects are indexed for quick access to specific characters in the String object, similar to a List. If we want to access the first character in my_string, we write my_string[0], just like we would to access the first element in a List.
# 
# We can also slice String objects to select the fragments of the String we want to pull out using the index. When we slice a String, we select a chunk, or a substring, from the original String. While we only needed to specify one number, the index, when we want to select a specific character, when slicing a String, we need to specify a range of values for the index instead of just a single number. 
# 
# If we want the first 4 characters in a String, what we are really asking for is the characters from index 0 to index 3 of the String. In Python, to represent ranges, we would specify the starting index as 0, but the ending index as 4. Python uses the ending index to stop iterating and does not return the character at index 4; this is one of the quirks of Python! If we want the characters in index 2 to index 5, we would need to specify 2 as the starting index and 5, not 4, as the ending index.
# 
# To represent ranges, we still use bracket notation as before, but now we instead specify 2 numbers: the starting index and the ending index, separated with a colon. If we want the first four characters of the String object my_string, we write:
# 
#     my_string[0:4]

# ####Instructions

# Select the fifth character of "password" and store the result in the variable fifth. Select the last 4 characters of "password" and store the result in the variable last_four.

# In[2]:

hello = "hello world"[0:5]
foo = "some string"
password = "password"

print("foo:", foo[5:11])

fifth = password[4]
print("fifth:", fifth)

last_four = password[4:8]
print("last_four:", last_four)


# ###2: Omitting starting or ending indices

# We can also take advantage of Python's flexibility with ranges to omit the starting or ending index for interesting effects. If we omit the first index, the Python interpreter will assume you want to start at the beginning, or index 0, and stop at the ending index. If we omit the ending index, the interpreter will assume you want to grab all the characters from the starting index all the way until the end of the String.
# 
# A quick example:
# 
#     password = "password"
#     first_three = password[:3]
#     last_three = password[3:]
# 
# first_three will contain the first three letters of "password" while last_three will, wait for it, contain the last three letters of "password".
# 
# What do you think happens when you don't specify either the starting index or the ending index?

# ####Instructions

# Select the first 9 characters of "string slicing is fun!" and store the result in first_nine. Select the substring from the 10th character to the end of the String and store the result in remainder.

# In[3]:

hello = "hello world"[:5]
foo = "some string"
print("foo:", foo[5:])

my_string = "string slicing is fun!"

first_nine = my_string[:9]
print("first_nine:", first_nine)

remainder = my_string[9:]
print("remainder:", remainder)


# ###3: Slicing with a step

# Now that you got a taste of slicing, let's explore some other ways we would want to select a substring from a String. What if we want to select every odd character in a String? Specifically, how do we select all the characters at index 1, 3, 5, etc. With what we know so far, we would have to iterate through every character and throw away all the even characters. Or we could create a List with just the odd indices and write a for loop to iterate and select just the characters at those indices. Thankfully, there's a simpler way!
# 
# We can actually provide a third number in our range that controls the distance between each character we want to select. This value is known as the step value and by default, it's 1. Let's see how we can use that functionality to select all of the characters in password with odd indices only.
# 
#     password = "password"
#     odds = my_string[1:8:2]
# 
# The slice [1:8:2] specifies that we want the substring to start at index 1, add 2 each time to the index until it observes or exceeds index 8. Therefore, the String object odds should be set to the value "asod", which correspond to the four characters at indices 1, 3, 5, and 7. If we didn't provide a step value, the interpreter would have defaulted to 1 and odds would contain all of the characters starting at index 1 instead of just the ones at odd indices.
# 
# By similar logic, password[0:6:4] would select just "pw". We would start at index 0, extract "p", step to index 4, and finally extract "w". If we step again, the index would be at 8, which is beyond our ending index of 6. 
# 
# We can combine this with the omission of indices to do advanced slicing with relatively simple notation. Instead of writing password[0:6:4] we could write password[:6:2]

# ####Instructions

# Slice "string slicing is fun!" to extract every other character, starting at index 0, in the entire string. Store the result in gibberish.
# 
# Slice "string slicing is fun!" to extract every third character starting at the first character of "slicing". Store the result in worse_gibberish.

# In[4]:

hlo = "hello world"[:5:2]

my_string = "string slicing is fun!"

gibberish = my_string[::2]
print("gibberish:", gibberish)

worse_gibberish = my_string[7::3]
print("worse_gibberish:", worse_gibberish)


# ###4: Negative Indexing

# We can also use negative values to index and slice String objects. The index -1, for example, refers to the last character of a String. "word"[-1] would evaluate to "d" while "word"[-2] would evaluate to "r". Now, how exactly does negative indexing benefit us?
# 
# Negative indexing allows us to step backwards by specifying a negative number for the step value. For example, "backwards"[3::-1] starts at index 3, steps backwards in increments of 1 until it gets to the first character, wraps around to the end of the String, and stops. The result of that slice is "kcab".

# ####Instructions

# A palindrome is a word or String that is spelled the same way forwards and backwards. "racecar" is a palindrome because reading it from left to right is the same as reading it right to left.
# 
# Write a function is_palindrome that takes a String, my_string, as an argument and returns True if the String is a palindrome. Store the result of calling is_palindrome on "able was I ere I saw elba" in phrase_palindrome.

# In[5]:

olleh = "hello world"[4::-1]
able_string = "able was I ere I saw elba"

def is_palindrome(my_string):
    return my_string == my_string[::-1]

phrase_palindrome = is_palindrome(able_string)
print("phrase_palindrome:", phrase_palindrome)


# ###5: The Password Data

# Now, we will be working with a long list of user passwords and will explore how we can use some of the techniques we learned. Each item in the list is a String that was once used as a password. A list like this is known as a password list and we will use it to find some interesting trends in how people select passwords. We have loaded this list into the passwords variable.

# ###6: Checking for Substrings

# If we want to check whether the characters in a String, inner_substring, are found in another String, big_string, we can use the Python in operator. If inner_substring contained the value "hello" and big_string contained the value "hello world", the following code segment would return True:
# 
#     inner_substring in big_string
# 
# If big_string instead contains the value "goodbye", the above expression would evaluate to False.

# ####Instructions

# Write a function called easy_patterns that takes a String argument corresponding to a pattern. The function should count the number of passwords in passwords contain that pattern and return it. 
# 
# After you've written the function, call easy_patterns with the argument "1234" and store the result as countup_passwords.

# In[6]:

import sys
import csv

with open("data/passwords.txt") as f:
    passwords = f.read().splitlines()

print("passwords:", passwords[:5])
    
def easy_patterns(pattern):
    count = 0
    for password in passwords:
        if pattern in password:
            count += 1
    return count

countup_passwords = easy_patterns("1234")
print("countup_passwords:", countup_passwords)


# ###7: First-Class Functions

# Python, like many programming languages, treat functions as first-class citizens. This means that functions can be passed in as arguments to other functions just like objects can. To understand why first-class functions are used, let's consider an example. 
# 
# Suppose we have a long List of floating point numbers, and we need to convert them to integers. While could use a list comprehension, Python has a built in function called map that we can use instead. map(func, ls) iterates through the list ls, and runs func on every item in the List. In this case, func could contain logic that converted floating point numbers to integers and that would be applied to every item on the list.

# ####Instructions

# The variable not_floats contains a list of String objects that are actually floating point numbers (e.g. "12.0"). Use Python's map function to convert every string into a floating point number and store the result in floats.

# In[7]:

ints = list(map(int, [1.5, 2.4, 199.7, 56.0]))
print("ints:", ints)

not_floats = ['1.4', '71.833', '0.1', '109.2', '77.7', '618.44', '12.004']
print("not_floats:", not_floats)

floats = list(map(float, not_floats))
print("floats:", floats)


# ###8: Average Password Length

# Recall that String objects are indexed like List objects and can treat them the same when it comes to selecting values. Therefore, just as we can use the len function to calculate the length of a List, we can also use it to calculate the length of a String.

# ####Instructions

# Use the map function to iterate over passwords, cast the result as a List object (containing the length of each password), and store the result in password_lengths. Then, calculate the average password length by using the sum function, which takes a List as the argument. Store the result in avg_password_length.

# In[8]:

password_lengths = list(map(len, passwords))

avg_password_length = float(sum(password_lengths)) / len(passwords)
print("avg_password_length:", avg_password_length)


# ###9: More Uses For First-Class Functions

# Many functions take advantage of first-class functions to simplify the logic. A common one is the filter function, which takes a func argument and an ls argument, and returns a list of all elements in ls for which func evaluates to True. In other words, it filters out every element for which func called on that argument will evaluate to False.
# 
# Just like with map, we need to cast the result of a filter to a List using the list function.

# ####Instructions

# Use our is_palindrome function to find a list of all passwords that are palindromes and store the result in palindrome_passwords.

# In[9]:

def is_palindrome(my_string):
    return my_string == my_string[::-1]

palindrome_passwords = list(filter(is_palindrome, passwords))
print("palindrome_passwords:", palindrome_passwords[:50])


# ###10: Lambda Functions

# Let's now talk about lambda functions, also known as an anonymous function. We use lambda functions when we only want to run a function once and don't need to save it for reuse. In the last screen, we wrote the is_palindromefunction but only used it once. Since the logic for is_palindrome was only one line, it would have been more convenient to write and apply the logic when we needed it to when we executed the filter function.
# 
# This is precisely what lambda functions allow us to do. The syntax is different than what we've been exposed to before, but it's similar to passing in a value rather than a variable to a function. Syntactically, a lambda function is represented in the following way:
# 
#     lambda arg1, arg2, etc. : perform task on arg1 and arg2
# 
# So,
# 
#     lambda x, y : x + y
# 
# is a lambda function that takes two parameters and adds them together.

# ####Instructions

# Use a lambda function to filter through the passwords list and produce a list of palindrome passwords. Store this list in palindrome_passwords.

# In[10]:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x : x % 2 == 0, numbers))
print("evens:", evens)

palindrome_passwords = list(filter(lambda password : password[::-1] == password, passwords))
print("palindrome_passwords:", palindrome_passwords[:50])


# ###11: Password Strengths

# In just one line of code, we parsed through a list of passwords and determined which ones were palindromes. Hopefully, you have a sense for how lambda functions helps keep code more maintainable by reducing the number of defined functions.
# 
# To conclude this mission, we'll ask to combine a few of the concepts we learned to calculate each password's strength. Let's assign any password with a length less than 6 to be "weak", any password with a length between 6 and 10 (inclusive) to be "medium", and any password with a length greater than 10 to be "strong".

# ####Instructions

# Using only one line of code each, calculate and store the list of all weak passwords in the weak_passwords variable, the list of all medium passwords in the medium_passwords variable, and the list of all strong passwords in the strong_passwords variable.

# In[11]:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x : x % 2 == 0, numbers))
print("evens:", evens)

weak_passwords = list(filter(lambda password : len(password) < 6, passwords))
print("weak_passwords:", len(weak_passwords))

medium_passwords = list(filter(lambda password : len(password) >= 6 and len(password) <= 10, passwords))
print("medium_passwords:", len(medium_passwords))

strong_passwords = list(filter(lambda password : len(password) > 10, passwords))
print("strong_passwords:", len(strong_passwords))

