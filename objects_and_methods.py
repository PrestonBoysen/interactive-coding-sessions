# First, we recreate a variable or two
this_is_an_integer = 10 
this_is_a_string = "Preston"
# I told you before that you can always see the type of a variable using type() 
type(this_is_an_integer)
type(this_is_a_string)

# Afeter creating a variable in python, you can check all the things 
# that are contained in that variable using the .dot in VSCode 
# After you press the dot, it will reveal a list of things 
# contained in the object. 
# These things come in two flavors: 
# PROPERTIES: signaled by the wrench icon, contains information, data. 
# METHODS: Described by a purple box. Describes all the actions that
# can be performed by the object. 
print(this_is_an_integer.numerator) # 10 
print(this_is_an_integer.denominator) # 1
# properties are describing the state of the object that we created. 
another_integer = 5 
print(another_integer.numerator)
# can we check some properties of the string now? 
print(this_is_a_string) # No properties in there !

# What is really useful are methods. 
# Methods allow us to DO stuff with the objects that we created. 
# They are like afunction, in that they can do things, 
# but theyare specifically attached (we say 'bounded') to the object. 

# Let's check out some methods of this is a string: 
this_is_a_string.upper() # A method require parenthesis, becuase they 
# are actions, they're like a function, so you need to "call" them. 
# all strings will have this method. ALL objects of a given type share the same methods. 
this_is_a_string.lower() # Everything in lowercase 
# We can store the result of that somewhere: 
my_upper_name = this_is_a_string.upper()
print(my_upper_name)
my_upper_name

my_integer = 10 
my_str = "Preston"
# What is stored inside these objects? 
my_str.upper # upper is a METHOD that is attached to all the objects of class str 
# A method is like a function, so it needs to be CALLED. How do we call a function 
# we put () after it 
my_str.upper() # Returning the upper, capitalized version of the string. 
my_str.upper() # What does it mean return a copy? 
# It means the original string is unchanged: 

#lets try another one: 
# what else is in there? 
my_str.endswith('!') # Does not end with a '!' 
my_str.endswith('orld') # returns true! 
# Methods are a way of pairing functions to specific types of objects 

# Some objects have other things thanmethods: Properties. 
# Properties are information about the oject that was created. 
my_integer.denominator 

# Properties are only meant to be read. They don't do anything. They just exist. 
# If something does not require anh calculation to be given to uou, 
# and does not fo anythin, it is probably a property 
# but to be sure: look at the icon 

# Strings comtain a lot of methods 
# becuase there are a. lot of things that we can do with them 
# we've already seen upper(), lower(), title() (capitalizing the first
# letter of each word) 
my_sentence = "hello my name is preston"
my_sentence.title()
# we've also seen 'endswith()'. Here are a few more: 
lots_of_white_space = "        Preston  "
lots_of_white_space.strip()
# practical example of how these methods can be useful 
entry = "     preston.boysen@colorado.edu   "
# this could be something someone entered into a form 
# I want to check if this person has a .edu email address 
is_it_edu = entry.endswith("edu")
is_it_edu # It is false because of the whitespaces! 
stripped_entry = entry.strip()
is_it_edu_for_real = stripped_entry.endswith("edu")
is_it_edu_for_real
# what is its type? boolean? 
type(is_it_edu_for_real) # is a boolean 
# Final thing for this, is that we could write is_it_edu_for_real more cleanly
# Here, we created a new variable with strip(), and then used the 
# endswith() method on this new variable. But we can skip this step: 
is_it_edu_for_real = entry.strip()
# what about ... 
is_it_edu_for_real = entry.strip().endswith('edu')
is_it_edu_for_real
# entry.strip() returns a string, meaning we can directly call 
# the mothod endswith() on this newly created string 

# This is called CHAINING. you call methods on an object that is returned 
# by another method 

# Common errors with methods and properties. 
entry.shout() # AttributeError: no attribute 'shout' 
# you tried to call a method that does not exist on the object. 
price = 12 
type(price)
price.numerator() # TypeError: int object is not callable. 
type(price.numerator) # Numerator is a property of the integer 12, stroed into price. 
# It contains an integer, which is 12 
# But an integer does not do anything – it is not a function or a method. 
# You cannot call it – which is what the not callable is telling you
# The error: attempting to call a property. You can only call a method inside 
# an object. 

# A few more explorations: 
price.is_integer # This is a mehtod: purple box, and it is an action that we are doing. 
# what will happen if I run the previous line? 
# We need the parenthesis to call the method! Otherwise it isn't doing anything. 
price.is_integer() # You get: True 

# So far, we've seen four big types of objects: 
# str, float, int, bool 
# In python, you are often going to create other objects 
# An Object that is going to solve a problem we've had before: 

from decimal import Decimal 
# What is Decimal? it is a factory for manufacturing a new kind of objects: Decimal objects. 
# To create a str, you only needed to put quotes around something. 
# to create a float or an int, you just need to type a float or an int. 
# to create a Boolean, you just need to type True or False, or have a logical comparison. 

# To create Decimal objects, we are going to use the Decimal thingie we just imported. 
a = Decimal(".1")
# We have created a new decimal object, with the value .1 
type(a)
b = Decimal(".2")
type(b)
print(.1 + .2) # What are we gettin? A floating point Error 
# This is because by defualt, Python represents floats with a limited number of zeros 
print (a + b) # if you print the sum of two Decimal objects, you get an exact 
# representation. 
(a + b) == (.1 + .2)
# That's the problem that Decimal is solving. 
a # if you reach into a Deimal object with the dot, you are going to see a lot 
# of new methods nad properties 

