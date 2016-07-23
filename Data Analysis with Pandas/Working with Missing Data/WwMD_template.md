

```python
from __future__ import print_function
```

#Data Analysis with Pandas

##Working with Missing Data

###1: Finding the missing data

Missing data can be presented a few different ways.

In python, we have the None keyword and type, which indicates no value.

pandas uses NaN, which stands for "not a number", to indicate a missing value.

We can also call NaN a null value.

####Instructions

Count the number of null values in the "Age" column.

Assign the result to age_null_count.


```python
import pandas as pd

f = "data/titanic.csv"
titanic_survival = pd.read_csv(f)

titanic_survival.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pclass</th>
      <th>survived</th>
      <th>name</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>ticket</th>
      <th>fare</th>
      <th>cabin</th>
      <th>embarked</th>
      <th>boat</th>
      <th>body</th>
      <th>home.dest</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>0</td>
      <td>Abbing, Mr. Anthony</td>
      <td>male</td>
      <td>42</td>
      <td>0</td>
      <td>0</td>
      <td>C.A. 5547</td>
      <td>7.55</td>
      <td>NaN</td>
      <td>S</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>0</td>
      <td>Abbott, Master. Eugene Joseph</td>
      <td>male</td>
      <td>13</td>
      <td>0</td>
      <td>2</td>
      <td>C.A. 2673</td>
      <td>20.25</td>
      <td>NaN</td>
      <td>S</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>East Providence, RI</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>0</td>
      <td>Abbott, Mr. Rossmore Edward</td>
      <td>male</td>
      <td>16</td>
      <td>1</td>
      <td>1</td>
      <td>C.A. 2673</td>
      <td>20.25</td>
      <td>NaN</td>
      <td>S</td>
      <td>NaN</td>
      <td>190</td>
      <td>East Providence, RI</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>1</td>
      <td>Abbott, Mrs. Stanton (Rosa Hunt)</td>
      <td>female</td>
      <td>35</td>
      <td>1</td>
      <td>1</td>
      <td>C.A. 2673</td>
      <td>20.25</td>
      <td>NaN</td>
      <td>S</td>
      <td>A</td>
      <td>NaN</td>
      <td>East Providence, RI</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>1</td>
      <td>Abelseth, Miss. Karen Marie</td>
      <td>female</td>
      <td>16</td>
      <td>0</td>
      <td>0</td>
      <td>348125</td>
      <td>7.65</td>
      <td>NaN</td>
      <td>S</td>
      <td>16</td>
      <td>NaN</td>
      <td>Norway Los Angeles, CA</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Print age column.
#print titanic_survival["age"]

# Use the isnull function to find which values in a column are missing
age_null = pd.isnull(titanic_survival["age"])

age_null_true = age_null[age_null == True]
age_null_count = len(age_null_true)
print("age_null_count:", age_null_count)
```

    age_null_count: 263
    

###2: Whats the big deal with missing data?

So, we know that quite a few values are missing in the "age" column, and other columns are missing data, too, but why is this a problem?

Let's try to compute the average age of passengers on the Titanic.

####Instructions

Use age_null to create a vector that only contains values from the "age" column that aren't "NaN".

Compute the mean of the new vector, and assign the result to correct_mean_age.


```python
import pandas as pd

mean_age = sum(titanic_survival["age"]) / len(titanic_survival["age"])

# 'mean_age' is NaN.  This is because any calculations we do with a null value also result in a null value.
print("mean_age:", mean_age)

# Filter the missing values out before we compute the mean.
age_null = pd.isnull(titanic_survival["age"])
good_ages = titanic_survival["age"][age_null == False]
correct_mean_age = sum(good_ages) / len(good_ages)

print("correct_mean_age:", correct_mean_age)
```

    mean_age: nan
    correct_mean_age: 29.8811345124
    

###3: Easier ways to do math

Luckily, missing data is so common that pandas automatically filters for it with some methods.

We can use the .mean() method to compute the mean, and it will automatically remove missing values.

####Instructions

Assign the mean of the "fare" column to 'correct_mean_fare'.


