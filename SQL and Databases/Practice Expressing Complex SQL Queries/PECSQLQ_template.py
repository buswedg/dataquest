
# coding: utf-8

# In[1]:

from __future__ import print_function


# #SQL and Databases

# ##Practice expressing complex SQL queries

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


# ###1: Introduction

# In this challenge, we'll continue working with the same table containing data on job outcomes by college major, for recent grads only, but will allow you to practice writing your own SQL queries.

# ###2: Select and Limit

# ####Instructions

# Write a query that retrieves:
# 
# The first 20 majors in the table, only these columns in the following order:
# 
# - College_jobs
# - Median
# - Unemployment_rate
# 
# Store the results in a variable named results.

# In[3]:

query = """
SELECT College_jobs, Median, Unemployment_rate
FROM recent_grads
LIMIT 20;
"""
results = conn.execute(query).fetchall()

for row in results:
    print(row)


# ###3: Where

# ####Instructions

# Write a query that returns the first 5 Arts majors (only include the Major column). Store the results in a variable named five_arts.

# In[4]:

query = """
SELECT major
FROM recent_grads 
WHERE Major_category = 'Arts'
LIMIT 5;
"""
results = conn.execute(query).fetchall()

for row in results:
    print(row)


# ###4: Operators

# ####Instructions

# Return all non-engineering majors with a median salary less than or equal to 50,000 or an unemployment rate higher than 6.5%.
# 
# Return only these columns in the following order:
# 
# - Major
# - Total
# - Median
# - Unemployment_rate
# 
# Store the results in a variable named non_engineering.

# In[5]:

query = """
 SELECT Major, Total, Median, Unemployment_rate
 FROM recent_grads 
 WHERE (Major_category != 'Engineering') and (Unemployment_rate > 0.065 or Median <= 50000);
"""
non_engineering = conn.execute(query).fetchall()

i = 0
for row in non_engineering:
    i += 1
    if i < 20:
        print(row)


# ###5: Ordering

# ####Instructions

# Return all non-engineering majors in reverse alphabetical order and store the results in the variable reverse_non_engineering. We're only interested in the major names in the results.

# In[6]:

query = """
SELECT major
FROM recent_grads
WHERE Major_category != 'Engineering'
ORDER by major desc;
"""
reverse_non_engineering = conn.execute(query).fetchall()

i = 0
for row in reverse_non_engineering:
    i += 1
    if i < 20:
        print(row)

