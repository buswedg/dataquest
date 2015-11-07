
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Linear Algebra in Python

# ##Solving Systems of Equations with Matrices

# ###1: Systems of equations

# Let's say that we have two ships. We know the total value of the cargo in each ship's hold, but we don't know how much each item costs. There are two different kinds of items -- fusion reactors, and giant robots.
# 
# We can represent fusion reactors with the variable x, and giant robots with the variable y. The first ship has 2 fusion reactors and 1 giant robot, and the cargo is worth 25 billion dollars. The second ship has 3 fusion reactors, and 2 giant robots, and the cargo is worth 40 billion dollars.
# 
# We can represent this mathematically as a system of equations:
# 
#     2x + y = 25
#     3x + 2y = 40
# 
# This is just rewriting the information we had from before -- 2 fusion reactors plus 1 giant robot equals 25 billion dollars, and 3 fusion reactors plus 2 giant robots equals 40 billion dollars.
# 
# To solve this, we can first multiply the top equation by two:
# 
#     4x + 2y = 50
#     3x + 2y = 40
# 
# This makes sense, because if 2x+y=25 , then it makes sense that 4x+2y=50  -- we're just doubling everything.
# 
# The next step is to subtract the bottom equation from the top equation:
# 
#     x = 10  
# 
# This tells us that x is 10, which means that a fusion reactor is worth 10 billion dollars. We can perform this subtraction because both equations are true statements -- thus subtracting one from the other also yields a true statement.
# 
# Now that we know that x equals 10, we can substitute that value into the bottom equation to solve for y:
# 
#     3∗10 + 2y = 40  
# 
# Which simplifies to:
# 
#     2y = 10  
# 
# And finally:
# 
#     y = 5  
# 
# So, fusion reactors are worth 10 billion dollars each, and giant robots are 5 billion dollars each.

# ###2: Systems of equations as matrices

# We've worked a bit with matrices before, and the very cool thing about systems of equations is that we can represent them the same way.
# 
# Our equations above could be represented as a matrix:
# 
# $\left[\begin{array}{rr|r}
# 2 & 1 & 25 \\ 
# 3 & 2 & 40
# \end{array}\right]$
# 
# This is just a matrix that contains the coefficients and constants in the equations we have. We called this an augmented matrix, because it has both the constants and the coefficients -- the line separates them, with constants to the right.
# 
# This matrix has two rows (each of which represents an equation in the system), and 3 columns. The first column represents x, the second represents y, and the third is the constants in the equations (the right of the = sign).
# 
# The underpinnings of linear algebra are systems of equations, but we generally work with matrices like this because they are simpler to represent.
# 
# The simplest way to represent a matrix in python is a numpy array. A numpy array can have rows and columns, just like a matrix.

# ####Instructions

# Multiply the first row of the matrix by two.
# 
# Then subtract the second row from the first row.
# 
# Then, subtract three times the first row from the second row.
# 
# Finally, divide the second row by 2 to get rid of the coefficient.
# 
# At the end, the first row should indicate that x equals 10, and the second row should indicate that y equals 5. We just solved our equation with matrices!

# In[2]:

import numpy as np

# Set the dtype to float to do float math with the numbers.
matrix = np.asarray([
    [2, 1, 25],
    [3, 2, 40]  
], dtype=np.float32)
print("matrix:\n", matrix)

# Multiply the first row by two.
matrix[0] *= 2
print("matrix:\n", matrix)

# Subtract the second row from the first row.
matrix[0] -= matrix[1]
print("matrix:\n", matrix)

# Subtract three times the first row from the second row.
matrix[1] -= (3 * matrix[0])
print("matrix:\n", matrix)

# Divide the second row by two.
matrix[1] /= 2
print("matrix:\n", matrix)


# ###3: Gauss's method

# We just used Gauss's Method to solve systems of linear equations, but we didn't explicitly state what it is. Gauss's method is pretty simple, and just states that:
# If a linear system is changed to another by one of the following operations:
# 
#     (1) an equation is swapped with another
#     (2) an equation has both sides multiplied by a nonzero constant
#     (3) an equation is replaced by the sum of itself and a multiple of another
# 
# then the two systems have the same set of solutions.
# 
# This is how we can transform our systems of equations through swapping and multiplying, and solve the system. It's because our simplified representation leads to the same solutions as the more complex initial system.

