

```python
from __future__ import print_function
```

#Machine Learning in Python

##Multiclass Classification

###1: Introduction to the Auto Dataset

The dataset we will be working with contains information regarding various cars. For each car we have information about the technical aspects of the vehicle such as the motor's displacement, the weight of the car, the miles per gallon, and how fast the car accelerates. Using this information we will predict the origin of the vehicle, either North America, Europe, or Asia. We can see, that unlike our previous classification datasets, we have three categories to choose from, making our task slightly more challenging.

In this particular dataset the columns are not contained within the file so we will need to explicitly name them. Fortunately pandas allows us to specify the column names while reading in the data. Also, the file is not in csv format as we've seen previously, instead each column in seperated by an unknown number of whitespaces. The file looks like:

    18.0   8   307.0      130.0      3504.      12.0   70  1    "chevrolet chevelle malibu"
    15.0   8   350.0      165.0      3693.      11.5   70  1    "buick skylark 320"
    18.0   8   318.0      150.0      3436.      11.0   70  1    "plymouth satellite"

Since it is not in csv format we use the more generic function read_table() with parameter delim_whitespaces=True to read the text file into a dataframe.

The columns of this table are:

- mpg -- Miles per gallon, Continuous.
- cylinders -- Number of cylinders in the motor, Integer, Ordinal, and Categorical.
- displacement -- Size of the motor, Continuous.
- horsepower -- Horsepower produced, Continuous.
- weight -- Weights of the car, Continuous.
- acceleration -- Acceleration, Continuous.
- year -- Year the car was built, Integer and Categorical.
- origin -- 1=North America, 2=Europe, 3=Asia. Integer and Categorical
- car_name -- Name of the Car, will not be needed in this analysis.


```python
import pandas
import numpy as np

auto_file = "data/auto.txt"

# Column names, not included in file.
names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 
         'year', 'origin', 'car_name']

# Delimited by an arbitrary number of whitespaces.
auto = pandas.read_table(auto_file, delim_whitespace=True, names=names)
auto.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mpg</th>
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>year</th>
      <th>origin</th>
      <th>car_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18</td>
      <td>8</td>
      <td>307</td>
      <td>130.0</td>
      <td>3504</td>
      <td>12.0</td>
      <td>70</td>
      <td>1</td>
      <td>chevrolet chevelle malibu</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15</td>
      <td>8</td>
      <td>350</td>
      <td>165.0</td>
      <td>3693</td>
      <td>11.5</td>
      <td>70</td>
      <td>1</td>
      <td>buick skylark 320</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18</td>
      <td>8</td>
      <td>318</td>
      <td>150.0</td>
      <td>3436</td>
      <td>11.0</td>
      <td>70</td>
      <td>1</td>
      <td>plymouth satellite</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16</td>
      <td>8</td>
      <td>304</td>
      <td>150.0</td>
      <td>3433</td>
      <td>12.0</td>
      <td>70</td>
      <td>1</td>
      <td>amc rebel sst</td>
    </tr>
    <tr>
      <th>4</th>
      <td>17</td>
      <td>8</td>
      <td>302</td>
      <td>140.0</td>
      <td>3449</td>
      <td>10.5</td>
      <td>70</td>
      <td>1</td>
      <td>ford torino</td>
    </tr>
  </tbody>
</table>
</div>



####Instructions

The .unique() function provided for pandas dataframes returns an array of the unique elements in a column. Use this function to assign the unique elements in the column origin to unique_regions.


```python
unique_regions = auto["origin"].unique()
print("unique_regions:", unique_regions)
```

    unique_regions: [1 3 2]
    

###2: Clean Dataset

The dataset auto has both an unneeded column and missing values. The column car_name does not provide any information that can help us with our analysis so we want to delete that one. Also, the column horsepower has a few missing values, marked with a '?', so we will omit those vehicles.

####Instructions

Select only those rows without a '?' in column horsepower and assign it back to auto.


```python
# Delete the column 'car_name'.
del auto["car_name"]

