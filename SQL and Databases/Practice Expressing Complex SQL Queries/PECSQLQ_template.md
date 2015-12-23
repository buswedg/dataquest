

```python
from __future__ import print_function
```

#SQL and Databases

##Practice expressing complex SQL queries


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
```

###1: Introduction

In this challenge, we'll continue working with the same table containing data on job outcomes by college major, for recent grads only, but will allow you to practice writing your own SQL queries.

###2: Select and Limit

####Instructions

Write a query that retrieves:

The first 20 majors in the table, only these columns in the following order:

- College_jobs
- Median
- Unemployment_rate

Store the results in a variable named results.


```python
query = """
SELECT College_jobs, Median, Unemployment_rate
FROM recent_grads
LIMIT 20;
"""
results = conn.execute(query).fetchall()

for row in results:
    print(row)
```

    (1534, 110000, 0.018380527)
    (350, 75000, 0.117241379)
    (456, 73000, 0.024096386)
    (529, 70000, 0.050125313)
    (18314, 65000, 0.061097712)
    (1142, 65000, 0.177226407)
    (1768, 62000, 0.095652174)
    (972, 62000, 0.021167415)
    (52844, 60000, 0.057342278)
    (45829, 60000, 0.059173845)
    (23694, 60000, 0.065409275)
    (8184, 60000, 0.065162085)
    (6439, 60000, 0.09208386)
    (2626, 60000, 0.023042836)
    (2439, 58000, 0.006334343)
    (3603, 57100, 0.087143069)
    (8306, 57000, 0.042875544)
    (26898, 56000, 0.059824231)
    (1665, 54000, 0.061930783)
    (402, 54000, 0.011689692)
    

###3: Where

####Instructions

Write a query that returns the first 5 Arts majors (only include the Major column). Store the results in a variable named five_arts.


```python
query = """
SELECT major
FROM recent_grads 
WHERE Major_category = 'Arts'
LIMIT 5;
"""
results = conn.execute(query).fetchall()

for row in results:
    print(row)
```

    ('MISCELLANEOUS FINE ARTS',)
    ('COMMERCIAL ART AND GRAPHIC DESIGN',)
    ('FILM VIDEO AND PHOTOGRAPHIC ARTS',)
    ('MUSIC',)
    ('FINE ARTS',)
    

###4: Operators

####Instructions

Return all non-engineering majors with a median salary less than or equal to 50,000 or an unemployment rate higher than 6.5%.

Return only these columns in the following order:

- Major
- Total
- Median
- Unemployment_rate

Store the results in a variable named non_engineering.


```python
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
```

    ('ACTUARIAL SCIENCE', 3777, 62000, 0.095652174)
    ('FOOD SCIENCE', 4361, 53000, 0.09693146)
    ('CONSTRUCTION SERVICES', 18498, 50000, 0.060023041)
    ('OPERATIONS LOGISTICS AND E-COMMERCE', 11732, 50000, 0.047858703)
    ('PUBLIC POLICY', 5978, 50000, 0.128426299)
    ('MISCELLANEOUS FINE ARTS', 3340, 50000, 0.089375)
    ('NURSING', 209394, 48000, 0.044862724)
    ('FINANCE', 174506, 47000, 0.060686356)
    ('ECONOMICS', 139247, 47000, 0.099092317)
    ('BUSINESS ECONOMICS', 13302, 46000, 0.096448381)
    ('NUCLEAR, INDUSTRIAL RADIOLOGY, AND BIOLOGICAL TECHNOLOGIES', 2116, 46000, 0.07154047)
    ('ACCOUNTING', 198633, 45000, 0.069749014)
    ('MATHEMATICS', 72397, 45000, 0.047277138)
    ('COMPUTER AND INFORMATION SYSTEMS', 36698, 45000, 0.093460326)
    ('PHYSICS', 32142, 45000, 0.048224496)
    ('MEDICAL TECHNOLOGIES TECHNICIANS', 15914, 45000, 0.03698279)
    ('INFORMATION SCIENCES', 11913, 45000, 0.060741445)
    ('STATISTICS AND DECISION SCIENCE', 6251, 45000, 0.086273666)
    ('APPLIED MATHEMATICS', 4939, 45000, 0.090823307)
    

###5: Ordering

####Instructions

Return all non-engineering majors in reverse alphabetical order and store the results in the variable reverse_non_engineering. We're only interested in the major names in the results.


```python
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
```

    ('ZOOLOGY',)
    ('VISUAL AND PERFORMING ARTS',)
    ('UNITED STATES HISTORY',)
    ('TREATMENT THERAPY PROFESSIONS',)
    ('TRANSPORTATION SCIENCES AND TECHNOLOGIES',)
    ('THEOLOGY AND RELIGIOUS VOCATIONS',)
    ('TEACHER EDUCATION: MULTIPLE LEVELS',)
    ('STUDIO ARTS',)
    ('STATISTICS AND DECISION SCIENCE',)
    ('SPECIAL NEEDS EDUCATION',)
    ('SOIL SCIENCE',)
    ('SOCIOLOGY',)
    ('SOCIAL WORK',)
    ('SOCIAL SCIENCE OR HISTORY TEACHER EDUCATION',)
    ('SOCIAL PSYCHOLOGY',)
    ('SECONDARY TEACHER EDUCATION',)
    ('SCIENCE AND COMPUTER TEACHER EDUCATION',)
    ('SCHOOL STUDENT COUNSELING',)
    ('PUBLIC POLICY',)
    
