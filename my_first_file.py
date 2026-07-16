print("Hello World")
print(2+2)
# Here, nothing gets executed when I press enter. 
# How can I run this code? 
# Two ways: 
# 1. You can put the carrot on a line and press shift + enter 
# It is going to send the line to the REPL and run it. 
print("hello world")
# The second way is to "run" the file. 
# Send the entire content of the file to Python, and all the lines will be executed in sequence. 
# Press the run button at the top right of the central panel. a
# You will want to do this once you've finished writing your script. 

# Reminder 1: We can create variables in python and assigna content to them: 
my_name = "Preston Boysen"
print(my_name) # This is printing the content of the variable. 
# Let's send line 16 (print) to the REPL. 
# I get NameError: Normal, I have not defined this variable in the REPL yet. 

# Four big types of data in python 
this_is_an_integer = 10 
this_is_a_float = 3.14 
this_is_a_string = "Hello World!" 
this_is_a_boolean = True or False 

# Print using the print() finction 
print(this_is_an_integer)
print(this_is_a_float)
print(this_is_a_string,this_is_a_boolean)
print(my_non_exisiting_variable)

# print is a function. A function takes between 0 
# and many arguments, and that has a specific behavior. It is an "action". 

# You can print: 
# A value: 
print(3.14)
print("Hello world")
# A Variable: 
print(my_name)
#an expresion, something that has not been calculated yet: 
print(2 + 2) 
# Reminder: Expressions are calculated 'inside out' 
# SKILL: when reading code, try to always understand what is going to happen 
# and in which order. 'Tracing the code': Understanding the steps the machine is taking 
# to arrive at a result. 
print(this_is_an_integer)
print(this_is_an_integer + 5) # Can you trace this? 
# 1. Read the value contained inside the variable: this_is_an_integer 
# 2. Do the operation, here, a sum, between this_is_an_integer (10) and (5) 
# 3. print the result of that operation. 

# How do you figure out the type of a variable: 
what_is_this = type(this_is_an_integer)
print(what_is_this)
# We can also see thst by simply typing the name of the variable we created 
what_is_this
what_is_that = type(3.12)
print(what_is_that)

# Calculations ! 
print(2+ 3)
print(2 + 3*5)
print((2+3)*5) # PEMDAS 

print(1 + 2)
print((1 + 2) == 3) # Double equal: A logical comparison, checking if the elements on the right 
# and on the left have the same value 
# Logical comparisons always have a Boolean. True or False. 
print(0.1 + 0.2) # Wait what?
print((0.1 + 0.2) == 0.3) # Why? 
# Floating Point Error. – When adding floats never expect that they will be exactly equal 
# Do not expect Float operations to be exact 
# What can you do? 
my_rounded_addition = round((0.1 + 0.2), 1)
# the element to be rounded
# The digitws of precision required 
print(my_rounded_addition) # The way to deal with Floating Point Error is to round. 
round(3.14) # Functions can have non-cumpolsory arguments, default arguments. For round, ndigit is equal to 0 
# if not specified. 

# Logical Comparisons: 
print(3 == 5) # Equality Comparison 
print(3 != 5) # Not equal, different
print(3 > 5) # Greater
print(3 < 5)  # Less 
print(3 <= 5) # Less or Equal 
print(3 >= 5) # More or Equal 

# You can combine logical comparisons using AND or OR 
condition_1 = True 
condition_2 = True 
condition_3 = False 
condition_4 = False 
print(condition_1 and condition_2) # True 
print(condition_1 and condition_3) # False 
# AND only returns True when ALL conditions are True. 
print(condition_1 and condition_2 and condition_3) # False 
# What about OR? 
print(condition_1 or condition_2) # True 
print(condition_1 or condition_3) # True 
print(condition_3 or condition_4) # False 
# OR returns True as soon as least one condition is True. 

# let's do a few more calculations! 
print(True + True) # True are 1, False are 0 
print(True == 1)
print(False == 0) 
print(True * 5) # This is 5, becuase for Python True is 1 
# and False is 0 
print(10/0) # cannot divide by 0 
print(10/False) # False is zero. 

# # Let's do some string manipulation. 
# 'Calculations with strings' 

greeting = "Hello " + "world!" 
print(greeting)
# Why does it work? 
# when used with strings, + is interpreted as a 
# "concatentation operator", technical for "putting things"
# next to each other. 
laugh = "ha " * 3
print(laugh)
# For strings, multiplication sign is interpreted as "repeat" 
# operation. 
weird_laugh = "ha " * 3.12
# Be careful when mixing up different types. Sometimes tolerated 
# but often rejeted... and always confusing to read 
very_complicated_laugh = "ha" * ('hello' == 'hello') * 3 
print(very_complicated_laugh) # Don't do that! 
# Keep things simple (stupid) (KISS principle : Keep it simple stupid) 

# How do we keep things simple? We make sure to convert variables 
# before working with them. 

number = 42 
is_this_a_number = "42" 
print(number + 10)
# If you attempt to add a numebr to a string, you will get an error 
print(is_this_a_number + 10) # How do we solve this? 
# Create a new variable 
now_this_is_a_number = int(is_this_a_number)
# int() turns something that is not a number into a number. 
print(now_this_is_a_number)
int("15") == 15
# What would I get if typed this? 
int("fifteen") # You get an Error 
int("Preston") # Also getting an error 
int(False) # This one works! 

# One more example 
my_age = 22 
my_intro = "Hello, my name is Preston and I am " + my_age
# How can I fix this then? 
my_intro_corrected = "Hello, my name is Preston and I am " + str(my_age)
print(my_intro_corrected)
# str(), float(), int(), bool() are functions 
# that can turn an input into the desired type...
# ...assuming this is possible. 