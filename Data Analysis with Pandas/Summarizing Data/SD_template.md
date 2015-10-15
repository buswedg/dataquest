
#Data Analysis with Pandas

##Summarizing Data

###1: College majors and employment

The American Community Survey is a survey run by the US Census Bureau that collects data on everything from the affordability of housing to employment rates for different industries. For this challenge, you'll be using the data derived from the American Community Survey for years 2010-2012.

Here's a quick overview of the files we'll be working with:

- all-ages.csv - employment data by major for all ages
- recent-grads.csv - employment data by major for just recent college graduates


```python
import pandas as pd

all_ages = pd.read_csv("data/all-ages.csv")
all_ages.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Major_code</th>
      <th>Major</th>
      <th>Major_category</th>
      <th>Total</th>
      <th>Employed</th>
      <th>Employed_full_time_year_round</th>
      <th>Unemployed</th>
      <th>Unemployment_rate</th>
      <th>Median</th>
      <th>P25th</th>
      <th>P75th</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1100</td>
      <td>GENERAL AGRICULTURE</td>
      <td>Agriculture &amp; Natural Resources</td>
      <td>128148</td>
      <td>90245</td>
      <td>74078</td>
      <td>2423</td>
      <td>0.026147</td>
      <td>50000</td>
      <td>34000</td>
      <td>80000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1101</td>
      <td>AGRICULTURE PRODUCTION AND MANAGEMENT</td>
      <td>Agriculture &amp; Natural Resources</td>
      <td>95326</td>
      <td>76865</td>
      <td>64240</td>
      <td>2266</td>
      <td>0.028636</td>
      <td>54000</td>
      <td>36000</td>
      <td>80000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1102</td>
      <td>AGRICULTURAL ECONOMICS</td>
      <td>Agriculture &amp; Natural Resources</td>
      <td>33955</td>
      <td>26321</td>
      <td>22810</td>
      <td>821</td>
      <td>0.030248</td>
      <td>63000</td>
      <td>40000</td>
      <td>98000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1103</td>
      <td>ANIMAL SCIENCES</td>
      <td>Agriculture &amp; Natural Resources</td>
      <td>103549</td>
      <td>81177</td>
      <td>64937</td>
      <td>3619</td>
      <td>0.042679</td>
      <td>46000</td>
      <td>30000</td>
      <td>72000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1104</td>
      <td>FOOD SCIENCE</td>
      <td>Agriculture &amp; Natural Resources</td>
      <td>24280</td>
      <td>17281</td>
      <td>12722</td>
      <td>894</td>
      <td>0.049188</td>
      <td>62000</td>
      <td>38500</td>
      <td>90000</td>
    </tr>
  </tbody>
</table>
</div>




```python
recent_grads = pd.read_csv("data/recent-grads.csv")
recent_grads.head(5)
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



###2: Summarizing major categories

In both of these datasets, majors are grouped into categories. As you may have noticed, there are multiple rows with a common value for Major_category but different values for Major. We would like to know the total number of people in each Major_category for both datasets.

####Instructions

Use the Total column to calculate the number of people who fall under each Major_category and store the result as a separate dictionary for each dataset. The key for the dictionary should be the Major_category and the value should be the total count. For the counts fromall_ages, store the results as a dictionary named all_ages_major_categories and for the counts from recent_grads, store the results as a dictionary named recent_grads_major_categories.

Format of dictionary:

{ 
    "Engineering": 500,
    "Business": 500
    ...
}


```python
# All values for "Major_category"
print all_ages['Major_category'].value_counts().index
print recent_grads['Major_category'].value_counts().index

all_ages_major_categories = dict()
recent_grads_major_categories = dict()
def calculate_major_cat_totals(df):
    cats = df['Major_category'].value_counts().index
    counts_dictionary = dict()

    for c in cats:
        major_df = df[df["Major_category"] == c]
        total = major_df["Total"].sum(axis=0)
        counts_dictionary[c] = total
    return counts_dictionary

all_ages_major_categories = calculate_major_cat_totals(all_ages)
recent_grads_major_categories = calculate_major_cat_totals(recent_grads)
```

    Index([u'Engineering', u'Education', u'Humanities & Liberal Arts',
           u'Biology & Life Science', u'Business', u'Health',
           u'Computers & Mathematics', u'Physical Sciences',
           u'Agriculture & Natural Resources', u'Psychology & Social Work',
           u'Social Science', u'Arts', u'Industrial Arts & Consumer Services',
           u'Law & Public Policy', u'Communications & Journalism',
           u'Interdisciplinary'],
          dtype='object')
    Index([u'Engineering', u'Education', u'Humanities & Liberal Arts',
           u'Biology & Life Science', u'Business', u'Health',
           u'Computers & Mathematics', u'Physical Sciences',
           u'Agriculture & Natural Resources', u'Psychology & Social Work',
           u'Social Science', u'Arts', u'Industrial Arts & Consumer Services',
           u'Law & Public Policy', u'Communications & Journalism',
           u'Interdisciplinary'],
          dtype='object')
    

###3: Low wage jobs rates

The press likes to talk a lot about how many college grads are unable to get higher wage, skilled jobs and end up working lower wage, unskilled jobs instead. As a data person, it is your job to be skeptical of any broad claims and explore if you can acquire and analyze relevant data to obtain a more nuanced view. Let's run some basic calculations to explore that idea further.

####Instructions

Use the "Low_wage_jobs" and "Total" columns to calculate the proportion of recent college graduates that worked low wage jobs. Store the resulting float object of the calculation as 'low_wage_percent'.


```python
low_wage_percent = 0.0

low_wage_percent = float(recent_grads['Low_wage_jobs'].sum(axis=0)) / (recent_grads['Total'].sum(axis=0))
print low_wage_percent
```

    0.0985254607612
    

###4: Comparing datasets

Both all_ages and recent_grads datasets have 173 rows, corresponding to the 173 college major codes. This enables us to do some comparisons between the two datasets and perform some initial calculations to see how similar or different the statistics of recent college graduates are from those of the entire population.

####Instructions

We want to know the number of majors where recent grads fare better than the overall population.

For each major:

- increment recent_grads_lower_emp_count if Unemployment_rate is lower for recent_grads
- increment all_ages_lower_emp_count if Unemployment_rate is lowwer for all_ages
- do nothing if Unemployment_rate is the same for both


```python
# All majors, common to both DataFrames
majors = recent_grads['Major'].value_counts().index

recent_grads_lower_emp_count = 0
all_ages_lower_emp_count = 0
for m in majors:
    recent_grads_row = recent_grads[recent_grads['Major'] == m]
    all_ages_row = all_ages[all_ages['Major'] == m]
    
    recent_grads_unemp_rate = recent_grads_row['Unemployment_rate'].values[0]
    all_ages_unemp_rate = all_ages_row['Unemployment_rate'].values[0]
    
    if recent_grads_unemp_rate < all_ages_unemp_rate:
        recent_grads_lower_emp_count += 1
    elif all_ages_unemp_rate < recent_grads_unemp_rate:
        all_ages_lower_emp_count += 1
        
print recent_grads_lower_emp_count
print all_ages_lower_emp_count
```

    43
    128
    
