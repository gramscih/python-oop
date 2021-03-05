---
title: Object Oriented Programming with Python
author: Gramsci Hermozo
institute: Session 06
theme: Copenhagen
colortheme: seahorse
---

# Content
+ The Clock
+ Exceptions
+ Error Handling
+ Manage Errors friendly
+ Logs

# Exe. Complete the clock 
**We want to build a Clock with a European style (24 hours). Where the display shows the time from _00:00_ (midnight) to _23:59_ (one minute before midnight)**
![](clock.png)

# Exceptions
Errors detected during execution are called exception and are not unconditionally fatal.
```python
"""
Most common exception handlend in python
"""
Exception # Base Exception
AttributeError
ZeroDivisionError
ArithmeticError
IndexError
SyntaxError
TypeError
...
```

# Error Handling
Use `try...except` to catch exceptions.
```python
try:
  x = 5/0
except ZeroDivisionError as ex:
  print("Division by zero!!!! The exception: {}".format(e))
```

# Error Handling
```python
# Don't catch everything
try:
  function_trow_except()
except Exception as ex:
  # TODO: do something with the error
```

# Error Handling
```python
# Caching multiple Exception
try:
  d = {}
  a = d[1]
  b = d.no_implemented_function()
except (KeyError, AttributeError) as e:
  print("A keyerror or an AttributeError exception")
```

# Error Handling
```python
# Separate exception block for each type.
try:
  a = {}
  b = a[1]
  d = b.no_implemented_funciton()
except KeyError as e:
  print("This is a keyerror. Exception message:", e)
except AttributeError as ex:
  print("Attribute error. Exception message:", ex)
```

# Error Handling
```python
# Else and finally
try:
  # Exception raise
except Exception as ex:
  pass
else:
  # This section would be executed just if no exception is trow in the try.
finally:
  # This section of code would be executed always even with exception
```

# Raise Excepton
```python
def function_rise_except():
  raise ValueError("This function is throwing an exception")
```

# Logs
```python
# use logging package
import logging

# Configure logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)

# how to use
logging.debug('<Class_name>:<Function_name>: {}'.format(args))
```




