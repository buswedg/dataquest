
#Python for Business Analysts

##Automate Repetitive Tasks

###1: Introduction

In this mission, we will explore how we can use Python to automate tasks for us.

####Instructions

Create 2 variables, housing_2007 and housing_2005, that contain the DataFrame objects associated with Hud_2007.csv and Hud_2005.csv, respectively.


```python
import pandas

housing_2007 = pandas.read_csv("data/Hud_2007.csv")
housing_2005 = pandas.read_csv("data/Hud_2005.csv")
```

###2: Lists

Now that we have read in both datasets into DataFrame objects, let's add them to a List. A List is type of object (just like a DataFrame, Integer, or String) that contains an ordered group of objects. Just like how a grocery list contains a group of "ingredient" objects to buy, is a List object in Python houses a group of the objects we add to it. Instead of writing code to manipulate each object separately (in our case the objects are DataFrames), we can group a few objects into a List object, write the logic once, and apply it to every object in that List. This saves us a lot of time and energy, and will be important when we deal with much larger datasets with tens, hundreds or even thousands of DataFrames.

In the following code block, we will create an empty List called data_frames_list by assigning it empty brackets: []

Then, we will add a year column for each DataFrame to keep track of which DataFrame is which:

housing_2005['year'] = '2005'
housing_2007['year'] = '2007'

Each row now has a value for year, either 2005 or 2007, identifying which dataset that row originated from. Finally, we will use .append() to first add housing_2005 then housing_2007 to the end of data_frames_list. The List object preserves the order by which the DataFrames were added:

data_frames_list.append(housing_2005)
data_frames_list.append(housing_2007)

The list now contains these two DataFrames in the order we added them.


```python
# Create list.
data_frames_list = []

# Add a year column to each dataframe.
housing_2005['year'] = '2005'
housing_2007['year'] = '2007'

# .append() adds the specified object to the end of the list.
data_frames_list.append(housing_2005)
data_frames_list.append(housing_2007)

# List now contains 2 objects, the respective dataframes for 2005 and 2007.
print len(data_frames_list)
```

    2
    

###3: Column Filtering

After appending both DataFrames, we ran print() on len(data_frames_list) to display the number of elements, or length, of the list to verify that we added two DataFrame objects to the list.

Let's now practice Pandas' column filtering feature that we learned in the previous lesson. Create a new DataFrame, filtered_housing_2007, that contains the column filtered version of housing_2007, with just the columns we are interested in. The columns we want are: ['AGE1', 'FMR', 'TOTSAL', 'year'].

####Instructions

First, create a List variable, columns, that contains the names of all of the columns we are interested in. When specifying the elements we want in the list, we need to surround each column name we want with quotes (either single or double quotes), add a comma between each column name, and then surround the whole thing with a starting [ and closing bracket ]. Then, we use bracket notation on the DataFrame object to specify a filter. We want the filter to just contain the columns list.


```python
columns = []
filtered_housing_2007 = []

# Create list of column names to filter by.
columns = ['AGE1', 'FMR', 'TOTSAL', 'year']

# Filter dataframe.
filtered_housing_2007 = housing_2007[columns]

print filtered_housing_2007[:5]
```

       AGE1   FMR  TOTSAL  year
    0    -9  1048      -9  2007
    1    69  1048       0  2007
    2    45   757   26000  2007
    3    47   847  126000  2007
    4    30   616   42000  2007
    

###4: Functions

Now, we will learn how to write our own functions. Functions are core to every programming language and are a powerful way to package logic and apply it wherever we see fit. They can take an object as an input, apply pre-written logic on the input, and then return a modified object. Functions are like factories that take in raw materials, add other materials and processes to them, and then crank out finished products. In the next code block, we define a function filter_columns, that takes in an input, data_frames_list, and returns a new list new_df_list.

We want the function to filter each DataFrame down to only the columns we want. Let's use the same columns from the last code block: * 'AGE1', 'FMR', 'TOTSAL', year


```python
def filter_columns(data_frames_list):
    # Create list.
    new_df_list = list()
    
    # Look through each dataframe.
    for df in data_frames_list:
        # Create list of column names to filter by.
        columns = ['AGE1', 'FMR', 'TOTSAL', 'year']
        # Filter dataframe.
        filtered_df = df[columns]
        # Append filtered dataframe to 'new_df_list'.
        new_df_list.append(filtered_df)

    return new_df_list

filtered_data_frames_list = filter_columns(data_frames_list)
```

###5: Explanation

Let's walk through what we wrote, step by step.

In the function above, we used a for loop:

for df in data_frames_list:

to iterate over all of the object in data_frames_list (which contained our twp DataFrames we added earlier) and applied our column filtering logic. We iterated over a list object by object, referring to the current object we were applying the logic to as df.

Instead of hard coding the columns we want at the filter level like we did in the last lesson:

filtered_housing_2013 = housing_2013[[ 'AGE1', 'FMR',  'TOTSAL', 'year' ]]

we assigned the column names to a list object, called columns:

columns = ['AGE1', 'FMR', 'TOTSAL', 'year']

and passed it into the filter criteria:

