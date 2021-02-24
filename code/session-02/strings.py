# Differents ways to cancat string
name = "Gramsci"
lastname = "Hermozo"

str_f = "{} {}".format(name, lastname)
str_f_2 = "{0} {1}".format(name, lastname)
str_f_3 = "The lastname from my dad is {1} who got me my name {0}".format(name, lastname)
print(str_f)
print(str_f_2)
print(str_f_3)

str_f_4 = f"{name} {lastname}"
# str_f_5 = name + " " + lastname + 6 not use this way
print(str_f_4)

# Count() function
txt = "This example is for python course for Jalasoft engineers"
x = txt.count("for")

print(x)
print(txt.count("not exits"))

# replace function
txt = "This is a cpp course"
new_txt = txt.replace("cpp", "python")
print(txt)
print(new_txt)

# strip() function
txt = "    Hello World     "
new_txt = txt.strip()
print(txt)
print(new_txt)

txt = "___---___Hello World,,,...."
next_txt= txt.strip("_-,.")

print(txt)
print(next_txt)

# Ex-2.
name = "adolf"
txt = "Adolf not was the only one in his politic, there was other tree adolf’s aDolf Junior, adolF, middle and the big ADOLF."
lower_txt = txt.lower()
num = lower_txt.count(name)
print("[+] The is {} {}'s".format(num, name))

# Upper() function
upper_txt = txt.upper()
print(upper_txt)

# lower() function
upper_txt = txt.lower()
print(upper_txt)

#title()function
full_name = "gramsci hermozo campero"
print(full_name.title())

# split () function
name_list = full_name.split(" ")
wrong_name_list = full_name.split("-")

print(name_list)
print(wrong_name_list)

# find() function
txt = "Hello and welcome to my world"
index = txt.find("welcome")

print(index)

# cast
str_num = "23"
num = int(str_num)
print(str_num, type(str_num))
print(num, type(num))

# len() function

# [] operator