```python
import pandas as pd

# This is the same value that we computed in the last screen, but it's much simpler.
correct_mean_age = titanic_survival["age"].mean()
print("correct_mean_age:", correct_mean_age)

correct_mean_fare = titanic_survival["fare"].mean()
print("correct_mean_fare:", correct_mean_fare)
```

    correct_mean_age: 29.8811345124283
    correct_mean_fare: 33.29547928134565
    

###4: Computing summary statistics

Let's compute some more advanced statistics about the data.

####Instructions

Fill in the missing code to compute fare_for_class for the given pclass.

When the loop is done, fares_by_class should have 1, 2, and 3 as keys, with the average fares as the corresponding values.


```python
# Passengers are divided into classes based on the "pclass" column
passenger_classes = [1, 2, 3]

# Create dictionary.
fares_by_class = {}
for pclass in passenger_classes:
    # Return fares for pclass.
    pclass_fares = titanic_survival["fare"][titanic_survival["pclass"] == pclass]
    # Calculate pclass mean fare.
    fare_for_class = pclass_fares.mean()
    # Store in 'fares_by_class' dictionary.
    fares_by_class[pclass] = fare_for_class

print("fares_by_class[1]:", fares_by_class[1])
print("fares_by_class[2]:", fares_by_class[2])
print("fares_by_class[3]:", fares_by_class[3])
```

    fares_by_class[1]: 87.50899164086687
    fares_by_class[2]: 21.1791963898917
    fares_by_class[3]: 13.302888700564957
    

###5: Making pivot tables

Let's compute the survival probability for each passenger class in the Titanic.

In order to help us out, we'll use the pivot_table method on dataframes -- it makes doing analysis like what we did in the last screen much simpler.

If you're familiar with pivot tables in excel, this will look familiar.

####Instructions

Use the pivot_table method to compute the mean "age" for each passenger class ("pclass").

Assign the result to passenger_age.


```python
import pandas as pd
import numpy as np

# index specifies which column to subset data based on 
# values specifies which column to subset based on the index
# The aggfunc specifies what to do with the subsets
# In this case, we split survived into 3 vectors, one for each passenger class, and take the mean of each
passenger_survival = titanic_survival.pivot_table(index="pclass", values="survived", aggfunc=np.mean)
print("passenger_survival:", passenger_survival)

passenger_age = titanic_survival.pivot_table(index="pclass", values="age", aggfunc=np.mean)
print("passenger_age", passenger_age)

passenger_fare = titanic_survival.pivot_table(index="pclass", values="fare", aggfunc=np.mean)
print("passenger_fare:", passenger_fare)
```

    passenger_survival: pclass
    1    0.619195
    2    0.429603
    3    0.255289
    Name: survived, dtype: float64
    passenger_age pclass
    1    39.159918
    2    29.506705
    3    24.816367
    Name: age, dtype: float64
    passenger_fare: pclass
    1    87.508992
    2    21.179196
    3    13.302889
    Name: fare, dtype: float64
    

###6: More complex pivot tables

We can use the pivot_table method to do more advanced things than we just did.

For starters, we can make more complex pivot tables that show multiple values at once.

####Instructions

Make a pivot table that computes the mean "age", survival chance("survived"), and "fare" for each embarkation port ("embarked").

Assign the result to 'port_stats'.

Make sure to put the values list in the same order that the columns are given here.


```python
import numpy as np

# Compute the mean survival chance and the mean age for each passenger class.
passenger_survival = titanic_survival.pivot_table(index="pclass", values=["age", "survived"], aggfunc=np.mean)
print("passenger_survival:\n", passenger_survival)

port_stats = titanic_survival.pivot_table(index="embarked", values=["age", "survived", "fare"], aggfunc=np.mean)
print("port_stats:\n", port_stats)
```

    passenger_survival:
                   age  survived
    pclass                     
    1       39.159918  0.619195
    2       29.506705  0.429603
    3       24.816367  0.255289
    port_stats:
                     age       fare  survived
    embarked                                
    C         32.332154  62.336267  0.555556
    Q         28.630000  12.409012  0.357724
    S         29.245205  27.418824  0.332604
    

###7: Drop missing values

We looked at how to remove missing values in a vector of data, but how about in a matrix?

We can use the dropna method on pandas dataframes to do this.

Using the method will drop any rows that contain missing values.

####Instructions

