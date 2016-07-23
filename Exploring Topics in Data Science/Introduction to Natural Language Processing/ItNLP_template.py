
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Exploring Topics in Data Science

# ##Introduction to Natural Language Processing

# ###1: Looking at the data

# We'll be looking at a dataset consisting of submissions to <a href = "http://news.ycombinator.com/">Hacker News</a> from 2006 to 2015. The data was taken from <a href = "https://github.com/arnauddri/hn">here</a>. Arnaud Drizard used the Hacker News API to scrape it. We've sampled 10000 rows from the data randomly, and removed all the extraneous columns. Our data only has four columns:
# 
# - submission_time -- when the story was submitted.
# - url -- the base url of the submission.
# - upvotes -- number of upvotes the submission got.
# - headline -- the headline of the submission.
# 
# We'll be using the headlines to predict the number of upvotes. The data is stored in the submissions variable.

# ###2: First steps

# We want to eventually train a machine learning algorithm to take in a headline and tell us how many upvotes it would receive. However, machine learning algorithms only understand numbers, not words. How do we translate our headlines into something an algorithm can understand?
# 
# The first step is to create something called a bag of words matrix. A bag of word matrix gives us a numerical representation of which words are in which headlines.
# 
# In order to construct a bag of words matrix, we first find the unique words across the whole set of headlines. Then, we setup a matrix where each row is a headline, and each column is one of the unique words. Then, we fill in each cell with the number of times that word occured in that headline.
# 
# This will result in a matrix where a lot of the cells have a value of zero, unless the vocabulary is mostly shared between the headlines.

# In[2]:

import pandas
from collections import Counter

headlines = [
    "PretzelBros, airbnb for people who like pretzels, raises $2 million",
    "Top 10 reasons why Go is better than whatever language you use.",
    "Why working at apple stole my soul (I still love it though)",
    "80 things I think you should do immediately if you use python.",
    "Show HN: carjack.me -- Uber meets GTA"
]

# Find all the unique words in the headlines.
unique_words = list(set(" ".join(headlines).split(" ")))
def make_matrix(headlines, vocab):
    matrix = []
    for headline in headlines:
        # Count each word in the headline, and make a dictionary.
        counter = Counter(headline)
        # Turn the dictionary into a matrix row using the vocab.
        row = [counter.get(w, 0) for w in vocab]
        matrix.append(row)
    df = pandas.DataFrame(matrix)
    df.columns = unique_words
    return df

matrix = make_matrix(headlines, unique_words)
print("matrix:\n", matrix)


# ###3: Removing punctuation

# The matrix we just made is very sparse -- that means that a lot of the values are zero. This is unavoidable to some extent, because the headlines don't have much shared vocabulary. We can take some steps to make the problem better, though. Right now Why and why, and use and use. are treated as different entities, but we know they refer to the same word.
# 
# We can help the parser recognize that these are in fact the same by lowercasing every word and removing all punctuation.

# In[3]:

import re

# Lowercase, then replace any non-letter, space, or digit character in the headlines.
new_headlines = [re.sub(r'[^\w\s\d]','',h.lower()) for h in headlines]
# Replace sequences of whitespace with a space character.
new_headlines = [re.sub("\s+", " ", h) for h in new_headlines]

unique_words = list(set(" ".join(new_headlines).split(" ")))
# We've reduced the number of columns in the matrix a bit.

matrix = make_matrix(new_headlines, unique_words)
print("matrix:\n", matrix)


# ###4: Removing stopwords

# Certain words don't help you discriminate between good and bad headlines. Words such as the, a, and also occur commonly enough in all contexts that they don't really tell us much about whether something is good or not. They are generally equally likely to appear in both good and bad headlines.
# 
# By removing these, we can reduce the size of the matrix, and make training an algorithm faster.

# In[4]:

stopwords = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 
             "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 
             'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 
             'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 
             'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', 
             "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", 
             "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 
             'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 
             'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', 
             "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', 
             "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 
             'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 
             'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 
             'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 
             'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", 
             "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']

# Do the same punctuation replacement that we did for the headlines, 
# so we're comparing the right things.
stopwords = [re.sub(r'[^\w\s\d]','',s.lower()) for s in stopwords]

unique_words = list(set(" ".join(new_headlines).split(" ")))
# Remove stopwords from the vocabulary.
unique_words = [w for w in unique_words if w not in stopwords]

# We're down to 34 columns, which is way better!
matrix = make_matrix(new_headlines, unique_words)
print("matrix:\n", matrix)


# ###5: Generating a matrix for all the headlines