# ###4: Solving more complex equations

# We looked at a pretty simple system of equations beforehand, but we can extend our methods to even solve more complex systems.
# 
# $\left[\begin{array}{rrr|r}
# 1 & 1 & 0 & 0 \\ 
# 2 & -1 & 3 & 3 \\
# 1 & -2 & -1 & 3
# \end{array}\right]$
# 
# In this system, we have three variables (first column is x, second is y, and the third is z). We also have three equations that we can manipulate.
# 
# The first thing we can do is subtract 2 times the first row from the second row:
# 
# $\left[\begin{array}{rrr|r}
# 1 & 1 & 0 & 0 \\ 
# 0 & -3 & 3 & 3 \\
# 1 & -2 & -1 & 3
# \end{array}\right]$
# 
# Then we can subtract the first row from the third row:
# 
# $\left[\begin{array}{rrr|r}
# 1 & 1 & 0 & 0 \\ 
# 0 & -3 & 3 & 3 \\
# 0 & -3 & -1 & 3
# \end{array}\right]$
# 
# Then, we can subtract the second row from the third row:
# 
# $\left[\begin{array}{rrr|r}
# 1 & 1 & 0 & 0 \\ 
# 0 & -3 & 3 & 3 \\
# 0 & 0 & -4 & 0
# \end{array}\right]$
# 
# This tells us that z equals 0. We can substitute into the second row to solve for y:
# 
# $\left[\begin{array}{rrr|r}
# 1 & 1 & 0 & 0 \\ 
# 0 & -3 & 0 & 3 \\
# 0 & 0 & 1 & 0
# \end{array}\right]$
# 
# This tells us that y equals -1. We can substitute into the first equation to solve for x:
# 
# $\left[\begin{array}{rrr|r}
# 1 & 0 & 0 & 1 \\ 
# 0 & 1 & 0 & -1 \\
# 0 & 0 & 1 & 0
# \end{array}\right]$
# 
# Now, we have everything solved!

# ####Instructions

# Solve for x, y, and z in matrix. When you're done, the matrix should look like this, except with the right answers substituted for the question marks:
# 
# $\left[\begin{array}{rrr|r}
# 1.0 & 0 & 0 & ? \\ 
# 0 & 1.0 & 0 & ? \\
# 0 & 0 & 1.0 & ?
# \end{array}\right]$
# 
# You can use print(matrix) to print the matrix out as you solve it and assess your progress.

# In[3]:

import numpy as np

matrix = np.asarray([
    [1, 2, 0, 7],
    [0, 3, 3, 11],
    [1, 2, 2, 11]
], dtype=np.float32)
print("matrix:\n", matrix)

# Subtract the first row from the third row.
matrix[2] -= matrix[0]
print("matrix:\n", matrix)

# Divide the third row by 2.
matrix[2] /= 2
print("matrix:\n", matrix)

# Subtract three times the third row from the second row.
matrix[1] -= (matrix[2] * 3)
print("matrix:\n", matrix)

# Divide the second row by three.
matrix[1] /= 3
print("matrix:\n", matrix)

# Subtract two times the second row from the first row.
matrix[0] -= (2 * matrix[1])
print("matrix:\n", matrix)


# ###5: Echelon form

# A leading variable is the first variable with a nonzero coefficient in a row. Echelon form is what happens when the leading variable of each row is to the right of the leading variable in the previous row. Any rows consisting of all zeros should be at the bottom.
# 
# Here's an example of a matrix representing a system of linear equations in echelon form:
# 
# $\left[\begin{array}{rrr|r}
# 1 & 0 & 1 & 5 \\ 
# 0 & 5 & 7 & 10 \\
# 0 & 0 & 1 & 4
# \end{array}\right]$
# 
# Here's another example of a matrix in echelon form:
# 
# $\left[\begin{array}{rrr|r}
# 1 & -1 & 1 & 5 \\ 
# 0 & 5 & 0 & -2 \\
# 0 & 0 & 2 & -5 \\
# 0 & 0 & 0 & 0
# \end{array}\right]$
# 
# And here's a matrix that isn't in echelon form:
# 
# $\left[\begin{array}{rrr|r}
# 1 & 1 & 0 & 0 \\ 
# 2 & -1 & 3 & 3 \\
# 1 & -2 & -1 & 3
# \end{array}\right]$
# 
# Getting a matrix into echelon form makes a system of linear equations much easier to solve. This is where row swapping can come in handy.

