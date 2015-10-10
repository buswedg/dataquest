

```python
from IPython.display import HTML

HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>''')
```




<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>



#Spark and Map-Reduce

##Transformations and Actions

###1: Introduction

####Shakespeare

In hamlet.txt we have the entire text of Shakespeare's Hamlet. Shakespeare was obviously well-known for his unique writing style and is arguably one of the most influential writers in history. Hamlet is one of his more popular works and it would be fun to perform some text analysis on it. The file is in pure text and isn't a format ready for analysis however. Before we can explore his work using text analysis methods, we will have to clean up the data and shape it into the format we want.

####Instructions

First things first, read the text file into an RDD named raw_hamlet using the textFile() method from SparkContext (this object is instantiated to sc on our end). Then, display the first 5 elements of the RDD.


```python
# Set environment variable SPARK_HOME = C:\spark-1.5.0-bin-hadoop2.6

# Configure the necessary Spark environment
import os
import sys

spark_home = os.environ.get('SPARK_HOME', None)
sys.path.insert(0, spark_home + "/python")

# Add the py4j to the path.
# You may need to change the version number to match your install
sys.path.insert(0, os.path.join(spark_home, 'python/lib/py4j-0.8.2.1-src.zip'))

# Initialize PySpark to predefine the SparkContext variable 'sc'
execfile(os.path.join(spark_home, 'python/pyspark/shell.py'))
```

    Welcome to
          ____              __
         / __/__  ___ _____/ /__
        _\ \/ _ \/ _ `/ __/  '_/
       /__ / .__/\_,_/_/ /_/\_\   version 1.5.0
          /_/
    
    Using Python version 2.7.10 (default, May 28 2015 16:44:52)
    SparkContext available as sc, HiveContext available as sqlContext.
    


```python
sc
```




    <pyspark.context.SparkContext at 0xc772cc0>




```python
raw_hamlet = sc.textFile("data/hamlet.txt")
raw_hamlet.take(5)
```




    [u'\tHAMLET', u'', u'', u'\tDRAMATIS PERSONAE', u'']



###2: Map

The text file is tab delimited and we need to split on the tab (\t) delimiter and convert this into an RDD that is more manageable.

####Instructions

Use the map method to split the data and name the resulting RDD split_hamlet.


```python
split_hamlet = raw_hamlet.map(lambda line: line.split('\t'))
split_hamlet.take(5)
```




    [[u'', u'HAMLET'], [u''], [u''], [u'', u'DRAMATIS PERSONAE'], [u'']]



###3: Beyond lambda functions

While lambda functions are great for writing quick functions to pass into PySpark methods with simple logic, they fall short when you need to write more custom logic. Thankfully, PySpark lets you define a function first in Python and pass that in. For any function that is returning a sequence of data (versus a guaranteed Boolean value, like filter() requires) in PySpark, the function needs to use a yield statement to specify the values to be pulled later.

'yield' is a technique in Python that allows "data to be generated on the fly" and pulled when necessary instead of stored to memory immediately. Because of its unique architecture, Spark takes advantage of this to reduce overhead and improve the speed of computations.

The named function is run on every element in the RDD and is restricted in scope. Each instance of the function only has access to the object(s) passed into the function and the Python libraries available in your environment. Trying to refer to variables outside the scope of the function or importing libraries can all cause the computation to crash since the function code is compiled down to Java code to run on the RDD objects (also in Java). Lastly, not all functions require the use of yield, only ones that generate a custom sequence of data. For map() or for filter(), you use return to return a value for every single element in the RDD you're running the functions on.

####flatMap()

In the following code cell, we will use the flatMap() combined with a named function hamlet_speaks to check if a line in the play contained HAMLET in all caps (indicating he spoke). flatMap() is different than map() since it doesn't require an output for every element in the RDD (a map() job does however). The flatMap() method is useful whenever you want to generate a sequence of values from an RDD.

In this case, we want an RDD object that contains tuples of the unique line id's and the text "hamlet speaketh!" but only for the elements in the RDD that have "HAMLET" in one of the values. We can't use the map() method for this because map() requires a return value for every element in the RDD.

We want each element in the resulting RDD to have the following format:

- The first value is the unique line id (e.g.'hamlet@0') , which is the first value in each of the elements in the split_hamlet RDD
- The second value is the String "hamlet speaketh!"


```python
def hamlet_speaks(line):
    id = line[0]
    speaketh = False
    
    if "HAMLET" in line:
        speaketh = True
    
    if speaketh:
        yield id,"hamlet speaketh!"

