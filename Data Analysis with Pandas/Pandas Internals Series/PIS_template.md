

```python
from __future__ import print_function
```

#Data Analysis with Pandas

##Pandas Internals: Series

###1: Data structures

In this mission and the next, we're going to dive into some of Pandas' internals to better understand how Pandas does things under the hood.

The three key data structures in Pandas are:

- Series (collection of values)
- DataFrame (collection of Series objects)
- Panel (collection of DataFrame objects)

and we'll be focusing on the Series object in this mission.

Series objects use NumPy arrays for fast computation but build on them by adding features valuable for analyzing data. For example, while NumPy arrays utilize an integer index, Series objects can utilize other index types, like a string index. Series objects also allow for mixed data types and utilize the NaN Python value for handling missing values.

A Series object can hold many data types, including:

- float - for representing float values
- int - for representing integer values
- bool - for representing Boolean values
- datetime64[ns] - for representing date & time, without time-zone
- datetime64[ns, tz] - for representing date & time, with time-zone
- timedelta[ns] - for representing differences in dates & times (seconds, minutes, etc.)
- category - for representing categorical values
- object - for representing String values

Before we dive further, let's introduce the dataset we'll be working with. The FiveThirtyEight team recently released a dataset containing the critics scores for all movies that have substantive user and critic reviews from IMDB, Rotten Tomatoes, Metacritic, and Fandango. We'll be working with the file fandango_score_comparison.csv, which you can download from their <a href = "https://github.com/fivethirtyeight/data/tree/master/fandango">Github repo</a>. Here are some of the columns in the dataset:

- FILM - film name
- RottenTomatoes - Rotten Tomatoes critics average score
- RottenTomatoes_User - Rotten Tomatoes user average score
- RT_norm - Rotten Tomatoes critics average score (normalized to a 0 to 5 point system)
- RT_user-norm - Rotten Tomatoes user average score (normalized to a 0 to 5 point system)
- Metacritic - Metacritic critics average score
- Metacritic_User - Metacritic user average score

The full column list and descriptions are available on the <a href = "https://github.com/fivethirtyeight/data/tree/master/fandango">Github repo</a>.

####Instructions

Use the read_csv() function to read in fandango_score_comparison.csv into a DataFrame object called fandango. Then use the head() function to print the first 2 rows.


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



###2: Integer index

DataFrames use Series objects to represent the columns in the data. When you select a single column from a DataFrame, Pandas will return the Series object representing that column. Each individual Series object in a DataFrame is indexed using the integer data type by default. Each value in the Series has a unique integer index, or position. The integer index is 0-indexed, like most Python data structures, and ranges from 0 to n-1, where n is the number of rows. With an integer index, you can select an individual value in the Series if you know it's position as well as select multiple values by passing in a list of index values (similar to a NumPy array). 

For both NumPy arrays and Series objects, you can utilize integer index by using bracket notation to slice and select values. Where Series objects diverge from NumPy arrays, however, is the abillity to specify a custom index for the values.

To explore this idea further, let's use two Series objects representing the film names and Rotten Tomatoes scores.

####Instructions

Select the FILM column, assign to the variable series_film, and print the first 5 values. Then select the RottenTomatoes column, assign to the variable series_rt, and print the first 5 values.


```python
import pandas as pd

fandango = pd.read_csv('data/fandango_score_comparison.csv')
series_film = fandango['FILM']
print("series_film[0:5]:\n", series_film[0:5])

series_rt = fandango['RottenTomatoes']
print("series_rt[0:5]:\n", series_rt[0:5])
```

    series_film[0:5]:
     0    Avengers: Age of Ultron (2015)
    1                 Cinderella (2015)
    2                    Ant-Man (2015)
    3            Do You Believe? (2015)
    4     Hot Tub Time Machine 2 (2015)
    Name: FILM, dtype: object
    series_rt[0:5]:
     0    74
    1    85
    2    80
    3    18
    4    14
    Name: RottenTomatoes, dtype: int64
    

###3: Custom index

Both these Series objects are use the same integer index, which means that the value at index 5, for example, would describe the same film in both Series objects (The Water Diviner (2015)). If we had a movie in mind, we need the integer index corresponding to that movie to look up information about it.

If we were given just these two Series objects and we wanted to look up the Rotten Tomatoes score for Minions (2015) and Leviathan (2014), we'd have to:
- find the integer index corresponding to Minions (2015) in series_film
- look up the value at that integer index from series_rt
- find the integer index corresponding to Leviathan (2014) in series_film
- look up the value at that integer index from series_rt

