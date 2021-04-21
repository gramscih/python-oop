---
title: Object Oriented Programming with Python
author: Gramsci Hermozo
institute: Final Session
theme: Copenhagen
colortheme: seahorse
---

# Content
+ Final Project
+ Questions.
+ Implemet Bank user registration
+ Python usages and refs

# Final Project (presentation May 5)
## Text-Based Computer Games
Este es un tipo de juego para computadora basado en texto ingresado por el usuarion y con una serie de instrucciones.
No es necesario un interfas grafica avanzada. Para este juego tenemos los siguientes requerimientos:

- Agregar un descripcion sobre su idea del juego.
- Diseña tu idea del juego (mapa, trampas, enemigos, puertas, pasajes, etc...).
- Diseña un diagrama de clases sobre todos los objectos que agregaras en el juego.
- Agregar Unittest para validar los posibles inputs y comportamiento del juego.
- Agregar Error handling, en caso de exister algun problema o exception el juego debe continuar.

# Final Project
## Extra Points:

- More than one level in the game (some option to pass the next level).
- Enter configuration by console in oneline
- A helper for command line.


An [_example_](https://www.youtube.com/watch?v=8al0RzkDqgM) of how we can play this kind of games.

# Image example
![](Rogue_Screen_Shot_CAR.PNG)

# Questions
- How to mock reader file

You can use the following decorator (thanks to Dennis Gamboa)
```python
@patch("builtins.open", mock_open(read_data=DATA_EMPTY))
```

# Implement Bank registration
- Design class diagram
- Implement classes according diagram
- Review Polymorphism

# Python usages and refs (1/3)
+ Web Development

Python can be used to make web-applications at a rapit rate. 
Some of the most well-known frameworks are [Django](https://www.djangoproject.com/) and [Flask](https://flask.palletsprojects.com/en/1.1.x/).

+ Game Developement

Python has his own library to develop games and is [PyGame](https://realpython.com/pygame-a-primer/) that provides functionality and a library for
gane development.

# Python usages and refs (2/3)
+ Machine learning & AI

We make the computer learn based on past experiences through the data stored or better yet, create algorithms which makes the computer learn by itself
Python has the following packages for this: [Pandas](https://pandas.pydata.org/) - [NumPy](https://numpy.org/) and [Scikit-Learn](https://scikit-learn.org/)

+ Data science and Data Visualization

Data is money if you know how to extract relevant information which can help you take calculated risks and increase profits. 
You study the data you have, perform operations and extract the information required. Libraries such as Pandas, NumPy help you 
in extracting information. 

You can even visualize the data libraries such as [Matplotlib](https://matplotlib.org/stable/), [Seaborn](https://seaborn.pydata.org/).

# Python usages and refs (3/3)
+ Descktop GUI

We use Python to program desktop applications. There are some other useful toolkits such as the, 
[Kivy](https://kivy.org/#home), [PYQT](https://wiki.python.org/moin/PyQt) that can be used to create applications on several platforms.

+ Web Scraping Applications

Python is a savior when it comes to pull a large amount of data from websites which can then be helpful in various real-world processes 
such as price comparison, job listings, research and development and much more. 

Python has [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) which we use to pull such data.
