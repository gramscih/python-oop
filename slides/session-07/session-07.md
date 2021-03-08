---
title: Object Oriented Programming with Python
author: Gramsci Hermozo
institute: Session 07
theme: Copenhagen
colortheme: seahorse
---

# Content
+ Logs
+ Physics problem
+ Static methods/functions
+ Use our Physics lib

# Logs
```python
# use logging package
import logging

# Configure logging
logging.basicConfig(filename='test.log', 
    level=logging.DEBUG)

# how to use
logging.debug('<Class_name>:<Function_name>: {}'.
    format(args))
```

# Physics problem
**Let's use all the things that we learn until now**

As a user I would like to have lib that help me to calculate 
physics problems, in this case parabolic movement.
![](parabolic.png)

# Physics formulas
Vox = Vo * cos \<angle\>

Voy = Vo * sen \<angle\>

D = Vo^2 * sen2\<angle\>

T = 2Vo sen\<angle\>

D = (Vo * sen2\<angle\>) / g

Where:
Vo = intial velocity
Vox = initial velocity in X
Voy = initial velocity in Y
T = run time
D = Distance


# Static Methods/Functions
```python
# to use static methods you can use the 
# following decorator

@staticmethod
def my_method():
  pass
```

# Use the new Physics lib
A goalkeeper shoot the ball out of his goal
with velocity 26 m/s and 40 grade. Calculate:

+ The max height 
+ The distance
+ The time that the ball would be in the air