filtered_df = df[columns]

Instead of creating two different DataFrame objects (like filtered_housing_2005, filtered_housing_2007, etc), we created an empty list called new_df_list:

new_df_list = list()

and appended each of the filtered_df objects to it:

new_df_list.append(filtered_df)

As you can see, we placed a heavy emphasis on abstracting, or generalizing, our logic so we can detail the logic once, and apply it in many cases. The filter_columns function that we wrote is essentially a piece of software that will filter any list of DataFrame objects into the 4 columns we want. Whether the list of DataFrame objects has 1 DataFrame object or 25, the same function can be applied to get the result we want. Another abstraction we could implement would be to modify the function and specify the columns we want filtered every time by adding it as an input to the function (alongside data_frames_list). This way, instead of always using a specific set of columns within the function, the user can now specify in the input which columns they prefer to filter their DataFrames.

This is the power of abstraction. It allows us to automate repetitive work incredibly easily.

###6: Column Filtering Verification

Let's quickly verify that each of the DataFrame objects in filtered_data_frames_list only contains the 4 columns we specified in columns. Here we will write a print() statement within a for loop to print all of the columns in each DataFrame housed in filtered_data_frames_list.


```python
# For every dataframe in the list 'filtered_data_frames_list'.
for df in filtered_data_frames_list:
    # Print dataframe columns.
    print df.columns
```

    Index([u'AGE1', u'FMR', u'TOTSAL', u'year'], dtype='object')
    Index([u'AGE1', u'FMR', u'TOTSAL', u'year'], dtype='object')
    

###7: Summary

As you can see, our column filter was applied to every DataFrame in the list, filtered_data_frames_list, and each DataFrame now contains only the 4 columns we are interested in.

###8: Multiple Dataset Analysis

Now let's write a function that counts the number of rows in each DataFrame that have negative values for the AGE1 column. We will also use Python's ability to custom print values.

In the following code block:

print( str(year) + " - " + str(len( negative_age_count ) ) + " rows")

we use the function str() to convert Integer objects, like year and len(negative_age_count), into String objects. The print function can only print String objects, so we must convert other objects to String objects. While not all objects can be converted to String objects for displaying, most can and we will cover in a later lesson how we can tell.


```python
# For every dataframe in the list 'filtered_data_frames_list'.
for df in filtered_data_frames_list:
    # Get the dataframe year.
    year = df['year'][0]
    # Return rows with negative age values.
    negative_age_count = df[df['AGE1']<0]
    # Print row count.
    print str(year) + " - " + str(len( negative_age_count ) ) + " rows"
```

    2005 - 3493 rows
    2007 - 3622 rows
    

###9: Explanation

As we loop through filtered_data_frames_list, we print that DataFrame's year, add (using +) a "-", add the len(negative_age_count) , and then finally add the text "rows".

Looks like both 2005 and 2007 have several thousand rows with negative ages. Its our job to clean this up now.

###10: Multiple Dataset Cleanup

If you recall from the previous mission, the 2013 dataset had 4438 rows with negative ages. The 2005 and 2007 datasets are not as bad, but now we have to clean up two years’ data at the same time. Let's write a function that automates the clean up we did in the last mission so that we are left only with the rows that contain positive values for the AGE1 column.

Now let's write a function clean_rows() that takes a List of DataFrames and returns a List of cleaned DataFrames with just rows containing positive AGE1 values.

Inside the function, we will first instantiate, or create, an empty list with no elements:

cleaned_list = list()

Then, we will iterate through each DataFrame in filtered_data_frames_list, create a temporary DataFrame cleaned_df containing just the positive AGE1 rows for each DataFrame:

cleaned_df = df[ df ['AGE1'] > 0 ]

And then we will append cleaned_df to cleaned_list for each iteration:

cleaned_list.append(cleaned_df)

Let's run this function clean_rows on data_frames_list and assign the results to cleaned_data_frames_list.


