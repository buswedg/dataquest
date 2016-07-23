

```python
from __future__ import print_function
```

#SQL and Databases

##Combining SQL operators


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

###1: Logical Operators

What if we want to use multiple filtering criteria to specify the data we want from the database?

Logical operators are keywords you can use to combine filtering criteria to express more specific conditions. Here are the 2 basic logical operators you will often use:

- Condition1 or Condition2: OR
- Condition1 and Condition2: AND

###2: And

The following is psuedo-code to help you conceptualize how the AND statement is used with a WHERE statement:

    SELECT [column1, column2,...] FROM [table1]
    WHERE [condition1] AND [condition2]

Instead of first writing a SQL query to pull all majors with majority women and then using Python to filter the results, we can use the AND operator to combine the 2 filtering criteria in SQL itself. Let's see what that query would look like:

    SELECT Major,ShareWomen,Employed FROM recent_grads 
    WHERE ShareWomen>0.5 AND Employed>10000;

We want the database to return all rows where both conditions are true:

- ShareWomen > 0.5
- Employed > 10000

We use the Python string <a href = "https://pyformat.info/#simple">format function</a> to print how many majors met both criteria.


```python
query = """
SELECT Major, ShareWomen, Employed
FROM recent_grads
WHERE ShareWomen > 0.5 AND Employed > 10000;
"""

both_conditions = conn.execute(query).fetchall()

print(both_conditions)
print('{} majors'.format(len(both_conditions)))
```

    [('COMPUTER SCIENCE', 0.578766338, 102087), ('NURSING', 0.896018988, 180903), ('COMPUTER AND INFORMATION SYSTEMS', 0.707718502, 28459), ('INTERNATIONAL RELATIONS', 0.632986838, 21190), ('AGRICULTURE PRODUCTION AND MANAGEMENT', 0.59420765, 12323), ('CHEMISTRY', 0.505140538, 48535), ('BUSINESS MANAGEMENT AND ADMINISTRATION', 0.580948004, 276234), ('BIOCHEMICAL SCIENCES', 0.515406449, 25678), ('HUMAN RESOURCES AND PERSONNEL MANAGEMENT', 0.672161443, 20760), ('MISCELLANEOUS HEALTH MEDICAL PROFESSIONS', 0.702020202, 10076), ('ENVIRONMENTAL SCIENCE', 0.584556133, 20859), ('JOURNALISM', 0.719858952, 61022), ('MULTI-DISCIPLINARY OR GENERAL SCIENCE', 0.669998505, 46138), ('ADVERTISING AND PUBLIC RELATIONS', 0.673143392, 45326), ('AREA ETHNIC AND CIVILIZATION STUDIES', 0.758060269, 24629), ('PHYSIOLOGY', 0.906677337, 14643), ('CRIMINOLOGY', 0.618223028, 16181), ('NUTRITION SCIENCES', 0.63814682, 13217), ('HEALTH AND MEDICAL ADMINISTRATIVE SERVICES', 0.770901106, 15419), ('COMMUNICATION TECHNOLOGIES', 0.864456079, 14779), ('NATURAL RESOURCES MANAGEMENT', 0.564639335, 11797), ('GENERAL EDUCATION', 0.812876606, 118241), ('HISTORY', 0.651741294, 105646), ('FRENCH GERMAN LATIN AND OTHER COMMON FOREIGN LANGUAGE STUDIES', 0.728032591, 38315), ('INTERCULTURAL AND INTERNATIONAL STUDIES', 0.507376968, 18824), ('SOCIAL SCIENCE OR HISTORY TEACHER EDUCATION', 0.733967583, 17700), ('COMMUNITY AND PUBLIC HEALTH', 0.652129817, 14512), ('MATHEMATICS TEACHER EDUCATION', 0.792095262, 13115), ('BIOLOGY', 0.601858152, 182295), ('SOCIOLOGY', 0.532333788, 92721), ('MASS MEDIA', 0.877227528, 44679), ('TREATMENT THERAPY PROFESSIONS', 0.64, 37861), ('HOSPITALITY MANAGEMENT', 0.733991928, 36728), ('LANGUAGE AND DRAMA EDUCATION', 0.576360061, 26033), ('LINGUISTICS AND COMPARATIVE LANGUAGE AND LITERATURE', 0.76432029, 11165), ('SECONDARY TEACHER EDUCATION', 0.601751825, 15116), ('GENERAL MEDICAL AND HEALTH SERVICES', 0.774576624, 24406), ('ART AND MUSIC EDUCATION', 0.6860244, 30007), ('ELEMENTARY EDUCATION', 0.923745479, 149339), ('PHYSICAL FITNESS PARKS RECREATION AND LEISURE', 0.683942619, 103078), ('LIBERAL ARTS', 0.70089843, 54844), ('FILM VIDEO AND PHOTOGRAPHIC ARTS', 0.686992952, 31433), ('PSYCHOLOGY', 0.779933204, 307933), ('PHYSICAL AND HEALTH EDUCATION TEACHING', 0.506720763, 23794), ('ART HISTORY AND CRITICISM', 0.845934379, 17579), ('FINE ARTS', 0.667033853, 59679), ('FAMILY AND CONSUMER SCIENCES', 0.752143884, 46624), ('SOCIAL WORK', 0.810704147, 45038), ('ANIMAL SCIENCES', 0.91093257, 17112), ('VISUAL AND PERFORMING ARTS', 0.697384245, 12870), ('TEACHER EDUCATION: MULTIPLE LEVELS', 0.798919817, 13076), ('THEOLOGY AND RELIGIOUS VOCATIONS', 0.728494624, 24202), ('STUDIO ARTS', 0.584776403, 13908), ('ANTHROPOLOGY AND ARCHEOLOGY', 0.968953683, 29633), ('COMMUNICATION DISORDERS SCIENCES AND SERVICES', 0.707136237, 29763), ('EARLY CHILDHOOD EDUCATION', 0.967998119, 32551), ('DRAMA AND THEATER ARTS', 0.629504564, 36165), ('COMPOSITION AND RHETORIC', 0.666119448, 15053)]
    58 majors
    

