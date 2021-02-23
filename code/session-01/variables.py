# Integer
num_1 = 43

# Float
float_1 = 3.1415

# String
say_hellow = "Hello World" # double quotes
single = 'Hellow World' # Single quotes

print(say_hellow)

name = "Gramsci"
lastname = "Hermozo"
full_name = "{} {}".format(name, lastname)

print(full_name)

# Boolean - Firts letter in uppercase always
b_t = True  
b_f = False

# Null value in python
n = None

# Arithmetic Operators (+, -, *, /, **, //)
x = 15
y = 2

division = x / y
floor_div = x // y
print(f"{x} divided by {y} is equals to {division}") # other way to concat string and variables
print(f"The Integer value from {x} divided by {y} is {floor_div}")

exponent = 2 ** 2
print("exponentiation - {} raised to the power {} is {}".format(2, 2, exponent))

# Logical Operators (and - or - not)

print(b_t and b_f)
print(b_f or b_t)

# Udentity Operator (is - is not)
num_to_val = 34
string_val = "54"
print("Is {} an Integer [{}]".format(num_to_val, type(num_to_val) is int))
print("Is {} an Integer [{}]".format(string_val, type(string_val) is not int))

# Membership Operators (in - not in)
long_string = "Welcome to the January 2021 release of Visual Studio Code. There are a number of updates in this version that we hope you will like."
str_to_search = "2021"

print("Is {} in the long_string [{}]".format(str_to_search, str_to_search in long_string))