# ####Instructions

# Swap rows to get matrix into echelon form. matrix[[0,2]] = matrix[[2,0]] will exchange the first and the third rows.

# In[4]:

matrix = np.asarray([
    [0, 0, 0, 7],
    [0, 0, 1, 11],
    [1, 2, 2, 11],
    [0, 5, 5, 1]
], dtype=np.float32)
print("matrix:\n", matrix)

# Swap the first and the third rows - first swap.
matrix[[0,2]] = matrix[[2,0]]
print("matrix:\n", matrix)

# Second swap.
matrix[[1,3]] = matrix[[3,1]]
print("matrix:\n", matrix)

# Third swap.
matrix[[2,3]] = matrix[[3,2]]
print("matrix:\n", matrix)


# ###6: Reduced row echelon form

# Generally, the way to solve systems of linear equations is to first try to get them into reduced row echelon form. We just covered echelon form. reduced row echelon form meets all the same conditions as echelon form, except every leading variable must equal 1, and it must be the only nonzero entry in its column.
# 
# Here's an augmented matrix in reduced row echelon form. Note that coefficients and constants are treated separately, so constants don't have to follow the guidelines for reduced row echelon form:
# 
# $\left[\begin{array}{rrr|r}
# 1 & 0 & 0 & 0 \\ 
# 0 & 1 & 0 & 3 \\
# 0 & 0 & 1 & 0
# \end{array}\right]$
# 
# Here's a regular matrix in reduced row echelon form:
# 
# $\begin{bmatrix}
# 1 & 0 \\ 
# 0 & 1
# \end{bmatrix}$
# 
# Generally, to get to reduced row echelon form, we repeat the following steps:
# - Start on a new row
# - Perform any needed swaps to move the leftmost available leading coefficient to the current row
# - Divide the row by its leading coefficient to make the leading coefficient equal 1
# - Subtract the row from all other rows (with an appropriate multiplier) to ensure that its leading variable is the only nonzero value in its column.
# - Repeat until entire matrix is in reduced row-echelon form.

# In[5]:

A = np.asarray([
        [0, 2, 1, 5],
        [3, 0, 1, 10],
        [1, 2, 1, 8]
        ], dtype=np.float32)
print("A:\n", A)

# First, we'll swap the second row with the first to get a nonzero coefficient in the first column.
A[[0,1]] = A[[1,0]]
print("A:\n", A)

# Then, we divide the first row by 3 to get a coefficient of 1.
A[0] /= 3
print("A:\n", A)

# Now, we need to make sure that our 1 coefficient is the only coefficient in its column.
# We have to subtract the first row from the third row.
A[2] -= A[0]
print("A:\n", A)

# Now, we move to row 2.
# We divide by 2 to get a one as the leading coefficient.
A[1] /= 2
print("A:\n", A)

# We subtract 2 times the second row from the third to get rid of the second column coefficient in the third row.
A[2] -= (2 * A[1])

# Now, we can move to the third row, but it already looks good.
# We're finished, and our system is solved!
print("A:\n", A)


# ###7: Inconsistency

# Not all systems of equations can be solved. In the cases where they can't, we call the system inconsistent. An inconsiste system will have two or more equations that conflict, making it impossible to find a solution. Here's an example:
# 
# $\left[\begin{array}{rr|r}
# 8 & 4 & 5 \\ 
# 4 & 2 & 5
# \end{array}\right]$
# 
# We can divide the first row by 2:
# 
# $\left[\begin{array}{rr|r}
# 4 & 2 & 2.5 \\ 
# 4 & 2 & 5
# \end{array}\right]$
# 
# There's no way that $4x+2y=2.5$ and $4x+2y=5$, so we would consider this an inconsistent system. Inconsistent systems have no solutions.

