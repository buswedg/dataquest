

```python
from __future__ import print_function
```

#Python for Business Analysts

##Cleaning Data

###1: Introduction

Art is a messy business. Over centuries, artists have created everything from simple paintings to complex sculptures, and art historians have been cataloging everything they can along the way. The Museum of Modern Art, or MoMA for short, is considered one of the most influential museums in the world and recently released a dataset of all the artworks they’ve cataloged in their collection. This dataset contains basic information on metadata for each artwork and is part of MoMA's push to make art more accessible to everyone.

The museum has put out a disclaimer however that the dataset is still a work in progress - an evolving artwork in its own right perhaps. Because it's still in progress, the dataset has data quality issues and needs some cleanup before we can analyze it.

###2: Show me the Data!

For this post, we'll be working with just the first 100 rows of the dataset. We will first need to import the Pandas library into our environment and then read in the dataset into a DataFrame called artworks. Then, let's preview the first 5 rows using artworks.head(5).


```python
import pandas

artworks = pandas.read_csv("data/Artworks.csv")
artworks.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>﻿Title</th>
      <th>Artist</th>
      <th>ArtistBio</th>
      <th>Date</th>
      <th>Medium</th>
      <th>Dimensions</th>
      <th>CreditLine</th>
      <th>MoMANumber</th>
      <th>Classification</th>
      <th>Department</th>
      <th>DateAcquired</th>
      <th>CuratorApproved</th>
      <th>ObjectID</th>
      <th>URL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Ferdinandsbrücke Project, Vienna, Austria , El...</td>
      <td>Otto Wagner</td>
      <td>(Austrian, 1841–1918)</td>
      <td>1896</td>
      <td>Ink and cut-and-pasted painted pages on paper</td>
      <td>19 1/8 x 66 1/2" (48.6 x 168.9 cm)</td>
      <td>Fractional and promised gift of Jo Carole and ...</td>
      <td>885.1996</td>
      <td>A&amp;D Architectural Drawing</td>
      <td>Architecture &amp; Design</td>
      <td>1996-04-09</td>
      <td>Y</td>
      <td>2</td>
      <td>http://www.moma.org/collection/works/2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>City of Music, National Superior Conservatory ...</td>
      <td>Christian de Portzamparc</td>
      <td>(French, born 1944)</td>
      <td>1987</td>
      <td>Paint and colored pencil on print</td>
      <td>16 x 11 3/4" (40.6 x 29.8 cm)</td>
      <td>Gift of the architect in honor of Lily Auchinc...</td>
      <td>1.1995</td>
      <td>A&amp;D Architectural Drawing</td>
      <td>Architecture &amp; Design</td>
      <td>1995-01-17</td>
      <td>Y</td>
      <td>3</td>
      <td>http://www.moma.org/collection/works/3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Villa near Vienna Project, Outside Vienna, Aus...</td>
      <td>Emil Hoppe</td>
      <td>(Austrian, 1876–1957)</td>
      <td>1903</td>
      <td>Graphite, pen, color pencil, ink, and gouache ...</td>
      <td>13 1/2 x 12 1/2" (34.3 x 31.8 cm)</td>
      <td>Gift of Jo Carole and Ronald S. Lauder</td>
      <td>1.1997</td>
      <td>A&amp;D Architectural Drawing</td>
      <td>Architecture &amp; Design</td>
      <td>1997-01-15</td>
      <td>Y</td>
      <td>4</td>
      <td>http://www.moma.org/collection/works/4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>The Manhattan Transcripts Project, New York, N...</td>
      <td>Bernard Tschumi</td>
      <td>(French and Swiss, born Switzerland 1944)</td>
      <td>1980</td>
      <td>Photographic reproduction with colored synthet...</td>
      <td>20 x 20" (50.8 x 50.8 cm)</td>
      <td>Purchase and partial gift of the architect in ...</td>
      <td>2.1995</td>
      <td>A&amp;D Architectural Drawing</td>
      <td>Architecture &amp; Design</td>
      <td>1995-01-17</td>
      <td>Y</td>
      <td>5</td>
      <td>http://www.moma.org/collection/works/5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Villa, project, outside Vienna, Austria, Exter...</td>
      <td>Emil Hoppe</td>
      <td>(Austrian, 1876–1957)</td>
      <td>1903</td>
      <td>Graphite, color pencil, ink, and gouache on tr...</td>
      <td>15 1/8 x 7 1/2" (38.4 x 19.1 cm)</td>
      <td>Gift of Jo Carole and Ronald S. Lauder</td>
      <td>2.1997</td>
      <td>A&amp;D Architectural Drawing</td>
      <td>Architecture &amp; Design</td>
      <td>1997-01-15</td>
      <td>Y</td>
      <td>6</td>
      <td>http://www.moma.org/collection/works/6</td>
    </tr>
  </tbody>
</table>
</div>



###3: Dating Artists

As you can see, the dataset comes with details on every artwork ranging from the author, his / her's short bio, the artwork's dimensions, date acquired, and even the URL to the artwork's page. While some columns, like DateAcquired, are formatted in the right way for us to plot as a time series, other columns like Date contain a mix of values that make it hard to explore. We ideally want this column to just have the year the artwork was published so that we can plot them.

Let's use a Pandas feature called value_counts(), which returns a list of all the values in that column in addition to their frequency of appearance, similar to a histogram. We want to make sure we have a good sense of all the different formats the values in the Date column take on.


```python
# Returns list of all values in 'Date' column, and their frequency
artworks['Date'].value_counts()
```




    1971                                      1713
    1967                                      1622
    1966                                      1422
    1968                                      1410
    1965                                      1388
    1973                                      1358
    1969                                      1275
    1964                                      1270
    1970                                      1231
    1963                                      1129
    2003                                      1110
    1972                                      1051
    1930                                      1031
    1962                                      1005
    1976                                       954
    1928                                       940
    1980                                       915
    2001                                       913
    2002                                       908
    1931                                       888
    1974                                       842
    1961                                       829
    1984                                       821
    1960                                       808
    1994                                       802
    1977                                       799
    1991                                       798
    1983                                       798
    1959                                       779
    1975                                       778
                                              ... 
    (September 18-21) 1961                       1
    Montroig, late summer-fall 1925              1
    1930-1939                                    1
    (newspaper published March 1, 2000)          1
    (June 27-28, 1961)                           1
    1952-1962                                    1
    (November 11-13, 1968)                       1
    (c. 1865-68)                                 1
    2010-ongoing                                 1
    (1955).  (Prints executed 1905-1955).        1
    1964–66                                      1
    December 12, 1966, published 1968            1
    (January 4-7, 1963)                          1
    1970/2001                                    1
    March 5, 1986                                1
    December 18, 1961-January 12, 1962           1
    (August 12-25) 1969                          1
    May 23, 1977                                 1
    1962 (Prints executed 1959-1961).            1
    c. 1880?                                     1
    1984-1986                                    1
    (1903-1904)                                  1
    (November 7, 1945)                           1
    (February 7-8) 1963                          1
    (newspaper published June 12/13, 2004)       1
    February 21, 1972, published 1972            1
    October 31, 1964                             1
    1925-36                                      1
    (July 24-27, 1962)                           1
    May 26, 1962.                                1
    dtype: int64



###4: Patterns

Looks like there are a few patterns in the Date column that we need to account for:
- Pattern 1: "1976-77" (year ranges)
- Pattern 2: "c. 1917"
- Pattern 3: "Unknown"
- Pattern 4: "n.d."

Now we need to come up Python logic to specify how we want these values to be handled.

For the first one, let's go ahead and just pick the lower of the 2 years provided in the range (e.g. "1976-77" becomes "1976"). For the second pattern, let's just get rid of the "c. " in front of "c. 1917". Finally, let's leave the third pattern alone, "Unknown", and actually convert the values where we see the fourth pattern, "n.d.", into the same value as the third pattern, "Unknown". This way, when we are calculating or plotting using the Date column, we can just filter out all of the artworks that have "Unknown" as their value and proceed without any issues.

Let's step through how we can write a function for dealing with each pattern and transforming the values based on the rules we described above.

###5: Pattern 1

Since all of the rows with pattern 1 are year ranges spanning only two years (e.g. 1980-81), we can select a year and have it replace the range. To keep things simple, let's select the first year in the range since it contains all four digits of the year (1980) while the second year in the range has only the last two digits (81).

We also need a reliable way to identify which rows actually exhibit pattern 1 so we only update those rows and leave the others intact. We need to leave the others intact either because they are already in the proper date format or because they will need to be modified later using the logic we write for handling the other patterns.

Since year ranges contain a hyphen - separating the two years, we can look for the - in each row's Date value and split it into two separate years. The core Python library contains a function named .split() which in this situation will return a list of the two years if a hyphen is found or the original value if it isn't. Since we are looking for just the first year, we can call .split("-") on every row's Date, check to see if the resulting list contains two elements, and if it does, return the first element. Let's write a function clean_split_dates(row) which will do exactly that:


```python
def clean_split_dates(row):
    # Return current value for the 'Date' column for that row.
    initial_date = str(row['Date'])
    final_date = initial_date
    
    # Split string by the dash and create a list with the values surrounding the dash, called `split_date`.
    split_date = initial_date.split('-') 

    # If no dash found, 'split_date' will just contain one item, the initial_date.
    # If dash is found, 'split_date' will contain a list of at least 2 elements, return first element.
    if len(split_date) > 1:
        final_date = split_date[0]
    
    return final_date

