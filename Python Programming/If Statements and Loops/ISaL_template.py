
# coding: utf-8

# #Python Programming

# ##If Statements and Loops

# ###1: Opening files

# A counter is a map from values to their frequencies. If you initialize a counter with a string, you get a map from each letter to the number of times it appears. If two words are anagrams, they yield equal Counters, so you can use Counters to test anagrams in linear time.

# In[7]:

# Open the csv file with the open function and assign to 'b'.
b = open('data/crime_rates.csv', 'r')


# ###2: CSV files

# crime_rates.csv stores the data on crime rates. This data will help us find the city with the lowest violent crime. We can use the .read() method to read the data in the file into a variable. Methods are different from functions in that they are associated with a specific object. We will get more into objects and classes later on, but for now, it is enough to know that methods act on objects, whereas functions are global, and unattached to any specific objects.

# In[3]:

# Read the csv file.
b = open('data/crime_rates.csv', 'r')
b = b.read()

print "First 50 elements in list:"
print b[:50]


# ###3: Making a list

# We can make a list by using square brackets. An empty list can be initialized by using []. We can also initialize lists with elements in them by doing something like [1,10,3]. Lists can contain any type of variable, including strings, floats, and integers.

# In[25]:

# Make an empty list
a = []

# Can also initialize a list with values
b = [1, "I'm a string in a list!", 5.1]
print b

c = [1,2,3]
print c

d = [1,2,3]
print d

e = ["hello", "bye", "hi"]
print e

f = [5.1, 3.4, 10.5]
print f


# ###4: Indexing a list

# We can get values from a list by using square brackets, along with an index. Python is a 0-indexed language, so we start counting at 0.

# In[30]:

# Get values from lists by using an index.
sample_list = [10, "Boris Yeltsin", 50]
print sample_list

b = sample_list[0]
print "First element of sample_list: ", b

c = [1, "Mikhail Gorbachev", 10.5]
d = c[0]
e = c[1]
f = c[2]


# ###5: Splitting a CSV file

# Remember how strings are also objects? Well, we can use the .split method to split strings. The .split method takes a character as input, and then turns a string into a list of strings.

# In[4]:

# Create string.
a_string = "This\nis\na\nstring\n"
print a_string

# Split string into a list.
split_string = a_string.split('\n')
print split_string

# Create string.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncan chuck wood?"
print string_two

# Split string into a list.
split_string_two = string_two.split('\n')
print split_string_two

#f = open('data/crime_rates.csv', 'r')
#data = f.read()
#rows = data.split('\n')


# ###6: The manual way -- doing it without loops

# Before we make a loop, let's try doing a repetitive task without loops.

# In[5]:

# Create list.
the_list = [3,5,8,10,15,17,19]
print the_list

# Print list elements.
print the_list[0]
print the_list[1]
print the_list[2]
print the_list[3]
print the_list[4]
print the_list[5]


# ###7: Now let's add loops to the equation

# We can loop over lists using the for i in the_list: notation. The area inside the for loop is indented 4 spaces, and will be run once for every item in the list. The variable i will be assigned the value of each element of the list in turn.

# In[6]:

# Loop over each item in a list.
a = [5, 10, 15]
print a
for i in a:
    print i

# Loop over each item in a list.
the_list = [3,5,8,10,15,17,19]
print the_list
for i in the_list:
    print i


# ###8: Multiline for loops

# There can be multiple indented lines inside a for loop. The first line that isn't indented will mark the end of the loop.

# In[6]:

# Create list.
the_list = [3,5,8,10,15,17,19]
print the_list

# Loop over each list item and apply function.
sum = 0
for i in the_list:
    # Double the value of i.
    double_i = i * 2
    # Add the doubled value to the sum.
    sum = sum + double_i
print sum

# Loop over each list item and apply function.
sum = 0
for i in the_list:
    triple_i = i * 3
    sum = sum + triple_i
print sum


# ###9: For loops with different variable names

# So far, we have been using for loops with the format for i in the_list. i is a special variable that will take on a different value every time through the loop. It takes on the value of each of the list elements in succession, starting from index 0. But we don't have to name the variable i. We can name it anything, as long as we refer to it inside the loop by the same name.

# In[9]:

# Create list.
the_list = [3,5,8,10,15,17,19]
print the_list

# Loop over each list item and apply function.
sum = 0
for i in the_list:
    double_value = i * 2
    sum = sum + double_value
print sum

# Loop over each list item and apply function.
sum = 0
for value in the_list:
    triple_value = value * 3
    sum = sum + triple_value
print sum


# ###10: Lists of lists

# We can store integers, floats, and strings into lists. We can also store other lists. [[1,2,3], [4,5,6], [7,8,9]] is a valid list. When we index the outer list, we get an inner list as the result.

# In[10]:

# Create a list of lists.
lolists = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]
print lolists

# Pull out the first element of the list, which is [1,2,3].
a = lolists[0]
print a

# Since [1,2,3] is a list, it can also be indexed.
b = a[0]
print b

list1 = lolists[1]
print list1