# Remove rows with missing data.
auto = auto[auto["horsepower"] != '?']
```

###3: Categorical Variables

Until now all the variables we have worked with have been continuous. Categorical variables are another type of variable which take on values that are names or labels. The color of a ball (e.g., red, green, blue) or the breed of a dog (e.g., collie, shepherd, terrier) are examples of categorical variables.

Imagine we want to predict the size of the ball using the color of the ball. We know the true diameter of each ball; all green balls are 3 inches in diameter, all red balls are 5 inches in diameter, and all blue balls are 10 inches in diameter. Using the same method as with continuous variables, a linear model may look something like $size = \beta_{color} * color + intercept$. Right away we see a problem, how do we input color to this model? We cannot simply say that red=1, green=2, and blue=3. This would mean that no matter what our data says a green ball is twice the diameter of a red ball. Instead we can write the equation differently, $diameter = \beta_{red} * red + \beta_{green} * green + intercept$ where red and green are binary variables and each $\beta$ is a coefficient. For each color ball we have the following cases:

- Red ball -- red=1, green=0, and blue=0. $diameter=\beta_{red} + intercept$
- Green ball -- red=0, green=1, and blue=0. $diameter=\beta_{green} + intercept$
- Blue ball -- red=0, green=0, and blue=1. $diameter=intercept$

We notice that our model does not explicity contain a blue variable. A blue variable is not needed since we know that if the ball is not red or green then it must be blue. By incorporating the intercept term the model picks this up implicitly. Here we don't make any assumption on which color is greater than the other, but instead we add a coefficient for each. The size of a green ball can be thought of as how much larger or smaller it is than a blue ball, and similar for a red ball. When modeling with these variables we would replace the variable color with two variables, red and green. These are called dummy variables and are used often in practice.

###4: Using Dummy Variables

In our case, categorical variables exist in three columns, cylinders, year, and origin. Columns cylinders and year must be modified accordingly to predict label origin. These columns take specific values or labels, similar to the ball example above, which cannot be directly used within the model. Though the column year is a number, each year could have vastly different manufacturing numbers. Since we don't have this information it is always safer to treat discrete value as categorical variables. We must use dummy variables for these. For more than two categories we create more columns to represent the categories. For example, there are 5 different categories of cylinders, 3, 4, 5, 6, 8. This single categorical column can also be represented by 4 binary columns.

- cylinders_3 -- Does the car have 3 cylinders? either a 0 or a 1
- cylinders_4 -- Does the car have 4 cylinders? either a 0 or a 1
- cylinders_5 -- Does the car have 5 cylinders? either a 0 or a 1
- cylinders_6 -- Does the car have 6 cylinders? either a 0 or a 1

Now, if each of these columns are 0 then the car does not have 3, 4, 5, or 6 cylinders so we can conclude the car has 8 cylinders. Since we can make this conclusion there is no need to have another column explaining the cars with 8 cylinders.

####Instructions

The year of the car is also considered a categorical variable. Use the function create_dummies() to get the dummy variables for year. Assign this value to year_dummies.

Merge year_dummies with auto_modified.

Delete the column year from auto_modified.


```python
import pandas

# Input a column with categorical variables.
def create_dummies(var):
    # Get the unique values in var and sort.
    var_unique = var.unique()
    var_unique.sort()
    
    # Initialize a dummy DataFrame to store variables.
    dummy = pandas.DataFrame()
    
    # Loop through all but the last value.
    for val in var_unique[:-1]:
        # Which columns are equal to our unique value.
        d = var == val
        
        # Make a new column with a dummy variable.
        dummy[var.name + "_" + str(val)] = d.astype(int)
    
    # Return dataframe with our dummy variables.
    return dummy

# Make a copy of our auto dataframe to modify with dummy variables.
modified_auto = auto.copy()

# Make dummy varibles from the cylinder categories.
cylinder_dummies = create_dummies(modified_auto["cylinders"])