# Assign the results of 'clean_split_dates' to the 'Date' column. Since we want Pandas to go
# row by row, we set "axis=1". If we wanted to go by columns, we would use "axis=0".
artworks['Date'] = artworks.apply(lambda row: clean_split_dates(row), axis=1)
artworks['Date'].value_counts()
```




    nan                                               2484
    1971                                              1839
    1967                                              1777
    1969                                              1661
    1968                                              1626
    1966                                              1617
    1965                                              1587
    1964                                              1536
    1973                                              1495
    1970                                              1465
    1900                                              1305
    1972                                              1292
    1930                                              1274
    1963                                              1218
    1931                                              1213
    1928                                              1211
    2003                                              1168
    1962                                              1164
    1926                                              1108
    1976                                              1066
    1980                                              1051
    1948                                              1050
    1925                                              1018
    2002                                              1013
    2001                                               999
    1975                                               994
    1991                                               990
    1974                                               980
    1927                                               956
    1934                                               949
                                                      ... 
    November 30, 1918                                    1
    (May 29) 1970                                        1
    1961, realized 1963                                  1
    (1968, published 1970)                               1
    (February 4                                          1
    Tangier, winter                                      1
    March 5, 1921                                        1
    January 16, 1945                                     1
    1994.  (Prints executed 1989                         1
    September 2, 1996.                                   1
    (late 1980s)                                         1
    (before 1930)                                        1
    February 1, 1977                                     1
    (newspaper published February 28, 1995)              1
    (2012)                                               1
    Waterbury, Connecticut, 1959                         1
    March 13, 1915                                       1
    1976–79                                              1
    1998–1999                                            1
    (October 5, 1945)                                    1
    May 28, 1939                                         1
    (newspapers published May 14 through 28, 2005)       1
    May 2, 1977                                          1
    January 1932                                         1
    1974/1981                                            1
    1964  (Prints executed 1963                          1
    May 24                                               1
    .a (1922), signed 1924 .b (1922)                     1
    (January 31, 1933, printed 1939)                     1
    2008/11                                              1
    dtype: int64



###6: Pattern 2

As you can see, there are no values in Date that are year ranges and contain a "-" separator. Let's now write a function to handle Pattern 2, called clean_c_dates.

This function needs to look for the characters, "c. ", at the beginning of each date and chop that sequence off if it finds it. Let's take advantage of another function that Strings have, called lstrip(chars). The lstrip(chars) function starts from the left side of the String and compares each letter of the String with the chars we passed in. If it finds the full chars phrase, it will remove it from the String. If it doesn't, it keeps it the same!

####Instructions

While the logic for clean_c_dates is written out, we are going to ask you to apply the function to the artworks DataFrame and assign the results to the Date column.


```python
def clean_c_dates(row):
    # Return current value for the 'Date' column for that row.
    initial_date = row['Date']
    # Use .lstrip() to strip from the left side of "c. ".
    final_date = initial_date.lstrip("c. ")
    return final_date

