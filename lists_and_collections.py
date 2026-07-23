# Talk about Collections. Collections are objects 
# designed to hold other objects inside them. 
# They're loke bags of different kinds. 

# First, Lists. 

# A list, is an ordered collection of items. 
# It is created using, square brackets. 

my_empty_list = [] # This is a list that does not contain anything. 
type(my_empty_list) # A list!  A new kind of object. 
# What do lists do? They contain other objects 

my_favorite_numbers = [1, 2, 3, 4, 5] # This is a list of integers. 
print(my_favorite_numbers)

# Lists can contain other elements! 
my_favorite_colors = ["Red", "Blue", "Green"] # This is a losts of strings! 
my_favorite_decimals = [3.14, 2.718, 1.618] # This is a list of floats! 
my_favorite_booleans = [False, True, False] # Lists can contain repeated elements! 

# Lists can contain different elements of different kinds! 
my_favorite_things = ["red", 3.14, 2, False] 

# You can put anything into a list. Even other lists! 
my_mixed_lists = [False, ["blue", 19], ["Red", False], 3.14]
# Don't be suprised: Lists are very flexible. You can just put a lot of things
# in them. 

# Lists are objects, meaning... 
# Objects contain properties and methods! 

# Let's see some methods of list! 
my_favorite_colors.append('Yellow') # ["Red", "Blue", "Green"]
# This did not print anything. Weird... 
print(my_favorite_colors) # It contains yellow now, a new item was added to it. 

# This method append is SUPER different from all the other methods we saw
#  before, on strings for instance. Why? 

# Because it CHANGED the object directly. It "mutated" the original object. 
# Refresh...
my_string = "Preston"
# What happens if I do: 
my_string.upper() # I run this, it prints a string in upper case. 
print(my_string) # The original string is still in lower case. 
# In technical terms, the method COPIES the original object, changes it, and returns 
# the copy. The original NEVER changed. 

# This is becuase strings are "immutable". Once created, their content will not change. 
# The only way to make changeds to a string is to create a new one with different content. 

# Back to lists: Let's see how methods affect them. 
my_favorite_colors # Contains ["Red", "Blue", "Green", "Yellow"]
print(my_favorite_colors)
# I am going to run the append method to add another color: pink. 
a = my_favorite_colors.append("Pink")
# after I run this line? 
print(my_favorite_colors)
# The method MUTATED the original list. The content was CHNAGED directly by the method. 
# But then what is inside of a? what did the method return? 
print(a) # When you are working with a method that mutates the original, 
# It will typically not return the original. It will simply do something on the original, 
# and return None. 


# VERY CONFUSING - WILL NOT BE ON EXAM - BUT WORTH KNOWING 

# Lets say we don't like that. We don't like the fact that everytime we are adding
# things to my favorite colors, it changes the original. 
my_original_colors = ["Pink", "Purple"]
# I want to add a color to this list, but not modify the original. 
my_updated_colors = my_original_colors # I want this to be my backup. 
# now, I can add something to my_updated_colors, and my_original_colors
# will still exists somewhere. 
my_updated_colors.append("Orange")
print(my_updated_colors) # Sweet! We added a color 
# Now, what of my original colors? 
print(my_original_colors)
# It prints the lists with orange in it! 
# This is because lists are mutable, so when you give lists different names, 
# it still points to the same lists, rather than creating a copy of the list 
# If you don't want that, you need to use the copy() method to create a copy 
# of that list. 

my_original_colors.copy() # This creates an exact identical copy somewhere else

# Back to less confusing things! 
# Other methods with lists: 
my_favorite_colors # ["Red", "Blue", "Green", "Yellow", "Pink"]
# What if you want to remove an element of the list? 
# you can use a method called 'pop'. POP is going to remove the last element of the list
# and returns it to you. 
removed_color = my_favorite_colors.pop()
# What will be the content of my_favorite_colors 
print(my_favorite_colors) # ["Red", "Blue", "Green", "Yellow"]
print(removed_color) # "Pink" 

# WHat if I re-run this line? 
removed_color = my_favorite_colors.pop() # It will remove yellow from the list
# returns it to us, and it will get assigned to remove_color. 

# Something new with lists: If you run the same command multiple times, the behavior
# will change. The list is being mutated, so you are not going to get the same results. 

# What happens if you don't assign the pop color? 
my_favorite_colors.pop() # The lists now contains ["Red", "Blue", "Green"]

# this is a behavior that we've seen before: if a function or a method returns something 
# and we don't "catch" it into a variable, it "falls" into the terminal. 

# Lists are ORDERED, meaning you cna reach into them at a specific position
#  and grab the content. 

