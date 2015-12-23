

```python
from __future__ import print_function
```

#SQL and Databases

##Introduction to SQL

###1: Databases

While CSV files are easy to interface with, they have a lot of limitations. As the data gets larger, it becomes more difficult to load the file into a computer's memory, which is how tools like Pandas work with data. CSV files also fall short at providing strict security for production applications (imagine if companies like Google or Facebook used CSV files to store and access data) and are optimized for static representation. If your data changes quickly, which is true for most technology companies, then you'll need to adopt a different method.

A database is a data store designed for storing, querying, and processing data. Databases store the data we want and expose an interface for interacting with that data. Most technology companies use databases to structure the data coming into the system and later query specific subsets of the data to answer questions or update existing data. Database systems also come with database management software with administrative controls, security and access controls, and a language to interface with the database.

In this course, we'll be focusing on a language called SQL, or Structured Query Language, which was designed to query, update, and modify data stored in a database.

###2: SQL

SQL is the most common language used to work with databases and is an important tool in any data professional's toolkit. While SQL is a language, it's quite different from languages like Python or R. SQL was built specifically for querying and interacting with databases and won't have much of the functionality you can expect in traditional programming languages. Since SQL is a <a href = "https://en.wikipedia.org/wiki/Declarative_programming">declarative language</a>, the user focuses on expressing what he or she wants and the computer focuses on figuring out how to perform the computation.

Before diving into SQL syntax, we'll introduce a few database concepts so you're aware of how the data is represented in a database and why SQL makes it easy to work with that data.

###3: Tables, rows, & columns

A database is a collection of tables, where each table is made up of rows of data and each row has values for the same set of columns across the table. A table is very similar to a DataFrame in Pandas or how a regular CSV file is structured. Both have rows of values with a consistent set of columns.

####College majors and job outcomes data 

Since we'll be using the data from the American Community Survey on college majors and job outcomes, let's see how a snapshot of the data from recent-grads.csv would be represented as a table in a database: 


```python
import pandas as pd

data = pd.read_csv("data/recent-grads.csv")
data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Major_code</th>
      <th>Major</th>
      <th>Major_category</th>
      <th>Total</th>
      <th>Sample_size</th>
      <th>Men</th>
      <th>Women</th>
      <th>ShareWomen</th>
      <th>Employed</th>
      <th>...</th>
      <th>Part_time</th>
      <th>Full_time_year_round</th>
      <th>Unemployed</th>
      <th>Unemployment_rate</th>
      <th>Median</th>
      <th>P25th</th>
      <th>P75th</th>
      <th>College_jobs</th>
      <th>Non_college_jobs</th>
      <th>Low_wage_jobs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2419</td>
      <td>PETROLEUM ENGINEERING</td>
      <td>Engineering</td>
      <td>2339</td>
      <td>36</td>
      <td>2057</td>
      <td>282</td>
      <td>0.120564</td>
      <td>1976</td>
      <td>...</td>
      <td>270</td>
      <td>1207</td>
      <td>37</td>
      <td>0.018381</td>
      <td>110000</td>
      <td>95000</td>
      <td>125000</td>
      <td>1534</td>
      <td>364</td>
      <td>193</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2416</td>
      <td>MINING AND MINERAL ENGINEERING</td>
      <td>Engineering</td>
      <td>756</td>
      <td>7</td>
      <td>679</td>
      <td>77</td>
      <td>0.101852</td>
      <td>640</td>
      <td>...</td>
      <td>170</td>
      <td>388</td>
      <td>85</td>
      <td>0.117241</td>
      <td>75000</td>
      <td>55000</td>
      <td>90000</td>
      <td>350</td>
      <td>257</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2415</td>
      <td>METALLURGICAL ENGINEERING</td>
      <td>Engineering</td>
      <td>856</td>
      <td>3</td>
      <td>725</td>
      <td>131</td>
      <td>0.153037</td>
      <td>648</td>
      <td>...</td>
      <td>133</td>
      <td>340</td>
      <td>16</td>
      <td>0.024096</td>
      <td>73000</td>
      <td>50000</td>
      <td>105000</td>
      <td>456</td>
      <td>176</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2417</td>
      <td>NAVAL ARCHITECTURE AND MARINE ENGINEERING</td>
      <td>Engineering</td>
      <td>1258</td>
      <td>16</td>
      <td>1123</td>
      <td>135</td>
      <td>0.107313</td>
      <td>758</td>
      <td>...</td>
      <td>150</td>
      <td>692</td>
      <td>40</td>
      <td>0.050125</td>
      <td>70000</td>
      <td>43000</td>
      <td>80000</td>
      <td>529</td>
      <td>102</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>2405</td>
      <td>CHEMICAL ENGINEERING</td>
      <td>Engineering</td>
      <td>32260</td>
      <td>289</td>
      <td>21239</td>
      <td>11021</td>
      <td>0.341631</td>
      <td>25694</td>
      <td>...</td>
      <td>5180</td>
      <td>16697</td>
      <td>1672</td>
      <td>0.061098</td>
      <td>65000</td>
      <td>50000</td>
      <td>75000</td>
      <td>18314</td>
      <td>4440</td>
      <td>972</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 21 columns</p>
</div>




```python
import csv, sqlite3