value_1_0 = list1[0]
print value_1_0
value_1_2 = list1[2]
print value_1_2

list2 = lolists[2]
print list2

value_2_0 = list2[0]
print value_2_0
value_2_2 = list2[2]
print value_2_2


# ###11: Skipping the assignment

# When a statement or function returns a variable, we can directly manipulate it instead of assigning it to a variable first.

# In[14]:

# Create a list of lists.
lolists = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]
print lolists

# Pull out the first element in the first list.
a = lolists[0][0]
print a

# Pull out the third element in the second list.
b = lolists[1][2]
print b

# Directly do math with expressions.
c = lolists[0][2] + 10
print c

# Directly do math with expressions.
d = 10
e = d * lolists[2][0]
print e


# ###12: Looping through lists of lists

# When we loop through a list of lists, the loop variable will be a list at each iteration. We can do computation inside the loop and pull values out of the list with indexing.

# In[16]:

lolists = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]
print lolists

# Loop through and print inner lists.
for inner_list in lolists:
    print(inner_list)
    
# Loop through and print first element of each inner list.
for inner_list in lolists:
    print(inner_list[0])


# ###13: Adding to lists

# We can use the .append method to add to a list. list.append(10) will add the element 10 to the end of the list.

# In[12]:

# Create empty list.
a = []
print a

# Append value to list.
a.append(10)
print a

# Create list with value.
b = [30]
print b

# Append value to list.
b.append(50)
print b

old_list = [1,2,5,10]
new_list = []

# Use loop to append values to list.
for item in old_list:
    new_list.append(item)
print new_list

c = [20,30]
c.append(60)
c.append(70)


# ###14: Splitting the csv file into columns

# When we left off with parsing our csv file, we had split it into rows, but still had to split up the strings we were left with into columns. We can use the .split method, along with our newfound knowledge of for loops and lists of lists, to split up the file.

# In[42]:

a_string = "1,10,15,20"
a_list = a_string.split(",")
print a_list
print type(a_list)
print a_list[0]

f = open('data/crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')

full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)


# ###15: Finding the number of rows

# We can iterate over the data to count up the number of rows.

# In[40]:

# Create list.
the_list = [5,6,10,13,17]
print the_list

# Count number of items in list.
count = 0

for item in the_list:
    count = count + 1
    
print "Number of items in list: ", count