This becomes especially cumbersome as we scale up the problem to looking up information for a larger number of movies. What we really want is a way to look up the Rotten Tomatoes scores for many movies at a time using just one command (and one Series object). To accomplish this, we need to find a way to move away from using an integer index corresponding to the row number and instead use a string index corresponding to the film name. Then we can utilize bracket notation to just pass in a list of strings matching the film names and get back the Rotten Tomatoes scores:

    series_custom[['Minions (2015)', 'Leviathan (2014)']]

####Instructions

Create a new Series object, series_custom, that has a string index (the values from film_names) and contains all of the Rotten Tomatoes scores from series_rt.

To create a new Series object:
- import Series from pandas
- instantiate a new Series object, which takes in a data parameter and an index parameter (<a href = "http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html#pandas.Series">documentation</a>)
- both of these parameters need to be lists

To return a list representation of the values in a Series object, use the <a href = "http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.Series.values.html">values attribute</a> available to Series objects.


```python
# Import the Series object from pandas
from pandas import Series

film_names = series_film.values
rt_scores = series_rt.values
film_names = series_film.values
rt_scores = series_rt.values

series_custom = Series(rt_scores , index=film_names)
series_custom[['Minions (2015)', 'Leviathan (2014)']]
```




    Minions (2015)      54
    Leviathan (2014)    99
    dtype: int64



###4: Integer index preserved

Even though we specified that the Series object use a custom, string index, the object still maintains an internal integer index that we can use for selection. In this way, Series objects act both like a dictionary and a list since we can access values using our custom index (like the keys in a dictionary) or the integer index (like the index in a list).

####Instructions

Assign the values from index 5 to index 10 to the variable fiveten then print fiveten to verify that you can still utilize integer values for selecting.


```python
fiveten = series_custom[5:10]
print(fiveten)
```

    The Water Diviner (2015)        63
    Irrational Man (2015)           42
    Top Five (2014)                 86
    Shaun the Sheep Movie (2015)    99
    Love & Mercy (2015)             89
    dtype: int64
    

###5: Reindexing

Reindexing is the Pandas way of modifying the alignment between labels (index) and the data (values). The <a href = "http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.Series.reindex.html">reindex() method</a> allows you to specify an alternate ordering of the labels (index) for a Series object. This method takes in a list of strings corresponding to the order of labels you'd like for that Series object. 

We can use the reindex() method to sort series_custom in alphabetical order by film. To accomplish this, we need to:

- return a list representation of the current index using tolist()
- sort the index using sorted()
- use reindex() to set the new ordered index

The following code cell contains the logic to accomplish the first task and we'll leave it upto you to finish the rest.

####Instructions

The list original_index contains the original index. Sort this index using the Python 3 core method sorted() and then pass in the sorted index to the Series method reindex().


```python
original_index = series_custom.index.tolist()
sorted_index = sorted(original_index)
sorted_by_index = series_custom.reindex(sorted_index)
```

###6: Sorting

We learned how to sort a Series object by the index using the reindex() method in this mission. Sorting by reindexing can be cumbersome if we want to order by the rating (the values in the Series) instead of by film name or for quick exploratory data analysis. To make sorting easier, Pandas comes with a <a href = "http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.Series.sort_index.html">sort_index() method</a>, which returns a Series sorted by the index, and a <a href = "http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.Series.sort_values.html">sort_values() method</a> method, which returns a Series sorted by the values. Since the values representing the Rotten Tomatoes scores are integers, sorting by values will sort in numerically ascending order (low to high) in our case.

In both cases, the link between each element's index (film name) and value (score) is preserved. This is known as data alignment and is a key tenet of Pandas that is incredibly important when analyzing data. Unless we specifically change a value or an index, Pandas allows us to assume the linking will be preserved.

####Instructions

Sort series_custom by index using sort_index() and assign to the variable sc2. Sort series_custom by values and assign to the variable sc3. Then print the first 10 values in sc2 and the first 10 values in sc3.


```python
sc2 = series_custom.sort_index()
#sc3 = series_custom.sort_values()

print("sc2[0:10]:\n", sc2[0:10])
#print("sc3[0:10]:\n", sc3[0:10])
```

    sc2[0:10]:
     '71 (2015)                    97
    5 Flights Up (2015)           52
    A Little Chaos (2015)         40
    A Most Violent Year (2014)    90
    About Elly (2015)             97
    Aloha (2015)                  19
    American Sniper (2015)        72
    American Ultra (2015)         46
    Amy (2015)                    97
    Annie (2014)                  27
    dtype: int64
    

###7: Vectorized operations

There are many cases where you want to transform an entire column in a dataset, since a column is really a vector of values. Series objects have powerful support for vectorized operations, which enable you to run computations over an entire column incredibly quickly. Since Pandas builds on top of NumPy, it takes advantage of NumPy's vectorizaton capabilities which generates incredibly optimized, low level C code to loop over the values instead. Using a for loop to iterate over the values in a Series object to run itemwise computations is much slower, especially for larger datasets.