conn = sqlite3.connect(":memory:")
curs = conn.cursor()
curs.execute("""
CREATE TABLE recent_grads (
Rank INTEGER PRIMARY KEY, 
Major_code INTEGER, 
Major TEXT, 
Major_category INTEGER, 
Total INTEGER, 
Sample_size INTEGER, 
Men INTEGER, 
Women INTEGER, 
ShareWomen DECIMAL, 
Employed INTEGER);
""")

with open("data/recent-grads.csv", "r") as fin:
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i["Rank"], 
              i["Major_code"],
              i["Major"],
              i["Major_category"],
              i["Total"],
              i["Sample_size"],
              i["Men"],
              i["Women"],
              i["ShareWomen"],
              i["Employed"]) for i in dr]

curs.executemany("""
INSERT INTO recent_grads (
Rank, 
Major_code, 
Major, 
Major_category, 
Total, 
Sample_size, 
Men, 
Women, 
ShareWomen, 
Employed) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
""", to_db)

conn.commit()
```

We have loaded the data in for years 2010-2012 for just recent college grads into a table in a database so we can explore how to query the data using SQL. You'll notice that the table contains the same columns for each row of data, with each row representing a major in college.

The full table has many more columns, 21 to be specific, than the ones displayed in the screenshot and they're explained in further detail on <a href = "https://github.com/fivethirtyeight/data/tree/master/college-majors">FiveThirtyEight's Github repo</a>.

Here are the descriptions of the columns in the above snapshot:

- Rank - Rank by median earnings
- Major_code - Major code
- Major - Major description
- Major_category - Category of major
- Total - Total number of people with major
- Sample_size - Sample size (unweighted) of full-time
- Men - Male graduates
- Women - Female graduates
- ShareWomen - Women as share of total
- Employed - Number employed

Let's dive into how to use SQL to query this database, which contains just this one table, to pull out just the 10 columns from the snapshot.

###4: Querying

Writing a SQL query is the primary way of interacting with a database. A SQL query is a string with a defined structure and vocabulary that we use to define what we want the database to do. The SQL language has a set of general statements that you combine with specific logic to express the intent of that query.

####Select

The first and most basic statement in SQL is a SELECT statement. To specify that we want 10 specific columns for all of the rows from a specific table, we use the SELECT keyword along with the names of the 10 columns we want the database to return. You use a SELECT statement whenever you want to return specific data from the database without editing or modifying the values in the database.

Let's explore the basic syntax for the SELECT statement.

    SELECT columnA, columnB
    FROM tableName;

The SQL syntax looks more like a spoken language like English than a programming language like Python. Let's see what an actual SQL query looks like:

    SELECT Rank,Major
    FROM recent_grads;

The database then converts this SQL to lower-level logic and returns all rows from the table recent_grads, but only with the columns Rank and Major . The table recent_grads represents the information from FiveThirtyEight's dataset as a table in a database. The ; at the end is essential since it specifies where that query ends.

###5: Python & SQLite

Python 3 has excellent built-in support for <a href = "https://docs.python.org/2/library/sqlite3.html">SQLite</a>, a lightweight database that's ideal for exploring and learning SQL. We'll dive more into how SQLite specifically works in a later lesson, but for these missions we will take care of setting up and loading the data into the database on our end.

We have set up a database containing the job outcome data in a table named recent_grads and created a Python SQLite object named connection that you can use to run SQL queries.

Use the following workflow to run SQL queries:

- Store the SQL query you'd like to run as a Python string
- Run the query against the database
- View the returned results from the database

As long as the query is a valid string and follows the SQL syntax, the query can be written on one line or multiple lines using triple quotes. Let's now excute the query we just wrote against the database and see the results.

####Instructions

After viewing the results of running first_query , try executing second_query against the database, assign the results to the variable results, and then print the values.


```python
first_query = """
SELECT Rank, Major
FROM recent_grads;
"""