```python
def clean_rows(filtered_data_frames_list):
    # Create list.
    cleaned_list = list()
    
    # For every dataframe in the list 'filtered_data_frames_list'.
    for df in filtered_data_frames_list:
        # Return rows with positive age values.
        cleaned_df = df[df['AGE1']>0] 
        # Append filtered dataframe to 'cleaned_list'.
        cleaned_list.append(cleaned_df)
    return cleaned_list

cleaned_data_frames_list = clean_rows(filtered_data_frames_list)

print cleaned_data_frames_list
```

    [       AGE1   FMR  TOTSAL  year
    0        43   680   20000  2005
    1        44   760   71000  2005
    2        58   680   63000  2005
    3        22   519   27040  2005
    4        48   600   14000  2005
    5        42   788   42000  2005
    7        23   546   48000  2005
    8        51   680   58000  2005
    9        47  1081  125000  2005
    10       66  1081       0  2005
    11       47  1006   54400  2005
    12       30   874  439364  2005
    13       49   916   75000  2005
    14       60   972       0  2005
    15       47   862   80000  2005
    16       59   629     550  2005
    17       45   862   42000  2005
    18       54   607   65000  2005
    19       35   892   57000  2005
    21       33   972   58000  2005
    22       42   760   59050  2005
    23       37   963   44000  2005
    24       52   879  136000  2005
    26       27   750   42500  2005
    27       54  1035    5000  2005
    28       37   833    2000  2005
    29       52   940   77883  2005
    30       70  1080       0  2005
    31       82  1017       0  2005
    32       46  1168   14000  2005
    ...     ...   ...     ...   ...
    46821    27   677   62000  2005
    46822    53   972       0  2005
    46823    42  1267   95000  2005
    46824    47  1190   53200  2005
    46825    28  1397   91000  2005
    46826    23   677   30000  2005
    46828    84   817       0  2005
    46829    36  1168   79919  2005
    46830    30  1607   82000  2005
    46831    54  1094   54000  2005
    46832    46  1190   79000  2005
    46833    46  1168   48000  2005
    46834    58   817   42500  2005
    46835    62  1168  124000  2005
    46836    56  1420   82000  2005
    46837    34  1420  103000  2005
    46838    41  1168   52000  2005
    46839    56  1607   85000  2005
    46840    30   825   24000  2005
    46841    60   825  100000  2005
    46842    46   693   46500  2005
    46843    28   825   50000  2005
    46844    26  1397   61000  2005
    46845    23  1190   57000  2005
    46846    34  1633  200000  2005
    46847    46  1168  302000  2005
    46848    33  1168  105000  2005
    46849    40  1397   65000  2005
    46850    44  1397  280400  2005
    46852    44  1420   75000  2005
    
    [43360 rows x 4 columns],        AGE1   FMR  TOTSAL  year
    1        69  1048       0  2007
    2        45   757   26000  2007
    3        47   847  126000  2007
    4        30   616   42000  2007
    5        50   605   15000  2007
    6        44   807  145000  2007
    8        24   599   96000  2007
    9        53   757   85000  2007
    10       49   974  165000  2007
    11       44   974   71000  2007
    12       61   956  104000  2007
    13       29   572       0  2007
    14       21   572   25000  2007
    15       49  1097   93000  2007
    16       31   871  485968  2007
    17       51   900   53500  2007
    18       49   930   90000  2007
    19       61   930       0  2007
    20       45   930       0  2007
    21       53   923  150000  2007
    22       56   818  125000  2007
    23       20   583   12000  2007
    24       48  1169  200000  2007
    25       34  1042   81000  2007
    26       44   847   70000  2007
    27       39   961   55000  2007
    28       54   882  130000  2007
    29       46   948  150000  2007
    30       50   951   50000  2007
    32       24   700   55000  2007
    ...     ...   ...     ...   ...
    42696    71  1010       0  2007
    42697    19   896     100  2007
    42698    36  1278   96000  2007
    42700    47  1097   80400  2007
    42701    44  1147  116000  2007
    42702    65   896   90000  2007
    42703    45  1784   80000  2007
    42704    33  1359  176000  2007
    42705    50   648   44000  2007
    42706    55  1042       0  2007
    42707    49  1139   48000  2007
    42708    21   648   10000  2007
    42710    38  1278   32000  2007
    42711    34  1470  100002  2007
    42712    44  1169  162000  2007
    42713    48  1139   25000  2007
    42714    48  1278   74100  2007
    42715    65  1278   87000  2007
    42716    58  1359  120000  2007
    42717    67   963       0  2007
    42718    58  1517       0  2007
    42719    65  1517       0  2007
    42721    35  1517   12000  2007
    42722    24  1359   60000  2007
    42723    48  1278  310000  2007
    42724    57  1278   40800  2007
    42725    42  1517   94000  2007
    42726    46  1517  185000  2007
    42727    25   782       0  2007
    42728    45  1310   90000  2007
    
    [39107 rows x 4 columns]]
    

###11: Verify Cleanup

Let's write a quick function to verify that cleaned_data_frames_list doesn't contain any DataFrame objects that have negative values for the AGE1 column.

####Instructions

Run the function verify_cleanup on cleaned_data_frames_list and assign the result to a new variable, verification_count.


```python
def verify_cleanup(data_frames_list):
    # Create count.
    negative_rows_count = 0
    
    # For every dataframe in the list 'data_frames_list'.
    for df in data_frames_list:
        # Add the number of negative rows to 'negative_rows_count'.
        negative_rows_count += len(df[df['AGE1']<0])
    return negative_rows_count

verification_count = -1
verification_count = verify_cleanup(cleaned_data_frames_list)

print verification_count
```

    0
    

###12: Summary

There are zero 0 rows in all of the DataFrame objects in data_frames_list with negative values for the AGE1 column. Just like with the filter_columns function that we wrote before, clean_rows can now be applied to any future HUD datasets that we want without having to rewrite all of the logic we just wrote.

###13: Conclusion

In this mission, you learned the power of automation by using lists, functions, filters and for loops. The process of writing code once that you can then apply in many situations is an underlying concept and principle in programming called Don’t Repeat Yourself, or DRY. By writing abstracted, or generalized, code that is versatile, you not only save yourself precious time, but ensure that your programs run efficiently and without bugs.
