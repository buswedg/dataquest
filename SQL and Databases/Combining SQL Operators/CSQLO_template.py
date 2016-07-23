
# coding: utf-8

# In[1]:

from __future__ import print_function


# #SQL and Databases

# ##Combining SQL operators

# In[2]:

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
Employed INTEGER, 
Full_time INTEGER, 
Part_time INTEGER, 
Full_time_year_round INTEGER, 
Unemployed INTEGER, 
Unemployment_rate DECIMAL, 
Median INTEGER, 
P25th INTEGER, 
P75th INTEGER, 
College_jobs INTEGER, 
Non_college_jobs INTEGER, 
Low_wage_jobs INTEGER
);
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
              i["Employed"],
              i["Full_time"],
              i["Part_time"],
              i["Full_time_year_round"],
              i["Unemployed"],
              i["Unemployment_rate"],
              i["Median"],
              i["P25th"],
              i["P75th"], 
              i["College_jobs"],
              i["Non_college_jobs"],
              i["Low_wage_jobs"]) for i in dr]

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
Employed,
Full_time, 
Part_time, 
Full_time_year_round, 
Unemployed, 
Unemployment_rate, 
Median, 
P25th, 
P75th, 
College_jobs, 
Non_college_jobs, 
Low_wage_jobs) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
""", to_db)

conn.commit()


# ###1: Logical Operators

# What if we want to use multiple filtering criteria to specify the data we want from the database?
# 
# Logical operators are keywords you can use to combine filtering criteria to express more specific conditions. Here are the 2 basic logical operators you will often use:
# 
# - Condition1 or Condition2: OR
# - Condition1 and Condition2: AND

# ###2: And

# The following is psuedo-code to help you conceptualize how the AND statement is used with a WHERE statement:
# 
#     SELECT [column1, column2,...] FROM [table1]
#     WHERE [condition1] AND [condition2]
# 
# Instead of first writing a SQL query to pull all majors with majority women and then using Python to filter the results, we can use the AND operator to combine the 2 filtering criteria in SQL itself. Let's see what that query would look like:
# 
#     SELECT Major,ShareWomen,Employed FROM recent_grads 
#     WHERE ShareWomen>0.5 AND Employed>10000;
# 
# We want the database to return all rows where both conditions are true:
# 
# - ShareWomen > 0.5
# - Employed > 10000
# 
# We use the Python string <a href = "https://pyformat.info/#simple">format function</a> to print how many majors met both criteria.

# In[3]:

query = """
SELECT Major, ShareWomen, Employed
FROM recent_grads
WHERE ShareWomen > 0.5 AND Employed > 10000;
"""

both_conditions = conn.execute(query).fetchall()

print(both_conditions)
print('{} majors'.format(len(both_conditions)))


# ###3: Or operator

# We used the AND operator to specify that our filter needs to pass 2 Boolean conditions, both of which had to evaluate to True for the record to be included in the result set. If we instead want to specify a filter that met either of the conditions, we would use the OR operator.
# 
#     SELECT [column1, column2,...] FROM [table1]
#     WHERE [condition1] OR [condition2]
# 
# We'll dive straight into a practice problem since the OR and AND operators are used in similar ways.

# ####Instructions

# Write a SQL query that will return the first 20 majors that either:
# 
# - had a Median salary greater than or equal to 10,000 or
# - less than or equal to 1,000 Unemployed people.
# 
# We only want to include the following columns in the results with the following order:
# 
# - Major
# - Median
# - Unemployed
# 
# Store the results of the query in a variable named either_conditions.

# In[4]:

query = """
SELECT Major, Median, Unemployed 
FROM recent_grads 
WHERE Median >= 50000 OR Unemployed <= 1000 LIMIT 20;
"""

either_conditions = conn.execute(query).fetchall()

for row in either_conditions:
    print(row)


# ###4: Grouping operators

# There is a certain class of questions that can't be answered using just the techniques we've learned so far. If we wanted to write a query that returned all Engineering majors that either had majority women or an unemployment rate below the August 2015 unemployment rate of 5.1%, we'll need to use parentheses to express this more complex logic.
# 
# The 3 raw conditions we'll need:
# 
#     Major_category = 'Engineering'
#     ShareWomen >= 0.5
#     Unemployment_rate < 0.051
# 
# How the SQL query looks like using parantheses:
# 
#     select Major, Major_category, ShareWomen, Unemployment_rate
#     from recent_grads
#     where (Major_category = 'Engineering') and (ShareWomen > 0.5 or Unemployment_rate < 0.051);
# 
# The first thing you may notice is that we didn't capitalize any of the operators or statements in the query. SQL is case-insensitive with its built-in keywords which means we don't have to capitalize operators like AND or statements like SELECT.
# 
# The second thing you may notice is how we grouped logic we wanted to be evaluated together in parentheses. This is very similar to how we group calculations in math together with a particular order. The parentheses makes it explictly clear to the database that we want all the rows where both the expressions in the statements evaluate to True:
# 
#     (Major_category = 'Engineering' and ShareWomen > 0.5) -> True or False
#     (Unemployment_rate < 0.051) -> True or False
# 
# If we had written the where statement without any parentheses, the database would guess what our intentions are and will actually execute the following query instead:
# 
#     where (Major_category = 'Engineering' and ShareWomen > 0.5) or (Unemployment_rate < 0.051) 
# 
# Leaving parentheses out implies that we want the calculation to happen from left to right in the order the logic is written and wouldn't return us the data we want. Let's now run our intended query and see the results!

# In[5]:

query = """
SELECT Major, Major_category, ShareWomen, Unemployment_rate
FROM recent_grads
WHERE (Major_category = 'Engineering') and (ShareWomen > 0.5 or Unemployment_rate < 0.051);
"""

grouped_conditions = conn.execute(query).fetchall()

for row in grouped_conditions:
    print(row)

print('{} majors'.format(len(grouped_conditions)))


# ###5: Practice grouping operators

# For this practice problem, we've increased the difficulty to give you better practice expressing complex logic.

# ####Instructions

# To practice using multiple operators, we're going to ask you to find all majors that meet the following criteria:
# 
# - Major_category of Business or Arts or Health
# 
# and
# 
# - Employed students greater than 20,000 or Unemployment_rate below 5.1%
# 
# We're only interested in the following columns (in the following order):
# 
# - Major
# - Major_category
# - Employed
# - Unemployment_rate
# 
# Store the results of the query in a variable named complex_conditions.

# In[6]:

query = """
SELECT Major, Major_category, Employed, Unemployment_rate
FROM recent_grads
WHERE (Major_category = 'Business' or Major_category = 'Arts' or Major_category = 'Health') and (Employed > 20000 or Unemployment_rate < 0.051);
"""

complex_conditions = conn.execute(query).fetchall()

for row in complex_conditions:
    print(row)
    
print('{} majors'.format(len(complex_conditions)))


# ###6: Order by

# The database has been returning all results ordered by the Rank column because that's how the original dataset was ordered. Since this may not make sense for all queries, SQL comes with a statement, ORDER BY, that allows us to specify, for each query, how we'd like the database to order the results. Using ORDER BY , we can specify not only the column we'd like the database to use to order the results by but also whether we'd like them in ascending (ASC), low to high, or descending (DESC), high to low, order. SQL uses the standard methods of ordering: alphabetically for text fields and numerically for numeric fields.
# 
# In the following cell, we'll run 2 queries that return the first 10 values in the Employed columns in first ascending (ASC) then descending order (DESC).

# In[7]:

asc_query = """
SELECT Employed
FROM recent_grads
ORDER BY Employed asc
LIMIT 10;
"""

asc_order = conn.execute(asc_query).fetchall()
print("Ascending Order \n")

for row in asc_order:
    print(row)

desc_query = """
SELECT Employed
FROM recent_grads
ORDER BY Employed desc
LIMIT 10;
"""

desc_order = conn.execute(desc_query).fetchall()
print("\n Descending Order \n")

for row in desc_order:
    print(row)


# 7: Order using multiple columns

# SQL also allows us to specify multiple columns in the ORDER BY statement if we'd like the database to order the results of the query first using the first column, then the second one, and so forth. The database will order the results by the first column and then will order by the second column specified if multiple rows have the same values for the first column. Let's see how the relevant psuedocode looks like:
# 
#     select [column1, column2..]
#     from table_name
#     order by column1 (asc or desc), column2 (asc or desc)
# 
# Ordering by multiple columns is especially useful when working with people's names, where the database will have separate columns for First Name and Last Name and you want the results to be ordered, or alphabetized in this case, by Last Name first then First Name. After alphabetizing all last names, the database will alphabetize by First Name for all rows containing the same values for Last Name. 

# ####Instructions

# We're interested in figuring out which majors in each Major_category have the highest Median salary. Write a query that orders the majors by Major in ascending order then by Median salary in descending order. Return only the first 20 rows so we can easily print the results.
# 
# We're interested in selecting only these columns in the following order:
# 
# - Major_category
# - Median
# - Major
# 
# Store the results of the query in a variable called multiple_order.

# In[8]:

query = """
SELECT Major_category, Median, Major
FROM recent_grads
ORDER BY Major asc, Median desc
LIMIT 20;
"""

multiple_order = conn.execute(query).fetchall()

for row in multiple_order:
    print(row)
    
print('{} majors'.format(len(multiple_order)))

