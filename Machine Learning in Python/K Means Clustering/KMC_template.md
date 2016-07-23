

```python
from __future__ import print_function
```

#Machine Learning in Python

##K Means Clustering

###1: Clustering NBA Players

In NBA media coverage, sports reporters usually focus on a handful of players who get a disproportionate share of the attention and paint stories of how unique these players' stats are. With our data science hats on, we can't help but feel a slight sense of skepticism to how different the players are from one another. Let's see how we can use data science to explore that thread further.

Let's look at the dataset of player performance from the 2013-2014 season.

Here are some selected columns:

- player -- name of the player
- pos -- the position of the player
- g -- number of games the player was in
- pts -- total points the player scored
- fg. -- field goal percentage
- ft. -- free throw percentage


```python
import pandas as pd
import numpy as np

nba = pd.read_csv("data/nba_2013.csv")
nba.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>player</th>
      <th>pos</th>
      <th>age</th>
      <th>bref_team_id</th>
      <th>g</th>
      <th>gs</th>
      <th>mp</th>
      <th>fg</th>
      <th>fga</th>
      <th>fg.</th>
      <th>...</th>
      <th>drb</th>
      <th>trb</th>
      <th>ast</th>
      <th>stl</th>
      <th>blk</th>
      <th>tov</th>
      <th>pf</th>
      <th>pts</th>
      <th>season</th>
      <th>season_end</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Quincy Acy</td>
      <td>SF</td>
      <td>23</td>
      <td>TOT</td>
      <td>63</td>
      <td>0</td>
      <td>847</td>
      <td>66</td>
      <td>141</td>
      <td>0.468</td>
      <td>...</td>
      <td>144</td>
      <td>216</td>
      <td>28</td>
      <td>23</td>
      <td>26</td>
      <td>30</td>
      <td>122</td>
      <td>171</td>
      <td>2013-2014</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Steven Adams</td>
      <td>C</td>
      <td>20</td>
      <td>OKC</td>
      <td>81</td>
      <td>20</td>
      <td>1197</td>
      <td>93</td>
      <td>185</td>
      <td>0.503</td>
      <td>...</td>
      <td>190</td>
      <td>332</td>
      <td>43</td>
      <td>40</td>
      <td>57</td>
      <td>71</td>
      <td>203</td>
      <td>265</td>
      <td>2013-2014</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jeff Adrien</td>
      <td>PF</td>
      <td>27</td>
      <td>TOT</td>
      <td>53</td>
      <td>12</td>
      <td>961</td>
      <td>143</td>
      <td>275</td>
      <td>0.520</td>
      <td>...</td>
      <td>204</td>
      <td>306</td>
      <td>38</td>
      <td>24</td>
      <td>36</td>
      <td>39</td>
      <td>108</td>
      <td>362</td>
      <td>2013-2014</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Arron Afflalo</td>
      <td>SG</td>
      <td>28</td>
      <td>ORL</td>
      <td>73</td>
      <td>73</td>
      <td>2552</td>
      <td>464</td>
      <td>1011</td>
      <td>0.459</td>
      <td>...</td>
      <td>230</td>
      <td>262</td>
      <td>248</td>
      <td>35</td>
      <td>3</td>
      <td>146</td>
      <td>136</td>
      <td>1330</td>
      <td>2013-2014</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Alexis Ajinca</td>
      <td>C</td>
      <td>25</td>
      <td>NOP</td>
      <td>56</td>
      <td>30</td>
      <td>951</td>
      <td>136</td>
      <td>249</td>
      <td>0.546</td>
      <td>...</td>
      <td>183</td>
      <td>277</td>
      <td>40</td>
      <td>23</td>
      <td>46</td>
      <td>63</td>
      <td>187</td>
      <td>328</td>
      <td>2013-2014</td>
      <td>2013</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 31 columns</p>
</div>



###2: Point Guards

Point guards play one of the most crucial roles on a team because their primary responsibility is to create scoring opportunities for the team. We are going to focus our lesson on a machine learning technique called clustering, which allows us to visualize the types of point guards as well as group similar point guards together. Using 2 features allows us to easily visualize the players and will also make it easier to grasp how clustering works. For point guards, it's widely accepted that the Assist to Turnover Ratio is a good indicator for performance in games as it quantifies the number of scoring opportunities that player created. Let's also use Points Per Game, since effective Point Guards not only set up scoring opportunities but also take a lot of the shots themselves.

####Instructions

Create a new pandas data frame which contains just the point guards from the data set. Point guards are specified as PG in the position column. Assign the filtered data frame to point_guards.


```python
point_guards = nba[nba['pos'] == 'PG'].copy()
point_guards.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>player</th>
      <th>pos</th>
      <th>age</th>
      <th>bref_team_id</th>
      <th>g</th>
      <th>gs</th>
      <th>mp</th>
      <th>fg</th>
      <th>fga</th>
      <th>fg.</th>
      <th>...</th>
      <th>drb</th>
      <th>trb</th>
      <th>ast</th>
      <th>stl</th>
      <th>blk</th>
      <th>tov</th>
      <th>pf</th>
      <th>pts</th>
      <th>season</th>
      <th>season_end</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>24</th>
      <td>D.J. Augustin</td>
      <td>PG</td>
      <td>26</td>
      <td>TOT</td>
      <td>71</td>
      <td>9</td>
      <td>1939</td>
      <td>298</td>
      <td>718</td>
      <td>0.415</td>
      <td>...</td>
      <td>115</td>
      <td>130</td>
      <td>313</td>
      <td>53</td>
      <td>3</td>
      <td>125</td>
      <td>147</td>
      <td>930</td>
      <td>2013-2014</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Leandro Barbosa</td>
      <td>PG</td>
      <td>31</td>
      <td>PHO</td>
      <td>20</td>
      <td>0</td>
      <td>368</td>
      <td>56</td>
      <td>131</td>
      <td>0.427</td>
      <td>...</td>
      <td>32</td>
      <td>37</td>
      <td>32</td>
      <td>7</td>
      <td>4</td>
      <td>19</td>
      <td>30</td>
      <td>150</td>
      <td>2013-2014</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Jose Barea</td>
      <td>PG</td>
      <td>29</td>
      <td>MIN</td>
      <td>79</td>
      <td>1</td>
      <td>1471</td>
      <td>254</td>
      <td>656</td>
      <td>0.387</td>
      <td>...</td>
      <td>138</td>
      <td>154</td>
      <td>303</td>
      <td>26</td>
      <td>0</td>
      <td>125</td>
      <td>129</td>
      <td>660</td>
      <td>2013-2014</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Jerryd Bayless</td>
      <td>PG</td>
      <td>25</td>
      <td>TOT</td>
      <td>72</td>
      <td>19</td>
      <td>1686</td>
      <td>248</td>
      <td>617</td>
      <td>0.402</td>
      <td>...</td>
      <td>123</td>
      <td>145</td>
      <td>194</td>
      <td>60</td>
      <td>9</td>
      <td>82</td>
      <td>161</td>
      <td>666</td>
      <td>2013-2014</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Steve Blake</td>
      <td>PG</td>
      <td>33</td>
      <td>TOT</td>
      <td>55</td>
      <td>28</td>
      <td>1498</td>
      <td>133</td>
      <td>353</td>
      <td>0.377</td>
      <td>...</td>
      <td>146</td>
      <td>159</td>
      <td>307</td>
      <td>54</td>
      <td>8</td>
      <td>102</td>
      <td>85</td>
      <td>378</td>
      <td>2013-2014</td>
      <td>2013</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 31 columns</p>
