# Control flow is a term describing all the tools in python that govern
# whether, when, and how much/often a block of code is going to run. 
# Up until now, every line that we were writing was running 

# First up: Conditional Logic 
# This is what governs whether a block of code is going to be executed. 

my_name = "Preston"
my_gender = "Male" 

if my_gender == "Male": # A conditional logic block always starts with IF
    # followed by a CONDITION: It is a statement that will evaluate to True or False 
    # The line ends wiht a colon : 
    # Then, the line below, you start an indented bock: 
    # This indented block describes the lines of code that will run, 
    # Only IF the condition evaluates to True 
    # For the most simple conditional logic block, that's all you need. 
    # A block with just one if is binary: Either the blovk gets executed (if CONDITION is True) 
    # or isn't (if CONDITION is False) 
    print("Hello Mr " + my_name) 
    # Sometimes the world is more complicated. There's more than one possibility. 
    # That's whereyou can add some bells and whistels to your conditional block 
    # using keywords elif and else. 
elif my_gender == "Female":
    # it describes a second possible condition 
    # that is ONLY going to be checked IF the previous condtions ecaluated to False 
    # It's sequential: We start at the top 
    # we check if the fits condition is True, 
    # it is True, we end here. 
    # If, it is False, we check the second condition 
    # If it is False again, we check the third condition... 
    # We can have zero, one, or many 'elif' statements 
    # allowing you to check additional specific conditions 
    print("Hello Ms " + my_name)
elif my_gender == "Non-Binary":
    print("Hello " + my_name)
else: # Then, at the bottom, after all elif statments (if any) 
    # we can have the 'else' block. The else block means: 
    # if ALL the conditions turned out to be False, 
    # here's what you should do. 
    print("Hello " + my_name + ", how should we address you?")
    # If there is no else statement, nothing happens when all the other conditions 
    # evaluates to False 
# A very common GOTCHA with conditional logic blocks: 
# Conditional logic blocks are vary common inside functions: 
# They allow you to have functions that have a different behavior as a function of their 
# inputs: 

def status_checker(age):
    # We want this function to return the status of the user 
    # as a function of the age that they specify! 
    if age >= 13 :
        return "You are a teenager"
    elif age >= 18 : 
        return "You are an adult"
    elif age >= 4:
        return "You are a child"
    elif age >=2: 
        return "You are a toddler" 
    else: 
        return "You are a baby" 

# Let's check our status Checker function 
status_checker(1) # You are a baby! 
status_checker(3) # You're a toddler! 
status_checker(9) # You're a Child! 
status_checker(14) # You're a teenager! 
status_checker(39) # It returns 'You Are a teenager' 
# Why? the first statement that is check is (39 >= 13) 
# It evaluates to True, the function then returns 'You are a teenager' 
# Let's fix this behavior: 

def correct_status_checker(age):
     # We should simply flip the first two conditions: 
     # Statements are now ordered from MOST to LEAST restrictive 
     # Meaning if a statement is Ture, all the other statments that follow are also True.
    if age >= 18: 
        return "You are an adult"
    elif age >= 13:
        return "You are a teenager"
    elif age >= 18: 
        return "You are an adult"
    elif age >= 4: 
        return "You are a child"
    elif age >=2: 
        return "You are a toddler" 
    else: 
        return "You are a baby" 

# If a conditional logic statment is not behaving as expected, 
# you should always check that the conditions are in order. 

# What happens when you have multiple conditions that you want to check? 

def can_legally_drink(country, age): 
    # The answer cdepends on the country AND the age: 
    # to do that, we can nest conditional logic blocks: 
    # first, we pick one condittion: 
    if country == "USA": 
        # Then, inside the other block, we handle the OTHER condition 
        if age >= 21: 
            return "You can legally drink in the USA" 
        else: 
            return "You cannot legally drink int he USA"
    elif country == "Canada":
        if age >= 19: 
            return "You can legally drink in Canada"
        else: 
            return "You cannot legally drink in Canada"
    elif country == "France":
        if age >= 16: 
            return "You can legally drink in France"
        else: 
            return "You cannot legally drink in France"
    else:
        return "Country not recognized"

can_legally_drink("France", 18)

# Could we write this differntly? Yes! 

def can_legally_drink_with_and(country, age):
    if (country == "USA") and (age >= 21):
        return "You can legally drink in the USA"
    elif (country == "USA") and (age < 21):
        return "You cannot legally drink in the USA"
    elif (country == "Canada") and (age >= 19):
        return "You can legally drink in Canada" 


# Trick 1: When you have a simple condition, you can write a conditional logic block
# in a single line: thats called the "Ternary Operator" 
age = 20 
status = "Adult" if age >= 18 else "Minor" 
# VALUE_IF_TRUE if CONDITION else VALUE_IF_FALSE 

# Second trick, very useful, very common: 
# A use case for conditional logic blocks is when you need to output one value depending on another value 
# let's say I want ot output the currency of a country depending on the ocuntry name 
# of course you can do: 
def get_country_currency(country_name):
    if country_name == "France":
        return "Euro" 
    elif country_name == "USA": 
        return "US Dollar" 
    elif country_name == "Canada": 
        return "Canadian Dollars"
    # Many lines like this 
    else:
        return "unknown country"

# Instead, a better sollution: 
country_currencies = { 
    "USA" : "US Dollars", 
    "France": "Euro", 
    "Canada": "Canadian Dollars",
    "UK" : "British Punds", 
    "Japan": " yen" 
} # this achieves the same structure, with much fewer words: 

# How do we use this then? 
country_currencies["Canada"] # Achives the same goal as a conditional bloack. 
# But it only works if you want to match the same variable to dfferent possible values. 

# One small caveat: 
country_currencies["Iran"] # Here, we get an error. With the function we would get "unkown certainty" 
#...unless we use the .get() method that we saw before! 
country_currencies.get("Iran", "Country not found")