# Assign the results of 'clean_c_dates' to the 'Date' column. Since we want Pandas to go
# row by row, we set "axis=1". If we wanted to go by columns, we would use "axis=0".
artworks['Date'] = artworks.apply(lambda row: clean_c_dates(row), axis=1)
```

###7: Verifying Pattern 2

Let's run value_counts() on the Date column to verify that our logic worked as we expected. Look to make sure the row with Pattern 2 no longer exhibits that pattern.


```python
artworks['Date'].value_counts()
```




    nan                                         2484
    1967                                        1889
    1971                                        1864
    1969                                        1779
    1966                                        1702
    1965                                        1699
    1968                                        1696
    1964                                        1618
    1970                                        1523
    1973                                        1523
    1900                                        1469
    1930                                        1433
    1972                                        1333
    1931                                        1315
    1928                                        1272
    1963                                        1268
    1962                                        1220
    2003                                        1188
    1926                                        1156
    1948                                        1126
    1925                                        1100
    1976                                        1088
    1980                                        1074
    1975                                        1054
    1927                                        1022
    2002                                        1017
    1934                                        1010
    2001                                        1004
    1991                                         992
    1974                                         989
                                                ... 
    (1926).  (Prints executed 1924                 1
    September 1929                                 1
    (1921), dated 1933                             1
    November 18, 1965.                             1
    January 11                                     1
    1994–2014                                      1
    October 1992                                   1
    March 1936                                     1
    January 8, 1986                                1
    January 10, 1914                               1
    (c. 1980/81 )                                  1
    1981.  (Prints executed 1980).                 1
    February 1943                                  1
    (c. 1910, published 1918)                      1
    June 12, 1936, printed 1939                    1
    March 17, 1969                                 1
    (newspaper published August 28/29, 2004)       1
    June 3, 1906                                   1
    November 6, 1998                               1
    (c. 1951)                                      1
    September 1, 1966                              1
    Mars                                           1
    December 10, 1933                              1
    October 18                                     1
    January 10, 1946                               1
    (newspaper published March 21, 2000)           1
    June, 1978                                     1
    1856–57                                        1
    (October 7) 1906                               1
    May 26, 1962.                                  1
    dtype: int64



###8: Pattern 3

The row with "c. 1917" is now just "1917", as expected! We don't have to write any specific code to handle Pattern 3 since we want those values to remain the same as the original. In the functions we use to clean the other 3 patterns, if a match wasn't found, the original Date value was returned. Since "Unknown" doesn't overlap in logic with our other patterns, all rows that had the initial value "Unknown" remained the same!

###9: Pattern 4

For pattern 4, we just need to check if initial_date is equal to n.d., and modify that row's Date value to Unknown if it is. Let's call this function clean_nd_dates then run .value_counts() on the updated Date column as before.


```python
def clean_nd_dates(row):
    # Return current value for the 'Date' column for that row.
    initial_date = row['Date']
    final_date = initial_date
    
    # If equal to "n.d.", replace with "Unknown".
    if initial_date == "n.d.":
        final_date = "Unknown"

    return final_date

