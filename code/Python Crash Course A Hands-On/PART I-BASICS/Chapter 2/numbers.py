"""
    Numbers
"""

"""
    Part One 
    Integers
    “You can add (+), subtract (-), multiply (*), and divide (/) integers in Python.”
"""

print(f"2 + 3 = {2 + 3}")
print(f"3 - 2 = {3 - 2}")
print(f"2 * 3 = {2 * 3}")
print(f"3 / 2 = {3 / 2}")

"""
split line for each point
"""
print("------------------------------split line------------------------------")


'''
“Python uses two multiplication symbols to represent exponents:”
'''

print(f"3 ** 2 = {3 ** 2}")
print(f"3 ** 3 = {3 ** 3}")
print(f"10 ** 6 = {10 ** 6}")


"""
split line for each point
"""
print("------------------------------split line------------------------------")


'''
Python supports the order of operations too, 
so you can use multiple operations in one expression. 
You can also use parentheses to modify the order of operations 
so Python can evaluate your expression in the order you specify.
'''

print(f"2 + 3 * 4 = {2 + 3 * 4}")
print(f"(2 + 3) * 4 = {(2 + 3) * 4}")

"""
split line for each part
"""
print("==============================split line==============================")


"""
    Floats
"""
print(f"0.1 + 0.1 = {0.1 + 0.1}")
print(f"0.2 + 0.2 = {0.2 + 0.2}")
print(f"2 * 0.1 = {2 * 0.1}")
print(f"2 * 0.2 = {2 * 0.2}")

"""
split line for each point
"""
print("------------------------------split line------------------------------")

print(f"0.2 + 0.1 = {0.2 + 0.1}")
print(f"3 * 0.1 = {3 * 0.1}")


"""
split line for each part
"""
print("==============================split line==============================")


"""
Integers and Floats
When you divide any two numbers, 
even if they are integers that result in a whole number, 
you’ll always get a float:
"""


print(f"4 / 2 = {4 / 2}")

"""
split line for each point
"""
print("------------------------------split line------------------------------")

'''
If you mix an integer and a float in any other operation, 
you’ll get a float as well: 
'''
print(f"1 + 2.0 = {1 + 2.0}")
print(f"2 * 3.0 = {2 * 3.0}")
print(f"3.0 ** 2 = {3.0 ** 2}")

"""
Finally :
Python defaults to a float in any operation that uses a float, 
even if the output is a whole number.
"""

"""
split line for each part
"""
print("==============================split line==============================")

"""
Underscores in Numbers

When you’re writing long numbers, 
you can group digits using underscores 
to make large numbers more readable:
"""

universe_age = 14_000_000_000
print(universe_age)

"""
Attention
Python ignores the underscores when storing these kinds of values. 
Even if you don’t group the digits in threes, the value will still be unaffected. 
To Python, 1000 is the same as 1_000, which is the same as 10_00. 
This feature works for integers and floats, but it’s only available in Python 3.6 and later.”

"""



