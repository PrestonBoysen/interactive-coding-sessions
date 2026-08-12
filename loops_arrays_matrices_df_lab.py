# August 11, 2026 
# Study Session for FINAL EXAM 

# Example 1
import numpy as np # import numpy library 
import pandas as pd # import pandas library

prices = [12, 5, 8] # generate a list named prices, with values: 12, 5, 8 
doubled = [] # generate an empty list named doubled 
for p in prices: # looping through lisr prices, take value p
    doubled.append(p*2) # we multiply p by 2, then append the new number to the list: doubled 
    # first iteration, p = 12, doubled beocmes [24]
    # 2nd iteration, p = 5, doubled list becomes [24, 10] 
    # 3rd iteration, p = 8, doubled list becomes [24, 10, 16]
print(doubled) # prints the full new list after the lopp containg [24, 10, 16]

arr = np.array(prices) # create an array from the list prices containing [12, 5, 8], 
# with the dtype (int64)
# shape of array: 
print(arr*2) # print array and multiply each element by 2 (called = VECTORIZED OPERATION) <- more concise, less code to write, faster 


# Example 2: 
temps = [70, 55, 81, 64] 
warm = [] 
for t in temps: 
    if t > 65: 
        warm.append(t)
    # Iterantion 1, t = 70, warm = 70 
    # it 2, t = 55, warm = 70 
    # it 3, t = 81, warm = 70, 81 
    # it 4, t = 64, warm = 70, 81
warm = np.array(warm) # warm now contains an array, with shape 2, 1-D array, dtype: Int
print(warm) # you get [70, 81] 
print(warm - 65) # vecotrized operation, takes each element of array and subtracts 65 [5, 16] 

# Exercise 3 
sales = np.array([30, 12, 45]) # create an array labeled sales with elements [30, 12, 45], shape : 3, dtype: int
for (i, s) in enumerate(sales): # we are looping on enumerate(sales), Index {i}:{s}
    # enumerate give position and variable itself 
    # iteration 1, i = 0, s = 30 
    if s > 20: # checks if element currently being read is greater than 20, 
        print(f"Index {i} : {s}") # if the element is greater it prints 
        # at iteration 1, "index 0:30"
        # at iteration 2, nothing printed 
        # at iteration 3, "Index 3:45"

# Exercise 4: 
data = np.array([3 , 6, 9 ,12]) # dtype: int, shape: 4 
i = 0 
while data[i] < 9: # while loops, loop until condtion is NOT met 
    print(data[i]) # prints element in data at index i 
    i = i + 1 # adds 1 to the current value of i 
    # iteration 1, condition is TRUE, so it prints 3, then increments i by 1, so i = 1 ... (0+1)
    # iteration 2, condition is TRUE, so it prints 6 , then increments i by 1, so i = 2 ... (1+1)
    # iteration 3, condition is FALSE, so it STOPS, prints: nothing, i remains at i = 2 
    # iteration 4, NEVER HAPPENS - STOPS After ITERATION 3 
print(i)

# Exercise 5: 

nums = ([])


# Exercise 6: 
grid = np.array([[5,12],[9,3]]) # 2-D matrix
mask = grid > 6
print(mask) # prints the mask's boolean values for each element 
print(grid[mask]) # prints [12, 9]
print(grid[mask].shape) # prints the shape : 2

# Exercise 7 
orders = np.array([2, 0, 5, 0, 7])
count = 0 # At the end of loop, count should be equal to the non-zero elements in the array orders 
for o in orders: 
    if o > 0: 
        count = count + 1 
print(count) # 
placed = orders > 0 # created a mask named placed, generating bolean values for each element 
print(len(orders[placed])) # print the length of the elements in the array after being masked with placed 
# prints 3 <- 

# Exercise 8***: 
actual = np.array([20, 23, 30])
predicted = np.array([20, 27, 30])
same = actual == predicted 
print(same)

#didnt finish writing

# Exercise 9***:  
names = np.array(["pen", "pad", "ink", "clip"])
stock = np.array ([4, 0, 12, 0])
out = stock 

#didnt finfish writing 

# Exercise 10***: 
scores = np.array([88, 42, 95, 61, ])
false = np.array([])

# didn't finish writing 

# Exercise 11: 
grid = np.array([[5,7],
                 [1,3,],
                 [9,2]])
grid[0, 0] = 99
grid[:, 1] = 0
print(grid)

# Exercise 12: 
grid = np.array([[5, 1, 4], 
                 [2, 8 ,3]])
for row in grid: # when iterating over a matrix you get the row 
    print(row) 
    print(row.sum) 
    # iteration 1, prints the 1st row, then prints the sum of first row
    # iteration 2: prints the 2nd row, then prints the sum of that row 

# Exercise 13: 
units = np.array([[3, 9], 
                  [7, 2], 
                  [5, 5]]) # Matrix that is 3 rows, 2 columns 
print(units.max())
print(units.max(axis=1)) # axis element tells you the dimentsion it collapses, 
# so if axis = 1 it collapses the columns (one per row) 
# if axis = 0, collapses the row (one per column)
for row in units: 
    print(row.max())

# Exercise 14 
grid = np.array([[10, 20, 30], 
                 [40, 50, 60]])
t = grid.transpose()
print(t)
print(grid.shape, t.shape)

# Exercise 15: 
grid = np.array ([[4, 19], 
                  [23, 7], 
                  [11, 2]])
big = grid > 10 
grid[big] = 10 
print(grid)
print(grid.shape)

# Exercis 16 
data = {"Month": ["Jan", "Feb", "Mar"],
                  "Spend":[200, 500, 300]}
df = pd.DataFrame(data)
print(df.shape)
print(df.columns)

# Exercise 17: 
df = pd.DataFrame({"Spend": [200, 500], 
                    "Leads": [10, 20]})
df["Cost"] = df["Spend"] / df["Leads"]
print(df)
print(df.shape)

# Exercise 18: 
df = pd.DataFrame({"Q1": [10, 20, 30],
                   "Q2": [40, 50, 60]}) # create a dataframe with 2 columns and 3 rows 
print(df["Q1"].mean()) # you get the mean of Q1 
print(df.mean()) # one mean per column: Q1, Q2 
print(df.mean(axis=1)) # one mean per row 

# Exercise 19 
sales = np.array([[120, 90, 140],
                  [60, 75, 50]])
per_product = sales.sum(axis=1)
print(per_product)
strong = per_product > 200 # creates another mask 
print(strong) # 
print(per_product[strong])

# Exercise 20 
scores = np.array([[80,90], 
                   [70, 65],
                   [95, 85]])
labels = ["A", "B", "C"]
for (name, row) in zip(labels, scores):
    avg = row.mean()
    if avg >=80:
        print(f"{name}:{avg}")
print(scores.mean(axis=1)) # sum across the columns when axis = 1, so left with one column for each row