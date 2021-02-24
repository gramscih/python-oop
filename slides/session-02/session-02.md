---
title: Object Oriented Programming with Python
author: Gramsci Hermozo
institute: Session 02
theme: Copenhagen
colortheme: seahorse
---

# Content
+ Strings
+ Lists
+ Tuple
+ Dictionaries
+ Functions

# String
## Ex-1.Concatenate
```python
name = "Gramsci"
lastname = "Hermozo"

# concatenate your name and lastname and print
full_name = ""
```
__Output:__
```bash
Gramsci Hermozo
```

# String
## Most common functions
**format()**
```python
"{}".format(var)
"{0} {1}".format(var, var1)
f"{<var_name>}"
```

# String
## Most common functions
**count()**
```python
txt = """
      This example is for python course
      for Jalasoft engineers
      """
# returns a number of times a specified
# value appears in the string
x = txt.count("for")
```
**output:** 2

# String
## Most common functions
**replace()**
```python
txt = "This is a cpp course"
new_txt = txt.replace("cpp", "python")
print(new_txt)
```
**output:**
```
This is a python course
```

# String
## Most common functions
**strip()**
```python
txt = "   Hello World    "
new_txt = txt.strip()
print(new_txt)
```
**output:**
```
Hello World
```

# String
## Ex-2. Count
As a crazy politician, I would like to know, 
how many times is mentioned my Name into this post.
My name is Adolf 

**Post**

Adolf not was the only one in his politic, 
there was other tree adolf's aDolf Junior, 
adolF, middle and the big ADOLF.


# List
**Create a List**
```python
my_list = ["Python", "is", "so", "cool"]
print(my_list)
```

# List
## Most common functions
**len()**
This function returns the size of a list
```python
my_list = ["C", "Pascal", "Javascript"]
print(len(my_list))
```
**output:**
```
3
```

# List
## Most common function
**Access List Items**
```python
my_list = ["cpp", "python", "c#"]
print(my_list[1])
```
**output:**
```
banana
```

# List
## Most common functions
**insert(index, value)**
```python
my_list = ["This", "a", "list"]
my_list.insert(1, "is")
print(my_list)
```
**output:**
```
["This", "is", "a", "list"]
```

# List
## Most common functions
**append(value)** 
This funciton add an item into the end of the list.
```python
my_list = ["c#", "java", "c#"]
my_list.append("python")
print(my_list)
```
**output:**
```
["c#", "java", "c#", python]
```

# List
## Most common functions
**remove(value)**
```python
list = ["dog", "cat", "mouse", "lion"]
list.remove("mouse")
```
**pop()**
```python
list = ["dog", "cat", "mouse", "lion"]
list.pop(2)
```
**del**
```python
list = ["dog", "cat", "mouse", "lion"]
del list[2]
```
**clear**
```python
list = ["dog", "cat", "mouse", "lion"]
list.clear()
```

# List
## Ex-3. Concatenate lists (who I am)
I had a transit accident and I don't remember my name
help me please!!
```python
memory_1 = ["M", "na", "i", "Jo", "Bla"]
memory_2 = ["y", "me", "s", "e", "ck"]
```
**Expected Result**
```python
['My', 'Name', "is", 'Joe', 'Black']
```

# List/String
## Ex-4. Need numbers
A crazy trainer returns my grade into single string and I need
to know the total and the average
```txt
"English=68 Logic=75 Uml=87 Code=80"
```

# List
## Ex-4. Replace value
I would like to change my firts option that was 20 
for 2000
```python
options = [5, 10, 15, 20, 25, 30, 4, 20]
```
**Expected Result**
```python
[5, 10, 15, 2000, 25, 30, 4, 20]
```

# Tuple
**Create a Tuple**
```python
my_tuple = ("this", "is", "a", "tuple")
print(my_tuple)
```
**output:**
```
("this", "is", "a", "tuple")
```
The supported functions by Tuple class are almost the same than
a List class

# Dictionary
**Create a Dictionary**
```python
my_dict = { "type": "Car", "brand": "Ford", 
          "model": "Mustang", "year": 2020 }
print(my_dict)
```
**output:**
```
{"type": "Car", "brand": "Ford", 
"model": "Mustang", "year": 2020}
```

# Dictionary
## Accessing Items(1/2)
**Brackets**
```python
my_dict = { "type": "Car", "brand": "Ford", 
          "model": "Mustang", "year": 2020 }
model = my_dict["model"]
```
**Get function**
```python
my_dict = { "type": "Car", "brand": "Ford", 
          "model": "Mustang", "year": 2020 }
model = my_dict.get("model")
```
**Get Keys**
```python
my_dict = { "type": "Car", "brand": "Ford", 
          "model": "Mustang", "year": 2020 }
keys = my_dict.keys()
```

# Dictionary
## Accessing Items(2/2)
**Get Values**
```python
my_dict = { "type": "Car", "brand": "Ford", 
          "model": "Mustang", "year": 2020 }
values = my_dict.values()
```
**Get Items**
```python
my_dict = { "type": "Car", "brand": "Ford", 
          "model": "Mustang", "year": 2020 }
items = my_dict.items()
```

# Dictionary
## How to change/add Values
**Brackets**
```python
my_dict = { "type": "Car", "brand": "Ford", 
          "model": "Mustang", "year": 2020 }
my_dict["year"] = "1988"
```
**Update function**
```python
my_dict = { "type": "Car", "brand": "Ford", 
          "model": "Mustang", "year": 2020 }
my_dict.update({"brand": "Toyoda"})
```

# Dictionary
## Remove Items
**Pop function**
```python
my_dict = { "type": "Car", "brand": "Ford",
          "model": "Mustang", "year": 2020 }
my_dict.pop("type")
```
**Del function**
```python
my_dict = { "type": "Car", "brand": "Ford",
          "model": "Mustang", "year": 2020 }
del my_dict["type"]
del my_dict # WARNING: if you no specify the key to
            # remove that could delete the dictionary 
            # completely and cause an error
```

# Functions
## Definition
```python
def function_name(parameters):
  statement(s)
```