# Merge dummy varibles to our dataframe.
modified_auto = pandas.concat([modified_auto, cylinder_dummies], axis=1)

# Delete cylinders column as we have now explained it with dummy variables.
del modified_auto["cylinders"]

# Make dummy varibles from the cylinder categories.
year_dummies = create_dummies(modified_auto["year"])

# Merge dummy varibles to our dataframe.
modified_auto = pandas.concat([modified_auto, year_dummies], axis=1)

# Delete cylinders column as we have now explained it with dummy variables.
del modified_auto["year"]

modified_auto.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mpg</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>origin</th>
      <th>cylinders_3</th>
      <th>cylinders_4</th>
      <th>cylinders_5</th>
      <th>cylinders_6</th>
      <th>...</th>
      <th>year_72</th>
      <th>year_73</th>
      <th>year_74</th>
      <th>year_75</th>
      <th>year_76</th>
      <th>year_77</th>
      <th>year_78</th>
      <th>year_79</th>
      <th>year_80</th>
      <th>year_81</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18</td>
      <td>307</td>
      <td>130.0</td>
      <td>3504</td>
      <td>12.0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15</td>
      <td>350</td>
      <td>165.0</td>
      <td>3693</td>
      <td>11.5</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18</td>
      <td>318</td>
      <td>150.0</td>
      <td>3436</td>
      <td>11.0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16</td>
      <td>304</td>
      <td>150.0</td>
      <td>3433</td>
      <td>12.0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>17</td>
      <td>302</td>
      <td>140.0</td>
      <td>3449</td>
      <td>10.5</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>



###5: Multiclass Classification

Multiclass classification is used when predicting 3 or more categories. Fortunately there are techniques to apply binary classification algorithms to these multiclass cases. The first which we will introduce is the one-versus-all technique. The one-versus-all method is a technique where we choose a single category as our true observation and the rest of the categories as false observations, splitting the problem into multiple binary classification problems. The model will then output a probability of whether the observation falls into the chosen class and continued for each other class. At the end, an observation is assigned to the class with the largest probability.

To start we split our data into a training and test set.

####Instructions

Split the data in modified_auto into two variables, train and test. Assign the first 70% of the shuffled_rows to train. Assign the last 30% of the shuffled_rows to test.


```python
import numpy as np

# Get all columns which will be used as features, remove 'origin'.
features = np.delete(modified_auto.columns, modified_auto.columns == 'origin')

# Shuffle data.
shuffled_rows = np.random.permutation(modified_auto.index)

# Select 70% of the dataset to be training data.
highest_train_row = int(modified_auto.shape[0] * .70)

# Select 70% of the dataset to be training data.
train = modified_auto.loc[shuffled_rows[:highest_train_row], :]

# Select 30% of the dataset to be test data.
test = modified_auto.loc[shuffled_rows[highest_train_row:], :]
```

    C:\Anaconda3\lib\site-packages\numpy\lib\function_base.py:3569: FutureWarning: in the future insert will treat boolean arrays and array-likes as boolean index instead of casting it to integer
      "as boolean index instead of casting it to integer", FutureWarning)
    

###6: Training a Multiclass Logistic Regression

To predict a car's origin, we will train a model where all observations built in North America as true and those built in Europe and Asia as false. Next, another model will be trained with all observations built in Europe are labeled true and those in North America and Asia are labeled false. Lastly, a thrid model will be trained with all observations built in Asia are labeled true and those built in North America and Europe are labeled false.

After training, each of the three models will return a probability between 0 and 1. We then classify the car by choosing the model with the largest probability. To do this, we will train 3 logistic regression models, 1 for each origin.

For each origin we train our data using LogisticRegression provided by sklearn. Each model is then stored in a dictionary.

####Instructions

Look over the code provided to understand how one-versus-all is trained.

For each origin, model, assign the probability of classification to columns in testing_probs. Each column in testing_probs is a unique origin. Ie. testing_probs[1] = probability returned from model 1.