You can use any of the standard Python arithmetic operators (+, -, *, and /) to transform every value in a Series object. For example, if we wanted to transform the Rotten Tomatoes scores from a 0 to 100 point scale to a 0 to 10 scale, we can use the Python / division operator to divide the Series by 10:

    series_custom/10


and we'll get back a new Series object with each value divided by 10. We can even use NumPy functions to transform and run calculations over Series objects:

    # Add each value with each other
    np.add(series_custom, series_custom)
    # Apply sine function to each value
    np.sin(series_custom)
    # Return the highest value (will return a single value not a Series)
    np.max(series_custom)


The values in a Series object are treated as an ndarray, the core data type in NumPy. Applying some NumPy functions will return a new Series object while others will return just a single value. <a href = "http://docs.scipy.org/doc/numpy/reference/generated/numpy.sin.html#numpy.sin">NumPy's documentation</a> gives you a good sense of the return value for each function. Whenever a NumPy function returns an ndarray usually, when applying a NumPy function over a Series a Series object is returned instead.

####Instructions

The original DataFrame contains the column RT_norm, which represents a normalized score (from 0 to 5) of the Rotten Tomatoes average critics score. Use vectorized operations to normalize series_custom (currently on a 0 to 100 point scale) to a 0 to 5 point scale and assign the new normalized Series object to series_normalized.


```python
series_normalized = (series_custom/10)*5
series_normalized[:5]
```




    Avengers: Age of Ultron (2015)    37.0
    Cinderella (2015)                 42.5
    Ant-Man (2015)                    40.0
    Do You Believe? (2015)             9.0
    Hot Tub Time Machine 2 (2015)      7.0
    dtype: float64



###8: Comparing and filtering

Pandas utilizes vectorized operations everywhere, including when filtering values within a single Series object or comparing 2 different Series objects. For example, to find all films that had above a 50 Rotten Tomatoes average critics rating, running:

    series_custom > 50

will actually return a Series object with a Boolean value for each film. This is because the filter (> 50) is applied to each value in the Series object. To retrieve the actual films a Series object containing just the films with a rating greater than 50, we need to pass in this Boolean series into the original Series object.

To help make it easy to separate complex comparison and filtering logic into modular pieces, Pandas returns Boolean Series objects as the intermediate representation of the logic. We can specify filtering criteria in different variables and chain them together using the & operator, which represents and, as well as the | operator, representing or. Finally, we can utilize a Series object's bracket notation to pass in an expression representing a Boolean Series object to get back the filtered dataset.

####Instructions

In the following code cell, we've written 2 statements, criteria_one and criteria_two, that return Boolean Series objects. Return a filtered Series object that only contains the values where both criteria are true named both_criteria.


```python
# Display
criteria_one = series_custom > 50
criteria_two = series_custom < 75

both_criteria = series_custom[criteria_one & criteria_two]
both_criteria[:5]
```




    Avengers: Age of Ultron (2015)    74
    The Water Diviner (2015)          63
    Unbroken (2014)                   51
    Southpaw (2015)                   59
    Insidious: Chapter 3 (2015)       59
    dtype: int64



###9: Alignment

One of the core tenets of Pandas is data alignment. A Series objects align along indices and DataFrame objects align along both indices and columns. This means that for Series objects, the link between the index labels and the actual values is implicitly preserved across operations and transformations unless we explicitly break the link. For DataFrame objects, the values are linked to the index labels and the column labels and area also preserved unless we explicitly break the link (by reassigning or editing a column or index label, for example).

This core tenet allows us to use Pandas well when working with data and is a big advantages over just using NumPy objects. For Series objects in particular, this means we can use the standard Python arithmetic operators (+, -, *, and /) to add, subtract, multiple, and divide the values at each index label for 2 different Series objects.

We can take advantage of this functionality to calculate the mean of the Rotten Tomatoes' critics average rating and the Rotten Tomatoes' average user rating.

####Instructions

rt_critics and rt_users are Series objects, that contain the critics average rating and the users average rating for each film. Both Series objects use the same custom string index with the film names. Use the Python arithmetic operators to return a new Series object, named rt_mean, containing the mean of the critics and users rating for each film.


```python
rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])

rt_mean = (rt_critics + rt_users)/2
rt_mean[:5]
```




    FILM
    Avengers: Age of Ultron (2015)    80.0
    Cinderella (2015)                 82.5
    Ant-Man (2015)                    85.0
    Do You Believe? (2015)            51.0
    Hot Tub Time Machine 2 (2015)     21.0
    dtype: float64


