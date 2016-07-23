

```python
from __future__ import print_function
```

#Exploring Topics in Data Science

##K-Nearest Neighbors Introduction

###1: A look at the data

Before we get started with the KNN algorithm, let's take a look at our data. Each row in the data contains information on how a player performed in the 2013-2014 NBA season.

Here are some selected columns:

- player -- name of the player
- pos -- the position of the player
- g -- number of games the player was in
- gs -- number of games the player started
- pts -- total points the player scored

See <a href = "http://www.databasebasketball.com/about/aboutstats.htm">this site</a> for an explanation of the rest of them.


```python
import pandas
with open("data/nba_2013.csv", "r") as csvfile:
    nba_raw = pandas.read_csv(csvfile)

# Replace NaN values with zeros.
nba = nba_raw.fillna(0)

# Convert strings to NaN and drop.
nba = nba.convert_objects(convert_numeric=True).dropna()
    
# The names of the columns in the data.
print("nba.columns.values:", nba.columns.values)

nba.head(5)
```

    nba.columns.values: ['Rk' 'Player' 'Pos' 'Age' 'Tm' 'G' 'GS' 'MP' 'FG' 'FGA' 'FG%' '3P' '3PA'
     '3P.1' '2P' '2PA' '2P.1' 'eFG%' 'FT' 'FTA' 'FT%' 'ORB' 'DRB' 'TRB' 'AST'
     'STL' 'BLK' 'TOV' 'PF' 'PTS']
    




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rk</th>
      <th>Player</th>
      <th>Pos</th>
      <th>Age</th>
      <th>Tm</th>
      <th>G</th>
      <th>GS</th>
      <th>MP</th>
      <th>FG</th>
      <th>FGA</th>
      <th>...</th>
      <th>FT%</th>
      <th>ORB</th>
      <th>DRB</th>
      <th>TRB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Quincy Acy</td>
      <td>PF</td>
      <td>22</td>
      <td>TOR</td>
      <td>29</td>
      <td>0</td>
      <td>342</td>
      <td>42</td>
      <td>75</td>
      <td>...</td>
      <td>0.816</td>
      <td>30</td>
      <td>47</td>
      <td>77</td>
      <td>11</td>
      <td>13</td>
      <td>15</td>
      <td>17</td>
      <td>53</td>
      <td>116</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Jeff Adrien</td>
      <td>PF</td>
      <td>26</td>
      <td>CHA</td>
      <td>52</td>
      <td>5</td>
      <td>713</td>
      <td>72</td>
      <td>168</td>
      <td>...</td>
      <td>0.650</td>
      <td>68</td>
      <td>128</td>
      <td>196</td>
      <td>36</td>
      <td>18</td>
      <td>27</td>
      <td>32</td>
      <td>80</td>
      <td>209</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Arron Afflalo</td>
      <td>SF</td>
      <td>27</td>
      <td>ORL</td>
      <td>64</td>
      <td>64</td>
      <td>2307</td>
      <td>397</td>
      <td>905</td>
      <td>...</td>
      <td>0.857</td>
      <td>29</td>
      <td>210</td>
      <td>239</td>
      <td>206</td>
      <td>40</td>
      <td>11</td>
      <td>138</td>
      <td>137</td>
      <td>1057</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Josh Akognon</td>
      <td>PG</td>
      <td>26</td>
      <td>DAL</td>
      <td>3</td>
      <td>0</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>...</td>
      <td>0.000</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Cole Aldrich</td>
      <td>C</td>
      <td>24</td>
      <td>TOT</td>
      <td>45</td>
      <td>0</td>
      <td>388</td>
      <td>44</td>
      <td>80</td>
      <td>...</td>
      <td>0.600</td>
      <td>30</td>
      <td>90</td>
      <td>120</td>
      <td>9</td>
      <td>5</td>
      <td>23</td>
      <td>23</td>
      <td>60</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 30 columns</p>
