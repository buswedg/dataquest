
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Exploring Topics in Data Science

# ##K-Nearest Neighbors Introduction

# ###1: A look at the data

# Before we get started with the KNN algorithm, let's take a look at our data. Each row in the data contains information on how a player performed in the 2013-2014 NBA season.
# 
# Here are some selected columns:
# 
# - player -- name of the player
# - pos -- the position of the player
# - g -- number of games the player was in
# - gs -- number of games the player started
# - pts -- total points the player scored
# 
# See <a href = "http://www.databasebasketball.com/about/aboutstats.htm">this site</a> for an explanation of the rest of them.

# In[2]:

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


# ###2: KNN overview

# The k-nearest neighbors is based around the simple idea of predicting unknown values by matching them with the most similar known values.
# 
# Let's say that we have 3 different types of cars:
# 
#     car,horsepower,racing_stripes,is_fast
#     Honda Accord,180,False,False
#     Yugo,500,True,True
#     Delorean DMC-12,200,True,True
# 
# Let's say that we now have another car:
# 
#     Chevrolet Camaro,400,True,Unknown
# 
# We don't know whether or not this car is fast. In order to predict if it is, we find the most similar known car. In this case, we would compare the horsepower and racing_stripes values to find the most similar car, which is the Yugo. Since the Yugo is fast, we would predict that the Camaro is also fast. This is an example of 1-nearest neighbors -- we only looked at the most similar car.
# 
# If we performed a 2-nearest neighbors, we would end up with 2 True values (for the Delorean and the Yugo), which would average out to True.
# 
# If we did 3-nearest neighbors, we would end up with 2 True values and a False value, which would average out to True.

# ###3: Euclidean distance

# Before we can predict using KNN, we need to find some way to figure out which data rows are "closest" to the row we're trying to predict on.
# 
# A simple way to do this is to use Euclidean distance. The formula is 
# $\sqrt{(q_1-p_1)^2 + (q_2-p_2)^2 + \cdots + (q_n-p_n)^2}$
# 
# Let's say we have these two rows (True/False has been converted to 1/0), and we want to find the distance between them:
# 
#     Honda Accord,180,0
#     Chevrolet Camaro,400,1
# 
# We would first only select the numeric columns. Then the distance becomes 
# $\sqrt{(180-400)^2 + (0-1)^2}$, which is about equal to 220.

# ####Instructions

# Make a function for calculating the euclidean distance between two pandas series. Use the function to find the euclidean distance between selected_player and each row in nba. Use the .apply(func, axis=1) method on dataframes to apply function func to each row. The function should take row as its first argument. Only use the columns in distance_columns to compute the distance. <a href= "http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.apply.html">Here's</a> more on the method.
# 
# Assign the resulting pandas series to lebron_distance.

# In[3]:

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


# ###4: Normalizing columns

# Variables which are much larger in absolute terms have the potential to have a larger impact on distance. This can be bad, because a variable having larger values doesn't necessarily make it better at predicting what rows are similar.
# 
# A simple way to deal with this is to normalize all the columns to have a mean of 0, and a standard deviation of 1. This will ensure that no single column has a dominant impact on the euclidean distance calculations.
# 
# To set the mean to 0, we have to find the mean of a column, then subtract the mean from every value in the column. To set the standard deviation to 1, we divide every value in the column by the standard deviation. The formula is $x=\frac{x-\mu}{\sigma}$.

# ####Instructions

# Normalize the columns in nba_numeric. Using .mean() on a dataframe will return the mean of each column. Using .std() will return the standard deviation of each column.

# In[4]:

nba_numeric = nba[distance_columns]
nba_numeric.head(5)

nba_normalized = (nba_numeric - nba_numeric.mean()) / nba_numeric.std()
nba_normalized.head(5)


# ###5: Finding the nearest neighbor

# We now know enough to find the nearest neighbor of a given row. We can use the distance.euclidean function from scipy.spatial, a much faster way to calculate euclidean distance.

# ####Instructions

# Find the player most similar to LeBron James by our distance metric. You can do this by finding the second lowest value in the euclidean_distances series (the lowest value will correspond to lebron, as he is most similar to himself), and then cross-referencing the nba dataframe with the same index.
# 
# Assign the name of the player to most_similar_to_lebron.

# In[5]:

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


# ###6: Generating training and testing sets

# Now that we know how to find the nearest neighbors, we can make predictions on a test set.
# 
# First, we have to generate test and train sets. In order to do this, we'll use random sampling. We'll randomly shuffle the index of the nba dataframe, and then pick rows using the randomly shuffled values.
# 
# If we didn't do this, we'd end up predicting and training on the same data set, which would overfit. We could do cross validation also, which would be slightly better, but slightly more complex.

# In[6]:

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


# ###7: Using sklearn

# Instead of having to do it all ourselves, we can use the k-nearest neighbors implementation in scikit-learn. <a href = "http://scikit-learn.org/stable/modules/neighbors.html">Here's</a> the documentation. There's a regressor and a classifier available, but we'll be using the regressor, as we have continuous values to predict on.
# 
# Sklearn performs the normalization and distance finding automatically, and lets us specify how many neighbors we want to look at.

# In[10]:

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


# ###8: Computing error

# Now that we know our predictions, we can compute the error involved. We can compute <a href = "http://en.wikipedia.org/wiki/Mean_squared_error">mean squared error</a>. The formula is $\frac{1}{n}\sum_{i=1}^{n}(\hat{y_{i}} - y_{i})^{2}$.

# ####Instructions

# Compute the mean squared error between actual and predictions. Assign the result to mse.

# In[9]:

actual = test[y_column]

mse = (((predictions - actual) ** 2).sum()) / len(predictions)

print("actual[:20]:\n", actual[:20])
print("mse:", mse)