</div>



###3: Points Per Game

While our dataset doesn't come with Points Per Game values, we can easily calculate those using each player's total points (pts) and the number of games (g) they played. Let's take advantage of pandas' ability to multiply and divide columns to create the Points Per Game ppg column by dividing the pts and g columns.


```python
point_guards['ppg'] = point_guards['pts'] / point_guards['g']

# Sanity check, make sure ppg = pts/g.
point_guards[['pts', 'g', 'ppg']].head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pts</th>
      <th>g</th>
      <th>ppg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>24</th>
      <td>930</td>
      <td>71</td>
      <td>13.098592</td>
    </tr>
    <tr>
      <th>29</th>
      <td>150</td>
      <td>20</td>
      <td>7.500000</td>
    </tr>
    <tr>
      <th>30</th>
      <td>660</td>
      <td>79</td>
      <td>8.354430</td>
    </tr>
    <tr>
      <th>38</th>
      <td>666</td>
      <td>72</td>
      <td>9.250000</td>
    </tr>
    <tr>
      <th>50</th>
      <td>378</td>
      <td>55</td>
      <td>6.872727</td>
    </tr>
  </tbody>
</table>
</div>



###4: Assist Turnover Ratio

Now let's create a column, atr, for the Assist Turnover Ratio, which is calculated by dividing total assists (ast) by total turnovers (tov):

$ATR =  \frac{ Assists} {Turnovers}$

####Instructions

First, drop the players who have 0 turnovers. Not only did these players only play a few games, making it hard to understand their true abilities, but we also cannot divide by 0 when we calculate atr. Utilize the same division technique we used with Points Per Game to create the Assist Turnover Ratio (ast) column for point_guards.


```python
point_guards = point_guards[point_guards['tov'] != 0]
point_guards['atr'] = point_guards['ast'] / point_guards['tov']

