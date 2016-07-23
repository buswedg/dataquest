

```python
from __future__ import print_function
```

#Spark and Map-Reduce

##Transforming Hamlet Into A Dataset

###1: Introduction

 In this challenge, you will be practicing the techniques you've learned to transform the Hamlet text into a dataset that's more useful for data analysis.

####Resources

<a href = "http://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD">PySpark RDD Documentation</a>: To learn more about the methods defined for an RDD object. 
- <a href = "http://nbviewer.ipython.org/github/jkthompson/pyspark-pictures/blob/master/pyspark-pictures.ipynb">Visual Representation of methods, IPython Notebook</a> 
- <a href = "http://training.databricks.com/visualapi.pdf">Visual Representation of methods, PDF</a>


```python
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
```

    Welcome to
          ____              __
         / __/__  ___ _____/ /__
        _\ \/ _ \/ _ `/ __/  '_/
       /__ / .__/\_,_/_/ /_/\_\   version 1.5.1
          /_/
    
    Using Python version 3.4.3 (default, Oct 28 2015 15:59:18)
    SparkContext available as sc, HiveContext available as sqlContext.
    


```python
sc
```




    <pyspark.context.SparkContext at 0x5b552e8>



###2: Extract line numbers

The first value in each element (or line from the play) is in the following format:

    'hamlet@0'
    'hamlet@8',
    'hamlet@9',
    ...

The hamlet@ at the beginning is unnecessary information for data analysis and extracting just the integer value of each line is much more useful.

####Instructions

Transform the RDD split_hamlet into hamlet_with_ids that contains the cleaned version of the id for each element (the first value). For example, we want hamlet@0 to be transformed to 0, but the rest of the values in that element to be untouched. Recall that the map() function will run on each element in the RDD, where each element is a List that can accessed using regular Python mechanics.


```python
raw_hamlet = sc.textFile("data/hamlet.txt")
split_hamlet = raw_hamlet.map(lambda line: line.split('\t'))
split_hamlet.take(5)
```




    [['', 'HAMLET'], [''], [''], ['', 'DRAMATIS PERSONAE'], ['']]




```python
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
```

###3: Remove blank values

We now want to get rid of any elements that don't have any actual words and only have the id in the first value. We also want to get rid of any blank '' values in an element since they don't contain any useful information for analysis.

####Instructions

Clean up the RDD and store the result as an RDD named hamlet_text_only.


```python
real_text = hamlet_with_ids.filter(lambda line: len(line) > 1)
hamlet_text_only = real_text.map(lambda line: [l for l in line if l != ''])
#hamlet_text_only.take(10)
```

###4: Remove pipe characters

If you've been previewing the RDD after each task using take() you'll notice there are some pipe characters | in odd places that add no value to us. There are both instances of the pipe character as a standalone value in an element and as part of an otherwise useful String value.

####Instructions

Remove any values in an element that contain just the | and replace any | characters that appear in text values with an empty character ''. Name the resulting RDD clean_hamlet.


```python
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
```


    ---------------------------------------------------------------------------

    Py4JJavaError                             Traceback (most recent call last)

    <ipython-input-7-3452f3adc922> in <module>()
    ----> 1 hamlet_text_only.take(10)
          2 
          3 def fix_pipe(line):
          4     results = list()
          5     for l in line:
    

    C:\spark-1.5.1-bin-hadoop2.6/python\pyspark\rdd.py in take(self, num)
       1297 
       1298             p = range(partsScanned, min(partsScanned + numPartsToTry, totalParts))
    -> 1299             res = self.context.runJob(self, takeUpToNumLeft, p)
       1300 
       1301             items += res
    

    C:\spark-1.5.1-bin-hadoop2.6/python\pyspark\context.py in runJob(self, rdd, partitionFunc, partitions, allowLocal)
        914         # SparkContext#runJob.
        915         mappedRDD = rdd.mapPartitions(partitionFunc)
    --> 916         port = self._jvm.PythonRDD.runJob(self._jsc.sc(), mappedRDD._jrdd, partitions)
        917         return list(_load_from_socket(port, mappedRDD._jrdd_deserializer))
        918 
    

    C:\spark-1.5.1-bin-hadoop2.6\python\lib\py4j-0.8.2.1-src.zip\py4j\java_gateway.py in __call__(self, *args)
        536         answer = self.gateway_client.send_command(command)
        537         return_value = get_return_value(answer, self.gateway_client,
    --> 538                 self.target_id, self.name)
        539 
        540         for temp_arg in temp_args:
    

    C:\spark-1.5.1-bin-hadoop2.6/python\pyspark\sql\utils.py in deco(*a, **kw)
         34     def deco(*a, **kw):
         35         try:
    ---> 36             return f(*a, **kw)
         37         except py4j.protocol.Py4JJavaError as e:
         38             s = e.java_exception.toString()
    

    C:\spark-1.5.1-bin-hadoop2.6\python\lib\py4j-0.8.2.1-src.zip\py4j\protocol.py in get_return_value(answer, gateway_client, target_id, name)
        298                 raise Py4JJavaError(
        299                     'An error occurred while calling {0}{1}{2}.\n'.
    --> 300                     format(target_id, '.', name), value)
        301             else:
        302                 raise Py4JError(
    

    Py4JJavaError: An error occurred while calling z:org.apache.spark.api.python.PythonRDD.runJob.
    : org.apache.spark.SparkException: Job aborted due to stage failure: Task 0 in stage 1.0 failed 1 times, most recent failure: Lost task 0.0 in stage 1.0 (TID 1, localhost): org.apache.spark.api.python.PythonException: Traceback (most recent call last):
      File "C:\spark-1.5.1-bin-hadoop2.6\python\lib\pyspark.zip\pyspark\worker.py", line 111, in main
      File "C:\spark-1.5.1-bin-hadoop2.6\python\lib\pyspark.zip\pyspark\worker.py", line 106, in process
      File "C:\spark-1.5.1-bin-hadoop2.6\python\lib\pyspark.zip\pyspark\serializers.py", line 263, in dump_stream
        vs = list(itertools.islice(iterator, batch))
      File "C:\spark-1.5.1-bin-hadoop2.6/python\pyspark\rdd.py", line 1295, in takeUpToNumLeft
        yield next(iterator)
      File "<ipython-input-5-b387753fa57d>", line 10, in <lambda>
      File "<ipython-input-5-b387753fa57d>", line 2, in format_id
    IndexError: list index out of range
    
    	at org.apache.spark.api.python.PythonRunner$$anon$1.read(PythonRDD.scala:166)
    	at org.apache.spark.api.python.PythonRunner$$anon$1.<init>(PythonRDD.scala:207)
    	at org.apache.spark.api.python.PythonRunner.compute(PythonRDD.scala:125)
    	at org.apache.spark.api.python.PythonRDD.compute(PythonRDD.scala:70)
    	at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:297)
    	at org.apache.spark.rdd.RDD.iterator(RDD.scala:264)
    	at org.apache.spark.scheduler.ResultTask.runTask(ResultTask.scala:66)
    	at org.apache.spark.scheduler.Task.run(Task.scala:88)
    	at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:214)
    	at java.util.concurrent.ThreadPoolExecutor.runWorker(Unknown Source)
    	at java.util.concurrent.ThreadPoolExecutor$Worker.run(Unknown Source)
    	at java.lang.Thread.run(Unknown Source)
    
    Driver stacktrace:
    	at org.apache.spark.scheduler.DAGScheduler.org$apache$spark$scheduler$DAGScheduler$$failJobAndIndependentStages(DAGScheduler.scala:1283)
    	at org.apache.spark.scheduler.DAGScheduler$$anonfun$abortStage$1.apply(DAGScheduler.scala:1271)
    	at org.apache.spark.scheduler.DAGScheduler$$anonfun$abortStage$1.apply(DAGScheduler.scala:1270)
    	at scala.collection.mutable.ResizableArray$class.foreach(ResizableArray.scala:59)
    	at scala.collection.mutable.ArrayBuffer.foreach(ArrayBuffer.scala:47)
    	at org.apache.spark.scheduler.DAGScheduler.abortStage(DAGScheduler.scala:1270)
    	at org.apache.spark.scheduler.DAGScheduler$$anonfun$handleTaskSetFailed$1.apply(DAGScheduler.scala:697)
    	at org.apache.spark.scheduler.DAGScheduler$$anonfun$handleTaskSetFailed$1.apply(DAGScheduler.scala:697)
    	at scala.Option.foreach(Option.scala:236)
    	at org.apache.spark.scheduler.DAGScheduler.handleTaskSetFailed(DAGScheduler.scala:697)
    	at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.doOnReceive(DAGScheduler.scala:1496)
    	at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.onReceive(DAGScheduler.scala:1458)
    	at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.onReceive(DAGScheduler.scala:1447)
    	at org.apache.spark.util.EventLoop$$anon$1.run(EventLoop.scala:48)
    	at org.apache.spark.scheduler.DAGScheduler.runJob(DAGScheduler.scala:567)
    	at org.apache.spark.SparkContext.runJob(SparkContext.scala:1822)
    	at org.apache.spark.SparkContext.runJob(SparkContext.scala:1835)
    	at org.apache.spark.SparkContext.runJob(SparkContext.scala:1848)
    	at org.apache.spark.api.python.PythonRDD$.runJob(PythonRDD.scala:393)
    	at org.apache.spark.api.python.PythonRDD.runJob(PythonRDD.scala)
    	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    	at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
    	at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
    	at java.lang.reflect.Method.invoke(Unknown Source)
    	at py4j.reflection.MethodInvoker.invoke(MethodInvoker.java:231)
    	at py4j.reflection.ReflectionEngine.invoke(ReflectionEngine.java:379)
    	at py4j.Gateway.invoke(Gateway.java:259)
    	at py4j.commands.AbstractCommand.invokeMethod(AbstractCommand.java:133)
    	at py4j.commands.CallCommand.execute(CallCommand.java:79)
    	at py4j.GatewayConnection.run(GatewayConnection.java:207)
    	at java.lang.Thread.run(Unknown Source)
    Caused by: org.apache.spark.api.python.PythonException: Traceback (most recent call last):
      File "C:\spark-1.5.1-bin-hadoop2.6\python\lib\pyspark.zip\pyspark\worker.py", line 111, in main
      File "C:\spark-1.5.1-bin-hadoop2.6\python\lib\pyspark.zip\pyspark\worker.py", line 106, in process
      File "C:\spark-1.5.1-bin-hadoop2.6\python\lib\pyspark.zip\pyspark\serializers.py", line 263, in dump_stream
        vs = list(itertools.islice(iterator, batch))
      File "C:\spark-1.5.1-bin-hadoop2.6/python\pyspark\rdd.py", line 1295, in takeUpToNumLeft
        yield next(iterator)
      File "<ipython-input-5-b387753fa57d>", line 10, in <lambda>
      File "<ipython-input-5-b387753fa57d>", line 2, in format_id
    IndexError: list index out of range
    
    	at org.apache.spark.api.python.PythonRunner$$anon$1.read(PythonRDD.scala:166)
    	at org.apache.spark.api.python.PythonRunner$$anon$1.<init>(PythonRDD.scala:207)
    	at org.apache.spark.api.python.PythonRunner.compute(PythonRDD.scala:125)
    	at org.apache.spark.api.python.PythonRDD.compute(PythonRDD.scala:70)
    	at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:297)
    	at org.apache.spark.rdd.RDD.iterator(RDD.scala:264)
    	at org.apache.spark.scheduler.ResultTask.runTask(ResultTask.scala:66)
    	at org.apache.spark.scheduler.Task.run(Task.scala:88)
    	at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:214)
    	at java.util.concurrent.ThreadPoolExecutor.runWorker(Unknown Source)
    	at java.util.concurrent.ThreadPoolExecutor$Worker.run(Unknown Source)
    	... 1 more