# ####Instructions

# Find whether A is consistent. Assign True to A_consistent if it is, False if it isn't.
# 
# Find whether B is consistent. Assign True to B_consistent if it is, False if it isn't.

# In[6]:

A = np.asarray([
    [10, 5, 20, 60],
    [3, 1, 0, 11],
    [8, 2, 2, 30],
    [0, 4, 5, 13]
], dtype=np.float32)

B = np.asarray([
    [5, -1, 3, 14],
    [0, 1, 2, 8],
    [0, -2, 5, 1],
    [0, 0, 6, 6]
], dtype=np.float32)

# Divide first row by 10.
A[0] /= 10

# Subtract 3 times the first row from the second.
A[1] -= (3 * A[0])

# Subtract 8 times the first row from the third.
A[2] -= (8 * A[0])

# Multiply the second row by -2.
A[1] *= -2

# Subtract .5 times the second row from the first.
A[0] -= (A[1] * .5)

#  Subtract -2 times the second row from the third.
A[2] -= (A[1] * -2)

# Subtract 4 times the second row from the fourth.
A[3] -= (A[1] * 4)

# Divide the third row by 10.
A[2] /= 10

# Subtract -4 times the third row from the first.
A[0] -= (A[2] * -4)

# Subtract 12 times the third row from the second.
A[1] -= (A[2] * 12)

# Subtract the third row times -43 from the fourth.
A[3] -= (A[2] * -43)

# A is in row echelon form, and we have a unique solution, so it is consistent.
A_consistent = True

# Divide the fourth row by 6.
B[3] /= 6

# Subtract -2 times the second row from the third row.
B[2] -= (B[1] * -2)

# Divide the third row by 9.
B[2] /= 9

# The last variable (z) cannot simultaneously equal 1.88 and 1, so B is inconsistent.
B_consistent = False


# ###8: Infinite solutions

# We've seen cases in which systems of equations have zero solutions, or one solution. There's one other case we need to worry about: sometimes, systems have infinite solutions. This ususally happens when we're unable to simplify an equation enough that each variable is alone in a row. In these cases, there are free variables, which do not lead any rows, and leading variables, which do. We express the values of the leading variables using the free variables.
# 
# Here's an example:
# 
# $\left[\begin{array}{rrr|r}
# 1 & 1 & 0 & 0 \\ 
# 2 & -1 & 3 & 3
# \end{array}\right]$
# 
# We can simplify, and subtract two times the first row from the second:
# 
# $\left[\begin{array}{rrr|r}
# 1 & 1 & 0 & 0 \\ 
# 0 & -3 & 3 & 3
# \end{array}\right]$
# 
# Now we're stuck -- we're in echelon form, but we can't simplify any more. 
# 
# x and y are the leading variables, and z is the free variable, because it doesn't lead any rows. Thus, we can express x and y in terms of z.
# 
# We start with the second row, and get:
# 
# $\begin{array}{lllcl} -3y & + & 3z & = & 3 \end{array}$
# 
# $\begin{array}{lllcl} y & - & z & = & -1 \end{array}$
# 
# $\begin{array}{lllcl} y & = & z & - & 1 \end{array}$
# 
# So, we have expressed y in terms of z. We can now do the same with x. First, we substitute the value for y into the first row:
# 
# $\begin{array}{lllcl} x & + & (z-1) & = & 0 \end{array}$
# 
# $\begin{array}{lllcl} x & = & 1 & - & z \end{array}$
# 
# This system of equations has infinite solutions, because z could take on any value -- we don't have any way to simplify any more. Since we have chosen to express y and x in terms of z, z is called a parameter. Not all free variables have to be parameters -- you can choose which ones to use when expressing a leading variable.

# ####Instructions

# Check whether A has infinite solutions. If it does, assign True to A_infinite, otherwise assign False.
# 
# Check whether B has infinite solutions. If it does, assign True to B_infinite, otherwise assign False.

# In[7]:

A = np.asarray([
        [2, 4, 8, 20],
        [4, 8, 16, 40],
        [20, 5, 5, 10]
], dtype=np.float32)