###3: Or operator

We used the AND operator to specify that our filter needs to pass 2 Boolean conditions, both of which had to evaluate to True for the record to be included in the result set. If we instead want to specify a filter that met either of the conditions, we would use the OR operator.

    SELECT [column1, column2,...] FROM [table1]
    WHERE [condition1] OR [condition2]

We'll dive straight into a practice problem since the OR and AND operators are used in similar ways.

####Instructions

Write a SQL query that will return the first 20 majors that either:

- had a Median salary greater than or equal to 10,000 or
- less than or equal to 1,000 Unemployed people.

We only want to include the following columns in the results with the following order:

- Major
- Median
- Unemployed

Store the results of the query in a variable named either_conditions.


```python
query = """
SELECT Major, Median, Unemployed 
FROM recent_grads 
WHERE Median >= 50000 OR Unemployed <= 1000 LIMIT 20;
"""

either_conditions = conn.execute(query).fetchall()

for row in either_conditions:
    print(row)
```

    ('PETROLEUM ENGINEERING', 110000, 37)
    ('MINING AND MINERAL ENGINEERING', 75000, 85)
    ('METALLURGICAL ENGINEERING', 73000, 16)
    ('NAVAL ARCHITECTURE AND MARINE ENGINEERING', 70000, 40)
    ('CHEMICAL ENGINEERING', 65000, 1672)
    ('NUCLEAR ENGINEERING', 65000, 400)
    ('ACTUARIAL SCIENCE', 62000, 308)
    ('ASTRONOMY AND ASTROPHYSICS', 62000, 33)
    ('MECHANICAL ENGINEERING', 60000, 4650)
    ('ELECTRICAL ENGINEERING', 60000, 3895)
    ('COMPUTER ENGINEERING', 60000, 2275)
    ('AEROSPACE ENGINEERING', 60000, 794)
    ('BIOMEDICAL ENGINEERING', 60000, 1019)
    ('MATERIALS SCIENCE', 60000, 78)
    ('ENGINEERING MECHANICS PHYSICS AND SCIENCE', 58000, 23)
    ('BIOLOGICAL ENGINEERING', 57100, 589)
    ('INDUSTRIAL AND MANUFACTURING ENGINEERING', 57000, 699)
    ('GENERAL ENGINEERING', 56000, 2859)
    ('ARCHITECTURAL ENGINEERING', 54000, 170)
    ('COURT REPORTING', 54000, 11)
    

###4: Grouping operators

There is a certain class of questions that can't be answered using just the techniques we've learned so far. If we wanted to write a query that returned all Engineering majors that either had majority women or an unemployment rate below the August 2015 unemployment rate of 5.1%, we'll need to use parentheses to express this more complex logic.

The 3 raw conditions we'll need:

    Major_category = 'Engineering'
    ShareWomen >= 0.5
    Unemployment_rate < 0.051

How the SQL query looks like using parantheses:

    select Major, Major_category, ShareWomen, Unemployment_rate
    from recent_grads
    where (Major_category = 'Engineering') and (ShareWomen > 0.5 or Unemployment_rate < 0.051);

