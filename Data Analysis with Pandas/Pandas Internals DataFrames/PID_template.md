

```python
from __future__ import print_function
```

#Data Analysis with Pandas

##Pandas Internals: DataFrames

###1: Shared index

DataFrame objects were designed to easily query and interact with many columns, each of which is represented as a Series object. We discussed how Series objects work in the previous mission and in this mission we'll learn about how DataFrames build on Series objects to provide a powerful data analysis toolkit. 

Series objects maintain data alignment between the index labels and the data values. Since DataFrame objects are, at the core, a collection of columns where each column is a Series, they also maintain alignment along both the columns and the rows. Pandas DataFrames utilize a shared row index across columns, which is an integer index by default. By default, Pandas enforces this shared row index by throwing an error if you read in a CSV where the columns don't contain exactly the same number of elements.

Whenever you call a method that returns or prints a DataFrame, the left-most column contains the values for the index. You can use the index attribute to access the values in the index directly as well. For this mission, we're going to continue working with the dataset containing average user and critic ratings from the major film review sites. FiveThirtyEight has compiled the dataset and made it available on their <a href = "https://github.com/fivethirtyeight/data/tree/master/fandango">Github repo</a>.

####Instructions

Read in fandango_score_comparison.csv into a DataFrame object named fandango. Then print the first 2 rows of the dataset using the head() method. Finally, print the index of the DataFrame use the index attribute.


```python
import pandas as pd
fandango = pd.read_csv('data/fandango_score_comparison.csv')

fandango.head(2)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FILM</th>
      <th>RottenTomatoes</th>
      <th>RottenTomatoes_User</th>
      <th>Metacritic</th>
      <th>Metacritic_User</th>
      <th>IMDB</th>
      <th>Fandango_Stars</th>
      <th>Fandango_Ratingvalue</th>
      <th>RT_norm</th>
      <th>RT_user_norm</th>
      <th>...</th>
      <th>IMDB_norm</th>
      <th>RT_norm_round</th>
      <th>RT_user_norm_round</th>
      <th>Metacritic_norm_round</th>
      <th>Metacritic_user_norm_round</th>
      <th>IMDB_norm_round</th>
      <th>Metacritic_user_vote_count</th>
      <th>IMDB_user_vote_count</th>
      <th>Fandango_votes</th>
      <th>Fandango_Difference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Avengers: Age of Ultron (2015)</td>
      <td>74</td>
      <td>86</td>
      <td>66</td>
      <td>7.1</td>
      <td>7.8</td>
      <td>5</td>
      <td>4.5</td>
      <td>3.70</td>
      <td>4.3</td>
      <td>...</td>
      <td>3.90</td>
      <td>3.5</td>
      <td>4.5</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>4.0</td>
      <td>1330</td>
      <td>271107</td>
      <td>14846</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cinderella (2015)</td>
      <td>85</td>
      <td>80</td>
      <td>67</td>
      <td>7.5</td>
      <td>7.1</td>
      <td>5</td>
      <td>4.5</td>
      <td>4.25</td>
      <td>4.0</td>
      <td>...</td>
      <td>3.55</td>
      <td>4.5</td>
      <td>4.0</td>
      <td>3.5</td>
      <td>4.0</td>
      <td>3.5</td>
      <td>249</td>
      <td>65709</td>
      <td>12640</td>
      <td>0.5</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 22 columns</p>
</div>




```python
print("fandango.index:\n", fandango.index)
```

    fandango.index:
     Int64Index([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9, 
                ...
                136, 137, 138, 139, 140, 141, 142, 143, 144, 145],
               dtype='int64', length=146)
    

###2: Selecting using integer index

In the previous cell, we observed the default integer index that Pandas uses for the DataFrame. In Series, each unique index value refers to a data value but in DataFrames, each index refers to an entire row. We can use the integer index to select rows a few different ways:

    # First 5 rows
    fandango[0:5]
    # From row at 140 and higher
    fandango[140:]
    # Just row at index 150
    fandango.iloc[50]
    # Just row at index 45 and 90
    fandango.iloc[[45,90]]


To select a slice, or a continuous sequence, of rows, use bracket notation, similar to when working with lists. To select an individual row, however, you need to use the <a href = "http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.iloc.html">iloc[] method</a>. The iloc[] method accepts a few different objects for selection:

- an integer
- list of integers
- slice object
- Boolean array

When selecting an individual row, Pandas will return a Series object but when selecting multiple rows, a DataFrame, representing a subset of the original DataFrame, will be returned.

####Instructions

Return a DataFrame containing just the first and the last row and assign to first_last.


```python
first_row = 0
last_row = fandango.shape[0] - 1

