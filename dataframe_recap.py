import pandas as pd
df = pd.read_csv("Sales_data.csv")

df.head()
df.info()

# to index a dataframe you can use .loc 
df.loc[:, "Marketing_Spend"] # ALL the rows, a single column 
# since I asked for a single column, I get a series: 
# it's like when I index a matrix with a single integer for columns: I get a 1-D array 

# you can also index a dataframe specifying multiple columns: 
df.loc[:, ["Marketing_Spend", "Sales_Spend"]] # I asked for two columns, so I get a dataframe. 

# the one case that may trip you up is this: 
df.loc[:, ["Marketing_Spend"]] # A collection of columns that just contain one. 
# and here, I get a dataframe gain, wiht a single column. 
# It's like when I index a matrix with mat[:, 0:1] 

# if you ask for a single column, ising a string, you get a series 
# if you ask for a collection of columns, using a list, you get a DataFrame, even if the 
# list contains a single element 