The first thing you may notice is that we didn't capitalize any of the operators or statements in the query. SQL is case-insensitive with its built-in keywords which means we don't have to capitalize operators like AND or statements like SELECT.

The second thing you may notice is how we grouped logic we wanted to be evaluated together in parentheses. This is very similar to how we group calculations in math together with a particular order. The parentheses makes it explictly clear to the database that we want all the rows where both the expressions in the statements evaluate to True:

    (Major_category = 'Engineering' and ShareWomen > 0.5) -> True or False
    (Unemployment_rate < 0.051) -> True or False

If we had written the where statement without any parentheses, the database would guess what our intentions are and will actually execute the following query instead:

    where (Major_category = 'Engineering' and ShareWomen > 0.5) or (Unemployment_rate < 0.051) 

Leaving parentheses out implies that we want the calculation to happen from left to right in the order the logic is written and wouldn't return us the data we want. Let's now run our intended query and see the results!


```python
query = """
SELECT Major, Major_category, ShareWomen, Unemployment_rate
FROM recent_grads
WHERE (Major_category = 'Engineering') and (ShareWomen > 0.5 or Unemployment_rate < 0.051);
"""

grouped_conditions = conn.execute(query).fetchall()

for row in grouped_conditions:
    print(row)

print('{} majors'.format(len(grouped_conditions)))
```

    ('PETROLEUM ENGINEERING', 'Engineering', 0.120564344, 0.018380527)
    ('METALLURGICAL ENGINEERING', 'Engineering', 0.153037383, 0.024096386)
    ('NAVAL ARCHITECTURE AND MARINE ENGINEERING', 'Engineering', 0.107313196, 0.050125313)
    ('MATERIALS SCIENCE', 'Engineering', 0.310820285, 0.023042836)
    ('ENGINEERING MECHANICS PHYSICS AND SCIENCE', 'Engineering', 0.183985189, 0.006334343)
    ('INDUSTRIAL AND MANUFACTURING ENGINEERING', 'Engineering', 0.343473218, 0.042875544)
    ('MATERIALS ENGINEERING AND MATERIALS SCIENCE', 'Engineering', 0.292607004, 0.027788805)
    ('ENVIRONMENTAL ENGINEERING', 'Engineering', 0.558548009, 0.093588575)
    ('INDUSTRIAL PRODUCTION TECHNOLOGIES', 'Engineering', 0.75047259, 0.028308097)
    ('ENGINEERING AND INDUSTRIAL MANAGEMENT', 'Engineering', 0.174122505, 0.03365166)
    10 majors
    

###5: Practice grouping operators

For this practice problem, we've increased the difficulty to give you better practice expressing complex logic.

####Instructions

To practice using multiple operators, we're going to ask you to find all majors that meet the following criteria:

- Major_category of Business or Arts or Health

and

- Employed students greater than 20,000 or Unemployment_rate below 5.1%

We're only interested in the following columns (in the following order):

- Major
- Major_category
- Employed
- Unemployment_rate

Store the results of the query in a variable named complex_conditions.


```python
query = """
SELECT Major, Major_category, Employed, Unemployment_rate
FROM recent_grads
WHERE (Major_category = 'Business' or Major_category = 'Arts' or Major_category = 'Health') and (Employed > 20000 or Unemployment_rate < 0.051);
"""

complex_conditions = conn.execute(query).fetchall()

for row in complex_conditions:
    print(row)
    
print('{} majors'.format(len(complex_conditions)))
```

    ('OPERATIONS LOGISTICS AND E-COMMERCE', 'Business', 10027, 0.047858703)
    ('NURSING', 'Health', 180903, 0.044862724)
    ('FINANCE', 'Business', 145696, 0.060686356)
    ('ACCOUNTING', 'Business', 165527, 0.069749014)
    ('MEDICAL TECHNOLOGIES TECHNICIANS', 'Health', 13150, 0.03698279)
    ('MEDICAL ASSISTING SERVICES', 'Health', 9168, 0.042506527)
    ('GENERAL BUSINESS', 'Business', 190183, 0.072861468)
    ('BUSINESS MANAGEMENT AND ADMINISTRATION', 'Business', 276234, 0.072218341)
    ('MARKETING AND MARKETING RESEARCH', 'Business', 178862, 0.061215064)
    ('HUMAN RESOURCES AND PERSONNEL MANAGEMENT', 'Business', 20760, 0.059569649)
    ('COMMERCIAL ART AND GRAPHIC DESIGN', 'Arts', 83483, 0.096797577)
    ('TREATMENT THERAPY PROFESSIONS', 'Health', 37861, 0.059821207)
    ('HOSPITALITY MANAGEMENT', 'Business', 36728, 0.061169193)
    ('GENERAL MEDICAL AND HEALTH SERVICES', 'Health', 24406, 0.082101621)
    ('FILM VIDEO AND PHOTOGRAPHIC ARTS', 'Arts', 31433, 0.10577224)
    ('MUSIC', 'Arts', 47662, 0.075959674)
    ('FINE ARTS', 'Arts', 59679, 0.084186296)
    ('COMMUNICATION DISORDERS SCIENCES AND SERVICES', 'Health', 29763, 0.047584)
    ('DRAMA AND THEATER ARTS', 'Arts', 36165, 0.07754113)
    19 majors
    