```python
from sklearn.linear_model import LogisticRegression

# Find the unique origins.
unique_origins = modified_auto["origin"].unique()
unique_origins.sort()

# Dictionary to store models.
models = {}

for origin in unique_origins:
    # Initialize model to dictionary.
    models[origin] = LogisticRegression()
    
    # Select columns for predictors and predictands.
    X_train = train[features]
    y_train = train["origin"] == origin
        
    # Fit model with training data.
    models[origin].fit(X_train, y_train)

# Dataframe to collect testing probabilities.
testing_probs = pandas.DataFrame(columns=unique_origins)
for origin in unique_origins:
    
    # Select testing features.
    X_test = test[features]   
    
    # Compute probability of observation being in the origin.
    testing_probs[origin] = models[origin].predict_proba(X_test)[:,1]
```

###7: Choose the Origin

Now that we trained the models and computed the probabilities in each origin we can classify each observation. To classify each observation we want to take the origin with the highest probability of classification.

While each column in our dataframe testing_probs represents an origin we just need to choose the one with the largest probability. Pandas dataframes have a method .idxmax() which computes the column or index where the maximum value occurs. By using the paramater axis=1 we can tell method to find the maximum value across columns. Since each column maps directly to an origin the resulting series will be the classification from our model.

####Instructions

Classify each observation in the test set using the testing_probs dataframe. Assign the predicted origin to predicted_origins.


```python
# Variable testing_probs is in memory.
predicted_origins = testing_probs.idxmax(axis=1)
```

###8: Confusion Matrix

Similar to binary classification, we must use measures other than accuracy to evaluate our classifier. For example, in our dataset, 62.5% of cars origin is North America (origin=1). This means that if we simply predicted North America each and every time our accuracy would be 62.5%. Instead it would be great to compute measures like precision and recall to understand the efficiency of this model. To do this, we must start by creating a confusion matrix which aggregates our predictions into a matrix. Each column and row in the matrix will represent observations and predictions for the 3 origins. The values within the matrix will represent the number times an origin was predicted and another was observed. For example, we will count the number of predictions of origin 1 where we observed origin 2. This will be done for all 9 possible pairs of (prediction, observation).

The confusion matrix for our problem:

    Prediction 	Observation
                Origin 1                    Origin 2                    Origin 3
    Origin 1 	Predicted 1 & Observed 1 	Predicted 1 & Observed 2 	Predicted 1 & Observed 3
    Origin 2 	Predicted 2 & Observed 1 	Predicted 2 & Observed 2 	Predicted 2 & Observed 3
    Origin 3 	Predicted 3 & Observed 1 	Predicted 3 & Observed 2 	Predicted 3 & Observed 3

We'd like to fill in this matrix using our predictions and observations in the test set. To compute cell (1,1), count the number of times we predicted origin 1 and observed origin 1. For cell (1,2), count the number of times we predicted origin 1 and observed origin 2. And so on.

####Instructions

Using test['origin'] and predicted_origins, fill in the confusion dataframe.


```python
# Remove pandas indicies.
predicted_origins = predicted_origins.values
origins_observed = test['origin'].values

# fill in this confusion matrix.
confusion = pandas.DataFrame(np.zeros(shape=(unique_origins.shape[0], unique_origins.shape[0])), 
                             index=unique_origins, columns=unique_origins)

# Each unique prediction.
for pred in unique_origins:
    # Each unique observation.
    for obs in unique_origins:
        # Check if pred was predicted.
        t_pred = predicted_origins == pred
        # Check if obs was observed.
        t_obs = origins_observed == obs
        # True if both pred and obs.
        t = (t_pred & t_obs)
        # Count of the number of observations with pred and obs.
        confusion.loc[pred, obs] = sum(t)
```

###9: Confusion Matrix Cont.

