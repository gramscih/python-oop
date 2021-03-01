def greet(name, name2):
    print("Hello {} and {}".format(name, name2))

greet("Jhon", "Steve")

def greet2(*args):
    print("Hello {} {} {}".format(args[0], args[1], args[2]))

greet2("Jhon", "Steve", "Mario", "GHC")


# def greet(name, lastname):
#     print('Hello', name, lastname)

def greet(**kwargs):
    print(type(kwargs))
    print('Hello', kwargs["name"], kwargs["lastname"])

greet(lastname="Snow", name="Jhon", other=123)


# print("arg1", "arg2", "arg3", "arg5")


# Default
def say_hello(name="Dude"):
    print("Hello {}".format(name))

say_hello()
say_hello("GHC")
say_hello(123)
say_hello(object)

#return function
def get_name():
    pass#return "jhon"

print("Hello {}".format(get_name()))


print("arg1", "arg2", "arg3", "arg5")

# my_print("arg1", "arg2", "arg3", "arg5")

#expected result
# arg1 - arg2 - arg3 - arg5
# type(str)

def get_lastname():
    return "GHC"

def say_something():
    lastname = get_lastname()
    print(lastname)


say_something()