Drop all rows in titanic_survival where the columns "age", "body", or "home.dest" have missing values.

Assign the result to new_titanic_survival.


```python
import pandas as pd

# Drop all rows that have missing values.
new_titanic_survival = titanic_survival.dropna()

# We have an empty dataframe now because every row has at least one missing value.
#print(new_titanic_survival)

# We can also use the axis argument to drop columns that have missing values
new_titanic_survival = titanic_survival.dropna(axis=1)
#print(new_titanic_survival)

# We can use the subset argument to only drop rows if certain columns have missing values.
# This drops all rows where "age" or "sex" is missing.
new_titanic_survival = titanic_survival.dropna(subset=["age", "sex"])
#print(new_titanic_survival)

new_titanic_survival = titanic_survival.dropna(subset=["age", "body", "home.dest"])
new_titanic_survival.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pclass</th>
      <th>survived</th>
      <th>name</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>ticket</th>
      <th>fare</th>
      <th>cabin</th>
      <th>embarked</th>
      <th>boat</th>
      <th>body</th>
      <th>home.dest</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>0</td>
      <td>Abbott, Mr. Rossmore Edward</td>
      <td>male</td>
      <td>16</td>
      <td>1</td>
      <td>1</td>
      <td>C.A. 2673</td>
      <td>20.25</td>
      <td>NaN</td>
      <td>S</td>
      <td>NaN</td>
      <td>190</td>
      <td>East Providence, RI</td>
    </tr>
    <tr>
      <th>10</th>
      <td>3</td>
      <td>0</td>
      <td>Adahl, Mr. Mauritz Nils Martin</td>
      <td>male</td>
      <td>30</td>
      <td>0</td>
      <td>0</td>
      <td>C 7076</td>
      <td>7.25</td>
      <td>NaN</td>
      <td>S</td>
      <td>NaN</td>
      <td>72</td>
      <td>Asarum, Sweden Brooklyn, NY</td>
    </tr>
    <tr>
      <th>11</th>
      <td>3</td>
      <td>0</td>
      <td>Adams, Mr. John</td>
      <td>male</td>
      <td>26</td>
      <td>0</td>
      <td>0</td>
      <td>341826</td>
      <td>8.05</td>
      <td>NaN</td>
      <td>S</td>
      <td>NaN</td>
      <td>103</td>
      <td>Bournemouth, England</td>
    </tr>
    <tr>
      <th>20</th>
      <td>3</td>
      <td>0</td>
      <td>Ali, Mr. William</td>
      <td>male</td>
      <td>25</td>
      <td>0</td>
      <td>0</td>
      <td>SOTON/O.Q. 3101312</td>
      <td>7.05</td>
      <td>NaN</td>
      <td>S</td>
      <td>NaN</td>
      <td>79</td>
      <td>Argentina</td>
    </tr>
    <tr>
      <th>25</th>
      <td>1</td>
      <td>0</td>
      <td>Allison, Mr. Hudson Joshua Creighton</td>
      <td>male</td>
      <td>30</td>
      <td>1</td>
      <td>2</td>
      <td>113781</td>
      <td>151.55</td>
      <td>C22 C26</td>
      <td>S</td>
      <td>NaN</td>
      <td>135</td>
      <td>Montreal, PQ / Chesterville, ON</td>
    </tr>
  </tbody>
</table>
</div>



###8: Row indices

In pandas, dataframes and series have row indexes.

These work just like column indexes, and can take values like numbers, characters, and strings.

####Instructions

Assign the row with index 25 to row_index_25.

Assign the fifth row to row_position_fifth.


```python
# Print out the first 5 rows in 'titanic_survival'.
#print(titanic_survival.iloc[:5,:])

new_titanic_survival = titanic_survival.dropna(subset=["body"])

# Print out the first 5 rows in 'new_titanic_survival'.
#print(new_titanic_survival.iloc[:5,:])

# Print out 4th row in 'new_titanic_survival'.
row_index_4 = new_titanic_survival.iloc[4,:]
print("row_index_4:\n", row_index_4)

# .loc instead addresses rows and columns by index, not position
# This actually prints the first row, because it has index 3
#print(new_titanic_survival.loc[3,:])

