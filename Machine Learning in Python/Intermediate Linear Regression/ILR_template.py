
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Machine Learning in Python

# ##Intermediate Linear Regression

# ###1: Introduction to the data

# The Leaning Tower of Pisa is one of the largest tourist attractions in Italy. For hundreds of years this tower slowly leaned to one side, eventually reaching 5.5 degrees off axis, nearly 3 meters horizontal at it's peak. Yearly data was recorded from 1975 to 1987 measuing the tower's lean. In 1988 restoration began on the tower to stop more leaning in the future. The data is provided in the dataframe pisa. The column lean represents the number of meters the tower is off axis at the respective year. In this mission we will try to estimate the leaning rate using a linear regression and interpret its coefficient and statistics.

# ####Instructions

# Create a scatter plot with year on the x-axis and lean on the y-axis.

# In[2]:

import pandas

pisa = pandas.DataFrame({"year": range(1975, 1988), 
                         "lean": [2.9642, 2.9644, 2.9656, 2.9667, 2.9673, 2.9688, 2.9696, 
                                  2.9698, 2.9713, 2.9717, 2.9725, 2.9742, 2.9757]})

pisa.head(5)


# In[3]:

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.scatter(pisa["year"], pisa["lean"])


# ###2: Fit the Linear Model

# From the scatter plot you just made, we visually see that a linear regression looks to be a good fit for the data.
# 
# Statsmodels is a library which allows for rigorous statistical analysis in python. For linear models, statsmodels provides ample statistical measures for proper evaluation. The class sm.OLS is used to fit linear models, standing for oridinary least squares. After the initialization of our model we fit data to it using the .fit() method that estimates the coefficients of the linear model. OLS() does not automatically add an intercept to our model. We can add a column of 1's to add another coefficient to our model and since the coefficient is multiplied by 1 we are given an intercept.

# ####Instructions

# linearfit contains the fitted linear model to our data. Print the summary of the model by using the method .summary(). Do not worry about understanding all of the summary, we will cover many of the statistics in the following screens.

# In[4]:

import statsmodels.api as sm

y = pisa.lean # target
X = pisa.year # features
X = sm.add_constant(X)  # Add a column of 1's as the constant term.

# OLS -- Ordinary Least Squares Fit.
linear = sm.OLS(y, X)

# Fit model.
linearfit = linear.fit()
print("linearfit.summary():\n", linearfit.summary())


# ###3: Define a Basic Linear Model

# We see that the printed summary contains a lot of information about our model. To understand these statistical measures we must start with a formal definition of a basic linear regression model. Mathematically, a basic linear regression model is defined as $y_i = \beta_0 + \beta_1 x_i + e_i$ where $e_i \sim N(0,\sigma^2)$ is the error term for each observation $i$ where $β0$ is the intercept and $β1$ is the slope. The residual for the prediction of observation $i$ is $e_i = \hat{y_i} - y_i$ where $\hat{y_i}$ is the prediction. As introduced previously, $N(0, \sigma^2)$ is a normal distribution with mean 0 and a variance $\sigma^2$. This means that the model assumes that the errors, known as residuals, between our prediction and observed values are normally distributed and that the average error is 0. Estimated coefficients, those which are modeled, will be refered to as $\hat{\beta_i}$ while $\beta_i$ is the true coefficient which we cannot calculated. In the end, $\hat{y_i} = \hat{\beta_0} + \hat{\beta_1} x_i$ is the model we will estimate.

# ####Instructions

# Using linearfit with data X and y predict the residuals. Residuals are computed by subtracting the observed values from the predicted values. Assign the residuals to variable residuals.

# In[5]:

# Predicted values of y.
yhat = linearfit.predict(X)
print("yhat:", yhat)

residuals = yhat - y
print("residuals[:5]:\n", residuals[:5])


# ###4: Histogram of Residuals

# We've used histograms in the past to visualize the distribution of our data. By creating a histogram of our residuals we can visually accept or reject the assumption of normality of the errors. If the histogram of residuals look similar to a bell curve then we will accept the assumption of normality. There are more rigorous statistical tests to test for normality which we will cover in future lessons.