first_last = fandango.iloc[[first_row, last_row]]
first_last
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FILM</th>
      <th>RottenTomatoes</th>
      <th>RottenTomatoes_User</th>
      <th>Metacritic</th>
      <th>Metacritic_User</th>
      <th>IMDB</th>
      <th>Fandango_Stars</th>
      <th>Fandango_Ratingvalue</th>
      <th>RT_norm</th>
      <th>RT_user_norm</th>
      <th>...</th>
      <th>IMDB_norm</th>
      <th>RT_norm_round</th>
      <th>RT_user_norm_round</th>
      <th>Metacritic_norm_round</th>
      <th>Metacritic_user_norm_round</th>
      <th>IMDB_norm_round</th>
      <th>Metacritic_user_vote_count</th>
      <th>IMDB_user_vote_count</th>
      <th>Fandango_votes</th>
      <th>Fandango_Difference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Avengers: Age of Ultron (2015)</td>
      <td>74</td>
      <td>86</td>
      <td>66</td>
      <td>7.1</td>
      <td>7.8</td>
      <td>5.0</td>
      <td>4.5</td>
      <td>3.70</td>
      <td>4.30</td>
      <td>...</td>
      <td>3.90</td>
      <td>3.5</td>
      <td>4.5</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>4.0</td>
      <td>1330</td>
      <td>271107</td>
      <td>14846</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>145</th>
      <td>Kumiko, The Treasure Hunter (2015)</td>
      <td>87</td>
      <td>63</td>
      <td>68</td>
      <td>6.4</td>
      <td>6.7</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>4.35</td>
      <td>3.15</td>
      <td>...</td>
      <td>3.35</td>
      <td>4.5</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>19</td>
      <td>5289</td>
      <td>41</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 22 columns</p>
</div>



###3: Custom Index

The DataFrame object contains a set_index() method that allow you to pass in the column name you'd like Pandas to use as the index for the DataFrame. Pandas by default will return a new DataFrame with the custom index and will drop the specified column from the DataFrame, but the set_index() method contains a few parameters to tweak this behavior:

- inplace: if set to True, will set the index to the current DataFrame instead of returning a new one
- drop: if set to False, will keep the column you specified for the index in the DataFrame

####Instructions

Use the Pandas DataFrame method set_index to assign the FILM column as the custom index for the DataFrame without the FILM column dropped from the DataFrame. We want to keep the original DataFrame so assign the new DataFrame to fandango_films. 

Then print the index of fandango_films, which you access using the index attribute.


```python
fandango = pd.read_csv("data/fandango_score_comparison.csv")
fandango_films = fandango.set_index('FILM', drop=False)
print("fandango_films.index:\n", fandango_films.index)
```

    fandango_films.index:
     Index(['Avengers: Age of Ultron (2015)', 'Cinderella (2015)', 'Ant-Man (2015)',
           'Do You Believe? (2015)', 'Hot Tub Time Machine 2 (2015)',
           'The Water Diviner (2015)', 'Irrational Man (2015)', 'Top Five (2014)',
           'Shaun the Sheep Movie (2015)', 'Love & Mercy (2015)', 
           ...
           'The Woman In Black 2 Angel of Death (2015)', 'Danny Collins (2015)',
           'Spare Parts (2015)', 'Serena (2015)', 'Inside Out (2015)',
           'Mr. Holmes (2015)', ''71 (2015)', 'Two Days, One Night (2014)',
           'Gett: The Trial of Viviane Amsalem (2015)',
           'Kumiko, The Treasure Hunter (2015)'],
          dtype='object', name='FILM', length=146)
    

###4: Selection using custom index

