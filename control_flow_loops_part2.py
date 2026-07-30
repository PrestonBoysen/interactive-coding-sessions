# You can consider this "advanced topics" in loops 

# In a for loop, the thing we are looping over: 
# for x in the _thing_we_are_looping_over is called ITERABE. 
# an Iterable means: something we can unpack into distinctive elements 

#we've also seen some of them: 
# lists are iterable: 
fruits = ["banana", "apple", "mango"]
for item in fruits: 
    print(item)

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
     