# imports are always at the top of your file: 
import numpy as np # import x as y. x is the library name, y is the shorthand 
# When libraries have short names, like math, we don't use a shorthand: 
import math 
import pandas as pd 

import tensorflow as tf 

# The first thing we are going to do is something we've done once or twice: 
# import a library 
# if a library is not installed, what do we do? UV! 
# in a regular terminal uv add pandas numpy 

# once you've installed and imported a library, you can access it content using 
# the dot notation: 
print(math.pi)
print(math.sqrt(9))

# let's talk about arrays now. Arrays are a new kind of object that live 
# inside the numpy package: 
my_array = np.array([1, 2, 3, 4, 5]) # you create an array, by supplying it a list of elements 
print(my_array) 
# it looks a lot like a list 
# you can index it: 
print(my_array[1])
# you can slice it: 
print(my_array[0:3])
# so whats the difference really?
type(my_array)
# two fundamental differneces between array and lists 
# first difference: an array requires that ALL its elements are of the same type 
my_list = ["Preston", False, 22]
print(type(my_list[0]))
print(type(my_list[1]))
# What if I create an array from this? 
my_array = np.array(my_list)
print(my_array) # All of the elements have been converted to STRing 
# In technical terms, we say they were coerced to a common type. 
# It finds a common type for all the elements to be converted to. 

# Because all elements of an array have the same type, arrays themselves have waht is called a dtype, short for data type: 
print(my_array.dtype)
# Other examples 
float_array = np.array([3.14, 2.16, 1.5])
print(float_array.dtype)
int_array = np.array([1, 2, 3])
print(int_array.dtype)

# second distinction between lists: 
# array have a FIXED SIZE. 
# You cannot add or remove elements from an array after it was created 

my_list = [1, 2, 3, 4, 5]
my_list.pop()
print(my_list) # The pop method has removed the last element of the list. 
my_list.append(6)
print(my_list) # the append method has added an element to the list. 


# What about arrays now? 
my_array = np.array([1, 2, 3, 4, 5]) # I create it here 
my_array.pop() 
my_array.append()
my_array.insert() # all the methods that allow you to insert, remove, or append elemetns to lists 
# do not exists on arrays. 

# Instead you need to use functions to create new arrays 
my_bigger_array = np.append(my_array, 6) # This will create a new array that has the same content 
# as my_array, plus the element 6 appended to the end. 
print(my_array) # Unchanged: still contains 1, 2, 3, 4, 5 
print(my_bigger_array)

# summary: arrays are more constrained. They have to have the same data type 
# they have a fixed length 

# these restrictions enable very powerful things. 

# let me show you: 
# First, lets not use arrays. 
prices = [9.99, 19.99, 4.99, 14.99, 24.99]
quantities = [120, 75, 300, 50, 40]
# I want to calculate, for each product, the total revenue: price * quantity 
# for each of these five products 
# how would I do that? 
totals = [] 
for (p, q) in zip(prices, quantities):
    totals.append(p * q)
print(totals) # you cna't rea;ly see it, but this operation is sloooooowwwwww. 
# What arrays allow you is to do VECTORIZED operations, Ratehr than taking the elements one by one 
# and checking, one by one, if the operation is allows and how it works, 
# all the calculations ar once on all the elements. 

arr_prices = np.array(prices)
arr_quantities = np.array(quantities)
arr_totals = arr_prices * arr_quantities
print(arr_totals) # I cna just multiply the list directly 

# Other examples 
units_jan = np.array([120, 75, 300, 50, 40])
units_feb = np.array([150, 60, 330, 80, 25])
# Units sold for five different products, in JAN and FEB 
totals = units_jan + units_feb
print(totals) 
# How much more or less we sold in FEB compared to JAN 
print(units_feb - units_jan)
# How about the growth rate over the 2 months...
print(units_feb / units_jan)

# A restriction though!! 
units_jan = np.array([120, 75, 300, 50, 40])
units_feb = np.array([150, 60, 330, 80]) # only data for FOUR products! 

print(units_feb - units_jan) # VALUEERROR 
# The two arrays do not have the smae SHAPE 
# the number of elements in an array is called the SHAPE 
print(units_jan.shape)
print(units_feb.shape) # to sum, divide, or multiply two arrays, they need to have compatible shapes
# By the way, this is why we cannot add or remove elements from arrays: We need to know their shape 
# at all times 

# What else can you do with arrays 

# We can comparet them 
units_jan = np.array([120, 75, 300, 50, 40])
units_feb = np.array([150, 60, 330, 80, 25])

feb_sold_more = units_feb > units_jan
print(feb_sold_more)

# you can squaare an array: 
print(units_jan ** 2 ) # again applies the operation in a vectorized way, to each of the elements 

# you can also use the square root (if we are careful to use the numpy version): 
print(np.sqrt(units_jan)) # the numpy library contains special varsions of common math operations 
# that are specifically designed to work with arrays 

