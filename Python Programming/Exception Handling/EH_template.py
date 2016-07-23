
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Python Programming

# ##Exception Handling

# ###1: The Science of Chopsticks

# In 1991, a group of Taiwanese researchers set out to determine what length of chopstick is most effective. Over 30 individuals participated in the experiment, each of which tried every length of chopstick. This ensured that the results were not skewed by different skill levels or individuals who have grown accustomed to using certain lengths of chopsticks.
# 
# After an exciting few days of picking up peanuts and placing them into cups, the researchers gathered enough data to determine which chopsticks are most efficient. Their findings form our dataset.
# 
# In the first column of the dataset is the "Food.Pinching.Efficiency" measurement, which is a decimal value. The higher the value, the better the chopstick.
# 
# The second column, "Individual", contains unique identifiers for the particular individual that used the chopstick.
# 
# In the third column is the "Chopstick.Length" measurement, in millimeters.
# 
# Each row in our dataset is a trial, where a particular individual uses a certain length of chopstick, and the food pinching efficiency is measured for that individual and that length of chopstick.

# ###2: Organizing our code

# Let's think a bit about how we want to structure our code. We want to answer questions like which chopstick is more efficient, which chopstick has the most consistent results, etc.
# 
# All these questions are specific to certain lengths of chopstick, so it would be useful to have a Chopstick class that contains methods to compute these values based on which Chopstick we are using.
# 
# However, we must also realize that in order to produce useful information from our Chopstick class, we need to store the data for that chopstick. There are a few ways to do this, but we'll create a whole Trial class that stores information about each row in our dataset.

# ####Instructions

# Write a Trial class with the following instance properties: efficiency, individual, chopstick_length. efficiency should be a floating point number, and the other two properties should be integers. These properties should be set within the class's constructor function (__init__), which should take in a row from our dataset as an argument.
# 
# Store the first trial in our dataset in first_trial.

# In[2]:

import csv

with open("data/chopstick-effectiveness.csv", "r") as f:
    reader = csv.reader(f, delimiter=',')
    chopsticks = list(reader)
    
chopsticks = chopsticks[1:]


class Trial(object):
    def __init__(self, datarow):
        self.efficiency = float(datarow[0])
        self.individual = int(datarow[1])
        self.chopstick_length = int(datarow[2])
        
    def __str__(self):
        return str(self.chopstick_length)
        
first_trial = Trial(chopsticks[0])
print("first_trial.chopstick_length:", first_trial.chopstick_length)


# ###3: The Chopstick class

# Let's also create a class, Chopstick, whose instance properties contain information about that chopstick. For now, the only instance property we'll store in our chopstick class is the chopstick length.

# ####Instructions

# Write a Chopstick class that is initialized with a length. Store that length in the length instance property.
# 
# Store the Chopstick instance with a length of 100 (millimeters) in mini_chopstick.

# In[3]:

class Chopstick(object):
    def __init__(self, length):
        self.length = length

mini_chopstick = Chopstick(100)
print("mini_chopstick.length:", mini_chopstick.length)


# ###4: Storing the trials

# Now we need to refine our Chopstick class a little to make it more useful. In each Chopstick instance, we're going to store all of the trials in our chopsticks dataset that correspond to that length of chopstick.

# ####Instructions

# Modify the __init__ method of our Chopstick class to store a list of trials corresponding to the proper chopstick length. We'll store this information in an instance property called trials. When searching for rows with the proper length, we should cast the dataset length to an integer before comparing so that we are not comparing a string to an integer.
# 
# Store the Chopstick instance with a length of 240 in medium_chopstick.

# In[4]:

class Chopstick(object):
    def __init__(self, length):
        self.length = length
        self.trials = []
        for row in chopsticks:
            if int(row[2]) == self.length:
                self.trials.append(Trial(row))
                
medium_chopstick = Chopstick(240)
print("medium_chopstick.length:", medium_chopstick.length)


# ###5: Average Efficiency

# ####Instructions

# Write an avg_efficiency method for our Chopstick class that returns the average food pinching efficiency for that chopstick. We recommend writing a num_trials method to help you with this implementation, since the method could be useful further down the line.
# 
# Store the average efficiency of chopsticks of length 210 in avg_eff_210.

# In[5]:

class Chopstick(object):
    def __init__(self, length):
        self.length = length
        self.trials = []
        for row in chopsticks:
            if int(row[2]) == self.length:
                self.trials.append(Trial(row))
                
    def num_trials(self):
        return len(self.trials)
    
    def avg_efficiency(self):
        efficiency_sum = 0
        for trial in self.trials:
            efficiency_sum += trial.efficiency
        return efficiency_sum / self.num_trials()
    
