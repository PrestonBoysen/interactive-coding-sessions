# Loops are code blocks that are going to run multiple times. 
# We are going to learn, about two different kinds of loops: 
# While loops, and for loops 

# let's start with the while loop: 
count = 0 # Don't worry about for now 
while count < 5: # WHile KeyWord, followed by a CONDITION: A statement that evaluates to True or False 
    print(count) 
    count = count + 1 

# A while loop is going to execute AS LONG AS the condition is True. 
# As soon as the condition becomes False, it will no longer run. 
# That means that the while loop will run zero, one, two, ... infinitely many times. 

# The typical structure of a while loop:
# 0. Initalization: The condition must be equal to something. 
# 1. Inside the loop, something will happend to the condition. 
# If the condition is never changed, the loop will run forever. 

# A very common use case for while loop, is to WAIT until some condition becomes True: 

user_input = "" # Initalization 
while user_input == "": 
    user_input = input("Please enter something:")
    print("you entered " + user_input)

# Let's use a while loop to process a todo list 
to_do = ["laundry", "Dishes", "yard cleaning", "dog walking"] # Initalization: 
while len(to_do) != 0: # As long as there are one iterm or more in the to_do list 
    item = to_do.pop() # Removing the last item of a list, and returns it: 
    print("Now I'm doing this: " + item)

# The skill that we are going to practice, that is important for reading code 
# is called tracing a loop: 
# Understanding, at each iteration, what happens. 
# Iteration 0: After iteration 0, what is item equal to? 'dog-walking'. 
# What is to_do equal to? ['Laundry', 'dishes', 'yard cleaning']
# what is len(to-do) equal to? 3 
# so is the while loop going to run again? 
# Iteration 1: After this loop, what is item equal to? 'yard cleaning' 

# One small detour: 
# Let me tell you about f-strings: 
my_age = 22 
my_name = "Preston"
my_school = "CU Boulder" 
greeting = "Hello, I'm " + my_name + ", I'm " + str(my_age) + ", and I am a grad student at " + my_school
print(greeting)
# This works, nothing wrong with that but: 
# It's ugly and long to write 
# and I need to reme,ber to convert any non-str variable into string before I can add it. 
better_greeting = f"Hello, I'm {my_name}, I'm {my_age}, and I am a grad student at {my_school}."
# adding an f in front of the first quote 
print(better_greeting)
# f-string. 

# Next FOR loops. 
# Remember a while loop is something that checks if a condition is True, 
# and runs for as a long as the condition is True 

# What is a FOR loop? 
# IF is something that ITERATES on an object, and runs as many times as the number of elements 
# in the object. 

for number in [1, 2, 3, 4, 5]: # it starts with the keyword: for
    # then it names a variable, called the 'STEP' varaible 
    # then the in keyword 
    # then an Iterable: something that contains a number of elements. 
    # while the loop is running, 
    # the STEP variable is going to take the value of all the elements 
    # in the iterable, one by one 
    print(f"The number is {number}.")

# a for loop runs a KNOWN number of times: the length of the iterable. 

# Another example: 
for letter in "Preston":
    print(letter)

# HEre the loop was just printing the element. We can do more complicated things! 

list_of_numbers = [1, 2, 3, 4, 5, 6]
for number in list_of_numbers:
    square = number**2
    print(f"The square root of {number} is {square}")

# Lets practice TRACING that loop: 
# Iteration #, number, square 
# First iteration, 1, 1 
# Second, 2, 4 
# Third 3, 9 

# Let's amp up the difficulty slightly 
# Here we were printing the squares. 
# we were not saving them abywhere. 
# lets build another for loop that stores the squares in a new list: 
list_of_numbers = [1, 2, 3, 4, 5, 6]
list_of_squares = [] # This is what will contain our square numbers once we calculate them. 
for numbers in list_of_numbers:
    square = numbers**2 
    list_of_squares.append(square) #Reminder: .append() adds to the exisitng list, 
    # modifying it in place. 

# Iteration #, number, square, list_of_squares 
# First, 1, 1, [1] 
# Second 2, 4, [1, 4]
# Third 3, 9, [1, 4, 9]

# After the loop concludes: 
# Final, 6, 36, [1, 4, 9, 16, 25, 36]
print(list_of_numbers)
print(list_of_squares)

# let's say your confused. you really do no understand how a loop is working: 
# My recommendations? add a print statemnt tracking exactly what is happening 
list_of_numbers = [1, 2, 3, 4, 5, 6]
list_of_squares = [] # This is what will contain our square numbers once we calculate them. 
for numbers in list_of_numbers:
    square = numbers**2 
    list_of_squares.append(square) #Reminder: .append() adds to the exisitng list, 
    # modifying it in place. 
    print(f'"Current Iteration: number is {number}, square is {square}, list_of_squares is {list_of_squares}.')

# EVEry common use case for a for loop: accumulating something. 
list_of_numbers = [4, 8, 15, 23, 42, 9]
# I want to know all these numbers sum to: 
# This is what you get when you add them all, one by one 
total = 0 # very importatn! Otherwise we cannot start adding. 
for number in list_of_numbers: 
    total = total + number
print(f"The sum of {list_of_numbers} is {total}.")
# Let's trace this: 
# Iteration #, number, total 
# First, 4, 4 
# Second, 8, 12 
# Third, 15, 27 
# Final, 9, 101
print(total == sum(list_of_numbers))

# Now lets do a for loop that gets us the MAXIMUM value in a list of numbers 
list_of_numbers = [4, -3, 9, -7, 14, 52]
max_value = -9999999999
for x in list_of_numbers: 
    if x > max_value: 
        max_value = x 
        # If x is SMALLER than our current maximum, we don't care, we move on 

# Iteration #, x, max_value: 
# First, 4, 4
# Second, -3, 4 
# Third, 9, 9 
# Fourth, - 7, 9 
# Fifth, 14, 14
# Sixth, 52, 52 
print(max_value)
print(max_value == max(list_of_numbers))