</div>



###2: KNN overview

The k-nearest neighbors is based around the simple idea of predicting unknown values by matching them with the most similar known values.

Let's say that we have 3 different types of cars:

    car,horsepower,racing_stripes,is_fast
    Honda Accord,180,False,False
    Yugo,500,True,True
    Delorean DMC-12,200,True,True

Let's say that we now have another car:

    Chevrolet Camaro,400,True,Unknown

We don't know whether or not this car is fast. In order to predict if it is, we find the most similar known car. In this case, we would compare the horsepower and racing_stripes values to find the most similar car, which is the Yugo. Since the Yugo is fast, we would predict that the Camaro is also fast. This is an example of 1-nearest neighbors -- we only looked at the most similar car.

If we performed a 2-nearest neighbors, we would end up with 2 True values (for the Delorean and the Yugo), which would average out to True.

If we did 3-nearest neighbors, we would end up with 2 True values and a False value, which would average out to True.

###3: Euclidean distance

Before we can predict using KNN, we need to find some way to figure out which data rows are "closest" to the row we're trying to predict on.

A simple way to do this is to use Euclidean distance. The formula is 
$\sqrt{(q_1-p_1)^2 + (q_2-p_2)^2 + \cdots + (q_n-p_n)^2}$

Let's say we have these two rows (True/False has been converted to 1/0), and we want to find the distance between them:

    Honda Accord,180,0
    Chevrolet Camaro,400,1

We would first only select the numeric columns. Then the distance becomes 
$\sqrt{(180-400)^2 + (0-1)^2}$, which is about equal to 220.

####Instructions

Make a function for calculating the euclidean distance between two pandas series. Use the function to find the euclidean distance between selected_player and each row in nba. Use the .apply(func, axis=1) method on dataframes to apply function func to each row. The function should take row as its first argument. Only use the columns in distance_columns to compute the distance. <a href= "http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.apply.html">Here's</a> more on the method.

Assign the resulting pandas series to lebron_distance.


```python
import math

selected_player = nba[nba["Player"] == "LeBron James"].iloc[0]
distance_columns = ['Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA',
 '3P.1', '2P', '2PA', '2P.1', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST',
 'STL', 'BLK', 'TOV', 'PF', 'PTS']

def euclidean_distance(row):
    inner_value = 0
    for k in distance_columns:
        inner_value += (row[k] - selected_player[k]) ** 2
    return math.sqrt(inner_value)

lebron_distance = nba.apply(euclidean_distance, axis=1)
print("lebron_distance[:5]:\n", lebron_distance[:5])
```

    lebron_distance[:5]:
     0    3878.055056
    1    3485.609452
    2    1561.897265
    3    4237.902735
    4    3845.353715
    dtype: float64
    

###4: Normalizing columns

Variables which are much larger in absolute terms have the potential to have a larger impact on distance. This can be bad, because a variable having larger values doesn't necessarily make it better at predicting what rows are similar.

A simple way to deal with this is to normalize all the columns to have a mean of 0, and a standard deviation of 1. This will ensure that no single column has a dominant impact on the euclidean distance calculations.

To set the mean to 0, we have to find the mean of a column, then subtract the mean from every value in the column. To set the standard deviation to 1, we divide every value in the column by the standard deviation. The formula is $x=\frac{x-\mu}{\sigma}$.

####Instructions

Normalize the columns in nba_numeric. Using .mean() on a dataframe will return the mean of each column. Using .std() will return the standard deviation of each column.


