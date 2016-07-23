

```python
from __future__ import print_function
```

#Python Programming

##Scopes and Debugging

###1: Find the total number of borrowers in default

Just so we can get an idea of how large the problem of student loan debt is, let's first find the total number of borrowers in default.

We can do this by adding together all of the values in the borrower_default_count_240 column.


```python
import pandas

loans = pandas.read_csv("data/loans.csv")
loans[:5]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>serial</th>
      <th>opeid</th>
      <th>institution</th>
      <th>address</th>
      <th>city</th>
      <th>state</th>
      <th>zip</th>
      <th>repayment_borrowers</th>
      <th>default_borrowers</th>
      <th>default_rate</th>
      <th>borrower_default_count_240</th>
      <th>principal_outstanding_240</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>100200</td>
      <td>Alabama Agricultural &amp; Mechanical University</td>
      <td>4900 Meridian Street</td>
      <td>Normal</td>
      <td>AL</td>
      <td>35762-1357</td>
      <td>145</td>
      <td>54</td>
      <td>37.24%</td>
      <td>1606</td>
      <td>954821</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>100500</td>
      <td>Alabama State University</td>
      <td>915 South Jackson Street</td>
      <td>Montgomery</td>
      <td>AL</td>
      <td>36104-5714</td>
      <td>164</td>
      <td>12</td>
      <td>7.32%</td>
      <td>1567</td>
      <td>1410608</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13</td>
      <td>100900</td>
      <td>Auburn University</td>
      <td>107 Samford Hall</td>
      <td>Auburn</td>
      <td>AL</td>
      <td>36849-5113</td>
      <td>479</td>
      <td>29</td>
      <td>6.05%</td>
      <td>269</td>
      <td>747267</td>
    </tr>
    <tr>
      <th>3</th>
      <td>14</td>
      <td>831000</td>
      <td>Auburn University Montgomery</td>
      <td>7440 East Drive</td>
      <td>Montgomery</td>
      <td>AL</td>
      <td>36117-3596</td>
      <td>88</td>
      <td>20</td>
      <td>22.73%</td>
      <td>184</td>
      <td>457312</td>
    </tr>
    <tr>
      <th>4</th>
      <td>16</td>
      <td>101200</td>
      <td>Birmingham Southern College</td>
      <td>900 Arkadelphia Road</td>
      <td>Birmingham</td>
      <td>AL</td>
      <td>35254-0002</td>
      <td>69</td>
      <td>12</td>
      <td>17.39%</td>
      <td>93</td>
      <td>240798</td>
    </tr>
  </tbody>
</table>
</div>




```python
# The data is in the loans variable.

# Let's add together all of the borrower counts to find how many people are in default
#sum = sum(loans["borrower_default_count_240"])

# Now let's add together the total principal on the loans in default
#sum = sum(loans["principal_outstanding_240"])

# It looks like the above code gives us an error.
# We overwrote the sum function with our sum variable, so we can't use it anymore.
# In the next few screens, we'll learn about what this overwriting is, and how variables in python work.
```

###2: Builtin functions

Python has some functions that are available by default, without having to import them. These are called builtin functions.

sum is one such builtin function. Others are len, float, min, and max. These are generally functions that are used so often that it makes sense to make them a part of the language itself.

As you saw in the previous screen, we overwrote a builtin function. Any variable in python can be overwritten, but there are specific rules about how the overwriting works.

####Instructions

Use the sum function to add 6 and 11. Assign the result to total.


```python
def add_things(a, b):
    sum = a + b
    return sum

print("add_things(5, 10):", add_things(5, 10))

total = sum([6, 11])
print("total:", total)
```

    add_things(5, 10): 15
    total: 17
    

###3: Functions and scopes

Every function has its own local scope. The global scope is what happens at the top level of the module -- outside any functions.

Inside a local scope, you can overwrite variables without it being reflected in the global scopes.

Scopes are a way to isolate pieces of the program from each other. Imagine calling a builtin or library function that overwrote all of your variables because some variables in the function are named the same as your own variables.

Instructions

Make a function that takes city and loans as input and returns the average debt per borrower in default (principal_outstanding_240 / borrower_default_count_240) in that city (city column).

Then, use it to compute the average debt per borrower in New York. Assign the result to average_debt.

The city should still be Boston in the global scope at the end.


```python
state = "MA"
def loan_defaults_by_state(state, loans):
    selected_data = loans[loans["state"] == state]
    return selected_data["borrower_default_count_240"].sum()
