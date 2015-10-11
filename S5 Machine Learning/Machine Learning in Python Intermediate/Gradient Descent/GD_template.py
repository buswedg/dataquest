
# coding: utf-8

# In[2]:

from IPython.display import HTML

HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>''')


# #Machine Learning in Python
# ##Gradient Descent

# ###1: Introduction to the data

# We have a dataset pga.csv containing professional golfers' driving statistics in two columns, accuracy and distance. Accuracy is measured as the percentage of fairways hit over many drives. Distances is measured as the average drive distance, in yards. Our goal is to predict accuracy using distance. In golf, it's expected that the further someone hits the ball the less accurate they will be. Lets see if this holds up.
# 
# For many machine learning algorithms it's important to scale, or normalize, the data before using it. Here we have distance, measured in yards, and accuracy, measured in percentages. These two fields are on very different scales which can produce bias into learning algorithms. Many algorithms compute the Eucilidean Distance between two observations and if one of the features is vastly larger than another, the distance will be biased towards that particular feature. To normalize the data, for each value, subtract each the mean and then divide by the standard deviation.
# 
# After normalizing the data, we plot the data to get a visual sense of the data.

# In[3]:

import pandas
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

# Read data from csv
pga = pandas.read_csv("data/pga.csv")

# Normalize the data
pga.distance = (pga.distance - pga.distance.mean()) / pga.distance.std()
pga.accuracy = (pga.accuracy - pga.accuracy.mean()) / pga.accuracy.std()

print(pga.head())

plt.scatter(pga.distance, pga.accuracy)
plt.xlabel('normalized distance')
plt.ylabel('normalized accuracy')
plt.show()


# ###2: Linear model

# From this plot, the data looks linear with a negative slope, lower accuracy with higher distance. We can use a linear model, as shown in previous missions, to model this data. This model is written as accuracyi=θ1distancei+θ0+ϵi where θ's are coefficients and ϵ are error terms. To start, lets use sklearn's LinearRegression class to estimate a linear model.

# ####Instructions

# Fit a linear model where distance is the independent variable and accuracy is the dependent variable. Use the sklearn class LinearRegression and assign the coefficient of distance to theta1.

# In[5]:

from sklearn.linear_model import LinearRegression
import numpy as np

# We can add a dimension to an array by using np.newaxis
print("Shape of the series:", pga.distance.shape)
print("Shape with newaxis:", pga.distance[:, np.newaxis].shape)

# The X variable in LinearRegression.fit() must have 2 dimensions
lm = LinearRegression()
lm.fit(pga.distance[:, np.newaxis], pga.accuracy)
theta1 = lm.coef_[0]


# ###3: Cost function, introduction

# We utilized a pre-existing library sklearn to estimate the coefficients of our linear model, using least squares. The least squares method can effectively fit linear models since it only requires matrix algebra and provides deterministic estimates of the coefficients. Least squares is a method which directly minimized the sum of square error in a model algebraically. Often times we have too much data to fit into memory and we can't use least squares.
# 
# Gradient descent is a general method that can be used to estimate coefficents of nearly any model, including linear models. At it's core, gradient descent minimizes the residuals in the estimated model by updating each coefficent based on it's gradient.
# 
# To start we must understand cost functions. Most cost functions measure the difference between a model predictions and it's corresponding observations with the coefficients as parameters. Lets say our model is hθ(x)=θ1x+θ0.
# 
# The cost function is then defined as, J(θ0,θ1)=12m∑mi=1(hθ(xi)−yi)2. The cost here is one half the average difference between our prediction and observation squared. As we change the coefficients of the model this cost changes. During modeling we will randomly choose the coefficients and update them intelligently to minimize this cost.

# ####Instructions

# Compute the cost for each theta1 in theta1s and theta0=100. Create a plot with theta1s on the x-axis and the corresponding costs on the y-axis.

# In[6]:

get_ipython().magic(u'matplotlib inline')

# The cost function of a single variable linear model
def cost(theta0, theta1, x, y):
    # Initialize cost
    J = 0
    # The number of observations
    m = len(x)
    # Loop through each observation
    for i in range(m):
        # Compute the hypothesis 
        h = theta1 * x[i] + theta0
        # Add to cost
        J += (h - y[i])**2
    # Average and normalize cost
    J /= (2*m)
    return J

# The cost for theta0=0 and theta1=1
print(cost(0, 1, pga.distance, pga.accuracy))

theta0 = 100
theta1s = np.linspace(-3,2,100)
costs = []
for theta1 in theta1s:
    costs.append(cost(theta0, theta1, pga.distance, pga.accuracy))

plt.plot(theta1s, costs)


# ###4: Cost function, continued

# The cost function above is quadratic, like a parabola, with respect to the slope and we can see there is a global minimum. A global minimum is the point where the function has the lowest value. We need to find the best set of parameters to minimize the cost function, but here we are only varying the slope and keeping the intercept constant. The minimum of the cost function is the point where the model has the lowest error, hence the point where our parameters are optimized. Instead we can use a 3D plot to visualize this cost function where the x and y axis will be the slope and intercept and the z axis will be the cost.

# ####Instructions

# Make a 3D surface plot with theta0s on the x-axis, theta1s on the y-axis, and the corrsponding cost on the z-axis. use the cost function provided above. Assign each cost into the repsective index in variable cost.

# In[7]:

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
get_ipython().magic(u'matplotlib inline')

# Example of a Surface Plot using Matplotlib
# Create x an y variables
x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)

# We must create variables to represent each possible pair of points in x and y
# ie. (-10, 10), (-10, -9.8), ... (0, 0), ... ,(10, 9.8), (10,9.8)
# x and y need to be transformed to 100x100 matrices to represent these coordinates
# np.meshgrid will build a coordinate matrices of x and y
X, Y = np.meshgrid(x,y)
print(X[:5,:5],"\n",Y[:5,:5])

# Compute a 3D parabola 
Z = X**2 + Y**2 

# Open a figure to place the plot on
fig = plt.figure()
# Initialize 3D plot
ax = fig.gca(projection='3d')
# Plot the surface
ax.plot_surface(X=X,Y=Y,Z=Z)

plt.show()

# Use these for your excerise 
theta0s = np.linspace(-2,2,100)
theta1s = np.linspace(-2,2, 100)
COST = np.empty(shape=(100,100))
# Meshgrid for paramaters 
T0S, T1S = np.meshgrid(theta0s, theta1s)
# for each parameter combination compute the cost
for i in range(100):
    for j in range(100):
        COST[i,j] = cost(T0S[0,i], T1S[j,0], pga.distance, pga.accuracy)

# make 3d plot
fig2 = plt.figure()
ax = fig2.gca(projection='3d')
ax.plot_surface(X=T0S,Y=T1S,Z=COST)
plt.show()


# ###5: Cost function, slopes

# Gradient descent relies on finding the direction of the largest gradient where a gradient is the "slope" of a multivariable function. To find this gradient we can take the partial derivative in terms of each parameter in the cost function. A partial derivative represents the slope of a multivariable function in terms of a single parameter, ie. holding all other variables constant, what is the slope in the direction of the one parameter. In the case of this cost function, we will take the partial derivatives in terms of theta0 and theta1. Visually, looking at the 3D plot above, we want to find the slope of the function in the direction either the x or y axis. If you are not familiar with derivatives do not worry, we will not require you to derive any in this lesson. Most importantly we must remember that we are just finding the incline of a function relative to each parameter.
# 
# ∂J(θ0,θ1)∂θ0 is read as the partial derivative of J(θ0,θ1) in terms of θ0. This is not part of the equation but just the representation of partial derivatives.
# 
# The partial derivative of the cost function in terms of theta0 is: ∂J(θ0,θ1)/∂θ0=1m∑mi=1(hθ(xi)−yi).
# 
# The partial deriviate of the cost function in terms of theta1 is: ∂J(θ1)/∂θ1=1m∑mi=1(hθ(xi)−yi)∗xi
# 
# We've written the code to compute the partial derivative in terms of theta1 below. theta0 and theta1 are inputs to the function to give a reference point of where to take the derivative from. x is our feature vector and y are the observed, target, values. We then find the error between our observations and hypothesised model and multiply by x. The average of all these terms is then the partial derivative. This function gives us the slope in the direction of the θ1 coefficient.

# ####Instructions

# Write a function named partial_cost_theta0(theta0, theta1, x, y) to compute ∂J(θ0,θ1)/∂θ0. theta0 and theta1 are initial parameters of the linear model, x is our feature vector (distance) and y are the observations (accuracy). Assign the partial derivative where theta0=1, theta1=1, x=pga.distance, and y=pga.accuracy to variable partial0.

# In[8]:

def partial_cost_theta1(theta0, theta1, x, y):
    # Hypothesis
    h = theta0 + theta1*x
    # Hypothesis minus observed times x
    diff = (h - y) * x
    # Average to compute partial derivative
    partial = diff.sum() / (x.shape[0])
    return partial

partial1 = partial_cost_theta1(0, 5, pga.distance, pga.accuracy)
print("partial1 =", partial1)
# Partial derivative of cost in terms of theta0
def partial_cost_theta0(theta0, theta1, x, y):
    # Hypothesis
    h = theta0 + theta1*x
    # Difference between hypothesis and observation
    diff = (h - y)
    # Compute partial derivative
    partial = diff.sum() / (x.shape[0])
    return partial

partial0 = partial_cost_theta0(1, 1, pga.distance, pga.accuracy)


# ###6: Gradient descent algorithm

# Visually, we see that by varying our slope and intercept we get drastically different costs. In order to minimize the error between our hypothesised model and observations we can find the minimum of the cost function by changing the parameters. Gradient descent is a widely used method to find the optimal parameters. To execute gradient descent we randomly initialize a set of parameters and update them by moving in the direction of the cost function's steepest slope, ie. the descending down the function. If we can find the downward slope in terms of each parameter we can move in the direction of the global minumum. Eventually the updates will converge to a near optimal set of parameters. When parameters converge the hypothesised parameters become very close to the optimal parameters. We measure convergence by finding the difference between the previous iterations cost versus the current cost.
# 
# The general gradient descent algorithm for two variables is:
# 
# 
# repeat until convergence {
#        θ1:=θ1−α∗∂J(θ0,θ1)∂θ0
#        θ0:=θ0−α∗∂J(θ0,θ1)∂θ1
# }
# 
# Let's go through this term by term. θ1 is the current value of our coefficient, ie. how much accuracy is lost per yard of distance. α is the learning rate. This value is set by the user and controls how fast the algorithm will converge by changing the parameters by some percentage of the slope. Values of this learning rate can vary from project to project but in general learning rates can be between 0.0001 and 1. This value must not be too large or the algorithm will overshoot the minimum but if it's too small it will take many iterations to converge. ∂J(θ0)∂θ1 is the partial derivative of our cost function in terms of θ0 and ∂J(θ1)∂θ1 is the partial derivative of our cost function in terms of θ1. These measure the partial derivatives in relation to our coefficients. Since we want to minimize the cost function we substract the partial derivatives times some learning rate from our coefficients to get our new set of coefficients.
# 
# We will start by initializing a few variables. updates will store our convergence data for visualization later. theta0 and theta1 will hold initial values of the slope and intercept. alpha is used for our learning rate. Finding a learning rate is often done by trial and error. A good starting point is 0.01. If you find that the algorithm is learning too slowly it can be increased. If the cost starts increasing out of control then the learning rate is probably overshooting the minimum and should be decreased. We will then use the max_epochs to limit the number of iterations so it doesn't run forever. c will be used to hold the initial cost using the initial parameters.

# ####Instructions

# Execute the gradient descent algorithm with alpha=0.01, x=pga.distance, and y=pga.accuracy. Make a plot of costs on the y-axis and the iteration (0 to len(costs)) on the x-axis.

# In[9]:

get_ipython().magic(u'matplotlib inline')

# x is our feature vector -- distance
# y is our target variable -- accuracy
# alpha is the learning rate
# theta0 is the intial theta0 
# theta1 is the intial theta1
def gradient_descent(x, y, alpha=0.1, theta0=0, theta1=0):
    max_epochs = 1000 # Maximum number of iterations
    counter = 0      # Intialize a counter
    c = cost(theta1, theta0, pga.distance, pga.accuracy)  ## Initial cost
    costs = [c]     # Lets store each update
    # Set a convergence threshold to find where the cost function in minimized
    # When the difference between the previous cost and current cost 
    #        is less than this value we will say the parameters converged
    convergence_thres = 0.000001  
    cprev = c + 10   
    theta0s = [theta0]
    theta1s = [theta1]

    # When the costs converge or we hit a large number of iterations will we stop updating
    while (np.abs(cprev - c) > convergence_thres) and (counter < max_epochs):
        cprev = c
        # Alpha times the partial deriviative is our updated
        update0 = alpha * partial_cost_theta0(theta0, theta1, x, y)
        update1 = alpha * partial_cost_theta1(theta0, theta1, x, y)

        # Update theta0 and theta1 at the same time
        # We want to compute the slopes at the same set of hypothesised parameters
        #             so we update after finding the partial derivatives
        theta0 -= update0
        theta1 -= update1
        
        # Store thetas
        theta0s.append(theta0)
        theta1s.append(theta1)
        
        # Compute the new cost
        c = cost(theta0, theta1, pga.distance, pga.accuracy)

        # Store updates
        costs.append(c)
        counter += 1   # Count

    return {'theta0': theta0, 'theta1': theta1, "costs": costs}

print("Theta1 =", gradient_descent(pga.distance, pga.accuracy)['theta1'])
descend = gradient_descent(pga.distance, pga.accuracy, alpha=.01)
plt.scatter(range(len(descend["costs"])), descend["costs"])
plt.show()


# ###7: Conclusion

# Gradient descent is a widely used algorithm for computing local and global minimum in functions. Here we showed that gradient descent produced nearly identical results as least squares. As your data becomes larger and more complex gradient descent can aid in parameter optimization. Looking forward, we will use a modified gradient descent to teach neural networks.