my_favorite_names = ["Preston", "Zoe", "Hope"]
# Let's say I want to read what is at the beginning of that list? 
# if you wnat to get an element, you can use an operation called INDEXING 
# # Indexing is: You put the square brackets after the list, and use the Index of the element 
# that you want to grab: 
print(my_favorite_names[1]) # R starts counting from 1, Python from 0. 
# 0 returns the first element, 1 the second, 2 the third... 
print(my_favorite_names[0]) # "Preston"
print(my_favorite_names[2]) # "Hope" 

# What happens if you index [3]? 
print(my_favorite_names[3]) # return an error: Index Error - list index out of range (trying to grab a position that is not there) 

# Contiuing the discussion on INDEXING 
# We can aslo use NEGATIVE indices: 
print(my_favorite_names[-1]) # -1 read the last value. 
print(my_favorite_names[-2]) # The second to last value 

# We can also do something called SLICING to grab multiple values 
# from a list 
my_favorite_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Indexing again first: 
my_favorite_numbers[2] # getting the 0, 1, 2, : Third value of the list. 
# Slicing now: 
# The syntax for slicing is [start:stop:step]. Let's see what that means: 
my_favorite_numbers[0:3:1] # This means: The values 
# between the first and fourth (excluded), and all of them. 
# more examples: 
my_favorite_numbers[1:6:1] # All values bewteen the second and seventh (excluded)
# and all of them 
my_favorite_numbers[3:8:1] # All values between the fourth and eight (or ninth excluded) 
my_favorite_numbers[0:6:2] # all the valuse between first and sixth excluded, taking every other value

# When you are slicing you can omit some arguments: 
my_favorite_numbers[0:3] # By default, step is one (if omitted) 
# this id equivalent to [0:3:1] 
# What about this? 
my_favorite_numbers[1] # all of the valuse starting from one. Both end is omitted (so it defaults
# to 'until the end') and the step is omitted (so it defaults to 1) 
my_favorite_numbers[:4] # Start is omitted (so it defaults to 0, beggining), 
# stop is 4 (meaning until the 4th element, excluded), step is ommitted, so 1: 
my_favorite_numbers[::2] # Start is omitted (so zero), stop is omitted (so until
# the end), and step is 2: every other value in the entire list 
# practice slicing: type slices, and try to predict what you will get. 
my_favorite_numbers[::-1] # Tricky, try to guess! 
# cool trick for reversing a list (counts backwards) 

# Something cool? 
my_name = "Preston Boysen"
my_name_but_mirrored = my_name[::-1]
my_name_but_mirrored # A string is an ordered collection of charachters, 
# so you can slice it like a list. 
my_name[0:4] # just so you know, you can slice strings too. 

# So far, we learned that
# 1) lists are mutable, meaning we can modify their content using methods. 
# 2) lists are ITERABLE, meaning we can select a subset of their content using slices. 

# let's put these two things together! 
my_favorite_names # ["Preston", "Zoe", "Hope"]
# It's weird to have my own name as a favorute. Let's replace it with something else. 
# How could I replace "Preston" by "Adam" in this list? 
my_favorite_names[0] = "Adam" # We are indexing the first element of the list, 
# and aszsigned the value "Adam" at that position. 
my_favorite_names # We have mutated the list! 

# We can do the same thing with slices! 
my_favorite_names[1:] # this is slicing ["Zoe", "Hope"]
my_favorite_names[1:] = ["Eve", "Joshua"]
my_favorite_names # we can use slicing and indexing to read or update
# the content of a list. 

# Bonus Question: Can we use indexing or slicing to update the content of a string? 
my_name[0] = "Z" # Nope, does not work. Strings are not mutable! 
# If you want a new string you need to create a new string. 

# Back to a few list methods: 
my_favorite_names.pop() # Removes the last element of a list 
my_favorite_names.append("Joshua") # add this element at the end of the list 
# pop and append can take an additional argument: The Position! 
my_favorite_names.pop(0) # This will pop the first element, Adam
my_favorite_names.insert(0, "Adam")
# All of these methods are modifying the original list, not returning a copy of the list. 
# Let's try one more: 
my_favorite_names.reverse() # What will this return? 
# It 'returns' nothing: It is changing the order of the original list. 

# Lists are collections of ordered items. 
# Dictionaries are collections of Key:value pairs. 

# let's start with an example 
my_friends_age = {"Nick": 40, "Sam": 35, "Juan": 37}
# Note the syntax: Curly brackets, containing key:value pais, separated by commas 

# Dictionaries can have different kinds of values: 
my_information = {"name": "Preston", "age": 22, "hobbies": ["coding", "skiing", "golfing"]}
# Here you have the key "name" that contains a string value, 
# the key "age" that contains an int value, 
# the key "hobbies" contains a list value. 