num_trials_210 = Chopstick(210).num_trials()
print("num_trials_210:", num_trials_210)

avg_eff_210 = Chopstick(210).avg_efficiency()
print("avg_eff_210:", avg_eff_210)


# ###6: Exceptions

# When programming, we usually try to avoid writing code that will produce errors. However, errors can be quite useful to us. An error tells us what went wrong with our code. We can use this information to help the logic of our program. If part of our code fails, we can check why it failed, and execute some other code instead.
# 
# We need a way to handle errors gracefully during the execution of our code so that our program doesn't crash. This is where exception handling comes into play.
# 
# An exception is a broad characterization of what can go wrong with a program. When a statement is syntactically correct, but something goes wrong when trying to execute it (e.g. a division by zero occurs or a non-existant file is read), the compiler raises an exception. An important distinction is that exceptions occur during the execution of the program, whereas syntax errors such as forgetting a colon or mispelling a variable are not.

# ###7: Exception Handling

# Typically when we write Python code, the interpretter will raise an exception (report an error) and keep executing the rest of the code after that exception is raised. We will see the exception, but our program will keep running as if it never happened. This is undesireable, because our program likely relies on previous statements being executed properly in order to succeed.
# 
# Instead, we want to handle exceptions. We want to observe when an exception is raised, and react accordingly. This way, every piece of code that is executed is executed deliberately, and we have complete control over what our program does. In Python, we use a try-except block to handle exceptions. Observe the following piece of code:
# 
#     try:
#         impossible_value = int("Not an integer")
#     except ValueError:
#         print("Cannot convert string to integer")
#     
# When the Python interpretter sees this code, it first attempts to execute the code in the try section of the statement. If any exceptions are raised within the try section (we hit some sort of error), our code will attempt to catch it, or gracefully handle it with different code. As it happens, our except statement will catch the exception because ValueError is the appropriate exception.
# 
# Now consider this code block:
# 
#     try:
#         f = open("data.txt", "r")
#         s = f.readline()
#         i = float(s)
#     except ValueError:
#         print("Cannot convert data to floating point value")
#     except IOError:
#         print("Could not read file")
# 
# Here, we caught a couple different types of exceptions that we suspected could arise during the execution of the try block.
# 
# Python offers the ability to catch any exception by simply writing an except: section without specifying an exception. This is a sort of "catch-all", and it works like an else: statement. However, using a catch-all for exceptions is usually bad practice. Trying to catch every exception without being specific is dangerous, since you can't execute exception-specific logic, and it means you may not understand your code as fully as you should.
# 
# If you catch every exception in one statement, you can't react to the exception that was raised because you have no idea what exception was raised. Instead, you should try catching as many specific exceptions as you possibly can. Think about what exceptions your code could cause, then catch and react to each one individually.
# 
# That being said, there are still times when a catch-all after you have caught all of your expected exceptions is a good idea. You may want to catch the unknown exception, store it somewhere so that later on you can find what went wrong, and change your code to handle that particular exception.

# ###8: Bad Data - Part 1

# We have a working program that can find the average efficiency for a length of chopstick. However, we need to account for what happens when we read in bad data. We'll handle this exception in our Trial class, since that's the class that handles reading the values in our dataset.

# ####Instructions

# Our Trial class's __init__ function uses floating point conversion and integer conversion. These conversions could fail with a ValueError exception. Catch this exception, and set each attribute to -1 if it occurs.
# 
# Create a Trial instance from the last row of our chopsticks dataset (chopsticks[-1]). Store this instance in bad_trial.

# In[6]:

class Trial(object):
    def __init__(self, datarow):
        try:
            self.efficiency = float(datarow[0])
            self.individual = int(datarow[1])
            self.chopstick_length = int(datarow[2])
        except ValueError:
            self.efficiency = -1.0
            self.individual = -1
            self.chopstick_length = -1

bad_trial = Trial(chopsticks[-1])
print("bad_trial.efficiency:", bad_trial.efficiency)


# ###9: Bad Data - Part 2

# While we wrote exceptions for handling bad data in the Trial class, we have not done the same for the Chopstick class.

# ####Instructions

# We set our Trial instance's attributes to -1 whenever we encountered bad data. Since we want to skip trials with bad data when populating a Chopstick instance's trials, verify that none of the attributes on the Trial instance are set to -1.

# In[7]:

