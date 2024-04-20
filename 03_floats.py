# ------------> FLOATS (float) <------------
# floats are numbers with a decimal

# lets bring back that calculator again
# this time, type cast the input returns as floats
x = float(input("what is x: "))
y = float(input("what is y: "))
print(x + y)
# notice the decimals in the output

# lets round the result to nearest integer:
# the round() function takes one or two parameters
# first parameter is variable to be rounded,
# second parameter is the number of decimal places to round to
z = round(x + y, 1)
print(z, "(rounded to nearest 1 decimal place)") 

# format with a coma for every hundredth integer using the f-string
print(f"{x} + {y} = {x + y:,} (formatted for every hundredth integer)")
# floats dont have finite amount of decimals because of hardware limitations
# but integers can be of a finite number

# round to nearest decimal places
# round this division to 2 decimal places
d = round(x / y, 2)
print(f"{x}/{y} = {d} (rounded to 2 decimal places)")
# alternatively, for the same result
print(f"{x}/{y} = {d:.2f} (formatted to 2 decimal places)")