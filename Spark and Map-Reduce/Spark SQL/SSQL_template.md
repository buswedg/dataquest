

```python
from __future__ import print_function
```

#Spark and Map-Reduce

##Spark SQL

###1: Overview

In this mission, we're going to learn about how to use Spark's SQL interface to query and interact with the data. We've been working with the U.S. 2010 Census dataset, which we'll continue to work with in this mission. Later in this mission, we'll add other datasets to demonstrate how to take advantage of SQL for working with multiple datasets.

###2: Register DataFrame as a table

Before we can write and run SQL queries, we need to tell Spark to treat the DataFrame as a SQL table. Spark internally maintains a virtual database within the SQLContext object, which contains methods for registering temporary tables. To register a DataFrame as a table for querying, call the method <a href = "https://spark.apache.org/docs/1.5.0/api/python/pyspark.sql.html#pyspark.sql.DataFrame.registerTempTable">registerTempTable() method</a> on that DataFrame object. This method requires a sole string parameter, name, that we use to indicate the desired table name for reference in our SQL queries.

####Instructions

Use the <a href = "https://spark.apache.org/docs/1.5.0/api/python/pyspark.sql.html#pyspark.sql.DataFrame.registerTempTable">registerTempTable() method</a> to register the DataFrame df as a table named census2010. Then run the SQLContext method tableNames to return the list of tables, assign that list to tables, and print the result.


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
from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("data/census_2010.json")
print(df[2])
    
df.registerTempTable('census2010')
tables = sqlCtx.tableNames()
print(tables)
```

    Column<b'males'>
    ['census2010']
    

###3: Querying

Now that the table is registered within sqlCtx, we can start writing and running SQL queries. With Spark SQL, you represent your query as a string and pass it into the the sql() method within the SQLContext object. The <a href = "http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.SQLContext.sql">sql() method</a> has a sole required parameter - the query string. Spark will return the results of the query as a DataFrame object, which means you'll have to use show() to display the results because of lazy loading.

While SQLite required that queries end with a semi-colon, Spark SQL will actually throw an error if you include it. Besides this, Spark's flavor of SQL is identical to SQLite and all the queries you've written from the <a href = "https://www.dataquest.io/section/databases-sql">SQL course</a> will work here as well.

####Instructions

Write a SQL query that returns the age column from the table census2010 and use show() method to display the first 20 results.


```python
sqlCtx.sql("SELECT age FROM census2010").show()
```

    +---+
    |age|
    +---+
    |  0|
    |  1|
    |  2|
    |  3|
    |  4|
    |  5|
    |  6|
    |  7|
    |  8|
    |  9|
    | 10|
    | 11|
    | 12|
    | 13|
    | 14|
    | 15|
    | 16|
    | 17|
    | 18|
    | 19|
    +---+
    only showing top 20 rows
    
    

###4: Filtering

If we were interested in just the males and females columns where that criteria were true, we'd need to chain additional operations to the Spark DataFrame. If we wanted to return in descending order instead of ascending order we'd need to chain another method. For simple queries, the DataFrame methods are quick and powerful but understanding the methods and how to chain them can be cumbersome for more advanced queries. SQL shines at expressing more complex logic in a more compact manner. Let's brush up on SQL by writing a query that expresses more specific criteria.

####Instructions

Write and run a SQL query that returns:
- the males and females columns (in that order)
- where age > 5 and where age < 15


```python
query = ""
query = "SELECT males,females FROM census2010 WHERE age > 5 AND age < 15"
sqlCtx.sql(query).show()
```

    +-------+-------+
    |  males|females|
    +-------+-------+
    |2093905|2007781|
    |2097080|2010281|
    |2101670|2013771|
    |2108014|2018603|
    |2114217|2023289|
    |2118390|2026352|
    |2132030|2037286|
    |2159943|2060100|
    |2195773|2089651|
    +-------+-------+
    
    

###5: Mixing functionality

Since the results of a SQL query are DataFrame objects, we can actually combine the best of DataFrames and SQL to enhance our workflow. We can write a SQL query to return a subset of the data that we want to explore rapidly, which DataFrame methods enable us to do.

####Instructions

Write a SQL query that returns a DataFrame containing the males and females columns from the census2010 table. Then use the <a href = "https://spark.apache.org/docs/1.5.0/api/python/pyspark.sql.html#pyspark.sql.DataFrame.describe">describe() method</a> to calculate summary statistics for the DataFrame and the show() method to display the results.


```python
query = ""
query = "SELECT males,females FROM census2010"
sqlCtx.sql(query).describe().show()
```

    +-------+
    |summary|
    +-------+
    |  count|
    |   mean|
    | stddev|
    |    min|
    |    max|
    +-------+
    
    

###6: Multiple tables

One of the most powerful use cases in SQL is joining tables. Spark SQL takes this a step further by enabling you to run join queries across data from multiple file types. Spark will read any of the file types and formats it supports into DataFrame objects and we can register each of these as tables within the SQLContext object to use for querying.

As we mentioned briefly in the previous mission, most data science organizations use a variety of file formats and data storage mechanisms. Spark SQL was built with the industry use cases in mind and enables data professionals to use one common query language, SQL, to interact with lots of different data sources. We'll explore joins in Spark SQL further, but first let's introduce the other datasets we'll be using:

- census_1980.json - 1980 U.S. Census data
- census_1990.json - 1990 U.S. Census data
- census_2000.json - 2000 U.S. Census data

####Instructions

Read these additional datasets into DataFrame objects and then use the registerTempTable() function to register these tables individually within SQLContext. Here are the table names we'd like:

- census_1980.json as census1980
- census_1990.json as census1990
- census_2000.json as census2000

Then use the method tableNames() to list the tables within the SQLContext object, assign to tables, and finally print tables.


```python
from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)

