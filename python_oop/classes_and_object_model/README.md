# Python - Classes & Object Model
---
## General Requirements
  
All tasks in this project must follow these requirements unless explicitly stated otherwise.

- The development environment used for evaluation is Ubuntu 20.04.
- Python version used for correction: Python 3.8.
- All Python files must be executable.
- The first line of all Python files must be:
```
#!/usr/bin/env python3
```
This ensures the script uses the Python interpreter available in the system environment rather than relying on a fixed system path.

- All files must end with a new line.
- Code must follow PEP8 style guidelines.
- All modules, classes, and functions should include clear and concise documentation strings.
- No external libraries may be imported unless explicitly allowed.
- All scripts must behave exactly as specified in the task instructions.
  
---

## 0. Exploring Objects

Introduction
  
Before creating your own classes, it is useful to explore how Python already uses objects internally.

In Python, everything is an object. Numbers, strings, lists, and dictionaries are all instances of classes defined by the Python language.

For example:
  
- ```"hello"``` is an instance of the ```str``` class
- ```[1, 2, 3]``` is an instance of the ```list``` class
- ```10``` is an instance of the ```int``` class
In this tutorial, you will explore existing Python objects using the Python interactive interpreter (REPL).

This will help you understand:

- how objects belong to classes
- how different objects have unique identities
- how objects expose behavior through methods
The following tasks will then show you how to create your own classes from scratch.

Objective
  
Use the Python REPL to explore:

- objects
- their classes
- their identities
- their available methods

Instructions
  
Open a terminal and start the Python interpreter:
```
python3
```
You should see the Python prompt:
```
>>>
```
Follow the steps below and observe the results.
  
Step 1 — Create Basic Python Objects

Create several Python objects using built-in types.
```
number = 42
text = "hello"
numbers = [1, 2, 3]
```
These objects are instances of classes already defined in Python.
  
Step 2 — Inspect the Class of an Object
  
Use the type() function to determine the class of each object.
  
Example:
```
type(number)
type(text)
type(numbers)
```
Observe the results.
  
Questions to consider:
  
- What class does each object belong to?
- Do different types of objects belong to different classes?
  
Step 3 — Inspect the Identity of an Object
  
Use the ```id()``` function to inspect the identity of objects.
  
Example:
```
id(number)
id(text)
id(numbers)
```
The returned value represents the unique identity of the object in memory.
  
Now create another object:
```
another_number = 42
```
Then check:
```
id(number)
id(another_number)
```
Observe whether the identities are the same or different.
  
Step 4 — Explore Object Behavior
  
Objects provide behavior through methods.
  
Use the ```dir()``` function to list the methods available on an object.
  
Example:
```
dir(text)
```
Try calling one of the methods:
```
text.upper()
text.replace("h", "H")
```
Observe how methods operate on the object's data.
  
Step 5 — Create Multiple Objects  
  
Create multiple objects of the same type:
```
list_a = [1, 2]
list_b = [1, 2]
```
Check their identities:
```
id(list_a)
id(list_b)
```
Even though the contents are the same, the objects are different instances.
  
Reflection  
  
Before continuing to the next task, reflect on the following questions:

- What does ```type(object)``` tell you about an object?
- Why do different objects have different identities?
- How do methods relate to objects?
In the next tasks, you will learn how to create your own classes, which allow you to define your own types of objects.
  
Evaluation
  
Before continuing with the implementation tasks, complete a short conceptual quiz.
  
This quiz will evaluate your understanding of:
  
- the difference between classes and instances
- how objects are created
- how instance attributes behave
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/classes_and_object_model  
  
---

## 1. My First Square

Objective  
Create your first Python class.
  
Instructions  
Define a class named ```Square``` that represents a square.

For this first version, the class does not need to contain any attributes or methods.
  
Example usage:
```
spam@camelot:~/$ cat 0-main.py
#!/usr/bin/env python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

spam@camelot:~/$ ./0-main.py
<class '0-square.Square'>
{}
spam@camelot:~/$ 
```
  
Repo:  

GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/classes_and_object_model  
File: 0-square.py  
  
---

## 2. Square with Size
  
Objective
  
Introduce instance attributes.
  
Instructions  
  
Define a class ```Square``` with:

- a private instance attribute ```size```
- The size must be set when the object is created.
Why is ```size``` private attribute?
  
The size is crucial for a square, many things depend of it (area computation, perimeter, etc.), so you, as a class builder, must control the type and value of this attribute. One way to have the control is to keep it privately.
  
This is known as the encapsulation principle.
  
Example:
```
spam@camelot:~/$ cat 1-main.py
#!/usr/bin/env python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

spam@camelot:~/$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
spam@camelot:~/$ 
```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/classes_and_object_model  
File: 1-square.py  
  
---

## 3. Size Validation
  
Objective
  
Ensure that object state is valid.
  
Instructions
  
Add validations to the ```size``` attribute on the ```Square``` class.