# error: We recorded 10 fake transactions for each of the products in JAn 
print(units_jan - 10)

# There are many operations you can apply to arrays... an arrays also have methods 
# that you can inspect! 
units_jan.mean() # you cna call the method mean() to know the mean value of an array... if the array 
# has a numeric dtype 
units_jan.max()
units_jan.std()

# We've already seen that you can index and slice arrays like lists: 
prices = np.array([0, 5, 220, 30, 8])
print(prices[0]) # The first price 
print(prices[0:3]) # the first three prices 
# When you index with a single valu, you get a value of the dtype of the array 
# when you slice an array, you get a new array 

# when working with arrays, like with lists, you cna edit the elements of the arrayL 
# let's replace the first price by 15: 
prices[0] = 15
print(prices)
# What if we want to now make the first two prices equal to 15 and 7? 
prices[0:2] = [15, 7]
print(prices) 
# Arrays are still mutable! We just cannot change thier shape. 

# Everything so far with Indexing and Slicing 
# is identical to what we could do with lists. 

# We can do more powerful stuff with arrays 

# 1. 'MASKING' or "Boolean Indexing" 
# We can index and array with a Boolean array of the same shape 
my_mask = np.array([True, False, True, False, True]) # This is a mask 
prices = np.array([15, 7, 20, 30, 8])
# I have my array, and my mask. 
print(prices[my_mask]) # I can index the prices using the mask: put the mask between square brackets 
# after the array 
# When you index with a mask, you are going to get in return only the values of the array 
# where the corresponding position of the mask is True. 
# Think of overlaying the mask on top of the arary: The True are the cutouts. Any value that is 
# in the cutout is going to be returned. 

# when are the masks useful? 
quantities = np.array([5, 10, 15, -5, -7, 10]) # Quantities cannot be negative, so this array 
# contains some coding errors 
# could we revela a mask that would reveal these errors? 
my_mask = quantities <=  0 # We get a mask: an array of shape 6, that contains True or False elements 
print(my_mask) # Now we have a mask 
# How can we uyse it to spot all the erroneous values in quantities 
print(quantities[my_mask]) # We use the mask to see all the negative values in quantities 
# and get them in an array. 
# Now can we use the mask to replace all of these negative values by 0?
quantities[my_mask] = 0 # You use the maks to HIGHLIGHT all the negative values...
# ... and you assign the value 0 to them. 
print(quantities)

quantities = np.array([5, 10, 15, 0, 0, 10]) # this is the number of customers a coffee shop had
# Monday through Saturday 
# 1. on Average, how many customers did they see on these six days? (reminder: .mean() is a method that gives 
# you the mean of an array). 

# 2. on all the days they saw at least one customer, how many customers did they see on average? 
# A1. 
mean = quantities.mean()
print(mean)
# A2. 
my_mask = quantities >= 1
print(my_mask)
print(quantities[my_mask].mean()) # apply the mask to the array 

# note we could have done that in one line 
quantities[quantities >= 1].mean() # What is between square brackets is the mask, we don't need to store it into a variable first 
# We don't need to store into a variable first 

# final thing with arrays: fancy indexing... and that's pretty fancy
# lets say you have emails from four customers: 
emails = ["preston@colorado.edu", "gal@yale.edu", "puntoni@wharton.edu", "gino@hbs.edu"]
# how do we het the first emails of that list? 
print(emails[0]) # The first email 
print(emails[0:2]) # The first two 
# With lists you can only (i) index with a single value OR (ii) use a slice 
# with arrays, you can index with multiple values 
# that's what fancy indexing is: 
print(emails[[0, 0, 1, 2, 0]]) # you give a LIST of values as an index.. 
# Note the double bracke: First set to index, second set to define the list. 
# If make easier to process, you can break down into two lines: 
my_indices = [0, 0, 1, 2, 0]
print(emails[my_indices])

# why fancy indices? very common: select a random sample of rows in a dataset. 

# lets wrap up on arrays: 

# 1. an array is a new type of iterable. It works a lot like a list 
# 2. Exception 1: Arrays only contain values of the same type. The data type of an array is called its dtype 
# 3. Exception 2: Arrays have a fixed shape. They can't be pop(), append(), or insert(). 
# 4. Thanks to these restrictions, arrays can be added to each other, subtracted from each other, 
# its elements can be multiplied, squared, divided, exponentiated... Whatever you want. These operations 
# are performed on all elements of the array and are much faster 
# 5. Arrays can be compared, element-wise, to create BOolean arrays (also called masks). 
# 6. you can use these masks to filter arrays and re-assign values at specific positions. 
# 7. Arrays, like lists, can be indexed and sliced, both to select and replace values 
# 8. Compared to lists, arrays accept two new forms of indexing: Boolean indexing (only the values facing 
# the true values in the mask are returned), and Fancy indexing (all the indices specified in the list 
# are returned). 