B = np.asarray([
        [1, 1, 1, 4],
        [3, -2, 5, 8],
        [8, -4, 5, 10]
        ], dtype=np.float32)

# Divide the first row in A by 2.
A[0] /= 2

# Subtract the first row times 4 from the second row.
# This zeros out the row
A[1] -= (A[0] * 4)

# Subtract the first row times 20 from the last row.
A[2] -= (A[0] * 20)

# Now we're stuck -- we can't simplify A any more, so it has infinite solutions.
A_infinite = True

# B -- Subtract the first row times 3 from the second row.
B[1] -= (B[0] * 3)

# Subtract the first row times 8 from the third row.
B[2] -= (B[0] * 8)

# Divide the second row by -5.
B[1] /= -5

# Subtract the second row from the first.
B[0] -= B[1]

# Subtract the second row times -12 from the third row.
B[2] -= (B[1] * -12)

# Divide the last row by -7.8 (the third column element).
B[2] /= B[2,2]

# Subtract the third row times the third column of the first row from the first row.
B[0] -= (B[2] * B[0][2])

# Subtract the third row times the third column of the second row from the second row.
B[1] -= (B[2] * B[1][2])

# B is solveable, and has a single solution -- it is not infinite.
B_infinite = False


# ###9: Homogeneity

# A linear equation is homogeneous if it has a constant of zero. Here's an example:
# 
# $4x+2y−4z=0$
# 
# These equations are special, because they can always be solved by setting the value of each variable to zero.
# 
# A system of linear equations is homogeneous if all the equations have a constant of zero.
# 
# $\left[\begin{array}{rrr|r}
# 1 & 1 & 0 & 0 \\ 
# 0 & -3 & 3 & 0 \\
# 1 & -7 & 4 & 0 \\
# \end{array}\right]$
# 
# A system of equations that is homogeneous always has at least one solution -- setting each variable to zero will always solve the system.

# ###10: Singularity

# A matrix is square if it has the same number of columns as rows. Here's a square matrix:
# 
# $\begin{bmatrix}
# 1 & 1 & 0 \\ 
# 0 & -3 & 3 \\
# 1 & -7 & 4 \\
# \end{bmatrix}$
# 
# A square matrix is nonsingular if it represents a homogenous system with one unique solution. When we represent a homegeneous system, we can skip showing the coefficients, because we can assume that they are zero. Here's a nonsingular matrix:
# 
# $\begin{bmatrix}
# 1 & 2 \\ 
# 3 & 4
# \end{bmatrix}$
# 
# This is nonsingular because when we simplify it, we find that x and y both are zero. First, we subtract three times the first row from the second row.
# 
# $\left[\begin{array}{rr|r}
# 1 & 2 & 0 \\ 
# 0 & -2 & 0
# \end{array}\right]$
# 
# So, we have −2y=0 , which simplifies to y=0 .
# 
# $\left[\begin{array}{rr|r}
# 1 & 2 & 0 \\ 
# 0 & 1 & 0
# \end{array}\right]$
# 
# Then, we can subtract two times the second row from the first row:
# 
# $\left[\begin{array}{rr|r}
# 1 & 0 & 0 \\ 
# 0 & 1 & 0
# \end{array}\right]$
# 
# This tells us that both x and y must equal zero.
# 
# A square matrix is singular if it represents a homogeneous system with infinite solutions. Here's an example:
# 
# $\begin{bmatrix}
# 1 & 2 \\ 
# 3 & 6
# \end{bmatrix}$
# 
# This is singular because we can't simplify it past a certain point. Let's try this. First, we subtract 3 times the first row from the second row:
# 
# $\left[\begin{array}{rr|r}
# 1 & 2 & 0 \\ 
# 0 & 0 & 0
# \end{array}\right]$
# 
# We have zeroed out the whole second row. We can't simplify this anymore, so all we have is $x+2y=0$. Infinite solutions will work for this, including $x=0$, $y=0$, $x=2$, $y=−1$, and $x=6$, $y=−3$.
# 
# The concept of singularity will be very important down the line, as we look into inverting matrices.