hamlet_spoken = split_hamlet.flatMap(lambda x: hamlet_speaks(x))
hamlet_spoken.take(10)
```




    [(u'', 'hamlet speaketh!'),
     (u'HAMLET', 'hamlet speaketh!'),
     (u'', 'hamlet speaketh!'),
     (u'', 'hamlet speaketh!'),
     (u'HAMLET', 'hamlet speaketh!'),
     (u'HAMLET', 'hamlet speaketh!'),
     (u'HAMLET', 'hamlet speaketh!'),
     (u'HAMLET', 'hamlet speaketh!'),
     (u'HAMLET', 'hamlet speaketh!'),
     (u'HAMLET', 'hamlet speaketh!')]



###4: Filter() using a named function

hamlet_spoken now contains only the line numbers where Hamlet spoke. While this is handy, we don't have the full line anymore. Let's instead use a filter() with a named function to extract just the original lines where Hamlet spoke. Functions passed into filter() must return a value, True or False.

####Instructions

In the next code cell, write a named function filter_hamlet_speaks to pass into filter() and apply it to split_hamlet to return just the elements (lines in the play in our case) that contain the word HAMLET. Name the resulting RDD, hamlet_spoken_lines.


```python
def filter_hamlet_speaks(line):
    return False

hamlet_spoken_lines = split_hamlet.filter(lambda line: filter_hamlet_speaks(line))
hamlet_spoken_lines.take(5)
def filter_hamlet_speaks(line):
    if "HAMLET" in line:
        return True
    else:
        return False
    
hamlet_spoken_lines = split_hamlet.filter(lambda line: filter_hamlet_speaks(line))
hamlet_spoken_lines.take(5)
```




    [[u'', u'HAMLET'],
     [u'HAMLET', u'son to the late, and nephew to the present king.'],
     [u'', u'HAMLET'],
     [u'', u'HAMLET'],
     [u'HAMLET', u'[Aside]  A little more than kin, and less than kind.']]



###5: Actions

As we've discussed before, Spark contains two kinds of methods, transformations and actions. While we've explored some of the transformations, we haven't utilized some of the other actions besides take(). Whenever you use an action method, Spark forces the evaluation of lazy code. If you only chain together transformation methods and print the resulting RDD object, you will only see the type of RDD (e.g. a PythonRDD or a PipelinedRDD object) but not any elements in the RDD since the computation hasn't happened yet.

Even though Spark makes it incredibly easy to chain lots of transformations together, it's good practice to utilize actions to observe the intermediate RDD objects between transformations so you have a better sense of if your transformations are working as expected.

####Count()

The method count() returns the number of elements in an RDD and is useful when you want to make sure the result of a transformation contains the right number of elements. For example, if you know there should be an element in the resulting RDD of a transformation for every element in the initial RDD, you can compare the counts of both RDD's and ensure that they match.

To get the number of elements in the RDD hamlet_spoken_lines, just run .count() on the RDD:

hamlet_spoken_lines.count()

####Collect()

We have used take() many times to preview the first few elements of an RDD, similar to head() in Pandas, but what if we want to return all of the elements in the collection? This is especially useful if we want to write an RDD to a CSV for example. This is also useful if we want to run some simple Python code over a collection without running it through PySpark.

Running .collect() on an RDD returns the List representation of that RDD. If you wanted to get a list of all the elements in hamlet_spoken_lines, you would write:

hamlet_spoken_lines.collect()

####Instructions

Compute the number of elements in hamlet_spoken_lines and assign to the variable named spoken_count. Grab the 101st element in hamlet_spoken_lines (List index of 100) and assign that List to spoken_101.


```python
spoken_count = 0
spoken_101 = list()
spoken_count = hamlet_spoken_lines.count()
spoken_collect = hamlet_spoken_lines.collect()
spoken_101 = spoken_collect[100]

print(spoken_101)
```

    [u'HAMLET', u'A goodly one; in which there are many confines,']
    
