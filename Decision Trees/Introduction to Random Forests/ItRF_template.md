

```python
from __future__ import print_function
```

#Decision Trees

##Introduction to Random Forests

###1: Introduction

In this mission, we'll learn how to construct and apply random forests.

The data is from the 1994 Census, and contains information on an individual's marital status, age, type of work, and more. The target column, high_income, is if they make less than or equal to 50k a year (0), or more than 50k a year (1).


```python
import pandas

# Set index_col to False to avoid pandas thinking that the first column is row indexes (it's age).
income = pandas.read_csv("data/income.csv", header=False, index_col=False)
income.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>workclass</th>
      <th>fnlwgt</th>
      <th>education</th>
      <th>education_num</th>
      <th>marital_status</th>
      <th>occupation</th>
      <th>relationship</th>
      <th>race</th>
      <th>sex</th>
      <th>capital_gain</th>
      <th>capital_loss</th>
      <th>hours_per_week</th>
      <th>native_country</th>
      <th>high_income</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>39</td>
      <td>State-gov</td>
      <td>77516</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Never-married</td>
      <td>Adm-clerical</td>
      <td>Not-in-family</td>
      <td>White</td>
      <td>Male</td>
      <td>2174</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>1</th>
      <td>50</td>
      <td>Self-emp-not-inc</td>
      <td>83311</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>2</th>
      <td>38</td>
      <td>Private</td>
      <td>215646</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Divorced</td>
      <td>Handlers-cleaners</td>
      <td>Not-in-family</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>3</th>
      <td>53</td>
      <td>Private</td>
      <td>234721</td>
      <td>11th</td>
      <td>7</td>
      <td>Married-civ-spouse</td>
      <td>Handlers-cleaners</td>
      <td>Husband</td>
      <td>Black</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>4</th>
      <td>28</td>
      <td>Private</td>
      <td>338409</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Wife</td>
      <td>Black</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>Cuba</td>
      <td>&lt;=50K</td>
    </tr>
  </tbody>
</table>
</div>




```python
from sklearn import preprocessing

#print("income.dtypes:\n", income.dtypes)

for column in income:
    if income[column].dtypes == "object":
        income[column] = income[column].astype("category")
        income[column] = income[column].cat.codes
        
income.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>workclass</th>
      <th>fnlwgt</th>
      <th>education</th>
      <th>education_num</th>
      <th>marital_status</th>
      <th>occupation</th>
      <th>relationship</th>
      <th>race</th>
      <th>sex</th>
      <th>capital_gain</th>
      <th>capital_loss</th>
      <th>hours_per_week</th>
      <th>native_country</th>
      <th>high_income</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>39</td>
      <td>7</td>
      <td>77516</td>
      <td>9</td>
      <td>13</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>1</td>
      <td>2174</td>
      <td>0</td>
      <td>40</td>
      <td>39</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>50</td>
      <td>6</td>
      <td>83311</td>
      <td>9</td>
      <td>13</td>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>39</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>38</td>
      <td>4</td>
      <td>215646</td>
      <td>11</td>
      <td>9</td>
      <td>0</td>
      <td>6</td>
      <td>1</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>39</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>53</td>
      <td>4</td>
      <td>234721</td>
      <td>1</td>
      <td>7</td>
      <td>2</td>
      <td>6</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>39</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>28</td>
      <td>4</td>
      <td>338409</td>
      <td>9</td>
      <td>13</td>
      <td>2</td>
      <td>10</td>
      <td>5</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>5</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
import numpy
import math

# Set a random seed so the shuffle is the same every time.
numpy.random.seed(1)

# Shuffle the rows.  This first permutes the index randomly using numpy.random.permutation.
# Then, it reindexes the dataframe with this.
# The net effect is to put the rows into random order.
income = income.reindex(numpy.random.permutation(income.index))

train_max_row = math.floor(income.shape[0] * .8)
train = income.iloc[:train_max_row]
test = income.iloc[train_max_row:]
```

###2: Ensemble models

A random forest is a kind of ensemble model. <a href = "https://en.wikipedia.org/wiki/Ensemble_learning">Ensembles</a> combine the predictions of multiple models to create a more accurate final prediction. We'll make a simple ensemble to see how it works.

We'll create two decision trees with slightly different parameters, and check their accuracy separately. Later on, we'll combine their predictions and compare the accuracy.

####Instructions

Fit both clf and clf2 to the data. Use train[columns] as the predictors, and train["high_income"] as the target.

Make predictions on the test set predictors (test[columns]) using both clf and clf2.

For both sets of predictions, compute the AUC between the predictions and the actual values (test["high_income"]) using the roc_auc_score function. Print the AUC out for both.


```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score

columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=75)
clf.fit(train[columns], train["high_income"])

clf2 = DecisionTreeClassifier(random_state=1, max_depth=6)
clf2.fit(train[columns], train["high_income"])

predictions = clf.predict(test[columns])
print(roc_auc_score(predictions, test["high_income"]))

predictions = clf2.predict(test[columns])
print(roc_auc_score(predictions, test["high_income"]))
```

    0.784853009097
    0.771031199892
    

###3: Combining our predictions

When we have multiple classifiers making predictions, we can treat each set of predictions as a column in a matrix. Here's an example where we have Decision Tree 1 (DT1), Decision Tree 2 (DT2), and DT3:

    DT1     DT2    DT3
    0       1      0
    1       1      1
    0       0      1
    1       0      0

When we add more models to our ensemble, we just add more columns to the combined predictions. Ultimately, we don't want this matrix, though -- we want one prediction per row in the training data. To do this, we'll need to create rules to turn each row of our matrix of predictions into a single number.

We want to create a Final Prediction vector:

    DT1     DT2    DT3    Final Prediction
    0       1      0      0
    1       1      1      1
    0       0      1      0
    1       0      0      0

There are many ways to get from the output of multiple models to a final vector of predictions. One method is majority voting, where each classifier gets a "vote", and the most commonly voted value for each row wins. This only works if there are more than 2 classifiers (and ideally an odd number so we don't have to write a rule to break ties). Majority voting is what we applied in the example above.

Since in the last screen we only had two classifiers, we'll have to use a different method to combine predictions. We'll take the mean of all the items in a row. Right now, we're using the predict method, which returns either 0 or 1. predict returns something like this:

    0
    1
    0
    1

We can instead use the predict_proba method, which will predict a probability from 0 to 1 that a given class is the right one for a row. Since 0 and 1 are our two classes, we'll get a matrix with as many rows as the income dataframe and 2 columns. predict_proba will return something like this:

    0     1
    .7    .3
    .2    .8
    .1    .9

Each row will correspond to a prediction. The first column is the probability that the prediction is a 0, the second column is the probability that the prediction is a 1. Each row adds up to 1.

If we just take the second column, we get the average value that the classifier would predict for that row. If there's a .9 probability that the correct classification is 1, we can use the .9 as the value the classifier is predicting. This will give us a continuous output in a single vector instead of just 0 or 1.

We can then add all of the vectors we get through this method together and divide by the number of vectors to get the mean prediction by all the members of the ensemble. We can then round off to get 0 or 1 predictions.

If we use the predict_proba method on both classifiers from the last screen to generate probabilities, take the mean for each row, and then round the results, we'll get ensemble predictions.

####Instructions

Add predictions and predictions2, then divide by 2 to get the mean. Use numpy.round to round all of the resulting predictions. Print the resulting AUC score between the actual values and the predictions.


```python
predictions = clf.predict_proba(test[columns])[:,1]
predictions2 = clf2.predict_proba(test[columns])[:,1]
combined = (predictions + predictions2) / 2
rounded = numpy.round(combined)

roc_auc = roc_auc_score(rounded, test["high_income"])
print("roc_auc:", roc_auc)
```

    roc_auc: 0.789959895266
    

###4: Why ensembling works

As we can see above, the combined predictions of the two trees are more accurate than any single tree.

To intuitively understand why this makes sense, think about two people at the same talent level. One learned programming in college. The other learned on their own (let's say using Dataquest!).

If you give both of them a project, since they both have different knowledge and experience, they'll both approach it in slightly different ways. They may both produce code that achieves the same result, but one may run faster in certain areas. The other may have a better interface. Even though both of them have about the same talent level, because they approach the problem differently, their solutions are stronger in different areas.

If we combine the best parts of both of their projects, we'll end up with a stronger combined project.

Ensembling is the exact same. Both models are approaching the problem slightly differently, and building a different tree because we used different parameters for each. Each tree makes different predictions in different areas. Even though both trees have about the same accuracy, when we combine them, the result is stronger because it leverages the strengths of both approaches.

The more "diverse", or dissimilar, the models used to construct an ensemble, the stronger the combined predictions will be (assuming that all models have about the same accuracy). Ensembling a decision tree and a logistic regression model, which use very different approaches to arrive at their answers, will result in stronger predictions than ensembling two decision trees with similar parameters.

On the other side, if the models you ensemble are very similar in how they make predictions, you'll get a negligible boost from ensembling.

Ensembling models with very different accuracies will not generally improve your accuracy. Ensembling a model with a .75 AUC and a model with a .85 AUC on a test set will usually result in an AUC somewhere in between the two original values. There's a way around this which we'll discuss later on, called weighting.

###5: Bagging

A random forest is an ensemble of decision trees. If we don't make any modifications to the trees, each tree will be the exact same, so we'll get no boost when we ensemble them. In order to make ensembling effective, we have to introduce variation into each individual decision tree model.

If we introduce variation, each tree will be be constructed slightly differently, and therefore will make different predictions. This variation is why the word "random" is in "random forest".

There are two main ways to introduce variation in a random forest -- bagging and random feature subsets. We'll dive into bagging first.

In a random forest, each tree isn't trained using the whole dataset. Instead, it's trained on a random sample of the data, or a "bag". This sampling is performed with replacement. When we sample with replacement, after we select a row from the data we're sampling, we put the row back in the data so it can be picked again. Some rows from the original data may appear in the "bag" multiple times.

####Instructions

predictions is a list of vectors corresponding to predictions on the test set. Use the technique we did earlier to add all the vectors together and divide by 10 to get the mean prediction for each row. Use numpy.round to round the resulting predictions. Finally, print the AUC score between the combined predictions and test["high_income"].


```python
# We'll build 10 trees
tree_count = 10