second_query = """
SELECT Rank,Major
FROM recent_grads;
"""

# Swap out the first_query for second_query
# in connection.execute()
# sql_cursor = connection.execute(first_query)
# results = sql_cursor.fetchmany(5)
# print(results)

sql_cursor = conn.execute(second_query)
results = sql_cursor.fetchmany(5)
print(results)
```

    [(1, u'PETROLEUM ENGINEERING'), (2, u'MINING AND MINERAL ENGINEERING'), (3, u'METALLURGICAL ENGINEERING'), (4, u'NAVAL ARCHITECTURE AND MARINE ENGINEERING'), (5, u'CHEMICAL ENGINEERING')]
    

###6: Explanation

We first stored the query in a string object named first_query, where we specified that we want to select just the columns Rank and Major from the table recent_grads:

    first_query = "SELECT Rank,Major FROM recent_grads;"

Then we used the execute() method on the connection object to run the query:

    sql_cursor = connection.execute(first_query)

The results of the query are stored in a Python object called sql_cursor, which is a <a href = "https://pysqlite.readthedocs.org/en/latest/sqlite3.html#cursor-objects">SQLite Cursor object</a>.

The sql_cursor Cursor object contains methods like:

- fetchone()
- fetchmany()
- fetchall()

that allow us to specify how many results we want to see. The Cursor object converts the results from the database into native Python data structures, which is why each row is a tuple object and the full results are a list of tuple objects. Finally, we used the Cursor object's fetchmany() method with the parameter 5 to specify that we'd like the first 5 rows from the table:

    results = sql_cursor.fetchmany(5)

###7: Specifying column order

SQL allows us to specify the order of columns in the returned results. Try swapping the order of the columns we specified in the previous query and hit run to see the results.

####Instructions

In the SELECT statement, switch the order from Major,Rank to Rank,Major. Store the first 5 results of the executed query in the variable results.


```python
first_query = """
SELECT Rank, Major 
FROM recent_grads;
"""
results = conn.execute(first_query).fetchmany(5)
print(results)
```

    [(1, u'PETROLEUM ENGINEERING'), (2, u'MINING AND MINERAL ENGINEERING'), (3, u'METALLURGICAL ENGINEERING'), (4, u'NAVAL ARCHITECTURE AND MARINE ENGINEERING'), (5, u'CHEMICAL ENGINEERING')]
    

###8: Practice: Select

Now it's your turn! Write a SELECT query that returns the 10 columns we were interested in earlier from the table recent_grads. Each column name you want returned must be separated by a , in the SELECT statement. The 10 columns we were originally interested in are:

Rank, Major_code, Major, Major_category, Total, Sample_size, Men, Women, ShareWomen, Employed

####Instructions

Store the query as a string, pass the string into connection.execute(), and use .fetchmany() to return the first 5 rows of the results. Store the first 5 rows in a variable named ten_columns. To print the results in an easy to read format, use a for loop to iterate over the results and print each result.


```python
# Query from the previous code cell, to be modified
ten_query = """
SELECT Rank, Major_code, Major, Major_category, Total, Sample_size, Men, Women, ShareWomen, Employed
FROM recent_grads;
"""
ten_columns = conn.execute(ten_query).fetchmany(5)