# ####Instructions

# Create a histogram with 5 bins of the residuals using matplotlib's hist() function. The bins parameter allows us to define the number of bins.

# In[6]:

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.hist(residuals, bins=5)


# ###5: Interpretation of Histogram

# Our dataset only has 13 observations in it making it difficult to interpret such a plot. Though the plot looks somewhat normal the largest bin only has 4 observations. In this case we cannot reject the assumption that the residuals are normal. Lets move forward with this linear model and look at measures of statistical fit.

# ###6: Sum of Squares

# Many of the statistical measures used to evaluate linear regression models rely on three sum of squares measures. The three measures include Sum of Square Error (SSE), Regression Sum of Squares (RSS), and Total Sum of Squares (TSS). In aggregate each of these measures explain the variance of the entire model. We define the measures as the following:
# 
# $SSE = \sum_{i=1}^n (y_i - \hat{y_i})^2 = \sum_{i=1}^n e_i^2$. We see that SSE is the sum of all residuals giving us a measure between the model's prediction and the observed values.
# 
# $RSS = \sum_{i=1}^n (\bar{y_i} - \hat{y_i})^2 \text{ where }\bar{y_i} = \dfrac{1}{n}\sum_{i=1}^n y_i$. RSS measures the amount of explained variance which our model accounts for. For instance, if we were to predict every observation as the mean of the observed values then our model would be useless and RSS would be very low. A large RSS and small SSE can be an indicator of a strong model.
# 
# $TSS = \sum_{i=1}^n (y_i - \bar{y_i})^2$. TSS measures the total amount of variation within the data.
# 
# With some algebra we can show that $TSS = RSS + SSE$. Intuitively this makes sense, the total amount of variance in the data is captured by the variance explained by the model plus the variance missed by the model.

# ####Instructions

# Compute the RSS and TSS for our model, linearfit, using the formulas above. Assign the RSS to variable RSS and the TSS to variable TSS.

# In[7]:

import numpy as np

# Sum the (predicted - observed) squared.
SSE = np.sum((yhat-y.values)**2)
print("SSE:", SSE)

# Average y.
ybar = np.mean(y.values)
print("ybar:", ybar)

# Sum the (mean - predicted) squared.
RSS = np.sum((ybar-yhat)**2)
print("RSS:", RSS)

# Sum the (mean - observed) squared.
TSS = np.sum((ybar-y.values)**2)
print("TSS:", TSS)


# ###7: R-Squared

# The coefficient of determination, also known as R-Squared, is a great measure of linear dependence. It is a single number which tells us what the percentage of variation in the target variable is explained by our model.
# 
# $R^2 = 1 - \dfrac{SSE}{TSS} = \dfrac{RSS}{TSS}$
# 
# Intuitively we know that a low SSE and high RSS indicates a good fit. This single measure tells us what percentage of the total variation of the data our model is accounting for. Correspondingly, the $R^2$ exists between 0 and 1.

# ####Instructions

# Compute the R-Squared for our model, linearfit. Assign the R-squared to variable R2.

# In[8]:

R2 = RSS / TSS
print("R2:", R2)


# ###8: Interpretation of R-Squared

# We see that the R-Squared value is very high for our linear model, 0.988, accounting for 98.8% of the variation within the data.

# ###9: Coefficients of the Linear Model

# The ability to understand and interpret coefficients is a huge advantage of linear models over some more complex ones. Each $βi$ in a linear model $f(x) = \beta_0 + \beta_1 x$ is a coefficient. Fortunately there are methods to find the confidence of the estimated coefficients.
# 
# Below we see the summary of our model. There are many statistics here including R-squared, the number of observations, and others. In the second section there are coefficients with corresponding statistics. The row year corresponds to the independent variable x while lean is the target variable. The variable const represents the model's intercept.
# 
# First we look at the coefficient itself. The coefficient measures how much the dependent variable will change with a unit increase in the independent variable. For instance, we see that the coefficient for year is 0.0009. This means that on average the tower of pisa will lean 0.0009 meters per year.