point_guards[['pts', 'g', 'ppg', 'atr']].head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pts</th>
      <th>g</th>
      <th>ppg</th>
      <th>atr</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>24</th>
      <td>930</td>
      <td>71</td>
      <td>13.098592</td>
      <td>2.504000</td>
    </tr>
    <tr>
      <th>29</th>
      <td>150</td>
      <td>20</td>
      <td>7.500000</td>
      <td>1.684211</td>
    </tr>
    <tr>
      <th>30</th>
      <td>660</td>
      <td>79</td>
      <td>8.354430</td>
      <td>2.424000</td>
    </tr>
    <tr>
      <th>38</th>
      <td>666</td>
      <td>72</td>
      <td>9.250000</td>
      <td>2.365854</td>
    </tr>
    <tr>
      <th>50</th>
      <td>378</td>
      <td>55</td>
      <td>6.872727</td>
      <td>3.009804</td>
    </tr>
  </tbody>
</table>
</div>



###5: Visualizing the Point Guards

Use matplotlib to create a scatter plot with Points Per Game (ppg) on the X axis and Assist Turnover Ratio (atr) on the Y axis.


```python
import matplotlib.pyplot as plt
%matplotlib inline

plt.scatter(point_guards['ppg'], point_guards['atr'], c='y')
plt.title("Point Guards")
plt.xlabel('Points Per Game', fontsize=13)
plt.ylabel('Assist Turnover Ratio', fontsize=13)
```




    <matplotlib.text.Text at 0xb7a9550>




![png](output_21_1.png)


###6: Clustering players

There seem to be 5 general regions, or clusters, that the point guards fall into (with a few outliers of course!). We can use a technique called clustering to segment all of the point guards into groups of alike players. While regression and other supervised machine learning techniques work well when we have a clear metric we want to optimize for and lots of pre-labelled data, we need to instead use unsupervised machine learning techniques to explore the structure within a data set that doesn't have a clear value to optimize.

There are multiple ways of clustering data but here we will focus on centroid based clustering for this lesson. Centroid based clustering works well when the clusters resemble circles with centers (or centroids). The centroid represent the geometric mean of all of the data points in that cluster.

K-Means Clustering is a popular centroid-based clustering algorithm that we will use. The K in K-Means refers to the number of clusters we want to segment our data into. The key part with K-Means (and most unsupervised machine learning techniques) is that we have to specify what k is. There are advantages and disadvantages to this, but one advantage is that we can pick the k that makes the most sense for our use case. We'll set k to 5 since we want K-Means to segment our data into 5 clusters.

###7: The Algorithm

Setup K-Means is an iterative algorithm that switches between recalculating the centroid of each cluster and the players that belong to that cluster. To start, select 5 players at random and assign their coordinates as the initial centroids of the just created clusters.

Step 1 (Assign to Cluster) For each player, calculate the Euclidean distance between that player's coordinates, or values for atr & ppg, and each of the centroids' coordinates. Assign the player to the cluster whose centroid is the closest to, or has the lowest Euclidean distance to, the player's values.

Step 2 (Recalculate Centroids) For each cluster, compute the new centroid by calculating the geometric mean of all of the points (players) in that cluster. We calculate the geometric mean by taking the average of all of the X values (atr) and the average of all of the Y values (ppg) of the points in that cluster.

Iterate Repeat steps 1 & 2 until the clusters are no longer moving and have converged.


```python
import numpy as np
import random

num_clusters = 5

# Use numpy's random function to generate a list, length: num_clusters, of indices.
random_initial_points = np.random.choice(point_guards.index, size=num_clusters)

# Use the random indices to create the centroids.
centroids = point_guards.ix[random_initial_points]
```