# Assign the results of 'clean_nd_dates' to the 'Date' column. Since we want Pandas to go
# row by row, we set "axis=1". If we wanted to go by columns, we would use "axis=0".
artworks['Date'] = artworks.apply(lambda row: clean_nd_dates(row), axis=1)
artworks['Date'].value_counts()
```




    nan                                                                              2484
    1967                                                                             1889
    1971                                                                             1864
    1969                                                                             1779
    1966                                                                             1702
    1965                                                                             1699
    1968                                                                             1696
    1964                                                                             1618
    1973                                                                             1523
    1970                                                                             1523
    1900                                                                             1469
    1930                                                                             1433
    1972                                                                             1333
    1931                                                                             1315
    1928                                                                             1272
    1963                                                                             1268
    1962                                                                             1220
    2003                                                                             1188
    1926                                                                             1156
    1948                                                                             1126
    1925                                                                             1100
    1976                                                                             1088
    1980                                                                             1074
    1975                                                                             1054
    1927                                                                             1022
    2002                                                                             1017
    1934                                                                             1010
    2001                                                                             1004
    1991                                                                              992
    1974                                                                              989
                                                                                     ... 
    (Commissioned by Vollard; prints  executed 1930)                                    1
    August 19, 1934                                                                     1
    (January 31, 1933, printed 1939)                                                    1
    published c. 1924                                                                   1
    June 29, 1979                                                                       1
    before 1971                                                                         1
    (Prints commissioned for various projects  by Vollard;  prints executed  1919       1
    (after 1890)                                                                        1
    August 16, 1913                                                                     1
    November, 1862                                                                      1
    January 16, 1945                                                                    1
    March 5, 1921                                                                       1
    Tangier, winter                                                                     1
    (February 4                                                                         1
    (newspapers published May 14 through 28, 2005)                                      1
    (late 1980s)                                                                        1
    (May 29) 1970                                                                       1
    September 2, 1996.                                                                  1
    November 1946                                                                       1
    July 1952                                                                           1
    1963–77                                                                             1
    October 18, 1940                                                                    1
    1914, published 1919                                                                1
    October 6, 1893                                                                     1
    July 1941                                                                           1
    (newspaper published April 1/2, 2000)                                               1
    November 30, 1918                                                                   1
    1961, realized 1963                                                                 1
    (1968, published 1970)                                                              1
    196?                                                                                1
    dtype: int64



###10: Packaging Logic Into One Function

We now only have specific year values or the value "Unknown" in our Date column. For the purposes of this lesson, we split up the pattern transformations into 3 different functions: clean_split_dates, clean_c_dates, and clean_nd_dates. As you become more familiar with Python and Pandas, you will become more comfortable reducing complexity by writing just one function to handle the patterns. Let's now see what that function could look like, by borrowing from the logic of the 3 functions we wrote above.


```python
# Single transformation function.
def clean_dates(row):
    initial_date = str(row['Date'])
    final_date = initial_date

    # Pattern 1
    split_date = initial_date.split("-")
    
    if len(split_date) > 1:
        final_date = split_date[0]
        return final_date
    
    # Pattern 4
    elif initial_date == "n.d.":
        final_date = "Unknown"
        return final_date
    
    # Pattern 2
    else:
        final_date = initial_date.lstrip("c. ")
    return final_date