###6: Order by

The database has been returning all results ordered by the Rank column because that's how the original dataset was ordered. Since this may not make sense for all queries, SQL comes with a statement, ORDER BY, that allows us to specify, for each query, how we'd like the database to order the results. Using ORDER BY , we can specify not only the column we'd like the database to use to order the results by but also whether we'd like them in ascending (ASC), low to high, or descending (DESC), high to low, order. SQL uses the standard methods of ordering: alphabetically for text fields and numerically for numeric fields.

In the following cell, we'll run 2 queries that return the first 10 values in the Employed columns in first ascending (ASC) then descending order (DESC).


```python
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
```

    Ascending Order 
    
    (0,)
    (559,)
    (604,)
    (613,)
    (640,)
    (648,)
    (703,)
    (730,)
    (742,)
    (758,)
    
     Descending Order 
    
    (307933,)
    (276234,)
    (190183,)
    (182295,)
    (180903,)
    (179633,)
    (178862,)
    (165527,)
    (149339,)
    (149180,)
    

7: Order using multiple columns

SQL also allows us to specify multiple columns in the ORDER BY statement if we'd like the database to order the results of the query first using the first column, then the second one, and so forth. The database will order the results by the first column and then will order by the second column specified if multiple rows have the same values for the first column. Let's see how the relevant psuedocode looks like:

    select [column1, column2..]
    from table_name
    order by column1 (asc or desc), column2 (asc or desc)

Ordering by multiple columns is especially useful when working with people's names, where the database will have separate columns for First Name and Last Name and you want the results to be ordered, or alphabetized in this case, by Last Name first then First Name. After alphabetizing all last names, the database will alphabetize by First Name for all rows containing the same values for Last Name. 

####Instructions

We're interested in figuring out which majors in each Major_category have the highest Median salary. Write a query that orders the majors by Major in ascending order then by Median salary in descending order. Return only the first 20 rows so we can easily print the results.

We're interested in selecting only these columns in the following order:

- Major_category
- Median
- Major

Store the results of the query in a variable called multiple_order.


```python
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
```

    ('Business', 45000, 'ACCOUNTING')
    ('Business', 62000, 'ACTUARIAL SCIENCE')
    ('Communications & Journalism', 35000, 'ADVERTISING AND PUBLIC RELATIONS')
    ('Engineering', 60000, 'AEROSPACE ENGINEERING')
    ('Agriculture & Natural Resources', 40000, 'AGRICULTURAL ECONOMICS')
    ('Agriculture & Natural Resources', 40000, 'AGRICULTURE PRODUCTION AND MANAGEMENT')
    ('Agriculture & Natural Resources', 30000, 'ANIMAL SCIENCES')
    ('Humanities & Liberal Arts', 28000, 'ANTHROPOLOGY AND ARCHEOLOGY')
    ('Computers & Mathematics', 45000, 'APPLIED MATHEMATICS')
    ('Engineering', 54000, 'ARCHITECTURAL ENGINEERING')
    ('Engineering', 40000, 'ARCHITECTURE')
    ('Humanities & Liberal Arts', 35000, 'AREA ETHNIC AND CIVILIZATION STUDIES')
    ('Education', 32100, 'ART AND MUSIC EDUCATION')
    ('Humanities & Liberal Arts', 31000, 'ART HISTORY AND CRITICISM')
    ('Physical Sciences', 62000, 'ASTRONOMY AND ASTROPHYSICS')
    ('Physical Sciences', 35000, 'ATMOSPHERIC SCIENCES AND METEOROLOGY')
    ('Biology & Life Science', 37400, 'BIOCHEMICAL SCIENCES')
    ('Engineering', 57100, 'BIOLOGICAL ENGINEERING')
    ('Biology & Life Science', 33400, 'BIOLOGY')
    ('Engineering', 60000, 'BIOMEDICAL ENGINEERING')
    20 majors
    