# Now that we know the basics, we can make a bag of words matrix for the whole set of headlines.
# 
# We don't want to have to code everything out manually every time, so we'll use a class from scikit-learn (http://scikit-learn.org/stable/) to do it automatically. Using the vectorizers from scikit-learn to construct your bag of words matrices will make the process much easier and faster.

# In[5]:

import pandas

submissions = pandas.read_csv("data/stories.csv", header=None)
submissions = submissions.drop([0, 2, 3, 6], 1)
submissions.columns = ['submission_time', 'upvotes', 'url', 'headline']
submissions = submissions.drop(submissions.index[10000:])
submissions.head(5)


# In[6]:

from sklearn.feature_extraction.text import CountVectorizer

# Construct a bag of words matrix.
# This will lowercase everything, and ignore all punctuation by default.
# It will also remove stop words.
vectorizer = CountVectorizer(lowercase=True, stop_words="english")

matrix = vectorizer.fit_transform(headlines)
# We created our bag of words matrix with far fewer commands.
print("matrix.todense():\n", matrix.todense())

# Let's apply the same method to all the headlines in all 100000 submissions.
# We'll also add the url of the submission to the end of the headline so we can take it into account.
submissions['full_test'] = submissions["headline"] + " " + submissions["url"]
full_matrix = vectorizer.fit_transform(submissions["headline"])
print("full_matrix.shape:\n", full_matrix.shape)


# ###6: Reducing dimensionality

# We've constructed a matrix, but it now has 13631 unique words, or columns. This will take a very long time to make predictions with. We want to speed it up, so we'll need to cut down the column count somehow.
# 
# One way to do this is to pick a subset of the columns that are the most informative -- that is, the columns that differentiate between good and bad headlines the best. A good way to figure out the most informative columns is to use something called a <a href = "http://en.wikipedia.org/wiki/Chi-squared_test">chi-squared test</a>.
# 
# A chi-squared test finds the words that discriminate the most between highly upvoted posts and posts that weren't upvoted. This can be words that occur a lot in highly upvoted posts, and not at all in posts without upvotes, or words that occur a lot in posts that aren't upvoted, but don't occur in posts that are upvoted.
# 
# A chi-squared test only works on binary values, so we'll make our upvotes column binary by setting anything with more upvotes than average to 1 and anything with less upvotes than average to 0.
# 
# One downside of this is that we are using knowledge from the dataset to select features, and thus introducing some overfitting. We could get around the overfitting in the "real world" by using a subset of the data for feature selection, and using a different subset for training the algorithm. We'll make things a bit simpler for now and skip that step.

# In[7]:

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# Convert the upvotes variable to binary so it works with a chi-squared test.
col = submissions["upvotes"].copy(deep=True)
col_mean = col.mean()
col[col < col_mean] = 0
col[(col > 0) & (col > col_mean)] = 1

# Find the 1000 most informative columns
selector = SelectKBest(chi2, k=1000)
selector.fit(full_matrix, col)
top_words = selector.get_support().nonzero()

# Pick only the most informative columns in the data.
chi_matrix = full_matrix[:,top_words[0]]


# ###7: Adding meta features

# If we ignore the "meta" features of the headlines we're missing out on a lot of good information. These features are things like length, amount of punctuation, average word length, and other sentence specific features.
# 
# Adding these in can greatly increase prediction accuracy.
# 
# To add them in, we'll loop over our headlines, and apply a function to each one. Some functions will count the length of the headline in characters, and others will do more advanced things, like counting the number of digits.

# In[8]:

import numpy

# Our list of functions to apply.
transform_functions = [
    lambda x: len(x),
    lambda x: x.count(" "),
    lambda x: x.count("."),
    lambda x: x.count("!"),
    lambda x: x.count("?"),
    lambda x: len(x) / (x.count(" ") + 1),
    lambda x: x.count(" ") / (x.count(".") + 1),
    lambda x: len(re.findall("\d", x)),
    lambda x: len(re.findall("[A-Z]", x)),
]

# Apply each function and put the results into a list.
columns = []
for func in transform_functions:
    columns.append(submissions["headline"].apply(func))
    
# Convert the meta features to a numpy array.
meta = numpy.asarray(columns).T


# ###8: Adding in more features

# There are more features we can work with than just text features. We have a column called submission_time, that tells us when a story was submitted, and could add more information.
# 
# Often when doing NLP work, you'll be able to add outside features that make your predictions much better. Some machine learning algorithms can figure out how these features interact with your textual features(ie "Posting at midnight with the word 'tacos' in the headline results in a high scoring post").

