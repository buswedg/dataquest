
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Data Structures and Algorithms

# ##Recursion and Advanced Data Structures

# ###1: Recursion

# Recursion is a concept that's difficult to grasp at first, but a very rewarding and fun tool to those who understand it. Recursion is a method of repeating code, without using loops. It usually takes the form of a function which calls itself during its execution.
# 
# From this simple mechanism arises a shocking amount of interesting algorithms. Recursive algorithms often seem lazy when we write them, and can appear magical when they work. It's important to understand recursion so that you can think about problems in new ways, and write satisfying code that performs logic succinctly.
# 
# The best way to understand recursion is through example. A simple use case is the factorial function in mathematics. Here are some examples of the factorial function:
# 
#     3! = 3 * 2 * 1
#     5! = 5 * 4 * 3 * 2 * 1
# 
# A factorial is denoted using the ! sign, so n! denotes multiplying n by n - 1, then n - 2, and so on until 1.

# ###2: A recursive look at factorials

# Upon inspection, we can see a pattern in the factorial function. Let's break down the evaluation of 5!.
# 
#     5! = 5 * 4 * 3 * 2 * 1 = 5 * (4 * 3 * 2 * 1) = 5 * (4!)
# 
# We can see that 5! is really 5 * (4!). Let's pretend we already know how to evaluate 4!. Then suddenly, 5! becomes a very easy thing to calculate.
# 
# But how do we know how to calculate 4!? Well, it's just 4 * (3!). Easy.
# 
# How about 3!? Just 3 * (2!).
# 
# This pattern of evaluation continues, and we're never really doing much difficult computation. Notice with each step of the calculation, we are actually using the factorial function to help us compute a factorial. All we need to know now is where to stop.

# ###3: Base cases

# The last component we need to define our recursive function is a base case. Our function needs to know when to stop, otherwise it will just keep calling itself forever. In the case of our factorial function, we want to stop at 0, so we'll make that our base case.
# 
# When we call factorial with 0 as its input, we want to simply return 1. This may seem a bit odd, but mathematically, 0! is defined to be 1. We don't have to worry much about why this is, we'll just accept the definition and use it in our recursion. 1! still evaluates to 1 * (0!), which is 1.
# 
# When our input is not 0, we want to recursively call our function, performing whatever operations are necessary to properly execute our recursive algorithm.

# ####Instructions

# Read the recursive implementation of factorial below. It's nearly complete, but will run forever in its current form. Add our base case to ensure that the function stops.
# 
# Store the result of calling factorial on 1 in factorial1.
# 
# Store the result of calling factorial on 5 in factorial5.
# 
# Store the result of calling factorial on 25 in factorial25.

# In[2]:

# Recursive factorial function
def factorial(n):
    # Check the base case
    if n == 0:
        return 1
    # Recursive case
    return n * factorial(n - 1)

factorial1 = factorial(1)
print("factorial1:", factorial1)

factorial5 = factorial(5)
print("factorial5:", factorial5)

factorial25 = factorial(25)
print("factorial25:", factorial25)


# ###4: Visualization of Recursion

# So recursion works, but you may not be entirely convinced of how and why it works. To illustrate, we'll use a real-life example of a recursive algorithm.
# 
# Suppose you are sitting in an auditorium, and you'd like to know which row you are in. Let's assume the rows are not labelled.
# 
# You could count all of the rows in front of you, but that would take quite awhile. This is analogous to the iterative approach (using a loop). You are doing a lot of work. However, you realize there is a way to delegate that work to other people.
# 
# You ask the person in front of you what row he is in. When he responds, you can simply add 1 to that row number. That person does the same thing. He asks the person in front of him, and that person asks the person in front of him, and so on.
# 
# Each time a person is asked represents a function call. You are the first function call, the man in front of you is the next. However, none of the function calls are finished executing yet, since they are still waiting for responses. When finally the man in the front row is asked what row he is in, we have reached our base case. There is nobody ahead of him, so he knows that he is in row 1.
# 
# He responds that he is in row 1. The person behind him knows he/she is in row 2, and this information bubbles back up to you, with each person in the chain adding 1 to the response they receive. This bubbling-up is analogous to the base case being reached, and then each recursive call resolving itself one by one, with the most recently called functions ending first.
# 
# Finally, the man in front of you tells you his row number, you add 1, and you've found your answer. Each function call did very little work, and you still achieved a correct answer.

# ###5: Fibonacci

# The Fibonacci sequence is a famous series of numbers that starts out as follows:
# 
#     1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# 
# Each number in the Fibonacci sequence is the sum of the previous two numbers. For instance, 34 in the above sequence is the sum of 13 and 21.
# 
# The only exceptions are the first two numbers. Since the sequence is too short to calculate them, the first two numbers of the sequence are ones by definition. These two numbers are the base cases for the Fibonacci sequence.

# ####Instructions

