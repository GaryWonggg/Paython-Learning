"""
Adding Whitespace to Strings with Tabs or Newlines
In programming, whitespace refers to any non printing character,
such as spaces, tabs, and end-of-line symbols.
You can use whitespace to organize your output so it’s easier for users to read.”

"""


"""
Add a Tab  \t
"""

print("Python")
print("\tPython")

"""
split line for each point
"""
print("------------------------------split line------------------------------")


"""
Add new line \n
"""

print("Languages:\nPython\nC\nJavaScript")

"""
Also could be like  \n\t
"""
print("Languages:\n\tPython\n\tC\n\tJavaScript")


"""
split line for each part
"""
print("============================split line===================================")


"""

Stripping Whitespace


Extra whitespace can be confusing in your programs. 
To programmers 'python' and 'python ' look pretty much the same. 
But to a program, they are two different strings. 
Python detects the extra space in 'python ' 
and considers it significant unless you tell it otherwise.

"""


favorite_language = "Python "       # 1
print(favorite_language)            # 2
print(favorite_language.rstrip())   # 3
print(favorite_language)            # 4

"""

The value associated with favorite_language at #1 contains extra whitespace at the end of the string. 
When you ask Python for this value in a terminal session, 
you can see the space at the end of the value #2. 
When the rstrip() method acts on the variable favorite_language at #3, this extra space is removed. 
However, it is only removed temporarily. If you ask for the value of favorite_language again, 
you can see that the string looks the same as when it was entered, including the extra whitespace #4.

"""


"""
split line for each point
"""
print("------------------------------split line------------------------------")


"""

To remove the whitespace from the string permanently, 
you have to associate the stripped value with the variable name

"""
favorite_language = "Python "
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)


"""
split line for each point
"""
print("------------------------------split line------------------------------")


"""

You can also strip whitespace from the left side of a string using the lstrip() method, 
right side of a string using the rstrip() method,
and from both sides at once using strip()

"""
favorite_language = ' Python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

