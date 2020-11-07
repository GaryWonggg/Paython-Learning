"""
Multiple Assignment

here’s how you can initialize the variables x, y, and z to zero:
>>> x, y, z = 0, 0, 0

You need to separate the variable names with commas,
and do the same with the values,
and Python will assign each value to its respectively positioned variable.
As long as the number of values matches the number of variables,
Python will match them up correctly.

"""

x, y, z = 0, 0, 0
print(f"x = {x}, y = {y}, z = {z}")

"""
split line for each part
"""
print("==============================split line==============================")

"""
Constants
A constant is like a variable whose value stays the same throughout the life of a program. 
Python doesn’t have built-in constant types, but Python programmers use all capital letters 
to indicate a variable should be treated as a constant and never be changed
"""
MAX_CONNECTIONS = 5000
print(f"MAX_CONNECTIONS = {MAX_CONNECTIONS}")

"""
Attention:

When you want to treat a variable as a constant in your code, 
make the name of the variable all capital letters.
"""
