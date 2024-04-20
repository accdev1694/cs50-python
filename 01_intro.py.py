# ---------------- >>> STRINGS (str) <<< -----------------------

# write my first program
print("hello, world")           
# type python hello.py to run the code
# prints "hello, world" to the console

# python command is calling the python interpreter to run the program by
# converting the command to computer language

# FUNCTIONS
# they are like actions or verbs that help us do something on the computer

# ARGUEMENTS
# string of instructions inside a function that predtermines its behaviour#

# SIDE EFFECTS
# what gets printed on the screen

# BUGS
# mistakes in a program

# INPUT
# the variable input has a return value that you then store in a variable and use in greeting
# input returns a string
name = input("what is your name? ")
print("hello, " + name)

# VARIABLES
# a reusable container to store values in a computer program
# "name" above is a variable-name
# "=" is an assignment operator - copies from right to left, whatever the users input is
# whatever the return value of the input function is, gets assigned as the value of the variable


# COMMENTS
# notes to self or other programmers
# doesnt get executed by the interpreter
# begins with "#" for single line comments
# begins and ends with ''' or """ for multi-line comments

# PSEUDOCODE
# a to do list for your program
# uses comments to create
# line by line,  natural human language, step by step what the program does or
# how it is to be structured
# breaks a big program doen into small byte-sized steps

# MULTIPLE PARAMETERS
# if you seperate the input parameters to a function with a comma, 
# you can pass in multiple parameters into that function
print("Hello", name)
# when you pass in multiple arguments seperated with commas, 
# it automatically inserts a space for you


# THE PRINT FUNCTION DOCUMENTATION
# print(*objects", sep=' ', end="\n")
# The print function moves your cursor to the next line after execution
# but you can override that behaviour by setting the end='\n' to ""
# it says after execution at the end, move the cursor to new line.
# \ is an excape; n is new line. set end=""
print("hello ", end=" ")
print(name)

# the sep parameter in the documentation says seperate 
# each parameter with spaces or whitespaces

# POSITIONAL VS NAMED PARAMETERS
# Positional parameters we pass ourselves inside brackets and they get executed in order
# Named parameters are inbuilt like "sep, end, *objects" from the print docs

# CORNER CASE FOR PARENTHESIS
# if you want to print a quotation imside  the string quotes
print("Hello, \"David\"", ) # or
print("Hello, 'David'")

# F- STRINGS
# use format or f strings to add variables or placeholders to print
print(f"My name is {name}")



# STRING METHODS

# string.strip()
# this method removes whitespaces from before and after the string
name = input("What is your name: ")
name = name.strip() 
print(f"{name}, your name has been stripped")    
# add some spaces before and after your name input

# string.capitalize()
name = name.capitalize()
# returns an upper case character for the first character
print(f"{name}, your name has been capitalize()")

# string.title
name = name.title()
# type in more than one name
print(f"{name}, your name is title()")
# returns first character of each string upper cased

# Combine functions - string.strip().title()
name = input("what is your name: ").strip().title()
print(f"{name}, your name is strip(), and title()")

# string.split()
# the split function takes in an input of the position of split()
name = name.split(" ")
print(f"Welcome {name[0]}, your name has been split()")
# you can also assign the split name to different variables