Now that we have a custom index, we can select rows using film names instead of by the row number (integer index). To select rows using the custom index, you can use the loc[] method, which mirrors the iloc[] method in usage, or slice using bracket notation:

    # Slice using either bracket notation or loc[]
    fandango_films["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]
    fandango_films.loc["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]

    # Specific movie
    fandango_films.loc['Kumiko, The Treasure Hunter (2015)']

    # Selecting list of movies
    movies = ['Kumiko, The Treasure Hunter (2015)', 'Do You Believe? (2015)', 'Ant-Man (2015)']
    fandango_films.loc[movies]

When selecting multiple rows, a DataFrame is returned, but when selecting an individual row, a Series object is returned instead. Similar to with Series objects, Pandas will maintain the original integer index even if you specify a custom index so you can still take advantage of selection by row number.

####Instructions

Select just these movies in the following order from fandango_films:

- "The Lazarus Effect (2015)"
- "Gett: The Trial of Viviane Amsalem (2015)"
- "Mr. Holmes (2015)"

and assign to best_movies_ever.


```python
movies = ["The Lazarus Effect (2015)", "Gett: The Trial of Viviane Amsalem (2015)", "Mr. Holmes (2015)"]

best_movies_ever = fandango_films.loc[movies]
best_movies_ever
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FILM</th>
      <th>RottenTomatoes</th>
      <th>RottenTomatoes_User</th>
      <th>Metacritic</th>
      <th>Metacritic_User</th>
      <th>IMDB</th>
      <th>Fandango_Stars</th>
      <th>Fandango_Ratingvalue</th>
      <th>RT_norm</th>
      <th>RT_user_norm</th>
      <th>...</th>
      <th>IMDB_norm</th>
      <th>RT_norm_round</th>
      <th>RT_user_norm_round</th>
      <th>Metacritic_norm_round</th>
      <th>Metacritic_user_norm_round</th>
      <th>IMDB_norm_round</th>
      <th>Metacritic_user_vote_count</th>
      <th>IMDB_user_vote_count</th>
      <th>Fandango_votes</th>
      <th>Fandango_Difference</th>
    </tr>
    <tr>
      <th>FILM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>The Lazarus Effect (2015)</th>
      <td>The Lazarus Effect (2015)</td>
      <td>14</td>
      <td>23</td>
      <td>31</td>
      <td>4.9</td>
      <td>5.2</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>0.70</td>
      <td>1.15</td>
      <td>...</td>
      <td>2.6</td>
      <td>0.5</td>
      <td>1</td>
      <td>1.5</td>
      <td>2.5</td>
      <td>2.5</td>
      <td>62</td>
      <td>17691</td>
      <td>1651</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Gett: The Trial of Viviane Amsalem (2015)</th>
      <td>Gett: The Trial of Viviane Amsalem (2015)</td>
      <td>100</td>
      <td>81</td>
      <td>90</td>
      <td>7.3</td>
      <td>7.8</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>5.00</td>
      <td>4.05</td>
      <td>...</td>
      <td>3.9</td>
      <td>5.0</td>
      <td>4</td>
      <td>4.5</td>
      <td>3.5</td>
      <td>4.0</td>
      <td>19</td>
      <td>1955</td>
      <td>59</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Mr. Holmes (2015)</th>
      <td>Mr. Holmes (2015)</td>
      <td>87</td>
      <td>78</td>
      <td>67</td>
      <td>7.9</td>
      <td>7.4</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4.35</td>
      <td>3.90</td>
      <td>...</td>
      <td>3.7</td>
      <td>4.5</td>
      <td>4</td>
      <td>3.5</td>
      <td>4.0</td>
      <td>3.5</td>
      <td>33</td>
      <td>7367</td>
      <td>1348</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 22 columns</p>
</div>



###5: Apply() over columns

The apply() method in Pandas allows us to specify Python logic that we want evaluated over Series objects in a DataFrame. Recall that rows and columns are both represented as Series objects in a DataFrame. Here are some of the things we can accomplish using the apply() method:

- calculate the standard deviations for each numeric column
- lower-case all film names in the FILM column

The apply() method requires you to pass in a vectorized operation that can be applied over each Series object. By default, the method runs over the DataFrame's columns but you can use the axis parameter to change this (which we'll dive into later). If the vectorized operation usually returns a single value (e.g. the NumPy std() function), a Series object will be returned containing the computed value for each column. If it instead usually returns a value for each element (e.g. multiplying or dividing by 2), a DataFrame will be returned instead with the transformation made over all the values.

In the following code cell, we filter to just the float columns and use the the apply() method calculate the standard deviation using the <a href = "http://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html">NumPy std() function</a>. Under the hood, Pandas takes advantage of Series objects' vectorized operations to apply the NumPy function for each iteration of the apply() method and return a final Series object.


```python
import numpy as np

# returns the data types as a Series
types = fandango_films.dtypes
# filter data types to just floats, index attributes returns just column names
float_columns = types[types.values == 'float64'].index
# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]

# `x` is a Series object representing a column
deviations = float_df.apply(lambda x: np.std(x))

print("deviations:\n", deviations)
```

    deviations:
     Metacritic_User               1.505529
    IMDB                          0.955447
    Fandango_Stars                0.538532
    Fandango_Ratingvalue          0.501106
    RT_norm                       1.503265
    RT_user_norm                  0.997787
    Metacritic_norm               0.972522
    Metacritic_user_nom           0.752765
    IMDB_norm                     0.477723
    RT_norm_round                 1.509404
    RT_user_norm_round            1.003559
    Metacritic_norm_round         0.987561
    Metacritic_user_norm_round    0.785412
    IMDB_norm_round               0.501043
    Fandango_Difference           0.152141
    dtype: float64
    

###6: Apply() over columns, practice

Since the NumPy std() method returns a single computed value when applied over a Series, in the previous code cell, the apply() method returned a single value for each column. If you instead used a NumPy function that returns a value for each element in a list (instead of just a single computed value), you can transform all of the values in each column and return a DataFrame with the new values instead. The following code will double all of the values in the float columns:

    float_df.apply(lambda x: x*2)

This will return a new DataFrame, with each of the values in the float columns doubled, instead of modifying the object inplace.

####Instructions

Transform float_df using the apply() method to halve each value and assign to halved_df. Then print the first row.


```python
double_df = float_df.apply(lambda x: x*2)
double_df.head(1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Metacritic_User</th>
      <th>IMDB</th>
      <th>Fandango_Stars</th>
      <th>Fandango_Ratingvalue</th>
      <th>RT_norm</th>
      <th>RT_user_norm</th>
      <th>Metacritic_norm</th>
      <th>Metacritic_user_nom</th>
      <th>IMDB_norm</th>
      <th>RT_norm_round</th>
      <th>RT_user_norm_round</th>
      <th>Metacritic_norm_round</th>
      <th>Metacritic_user_norm_round</th>
      <th>IMDB_norm_round</th>
      <th>Fandango_Difference</th>
    </tr>
    <tr>
      <th>FILM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Avengers: Age of Ultron (2015)</th>
      <td>14.2</td>
      <td>15.6</td>
      <td>10</td>
      <td>9</td>
      <td>7.4</td>
      <td>8.6</td>
      <td>6.6</td>
      <td>7.1</td>
      <td>7.8</td>
      <td>7</td>
      <td>9</td>
      <td>7</td>
      <td>7</td>
      <td>8</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
halved_df = float_df.apply(lambda x: x/2)
halved_df.head(1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Metacritic_User</th>
      <th>IMDB</th>
      <th>Fandango_Stars</th>
      <th>Fandango_Ratingvalue</th>
      <th>RT_norm</th>
      <th>RT_user_norm</th>
      <th>Metacritic_norm</th>
      <th>Metacritic_user_nom</th>
      <th>IMDB_norm</th>
      <th>RT_norm_round</th>
      <th>RT_user_norm_round</th>
      <th>Metacritic_norm_round</th>
      <th>Metacritic_user_norm_round</th>
      <th>IMDB_norm_round</th>
      <th>Fandango_Difference</th>
    </tr>
    <tr>
      <th>FILM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Avengers: Age of Ultron (2015)</th>
      <td>3.55</td>
      <td>3.9</td>
      <td>2.5</td>
      <td>2.25</td>
      <td>1.85</td>
      <td>2.15</td>
      <td>1.65</td>
      <td>1.775</td>
      <td>1.95</td>
      <td>1.75</td>
      <td>2.25</td>
      <td>1.75</td>
      <td>1.75</td>
      <td>2</td>
      <td>0.25</td>
    </tr>
  </tbody>
</table>
</div>



###7: Apply() over rows

So far we've used the default behavior of the apply() method, which operates over the columns in a DataFrame. To apply a function the rows (each row will be treated as a Series object) in a DataFrame, we need to set the axis parameter to 1 after we specify the function we want applied. Applying over the rows allows us to, for example, calculate the standard deviation of multiple column values for each movie:

- rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
- rt_mt_user.apply(lambda x: np.std(x), axis=1)

This code filters the DataFrame to the two we want and then returns a Series object (since std() returns a value for each iteration) containing the standard deviation of each movie's values for RT_user_norm and Metacritic_user_norm.

####Instructions

Use the apply() method to calculate the average of each movie's values for RT_user_norm and Metacritic_user_norm and assign to the variable rt_mt_means. Then print the first 5 values.


```python
rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_means = rt_mt_user.apply(lambda x: np.mean(x), axis=1)
print("rt_mt_means[0:5]:\n", rt_mt_means[0:5])
```

    rt_mt_means[0:5]:
     FILM
    Avengers: Age of Ultron (2015)    3.925
    Cinderella (2015)                 3.875
    Ant-Man (2015)                    4.275
    Do You Believe? (2015)            3.275
    Hot Tub Time Machine 2 (2015)     1.550
    dtype: float64
    