df = sqlCtx.read.json("data/census_2010.json")
df.registerTempTable('census2010')

df_2000 = sqlCtx.read.json("data/census_2000.json")
df_1990 = sqlCtx.read.json("data/census_1990.json")
df_1980 = sqlCtx.read.json("data/census_1980.json")

df_2000.registerTempTable('census2000')
df_1990.registerTempTable('census1990')
df_1980.registerTempTable('census1980')

tables = sqlCtx.tableNames()
print(tables)
```

    ['census1980', 'census1990', 'census2000', 'census2010']
    

###7: Joins

Now that we have a table for each dataset, we can write join queries to compare values across them. Since we're working with Census data, let's use the age column as the joining column.

####Instructions

Write a query that returns a DataFrame with the total columns for the tables census2000 and census2010. Then run the query and use the show() method to display the first 20 results.


```python
query = """
 SELECT census2010.total, census2000.total
 FROM census2010
 INNER JOIN census2000
 ON census2010.age=census2000.age
"""

sqlCtx.sql(query).show()
```

    +-------+-------+
    |  total|  total|
    +-------+-------+
    |4079669|3733034|
    |4085341|3825896|
    |4089295|3904845|
    |4092221|3970865|
    |4094802|4024943|
    |4097728|4068061|
    |4101686|4101204|
    |4107361|4125360|
    |4115441|4141510|
    |4126617|4150640|
    |4137506|4152174|
    |4144742|4145530|
    |4169316|4139512|
    |4220043|4138230|
    |4285424|4137982|
    |4347028|4133932|
    |4410804|4130632|
    |4451147|4111244|
    |4454165|4068058|
    |4432260|4011192|
    +-------+-------+
    only showing top 20 rows
    
    

The functions and operators from SQLite that we've used in the past are available for us to use in Spark SQL:

- COUNT()
- AVG()
- SUM()
- AND
- OR

####Instructions

Write a query that calculates the sums of the total column from each of these tables: census2010, census2000, and census1990. You'll need to perform two inner joins for this query (all datasets have the same values for age, which makes things convenient for joining).


```python
query = """
 SELECT sum(census2010.total), sum(census2000.total), sum(census1990.total)
 FROM census2010
 INNER JOIN census2000
 ON census2010.age=census2000.age
 INNER JOIN census1990
 ON census2010.age=census1990.age
"""

sqlCtx.sql(query).show()
```

    +------------+------------+------------+
    |         _c0|         _c1|         _c2|
    +------------+------------+------------+
    |3.12247116E8|2.84594395E8|2.54506647E8|
    +------------+------------+------------+
    
    
