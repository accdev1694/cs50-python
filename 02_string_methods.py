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
print(f"{name}, your name has been capitalized")

# string.title
name = name.title()
# type in more than one name
print(f"{name}, your name is title-cased")
# returns first character of each string upper cased

# Combine functions - string.strip().title()
name = input("what is your name: ").strip().title()
print(f"{name}, your name is stripped, and title cased")


