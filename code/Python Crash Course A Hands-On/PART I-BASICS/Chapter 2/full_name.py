"""
“Using Variables in Strings”

page : 121
"""

first_name = "ada"
last_name = "lovelace"

"""
Attention :
“These strings are called f-strings. 
The f is for format, because Python formats 
the string by replacing the name of any variable 
in braces with its value. ”

"""

full_name = f"{first_name} {last_name}"

# 1
print(full_name)

# 2
print(f"Hello, {full_name.title()}")


# 3
message = f"Hello, {full_name.title()}~!"
print(message)


"""
Attention : 

F-string 需要 Python 3.6 以上的版本才能执行

3.6及以下更早期的版本需要使用 format() 方法


first_name = "ada"
last_name = "lovelace"
message = "{} {}".format(first_name, last_name)
"""