###8: Visualize Centroids

Let's plot the centroids, in addition to the point_guards, so we can see where the randomly chosen centroids started out.


```python
import matplotlib.pyplot as plt
%matplotlib inline

plt.scatter(point_guards['ppg'], point_guards['atr'], c='yellow')
plt.scatter(centroids['ppg'], centroids['atr'], c='red')
plt.title("Centroids")
plt.xlabel('Points Per Game', fontsize=13)
plt.ylabel('Assist Turnover Ratio', fontsize=13)
```




    <matplotlib.text.Text at 0xb7ffef0>




![png](output_29_1.png)


While the centroids data frame object worked well for the initial centroids, where the centroids were just a subset of players, as we iterate the centroids' values will be coordinates that may not match another player's coordinates. Moving forward, let's use a dictionary object instead to represent the centroids.

We will need a unique identifier, like cluster_id, to refer to each cluster's centroid and a list representation of the centroid's coordinates (or values for ppg and atr). Let's create a dictionary then with the following mapping:

    * key: `cluster_id` of that centroid's cluster
    * value: centroid's coordinates expressed as a list ( `ppg` value first, `atr` value second )

To generate the cluster_ids, let's iterate through each centroid and assign an integer from 0 to k-1. For example, the first centroid will have a cluster_id of 0, while the second one will have a cluster_id of 1. We'll write a function, centroids_to_dict, that takes in the centroids data frame object, creates a cluster_id and converts the ppg and atr values for that centroid into a list of coordinates, and adds both the cluster_id and coordinates_list into the dictionary that's returned.


```python
def centroids_to_dict(centroids):
    dictionary = dict()
    # Iterating counter we use to generate a cluster_id.
    counter = 0

    # Iterate a pandas data frame row-wise using .iterrows().
    for index, row in centroids.iterrows():
        coordinates = [row['ppg'], row['atr']]
        dictionary[counter] = coordinates
        counter += 1

    return dictionary

centroids_dict = centroids_to_dict(centroids)
print("centroids_dict", centroids_dict)
```

    centroids_dict {0: [9.123287671232877, 2.3833333333333333], 1: [9.743243243243244, 2.1543624161073827], 2: [9.5, 2.43609022556391], 3: [12.058823529411764, 2.8674698795180724], 4: [3.8181818181818183, 3.8]}
    

###9: Euclidean Distance

Before we can assign players to clusters, we need a way to compare the ppg and atr values of the players with each cluster's centroids. Euclidean distance is the most common technique used in data science for measuring distance between vectors and works extremely well in 2 and 3 dimensions. While in higher dimensions, Euclidean distance can be misleading, in 2 dimensions Euclidean distance is essentially the Pythagorean theorem. 

The formula is $\sqrt{(q_1-p_1)^2 + (q_2-p_2)^2 + \cdots + (q_n-p_n)^2}$

q and p are the 2 vectors we are comparing. If q is [5, 2] and p is [3, 1], the distance comes out to:

$\sqrt{(5-3)^2 + (2-1)^2} = \sqrt{5} = ~2.23607$

Let's create the function calculate_distance, which takes in 2 lists (the player's values for ppg and atr and the centroid's values for ppg and atr).


```python
import math

def calculate_distance(centroid, player_values):
    root_distance = 0
    
    for x in range(0, len(centroid)):
        difference = centroid[x] - player_values[x]
        squared_difference = difference**2
        root_distance += squared_difference

    euclid_distance = math.sqrt(root_distance)
    return euclid_distance

q = [5, 2]
p = [3,1]

# Sqrt(5) = ~2.24
print("calculate_distance(q, p)", calculate_distance(q, p))
```

    calculate_distance(q, p) 2.23606797749979
    

###10: Step 1 (Assign to Cluster)

Now we need a way to assign data points to clusters based on Euclidean distance. Instead of creating a new variable or data structure to house the clusters, let's keep things simple and just add a column to the point_guards data frame that contains the cluster_id of the cluster it belongs to.

####Instructions

Create a function that can be applied to every row in the data set (using the apply function in pandas). For each player, we want to calculate the distances to each cluster's centroid using euclidean_distance. Once we know the distances, we can determine which centroid is the closest (has the lowest distance) and return that centroid's cluster_id.

Create a new column, cluster, that contains the row-wise results of assign_to_cluster.


