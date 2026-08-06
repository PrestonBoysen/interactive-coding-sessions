import pandas as pd

# what is a dataframe? 
# We are going to start from a familiar object to understand what it is and what it does 

data = { 
    "Month": ["Janruary", "Febraury", "March", "April"],
    "Marketing_Spend": [2000, 3000, 2500, 4000], 
    "Sales_Spend": [5000, 7000, 6000, 8000],
    "Leads_Generated": [150, 200, 180, 250]
} # Adictoionary where the keys are the column names 
# and the values are lists, or arrays, containing the column values 
# Most important: ALl these lists/arrays must have the same size. 
# they determine how many rows you have in your data 

# now that we habe this data, we can create a dataframe like so: 
df = pd.DataFrame(data)
print(type(df))

# In pradctice, you are rarely going to type your data into a dictionary and creata dictionary from it
# you are going to read data from files 
df = pd.read_csv("sales_data.csv") # We give relative path of the file we want to read 

# now that we read it, let's see what's in our dataframe. 
print(df) # print the dataframe 
# this dataset is very small, 12 rows only 
# if you print a datafram hundreds of thousands of rows, your terminal might crash 
# instead, it is recommended to inspect a dataset using: "peeking into the dataframe"
print(df.head()) # First five rows 
# for good measure, you can also look at the end of the data 
print(df.tail()) # Last five rows 

# if you want a rich summary of the dataframe, 
# you can use the method info(): 
print(df.info())

# you can access a bunch of these things individually 
print(df.columns) # Note: no parenthisis. This is a property, not a method 
print(df.shape) # Exactly like the matrices we saw: first rows, second is column 
print(df.dtypes) # name of columns and corresponding dtypes 

print(df.index) # the index in a dataframe is "the names of the rows". 
# by default, when you read or create a dataset, the rows are going to be assigned 
# names using a rane(): first raow ill be 0, second will be 1, and so on 

# a dataframe is: 
# an index, containing the name of the columns 
# a list of column names, containing the name of the columns 
# a collection of arrays, mapped to individual column names 
# like a mix of a dictionary and arrays 

# HOW DO YOU INDEX A DATAFRAME. 
# how do you access individual rows and columns of the dataframe 
# for reading and writing data 

# let's first start easy : 
# how do you read the content of a column in a dataframe 
# remember dataframes are a lot like dictionaries 
print(df["Month"]) # you get the column "Month" back
# index by the name of the column, and get the content of the column back 
# a column in a dataframe is called a Series. 
# For intents and purposes, its going to work like 
# an array, with the row indices in front of each value 

print(df["Marketing_Spend"])

# You can ask for the content of multiple columns at once: 
print(df[["Month", "Marketing_Spend"]]) # Note the double brakets, one to index, one to say: 
# a list with multiple elements 
# when you ask for multiple columns, you get a dataframe 

# Much like on arrays, we can then replace the content of a column, or create a new one 
df["Marketing_Spend"] = df["Marketing_Spend"] * 1.1 # We get the content of the column 
# marketing_Spend, multiply it by 1.1, and store it back into the dataframe 

# We can also create new columns 
# to add a new key to a dictionary, we do: my_dict["new_key"] = "value" 
# we use same logic to create a new column in a dataframe 
df["Cost_Per_Lead"] = df["Marketing_Spend"] / df["Leads_Generated"] 
print(df.head())

# we saw how to index columns. Useful! 
# How do we index rows 
# Atypical reason to want to ndex rows is to identify 
# rows that have a specific condition. That's called filtering data

# lets say you want to flag the months (the rows) where the cost_per_lead was cheap: 
# lets say < 15 

# we can create a mask in a dataframe using the same logic as on 1D arrays 

mask = df["Cost_Per_Lead"] < 15
print(mask)

# now that we have the mask. How do we use it? 
# exactly like an array: you inndex the dataframe with the mask: 
print(df[mask]) # returns a dataframe restricted to the rows for which the mask is True 

# Wait, this is very confusing 
# we can index with column names and it works 
# we can also index with a boolean mask on the rows, and it works as well? 

# df["Cost_Per_lead"] <- gives me all the rows for this column only 
# df[mask] <- gives me only the rows where the mask is True, and all the columns 
# it is not supper clean, and potentially confusing to use the smae way of indexing 
# both to get rows nad columns 

# on matrices, we were doing two_d[row_index, col_index]. that was cleaner 

# lets see how we can have the same [row_index, col_index] behavior on a dataframe 

# To do that, you type df.loc[[row_index, col_index]
# For instance, if I want particular columns and all the rows, I type: 
print(df.loc[:, ["Month", "Marketing_spend"]])
# If I want just the wors that I masked, and all the columns, I type: 
print(df.loc[mask, :])
# and if I want jsut one column for the rows I masked, I type: 
print(df.loc[mask, ["Month", "Marketing_Spend", "Leads_Generated"]])

# Final topic: Analyzing data 

# Both DataFrames and Series (series: a single column in a dataframe) contain methods 
# for calculating stuff 

df.loc[:, "Cost_Per_lead"].mean() # The series "Cost_Per_lead" with all the rows 
# .mean() will return the mean cost per lead across all the rows 

df.loc[:, "Leads_Generated"].max() # 300 is the maximum number of leads generated in the data 
# max(), min() value taken across all the values 

# Methods on series work in exactly the same way as methods on arrays: they return the mean(), 
# max(), min() value taken across all the values 

# what if you use these mehtods on DataFrames instead, meaning when you hav multiple columns: 
df.loc[:, ["Marketing_Spend", "Sales_Spend"]].max() # I am getting a dataframe with all the rows and two 
# columns. What happens if I call max() on it? 
# When you call a method like max or min ona. dataframe 
# that has multiple columns, the default behavior is calculating across the rows for each of the columns 
# Here, we are getting the max value for marketing_spend and the max value for sales spend 
# what if i did this now? 
df.loc[:, ["Marketing_Spend", "Sales_Spend"]].sum()# same behavior: We are taking the sum
# across all the rows, for each of the Two columns. We are getting one sum, across the 12 months 
# for marketing_spend, and one sum across the 12 months for sales_spend 

# but waht if instead, i wanted the total spend for each month: 
# Meaning, for each month, the sum of marketing spend and the sum of sales spend for that month 
df.loc[:, ["Marketing_Spend", "Sales_Spend"]].sum(axis=1) # we are collapsing all the columns 
# and keeping the rows. We are taking the sum of marketing + sales spend, for each of the rows 

# now, that we have calcualted this total spend, we might want to save it in our dataframe 
df["Total_Spend"] = df.loc[:, ["Marketing_Spend", "Sales_Spend"]].sum(axis=1)
print(df.head())

# to summarixe again: by default, methods on dataframes are applied across rows, for each of 
# the columns. If we want ot instead apply across columns 
# we use axis=1 as argument 

# We have loaded daata, maipulated the rows and columns, 
# and created two new columns 
# now, lets save our new dataframe into a file 
df.to_csv("Clean_Sales_data.csv", index=False)