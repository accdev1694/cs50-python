# Return Value
# where a function does not have a side effect like printing something to the console
# it should return something as a result of its code body

# lets create a version of our calculator from before:
def main(x):
    print(f"the square of {x} is {square(x)}")
# the function square doesnt exist, so we create it
    
def square(n):
    return n ** 2

main(3)