```python
def assign_to_cluster(row):
    lowest_distance = -1
    closest_cluster = -1
    
    for cluster_id, centroid in centroids_dict.items():
        df_row = [row['ppg'], row['atr']]
        euclidean_distance = calculate_distance(centroid, df_row)
        
        if lowest_distance == -1:
            lowest_distance = euclidean_distance
            closest_cluster = cluster_id 
        elif euclidean_distance < lowest_distance:
            lowest_distance = euclidean_distance
            closest_cluster = cluster_id
    return closest_cluster

point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)
```

Let's write a function, visualize_clusters, that we can use to visualize the clusters easily.


```python
# Visualizing clusters
def visualize_clusters(df, num_clusters):
    import matplotlib.pyplot as plt
    %matplotlib inline
    
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    for n in range(num_clusters):
        clustered_df = df[df['cluster'] == n]
        plt.scatter(clustered_df['ppg'], clustered_df['atr'], c=colors[n-1])
        plt.xlabel('Points Per Game', fontsize=13)
        plt.ylabel('Assist Turnover Ratio', fontsize=13)

visualize_clusters(point_guards, 5)
```


![png](output_41_0.png)


###11: Step 2 (Recalculate Centroids)

####Instructions

Finish the function, recalculate_centroids, that takes in the point_guards data frame object, uses each cluster_id(from 0 to num_clusters - 1) to pull out all of the players in each cluster, calculates the new geometric mean, and adds the cluster_id and the new geometric mean to new_centroids_dict, the final dictionary to be returned.


```python
def recalculate_centroids(df):
    new_centroids_dict = dict()
    
    for cluster_id in range(0, num_clusters):
        values_in_cluster = df[df['cluster'] == cluster_id]
        # Calculate new centroid using mean of values in the cluster.
        new_centroid = [np.average(values_in_cluster['ppg']), np.average(values_in_cluster['atr'])]
        new_centroids_dict[cluster_id] = new_centroid
    return new_centroids_dict

centroids_dict = recalculate_centroids(point_guards)
print("centroids_dict:", centroids_dict)
```

    centroids_dict: {0: [7.8182493001231235, 2.4881301771711155], 1: [10.116394175327985, 2.1719209175677516], 2: [9.6791583006923183, 2.7589321258482964], 3: [16.406803554549132, 2.3296531690315971], 4: [3.3698798132898649, 2.073854692509141]}
    

###12: Repeat Step 1 (Assign to Cluster)

Now that we recalculated the centroids, let's re-run Step 1 (assign_to_cluster) and see how the clusters shifted.


```python
point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)
visualize_clusters(point_guards, num_clusters)
```


![png](output_48_0.png)


###15: Repeat Step 2 (Recalculate Centroids) and Step 1 (Assign to Cluster)

Now we need to recalculate the centroids, and shift the clusters again.


```python
centroids_dict = recalculate_centroids(point_guards)
point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)
visualize_clusters(point_guards, num_clusters)
```


![png](output_51_0.png)


###13: Challenges of K-Means

As you repeat Steps 1 and 2 and run visualize_clusters, you'll notice that a few of the points are changing clusters between every iteration (especially in areas where 2 clusters almost overlap), but otherwise, the clusters visually look like they don't move a lot after every iteration. This means 2 things:

- K-Means doesn't cause massive changes in the makeup of clusters between iterations, meaning that it will always converge and become stable
- Because K-Means is conservative between iterations, where we pick the initial centroids and how we assign the players to clusters initially matters a lot

To counteract these problems, the sklearn implementation of K-Means does some intelligent things like re-running the entire clustering process lots of times with random initial centroids so the final results are a little less biased on one passthrough's initial centroids.


```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(point_guards[['ppg', 'atr']])
point_guards['cluster'] = kmeans.labels_

visualize_clusters(point_guards, num_clusters)
```


![png](output_54_0.png)


###14: Conclusion

In this lesson, we explored how to segment NBA players into groups with similar traits. Our exploration helped us get a sense of the 5 types of point guards as based on each player's Assist Turnover Ratio and Points Per Game. In future lessons, we will explore how to cluster using many more features, as well as alternative ways of clustering data without using centroids.

We also got to experience the beautify of sklearn and the simplicity of using sophisticated models to get what we need accomplished quickly. In just a few lines, we ran and visualized the results of a robust K-means clustering implementation. When using K-means in the real world, use the sklearn implementation.