# Each "bag" will have 60% of the number of original rows.
bag_proportion = .6

predictions = []
for i in range(tree_count):
    # We select 60% of the rows from train, sampling with replacement.
    # We set a random state to ensure we'll be able to replicate our results.
    # We set it to i instead of a fixed value so we don't get the same sample every loop.
    # That would make all of our trees the same.
    bag = train.sample(frac=bag_proportion, replace=True, random_state=i)
    
    # Fit a decision tree model to the "bag".
    clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=75)
    clf.fit(bag[columns], bag["high_income"])
    
    # Using the model, make predictions on the test data.
    predictions.append(clf.predict_proba(test[columns])[:,1])
combined = numpy.sum(predictions, axis=0) / 10
rounded = numpy.round(combined)

roc_auc = roc_auc_score(rounded, test["high_income"])
print("roc_auc:", roc_auc)
```

    roc_auc: 0.785415640465
    

###6: Selecting random features

With the bagging example above, we gained some accuracy over a single decision tree. Now, we'll go back to the decision tree algorithm we created 2 missions ago to explain random feature subsets.

We first pick a maximum number of features that we want to evaluate each time we split the tree. This has to be less than the total number of columns in the data.

Every time we split, we pick a random sample of features from the data. We then compute the information gain for each feature in our random sample, and pick the one with the highest information gain to split on.

We're repeating the same process to select the optimal split for a node, but we'll only evaluate a constrained set of features, selected randomly. This introduces variation into the trees, and makes for more powerful ensembles.

Below is an ID3 algorithm. We'll modify it to only consider a certain subset of the features.

####Instructions

Modify find_best_column to select a random sample from columns before computing information gain. Look where it says Insert code here. Each subset will have 2 items in it. You can use numpy.random.choice to do this. The first input is the list you're picking from, and the second is the number of items you want to pick.

Be careful not to overwrite columns when you do the selection -- the random sample should go in a different variable, and you'll have to modify some of the surrounding code to match.


```python
def calc_information_gain(data, split_name, target_name):
    """
    Calculate information gain given a dataset, column to split on, and target.
    """
    # Calculate original entropy.
    original_entropy = calc_entropy(data[target_name])
    
    # Find the median of the column we're splitting.
    column = data[split_name]
    median = column.median()
    
    # Make two subsets of the data based on the median.
    left_split = data[column <= median]
    right_split = data[column > median]
    
    # Loop through the splits, and calculate the subset entropy.
    to_subtract = 0
    for subset in [left_split, right_split]:
        prob = float(subset.shape[0]) / data.shape[0]
        to_subtract += prob * calc_entropy(subset[target_name])
    
    # Return information gain.
    return original_entropy - to_subtract

def calc_entropy(column):
    """
    Calculate entropy given a pandas Series, list, or numpy array.
    """
    # Compute the counts of each unique value in the column.
    counts = numpy.bincount(column)
    
    # Divide by the total column length to get a probability.
    probabilities = counts / float(len(column))
    
    # Initialize the entropy to 0.
    entropy = 0
    
    # Loop through the probabilities, and add each one to the total entropy.
    for prob in probabilities:
        if prob > 0:
            entropy += prob * math.log(prob, 2)
    
    return -entropy