# Recursively implement the function fib, which takes n as an argument and returns the nth Fibonacci number. Check our base case by checking if n is 0 or 1 (the indices of the first two Fibonacci numbers, which should both be 1).
# 
# Use recursive function calls that match the Fibonacci definition when n is not a base case.
# 
# Store the result of calling fib on 1 in fib1.
# 
# Store the result of calling fib on 5 in fib5.
# 
# Store the result of calling fib on 25 in fib25.

# In[3]:

def fib(n):
    # Check the base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return fib(n - 1) + fib(n - 2)

fib1 = fib(1)
print("fib1:", fib1)

fib5 = fib(5)
print("fib5:", fib5)

fib25 = fib(25)
print("fib25:", fib25)


# ###6: Linked Lists - A Recursive Data Structure

# Linked lists are very similar to arrays, but differ in how they are implemented. A linked list is made up of many nodes, each of which contains a few pieces of information, depending on the type of linked list we are implementing. We will implement a singly linked list.
# 
# In a singly linked list, each node contains its data, and the next node. Let's think about how this works. Suppose we want to access the data in the third node. From the first node, we can access its next node, which is the second. From that node, we can access its next node, which is the third node. We now have access to the data we were looking for. Each node is like an element in an array, except that it has some extra information (the next node) aside from just the data.
# 
# Linked lists are a recursive data structure. Each node contains the data, and then points to another linked list (the next node). This is a recursive definition for the data structure, since we include a linked list in the definition. The base case is our empty linked list, which we will represent with the Python None value.
# 
# Since linked lists are recursive, we can write a lot of interesting algorithms to work with them. Looping through a linked list is awkward, but we will see that recursing on them feels more natural.

# ###7: Linked List Length

# We said before that linked lists are recursive data structures. In recursive data structures, we can often take advantage of recursion to perform operations.
# 
# With a linked list, we can find the length of any linked list by adding 1 to the length of its tail list (the list after the first element). By recursing in this fashion, and only stopping when we reach the empty, or None, linked list, we can write a simple function without loops that calculates a linked list's length.
# 
# We have loaded a linked list of names for you to play with, called people. In our implementation, we can access the first node of a linked list with people.head(), and the rest of the linked list with people.tail(). We've also provided a helpful is_empty method for linked lists. people.is_empty() returns a boolean value.

# ####Instructions

# Read the iterative implementation of the length_iterative function, which returns the length of the given linked list.
# 
# Recursively implement the function length_recursive, which takes ls (a linked list) as an argument and returns the length of the linked list.
# 
# Store the result of calling length_recursive on people in people_length.
# 
# We've provided you with a print_list function to help you debug. It can be used by calling people.print_list().

# In[4]:

# First person's name
#first_item = people.head().get_data()

# Getting linked list length using iteration
def length_iterative(ls):
    count = 0
    while not ls.is_empty():
        count = count + 1
        ls = ls.tail()
    return count

# Getting linked list length using recursion
def length_recursive(ls):
    if ls.is_empty():
        return 0
    return 1 + length_recursive(ls.tail())

#people_length = length_recursive(people)


# ###8: Linked List Insertion and Deletion

# Since linked lists don't maintain a central index of any kind, searching for a specific node means starting from the first node and accessing the next node until the value is found or returning false if it isn't. This is inefficient, but linked lists do have some advantages.
# 
# One advantage of a linked list is that we need to modify very few nodes when inserting or deleting, since only a constant number of changes are necessary.
# 
# To understand linked list insertion and deletion, imagine a line of people with their hands on the backs of the person in front of them. If we want to add a person to this line, only one person needs to remove his/her hands, and place them on the new person's shoulders. The new person now puts his hands on the shoulders of the person in front of him, and nobody else needed to detach from their neighbors.
# 
# Similarly, if we want to remove someone from the line, his/her neighbor behind must let go, and then hold the shoulders of the next person, but nobody else needs to do anything.
# 
# In a linked list, very few nodes need to change when a new node is inserted or a node is deleted. This makes insertion and deletion very quick, as only a constant number of changes need to be made. In contrast, an array requires a lot of elements to shift when we perform insertions or deletions.
# 
# It's important to note that when we're discussing the time complexity of insertion and deletion, we already have immediate access to the node we're working with. If we need to search for a node to delete, or for the location where we'd like to insert a node, that would require some more time since we first need to find the node.

# ###9: Linked List Time Complexity

# ####Instructions

# Read the commented descriptions of linked list operations. Based on the description and your knowledge of time complexity, set the variable below to "constant", "logarithmic", or "linear", depending on the complexity you believe the operation has.

# In[5]:

# Retrieving an item in the linked list by index
retrieval_by_index = ""

# Retrieving an item in the linked list by value
retrieval_by_value = ""

# Deleting an item from the linked list, with access to the item and 
#     the item before it
deletion = ""

# Inserting an item into the linked list, with access to the location
#     where we are inserting
insertion = ""

# Calculating the length of a linked list using a loop
length_iterative = ""

# Calculating the length of a linked list using recursion
length_recursive = ""
retrieval_by_index = "linear"
retrieval_by_value = "linear"
deletion = "constant"
insertion = "constant"
length_iterative = "linear"
length_recursive = "linear"