for row in ten_columns:
    print(row)
```

    (1, 2419, u'PETROLEUM ENGINEERING', u'Engineering', 2339, 36, 2057, 282, 0.120564344, 1976)
    (2, 2416, u'MINING AND MINERAL ENGINEERING', u'Engineering', 756, 7, 679, 77, 0.101851852, 640)
    (3, 2415, u'METALLURGICAL ENGINEERING', u'Engineering', 856, 3, 725, 131, 0.153037383, 648)
    (4, 2417, u'NAVAL ARCHITECTURE AND MARINE ENGINEERING', u'Engineering', 1258, 16, 1123, 135, 0.107313196, 758)
    (5, 2405, u'CHEMICAL ENGINEERING', u'Engineering', 32260, 289, 21239, 11021, 0.341630502, 25694)
    

###9: Where

If we wanted to figure out which majors had more female graduates than male graduates (when ShareWomen is larger than 0.5), we'd need to first return all rows and then iterate over the list of results to filter appropriately. This is not the most efficient way to get the data we want since we're pulling out more data than we need to and then filtering in Python, instead of just returning the rows we want from the database itself.

We can use the WHERE statement in SQL to add filtering criteria to the query so that we only return the rows that meet that criteria from the database.

The WHERE statement requires 3 things:

- The column we want the database to filter on: ShareWomen
- A comparison operator to specify how we want a value in a column to be compared: >
- The comparison value we want the database to compare each value to: 0.5

In the below query, we:

- Use SELECT along with the columns: Major and ShareWomen
- Use FROM along with the same table name as before: recent_grads
- Use WHERE along with the filtering criteria: ShareWomen > 0.5


        SELECT Major,ShareWomen
        FROM recent_grads
        WHERE ShareWomen > 0.5;

Here are the comparison operators we can use:

        Less than: <
        Less than or equal to: <=
        Greater than: >
        Greater than or equal to: >=
        Equal to: =
        Not equal to: !=

The comparison value after the operator must either be text or a number depending on the field. Since ShareWomen is a number, we don't have to wrap the number 0.5 with quotes. Lastly, most database systems require that the SELECT and FROM statements come first before any WHERE or other statements.

In the following code cell, we run the query against the database, return the results (represented as list of tuples), print the first 10 elements in the list, and then print the length of the list to observe how many majors had majority female students.


```python
women_query = """
SELECT Major, ShareWomen
FROM recent_grads
WHERE ShareWomen > 0.5;
"""
women_majority = conn.execute(women_query).fetchall()

for row in women_majority[0:9]:
    print(row)
    
print(len(women_majority))
```

    (u'ACTUARIAL SCIENCE', 0.535714286)
    (u'COMPUTER SCIENCE', 0.578766338)
    (u'ENVIRONMENTAL ENGINEERING', 0.558548009)
    (u'NURSING', 0.896018988)
    (u'INDUSTRIAL PRODUCTION TECHNOLOGIES', 0.75047259)
    (u'COMPUTER AND INFORMATION SYSTEMS', 0.707718502)
    (u'INFORMATION SCIENCES', 0.526475764)
    (u'APPLIED MATHEMATICS', 0.75392736)
    (u'PHARMACOLOGY', 0.524152583)
    97
    

###10: Practice: Where

Let's now practice writing a SQL query using the WHERE statement.

####Instructions

Write a SQL query that returns all majors that have more than 10,000 people employed with that background. In the SELECT, specify that we only want the Major and Employed columns (in that order). Store the results of the query in a variable named ten_thousand_employed and print the first 10 rows.


```python
ten_thousand_query = """
SELECT Major,Employed
FROM recent_grads
WHERE Employed > 10000;
"""
ten_thousand_employed = conn.execute(ten_thousand_query).fetchall()