```python
nba_numeric = nba[distance_columns]
nba_numeric.head(5)

nba_normalized = (nba_numeric - nba_numeric.mean()) / nba_numeric.std()
nba_normalized.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>G</th>
      <th>GS</th>
      <th>MP</th>
      <th>FG</th>
      <th>FGA</th>
      <th>FG%</th>
      <th>3P</th>
      <th>3PA</th>
      <th>3P.1</th>
      <th>...</th>
      <th>FT%</th>
      <th>ORB</th>
      <th>DRB</th>
      <th>TRB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-1.072090</td>
      <td>-0.779918</td>
      <td>-0.788082</td>
      <td>-0.877945</td>
      <td>-0.786532</td>
      <td>-0.864840</td>
      <td>1.275708</td>
      <td>-0.692923</td>
      <td>-0.744648</td>
      <td>1.442072</td>
      <td>...</td>
      <td>0.623629</td>
      <td>-0.345612</td>
      <td>-0.684541</td>
      <td>-0.600830</td>
      <td>-0.716027</td>
      <td>-0.658966</td>
      <td>-0.254608</td>
      <td>-0.773548</td>
      <td>-0.563340</td>
      <td>-0.764147</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.126638</td>
      <td>0.107234</td>
      <td>-0.612946</td>
      <td>-0.455442</td>
      <td>-0.601922</td>
      <td>-0.597891</td>
      <td>0.051613</td>
      <td>-0.714468</td>
      <td>-0.744648</td>
      <td>-1.283917</td>
      <td>...</td>
      <td>-0.158543</td>
      <td>0.284652</td>
      <td>-0.096167</td>
      <td>0.020484</td>
      <td>-0.519700</td>
      <td>-0.513235</td>
      <td>0.117009</td>
      <td>-0.526808</td>
      <td>-0.167436</td>
      <td>-0.550369</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.109725</td>
      <td>0.570095</td>
      <td>1.453660</td>
      <td>1.359842</td>
      <td>1.398023</td>
      <td>1.517615</td>
      <td>0.145056</td>
      <td>0.836742</td>
      <td>1.215335</td>
      <td>0.351676</td>
      <td>...</td>
      <td>0.816816</td>
      <td>-0.362198</td>
      <td>0.499470</td>
      <td>0.244992</td>
      <td>0.815321</td>
      <td>0.127978</td>
      <td>-0.378481</td>
      <td>1.216818</td>
      <td>0.668362</td>
      <td>1.398917</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.126638</td>
      <td>-1.782785</td>
      <td>-0.788082</td>
      <td>-1.257173</td>
      <td>-1.032679</td>
      <td>-1.068641</td>
      <td>0.715054</td>
      <td>-0.692923</td>
      <td>-0.744648</td>
      <td>1.442072</td>
      <td>...</td>
      <td>-3.221262</td>
      <td>-0.843189</td>
      <td>-1.018679</td>
      <td>-0.997636</td>
      <td>-0.794557</td>
      <td>-1.037865</td>
      <td>-0.719130</td>
      <td>-1.053186</td>
      <td>-1.296497</td>
      <td>-1.019301</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.599364</td>
      <td>-0.162769</td>
      <td>-0.788082</td>
      <td>-0.825559</td>
      <td>-0.774225</td>
      <td>-0.850488</td>
      <td>1.182265</td>
      <td>-0.714468</td>
      <td>-0.761119</td>
      <td>-1.283917</td>
      <td>...</td>
      <td>-0.394137</td>
      <td>-0.345612</td>
      <td>-0.372194</td>
      <td>-0.376322</td>
      <td>-0.731733</td>
      <td>-0.892134</td>
      <td>-0.006864</td>
      <td>-0.674852</td>
      <td>-0.460699</td>
      <td>-0.800926</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 26 columns</p>
</div>



###5: Finding the nearest neighbor

We now know enough to find the nearest neighbor of a given row. We can use the distance.euclidean function from scipy.spatial, a much faster way to calculate euclidean distance.

####Instructions

Find the player most similar to LeBron James by our distance metric. You can do this by finding the second lowest value in the euclidean_distances series (the lowest value will correspond to lebron, as he is most similar to himself), and then cross-referencing the nba dataframe with the same index.

Assign the name of the player to most_similar_to_lebron.


```python
from scipy.spatial import distance