The ```size``` attribute must satisfy:

- must be an integer. Otherwise raise a ```TypeError``` exception with the message ```size must be an integer```
- must be greater than or equal to 0. Otherwise raise a ```ValueError``` exception with the message ```size must be >= 0```
  
Example:
```
spam@camelot:~/$ cat 2-main.py
#!/usr/bin/env python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

spam@camelot:~/$ ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
spam@camelot:~/$ 
```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/classes_and_object_model  
File: 2-square.py  
  
---

## 4. Area of a Square
  
Objective
  
Implement instance methods.
  
Instructions
  
Add an instance method ```area(self)``` to the ```Square``` class that returns the area of the square based on it's ```side``` length.
  
Example:
```
spam@camelot:~/$ cat 3-main.py
#!/usr/bin/env python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

spam@camelot:~/$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
spam@camelot:~/$ 
```
  
Repo:

GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/classes_and_object_model  
File: 3-square.py  
  
---

## 5. Access and Update Private Attribute

Objective
  
Implement controlled access to attributes.
  
Instructions
  
Add getters and setters for the ```size``` attribute.

The setter must validate input using the same rules as before.
  
Why a getter and setter?
  
```size``` is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.
  
Be sure to read and understand this: Getters and Setters: Manage Attributes in Python
  
```
spam@camelot:~/$ cat 4-main.py
#!/usr/bin/env python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

spam@camelot:~/$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
spam@camelot:~/$ 
```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/classes_and_object_model  
File: 4-square.py  
  
---

## 6. Printing a Square

Objective
  
Use object state to generate output.
  
Instructions
  
- Add a public instance method ```def my_print(self)``` that prints in stdout the square with the character ```#```
- If size is equal to 0, print an empty line
```
spam@camelot:~/$ cat 5-main.py
#!/usr/bin/env python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

spam@camelot:~/$ ./5-main.py
###
###
###
--
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
--

--
spam@camelot:~/$ 
```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/classes_and_object_model  
File: 5-square.py  
  
---

## 7. Print Square Instance

Objective
  
Control how objects are represented as strings.
  
Instructions
  
Add and implement the special method:
```
__str__()
```
- Private instance attribute: ```position:```
    - property ```def position(self):``` to retrieve it
    - property setter ```def position(self, value):``` to set it:
        - ```position``` must be a tuple of 2 positive integers, otherwise raise a ```TypeError``` exception with the message ```position must be a tuple of 2 positive integer```
- Instantiation with optional ```size``` and optional ```position```: ```def __init__(self, size=0, position=(0, 0)):```
- Public instance method: ```def my_print(self):``` that prints in stdout the square with the character ```#```:
    - if ```size``` is equal to 0, print an empty line
    - ```position``` should be used by using space
- Printing a ```Square``` instance should have the same behavior as ```my_print()```
```
spma@camelot:~/$ cat 6-main.py
#!/usr/bin/env python3
Square = __import__('6-square').Square

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)

spma@camelot:~/$ ./6-main.py | tr " " "_" | cat -e
#####$
#####$
#####$
#####$
#####$
--$
$
____#####$
____#####$
____#####$
____#####$
____#####$
spma@camelot:~/$ 
```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/classes_and_object_model  
File: 6-square.py  
  
---

## 8. Rectangle Class
  
Objective
  
Reinforce object modeling with a second class.
  
Instructions
  
Define a class ```Rectangle``` with:

- Private instance attribute ```width:```

- property ```width(self)``` to retrieve it

- property setter ```width(self, value)``` to set it.

    - ```width``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```width must be an integer```
    - if ```width``` is less than 0, raise a ```ValueError``` exception with the message ```width must be >= 0```
- Private instance attribute ```height:```

- property ```height(self)``` to retrieve it

- property setter ```height(self, value)``` to set it

    - ```height``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```height must be an integer```
    - if ```height``` is less than 0, raise a ```ValueError``` exception with the message ```height must be >= 0```
Instantiation with optional ```width``` and ```height``` and default value of ```0```. (```__init__(self, width=0, height=0)```)
```
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

spam@camelot:~/$ ./main.py
{'_Rectangle__width': 2, '_Rectangle__height': 4}
{'_Rectangle__width': 10, '_Rectangle__height': 3}
spam@camelot:~/$ 
```
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/classes_and_object_model  
File: 1-rectangle.py  
  
---

## 9. Area and Perimeter
  
Objective
  
Implement behavior for the rectangle class.
  
Instructions
  
Add the following instance methods to the ```Rectangle``` class:

- ```area()``` that returns the rectangle area
- ```perimeter()``` that returns the rectangle perimeter:
- if ```width``` or ```height``` is equal to ```0```, perimeter is equal to ```0```
Example:
```
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

spam@camelot:~/$ ./main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
spam@camelot:~/$ 
```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/classes_and_object_model  
File: 2-rectangle.py  
  