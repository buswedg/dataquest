

```python
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
```




<script>
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
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>



#Python Programming

##Functions and Debugging

###1: Reading the file in

The story is stored in the "story.txt" file. Open the file and read the contents into the story variable.


```python
# The story is stored in the file "story.txt".
f = open("data/story.txt", 'r')
story = f.read()
```

###2: Tokenizing the file

We now have to tokenize the file. Tokenizing is the process of splitting the file into individual words. For now, we'll split the file up based on whitespace (the space character).

The story is loaded into the story variable. Tokenize the story, and store the tokens into the tokenized_story variable.


```python
# We can split strings into lists with the .split() method.
# If we use a space as the input to .split(), it will split based on the space.
text = "Bears are probably better than sharks, but I can't get close enough to one to be sure."
tokenized_text = text.split(" ")
tokenized_story = story.split(" ")
```

###3: Replacing punctuation

In order to spell check our words, we'll be comparing the words in the story to a dictionary. If the word is in the dictionary, it will be correct. If it isn't, it will be incorrect.

In order to ensure that words that have apostrophes, commas, or other punctuation don't get falsely marked as incorrect, we need to remove all punctuation.

The story has been loaded into tokenized_story. Replace all of the punctuation in each of the tokens. You'll need to loop through tokenized_story to do so. You'll need to use multiple replace statements, one for each punctuation character to replace. Append the token to no_punctuation_tokens once you are done replacing characters.

Print out no_punctuation_tokens if you want to see which types of punctuation are still in the data.


```python
# We can use the .replace function to replace punctuation in a string.
text = "Who really shot John F. Kennedy?"
text = text.replace("?", "?!")

# The question mark has been replaced with ?!.
print(text)

# We can replace strings with blank spaces, meaning that they are just removed.
text = text.replace("?", "")

# The question mark is gone now.
print(text)

no_punctuation_tokens = []
for token in tokenized_story:
    token = token.replace(".","")
    token = token.replace(",","")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    no_punctuation_tokens.append(token)
```

    Who really shot John F. Kennedy?!
    Who really shot John F. Kennedy!
    

###4: Lowercasing the words

For the same reason that we replace punctuation, we also need to make the tokens lower case. We don't want to run into a situation where 'Farmer' isn't in the dictionary, but 'farmer' is.

The tokens without punctuation have been loaded into no_punctuation_tokens. Loop through the tokens and lowercase each one. Append each token to lowercase_tokens when you're done lowercasing.


```python
# We can make strings all lowercase using the .lower() method.
text = "MY CAPS LOCK IS STUCK"
text = text.lower()

# The text is much nicer to read now.
print(text)

lowercase_tokens = []
for token in no_punctuation_tokens:
    token = token.lower()
    lowercase_tokens.append(token)
```

    my caps lock is stuck
    

###5: Making a basic function

Define a function that takes degrees in fahrenheit as an input, and return degrees celsius

Use it to convert 100 degrees fahrenheit to celsius. Assign the result to celsius_100. 
Use it to convert 150 degrees fahrenheit to celsius. Assign the result to celsius_150.


```python
# A simple function that takes in a number of miles, and turns it into kilometers
# The input at position 0 will be put into the miles variable.
def miles_to_km(miles):
    # return is a special keyword that indicates that the function will output whatever comes after it.
    return miles/0.62137

# Returns the number of kilometers equivalent to one mile
print(miles_to_km(1))

# Convert a from 10 miles to kilometers
a = 10
a = miles_to_km(a)

# We can convert and assign to a different variable
b = 50
c = miles_to_km(b)

fahrenheit = 80
celsius = (fahrenheit - 32)/1.8
def convert(degrees):
    return (degrees - 32)/1.8
celsius_100 = convert(100)
celsius_150 = convert(150)
```

    1.60934708789
    

###6: Function introduction


```python
Make a function that takes a string as input and outputs a lowercase version. 

Use it to turn the string lowercase_me to lowercase. Assign the result to lowercased_string.
```


```python
def split_string(text):
    return text.split(" ")

sally = "Sally sells seashells by the seashore."
# This splits the string into a list.
print(split_string(sally))

# We can assign the output of a function to a variable.
sally_tokens = split_string(sally)

lowercase_me = "I wish I was in ALL lowercase"
def lowercase(text):
    return text.lower()

lowercased_string = lowercase(lowercase_me)
```

    ['Sally', 'sells', 'seashells', 'by', 'the', 'seashore.']
    

###7: Types of errors

There are multiple syntax errors in the code to the right. You can tell because of the error showing up in the results panel. Fix the errors and get the code running properly. It should print all of the items in a.


```python
a = ["Errors are no fun!", "But they can be fixed", "Just fix the syntax and everything will be fine"]
b = 5

for item in a:
    if b == 5:
        print(item)
```

    Errors are no fun!
    But they can be fixed
    Just fix the syntax and everything will be fine
    