To use the confusion matrix to compute measures like precision, recall, average accuracy, and others we need to find the true positive, false positive, true negative, and false negative counts. To do this, we can view the confusion matrix in a slightly different way by analyzing it one class at a time, just as we did during training using one-versus-all. For example, we can compute the true positive, false positive, true negative, and false negative counts for the first class, then the second, and lastly the third class. The counts for the first class will look like the following.

    Prediction 	    Observation
                    Origin 1 	    Origin 2 or 3
    Origin 1 	    True Positive 	False Positive
    Origin 2 or 3 	False Negative 	True Negative

####Instructions

Use the confusion DataFrame and assign the number of false positives for origin 2 to fp1.


```python
# Variable confusion is in memory.
# false positives = observed 1 and predicted 2 or 3
fp1 = confusion.ix[2,[1,3]].sum()
```

###10: Average Accuracy

Now that we understand the confusion matrix for multiclass classification problems, lets learn ways to measure performance. One of the simpliest and most effective measures is average accuracy.

$\text{Average Accuracy} = \dfrac{1}{l} \sum_{i=1}^l \dfrac{\text{true positive} + \text{true negative}}{n}$ where $l$ is the number of classes and $n$ is the number of observations.

In our problem in predicting the origin of a car we have unbalanced classes. The classes are unbalanced since a large proportion of cars are from a single origin. 62.5% of cars of from North America while just 37.5% are from Asia and Europe combined. This measure will take the unbalanced classes into account by averaging the accuracies over each class. The average accuracy measure will be a value between 0 and 1. The closer to 1 our average accuracy the better the classifier.

####Instructions

Compute the average accuracy of our model using the confusion DataFrame. Assign this value to avgacc.


```python
# The confusion DataFrame is in memory.
# The total number of observations in the test set.
n = test.shape[0]

# Variable to store true predictions.
sumacc = 0

# Loop over each origin.
for i in confusion.index:
    # True Positives.
    tp = confusion.loc[i, i]
    # True negatives.
    tn = confusion.loc[unique_origins[unique_origins != i], unique_origins[unique_origins != i]]
    # Add the sums.
    sumacc += tp.sum() + tn.sum().sum()

# Compute average accuracy.
avgacc = sumacc/(n*unique_origins.shape[0])
print("avgacc:", avgacc)
```

    avgacc: 0.949152542373
    

###11: Precision and Recall

Similar to binary classification, we can compute both precision and recall.

Precision measures the number of correctly predicting origins relative to the total number of positive predictions. For our dataset this measure will give us an idea of how many origins were predicted correctly while accounting for falsely predicted cars in that origin. The equation states, $\text{precision} = \dfrac{1}{l}\sum_{i=1}^l \frac{tp_i}{tp_i+fp_i}$ where $l$ is the number of classes, $tp_i$ is the true positive count for class $i$ and $tn_i$ is the false positive count for class $i$. This is taking the average of precisions over each class. The precision is in range 0 to 1 where 1 is the best. A precision of 1 states that there were no falsely predicted observations.

Recall measures the ability to predict the correct class relative to the total number of observations within that class. If many observations for that class are predicted as false then the classifier is not effective at predicting that class. In our example, if half of the cars in origin 1 are predicted to be in origins 2 and 3 then the classifier would not be considered very effective. The equation generalizes this over each class by averaging, $\text{recall} = \dfrac{1}{l}\sum_{i=1}^l \frac{tp_i}{tp_i+fn_i}$ where $fn_i$ is the number of false negative predictions of origin i. As with precision, a higher recall indicates a better performing classifier.

####Instructions

Assign the recall of our classifier to recall. Use the confusion DataFrame.


```python
# Variable to add all precisions.
ps = 0
# Loop through each origin (class).
for j in confusion.index:
    # True positives.
    tps = confusion.ix[j,j]
    # Positively predicted for that origin.
    positives = confusion.ix[j,:].sum()
    # Add to precision.
    ps += tps/positives

# Divide ps by the number of classes to get precision.
precision = ps/confusion.shape[0]
print("precision:", precision)

# Variable to add all recalls.
rcs = 0
for j in confusion.index:
    # Current number of true positives.
    tps = confusion.ix[j,j]
    # True positives and false negatives.
    origin_count = confusion.ix[:,j].sum()
    # Add recall.
    rcs += tps/origin_count

# Compute recall.
recall = rcs/confusion.shape[0]
print("recall:", recall)
```

    precision: 0.930372807018
    recall: 0.842105263158
    