# What about the keys in a dictionary? what can they be? 
# They are typically int or str. The most important rules: 
# they have to be UNIQUE (only one key must have a given name)
# and they have to be IMMUTABLE. 

# How to use dictionaries? 
# We can also reach inside them to see the values. That's again called
# 'INDEXING'. For a list, it is ordered, so we index with numbers. 
# What do we index with when you have a dictionary?
 
my_friends_age["Nick"] # How do I get Nick's age? 
# I use square brackets to index, and I give the key for which I want to see the value

# What will I get if I type this? 
my_information["hobbies"]

# Dictionaries, like lists, are mutable. We can update them! 
# Let's say my friend Nick just celebrated his birthday. 
# How do I update his age? 
my_friends_age["Nick"] = 41 # You reach into the dict at the desired key 
# and you assing a new value to it. 
my_friends_age

# Let's try another example. 
# can I cahnge my name to "Preston Boysen"? 
my_information["name"] = "Preston Boysen"
my_information

# Through your mistake, we learned something: *the mistake: originally had "preston", not name 
# we can add new keys to a dictionary! 
# I want to add my job to my information 
my_information['job title'] = "student"
my_information
# We can use indexing to: 
# 1) Read the values of an existing key 
# 2) Update the value of an existing key 
# 3) Create a key with a given value.  

del my_information['Preston'] # can be used to delete, not usedusually tho 

# since dictionaries are OBJECTS... they haev METHODS 
# my_information. 
# First useful method: get() 
# If you index a dictionary with a value that does not exist, what happens? 
my_information["address"]
# If you accidentally check for a value that does not exist, you will get a KeyError
# Errors aren't great when you're writing code, becuase they will stop your code. 
# a better way to check if a key exists is to use method get() 
preston_address = my_information.get("address")
print(preston_address) # This will print None. .get() returns None when the key is not found. 

# Three other useful methods: Rather than blindly checking if a key exists, sometimes you want to see 
# ALL the keys that exist in a dictionary: 
my_information.keys() # check all the keys 
# you can do the same thing to see all the value with... .values() 
my_information.values()
# You can now know all the keys, all the values... but you don't know which each correspond 
# sollution? 
my_information.items()


# Reminder: The keys of dictionaries must be int or str. 
# the values can be anything. so far we've seen: 
# str values 
# int values 
# list values 

# what is very common is to have dictionaries as values, to store complex information. 
# let me give you an example. 
my_friends_info = { 
    "Nick": { # One key, Nick, one value: His dictionary. 
        "age": 41, # Inside that dictionary, other keys (his information) and values (what they are)
        "city": "Boulder", 
        "hobbies": ["skiing", "cooking"]
    },
    "Sam": {
        "age": 35, # Here again, we have key:value pairs containing Sam's information
        "city": "Chicago", 
        "hobbies": ["hiking", "coffee"],
        "job": "professor" 
        } # Another key: Sam, one value: his dictionary of information 
}

# How would we use a dictionary like this? 
# How would you get your friend Nick's information? 
my_friends_info["Nick"]
# We just got Nick's dictionary! 
# Now, how would you get Nick's age from that dictionary?
my_friends_info["Nick"]["age"] # We index Nick's dictionary to get his age, by using the 'age' index 
# How would you get Sam's hobbies? 
my_friends_info["Sam"]["hobbies"]
# What if you're not sure if you have information about a friend's job? 
my_friends_info["Sam"].get("job") # If we do it for Sam, we get: professor
my_friends_info["Nick"].get("job") # If we do it for Nick, we get: Nothing. 

# Mini-Assignment. Sam recently picked up birdwatching. Can you add this hobby to his list of hobbies? 
# Hint: use .append() to add an element to a list. 
my_friends_info["Sam"].get("hobbies")
my_friends_info["Sam"]["hobbies"] # We can verify Sam's Hobbies: 
# This is a list. What do we know about lists? 
# They are mutable: we can modify them in place.  
# We can change their contents, add to it, or remove from it 
# If we grab this list, we can add to it using append: 
my_friends_info["Sam"]["hobbies"].append("birdwatching") # It does not print anything, Nothing gets Returned. 
# can check Sam's hobbies again: (either one below works...)
my_friends_info["Sam"]["hobbies"]
my_friends_info["Sam"].get("hobbies")
# Success! 

# Lists are ORDERED collections of elements of any kind. 
# We manipulate lists using INDEXING or SLICING to access and modify the elements that they contain. 
# We can also use methods like .pop(), .append(), or .insert() to do that. 

# Dictionaries are UNORDERED collectuons of key:value pairs 
# We access their values by their keys 
# We manipulate dictionaries using INDEXING to access and modify the values associated with given keys. 
my_friends_info[0] # There is no key called 0, so it will return a KeyError. 