# ####Instructions

# Assuming no external forces on the tower, how many meters will the tower of pisa lean in 15 years? Assign the number of meters moved to variable delta.

# In[9]:

print("linearfit.params:\n", linearfit.params)

delta = linearfit.params["year"] * 15
print("delta:", delta)


# ###10: Variance of Coefficients

# The variance of each of the coefficients is an important and powerful measure. In our example the coefficient of year represents the number of meters the tower will lean each year. The variance of this coefficient would then give us an interval of the expected movement for each year.
# 
# In the summary output, next to each coefficient, you see a column with standard errors. The standard error is the square root of the estimated variance. The estimated variance for a single variable linear model is defined as: 
# 
# $s^2(\hat{\beta_1}) = \dfrac{\sum_{i=1}^n (y_i - \hat{y_i})^2}{(n-2) \sum_{i=1}^n (x_i - \bar{x})^2} = \dfrac{SSE}{(n-2) \sum_{i=1}^n (x_i - \bar{x})^2}$
# 
# This formulation can be shown by taking the variance of our estimated β1^ but we will not cover that here. Analyzing the formula term by term we see that the numerator, SSE, represents the error within the model. A small error in the model will then decrease the coefficient's variance. The denomenator term, $\sum_{i=1}^n (x_i - \bar{x})^2$, measures the amount of variance within x. A large variance within the independent variable decreases the coefficient's variance. The entire value is divided by (n-2) to normalize over the SSE terms while accounting for 2 degrees of freedom in the model.
# 
# Using this variance we will be able to compute t-statistics and confidence intervals regarding this $\beta_1$. We will get to these in the following screens.

# ####Instructions

# Compute $s^2({\hat{\beta_1}})$ for linearfit. Assign this variance to variable s2b1.

# In[10]:

# Compute SSE.
SSE = np.sum((y.values - yhat)**2)
print("SSE:", SSE)

# Compute variance in X.
xvar = np.sum((pisa.year - pisa.year.mean())**2)
print("xvar:", xvar)

# Compute variance in b1 .
s2b1 = (SSE / (y.shape[0] - 2)) / xvar
print("s2b1:", s2b1)


# ###11: T-Distribution

# Statistical tests can be done to show that the lean of the tower is dependent on the year. A common test of statistical signficance is the student t-test. The student t-test relies on the t-distribution, which is very similar to the normal distribution, following the bell curve but with a lower peak.
# 
# The t-distribution accounts for the number of observations in our sample set while the normal distribution assumes we have the entire population. In general, the smaller the sample we have the less confidence we have in our estimates. The t-distribution takes this into account by increasing the variance relative to the number of observations. You will see that as the number of observations increases the t-distribution approaches the normal distributions.
# 
# The density functions of the t-distributions are used in signficance testing. The probability density function (pdf) models the relative likelihood of a continous random variable. The cumulative density function (cdf) models the probability of a random variable being less than or equal to a point. The degrees of freedom (df) accounts for the number of observations in the sample. In general the degrees of freedom will be equal to the number of observations minus 2. Say we had a sample size with just 2 observations, we could fit a line through them perfectly and no error in the model. To account for this we subtract 2 from the number of observations to compute the degrees of freedom.
# 
# Scipy has a functions in the library scipy.stats.t which can be used to compute the pdf and cdf of the t-distribution for any number of degrees of freedom. scipy.stats.t.pdf(x,df) is used to estimate the pdf at variable x with df degrees of freedom.

# In[11]:

from scipy.stats import t
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

# 100 values between -3 and 3.
x = np.linspace(-3,3,100)

# Compute the pdf with 3 degrees of freedom.
print("t.pdf:\n", t.pdf(x=x, df=3))
# Pdf with 3 degrees of freedom.
tdist3 = t.pdf(x=x, df=3)
# Pdf with 30 degrees of freedom.
tdist30 = t.pdf(x=x, df=30)