```


```python
# Create the dataset that we used 2 missions ago.
data = pandas.DataFrame([
    [0,4,20,0],
    [0,4,60,2],
    [0,5,40,1],
    [1,4,25,1],
    [1,5,35,2],
    [1,5,55,1]
    ])
data.columns = ["high_income", "employment", "age", "marital_status"]

# Set a random seed to make results reproducible.
numpy.random.seed(1)

# The dictionary to store our tree.
tree = {}
nodes = []

# The function to find the column to split on.
def find_best_column(data, target_name, columns):
    information_gains = []
    
    # Insert your code here.
    
    for col in columns:
        information_gain = calc_information_gain(data, col, "high_income")
        information_gains.append(information_gain)

    # Find the name of the column with the highest gain.
    highest_gain_index = information_gains.index(max(information_gains))
    highest_gain = columns[highest_gain_index]
    return highest_gain

# The function to construct an id3 decision tree.
def id3(data, target, columns, tree):
    unique_targets = pandas.unique(data[target])
    nodes.append(len(nodes) + 1)
    tree["number"] = nodes[-1]

    if len(unique_targets) == 1:
        if 0 in unique_targets:
            tree["label"] = 0
        elif 1 in unique_targets:
            tree["label"] = 1
        return
    
    best_column = find_best_column(data, target, columns)
    column_median = data[best_column].median()
    
    tree["column"] = best_column
    tree["median"] = column_median
    
    left_split = data[data[best_column] <= column_median]
    right_split = data[data[best_column] > column_median]
    split_dict = [["left", left_split], ["right", right_split]]
    
    for name, split in split_dict:
        tree[name] = {}
        id3(split, target, columns, tree[name])

def find_best_column(data, target_name, columns):
    information_gains = []
    
    # Select two columns randomly.
    cols = numpy.random.choice(columns, 2)
    
    for col in cols:
        information_gain = calc_information_gain(data, col, "high_income")
        information_gains.append(information_gain)

    highest_gain_index = information_gains.index(max(information_gains))
    
    # Get the highest gain by indexing cols.
    highest_gain = cols[highest_gain_index]
    
    return highest_gain

id3(data, "high_income", ["employment", "age", "marital_status"], tree)
print("tree:", tree)
```

    tree: {'number': 1, 'left': {'number': 2, 'left': {'number': 3, 'left': {'number': 4, 'label': 0}, 'median': 22.5, 'column': 'age', 'right': {'number': 5, 'label': 1}}, 'median': 4.0, 'column': 'employment', 'right': {'number': 6, 'label': 1}}, 'median': 37.5, 'column': 'age', 'right': {'number': 7, 'left': {'number': 8, 'left': {'number': 9, 'label': 0}, 'median': 47.5, 'column': 'age', 'right': {'number': 10, 'label': 1}}, 'median': 55.0, 'column': 'age', 'right': {'number': 11, 'label': 0}}}
    

###7: Random subsets in scikit-learn

We can also repeat our random subset selection process in scikit-learn. We just set the splitter parameter on DecisionTreeClassifier to "random", and the max_features parameter to "auto". If we have N columns, this will pick a subset of features of size N−−√, compute the gini coefficient (similar to information gain) for each, and split the node on the best column in the subset.

This is essentially the same thing we did above, but with far less typing.

####Instructions

Add the right parameters to the DecisionTreeClassifier instantiation below. Set splitter to "random", and max_features to "auto".

Print the resulting AUC score.


```python
# We'll build 10 trees
tree_count = 10

# Each "bag" will have 70% of the number of original rows.
bag_proportion = .7

predictions = []
for i in range(tree_count):
    # We select 80% of the rows from train, sampling with replacement.
    # We set a random state to ensure we'll be able to replicate our results.
    # We set it to i instead of a fixed value so we don't get the same sample every time.
    bag = train.sample(frac=bag_proportion, replace=True, random_state=i)
    
    # Fit a decision tree model to the "bag".
    clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=75, splitter="random", max_features="auto")
    clf.fit(bag[columns], bag["high_income"])
    
    # Using the model, make predictions on the test data.
    predictions.append(clf.predict_proba(test[columns])[:,1])

combined = numpy.sum(predictions, axis=0) / 10
rounded = numpy.round(combined)

