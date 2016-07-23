

```python
from __future__ import print_function
```

#Data Structures and Algorithms

##Data Structures

###1: What is a data structure?

A data structure is a way of organizing data. Lists and dictionaries are examples of data structures we have already seen, but there are many more. Specifically, data structures are concerned with organization of data within a program, rather than raw data that is read into a program.

The choice of data structure is driven by a few factors. First, and most importantly, is the structure of the data we are storing. If we want to store a bunch of strings with no other related data, we would just use a list.

Another factor to consider when choosing a data structure is time efficiency. Inserting, deleting, or finding items in data structures may take different amounts of time for different data structures, which is important when we want to be processing data efficiently.

###2: Arrays

The most basic data structure is an array. Arrays are simply lists that contain items.

Computer memory can be thought of as a long chain of memory slots. Arrays are stored in memory in a very easy, intuitive way. The first element of an array is stored right next to the second element, which is next to the third, and so on. Each element in an array occupies a slot in that array. So, in an array of 10 elements, we can say definitively which item is in the first slot, the second slot, etc.

Since this storage pattern is very predictable, it's very easy to access a given element by its index. However, since the elements all have to be shifted when we delete or add an element to the middle of the list, those operations can be quite costly.

Arrays typically cannot be expanded beyond their initial size. So, if we create an array of size 10, it can only hold 10 elements.

###3: Dynamic arrays

Dynamic arrays are a flavor of array that can be expanded to fit as many elements as we'd like. These are much more useful in data science than fixed-size arrays.

Many languages have primitive arrays build into the language. A primitive data structure can be used without having to manually implement the data structure or include any external libraries.

Python doesn't have a primitive, fixed-size array implementation build into the language. However, the Python list primitive is really just a dynamic array, so we'll be using lists to get familiar with array operations.

####Instructions

Read the commented descriptions of array operations. Based on the description and your knowledge of time complexity, set the variable below to "constant", "logarithmic", or "linear", depending on the complexity you believe the operation has.


```python
# Retrieving an item in an array by index
retrieval_by_index = ""

# Searching for a value in an unordered array
search = ""

# Deleting an item from an array, and filling the gap
#     by shifting all later items back by one
deletion = ""

# Inserting an item into the array, and shifting forward
#     every item that comes after it
insertion = ""
retrieval_by_index = "constant"
search = "linear"
deletion = "linear"
insertion = "linear"
```

###4: Array insertion practice

Let's practice inserting values into arrays.

####Instructions

Use the list insert function to insert "Evan Turner" and "Quincy Acy" into players so that players is in order alphabetically by last name.

The first argument to insert is the index at which the value should be inserted, and the second argument is the value itself. For instance,

    players.insert(1, "C.J. Watson")

inserts "C.J. Watson" at index 1 of players. The items in players that come after index 0 must shift over to make room for "C.J. Watson".

Print the list after each operation is performed, so that you can visualize how each operation affects the list.


```python
players = ["Reggie Jackson"]
print("players:", players)

players.insert(1, "C.J. Watson")
print("players:", players)

players.insert(0, "Jeff Adrien")
print("players:", players)

players.remove("Reggie Jackson")
print("players:", players)

players.insert(0, "Quincy Acy")
players.insert(2, "Evan Turner")
```

    players: ['Reggie Jackson']
    players: ['Reggie Jackson', 'C.J. Watson']
    players: ['Jeff Adrien', 'Reggie Jackson', 'C.J. Watson']
    players: ['Jeff Adrien', 'C.J. Watson']
    

###5: 2-Dimensional Arrays

So far we've been working with 1-dimensional arrays. They're 1-dimensional because they are a list in only one direction. A 1-D array has only a length, and no other dimension.

On the other hand, a 2-dimensional array has a height and a width. Consequently, they also have 2 indices. The element in the 3rd row and 4th column of the array arr can be accessed like so:

    arr[2][3]

The indexing still follows familiar conventions, like 0-indexing, but there are more indices now.

Imagine a stack of checkers. The stack has a height, and that's the only significant dimension. It has a bottom, and a top, and in between is a number of checkers, either black or red. This checker tower is like a 1-D array.

However, when you play checkers you are moving the checkers around on a 2-D board. There is a height and a width. Two dimensions. Checkers can move forwards, backwards, left, right. We refer to a space by row and column, yet each space still stores one piece of data (the checker). This is analogous to a 2-D array.

In data science, 1-dimensional arrays are called vectors, and 2-dimensional arrays are called matrices. You may already be familiar with these terms from previous missions.

