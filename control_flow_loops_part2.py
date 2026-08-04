# You can consider this "advanced topics" in loops 

# In a for loop, the thing we are looping over: 
# for x in the _thing_we_are_looping_over is called ITERABE. 
# an Iterable means: something we can unpack into distinctive elements 

#we've also seen some of them: 
# lists are iterable: 
fruits = ["banana", "apple", "mango"]
for f in fruits: 
    print(f)

# we've also seen in strings 
my_word = "Superfragilistic" 
for letter in my_word: 
    print(letter)
# When you loop over a string, you are getting the letters, one by one 

# Dictionaries are iterable: 
my_info = {"name":"Preston", "age": 22, "city": "Boulder"}
for info in my_info:
    print(info) # I am getting the keys of the dictionary, one by one 

# How would I print both the key and the value 
for key in my_info: 
    value =  my_info[key] 
    print(f'The Key is {key} and the value is {value}')

# If I want the value associated wiht the key "name": 
print(my_info["name"])

# There is an even better way that I'm showing you so that you can recognize it: 
my_info.items() # This is giving me each of the  (key, value) pairs in succession. 
# The best news is? We can iterate on that! 

for (key, value) in my_info.items():
        print(f'The Key is {key} and the value is {value}')

# Much simplier example of unpacking 
fruits = ["banana", "apple", "mango"] # This list contains three elements 
my_first_fruit, my_second_fruit, my_third_fruit = fruits 
print(my_first_fruit)

Fruits = ["Banana", "Mango", "Apple"]
# I want to write a loop that prints me: 
# Fruit 1: Banana 
# Fruit 2: Mamgo
# Fruit 3: Apple 

# The first function is called enumerate(): 
for (index, item) in enumerate(Fruits):
     # When, instead of iterating on the ITERABLE directly 
     # we use enumerate(ITERABLE), we are getting both the index, and the element 
     # at each loop. 
     print(f"The element at position {index} is {item}.")

# Final one for today. 
# Lets say we have multiple lists that are somehow connected to each other: 
list_of_foods = ["pickle", "pepper", "cherry"]
list_of_tastes = ["sour", "spicy", "sweet"]
# Here, we might want to print: "A pickle is sour", "A pepper is spicy", ... 
# There is a way of connecting, zipping, multiple iterables together: 

for (food, taste) in zip(list_of_foods, list_of_tastes):
     # At each iteration, we are getting one element of each list, 
     # unpacked, into their respective step variable. 
     print(f"A {food} is {taste}.")

# What if we have three lists? 
list_of_colors = ["green", "red", "red"]
for (food, taste, color) in zip(list_of_foods, list_of_tastes, list_of_colors):
     print(f"A {food} is {color} and {taste}.")

# enumerate : contais an index that we are working on 
# zip : allows you to combine and unpack each list at each ITERATION : usually only useful with clear one-to-one mapping 

for (food, taste, color) in zip(list_of_foods, list_of_tastes, list_of_colors):
     # at each iteration, we are getting one element of each list, 
     # unpacked into their respective step variable. 
     print(f"A {food} is {color} and tastes {taste}.")

# Let's talk about range(). 

for i in [1, 2, 3, 4, 5]: # i is the STEP VARIABLE, [1, 2, 3, 4, ,5] is the ITERABLE. 
     print(i) # i is goint to take, in turn, the value of each of the elements in the iterable 
# Now, imagine we ewnat to get all the numbers 0 to 1000. 
# Writing the loop the old way: 
for i in [0, 1, 2, 3, 4, 5, 1000]: # a bit of  a pain to write
     print(i)
# so, ... enter range() 
# range is a function that creates an iterable for you that you can loop on 
# range takes 3 arguments: start, stop, step 
# start is optional, and defaults to 0
# step is optional, and defaults to 1 
for i in range(1001): # all the numbers between 0 and 1001 excluded. 
     print(i)

# start, stop, step should reminf you of slices: 
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list[0:4]
my_list[::2]

for i in range(0, 1000, 2):
     print(i)

# All there is to know about range: a comvenoent way of gettin 
# an iterable of numbers to loop on 

# The final thing on loops I want to show you is something called 
# list comprehensions. 

# Let say I want the square of all the numbers between 0 and 9: 
# let's write a loop that iterates over nu,bers between 0 and 9, 
# takes the square of each of them, and stores them in a list called my_squares. 

my_squares = [] 
my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
for i in my_numbers:
     square = i**2 
     my_squares.append(square)
print(my_squares)
# could also write as 
my_squares1 = []
for i in my_numbers:
     my_squares1.append(i**2)
print(my_squares1)
# could also write 
my_squares2 = []
for i in range(10):
    my_squares2.append(i**2)
    print(my_squares2) 
print(f"my squares: {my_squares}, my squares 1: {my_squares1}, my squares 2: {my_squares2}")

# this task, creating a new list from an existing iterabke, is EXTREMELY common in Python 
# that's what a shortcut called LIST COMPREHENSSION is doing. 
# here, i could have done the same thing by typing: 
my_squares3 = [i ** 2 for i in range (10)]
# A list comprehension is surrounded by square brackets. This is because we are creating a list. 
# Them, you seen AN EXPRESSION: i ** 2. This defines how the step variable is going to be modified 
# to create the elements of the list 
# Finally, you see the loop itself: for STEP_VARIABLE in ITERABLE. ote, there is no colon here 
print(my_squares3)

my_list = [x.upper() for x in "Preston"] 
my_list

# One final thing on lilst comprehensions: 
# We can add, after the (STEP_VARIABLE in ITERABLE) an optional IF statemente, 
# that filters the elements of the list. 

my_filtered_squares = [i ** 2 for i in range (10) if i ** 2 < 30 ] 
# Only add to the list of the squares are less than 30: 
my_filtered_squares

# very common use case for this filter: 
paths = ["data.csv", "report.pdf", "summary.csv", "image. png", "notes.txt", "data2.csv"]
# lots of files of different types. 
# lets say I just want to keep the .csv files 
my_csv = [i for i in paths if i.endswith(".csv")]
print(my_csv)

# How could I write a for loop that would do the same job 
my_csv = [] 
for path in paths:
     if path.endswith(".csv"):
          my_csv.append(path)
print(my_csv)