class Chopstick(object):
    def __init__(self, length):
        self.length = length
        self.trials = []
        for row in chopsticks:
            if int(row[2]) == self.length:
                trial = Trial(row)
                if trial.efficiency != -1 and trial.individual != -1 and trial.chopstick_length != -1:
                    self.trials.append(trial)
                    
    def num_trials(self):
        return len(self.trials)
    
    def avg_efficiency(self):
        efficiency_sum = 0
        for trial in self.trials:
            efficiency_sum += trial.efficiency
        return efficiency_sum / self.num_trials()

bad_chopstick = Chopstick(400)
print("bad_chopstick.length:", bad_chopstick.length)


# ###10: Division By Zero

# When we try to find the average efficiency for a chopstick length that isn't in our dataset, we end up dividing by zero in our avg_efficiency method. Thankfully, this throws a exception, and we can catch it.

# ####Instructions

# Modify the Chopstick class so that computing the average efficiency of a chopstick whose length is outside our data set returns -1.0. The Python interpreter will throw a ZeroDivisionError exception when trying to divide by zero. We must write a try-except statement to handle this.
# 
# Store the result of finding the average efficiency of a chopstick of length 100 in bad_average.

# In[8]:

class Chopstick(object):
    def __init__(self, length):
        self.length = length
        self.trials = []
        for row in chopsticks:
            if int(row[2]) == self.length:
                trial = Trial(row)
                if trial.individual >= 0:
                    self.trials.append(trial)
                    
    def num_trials(self):
        return len(self.trials)
    
    def avg_efficiency(self):
        efficiency_sum = 0
        for trial in self.trials:
            efficiency_sum += trial.efficiency
        try:
            return efficiency_sum / self.num_trials()
        except ZeroDivisionError:
            return -1.0
        
bad_average = Chopstick(100).avg_efficiency()
print("bad_average:", bad_average)


# ###11: Most Efficient Chopsticks - Part 1

# Now it's time to answer our question. We want to determine which chopstick is best by checking which chopstick length has the highest average food pinching efficiency. Because we defined our average efficiencies to be -1.0 for chopsticks with bad data, those averages won't interrupt our calculations. 0 is the lowest possible average efficiency, so -1.0 shouldn't be an issue.

# ####Instructions

# We've provided you with a list of chopstick lengths called chopstick_lengths. Some of these lengths are not in our dataset, but we've already made sure our code is robust enough to ignore them.
# 
# Use a list comprehension to convert this list of chopstick lengths into a list of Chopstick instances. Store the resultant list in chopstick_list.

# In[9]:

chopstick_lengths = [180, 195, 210, 225, 240, 255, 270, 285, 300, 315, 330]
chopstick_list = [Chopstick(length) for length in chopstick_lengths]
print("chopstick_list.length:", chopstick_list[0].length, chopstick_list[1].length, chopstick_list[2].length)


# ###12: Most Efficient Chopsticks - Part 2

# ####Instructions

# Overload the __lt__ (<), __gt__ (>), __le__ (<=), __ge__ (>=), __eq__ (==), and __ne__ (!=) methods for the Chopstick class so that you can simply use Python's built in max function. Remember that each of these methods takes self and other as arguments, where each argument is an instance of our class.
# 
# Use the max function to store the most efficient chopstick in most_efficient.

# In[10]:

class Chopstick(object):
    def __init__(self, length):
        self.length = length
        self.trials = []
        for row in chopsticks:
            if int(row[2]) == self.length:
                trial = Trial(row)
                if trial.individual >= 0:
                    self.trials.append(trial)
                    
    def num_trials(self):
        return len(self.trials)
    
    def avg_efficiency(self):
        efficiency_sum = 0
        for trial in self.trials:
            efficiency_sum += trial.efficiency
        try:
            return efficiency_sum / self.num_trials()
        except ZeroDivisionError:
            return -1.0
        
    def __lt__(self, other):
        return self.avg_efficiency() < other.avg_efficiency()
    def __gt__(self, other):
        return self.avg_efficiency() > other.avg_efficiency()
    def __le__(self, other):
        return self.avg_efficiency() <= other.avg_efficiency()
    def __ge__(self, other):
        return self.avg_efficiency() >= other.avg_efficiency()
    def __eq__(self, other):
        return self.avg_efficiency() == other.avg_efficiency()
    def __ne__(self, other):
        return self.avg_efficiency() != other.avg_efficiency()
    
chopstick_list = [Chopstick(length) for length in chopstick_lengths]
most_efficient = max(chopstick_list)
print("most_efficient.length:", most_efficient.length)