###6: 2-D Array Implementation

There are a number of ways to implement a 2-D array. One implementation is to simply have an array full of arrays. This may be difficult to visualize at first, but with a few guided examples it's simple enough.

Imagine we are trying to access the element at row 2, column 5. What we are really doing is accessing the fifth element of the second row. So, first we access the second row. Then we access the fifth element in that row. In other words, our 2-D array is really just a 1-D array of rows. So, when we write

    arr[1][4]

we can view it equivalently as

    (arr[1])[4]

where we first access the desired row, and then the desired element within that row.

####Instructions

We have loaded a checker_board variable filled with "red" and "black" pieces, and "blank" spaces. Each slot contains the string "red", "black", or "blank".

Store the number of red pieces in red_pieces, and the number of black pieces in black_pieces.

You will have to use 2 for loops, one within the other.


```python
checker_board = [['blank', 'blank', 'blank', 'blank', 'blank', 'black', 'blank', 'blank'], 
                 ['blank', 'blank', 'red', 'blank', 'blank', 'blank', 'blank', 'blank'], 
                 ['blank', 'blank', 'blank', 'black', 'blank', 'red', 'blank', 'blank'], 
                 ['red', 'blank', 'black', 'blank', 'blank', 'blank', 'red', 'blank'], 
                 ['blank', 'blank', 'blank', 'black', 'blank', 'red', 'blank', 'blank'], 
                 ['blank', 'blank', 'black', 'blank', 'blank', 'blank', 'blank', 'blank'], 
                 ['blank', 'blank', 'blank', 'black', 'blank', 'blank', 'blank', 'blank'], 
                 ['blank', 'blank', 'red', 'blank', 'red', 'blank', 'red', 'blank']]
red_pieces = 0
black_pieces = 0

# Find how many red and black pieces there are
for row in checker_board:
    for piece in row:
        if piece == "red":
            red_pieces += 1
        elif piece == "black":
            black_pieces += 1
            
print("red_pieces:", red_pieces)
print("black_pieces:", black_pieces)
```

    red_pieces: 8
    black_pieces: 6
    

###7: 2-D Array Time Complexity

We can't fully understand a data structure without first analyzing it's time complexity. 2-D arrays are tricky though. We haven't really discussed whether our 2-D array can be expanded, and even if it could, it's a bit awkward to do so.

For the sake of simplicity, let's make a few assumptions about the 2-D arrays we are using. First and foremost, let's assume they are static. In other words, their size does not change. Another simplifying assumption that follows is that insertion into our 2-D arrays simply replaces whatever element was there, and that deletion leaves an "empty" slot in the array.

The only interesting complexity analysis is accessing elements of a 2-D array. Since deletion and insertion replace elements, their complexities will be the same as array access because we must always first find the element we are dealing with.

Accessing by index is constant time because we're really dealing with an array of arrays. Accessing the row is constant time, since the row is just an element in a regular array. Then accessing the element within that row is constant time again. Nothing depends on the size of the array, so it is simply constant time.

Now let's consider searching for an element (accessing by value). Let's call the height of our array m, and the width n. Behind the scenes, we are really working with an array of size m, where each element in the array is an array of size n. This is simply the array-of-arrays implementation we discussed earlier.

Let's say we are searching for an element. In the worst case, we must touch every slot in the array once to find what we are looking for. Since the array is m rows by n columns, there are m * n total slots. We touch each slot once, so our time complexity is O(m * n).

This looks a bit different from time complexities we've seen before, but we need to remember what time complexity represents. Our input size is expressed in both height and width, and the time our search takes increases as either m or n grows. Thus, O(m * n) makes sense for the time complexity of a 2-D array traversal.

###8: Hash Tables/Dictionaries

A hash table is a useful data structure that stores data based on key-value pairs. When using a hash table, you use the key to locate the data in the table.

One of the most common forms of a hash table is a dictionary, where the keys are almost always strings. Let's say we're storing the populations of cities around the world. We choose to store them in a dictionary, called city_populations. If we want to find the population of "Boston", we simply write

city_populations["Boston"]

The population is accessed quickly in one operation, and we don't need to worry about searching for the city. The hash table takes care of that for us.

###9: Dictionary Access

We will focus on dictionaries that use strings as keys, and any data type as values. We access a dictionary value using square brackets in the following fashion:

    myDict["key"]

Setting dictionary values is done in a very similar way:

    myDict["key"] = myValue

####Instructions

We have loaded a city_populations dictionary for you to use.

Assign the population of "Boston" to boston_population.

Assign the population of "Paris" to paris_population.