###8: More syntax errors

The code to the right has multiple syntax errors. Fix them so the code prints out "I never liked that 6"


```python
a = 5

if a == 6:
    print("6 is obviously the best number")
else:
    print("I never liked that 6")
```

    I never liked that 6
    

###9: Index errors

Index errors occur when a list index that doesn't exist is referenced.

The code to the right has multiple index errors. Fix them so that the code prints the last item in each list.


```python
the_list = ["Harrison Ford", "Mark Hammil"]

print(the_list[1])

another_list = ["Jabba"]

print(another_list[0])
```

    Mark Hammil
    Jabba
    

###10: Multiline functions

Let's make a function to remove all punctuation.

All the tokens from Julius's story are in the tokenized_story variable. Write a function that removes all punctuation from an input string. Then loop over tokenized_story and call the function to remove the punctuation from each token. Append the tokens to no_punctuation_tokens.


```python
# Functions can have multiple lines in the function body.
def do_math(number):
    # Multiply the number by 10
    number = number * 10
    # Add 20 to the number
    number = number + 20
    return number

print(do_math(20))
a = do_math(10)

no_punctuation_tokens = []
def remove_punctuation(token):
    token = token.replace(".","")
    token = token.replace(",","")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    return token

for token in tokenized_story:
    token = remove_punctuation(token)
    no_punctuation_tokens.append(token)
```

    220
    

###11: Making a function to lowercase input

Now, let's add to our function so that it also lowercases input.

The remove_punctuation function is to the right. Can you add to it so that it also makes the output lowercase? Then loop over the tokens in tokenized_story and normalize them with the function. Append the tokens to normalized_tokens when you're done.


```python
def normalize(token):
    token = token.replace(".","")
    token = token.replace(",","")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    token = token.lower()
    return token

# We've read the tokens from Julius's story into the tokenized_story variable.
# Can you add to the remove_punctuation function so it also lowercases the tokens?
# Then loop over the tokens in tokenized_story, normalize them with the function, and append them to normalized_tokens.
normalized_tokens = []

for token in tokenized_story:
    token = normalize(token)
    normalized_tokens.append(token)
```

###12: Practice with multiple argument functions

Let's practice with functions that take multiple arguments.

Create a multiply function that takes in x, y, and z argument. The function should return x * y * z.

Assign the values of multiply(10,3,5) to a.
Assign the values of multiply(20,-1,3) to b.


```python
# This function takes two arguments, at positions 0 and 1
def divide(x,y):
    return x/y

# 5 is assigned to x, and 1 is assigned to y based on positions
print(divide(5,1))

# 1 is assigned to x, and 5 is assigned to y based on positions.
print(divide(1,5))
def multiply(x, y, z):
    return x * y * z

a = multiply(10,3,5)
b = multiply(20,-1,3)
```

    5
    0
    

###13: Reading in and normalizing the dictionary

Read in the dictionary from the "dictionary.txt" file. Split it into tokens based on the space character. Normalize each token using the normalize function. Append the normalized tokens to normalized_dictionary_tokens.

Do the same for the "story.txt" file.


```python
def normalize(token):
    token = token.replace(".","")
    token = token.replace(",","")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    token = token.lower()
    return token

normalized_dictionary_tokens = []
f = open("data/dictionary.txt", 'r')
tokens = f.read().split(" ")
for token in tokens:
    token = normalize(token)
    normalized_dictionary_tokens.append(token)


normalized_story_tokens = []
f = open("data/story.txt", 'r')
tokens = f.read().split(" ")
for token in tokens:
    token = normalize(token)
    normalized_story_tokens.append(token)
```

###14: Finding words that aren't spelled correctly

The normalized story tokens are in normalized_story_tokens, and the normalized dictionary tokens are in normalized_dictionary_tokens.

Loop through the story tokens, and check if each token is in the dictionary. If the token is in normalized_dictionary_tokens, append it to correctly_spelled. If it isn't, append it to potential_misspellings.


```python
potential_misspellings = []
correctly_spelled = []
for token in normalized_story_tokens:
    if token in normalized_dictionary_tokens:
        correctly_spelled.append(token)
    else:
        potential_misspellings.append(token)

print(potential_misspellings)
```

    ['therewasonceagreatandnoblefrmernamedjuliushewasthebestfarmerinhisvillageandprabablyeventhewholeworldonedayhedecididtogrwpotatoesjuliusknewthatpotatoeswerehardtogrowsohekniwhehdtogoetothemagicfarmerintheskytoseekhisguidancejuliussetoutonhisjourneyaroudnnoononedayitstartedrainingalmostyimmediatelytgoonbutheperservedhebecamesoakedandstopedinthestoretobuyanumbrellahetoldthestorekeeperreggieabouthisjourney""juliuscamebacktothevillageandmanagedtogrowthefinestcropthevillagehadeverseeneveryonehadpotatoestoeatformonthsandsangjuliusspraises']
    
