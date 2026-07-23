# We've been using functions from Day 1: 
# print(), type(), round(), str(), float(), int(), bool(), len()
len("Preston") # Number of elements in a string, or a sequence. 

# What is a function? 
# A function is like a machine: It does someting. 
# It usually takes one or more inputs 
# and usually returns a result 

# print() <- What does it take? 
# Any expression that we want to print 
# What does it do? It prints stuff to the user. 

# str() <- What does it take? 
# It takes any expression 
# What does it do? It turns it into a string, and return it to the other user. 

# What does it mean to RETURN something? 
# Let's take print() as an example 
print("1234") # It is going to print '1234' in the terminal 
my_content = print("1234") 
my_content # my content is empty. print("1234") did not store anything in it. 
# Why? 

# Some functions (most) return something. Think of it like a conveyor belt: 
# They are going to take an object on one side, do things to it, and then RETURN 
# the result of what it did on the other side of the machine. 

# Other function s are just doing stuff: Think t=of them as an engine. 
# you are going to put some gas into them, they are going to do something; 
# but they are not going to hand you back anything. 

# Writing functions practice to understand this distinction. 
# We are going to write a function that takes a price, a rate,a nd areturns 
# the price updated with the rate 

# How do we create a new function? We use this syntax: 
def print_total(price, rate): # def, followed by function name, parenthesis (arguments) 
    # you will see that your cursor moved to the right: 
    # This defines the body of the function. Every code inside 
    # is going to define what the function will do. 
    total = price * (1 + rate) 
    print(total)

# We've created our functions, lets test drive it! 
print_total(10, .1) # Lets run this an practice tracing the code. 
# LEts say I want to store this result for later use: 
my_total = print_total(10, .1)
my_total # Nothing inside my_total. why? lets trace the function back again. 
# this function does not RETURN anything to me as a user It is just doing things. 
# Engine, not conveyor belt. 
# LEts write another function then that solves this ussue 

def calculate_total(price, rate): # same structure as before 
    total = price * (1 + rate)
    return total # On the other side of the conveyor bel, spit out the total 

my_total = calculate_total(10, .1)
print(my_total) # Success, this function calculated something
# RETURNED it back to me, and now I can store it into a variable. 
# What happens if you don't store it? 
calculate_total(10, .1) # Just falls into the terminal and gets printed. 
# ALways better to have functions that RETURN stuff. Gives more flexibility to the user. 

# More vocabulary: The inputs of a function are called ARGUMENTS 
# They come into two flavors: 
# 1. 'Positional Arguments', defined by the order in which you enter them. 
round(3.14, 1) # ROunds the first number to the number of digits in the second number
round(1, 3.14) # Position matters! 

calculate_total(10, .1)
calculate_total(.1, 10) # Positional arguments are expected in a certain order, 
# and are given into a certian order 

# Some functions take a variable number of the arguments. 
round(3.14) # HEre, the second argumnet is not compulsory. It has a default, which is 0. 
print("ABC") # Print ABC 
print("ABC", "DEF", "GHI") # print's ABC DEF GHI 
# Print is an example of a function that takes an arbitrary number of arguments. 
# you can give as many as you want, and its going to print them all. 

# Second flavor of arguments: 'named' arguments, or 'keyword' arguments
# These are arguments that are added by specifying their name: 
print("A", "B", "C", "D", sep="*") # here Sep is a 'Named' argument and I give it the value * 
# Named arguments are not compulsory and have a default value 
# The default for sep is a space 
print("A", "B", "C", "D", sep="-", end ="!") 

# One final but important thing: 

def add_excitment(string): 
    excited_str = string + " !!!!!!!!!!"
    return excited_string
    print("The Function ran successfully.") #Added this 
# Anything after the return will not do anything 

python_is_fun = add_excitment("Python is fun")
python_is_fun