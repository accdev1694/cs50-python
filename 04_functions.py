# -----------------> FUNCTIONS <---------------------
# if you ever find yourself repeating something over and over, then you need a function

# use the keyword def to define a function, followed by the function name
def hello(to):
    print("hello", to)
# every code block indented under this function belongs to the function hello()
# the hello() function takes some parameters (to)
name = input("what is your name: ")
hello(name)
# call the function with argument of "name"

# you can give functions default values so if the function is called without an arguement,
# it reverts to the default value for an argument
def username(name="Candidate"):
    print(f"Sign Here, {name} (with a default argument)")
    
name = input("Candidate's name Here: ")
username()

# if you call a function, then it must already exist by the time you are calling it
# as a convension, if you are going to have a series of functions, start with the main

def main():
    username = input("what is your name: ")   
    hello(username)
    
def hello(to="Everyone"):
    print(f"hello, {to} (from main)")
    
main()