roc_auc = roc_auc_score(rounded, test["high_income"])
print("roc_auc:", roc_auc)
```

    roc_auc: 0.789767997764
    

###8: Putting it all together

As you can see, using random subsets above improved the accuracy versus just using bagging.

So far we've demonstrated the two building blocks of random forests, bagging and random feature subsets. Luckily, we don't have to write our own code to perform these each time. Scikit-learn has a <a href = "http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html">RandomForestClassifier</a> class and a <a href = "http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html">RandomForestRegressor</a> class that enable us to quickly train random forests.

When we instantiate a RandomForestClassifier, we pass in an n_estimators parameter that indicates how many trees to build. There's never any harm in building more trees, but each tree will take time to build, so more trees will take longer.

RandomForestClassifier has a similar interface to DecisionTreeClassifier, and we can use the fit and predict methods to train and make predictions.

####Instructions

Fit clf to the training data. Make predictions on the test data. Compute and print the AUC score between the test predictions and the actual values.


```python
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=10, random_state=1, min_samples_leaf=75)
clf.fit(train[columns], train["high_income"])

predictions = clf.predict(test[columns])

roc_auc = roc_auc_score(rounded, test["high_income"])
print("roc_auc:", roc_auc)
```

    roc_auc: 0.789767997764
    

###9: Parameter tweaking

Similarly to decision trees, we can tweak a few parameters with random forests:

- min_samples_leaf
- min_samples_split
- max_depth
- max_leaf_nodes

These parameters apply to the individual trees in the model, and change how they are constructed. There are also parameters specific to the random forest that alter how it's constructed as a whole:

- n_estimators
- bootstrap -- defaults to True. Bootstrap aggregation is another name for bagging, and this indicates whether to turn it on.

Check the <a href = "http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html">documentation</a> for a full list of parameters.

By tweaking parameters, we can increase the accuracy of the forest. The easiest tweak is to increase the number of estimators we use. This has diminishing returns -- going from 10 trees to 100 will make a bigger difference than going from 100 to 500, which will make a bigger difference than going from 500 to 1000. The accuracy increase function is logarithmic, so increasing the number of trees beyond a certain number (usually 200) won't help much at all.

####Instructions

Increase n_estimators to 150.


```python
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=150, random_state=1, min_samples_leaf=75)

clf.fit(train[columns], train["high_income"])

predictions = clf.predict(test[columns])

roc_auc = roc_auc_score(rounded, test["high_income"])
print("roc_auc:", roc_auc)
```

    roc_auc: 0.789767997764
    

###10: Reducing overfitting

One of the major advantages of random forests over single decision trees is they overfit less. Although each individual decision tree in a random forest varies widely, the average of their predictions is less sensitive to the input data than a single tree is. This is because while one tree can construct an incorrect and overfit model, the average of 100 or more trees will be more likely to hone in on the signal and ignore the noise. The signal will be the same across all the trees, whereas each tree will hone into the noise differently. This means that the average will discard the noise and keep the signal.

If you look below, you'll see that we've fit a single decision tree to the training set, and made predictions for both the training set and testing set. The AUC for the training set predictions is .789, and the AUC for the testing set is .784. This indicates a mild degree of overfitting.

Let's do the same with a random forest, and contrast.

####Instructions

Fit clf to the training set. Make predictions on the training set. Print the resulting AUC score.

Make predictions on the testing set. Print the resulting AUC score.


```python
clf = RandomForestClassifier(n_estimators=150, random_state=1, min_samples_leaf=75)
clf.fit(train[columns], train["high_income"])

predictions = clf.predict(train[columns])
print(roc_auc_score(predictions, train["high_income"]))

predictions = clf.predict(test[columns])
print(roc_auc_score(predictions, test["high_income"]))
```

    0.794137608735
    0.793788646293
    

###11: When to use random forests

As we can see in the above code cell, overfitting decreases significantly with a random forest, and accuracy goes up overall.

The random forest algorithm is incredibly powerful, but isn't applicable to all tasks. The main strengths of a random forest are:

- Very accurate predictions -- Random forests achieve near state of the art performance on many machine learning tasks. Along with neural networks and gradient boosted trees, they are typically one of the top performing algorithms.
- Resistance to overfitting -- due to how they're constructed, random forests are fairly resistant to overfitting. Parameters like max_depth still have to be set and tweaked, though.

The main weaknesses are:

- Hard to interpret -- because we've averaging the results of many trees, it can be hard to figure out why a random forest is making predictions the way it is.
- Longer creation time -- making two trees takes twice as long as making one, 3 takes three times as long, and so on. Luckily, we can exploit multicore processors to parallelize tree construction. Scikit allows us to do this through the n_jobs parameter on <a href = "http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html">RandomForestClassifier</a>. We'll get more into parallelization later.

Given these tradeoffs, it makes sense to use random forests in situations where accuracy is of the utmost importance, and being able to interpret or explain the decisions the model is making isn't key. In cases where time is of the essence, or interpretability is important, a single decision tree may be a better choice.