row_index_25 = new_titanic_survival.loc[25,:]
print("row_index_25:\n", row_index_25)

row_position_fifth = new_titanic_survival.iloc[4,:]
print("row_position_fifth:\n", row_position_fifth)
```

    row_index_4:
     pclass                                          1
    survived                                        0
    name         Allison, Mr. Hudson Joshua Creighton
    sex                                          male
    age                                            30
    sibsp                                           1
    parch                                           2
    ticket                                     113781
    fare                                       151.55
    cabin                                     C22 C26
    embarked                                        S
    boat                                          NaN
    body                                          135
    home.dest         Montreal, PQ / Chesterville, ON
    Name: 25, dtype: object
    row_index_25:
     pclass                                          1
    survived                                        0
    name         Allison, Mr. Hudson Joshua Creighton
    sex                                          male
    age                                            30
    sibsp                                           1
    parch                                           2
    ticket                                     113781
    fare                                       151.55
    cabin                                     C22 C26
    embarked                                        S
    boat                                          NaN
    body                                          135
    home.dest         Montreal, PQ / Chesterville, ON
    Name: 25, dtype: object
    row_position_fifth:
     pclass                                          1
    survived                                        0
    name         Allison, Mr. Hudson Joshua Creighton
    sex                                          male
    age                                            30
    sibsp                                           1
    parch                                           2
    ticket                                     113781
    fare                                       151.55
    cabin                                     C22 C26
    embarked                                        S
    boat                                          NaN
    body                                          135
    home.dest         Montreal, PQ / Chesterville, ON
    Name: 25, dtype: object
    

###9: Column indices

We can also index columns using the .loc[] method.

####Instructions

Assign the value at row index 1100, column index "age" to row_1100_age.

Assign the value at row index 25, column index "survived" to row_25_survived.


```python
new_titanic_survival = titanic_survival.dropna(subset=["body"])
print("new_titanic_survival[:5]:\n", new_titanic_survival[:5])

# Print the value in the first column of the first row.
#print(new_titanic_survival.iloc[0,0])

# Prints the value at row index 3 and column "pclass".
#print(new_titanic_survival.loc[3,"pclass"])

#row_1100_age = new_titanic_survival.loc[1100, "age"]
row_25_survived = new_titanic_survival.loc[25, "survived"]

#print(row_25_survived)
```

    new_titanic_survival[:5]:
         pclass  survived                                  name   sex  age  sibsp  \
    2        3         0           Abbott, Mr. Rossmore Edward  male   16      1   
    10       3         0        Adahl, Mr. Mauritz Nils Martin  male   30      0   
    11       3         0                       Adams, Mr. John  male   26      0   
    20       3         0                      Ali, Mr. William  male   25      0   
    25       1         0  Allison, Mr. Hudson Joshua Creighton  male   30      1   
    
        parch              ticket    fare    cabin embarked boat  body  \
    2       1           C.A. 2673   20.25      NaN        S  NaN   190   
    10      0              C 7076    7.25      NaN        S  NaN    72   
    11      0              341826    8.05      NaN        S  NaN   103   
    20      0  SOTON/O.Q. 3101312    7.05      NaN        S  NaN    79   
    25      2              113781  151.55  C22 C26        S  NaN   135   
    
                              home.dest  
    2               East Providence, RI  
    10      Asarum, Sweden Brooklyn, NY  
    11             Bournemouth, England  
    20                        Argentina  
    25  Montreal, PQ / Chesterville, ON  
    

###10: Reindex rows

Remember how new_titanic_survival didn't have sequential row indexes?

Each row retained its original index from titanic_survival.

Sometimes it is useful to reindex, and make new indexes starting from 0.

To do this, we can use the reset_index() method.

####Instructions

Use the dropna method to remove rows that have missing values in the "age" or "boat" columns.

Then, reindex the resulting dataframe so the row indexes start from 0.

Assign the final result to titanic_reindexed.


```python
new_titanic_survival = new_titanic_survival.reset_index(drop=True)
print("new_titanic_survival[:5]:\n", new_titanic_survival[:5])