wa_defaults = loan_defaults_by_state("WA", loans)

# state still contains the value from our global scope, even though we assigned "WA" to it in the local scope of the function.
print("state:", state)

city = "Boston"
def loan_principal_average(city, loans):
    selected_data = loans[loans["city"] == city]
    average_debt = float(selected_data["principal_outstanding_240"].sum()) / selected_data["borrower_default_count_240"].sum()
    return average_debt

average_debt = loan_principal_average("New York", loans)
print("average_debt:", average_debt)
```

    state: MA
    average_debt: 2399.9490449470045
    

###4: Global variables

Global variables are a way to define variables that are available across all scopes.

These are rarely a good solution, and should be used sparingly, but are good to know about.

We define global variables with the global keyword.

####Instructions

Make a global variable called b. Assign the value 20 to it.


```python
def test_function():
    # We define a as a global by using the global keyword
    global a
    # We can now assign a value to the variable a
    a = 10
# Running the function executes the code inside and assigns to a
test_function()
# Because we defined a as a global, even though it was in a local scope, it is now available here
print("a:", a)

def new_function():
    global b
    b = 20
new_function()
```

    a: 10
    

###5: Using documentation

You might not be surprised to know that most professional coders don't know all of the basic functions of the languages they use. Python has a lot of syntax, functions, and concepts to remember, and its only natural to forget how something works, or not know in the first place.

In times like these, documentation can be great. Python has some extensive documentation that you can read through <a href = "https://docs.python.org/3/">here</a>. The library reference is <a href = "https://docs.python.org/3/library/index.html">here</a>, and tells you have different standard modules and functions work. For example, <a href = "https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str">here's</a> the page on strings.

Instructions

Count the number of times "University" appears in the all_school_names string. Assign the result to university_count.

Count the number of times "College" appears in all_school_names. Assign the result to college_count.

There's a method on strings that you can use to do this. Look at the string <a href = "https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str">documentation</a> to find it.


```python
# The loans data is loaded into the loans variable.
all_school_names = " ".join(loans["institution"])
university_count = all_school_names.count("University")
college_count = all_school_names.count("College")
```

###6: Library documentation

Most python libraries also have good documentation. You can usually find these by googling the name of the library, and looking for a documentation link. For example, pandas has some documentation that can be found <a href = "http://pandas.pydata.org/pandas-docs/stable/">here</a>. You can find descriptions of each of the methods <a href = "http://pandas.pydata.org/pandas-docs/stable/api.html">here</a>.

For example, <a href = "http://pandas.pydata.org/pandas-docs/stable/api.html#id3">here</a> is the link to documentation on dataframe indexing.

Instructions

Get the first 5 rows of the loans dataframe. Assign the result to loans_first_5.

There's a method on dataframes that lets us do this. It's in <a href = "http://pandas.pydata.org/pandas-docs/stable/api.html#id3">this</a> documentation section.


```python
# The loans data is loaded into the loans variable.
loans_first_5 = loans.head(5)
```

###7: Getting more help

Sometimes, even the best documentation can't help you with a specific error you're having. It's times like these that question and answer sites can be a big help. The most popular site for programmers is <a href = "http://stackoverflow.com/">StackOverflow</a>. It has a huge database of questions and answers, and a large community.

In stackoverflow, the top of the page has the question, and responses are below it. The community can upvote and downvote responses, and the answer that the asker accepted has a checkmark next to it. <a href = "http://stackoverflow.com/questions/509211/explain-pythons-slice-notation">Here's</a> an example question.

Searching on stackoverflow or google for the error you're seeing can usually help you solve the problem.

####Instructions

The above code causes an error when trying to assign to loyola_defaults. <a href = "http://stackoverflow.com/questions/23944657/typeerror-method-takes-1-positional-argument-but-2-were-given">This</a> stackoverflow link explains a little more about what the error is and how to fix it.

Fix the code above so that the correct value for the borrower_default_count_240 column in the row for Loyola Marymount University is assigned to loyola_defaults.


```python
class University():
    def __init__(self, name):
        self.data = loans[loans["institution"] == name].iloc[0,:]

    def get_defaults(self):
        return self.data["borrower_default_count_240"]

loyola = University("Loyola Marymount University")
loyola_defaults = loyola.get_defaults()
print("loyola_defaults:", loyola_defaults)
```

    loyola_defaults: 312
    
