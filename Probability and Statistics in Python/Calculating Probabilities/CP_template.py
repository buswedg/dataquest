
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Probability and Statistics in Python

# ##Calculating Probabilities

# ###1: The dataset

# In many countries, there are bikesharing programs where anyone can rent a bike from a depot, and return it at other depots throughout a city. There is one such program in Washington, D.C., in the US. We'll be looking at the number of bikes that were rented by day. Here are the relevant columns:
# - dteday -- the date that we're looking at.
# - casual -- the number of casual riders (people who hadn't previously signed up with the bikesharing program) that rented bikes on the day.
# - registered -- the number of registered riders (people who signed up previously) that rented bikes.
# - cnt -- the total number of bikes rented.
# 
# This data was collected by Hadi Fanaee-T at the University of Porto and can be downloaded <a href = "http://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset">here</a>.

# In[2]:

import pandas

bikes = pandas.read_csv("data/day.csv")
bikes[:5]


# ###2: Probability of renting bikes

# Let's explore our data a bit, and find the probability that more than 2000 bikes will be rented on any given day.

# ####Instructions

# Find the probability that more than 4000 bikes were rented on any given day. Assign the result to probability_over_4000.

# In[3]:

# Find the number of days the bikes rented exceeded the threshold.
days_over_threshold = bikes[bikes["cnt"] > 2000].shape[0]
# Find the total number of days we have data for.
total_days = bikes.shape[0]

# Get the probability that more than 2000 bikes were rented for any given day.
probability_over_2000 = float(days_over_threshold) / total_days
print("probability_over_2000:", probability_over_2000)

days_over_threshold = bikes[bikes["cnt"] > 4000].shape[0]
probability_over_4000 = float(days_over_threshold) / total_days
print("probability_over_4000:", probability_over_4000)


# ###3: Up to or greater

# Let's say we flip three coins, and we want to know the probability of getting 2 or more heads. In order to do this, we'd need to add the probability of getting exactly 2 heads with the probability of getting exactly 3 heads. The probability that any single coin will be heads is .5 (the probability that the coin will be tails is the same, .5).
# 
# The probability of 3 heads is easy to calculate -- this can only happen in one situation, where all three coins are heads, or `.5*.5*.5`, which equals .125.
# 
# The probability of 2 heads is a little trickier -- there are three different combinations that the three coins can configure themselves in to end up with 2 heads. We'll show this in the table below, using H for heads, and T for tails.
# 
#     Coin 1    Coin 2    Coin 3
#     H         H         T
#     T         H         H
#     H         T         H
# 
# Each one of these has a probability of `.5*.5*.5`, so we just multiply 3 * .125 to get .375, the probability that we'll get 2 heads.
# 
# We then just have to add up the probability of getting 2 heads to the probability of getting 3 heads to get .5, the probability of getting 2 or more heads when we flip 3 coins.

# ###4: Calculating probabilities

# Now that we know how to calculate probabilities for coins, let's calculate the probability that 1 coin out of 3 is heads.

# ####Instructions

# Find the probability that 1 coin out of 3 is heads. Assign the result to coin_1_prob.

# In[4]:

# There are three combinations in which we can have one coin heads.
# HTT, THT, TTH
# Each combination's probability is (.5 * .5 * .5)
combination_prob = (.5 * .5 * .5) 

# The probability for one combination is in combination_prob -- multiply by the three possible combinations.
coin_1_prob = 3 * combination_prob
print("coin_1_prob:", coin_1_prob)


# ###5: Number of combinations

# What we found in the last screen was that there were exactly 3 combinations of coins to get 2 out of the 3 coins to be heads. There was exactly 1 combination to get all three coins to be heads.
# 
# Let's scale this example up a little bit. Let's say that we live in Los Angeles, CA, and the chance of any single day being sunny is .7. The chance of a day not being sunny is .3.
# 
# If we have a sample of 5 days, and we want to find the chance that all 5 of them will be sunny, there's only one combination that allows this to happen -- the sunny outcome has to occur on all 5 days:
# 
#     Day 1    Day 2    Day 3    Day 4    Day 5
#     S        S        S        S        S
# 
# If we want to find the probability that only 4 days will be sunny, there are 5 possible combinations.
# 
#     Day 1    Day 2    Day 3    Day 4    Day 5
#     S        S        S        S        N
#     S        S        S        N        S
#     S        S        N        S        S
#     S        N        S        S        S
#     N        S        S        S        S
# 
# You may notice a pattern here. The most extreme cases -- a given outcome happening all the time or none of the time, can only occur in one combination. The next step lower, a given outcome happening every time except once, or a given outcome only happening once, can happen in as many combinations as there total events.