new_titanic_survival = titanic_survival.dropna(subset=["age", "boat"])
titanic_reindexed = new_titanic_survival.reset_index(drop=True)
```

    new_titanic_survival[:5]:
        pclass  survived                                  name   sex  age  sibsp  \
    0       3         0           Abbott, Mr. Rossmore Edward  male   16      1   
    1       3         0        Adahl, Mr. Mauritz Nils Martin  male   30      0   
    2       3         0                       Adams, Mr. John  male   26      0   
    3       3         0                      Ali, Mr. William  male   25      0   
    4       1         0  Allison, Mr. Hudson Joshua Creighton  male   30      1   
    
       parch              ticket    fare    cabin embarked boat  body  \
    0      1           C.A. 2673   20.25      NaN        S  NaN   190   
    1      0              C 7076    7.25      NaN        S  NaN    72   
    2      0              341826    8.05      NaN        S  NaN   103   
    3      0  SOTON/O.Q. 3101312    7.05      NaN        S  NaN    79   
    4      2              113781  151.55  C22 C26        S  NaN   135   
    
                             home.dest  
    0              East Providence, RI  
    1      Asarum, Sweden Brooklyn, NY  
    2             Bournemouth, England  
    3                        Argentina  
    4  Montreal, PQ / Chesterville, ON  
    

###11: Use the apply function

The first step we need to take to figure out the age breakdown is to learn about the .apply() method.

By default, .apply() will iterate through each column in a dataframe, and perform a function on it.

The column will be passed into the function.

The result from the function will be combined with all of the other results, and placed into a new series.

The function results will have the same position as the column they were generated from.

####Instructions

Write a function to count up the number of non-null elements in a series.

Use the .apply() method, along with your function, to run across all the columns in titanic_survival.

Assign the result to column_not_null_count.


```python
import pandas as pd

# Function counts the number of null values in a series.
def null_count(column):
    # Make a vector that contains True if null, False if not.
    column_null = pd.isnull(column)
    # Create a new vector with only values where the series is null.
    null = column[column_null == True]
    # Return the count of null values.
    return len(null)

# Compute null counts for each column.
column_null_count = titanic_survival.apply(null_count)
print("column_null_count:\n", column_null_count)

def not_null_count(column):
    column_null = pd.isnull(column)
    null = column[column_null == False]
    return len(null)

column_not_null_count = titanic_survival.apply(not_null_count)
```

    column_null_count:
     pclass          0
    survived        0
    name            0
    sex             0
    age           263
    sibsp           0
    parch           0
    ticket          0
    fare            1
    cabin        1014
    embarked        2
    boat          823
    body         1188
    home.dest     563
    dtype: int64
    

###12: Applying a function to a row

By passing in the axis argument, we can use the .apply() method to iterate over rows, not columns.

####Instructions

If someone is under 18, they are a "minor". If they are over 18, they are an "adult". If their age is missing (is null), their age is "unknown".

Make a function that returns the string "minor" if someone is under 18, "adult" if they are over 18, and "unknown" if their age is null.

Then, use the function along with .apply() to find the right label for everyone.

Assign the result to age_labels.

You can use isnull to check if a value is null or not.


```python
import pandas as pd

# Function will check if a row is an entry for a minor (under 18), or not.
def is_minor(row):
    if row["age"] < 18:
        return True
    else:
        return False

# This is a boolean series with the same length as the number of rows in titanic_survival
# Each entry is True if the row at the same position is a record for a minor
# The axis of 1 specifies that it will iterate over rows, not columns
minors = titanic_survival.apply(is_minor, axis=1)

def generate_age_label(row):
    age = row["age"]
    if pd.isnull(age):
        return "unknown"
    elif age < 18:
        return "minor"
    else:
        return "adult"

age_labels = titanic_survival.apply(generate_age_label, axis=1)

print("age_labels[:5]:\n", age_labels[:5])
```

    age_labels[:5]:
     0    adult
    1    minor
    2    minor
    3    adult
    4    minor
    dtype: object
    

###13: Computing survival percentage by age group

Now that we have age labels for everyone, let's make a pivot table to find survival chance by age group.

####Instructions

Make a pivot table that computes the mean survival chance("survived"), for each age group ("age_labels").

Assign the result to age_group_survival.


```python
import numpy as np

#age_group_survival = titanic_survival.pivot_table(index="age_labels", values=["survived"], aggfunc=np.mean)
```
