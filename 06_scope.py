# ----------------> SCOPE <--------------------------------
# the concept of scope means that a variable only exists in the context
# within which it is defined

# lets take the previous functions for instance

def main():
    username = input("What is your name: ")
    hello(username)
    
#def hello():
    #print(f"hello, {username} (from main)")
    
#main()
# there is an error because  username is not defined in hello, it is locally scoped to main
# the solution here is to pass in a parameter from the main function and into the hello function (to)

def hello(to="Everyone"):
    print(f"Hello, {to}")
    
main()



