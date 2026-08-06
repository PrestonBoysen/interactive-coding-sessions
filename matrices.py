import numpy as np

# Reminder this is a one-dimensional array: 
one_d = np.array([1, 2, 3, 4, 5]) # Single argument - a list of numbers 
# REmember: We can use the property shape to see the sape of an arrray 
print(one_d.shape)

# the innovation this morning: Introducing 2-d array 
# arrays. A 2-d array is like a matrix with rows and columns 

# How t create a two-d array?
# like this: 

two_d = np.array( # here I also have a single argument 
    [[1, 2, 3],
     [4, 5, 6]]
) # I have a list, that itself contains two lists 
# Each of these inside lists correspond to a row of values in the matrix 

print(two_d) # it shows a matrix with rows and colims 
# How many rows: the number of inside lists 
# How many columns: The number of elements within each list 

print(two_d.shape) 
# The First number is ALWAYS the number of rows 
# The Second number is ALWAYS the number of columns 
# Order: Rows, Columns 

# What happens if we index a Two-dd array 
print(two_d[0])  # You get the first row [1, 2, 3]. Thgis is an array 
# A (one-dimensional array) 
print(two_d[1]) # secind rwo: [4, 5, 6]
 
# So far, its exactly like we saw with lists and one-d array: 
# when you index with a number, you get the corresponding element. 
print(two_d[0:2]) # We get the first and second row. ur original 2-d array. 
# You can also slice a 2-D array, and it works in the same way 

# Waht's new? 
# Since 2-D arrays, have 2-Dimensions, we can use TWO sets of indices 
# The first one for the rows, the second one for the columns: 
print(two_d[0, 0]) # We get 1: the element at the first row and first column 
print(two_d)
print(two_d[1, 1]) # Element at the second row, in the second position is value 5. 

# lets practice: 
print(two_d[0, 0:2]) 
# My prediction: 1, 4
# Actual: 1, 2 (take first, row, then take first two columns)
print(two_d[1, 1:2]) 
# My prediction: 5
# Actual: 5 (take second row (row 1), then take the array of column 2) type is still array 
print(two_d[1:2, 1:3]) 
# My prediction: 5 
# Actual: 5, 6(take row 1, then take column 1 and 2 (not coulmn 0)) # get a 2-D array for type 
print(two_d[-1, -1]) 
# My prediction: 6 
# Actual: 6 (take the last row, and the last column) Type is an integer 

# Pay attention to what you are getting: 
# If you use a slice, you keep the dimension 
# If you use an index, you just get the single element 

# Introducing a new notation: 
print(two_d[:,0]) # just an empty colon, called an empty slice 
# you get all the elements. # All the rows, just column 0 
# This is a One-D array 

# Bigger two-d array to mess around with: 
two_d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]) # This is a square matrix 

# like a  1-D array, we can use slices and indexing to replace values 
# Exercise: replace tthe value 5 by 999 using indexing 
two_d[1, 1] = 999 
print(two_d) 
# Great! Now make the final column be [7, 14, 21]
two_d[:, -1] = [7, 14, 21]
print(two_d)

# Same, logic as on 1-D arrays 
# let's resotre our 2-D array 

two_d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]) 

# 2-D arrays are ARRAYS. Meaning we can do the same thing we 
# saw Tuesday on 1-D arrays. 

# Can you create an array that flags all the value in two_d 
# that are greater than 5 (strictly greater). 

mask = two_d > 5
print(mask)

# Can we use this mask to repalce all the values strictly greater 
# than 5 with 999 
two_d[mask] = 999 
print(two_d)

# Refresher 
a = np.array([1, 2, 3, 4, 5]) # an array 
b = np.array([False, True, True, False, True]) # A mask of the same shape 
a[b] # We can apply the mask to the array and only get the values 
# where the mask is true 
# another thing we say is that we can use Boolean indexing to replace values 
a[b] = 999 
print(a)

# Lets re-create our array 
two_d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]) 

mask = two_d > 5
print(mask)

print(two_d[mask])

# lets re-show a few things that we can do with 2-D arrays: 

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [1, 1],
    [2, 4]
])

# We already saw that when arrays have compatible shapes, we can Sum them: 
print(a + b)
# Subtract them 
print(a - b)
# Multiply them 
print( a * b)
# Divide them 
print(a / b)
# You can add a single number to them 
print(a + 10)

# Final thing: 
one_d = np.array([1, 2, 3, 4, 5])
print(one_d.sum())
print(one_d.max())

# Two-D arrays also have methods...with a small twist 
units_sold = np.array([ 
# How many products of type A, B, C were sold in months Jan, Feb, March, April 
    [120, 150, 130, 170], 
    [75, 60, 90, 80],
    [300, 330, 310, 350]
]) # One thing to mention: When creating an array... all the rows need to have 
# the same number of elements 

print(units_sold) # Rows are product types, Columns are product Months: Jan-Apr 
print(units_sold.sum()) # This is the grand sum, of all the Sum of ALL the products, 
# sold in ALL the months 

# But what about instead... total per product? 
# or total per month? 
# this is where nifty keyword comes in: axis= 
# This is an argument on most array methods 
print(units_sold.sum(axis=0))
# The axis tells us the dimension that we are collapsing. 
# That we are taking the method over. 
# here, we sum the dimension (0) (the rows) and are left with the columns 
# Essentially final sum by Month 
print(units_sold.sum(axis=1)) # Here we do opposite: 
# We take the sum across the columns and are left with the rows: 
# Essentially is the fianl sum of each by type 

# Practice: the method mean() goves you the mean of an array 
# it also takes an optional axis argument 
# use this method to give me the mean units sold in each of the four months 
print(units_sold.mean(axis=0))

# Practice 2: 
# Using method max(), find the best performing product and the 
print(units_sold.max()) # no need for argument, as we don't care about axis, its across all rows and all columns 

# Practice 3: 
# find minimum number of sales for product a across 4 months 
print(units_sold[0, :].min()) # combining indexing and methods to find value 