f = open('data/crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
    
    
# Count number of items in list.
count = 0

for row in full_data:
    count = count + 1
    
print "Number of items in list: ", count


# ###16: Finding the number of columns

# Now that we understand the table structure better, we can count up the number of columns.

# In[38]:

# Create list of lists.
l = [[1,2,3],[3,4,5],[5,6,7]]
print l

first_row = l[0]
count = 0
for column in first_row:
    count = count + 1
    
print "Columns in first row: ", count


# We parse our csv file
f = open('data/crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
    
first_row = full_data[0]
count = 0
for column in first_row:
    count = count + 1

print "Columns in first row: ", count


# ###17: Practicing with booleans

# Booleans can be used to compare equality and return True or False. Let's practice a bit with creating booleans.

# In[13]:

# Create boolean by comparing two values.
print "Andre the Giant" == "Short"
print "Andre the Giant" == "Andre the Giant"

# True and False are special python keywords of the boolean type.
print type(True)
print type(False)

a = 10
b = 5

# False
print a == b

# True
print a == 10

# Assigning boolean to a variable.
c = a == b
print c

d = a == 10
e = b == 5
f = a == 9
g = b == 4

print d
print e
print f
print g


# ###18: Booleans with greater than

# We can also use the greater than sign with booleans Saying 5 > 4 will evaluate to True, and 4 > 5 will be False.

# In[14]:

# Create boolean by comparing two values.
print 5 > 4
print 4 > 5

# Assigning boolean to a variable.
a = 5 > 4
print a
print type(a)

b = 10 > 8
c = 8 > 10

print b
print c


# ###19: Booleans with less than

# We can also use the less than sign with booleans Saying 5 < 4 will evaluate to False, and 4 < 5 will be True.

# In[15]:

# Create boolean by comparing two values.
print 4 < 5
print 5 < 4

# Assigning boolean to a variable.
a = 4 < 5
print a
print type(a)

b = 3 < 5
c = 5 < 3

print b
print c


# ###20: Using booleans in if statements

# You can use booleans to control when certain code gets executed. When the statement after the if statement is True, then the code runs. Otherwise, it doesn't.

# In[16]:

# Create 'if' statement based on boolean by comparing two values.
if 4 == 4:
    print "Success!"

# Create 'if' statement based on boolean by comparing two values.
if 10 == 8:
    print "No success!"
if 10 == 10:
    print "Hello world!"


# ###21: If statement with variables

# We can also use if statements with booleans that contain variables. if a == 5: will evaluate to True, and run the code inside the if statement.

# In[17]:

a = 4
b = 10
c = 15

# Create 'if' statement based on boolean by comparing two values.
if a == 4:
    print "Success!"

# Create 'if' statement based on boolean by comparing two values.
if b > 10:
    print "No success!"

# Create 'if' statement based on boolean by comparing two values.
if c == 15:
    print "Much success!"


# ###22: Ifs and for loops, together at last!

# We can also use if statements inside for loops (or vice versa). When this happens, we need to indent everything in the inner block another 4 spaces.

# In[18]:

the_list = [5, 10, 15, 20]
print the_list

# Count how many elements in the_list are greater than 10.
count = 0
for item in the_list:
    if item > 10:
        count = count + 1
print count


a = 2

# Print all of the elements in the_list if a > 1.
if a > 1:
    for item in the_list:
        print item

# Print all of the elements in the_list if item > 5.
for item in the_list:
    if item > 5:
        print item


# ###23: Using if statements to find the smallest value

# Now that we know how we can combine if statements and for loops, we can learn how to use for loops to find minimum values.

# In[24]:

the_list = [20,50,5,100]
print the_list

# Set 'smallest_item' to a value that is bigger than anything in 'the_list'.
smallest_item = 1000
for item in the_list:
    # Check if each item is less than smallest_item.
    if item < smallest_item:
        # If it is, set smallest_item equal to its value.
        smallest_item = item
        
print "Smallest item in list: ", smallest_item


# Set smallest_item to a value that is bigger than anything in the_list.
smallest_item = 1000

a = [500,10,200,5,78,-1,-10,-100,567,890,400,34,-101,895]
print a

for item in a:
    if item < smallest_item:
        smallest_item = item
        
print "Smallest item in list: ", smallest_item


# ###24: Converting types

# We can convert between different data types. The int() function will convert an object to an integer.

# In[21]:

# There's one problem with our parsed CSV file -- because we parsed it from a string, all of the values are stored as strings.

# Use the int() function to turn a string into an int.
a = '5'
print a
print type(a)

# We can use the int function to parse it into the integer 5.
b = int(a)
print b
print type(b)

c = '10'
d = '20'
e = '30'
c_int = int(c)
d_int = int(d)
e_int = int(e)


# ###25: Converting a list to integers

# Now, let's convert a list into integers.

# In[25]:

# Use the 'int' function to convert values in a list to integers.
the_list = ['1', '2', '3']
print the_list

new_list = []
# Loop through the_list.
for item in the_list:
    # Get the int value of the item in the list.
    item_int = int(item)
    # Add the int item to the new list.
    new_list.append(item_int)
    
print new_list

a = ['10', '15', '20', '35']
print a

new_a = []
for item in a:
    item_int = int(item)
    new_a.append(item_int)


# ###26: Convert csv to integers

# Let's convert our crime rate column to integers while we are reading it in. In order to do this, we'll need to convert the values in the second column to integers after splitting the rows.

# In[17]:

f = open('data/crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')

# Convert crime rate to integer and store in full_data.
full_data = []
for row in rows:
    split_row = row.split(",")
    if row:
        split_row[1] = int(split_row[1])
        full_data.append(split_row)


# ###27: Finding the lowest crime rate

# We now know enough to find the lowest crime rate. We can scan through the list, and check if there is a lower crime rate in it.

# In[6]:

# Find city with lowest crime rate.
lowest_crime_rate = 10000
for row in full_data:
    crime_rate = row[1]
    if crime_rate < lowest_crime_rate:
        lowest_crime_rate = crime_rate

print "Lowest crime rate: ", lowest_crime_rate


# ###28: Searching a list

# We can search a list for a value. We can do this by looping through the list, and then using an if statement.

# In[26]:

the_list = [5, 6, 7, 10, 50]
print the_list

# Loop through 'the_list', if the list item equals 5, print out "Found".
for item in the_list:
    if item == 5:
        print "Found"

a = [500,10,200,5,78,-1,-10,-100,567,890,400,34,-101,895]

# Loop through 'a', if the list item equals 78, print out "Yes".
for item in a:
    if item == 78:
        print "Yes"


# ###29: Searching a list of lists

# Just like we can search through a list, we can search through a list of lists.

# In[27]:

lolist = [[1,5,7],[10,8,9],[7,10,11]]
print lolist

# Get the first element of the inner list whose third element is 9.
value = 0
for item in lolist:
    last_value = item[2]
    first_value = item[0]
    if last_value == 9:
        value = first_value
        
print value


# Get the second element in the inner list whose first element is 7.
value = 0
for item in lolist:
    if item[0] == 7:
        value = item[1]
        
print value


# ###30: Finding the answer!

# We know the lowest crime rate, and we know how to search through lists. Let's combine the knowledge to find out the city with the lowest crime rate.

# In[12]:

# We know that the lowest crime rate is 0.
# We need to find the corresponding value in the first column -- the city with the lowest crime rate.

f = open('data/crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')

full_data = []
for row in rows:
    split_row = row.split(",")
    if row:
        split_row[1] = int(split_row[1])
        full_data.append(split_row)

city = ""
for row in full_data:
    if row[1] == 0:
        city = row[0]

print "City with lowest crime rate: ", city

