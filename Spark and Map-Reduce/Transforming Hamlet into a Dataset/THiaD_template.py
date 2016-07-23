
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Spark and Map-Reduce

# ##Transforming Hamlet Into A Dataset

# ###1: Introduction

#  In this challenge, you will be practicing the techniques you've learned to transform the Hamlet text into a dataset that's more useful for data analysis.

# ####Resources

# <a href = "http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD">PySpark RDD Documentation</a>: To learn more about the methods defined for an RDD object. 
# - <a href = "http://nbviewer.ipython.org/github/jkthompson/pyspark-pictures/blob/master/pyspark-pictures.ipynb">Visual Representation of methods, IPython Notebook</a> 
# - <a href = "http://training.databricks.com/visualapi.pdf">Visual Representation of methods, PDF</a>

# In[2]:

# Set environment variable SPARK_HOME = C:\spark-1.5.1-bin-hadoop2.6

# Configure the necessary Spark environment
import os
import sys

spark_home = os.environ.get('SPARK_HOME', None)
sys.path.insert(0, spark_home + "/python")

# Add the py4j to the path.
# You may need to change the version number to match your install
sys.path.insert(0, os.path.join(spark_home, 'python/lib/py4j-0.8.2.1-src.zip'))

# Initialize PySpark to predefine the SparkContext variable 'sc'
filename = os.path.join(spark_home, 'python/pyspark/shell.py')
#execfile(filename)
exec(compile(open(filename, "rb").read(), filename, 'exec'))


# In[3]:

sc


# ###2: Extract line numbers

# The first value in each element (or line from the play) is in the following format:
# 
#     'hamlet@0'
#     'hamlet@8',
#     'hamlet@9',
#     ...
# 
# The hamlet@ at the beginning is unnecessary information for data analysis and extracting just the integer value of each line is much more useful.

# ####Instructions

# Transform the RDD split_hamlet into hamlet_with_ids that contains the cleaned version of the id for each element (the first value). For example, we want hamlet@0 to be transformed to 0, but the rest of the values in that element to be untouched. Recall that the map() function will run on each element in the RDD, where each element is a List that can accessed using regular Python mechanics.

# In[4]:

raw_hamlet = sc.textFile("data/hamlet.txt")
split_hamlet = raw_hamlet.map(lambda line: line.split('\t'))
split_hamlet.take(5)


# In[5]:

def format_id(x):
    id = x[0].split('@')[1]
    results = list()
    results.append(id)
    if len(x) > 1:
        for y in x[1:]:
            results.append(y)
    return results

hamlet_with_ids = split_hamlet.map(lambda line: format_id(line))
#hamlet_with_ids.take(5)


# ###3: Remove blank values

# We now want to get rid of any elements that don't have any actual words and only have the id in the first value. We also want to get rid of any blank '' values in an element since they don't contain any useful information for analysis.

# ####Instructions

# Clean up the RDD and store the result as an RDD named hamlet_text_only.

# In[6]:

real_text = hamlet_with_ids.filter(lambda line: len(line) > 1)
hamlet_text_only = real_text.map(lambda line: [l for l in line if l != ''])
#hamlet_text_only.take(10)


# ###4: Remove pipe characters

# If you've been previewing the RDD after each task using take() you'll notice there are some pipe characters | in odd places that add no value to us. There are both instances of the pipe character as a standalone value in an element and as part of an otherwise useful String value.

# ####Instructions

# Remove any values in an element that contain just the | and replace any | characters that appear in text values with an empty character ''. Name the resulting RDD clean_hamlet.

# In[7]:

hamlet_text_only.take(10)

def fix_pipe(line):
    results = list()
    for l in line:
        if l == "|":
            pass
        elif "|" in l:
            fmtd = l.replace("|", "")
            results.append(fmtd)
        else:
            results.append(l)
    return results

#clean_hamlet = hamlet_text_only.map(lambda line: fix_pipe(line))