Your friend just moved from "Boston" to "Beijing". Subtract 1 from the population of "Boston", add 1 to the population of "Beijing", and store the result back in city_populations.


```python
city_populations = {'Rio de Janeiro': 6320000, 'Beijing': 11510000, 'Paris': 2244000, 'Boston': 645966}

rio_population = city_populations["Rio de Janeiro"]
boston_population = city_populations["Boston"]
paris_population = city_populations["Paris"]

city_populations["Beijing"] += 1
city_populations["Boston"] -= 1
```

###10: Hash Table Implementation

Behind the scenes, a hash table is just a big array. Recall that accessing array elements by index is very quick. A hash table is a clever construct that takes advantage of this property by converting keys to indices using a hash function. A hash function takes a key as input, and outputs an integer index. This way, we can find the appropriate index for any key.

Let's say our city_populations dictionary contains 10 cities. We could write a hash function that converts a city name to the indices between 0 and 9, but it's very likely that multiple city names would be converted to the same index. When two keys map to the same index, we have a collision. We want to avoid collisions.

Let's instead implement our hash table using an array of size 10000. It seems excessive, but we can add plenty of cities to our hash table without having to worry much about collisions.

Imagine we want to store the population of "New York". Our hash function takes the string "New York", performs some fancy operations on it, and returns some index, let's assume 4955. It then stores the population of New York in slot 4955. When we later want to access the population of New York, it does exactly the same thing: compute the index, and retrieve the population.

Even when we use large arrays, collisions can still happen. There are ways to resolve these collisions, but the details aren't really important. Just know that collisions are inefficient and undesirable, and larger arrays lead to fewer collisions.

###11: Hash Table Analysis

Accessing and storing in hash tables is very quick, so what's the trade-off? Hash tables need to be very large in order to minimize collisions and maximize time efficiency. However, maximizing time efficiency in this case hurts space efficiency. In other words, using a hash table uses a lot of memory.

Imagine, for some reason, that a group of about 30 people in an auditorium are organizing themselves by birthday. There is a seat in the auditorium for every day in the year. Each person sits in his/her appropriate seat, and they all fit in the auditorium.

Somebody with a clipboard of birthdays and names can now easily find any person by going to the seat corresponding to his/her birthday, even if they are total strangers.

However, a lot of space in the auditorium has been wasted so that these 30 people could play their silly game. If somebody else needs to use the room, they are confined to using less space.

This is analogous to the space efficiency trade-off of a hash table. There is a lot of empty space in most hash tables, and empty space is wasted space in computer memory. If that memory is precious to us, we may want to consider another data structure. However, if we have plenty of space to spare and would rather optimize for time, hash tables are a good candidate due to quick item accessing.

Hash tables are the perfect example of trade-offs in computer science. By using a hash table, we are getting time efficiency at the cost of space efficiency.

###12: Choosing a data structure

Now that we've seen a few data structures, it's important to be able to choose which data structure to use in any situation. Having many data structures to choose from is only useful if we know how to use them.

Which data structure best fits a particular problem is rarely an easy choice. There are a lot of trade-offs to consider. You want to optimize the time that your program takes, while also choosing data structures that easily represent your data.

We have provided a set of scenarios for which you will choose an appropriate data structure. We have provided enough description of each scenario that there is a clear best option among the data structures we have learned in this mission. Though this is rarely the case in most applications of data structures, this exercise will help you recall and reason about the trade-offs for each data structure.

####Instructions

After each scenario, set the appropriate variable to the values "static array", "dynamic array", "2d array", or "hash table", depending on which data structure you feel is most appropriate.

In this exercise, we focus primarily on the nature of the data, since each data structure is very different from one another.


```python
# Scenario A: You need to keep track of people sitting in an auditorium for a play. You will have to identify which seats are empty, and sell tickets until the auditorium is completely full. How will you store the names of who is sitting where?
scenario_A_data_structure = ""

# Scenario B: You are in charge of maintaining a guest list for a wedding. You are only concerned with a list of who is coming to the party. You have to add someone's name whenever they RSVP that they will be attending the wedding.
scenario_B_data_structure = ""

# Scenario C: Now every person who RSVP's for the wedding indicates which meal they will be eating. You have to keep track of the person, and the meal order. You need to be able to quickly find out what meal a particular person ordered, so that the waiters don't delay too long when it comes time to eat.
scenario_C_data_structure = ""
scenario_A_data_structure = "2d array"
scenario_B_data_structure = "dynamic array"
scenario_C_data_structure = "hash table"
```