# Assign the results of 'clean_dates' to the 'Date' column. Since we want Pandas to go
# row by row, we set "axis=1". If we wanted to go by columns, we would use "axis=0".
artworks = pandas.read_csv("data/Artworks.csv")
artworks['Date'] = artworks.apply(lambda row: clean_dates(row), axis=1)
artworks['Date'].value_counts()
```




    nan                                      2484
    1971                                     1863
    1967                                     1862
    1969                                     1762
    1965                                     1698
    1966                                     1695
    1968                                     1694
    1964                                     1613
    1973                                     1523
    1970                                     1517
    1900                                     1466
    1930                                     1425
    1972                                     1333
    1931                                     1310
    1963                                     1261
    1928                                     1255
    1962                                     1203
    2003                                     1188
    1926                                     1153
    1948                                     1108
    1925                                     1091
    1976                                     1088
    1980                                     1067
    1975                                     1052
    2002                                     1017
    2001                                     1004
    1934                                     1000
    1991                                      992
    1974                                      988
    1927                                      986
                                             ... 
    September 1, 1966                           1
    Mars                                        1
    Published March 1945 (original ready        1
    October 18                                  1
    January 10, 1946                            1
    (newspaper published March 2, 2005)         1
    June, 1978                                  1
    1856–57                                     1
    (October 7) 1906                            1
    June 12, 1936, printed 1939                 1
    1969 (fabricated 1986)                      1
    June 5, 1977                                1
    (1911, dated 1912, published c. 1917)       1
    September 20, 1919                          1
    September 26, 1918                          1
    September 10, 1973                          1
    1953, printed 1980s                         1
    May 1865                                    1
    June 7, 1907                                1
    June 21, 1919                               1
    1917–18                                     1
    (December 29) 1960                          1
    1952/1953                                   1
    January 17, 1995                            1
    (newspaper published: May 27, 1999)         1
    October 16, 1927                            1
    April 1966                                  1
    June 1891                                   1
    2000–2001                                   1
    May 26, 1962.                               1
    dtype: int64



###11: Challenge, Introduction

We've left this next problem up to you as a challenge. If you run .value_counts() on the the ArtistBio column, you'll notice that every value is surrounded by parentheses.


```python
artworks['ArtistBio'].value_counts()[:10]
```




    (French, 1857–1927)                      5050
    (American, born France. 1911–2010)       3229
    (American, born Germany. 1886–1969)      2497
    (American, born 1934)                    1657
    (French, 1901–1985)                      1426
    (Spanish, 1881–1973)                     1311
    (French, born Belarus. 1887–1985)        1151
    (French, 1869–1954)                      1064
    (French, 1867–1947)                       940
    (American, born Lithuania. 1931–1978)     937
    dtype: int64



##12: Challenge, Go!

####Instructions

Write a function clean_parentheses(row) that removes the trailing parentheses from both sides. Just like we used .lstrip() on each value to remove "c. " from values in the Date column, use the function .rstrip() to remove trailing characters from the right side.


```python
def clean_parentheses(row):
    initial_bio = str(row['ArtistBio'])
    left_stripped = initial_bio.lstrip("(")
    final_stripped = left_stripped.rstrip(")")
    final_bio = final_stripped
    return final_bio

artworks['ArtistBio'] = artworks.apply(lambda row: clean_parentheses(row), axis=1)
artworks['ArtistBio'].value_counts()[:10]
```




    French, 1857–1927                    5050
    nan                                  4495
    American, born France. 1911–2010     3229
    American, born Germany. 1886–1969    2497
    American, born 1934                  1657
    French, 1901–1985                    1426
    Spanish, 1881–1973                   1311
    French, born Belarus. 1887–1985      1151
    French, 1869–1954                    1064
    French, 1867–1947                     940
    dtype: int64



##13: Conclusion

The ArtistBio column is now much cleaner without the starting and ending parentheses. You may have noticed that some of the values have parentheses in the middle of the String, instead of just at the edges. Usually in these kinds of situations, you go from exploring the values, coming up with patterns, writing code to deal with them, and then revising and repeating until the data is ready to go. Because our code persists even after we run it, it's easy to iterate through ideas.