# ###6: Calculating the number of combinations

# Now that we've worked out some tables, let's practice a bit.

# ####Instructions

# Find the number of combinations in which 1 day will be sunny. Assign the result to sunny_1_combinations.

# In[5]:

sunny_1_combinations = None
# There are 5 combinations in which one day can be sunny.
# SNNNN
# NSNNN
# NNSNN
# NNNSN
# NNNNS

sunny_1_combinations = 5


# ###7: Number of combinations formula

# In fact, there's an easily quantifiable pattern with the number of combinations. We can calculate the number of combinations in which an outcome can occur k times in a set of events with a formula.
# 
# $\frac{N!}{k!(N-k)!}$
# 
# In this formula, $N$ is the total number of events we have, and $k$ is the target number of times we want our desired outcome to occur. So if we wanted to find the number of combinations in which 4 out of 5 days can be sunny, we'd set $N$ to 5, and $k$ to 4. The $!$ symbol means <a href = "https://en.wikipedia.org/wiki/Factorial">factorial</a>. A factorial means "multiply every number from 1 to this number together". So $4!$ is `1*2*3*4`, which is 24.
# 
# Plugging 4 and 5 into this formula gives us:
# 
# $\frac{5!}{4!(5-4)!}=\frac{5!}{4!(5-4)!}=\frac{1*2*3*4*5}{1*2*3*4(1!)}=\frac{120}{24}=5$
# 
# This matches our intuitive answer that we got earlier!

# ###8: Finding the number of combinations

# We can calculate probabilities greater than or equal to a threshold with our bike sharing data. We found that the probability of having more riders than 4000 is about .6. We can use this to find the probability that in 10 days, 7 or more days have more than 4000 riders.
# 
# But first, let's find the number of combinations in which 7 days out of 10 can have more than 4000 rentals.

# ####Instructions

# Find the probability that 8 days out of 10 can have more than 4000 rentals. Assign the result to combinations_8.
# 
# Find the probability that 9 days out of 10 can have more than 4000 rentals. Assign the result to combinations_9.

# In[6]:

import math

def find_outcome_combinations(N, k):
    # Calculate the numerator of our formula.
    numerator = math.factorial(N)
    # Calculate the denominator.
    denominator = math.factorial(k) * math.factorial(N - k)
    # Divide them to get the final value.
    return float(numerator) / denominator

combinations_7 = find_outcome_combinations(10, 7)
print("combinations_7:", combinations_7)

combinations_8 = find_outcome_combinations(10, 8)
print("combinations_8:", combinations_8)

combinations_9 = find_outcome_combinations(10, 9)
print("combinations_9:", combinations_9)


# ###9: The probability for each combination

# Let's go back to our example about the number of sunny days in Lost Angeles. We can call the probability that a day will be sunny $p$, and the probability that a day won't be sunny $q$.
# 
# $p$ is the probability that an outcome will occur, and $q$ is the complementary probability that the outcome won't happen -- $1-p=q$.
# 
# When we calculate the number of combinations in which a given outcome can occur k times in N events, each of those combinations has a probability of occurring.
# 
# Let's say that for sunny days in Los Angeles, $p$ is .7, and $q$ is .3. If we look at 5 days, there is one combination in which every day is sunny -- `.7*.7*.7*.7*.7`, which equals .168. 
# 
# There are 5 combinations in which only 4 days are sunny -- you can see our table earlier for a closer look. We can calculate the probability of the first combination with `.7*.7*.7*.7*.3`, which equals .072. The probability of the second combination is `.7*.7*.7*.3*.7`, which equals .072. We're multiplying all the same numbers, just in a different order, so this combination has the same probability as the first combination. The probability for each combination in which $k$ of the same outcome can happen in $N$ events is always the same.

# ###10: Calculating the probability of one combination

# Now that we calculated the probability for a single combination occurring, let's practice the calculation a bit more.

