

```python
from __future__ import print_function
```

#Data Cleaning

##Cleaning Data

###1: Life and death of Avengers

The Avengers are a well-known and widely loved team of superheroes in the Marvel universe that were introduced in the 1960's in the original comic book series. They've since become popularized again through the recent Disney movies as part of the new Marvel Cinematic Universe.

The team at FiveThirtyEight wanted to dissect the deaths of the Avengers in the comics over the years. The writers were known to kill off and revive many of the superheroes so they were curious to know what data they could grab from the Marvel Wikia <a href = "http://marvel.wikia.com/wiki/Main_Page">site</a>, a fan-driven community site, to explore further. To learn how they collected their data, available on their Github <a href = "https://github.com/fivethirtyeight/data/tree/master/avengers">repo</a>, read the writeup they published on their <a href = "http://fivethirtyeight.com/features/avengers-death-comics-age-of-ultron/">site</a>.

###2: Exploring the data

While the FiveThirtyEight team has done a wonderful job acquiring this data, the data still has some inconsistencies. Your mission is to clean up their dataset so it can be more useful for analysis in Pandas. First things first, let's read our dataset into Padas as a DataFrame and preview the first 5 rows to get a better sense of our data.


```python
import pandas as pd

avengers = pd.read_csv("data/avengers.csv", encoding="cp1252")
avengers.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>URL</th>
      <th>Name/Alias</th>
      <th>Appearances</th>
      <th>Current?</th>
      <th>Gender</th>
      <th>Probationary Introl</th>
      <th>Full/Reserve Avengers Intro</th>
      <th>Year</th>
      <th>Years since joining</th>
      <th>Honorary</th>
      <th>...</th>
      <th>Return1</th>
      <th>Death2</th>
      <th>Return2</th>
      <th>Death3</th>
      <th>Return3</th>
      <th>Death4</th>
      <th>Return4</th>
      <th>Death5</th>
      <th>Return5</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>http://marvel.wikia.com/Henry_Pym_(Earth-616)</td>
      <td>Henry Jonathan "Hank" Pym</td>
      <td>1269</td>
      <td>YES</td>
      <td>MALE</td>
      <td>NaN</td>
      <td>Sep-63</td>
      <td>1963</td>
      <td>52</td>
      <td>Full</td>
      <td>...</td>
      <td>NO</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Merged with Ultron in Rage of Ultron Vol. 1. A...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>http://marvel.wikia.com/Janet_van_Dyne_(Earth-...</td>
      <td>Janet van Dyne</td>
      <td>1165</td>
      <td>YES</td>
      <td>FEMALE</td>
      <td>NaN</td>
      <td>Sep-63</td>
      <td>1963</td>
      <td>52</td>
      <td>Full</td>
      <td>...</td>
      <td>YES</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Dies in Secret Invasion V1:I8. Actually was se...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>http://marvel.wikia.com/Anthony_Stark_(Earth-616)</td>
      <td>Anthony Edward "Tony" Stark</td>
      <td>3068</td>
      <td>YES</td>
      <td>MALE</td>
      <td>NaN</td>
      <td>Sep-63</td>
      <td>1963</td>
      <td>52</td>
      <td>Full</td>
      <td>...</td>
      <td>YES</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Death: "Later while under the influence of Imm...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>http://marvel.wikia.com/Robert_Bruce_Banner_(E...</td>
      <td>Robert Bruce Banner</td>
      <td>2089</td>
      <td>YES</td>
      <td>MALE</td>
      <td>NaN</td>
      <td>Sep-63</td>
      <td>1963</td>
      <td>52</td>
      <td>Full</td>
      <td>...</td>
      <td>YES</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Dies in Ghosts of the Future arc. However "he ...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>http://marvel.wikia.com/Thor_Odinson_(Earth-616)</td>
      <td>Thor Odinson</td>
      <td>2402</td>
      <td>YES</td>
      <td>MALE</td>
      <td>NaN</td>
      <td>Sep-63</td>
      <td>1963</td>
      <td>52</td>
      <td>Full</td>
      <td>...</td>
      <td>YES</td>
      <td>YES</td>
      <td>NO</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Dies in Fear Itself brought back because that'...</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 21 columns</p>
</div>



###3: Filter out the bad years

Since the data was collected from a community site, where most of the contributions came from individual users, there's room for errors to surface in the dataset. If you plot a histogram of the values in the Year column, which describe the year that Avenger was introduced, you'll immediately notice some oddities. There are quite a few Avengers who look like they were introduced in 1900, which we know is a little fishy. The Avengers weren't introduced in the comic series until the 1960's!

This is obviously a mistake in the data and you should remove all Avengers before 1960 from the DataFrame.

####Instructions

We only want to keep the Avengers who were introduced after 1960. Filter out all Avengers introduced before 1960 and store only the ones added in 1960 or later in true_avengers.


```python
import matplotlib.pyplot as plt
%matplotlib inline

true_avengers = pd.DataFrame()

avengers['Year'].hist()
true_avengers = avengers[avengers["Year"] > 1959]
```


![png](output_12_0.png)


###4: Consolidating deaths

We are interested in the number of total deaths each character experienced and we'd like a field containing that distilled information. Right now, there are 5 fields (Death1 to Death5) that each contain a binary value representing if a superhero experienced that death or not. For example, a superhero can experience Death1, then Death2, etc. until they were no longer brought back to life by the writers.

We'd like to coalesce that information into just one field so we can do numerical analysis more easily.

####Instructions

Create a new column, Deaths, that contains the number of times each superhero died. The possible values for each death field are YES, NO, and the Pandas NaN value used to represent missing data. Keep all of the the original columns (including Death1 to Death5) and update true_avengers with the new Deaths column.


```python
def clean_deaths(row):
    num_deaths = 0
    columns = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
    
    for c in columns:
        death = row[c]
        if pd.isnull(death) or death == 'NO':
            continue
        elif death == 'YES':
            num_deaths += 1
    return num_deaths

true_avengers['Deaths'] = true_avengers.apply(lambda row: clean_deaths(row), axis=1)
print("true_avengers['Deaths'][:5]:\n", true_avengers['Deaths'][:5])
```

    true_avengers['Deaths'][:5]:
     0    1
    1    1
    2    1
    3    1
    4    2
    Name: Deaths, dtype: int64
    

    C:\Anaconda3\lib\site-packages\ipykernel\__main__.py:13: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
    

###5: Years since joining

For the final task, we want to know if the Years since joining field accurately reflects the Year column. If an Avenger was introduced in Year 1960, is the Years since joined value for that Avenger 55?

####Instructions

Calculate the number of rows where Years since joined is accurate. This challenge was created in 2015, so use that as the reference year. We want to know for how many rows Years since joinedwas correctly calculated as Year value subtracted from 2015.


```python
correct_joined_years = true_avengers[true_avengers['Years since joining'] == (2015 - true_avengers['Year'])]
joined_accuracy_count = len(correct_joined_years)

print("joined_accuracy_count:", joined_accuracy_count)
```

    joined_accuracy_count: 159
    