# Plot pdfs
plt.plot(x, tdist3)
plt.plot(x, tdist30)


# ###12: Statistical Significance of Coefficients

# Now that we know what the t-distribution is we can use it for significance testing. To do significance testing we must first start by stating our hypothesis. We want to test whether the lean of the tower depends on the year, ie. every year the tower leans a certain amount. This is done by setting null and alternative hypotheses. In our case we will say the null hypothesis is that the lean of the tower of pisa does not depend on the year, meaning the coefficient will be equal to zero. The alternative hypothesis would then follow as the lean of the tower depend on the year, the coefficient is not equal to zero. These are written mathematically as,
# 
# $H_0: \beta_1=0$
# $H_1: \beta_1\neq0$
# 
# Testing the null hypothesis is done by using the t-distribution. The t-statistic is defined as,
# 
# $t = \dfrac{\left|\hat{\beta_1} - 0\right|}{s(\hat{\beta_1})}$
# 
# This statistic measures how many standard deviations the expected coefficient is from 0. If $\beta_1$ is far from zero with a low variance then t will be very high. We see from the pdf, a t-statistic far from zero will have a very low probability.

# ####Instructions

# Using the formula above, compute the t-statistic of $\beta_1$. Assign the t-statistic to variable tstat.

# In[12]:

tstat = linearfit.params["year"] / np.sqrt(s2b1)
print("tstat:", tstat)


# ###13: The P-Value

# Finally, now that we've computed the t-statistic we can test our coefficient. Testing the coefficient is easy, we need to find the probability of β1 being different than 0 at some significance level. Lets use the 95% significance level, meaning that we are 95% certian that $\beta_1$ differs from zero. This is done by using the t-distribution. By computing the cumulative density at the given p-value and degrees of freedom we can retrieve a corresponding probability.
# 
# A two-sided test, one which test whether a coefficient is either less than 0 and greater than 0, should be used for linear regression coefficients. For example, the number of meters per year which the tower leans could be either positive or negative and we must check both. To test whether $\beta_1$ is either positive or negative at the 95% confidence interval we look at the 2.5 and 97.5 percentiles in the distribution, leaving a 95% confidence between the two. Since the t-distribution is symmetrical around zero we can take the absolute value and test only at the 97.5 percentile (the positive side).
# 
# If probability is greater than 0.975 than we can reject the null hypothesis ($H_0$) and say that the year significantly affects the lean of the tower. 
# 
# $H_0: \beta_1=0$, Accept if $Tcdf(|t|, df) > 0.975$ else accept $H_1$

# ####Instructions

# Do we accept $\beta_1 > 0$? Assign the boolean value, True or False, to variable beta1_test.

# In[13]:

# At the 95% confidence interval for a two-sided t-test we must use a p-value of 0.975.
pval = 0.975
print("pval:", pval)

# The degrees of freedom.
df = pisa.shape[0] - 2
print("df:", df)

# The probability to test against.
p = t.cdf(tstat, df=df)
print("prob:", p)

beta1_test = p > pval
print("beta1_test:", beta1_test)


# ###14: Conclusion

# Here we learned how to compute and interpret statistics often used to measure linear models. We introduce t-statistics which are used in many field and applications. The assumption of normality is very important in rigorous statistical analysis. This assumption allows each of these statistical tests to be valid. If the assumption is rejected than a different model may be in order.
# 
# R-squared is a very powerful measure but it is often over used. A low R-squared value does not necessarily mean that there is no dependency between the variables. For instance, if $y = sin(x)$ the r-square would equal 0 but there is certianly a relationship. A high r-squared value does not necessarily mean that the model is good a predicting future events because it does not account for the number of observations seen.
# 
# Student t-tests are great for multivariable regressions where we have many features. The test can allow us to remove certian variables which do not help the model signficantly and keep those which do.
# 
# In practice be sure to use the statistics that are most important to your given application and not use ones that could give unreliable results. Following lessons will include statistics such as AIC, BIC, and F-statistic on multivariate linear models.