for row in ten_thousand_employed[0:9]:
    print(row)
```

    (u'CHEMICAL ENGINEERING', 25694)
    (u'MECHANICAL ENGINEERING', 76442)
    (u'ELECTRICAL ENGINEERING', 61928)
    (u'COMPUTER ENGINEERING', 32506)
    (u'AEROSPACE ENGINEERING', 11391)
    (u'BIOMEDICAL ENGINEERING', 10047)
    (u'INDUSTRIAL AND MANUFACTURING ENGINEERING', 15604)
    (u'GENERAL ENGINEERING', 44931)
    (u'COMPUTER SCIENCE', 102087)
    

###11: Limit

When you work with tables that have millions of rows, returning all the rows and just extracting the ones you want in Python can take a long time (and is also inefficient!). Thankfully, SQL comes with a statement called LIMIT that allows us to specify how many results we'd like the database to return.

Let's now look at how we'd return the first 10 rows using the LIMIT statement.


```python
ten_thousand_query = """
SELECT Major, Employed
FROM recent_grads
WHERE Employed > 10000 LIMIT 10;
"""
ten_thousand_employed = conn.execute(ten_thousand_query).fetchall()

for row in ten_thousand_employed:
    print(row)
```

    (u'CHEMICAL ENGINEERING', 25694)
    (u'MECHANICAL ENGINEERING', 76442)
    (u'ELECTRICAL ENGINEERING', 61928)
    (u'COMPUTER ENGINEERING', 32506)
    (u'AEROSPACE ENGINEERING', 11391)
    (u'BIOMEDICAL ENGINEERING', 10047)
    (u'INDUSTRIAL AND MANUFACTURING ENGINEERING', 15604)
    (u'GENERAL ENGINEERING', 44931)
    (u'COMPUTER SCIENCE', 102087)
    (u'MANAGEMENT INFORMATION SYSTEMS AND STATISTICS', 16413)
    

###12: SQL and Python

What if we want to find all majors that met both criteria described in the last 2 SQL queries? Specifically, how do we find all the majors where the majority of the students are women AND have more than 10,000 people employed? We can accomplish this by first pulling all women majority majors from the database (this time including the Employed column) then filtering the resulting list in Python and returning only the majors where the value for Employed exceeds 10,000.

Each tuple in the resulting list of tuples after running a query is essentially a row from the table. Each tuple is a sequence of values whose order matches the order of columns specified in the SELECT statement. If we specify:

    SELECT Major, ShareWomen, Employed
    FROM recent_grads

then the resulting rows will resemble:

    first_row = ('PETROLEUM ENGINEERING', 0.120564344, 1976)

and you use index notation to access specific values.

- first_row[0] will return the tuple's first value, 'PETROLEUM ENGINEERING', corresponding to the Major column
- first_row[1] will return the tuple's second value, 0.120564344, corresponding to the ShareWomen column
- first_row[2] will return the tuple's third value, 1976, corresponding to the Employed column.

####Instructions

Modify the SQL query we wrote earlier to return majority women majors but this time including these columns in the following order:

- Major
- ShareWomen
- Employed

Then, filter the results to just the majors where Employed exceeds 10,000 and assign to the variable combined_results.


```python
query = """
SELECT Major, ShareWomen, Employed
FROM recent_grads
WHERE ShareWomen > 0.5;
"""
women_majority = conn.execute(query).fetchall()

combined_results = []
for wm in women_majority:
    if wm[2] > 10000:
        combined_results.append(wm)
        
print(len(combined_results))
```

    58
    