###12: F-Score

A measure called the F-score is used to simplify analysis and allow for comparision against different classifiers. The F-score is a weighted measure of precision and recall defined as $F_i = \dfrac{2*precision_i*recall_i}{precision_i + recall_i}$ for class $i$. For the multiclass case, an F score is computed per class then averaged over each, $F = \dfrac{1}{l} \sum_{i=1}^l F_i$. This measure is used to find a balance between precision and recall while allowing for comparision against other models. The F-score falls in the range 0 to 1 with 1 being 'perfect'.

####Instructions

Compute the F-score for our car origin classifier using the test set. Assign the F-score to variable fscore.


```python
# Variable to add all precisions.
scores = []

# Loop through each origin (class).
for j in confusion.index:
    # True positives.
    tps = confusion.ix[j,j]
    # Positively predicted for that origin.
    positives = confusion.ix[j,:].sum()
    # True positives and false negatives.
    origin_count = confusion.ix[:,j].sum()
    # Compute precision.
    precision = tps / positives
    # Compute recall.
    recall = tps / origin_count
    # Append F_i score.
    fi = 2*precision*recall / (precision + recall)
    scores.append(fi)
shape = modified_auto.shape

# Average over all scores.
fscore = np.mean(scores)
print("fscore:", fscore)
```

    fscore: 0.859294127558
    

###13: Metrics with Sklearn

Since we now understand how to compute precision, recall, and F-scores, we can use builtin sklearn functions to compute them. sklearn.metrics has many scoring metrics for all different kinds of classifiers. Here we can use precision_score, recall_score, and f1_score. Each of these metrics need two inputs, the true class and the predicted class. There are many other options which we recommend you to read through at http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html. Most importantly we must pay attention to the option average. average is a parameter which tells the function how to compute the score. The options are binary -- Only report results for the class specified by pos_label. This is applicable only if targets (y_{true,pred}) are binary. micro -- Calculate metrics globally by counting the total true positives, false negatives and false positives. macro -- Calculate metrics for each label, and find their unweighted mean. This does not take label imbalance into account. weighted -- Calculate metrics for each label, and find their average, weighted by support (the number of true instances for each label). This alters ‘macro’ to account for label imbalance; it can result in an F-score that is not between precision and recall. * samples -- Calculate metrics for each instance, and find their average (only meaningful for multilabel classification where this differs from accuracy_score).

####Instructions

Use the parameter average=weighted and the test set to compute the precision, recall, and F-score of our classifier with the sklearn.metrics functions. Assign these values to pr_weighted, rc_weighted, and f_weighted, respectively.


```python
# Import metric functions from sklearn.
from sklearn.metrics import precision_score, recall_score, f1_score

# Compute precision score with micro averaging.
pr_micro = precision_score(test["origin"], predicted_origins, average='micro')
pr_weighted = precision_score(test["origin"], predicted_origins, average='weighted')
rc_weighted = recall_score(test["origin"], predicted_origins, average='weighted')
f_weighted = f1_score(test["origin"], predicted_origins, average='weighted')
```

###14: Conclusion

Here we have introduced multiclass classification using the one-versus-all technique with logistic regression. Another popular technique is one-versus-one which requires a model for each possible pair of categories. This technique uses a voting scheme where the class with the largest number of votes is predicted. In our example with 3 classes we would train 3 models, Origin 1 versus Origin 2, Origin 2 versus Origin 3 and Origin 1 versus Origin 3. At test time, an observation would be classifed by choosing the origin with the most "votes". The one-versus-one technique is less frequently used because the number of models grows quadratically with the number of classes. A classifier with 10 classes takes a total of 45 models!