# Fill in NA values in nba_normalized.
nba_normalized.fillna(0, inplace=True)

# Find the normalized vector for lebron james.
lebron_normalized = nba_normalized[nba["Player"] == "LeBron James"]

# Find the distance between lebron james and everyone else.
euclidean_distances = nba_normalized.apply(lambda row: distance.euclidean(row, lebron_normalized), axis=1)
distance_frame = pandas.DataFrame(data={"dist": euclidean_distances, "idx": euclidean_distances.index})
distance_frame.sort("dist", inplace=True)

second_smallest = distance_frame.iloc[1]["idx"]

most_similar_to_lebron = nba.loc[int(second_smallest)]["Player"]
print("most_similar_to_lebron:", most_similar_to_lebron)
```

    most_similar_to_lebron: Russell Westbrook
    

###6: Generating training and testing sets

Now that we know how to find the nearest neighbors, we can make predictions on a test set.

First, we have to generate test and train sets. In order to do this, we'll use random sampling. We'll randomly shuffle the index of the nba dataframe, and then pick rows using the randomly shuffled values.

If we didn't do this, we'd end up predicting and training on the same data set, which would overfit. We could do cross validation also, which would be slightly better, but slightly more complex.


```python
import random
from numpy.random import permutation

# Randomly shuffle the index of nba.
random_indices = permutation(nba.index)

# Set a cutoff for how many items we want in the test set (in this case 1/3 of the items).
test_cutoff = math.floor(len(nba)/3)

# Generate the test set by taking the first 1/3 of the randomly shuffled indices.
test = nba.loc[random_indices[1:test_cutoff]]

# Generate the train set with the rest of the data.
train = nba.loc[random_indices[test_cutoff:]]
```

###7: Using sklearn

Instead of having to do it all ourselves, we can use the k-nearest neighbors implementation in scikit-learn. <a href = "http://scikit-learn.org/stable/modules/neighbors.html">Here's</a> the documentation. There's a regressor and a classifier available, but we'll be using the regressor, as we have continuous values to predict on.

Sklearn performs the normalization and distance finding automatically, and lets us specify how many neighbors we want to look at.


```python
from sklearn.neighbors import KNeighborsRegressor

# The columns that we will be making predictions with.
x_columns = ['Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA',
 '3P.1', '2P', '2PA', '2P.1', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST',
 'STL', 'BLK', 'TOV', 'PF']
# The column that we want to predict.
y_column = ['PTS']

# Create the knn model.
knn = KNeighborsRegressor(n_neighbors=5)

# Fit the model on the training data.
knn.fit(train[x_columns], train[y_column])

# Make predictions on the test set using the fit model.
predictions = knn.predict(test[x_columns])

print("predictions[:5]:\n", predictions[:5])
```

    predictions[:5]:
     [[  58.2]
     [  73. ]
     [ 490.6]
     [ 194.2]
     [ 372.2]]
    

###8: Computing error

Now that we know our predictions, we can compute the error involved. We can compute <a href = "http://en.wikipedia.org/wiki/Mean_squared_error">mean squared error</a>. The formula is $\frac{1}{n}\sum_{i=1}^{n}(\hat{y_{i}} - y_{i})^{2}$.

####Instructions

Compute the mean squared error between actual and predictions. Assign the result to mse.


```python
actual = test[y_column]

mse = (((predictions - actual) ** 2).sum()) / len(predictions)

print("actual[:20]:\n", actual[:20])
print("mse:", mse)
```

    actual[:20]:
           PTS
    15     44
    361    51
    438   441
    406   232
    113   486
    311    77
    216   625
    370   165
    547   353
    350  1077
    583   146
    585   929
    559   531
    371   729
    92      0
    28    356
    501   687
    211   208
    255  1038
    264  2036
    mse: PTS    4925.349895
    dtype: float64
    
