# Python – Inheritance & Polymorphism
---
## Class Hierarchy in This Project
  
Throughout this project you will progressively build the following class hierarchy:
  
```
BaseGeometry
      │
      ▼
   Rectangle
      │
      ▼
     Square
```
Interpretation
  
- BaseGeometry defines behavior shared by geometric shapes.
- Rectangle inherits from ```BaseGeometry``` and implements concrete behavior.
- Square inherits from ```Rectangle``` and represents a more specialized shape.
Because ```Square``` inherits from ```Rectangle```, and ```Rectangle``` inherits from ```BaseGeometry```, a ```Square``` object can also be treated as:

- a ```Rectangle```
- a ```BaseGeometry```
This relationship enables code reuse and polymorphism, allowing programs to work with related objects through a shared interface.
  
## General Requirements
  
All tasks in this project must follow these requirements unless explicitly stated otherwise.
  
Environment
  
- Ubuntu 20.04
- Python 3.8
  
Python files
  
All Python files must:

- be executable
- start with the following line
```
#!/usr/bin/env python3
```
Coding rules
  
- All files must end with a newline
- Code must follow PEP8
- All modules, classes, and functions must include documentation strings
- Only the Python standard library may be used unless otherwise stated
- Do not use the words ```import``` or ```from``` inside your comments, the checker will think you are trying to import some modules.
- To import any base class use the ```__import__``` method.
  
---
  
## 0. Introduction to Inheritance and Polymorphism
  
Objective
  
This tutorial introduces the concepts of inheritance and polymorphism through a guided example.
  
Step 1 — Create a Parent Class
  
Create a file:
```
0-polymorphism_demo.py
```
Define the following class:
```
#!/usr/bin/env python3

class Animal:
    def speak(self):
        return "Some sound"
```
This class defines behavior shared by all animals.
  
Step 2 — Create Child Classes
  
Create two subclasses that inherit from ```Animal```.
```
class Dog(Animal):
    pass

class Cat(Animal):
    pass
```
These classes inherit the ```speak()``` method from ```Animal```.
  
Step 3 — Create Objects
  
Add the following code:
```
dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())
```
Run the program and observe the output.
  
Step 4 — Override Methods
  
Modify the subclasses so each animal produces a different sound.
```
class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"
```
Run the program again.
  
Although the same method is called, each object produces a different result.
  
This behavior illustrates polymorphism.
  
Step 5 — Demonstrate Polymorphism
  
Modify the program:
```
animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())
```
Each object responds to the same method call with its own behavior.
  
Step 6 — Check Class Relationships
  
Python provides tools to check relationships between classes and objects.
  
Example:
```
dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

print(issubclass(Dog, Animal))
```
  
Repo:  
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/inheritance  
  
---

## 1. Base Geometry
  
Create a class named ```BaseGeometry```.
  
This class represents a foundational concept for geometric shapes. It defines behavior that other shape classes will build upon.
  
The purpose of this class is to provide shared functionality that subclasses can reuse.
  
Requirements
  
The class must include the following methods.
  
## ```area(self)```
  
This method represents the area of a geometric shape.
  
At this stage, the base class does not define how the area should be calculated, because different shapes compute their area differently.
  
Instead, this method should raise an exception indicating that the calculation is not implemented in this class.
  
Later classes representing specific shapes will provide their own implementation of this method.
```
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
BaseGeometry = __import__('base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

spam@camelot:~/$ ./main.py
[Exception] area() is not implemented
spam@camelot:~/$ 
```
## ```integer_validator(self, name, value)```
This method validates that a value represents a valid positive integer.
  
The method must verify that:

- ```value``` is an integer
- ```value``` is greater than ```0```
If ```value``` is not an integer, raise:
```
TypeError: <name> must be an integer
```
If ```value``` is less than or equal to ```0```, raise:
```
ValueError: <name> must be greater than 0
```
The parameter ```name``` must be used in the error messages.
```
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
BaseGeometry = __import__('base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

spam@camelot:~/$ ./main.py
[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
spam@camelot:~/$ 
```
Why this matters
  
The ```BaseGeometry``` class defines common behavior that can be reused by multiple geometric shapes.
  
