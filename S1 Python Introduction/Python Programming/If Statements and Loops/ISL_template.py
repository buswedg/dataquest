
# coding: utf-8

# In[1]:

from IPython.display import HTML

HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>''')


# #Python Programming

# ##If Statements and Loops

# ###1: Opening files

# A counter is a map from values to their frequencies. If you initialize a counter with a string, you get a map from each letter to the number of times it appears. If two words are anagrams, they yield equal Counters, so you can use Counters to test anagrams in linear time.

# In[2]:

# We can open files with the open function.
# The open function returns a file object, which we store in a variable so that we can use it later.
b = open('data/crime_rates.csv', 'r')


# ###2: CSV files

# crime_rates.csv stores the data on crime rates. This data will help us find the city with the lowest violent crime. We can use the .read() method to read the data in the file into a variable. Methods are different from functions in that they are associated with a specific object. We will get more into objects and classes later on, but for now, it is enough to know that methods act on objects, whereas functions are global, and unattached to any specific objects.

# In[4]:

f = open("data/crime_rates.csv", 'r')

b = f.read()


# ###3: Making a list

# We can make a list by using square brackets. An empty list can be initialized by using []. We can also initialize lists with elements in them by doing something like [1,10,3]. Lists can contain any type of variable, including strings, floats, and integers.

# In[5]:

# We can make an empty list with square brackets
a = []

# We can also initialize a list with values inside of it
b = [1, "I'm a string in a list!", 5.1]
c = [1,2,3]
d = [1,2,3]
e = ["hello", "bye", "hi"]
f = [5.1, 3.4, 10.5]


# ###4: Indexing a list

# We can get values from a list by using square brackets, along with an index. Python is a 0-indexed language, so we start counting at 0.

# In[6]:

# We can get values from lists by using an index.
sample_list = [10, "Boris Yeltsin", 50]
b = sample_list[0]

c = [1, "Mikhail Gorbachev", 10.5]
d = c[0]
e = c[1]
f = c[2]


# ###5: Splitting a CSV file

# Remember how strings are also objects? Well, we can use the .split method to split strings. The .split method takes a character as input, and then turns a string into a list of strings.

# In[7]:

# We can split a string into a list.
a_string = "This\nis\na\nstring\n"
split_string = a_string.split('\n')
print(split_string)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncan chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

f = open('data/crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')


# ###6: The manual way -- doing it without loops

# Before we make a loop, let's try doing a repetitive task without loops.

# In[8]:

# We have a list, the_list
the_list = [3,5,8,10,15,17,19]

# We can print the first element out
print(the_list[0])
print(the_list[0])
print(the_list[1])
print(the_list[2])
print(the_list[3])
print(the_list[4])
print(the_list[5])
print(the_list[6])


# ###7: Now let's add loops to the equation

# We can loop over lists using the for i in the_list: notation. The area inside the for loop is indented 4 spaces, and will be run once for every item in the list. The variable i will be assigned the value of each element of the list in turn.

# In[9]:

# We can loop over each item in a list.
a = [5, 10, 15]
for i in a:
    print(i)

# The whole block underneath a for loop needs to be indented 4 spaces, and is run once for each item in the list.

the_list = [3,5,8,10,15,17,19]
for i in the_list:
    print(i)


# ###8: Multiline for loops

# There can be multiple indented lines inside a for loop. The first line that isn't indented will mark the end of the loop.

# In[10]:

# We can have multiple lines underneath a for loop.
# The code above will go through the_list.
# At the end, sum will equal the sum of all of the items in the list doubled.
the_list = [3,5,8,10,15,17,19]
sum = 0
for i in the_list:
    # Double the value of i.
    double_i = i * 2
    # Add the doubled value to the sum.
    sum = sum + double_i
print(sum)

sum = 0
for i in the_list:
    triple_i = i * 3
    sum = sum + triple_i


# ###9: For loops with different variable names

# So far, we have been using for loops with the format for i in the_list. i is a special variable that will take on a different value every time through the loop. It takes on the value of each of the list elements in succession, starting from index 0. But we don't have to name the variable i. We can name it anything, as long as we refer to it inside the loop by the same name.

# In[11]:

# We can name the loop variable anything we want, it just has to be also used inside the loop.
the_list = [3,5,8,10,15,17,19]
sum = 0
for i in the_list:
    double_value = i * 2
    sum = sum + double_value
print(sum)

sum = 0
for value in the_list:
    triple_value = value * 3
    sum = sum + triple_value


# ###10: Lists of lists

# We can store integers, floats, and strings into lists. We can also store other lists. [[1,2,3], [4,5,6], [7,8,9]] is a valid list. When we index the outer list, we get an inner list as the result.

# In[12]:

# Create a list of lists
lolists = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]

# We can pull out the first element of the list, which is [1,2,3].
# Since [1,2,3] is a list, we can also index it to get elements out.
a = lolists[0]
b = a[0]
list1 = lolists[1]
value_1_0 = list1[0]
value_1_2 = list1[2]

list2 = lolists[2]
value_2_0 = list2[0]
value_2_2 = list2[2]


# ###11: Skipping the assignment

# When a statement or function returns a variable, we can directly manipulate it instead of assigning it to a variable first.

# In[13]:

# Create a list of lists
lolists = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]

# Pulls out the first element in the first list.
a = lolists[0][0]

# Pulls out the third element in the second list.
b = lolists[1][2]

# We can also directly do math with expressions.
c = lolists[0][2] + 10

# Any expression in python can be manipulated without first assigning it to a variable.
d = 10
e = d * lolists[2][0]


# ###12: Looping through lists of lists

# When we loop through a list of lists, the loop variable will be a list at each iteration. We can do computation inside the loop and pull values out of the list with indexing.

# In[15]:

lolists = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]

for inner_list in lolists:
    # This will loop through and print each inner list, starting from the one at index 0.
    print(inner_list)
    
for inner_list in lolists:
    print(inner_list[0])


# ###13: Adding to lists

# We can use the .append method to add to a list. list.append(10) will add the element 10 to the end of the list.

# In[17]:

# The append method adds items to the end of lists.
# a will go from having no items in it to having 10 at index 0.
a = []
print(a)
a.append(10)
print(a)

# b will go from having one item to having two items.
b = [30]
print(b)
b.append(50)
print(b)

# We can setup an old list with items, and an empty new list.
old_list = [1,2,5,10]
new_list = []

# At the end of this loop, new_list will be equal to old_list.
# The loop will have gone through each item in old_list, starting from index 0, and appended it to the end of new_list.
for item in old_list:
    new_list.append(item)
print(new_list)

c = [20,30]
c.append(60)
c.append(70)


# ###14: Splitting the csv file into columns

# When we left off with parsing our csv file, we had split it into rows, but still had to split up the strings we were left with into columns. We can use the .split method, along with our newfound knowledge of for loops and lists of lists, to split up the file.

# In[18]:

# We can use the .split method, with a comma as an input, to split a string on a comma.
# a_list is a list with 1,10,15, and 20 as elements.
a_string = "1,10,15,20"
a_list = a_string.split(",")
print(a_list)
print(type(a_list))
print(a_list[0])

# We split our csv file data into rows earlier.
f = open('data/crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')

full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)


# ###15: Finding the number of rows

# We can iterate over the data to count up the number of rows.

# In[19]:

# Remember how we counted the length of our list before?
# When the loop finishes, count will be equal to 5, which is the number of items in the_list.
# This is because 1 will be added to count for every iteration of the loop.
the_list = [5,6,10,13,17]
count = 0
for item in the_list:
    count = count + 1

# We can parse our csv file like we did before.
f = open('data/crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
count = 0
for row in full_data:
    count = count + 1


# ###16: Finding the number of columns

# Now that we understand the table structure better, we can count up the number of columns.

# In[20]:

# We just counted the number of rows.  We can do the same for the number of columns.
# Let's create a list of lists, and assume that the inner lists are the rows.
# If this is the case, the number of columns is the number of items in any row.
l = [[1,2,3],[3,4,5],[5,6,7]]
first_row = l[0]
count = 0
for column in first_row:
    count = count + 1

# Count is now equal to 3, the number of items in the first row of data.
# All of the rows have the same number of items, so 3 is our column count.

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


# ###17: Practicing with booleans

# Booleans can be used to compare equality and return True or False. Let's practice a bit with creating booleans.

# In[22]:

# Booleans are statements that take on either True or False as a value.
# We can create booleans by comparing two values and seeing if they are equal
# This will be False
print("Andre the Giant" == "Short")

# This is True
print("Andre the Giant" == "Andre the Giant")

# True and False are special python keywords of the boolean type.
# Boolean is abbreviated to bool.
print(type(True))
print(type(False))

a = 10
b = 5

# False
print(a == b)

# True
print(a == 10)

# Assigning a boolean to a variable
c = a == b
print(c)
d = a == 10
e = b == 5
f = a == 9
g = b == 4


# ###18: Booleans with greater than

# We can also use the greater than sign with booleans Saying 5 > 4 will evaluate to True, and 4 > 5 will be False.

# In[23]:

# This will be True
print(5 > 4)

# This is False
print(4 > 5)

# We can also assign these values to variables
# The value of a will be True, and it will be a boolean type
a = 5 > 4
print(a)
print(type(a))
b = 10 > 8
c = 8 > 10


# ###19: Booleans with less than

# We can also use the less than sign with booleans Saying 5 < 4 will evaluate to False, and 4 < 5 will be True.

# In[24]:

# Just like with the greater than sign, we can use the less than sign.
print(4 < 5)
print(5 < 4)

# We can assign these values to variables.
# They will be of the boolean type.
a = 4 < 5
print(a)
print(type(a))
b = 3 < 5
c = 5 < 3


# ###20: Using booleans in if statements

# You can use booleans to control when certain code gets executed. When the statement after the if statement is True, then the code runs. Otherwise, it doesn't.

# In[25]:

# If statements are followed by a boolean, which evaluates to True or False.
# If the boolean is True, the code is run.
# Otherwise, it isn't.
# Success! will be printed here.
if 4 == 4:
    print("Success!")

# Nothing will be printed here, because 10 doesn't equal 8.
if 10 == 8:
    print("No success!")
if 10 == 10:
    print("Hello world!")


# ###21: If statement with variables

# We can also use if statements with booleans that contain variables. if a == 5: will evaluate to True, and run the code inside the if statement.

# In[26]:

# We can also use if statements with boolean statements containing variables.
# The if statement below will print "Success!" because a == 4 evaluates to True.
a = 4
if a == 4:
    print("Success!")

# This will print nothing, because b > 10 is False.
b = 10
if b > 10:
    print("No success!")

c = 15
if c == 15:
    print("Much success!")


# ###22: Ifs and for loops, together at last!

# We can also use if statements inside for loops (or vice versa). When this happens, we need to indent everything in the inner block another 4 spaces.

# In[27]:

# We can 'nest' if statements inside for loops, or vice versa.
the_list = [5, 10, 15, 20]

# Let's say we want to count how many elements in the_list are greater than 10.
count = 0
for item in the_list:
    if item > 10:
        count = count + 1
print(count)

# Count equals two because item > 10 evaluated to True for 2 of the items in the_list.
# Notice how we indented the body of the if statement another 4 spaces.
# Whenever you put statements that have indented blocks inside each other, you will need to indent 4 more spaces.

a = 2

# Let's say we want to print all of the elements in the_list if a > 1.
if a > 1:
    for item in the_list:
        print(item)

# The above code will print all of the items in the_list, because a > 1 evaluates to True.
for item in the_list:
    if item > 5:
        print(item)


# ###23: Using if statements to find the smallest value

# Now that we know how we can combine if statements and for loops, we can learn how to use for loops to find minimum values.

# In[28]:

# We can use for loops and if statements to find the smallest value in a list.
the_list = [20,50,5,100]

# Set smallest_item to a value that is bigger than anything in the_list.
smallest_item = 1000
for item in the_list:
    # Check if each item is less than smallest_item.
    if item < smallest_item:
        # If it is, set smallest_item equal to its value.
        smallest_item = item
print(smallest_item)

# The first time through the loop above, smallest_item will be set to 20, because 20 < 1000 is True.
# The second time through, smallest_item will stay at 20, because 50 < 20 is False.
# The third time through, smallest_item will be set to 5, because 5 < 20 is True.
# The last time through, smallest_item will stay at 5, because 100 < 5 is False.

smallest_item = 1000
a = [500,10,200,5,78,-1,-10,-100,567,890,400,34,-101,895]
for item in a:
    if item < smallest_item:
        smallest_item = item


# ###24: Converting types

# We can convert between different data types. The int() function will convert an object to an integer.

# In[29]:

# There's one problem with our parsed CSV file -- because we parsed it from a string, all of the values are stored as strings.
# (go to the csv parsing and check types if you want to verify)
# We need the crime rate column s an integer so we can work with it.

# We can use the int() function to turn a string into an int.
# It only works with strings that have int values inside them.
a = '5'
print(type(a))

# a is a string containing the integer '5'.
# We can use the int function to parse it into the integer 5.
b = int(a)
print(b)
print(type(b))

c = '10'
d = '20'
e = '30'
c_int = int(c)
d_int = int(d)
e_int = int(e)


# ###25: Converting a list to integers

# Now, let's convert a list into integers.

# In[30]:

# Now that we know about the int() function, let's use it to convert the values in a list to integers.
the_list = ['1', '2', '3']
new_list = []

# Loop through the_list
for item in the_list:
    # Get the int value of the item in the list
    item_int = int(item)
    # Add the int item to the new list
    new_list.append(item_int)
# Print out the new list
print(new_list)

a = ['10', '15', '20', '35']
new_a = []
for item in a:
    item_int = int(item)
    new_a.append(item_int)


# ###26: Convert csv to integers

# Let's convert our crime rate column to integers while we are reading it in. In order to do this, we'll need to convert the values in the second column to integers after splitting the rows.

# In[ ]:

# We need to convert the crime rate values from our csv file into integers.
# They are strings now because we originally split them up from a large string we read in.

# Here's our csv reading code from before
f = open('data/crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')

full_data = []
for row in rows:
    split_row = row.split(",")
    split_row[1] = int(split_row[1])
    full_data.append(split_row)


# ###27: Finding the lowest crime rate

# We now know enough to find the lowest crime rate. We can scan through the list, and check if there is a lower crime rate in it.

# In[ ]:

# We now know everything we need to find the smallest crime rate.
# Remember that we are finding the smallest crime rate (second column), not the city (first column) with the lowest crime rate.
# We parse our csv file
f = open('data/crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    split_row[1] = int(split_row[1])
    full_data.append(split_row)

lowest_crime_rate = 10000
for row in full_data:
    crime_rate = row[1]
    if crime_rate < lowest_crime_rate:
        lowest_crime_rate = crime_rate


# ###28: Finding the lowest crime rate

# We can search a list for a value. We can do this by looping through the list, and then using an if statement.

# In[45]:

# We can search a list for a given value
the_list = [5, 6, 7, 10, 50]

# Loop through the_list
for item in the_list:
    # If the list item equals 5, print out "Found"
    if item == 5:
        print("Found")

# The above code will print "Found" once.

a = [500,10,200,5,78,-1,-10,-100,567,890,400,34,-101,895]
for item in a:
    if item == 78:
        print("Yes")


# ###29: Searching a list

# We can search a list for a value. We can do this by looping through the list, and then using an if statement.

# In[1]:

# We can search a list for a given value
the_list = [5, 6, 7, 10, 50]

# Loop through the_list
for item in the_list:
    # If the list item equals 5, print out "Found"
    if item == 5:
        print("Found")

# The above code will print "Found" once.

a = [500,10,200,5,78,-1,-10,-100,567,890,400,34,-101,895]
for item in a:
    if item == 78:
        print("Yes")


# ###30: Searching a list of lists

# Just like we can search through a list, we can search through a list of lists.

# In[46]:

lolist = [[1,5,7],[10,8,9],[7,10,11]]

# Let's say we want to get the first element of the inner list whose third element is 9.
value = 0
for item in lolist:
    last_value = item[2]
    first_value = item[0]
    if last_value == 9:
        value = first_value
print(value)

# The above code will print 10, which is the first value in the inner list where 9 is the last value.
# What we are doing can also be described in terms of rows and columns.
# We are finding the first column in the rows where the third column equals 9.

# Can you write code to find the second element in the inner list whose first element is 7? (search through lolist)
# Set the value variable equal to the answer.
value = 0
for item in lolist:
    if item[0] == 7:
        value = item[1]


# ###31: Finding the answer!

# We know the lowest crime rate, and we know how to search through lists. Let's combine the knowledge to find out the city with the lowest crime rate.

# In[ ]:

# We know that the lowest crime rate is 130.
# This is the second column of the data.
# We need to find the corresponding value in the first column -- the city with the lowest crime rate.

# Let's load the csv file
f = open('data/crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    split_row[1] = int(split_row[1])
    full_data.append(split_row)

city = ""
for row in full_data:
    if row[1] == 130:
        city = row[0]


# In[ ]:



