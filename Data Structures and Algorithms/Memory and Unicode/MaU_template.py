
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Data Structures and Algorithms

# ##Memory and Unicode

# ###1: Intro to binary

# Computers can't directly store values like strings or integers.
# 
# Instead, they store information in binary -- the only valid numbers in binary are a 0 or a 1.
# 
# This lets data be stored on devices like hard drives -- we just learned how hard drives store data.
# 
# We normally count in base 10.
# 
# It's called base 10 because there are 10 possible digits -- 0 through 9.
# 
# Binary is base two, because there are only two possible digits - 0 and 1.
# 
# Let's explore how binary numbers work.

# ####Instructions

# Convert the binary number "100" to a base 10 integer. Assign the result to base_10_100.

# In[2]:

# Let's say 'a' is a binary number.  In Python, we have to store binary numbers as strings.
# Trying to say b = 10 directly will assume base 10, so strings are needed.
b = "10"
print("b:", b)

# We can convert 'b' to a binary number from a string using the int function.
# The optional second argument base is set to 2 (binary is base two).
print("int(b, 2):", int(b, 2))

base_10_100 = int("100", 2)
print("base_10_100:", base_10_100)

base_10_101 = int("101", 2)
print("base_10_101:", base_10_101)


# ###2: Binary addition

# Just like with base 10 numbers, we can add binary numbers together.

# ####Instructions

# Add "10" (base 2) to c.

# In[3]:

# 'a' is in base 10 -- because we have 10 possible digits, the highest value we can represent with one digit is 9.
a = 9
#print("a:", a)

# When we want to represent a value one higher, we need to add another digit.
a += 1

# 'a' now has two digits -- we incremented the invisible leading digit, which was 0 and is now 1, and set the last digit back to zero.
#print("a:", a)

# When we add 1 to 19, we increment the leading 1 by 1, and then set the last digit to 0, giving us 20.
a = 19
#print("a:", a)

a += 1
#print("a:", a)

# When we add 1 to 99, we increment the last digit by 1, and add 1 to the first digit, but the first digit is now greater than 9, so we have to increment the invisible leading digit.
a = 99
#print("a:", a)

a += 1
#print("a:", a)

# Binary addition works the exact same way, except the highest value any single digit can represent is 1.
b = "1"

# We'll add binary values using a binary_add function that was made just for this exercise.
# It's not extremely important to know how it works right this second.
def binary_add(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

c = binary_add(b, "1")

# We now see that 'c' equals "10", which is exactly what happens in base 10 when we reach the highest possible digit.
#print("c:", c)

# c now equals "11".
c = binary_add(c, "1")
#print("c:", c)

# c now equals "100".
c = binary_add(c, "1")
#print("c:", c)

# c now equals "110".
c = binary_add(c, "10")
#print("c:", c)


# ###3: Converting binary values

# We saw how we could convert between bases with the int() function.
# 
# Let's see what values in binary equal what values in base 10.

# ####Instructions

# Convert "1001" to base 10. Assign the result to base_10_1001.

# In[4]:

def binary_add(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

# Start both at 0.
a = 0
b = "0"

# Loop 10 times.
for i in range(0, 10):
    # Add 1 to each.
    a += 1
    b = binary_add(b, "1")

    # Check if they are equal.
    #print int(b, 2) == a

# The cool thing here is that a and b are always equal if you add the same amount to both.
# This is because base 2 and base 10 are just ways to write numbers.
# Counting 100 apples in base 2 or base 10 will always give you an equivalent result, you just have to convert between them.
# We can represent any number in binary, we just need more digits than we would in base 10.
base_10_1001 = int("1001", 2)
print("base_10_1001:", base_10_1001)


# ###4: Characters to binary

# Just like how integers are stored as binary, so are strings.
# 
# Strings are split into single characters, then converted into integers, which are then converted to binary and stored.
# 
# We'll look at simple characters first -- the so called ascii characters.
# 
# These contain all the upper and lowercase english letters, all the digits, and a lot of punctuation symbols.

# ####Instructions

# Convert "w" to binary. Assign the result to binary_w.
# 
# Convert "}" to binary. Assign the result to binary_bracket.

# In[5]:

# We can use the ord() function to get the integer associated with an ascii character.
print("ord('a'):", ord("a"))

# Then we use the bin() function to convert to binary.
# The bin function adds "0b" to the start of strings to indicate that they contain binary values.
print("bin(ord('a')):", bin(ord("a")))

# ÿ is the "last" ascii character -- it has the highest integer value of any ascii character.
# This is because 255 is the highest value that can be represented with 8 binary digits.
#print("ord('ÿ'):", ord("ÿ"))

# As you can see, we get 8 1's, which shows that this is the highest possible 8 digit value.
#print("bin(ord('ÿ')):", bin(ord("ÿ")))

# Why is this?  It's because a single binary digit is called a bit, and computers store values in sequences of bytes, which are 8 bits together.
# You might be more familiar with kilobytes or megabytes -- a kilobyte is 1000 bytes, and a megabyte is 1000 kilobytes.
# There are 256 different ascii symbols, because the largest amount of storage any single ascii character can take up is one byte.
binary_w = bin(ord("w"))
binary_bracket = bin(ord("}"))


# ###5: Intro to unicode

# You might be wondering right now what happened to all of the other characters and alphabets in the world.
# 
# Because it only supports 255 characters, ascii can't deal with them, so a new standard was needed, called unicode.
# 
# Unicode assigns code points to characters. In python, these code points look like this: "\u3232".
# 
# We can use an encoding to turn these code points into binary integers.
# 
# The most common encoding for unicode is utf-8. It tells a computer which code points are associated with which integers.
# 
# utf-8 can encode values that are longer that one byte, enabling it to store all unicode characters.
# 
# utf-8 encodes characters using a variable length of bytes, which means that it also supports regular ascii characters (which are one byte each).

# ####Instructions

# Find the binary representation of "\u1019". Assign it to binary_1019.

# In[6]:

# We can initialize unicode code points (the value for this code point is \u27F6, but you see it as a character because it is being automatically converted).
code_point = "⟶"

# This particular code point maps to a right arrow character.
print("code_point:", code_point)

# We can get the base 10 integer value of the code point with the ord function.
#print ord(code_point)

# As you can see, this takes up a lot more than 1 byte.
#print bin(ord(code_point))

code_point = "မ"
#binary_1019 = bin(ord(code_point))


# ###6: Strings with unicode

# ascii is a subset of unicode. Unicode implements all of the ascii characters, as well as the additional characters that code points allow.
# 
# This lets us create unicode strings, that have ascii and unicode characters together.
# 
# By default in python 3, all strings are unicode, and encoded with utf-8, so we can directly use unicode code points or characters.

# ####Instructions

# Make a string with mixed unicode and ascii, and assign it to s3.

# In[7]:

s1 = "café"

# The \u prefix means "the next 4 digits are a unicode code point".
# It doesn't change the value at all (the last character in the string below is \u00e9).
s2 = "café"

# These strings are the same, because code points are equal to their corresponding unicode character.
# \u00e9 and é are equivalent.
print("s1 == s2:", s1 == s2)

s3 = "hello မ"


# ###7: The bytes type

# In Python, there's a datatype called "bytes".
# 
# It's like a string, except it contains encoded bytes values.
# 
# When we create an object with a bytes type from a string, we specify an encoding (usually utf-8).
# 
# We can then use the .encode() method to encode the string into bytes.

# ####Instructions

# Encode batman with the utf-8 encoding, and assign to batman_bytes.

# In[8]:

# We can make a string with some unicode values.
superman = "Clark Kent␦"
print("superman:", superman)

# This tells python to encode the string superman into unicode using the utf-8 encoding.
# We end up with a sequence of bytes instead of a string.
#superman_bytes = "Clark Kent␦".encode("utf-8")

batman = "Bruce Wayne␦"
#batman_bytes = batman.encode("utf-8")


# ###8: Hexadecimal conversions

# You might have noticed in the last screen that using .encode() turned code points into something like \xe2\x90\xa6.
# 
# These are three hexadecimal bytes.
# 
# The \x prefix means "the next two digits are in hexadecimal".
# 
# Two hexadecimal digits equal 8 binary digits, because digits can have higher values in hexadecimal (base 16).
# 
# For instance, "F" is 15 in hexadecimal, but 1111 is 15 in binary.
# 
# Because it's shorter to display, and 4 binary digits always equal 1 hexadecimal digit, programs often use hexadecimal to print out values.
# 
# This is purely for convenience.
# 
# Let's experiment a bit with hexadecimal conversions.

# ####Instructions

# Add "2" to "ea" in hexadecimal. Assign the result to hex_ea.
# 
# Add "e" to "f" in hexadecimal. Assign the result to hex_ef.

# In[9]:

# F is the highest single digit in hexadecimal (base 16).
# Its value is 15 in base 10.
print("int('F', 16):", int("F", 16))

# A in base 16 has the value 10 in base 10.
print("int('A', 16):", int("A", 16))

# Just like the earlier binary_add function, this adds two hex numbers.
def hexadecimal_add(a, b):
    return hex(int(a, 16) + int(b, 16))[2:]

# When we add 1 to 9 in hexadecimal, it becomes "a".
value = "9"
value = hexadecimal_add(value, "1")
print("value:", value)

hex_ea = hexadecimal_add("2", "ea")
print("hex_ea:", hex_ea)

hex_ef = hexadecimal_add("e", "f")
print("hex_ef:", hex_ef)


# ###9: Hex to binary

# We can convert hexadecimal to binary pretty easily.
# 
# We can even use the ord() and bin() functions that helped us convert code points to binary.

# ####Instructions

# Convert the hexadecimal byte "\xaa" to binary. Assign the result to binary_aa.
# 
# Convert the hexadecimal byte "\xab" to binary. Assign the result to binary_ab.

# In[10]:

# One byte (8 bits) in hexadecimal (the value of the byte below is \xe2).
hex_byte = "â"

# Print the base 10 integer value for the hex byte.
#print ord(hex_byte)

# This gives the exact same value -- remember than \x is just a prefix, and doesn't affect the value.
print("int('e2', 16):", int("e2", 16))

# Convert the base 10 integer to binary.
#print("bin(ord("â")):", bin(ord("â")))

#binary_aa = bin(ord("ª"))
#print("binary_aa:", binary_aa)

#binary_ab = bin(ord("\xab"))
#print("binary_ab:", binary_ab)


# ###10: Bytes and strings

# Once we have an object with datatype bytes, there isn't an encoding associated, so python doesn't know how to display the (encoded) code points in it.
# 
# Because of this, we can't mix bytes objects and strings together.

# ####Instructions

# Make a bytes object containing "Thor", and assign it to thor_bytes.

# In[11]:

#hulk_bytes = "Bruce Banner␦".encode("utf-8")

# We can't mix strings and bytes.
# For instance, if we try to replace the unicode ␦ character as a string, it won't work, because that value has been encoded to bytes.
try:
    hulk_bytes.replace("Banner", "")
except Exception:
    print("TypeError with replacement")

# We can create objects of the bytes datatype by putting a b in front of the quotation marks in a string.
hulk_bytes = b"Bruce Banner"

# Now, instead of mixing strings and bytes, we can use the replace method with bytes objects instead.
hulk_bytes.replace(b"Banner", b"")
thor_bytes = b"Thor"


# ###11: Decode bytes to strings

# Once we have a bytes object, we can decode it into a string using an encoding.
# 
# We use the .decode() method to do this.

# ####Instructions

# Decode morgan_freeman_bytes using the 'utf-8' encoding. Assign the result to morgan_freeman.

# In[12]:

# Make a bytes object with aquaman's secret identity.
aquaman_bytes = b"Who knows?"

# Now, we can use the decode method, along with the encoding (utf-8) to turn it into a string.
aquaman = aquaman_bytes.decode("utf-8")

# We can print the value and type out to verify that it is a string.
print("aquaman:", aquaman)
print("type(aquaman):", type(aquaman))

morgan_freeman_bytes = b"Morgan Freeman"
morgan_freeman = morgan_freeman_bytes.decode("utf-8")


# ###12: Read in file data

# Now that we understand unicode, we can go ahead and read our data in.
# 
# The data has a lot of symbols and other unicode characters, so we'll learn how to deal with them as we go along.

# ####Instructions

# Assign the second column of the tenth row in sentences_cia to sentences_ten.

# In[13]:

# We can read our data in using csvreader.
import csv

# When we open a file, we can specify the encoding that it's in. In this case, utf-8.
#f = open("data/sentences_cia.csv", 'r', encoding="utf-8")
f = open("data/sentences_cia.csv", 'r')
csvreader = csv.reader(f)
sentences_cia = list(csvreader)

# The data is two columns.
# First column is year, second is a sentence from a CIA report written that year.
# Print the first column of the second row.
print("sentences_cia[1][1]:", sentences_cia[1][1])
sentences_ten = sentences_cia[9][1]


# ###13: Convert to a dataframe

# In order to make this easier for ourselves, let's convert our sentences to a pandas dataframe.
# 
# Having a dataframe will make processing and analysis much simpler because we can use the .apply() method.

# ####Instructions

# Convert sentences_cia to a dataframe. Remember to deal with the headers properly. Assign the result to sentences_cia_df.

# In[14]:

import pandas as pd

# The sentences_cia data from last screen is available.
sentences_cia = pd.DataFrame(sentences_cia[1:], columns=sentences_cia[0])
sentences_cia.head(5)


# ###14: Clean up sentences

# Now that we have our data in a nice format, we need to process the strings to count up term occurences.
# 
# First, though, we need to clean up the strings so that extraneous symbols are removed. We only really care about letters, digits, and spaces.
# 
# Luckily, we can check the integer code of each character using ord() to see if it's a character we want to keep.

# Instructions

# Make a function that takes a dataframe row, and then returns the cleaned up version of the "statement" column.
# 
# Use the .apply() method on dataframes to apply the function to each row of sentences_cia.
# 
# Assign the resulting vector to the cleaned_statement column of sentences_cia.
# 
# You will have to initialize good_characters inside your function.

# In[15]:

# The integer codes for all the characters we want to keep.
good_characters = [48, 49, 50, 51, 52, 53, 54, 55, 56, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 32]

sentence_15 = sentences_cia["statement"][14]
print("sentence_15:", sentence_15)

# Iterate over the characters in the sentence, and only take those whose integer representations are in good_characters.
# This will construct a list of single characters.
cleaned_sentence_15_list = [s for s in sentence_15 if ord(s) in good_characters]

# Join the list together, separated by "" (no space), which creates a string again.
cleaned_sentence_15 = "".join(cleaned_sentence_15_list)

def clean_statement(row):
    good_characters = [48, 49, 50, 51, 52, 53, 54, 55, 56, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 32]
    statement = row["statement"]
    clean_statement_list = [s for s in statement if ord(s) in good_characters]
    return "".join(clean_statement_list)

sentences_cia["cleaned_statement"] = sentences_cia.apply(clean_statement, axis=1)


# ###15: Tokenize statements

# Now, we need to combine the sentences and turn them into tokens.
# 
# The eventual goal is to count up how many times each term occurs.

# ####Instructions

# Tokenize combined_statements by splitting it into words on spaces.
# 
# You should end up with a list of all the words in combined_statements.
# 
# Assign the result to statement_tokens.

# In[16]:

# We can use the .join() method on strings to join lists together.
# The string we use the method on will be used as the separator -- the character(s) between each string when they are joined.
combined_statements = " ".join(sentences_cia["cleaned_statement"])
statement_tokens = combined_statements.split(" ")


# ###16: Filter the tokens

# We want to count up how many times each term occurs in our data, so we can find the most common items.
# 
# The problem is that the most common words in the English language are ones that are relatively uninteresting to us right now -- words like "the", "a", and so on.
# 
# These words are called stopwords -- words that don't add much information to our analysis.
# 
# A common way to deal with this by filtering out any words that is in a list of known stopwords.
# 
# What we'll do for the sake of simplicity here is to filter out any words that are less than 5 characters long.
# 
# This should remove most of the least interesting words.

# ####Instructions

# Filter the statement_tokens list so that it only contains tokens 5 characters or more in length. Assign the result to filtered_tokens.

# In[17]:

# statement_tokens has been loaded in.
filtered_tokens = [s for s in statement_tokens if len(s) > 4]


# ###17: Count the tokens

# Now that we've filtered the tokens, we can count up how many times each one occurs.
# 
# The Counter object from the collections library will help us with this.
# 
# Counter takes a list as input, and creates a dictionary where the keys are list items, and the values are how many times those items appear in the list.

# ####Instructions

# Count up the items in filtered_tokens. Assign the result to filtered_token_counts.

# In[18]:

from collections import Counter

fruits = ["apple", "apple", "banana", "orange", "pear", "orange", "apple", "grape"]
fruit_count = Counter(fruits)

# Each of the items in the list has been counted up, and given a dictionary key.
print("fruit_count:", fruit_count)

# filtered_tokens has been loaded in.
filtered_token_counts = Counter(filtered_tokens)


# ###18: Most common tokens

# Now that we have a Counter object created using filtered_tokens as input, let's get the most common tokens out.

# ####Instructions

# Get the 3 most common items in filtered_token_counts. Assign the result to common_tokens.

# In[19]:

from collections import Counter

fruits = ["apple", "apple", "banana", "orange", "pear", "orange", "apple", "grape"]
fruit_count = Counter(fruits)

# We can use the most_common method of a Counter class to get the most common items.
# We pass in a number, which is the number of items we want to get.
print("fruit_count.most_common(2):", fruit_count.most_common(2))
print("fruit_count.most_common(3):", fruit_count.most_common(3))

# Filtered_token_counts has been loaded in.
common_tokens = filtered_token_counts.most_common(3)


# ###19: Finding the most common tokens by year

# Let's write a function to compute the most common terms by year.

# ####Instructions

# Write a function to find the 3 most common terms in sentences_cia in a given year (the "year" column).
# 
# The "year" column in sentences_cia stores strings, so you'll need to pass strings into the function.
# 
# You'll need to select the rows in sentences_cia that match that year, combine the cleaned statements, split into a list based on " ", filter out the words with a length of less than 5, make a counter object with the results, and finally find the 2 most common items in the counter.
# 
# Use the function to find the most common terms for "2000". Assign to common_2000.
# 
# Use the function to find the most common terms for "2002". Assign to common_2002.
# 
# Use the function to find the most common terms for "2013". Assign to common_2013.

# In[20]:

# Sentences_cia has been loaded in.
# It already has the cleaned_statement column.
from collections import Counter

def find_most_common_by_year(year, sentences_cia):
    data = sentences_cia[sentences_cia["year"] == year]
    combined_statement = " ".join(data["cleaned_statement"])
    statement_split = combined_statement.split(" ")
    counter = Counter([s for s in statement_split if len(s) > 4])
    return counter.most_common(2)

common_2000 = find_most_common_by_year("2000", sentences_cia)
print("common_2000:", common_2000)

common_2002 = find_most_common_by_year("2002", sentences_cia)
print("common_2002:", common_2002)

common_2013 = find_most_common_by_year("2013", sentences_cia)
print("common_2013:", common_2013)