# In[9]:

import numpy

columns = []

# Convert the submission dates column to datetime.
submission_dates = pandas.to_datetime(submissions["submission_time"])

# Transform functions for the datetime column.
transform_functions = [
    lambda x: x.year,
    lambda x: x.month,
    lambda x: x.day,
    lambda x: x.hour,
    lambda x: x.minute,
]

# Apply all functions to the datetime column.
for func in transform_functions:
    columns.append(submission_dates.apply(func))

# Convert the meta features to a numpy array.
non_nlp = numpy.asarray(columns).T

# Concatenate the features together.
features = numpy.hstack([non_nlp, meta, chi_matrix.todense()])


# ###9: Making predictions

# Now that we can translate words to numbers, we can make predictions using an algorithm. We'll randomly pick 7500 headlines as a training set, and then evaluate the performance of the algorithm on the test set of 2500 headlines.
# 
# Predicting the results on the same set that we train on will result in <a href = "http://en.wikipedia.org/wiki/Overfitting">overfitting</a>, where your algorithm is overly optimized to the training set -- we'll think that the error rate is good, but it could actually be much higher on new data.
# 
# For the algorithm, we'll use <a href = "http://en.wikipedia.org/wiki/Tikhonov_regularization">ridge regression</a>. As compared to ordinary linear regression, ridge regression introduces a penalty on the coefficients, which prevents them from becoming too large. This can help it work with large numbers of predictors (columns) that are correlated to each other, like we have.

# In[10]:

from sklearn.linear_model import Ridge
import numpy
import random

train_rows = 7500
# Set a seed to get the same "random" shuffle every time.
random.seed(1)

# Shuffle the indices for the matrix.
indices = list(range(features.shape[0]))
random.shuffle(indices)

# Create train and test sets.
train = features[indices[:train_rows], :]
test = features[indices[train_rows:], :]
train_upvotes = submissions["upvotes"].iloc[indices[:train_rows]]
test_upvotes = submissions["upvotes"].iloc[indices[train_rows:]]
train = numpy.nan_to_num(train)

# Run the regression and generate predictions for the test set.
reg = Ridge(alpha=.1)
reg.fit(train, train_upvotes)
predictions = reg.predict(test)


# ###10: Evaluating error

# We now have predictions, but how do we determine how good they are? One way is to calculate the error rate between the predictions on the test set and the actual upvote counts for the test set.
# 
# We'll also want a baseline to compare the error to to see if the results are good. We can do this by using a simple method to make baseline estimates for the test set, and comparing the error rate of our predictions to the error rate of the baseline estimates. One very simple baseline is to take the average number of upvotes per submission in the training set, and use that as a prediction for every submission.
# 
# We'll use <a href = "http://en.wikipedia.org/wiki/Mean_absolute_error">mean absolute error</a> as an error metric. It's very simple -- just subtract the actual value from the prediction, take the absolute value of the difference, then find the mean of all the differences.

# In[11]:

# We're going to use mean absolute error as an error metric.
# Our error is about 13.6 upvotes, which means that, on average, 
# our prediction is 13.6 upvotes away from the actual number of upvotes.
mse = sum(abs(predictions - test_upvotes)) / len(predictions)
print("mae:", mse)

# As a baseline, we'll use the average number of upvotes
# across all submissions.
# The error here is 17.2 -- our estimate is better, but not hugely so.
# There either isn't a ton of predictive value encoded in the 
# data we have, or we aren't extracting it well.
average_upvotes = sum(test_upvotes)/len(test_upvotes)

mse = sum(abs(average_upvotes - test_upvotes)) / len(predictions)
print("mae:", mse)


# ###11: Improvements

# This method worked reasonably but not stunningly well on this dataset. We found that the headlines and other columns have some predictive value.
# 
# We could improve this approach by using a different predictive algorithm, like a random forest or a neural network. We could also use ngrams, such as bigrams and trigrams, when we are generating our bag of words matrix. Trying a <a href = "http://en.wikipedia.org/wiki/Tf%E2%80%93idf">tf-idf</a> transform on the matrix could also help -- scikit-learn has a class that does this automatically.
# 
# We could also take other data into account, like the user who submitted the article, and generate features indicating things like the karma of the user, and the recent activity of the user. Other statistics on the submitted url, like the average number of upvotes submissions from that url received would also be potentially useful. Be careful when doing these to only take into account information that existed before the submission you're predicting for was made.
# 
# All of these additions will take much longer to run than what we have so far, but will reduce error.