# ####Instructions

# Find the probability of a single combination for finding 3 days out of 5 are sunny. The combination is Sunny, Sunny, Sunny, Not Sunny, Not Sunny. Assign the result to prob_combination_3.

# In[7]:

prob_combination_3 = None
prob_combination_3 = .7 * .7 * .7 * .3 * .3


# ###11: Per combination probability formula

# As we learned earlier, the probability for each combination in which $k$ of the same outcome can happen in $N$ events is always the same. Given this, we can calculate the probability of a given outcome happening $k$ times in $N$ events by multiplying the number of combinations in which our result can occur by the probability of a single combination occurring.
# 
# The probability of a single combination occurring is given by $p^{k} * q^{N-k}$. We can verify this with our sunny days example. First, let's find the probability of one combination in which there are 5 sunny days out of 5:
# 
# $.7^{5} * .3^{5-5} = .168 * .3^{0} = .168 * 1 = .168$
# 
# Now, let's find the probability of one combination in which there are 4 sunny days out of 5:
# 
# $.7^{4} * .3^{5-4} = .24 * .3^{1} = .24 * .3 = .072$
# 
# This matches up perfectly with what we did earlier. To find the overall probabilty of 4 days out of 5 being sunny, we just multiply the number of combinations by the probability of any single combination occurring. This gives us .36.

# ###12: Finding the number of combinations

# Now we know enough to find the probability that in 10 days, 7 or more days have more than 4000 riders. The probability of having more than 4000 riders on any single day is about .6. This means that $p$ is .6, and $q$ is .4.

# ####Instructions

# Write a function to find the probability of a single combination occuring. 
# 
# Use it to calculate the probability of 8 days out of 10 having more than 4000 riders. Assign the result to prob_8.
# 
# Use it to calculate the probability of 9 days out of 10 having more than 4000 riders. Assign the result to prob_9.
# 
# Use it to calculate the probability of 10 days out of 10 having more than 4000 riders. Assign the result to prob_10.

# In[8]:

p = .6
q = .4
def find_combination_probability(N, k, p, q):
    # Take p to the power k, and get the first term.
    term_1 = p ** k
    # Take q to the power N-k, and get the second term.
    term_2 = q ** (N-k)
    # Multiply the terms out.
    return term_1 * term_2

prob_8 = find_outcome_combinations(10, 8) * find_combination_probability(10, 8, p, q)
print("prob_8:", prob_8)

prob_9 = find_outcome_combinations(10, 9) * find_combination_probability(10, 9, p, q)
print("prob_9:", prob_9)

prob_10 = find_outcome_combinations(10, 10) * find_combination_probability(10, 10, p, q)
print("prob_10:", prob_10)


# ###13: Statistical significance

# Let's say we've invented a weather control device that can make the weather sunny (if only!), and we decide to test it on Los Angeles. The device isn't perfect, and can't make every single day sunny -- it can only increase the chance that a day is sunny. We turn it on for 10 days, and notice that the weather is sunny in 8 of those.
# 
# We touched on the question of statistical significance before -- it's the question of whether a result happened as the result of something we changed, or whether a result is a matter of random chance. 
# 
# Typically, researchers will use 5% as a significance threshold -- if an event would only happen 5% or less of the time by random chance, then it is statistically significant. If an event would happen more than 5% of the time by random chance, then it isn't statistically significant.
# 
# In order to determine statistical significance, we need to determine the percentage chance that the number of outcomes we saw or greater could happen by random chance.
# 
# In our case, there is 12% chance that the weather would be sunny 8 days out of 10 by random chance. We add this to 4% for 9 days out of 10, and .6% for 10 days out of 10 to get a 16.6% total chance of the sunny outcome happening 8 or more time in our 10 days. Our result isn't statistically significant, so we'd have to go back to the lab and spend some time adding more flux capacitors to our weather control device.
# 
# Let's say we recalibrate our weather control device successfully, and observe for 10 more days, of which 9 of them are sunny. This only has a 4.6% chance of happening randomly (probability of 9 plus probability of 10). This is a statistically significant result, but it isn't a slam-dunk. It would require more investigation, including collecting results for more days, to get a more conclusive result.
# 
# In practice, setting statistical significance thresholds is tricky, and can be highly variable.
