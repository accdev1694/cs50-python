# -- -----------> INTEGERS (int) <-------------------
# integers are positive and negative numbers without decimals
# you can add (+), subtract (-), multiply(*), divide(/) and get the modullo(%) or remainder of division

# Interactive mode in python
# allows you to run python code directly in the terminal
# type python in the terminal and you see >>>> means your are in interactive mode
# there add, subtract, divide and multiply numbers and see results immediately

# Calculator:
x = 2 
y = 3
z = x + y
print(z)            # gives 5

# lets make the calulator more dynamic
# get input of numbers and convert to integer
x = int(input("what is x: "))
y = int(input("what is y: "))
# when you nest or wrap functions inside another function, python
# works from inside out, passing the return value of the inner function as parameter
# for the outer function, in a concentric manner
z = x + y
print(z)
# it turns out that int() is not just a data type but a function used for type casting

# lets get rid of the z variable
print(x + y, "(got rid of z variable)")