For example, validating numeric parameters is a task that several shape classes will need to perform. Instead of repeating this logic in every class, it is defined once and reused through inheritance.
  
The ```area()``` method also establishes a shared interface: all shapes derived from this class will provide their own way to compute an area.
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/inheritance  
File: base_geometry.py  
  
---

## 2. Rectangle
  
Create a class ```Rectangle``` that inherits from ```BaseGeometry```.
  
The class must represent a rectangle defined by its width and height.
  
Both values must be validated using the validator defined in the parent class.

- Instantiation with ```width``` and ```height```: ```def __init__(self, width, height):```
- ```width``` and ```height``` must be private. No getter or setter
- ```width``` and ```height``` must be positive integers, validated by ```integer_validator```
```
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
Rectangle = __import__('1-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

spam@camelot:~/$ ./main.py
<1-rectangle.Rectangle object at 0x7f6f488f7eb8>
['_Rectangle__height', '_Rectangle__width', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']
[AttributeError] 'Rectangle' object has no attribute 'width'
[TypeError] height must be an integer
spam@camelot:~/$ 
```
  
Observation
  
The validation logic does not need to be rewritten in this class. Instead, it is reused from ```BaseGeometry```.
  
This demonstrates code reuse through inheritance.
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/inheritance  
File: 1-rectangle.py  
  
---

## 3. Full Rectangle
  
Extend the ```Rectangle``` class.
  
The class must now include:

- an implementation of the ```area()``` method

- a readable string representation of the rectangle

- Instantiation with ```width``` and ```height```: ```def __init__(self, width, height):```:

- ```width``` and ```height``` must be private. No getter or setter

- ```width``` and ```height``` must be positive integers validated by ```integer_validator```

- the ```area()``` method must be implemented

- ```print()``` should print, and ```str()``` should return, the following rectangle description: ```[Rectangle] <width>/<height>```
```
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
Rectangle = __import__('2-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())

spam@camelot:~/$ ./main.py
[Rectangle] 3/5
15
spam@camelot:~/$ 
```
  
Observation
  
At this point, your ```Rectangle``` class provides a concrete implementation of ```area()```.
  
The parent class defined that the method should exist, while the ```Rectangle``` class defines how the area is actually computed.
  
Other shapes, such as ```Square```, may also implement ```area()```.
  
Because different objects can respond to the same method call with their own implementation, programs can work with different shapes through a common interface. This is an example of polymorphism.
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/inheritance  
File: 2-rectangle.py  
  
---

## 4. Square #1
  
Create a class ```Square``` that inherits from ```Rectangle```.
  
A square is a specialized rectangle where width and height are equal.
  
The constructor must receive a single parameter representing the size of the square and initialize the parent class accordingly.
  
- Instantiation with ```size```: ```def __init__(self, size):```:
- ```size``` must be private. No getter or setter
- ```size``` must be a positive integer, validated by ```integer_validator```
- the ```area()``` method must be implemented
```
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
Square = __import__('1-square').Square

s = Square(13)

print(s)
print(s.area())

spam@camelot:~/$ ./main.py
[Rectangle] 13/13
169
spam@camelot:~/$ 
```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/inheritance  
File: 1-square.py  
  
---

## 5. Square #2
  
Extend the ```Square``` class.

Add the appropriate string representation for the square.

- ```print()``` should print, and ```str()``` should return, the square description: ```[Square] <width>/<height>```
```
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
Square = __import__('2-square').Square

s = Square(13)

print(s)
print(s.area())

spam@camelot:~/$ ./2-main.py
[Square] 13/13
169
spam@camelot:~/$ 
```
  
Reflection
  
Consider the following example:
```
shapes = [Rectangle(3, 5), Square(4)]

for shape in shapes:
    print(shape.area())
```
Even though the objects in the list are not the same class, the program can call the same method on each object.
  
Each class provides its own implementation of ```area()```, so the correct calculation is performed for each shape.
  
This illustrates an important benefit of inheritance and polymorphism: programs can work with related objects through a shared set of methods, without needing to know the exact class of each object.
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/inheritance  
File: 2-square.py  
  