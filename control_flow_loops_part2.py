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
list_of_tatstes = ["sour", "spicy", "sweet"]
# Here, we might want to print: "A pickle is sour", "A pepper is spicy", ... 
# There is a way of connecting, zipping, multiple iterables together: 

for (food, taste) in zip(list_of_foods, list_of_tatstes):
     # At each iteration, we are getting one element of each list, 
     # unpacked, into their respective step variable. 
     print(f"A {food} is {taste}.")

# What if we have three lists? 
list_of_colors = ["green", "red", "red"]
for (food, taste, color) in zip(list_of_foods, list_of_tatstes, list_of_colors):
     print(f"A {food} is {color} and {taste}.")

# enumerate : contais an index that we are working on 
# zip : allows you to combine and unpack each list at each ITERATION : usually only useful with clear one-to-one mapping 

