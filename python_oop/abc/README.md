# Python - Abstract Classes & Interfaces
---
## Concept Guide
  
Abstract Classes and Concrete Classes
  
An abstract class defines behavior that subclasses must implement.
  
For example, a class may define a method that all subclasses must provide, while leaving the actual implementation to each subclass.
  
A simplified relationship looks like this:
```
          Animal (Abstract Class)
                 │
        ┌────────┴────────┐
        │                 │
       Dog               Cat
   (Concrete Class)  (Concrete Class)
```
Interpretation:

- ```Animal``` defines required behavior
- ```Dog``` and ```Cat``` provide concrete implementations
- all subclasses share the same contract
  
Duck Typing
  
In Python, objects are often used based on what they can do, not only on what they inherit from.
  
Example idea:

- if an object provides a method named ```draw()```, it may be usable in a function that expects something drawable
- the object does not always need to inherit from a specific class for that use case
This approach is often called duck typing.
  
## General Requirements
  
All tasks in this project must follow these requirements unless otherwise specified.
  
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
Coding requirements
  
- All files must end with a newline
- Code must follow PEP8
- All modules, classes, and functions must include documentation strings
- Only the Python standard library may be used unless otherwise stated

---

0. Abstract Animal Class and its Subclasses
  
Background
  
In object-oriented programming, Abstract Base Classes (ABCs) ensure that derived classes implement specific methods from the base class. This provides a blueprint for creating and structuring derived classes. Python’s ```ABC``` package facilitates the creation of abstract base classes.
  
Objective
  
1. Create an abstract class named ```Animal``` using the ```ABC``` package. This class must have an abstract method called ```sound```.
2. Create two subclasses of ```Animal```: ```Dog``` and ```Cat```.
3. Implement the ```sound``` method in ```Dog``` so it returns the string ```"Bark"```.
4. Implement the ```sound``` method in ```Cat``` so it returns the string ```"Meow"```.
  
Instructions
  
1. Import the necessary components from the ```abc``` module.
2. Define the ```Animal``` class so it inherits from ```ABC```.
3. Inside ```Animal```, declare an abstract method named ```sound``` using the ```@abstractmethod``` decorator.
4. Create a subclass named ```Dog``` that inherits from ```Animal```.
5. Implement ```sound``` in ```Dog``` so it returns ```"Bark"```.
6. Create a subclass named ```Cat``` that inherits from ```Animal```.
7. Implement ```sound``` in ```Cat``` so it returns ```"Meow"```.
  
Hint
  
If a class still has abstract methods without implementation, Python will raise a ```TypeError``` when you try to instantiate it.
Example:
  
```
$ cat main.py
#!/usr/bin/env python3
from animals import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()

print(bobby.sound())
print(garfield.sound())

animal = Animal()
print(animal.sound())

$ ./main.py
Bark
Meow
Traceback (most recent call last):
  File "main.py", line 10, in <module>
    animal = Animal()
TypeError: Can't instantiate abstract class Animal with abstract method sound
```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/abc  
File: animals.py  
  
---

## 1. Shapes, Interfaces, and Duck Typing
  
Background
  
Python employs a concept called duck typing, which is concerned with the semantics of objects rather than their inheritance hierarchy. If an object behaves like a duck, then it is considered a duck, regardless of its actual class. This allows flexible and dynamic polymorphism. In this task, you will use abstract base classes to design a blueprint for shapes and use duck typing to handle objects of different shapes uniformly.
  
Objective
  
1. Create an abstract class named ```Shape``` with two abstract methods: ```area``` and ```perimeter```.
2. Implement two concrete classes: ```Circle``` and ```Rectangle```, both inheriting from ```Shape```.
3. Each class must provide implementations for ```area``` and ```perimeter```.
4. Write a standalone function named ```shape_info``` that accepts an object of type ```Shape``` by duck typing and prints its area and perimeter.
5. Test ```shape_info``` with instances of both ```Circle``` and ```Rectangle```.
  
Instructions
  
1. Define an abstract class ```Shape``` using the ```ABC``` package.

2. Inside ```Shape```, declare two abstract methods: ```area``` and ```perimeter```.

3. Create a ```Circle``` class that inherits from ```Shape```.

    - Its constructor must accept a radius.
    - It must implement ```area```.
    - It must implement ```perimeter```.
4. Create a ```Rectangle``` class that inherits from ```Shape```.

    - Its constructor must accept the width and height.
    - It must implement ```area```.
    - It must implement ```perimeter```.
5. Define a function named ```shape_info``` that takes a single argument.

6. Without explicitly checking the type of the argument, call its ```area``` and ```perimeter``` methods.

7. Print the area and perimeter of the shape passed to the function.

8. Instantiate a ```Circle``` and a ```Rectangle```.

9. Pass each object to ```shape_info``` and observe the output.
  
Hint
  
Do not use ```isinstance``` checks inside ```shape_info```. The function should rely on the presence of the required methods.
  
Example:
```
$ cat main.py
#!/usr/bin/env python3
from shapes import Circle, Rectangle, shape_info

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)

$ ./main.py
Area: 78.53981633974483
Perimeter: 31.41592653589793
Area: 28
Perimeter: 22
```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/abc  
File: shapes.py  
  
---

## 2. The Enigmatic FlyingFish - Exploring Multiple Inheritance
  
Background
  
In some object-oriented languages, a class can inherit attributes and behaviors from more than one parent class. This is known as multiple inheritance. Python supports multiple inheritance, but it also comes with complexities, particularly regarding method resolution order (MRO).
  
Objective
  
Construct a ```FlyingFish``` class that inherits from both a ```Fish``` class and a ```Bird``` class. Within ```FlyingFish```, override methods from both parents. The goal is to understand multiple inheritance and how Python determines method resolution order.
  
Instructions
  
1. Create a ```Fish``` class with:

    - a method ```swim``` that prints ```"The fish is swimming"```
    - a method ```habitat``` that prints ```"The fish lives in water"```
2. Create a ```Bird``` class with:

    - a method ```fly``` that prints ```"The bird is flying"```
    - a method ```habitat``` that prints ```"The bird lives in the sky"```
3. Construct a ```FlyingFish``` class that inherits from both ```Fish``` and ```Bird```.

4. Override ```fly``` in ```FlyingFish``` so it prints ```"The flying fish is soaring!"```.

5. Override ```swim``` in ```FlyingFish``` so it prints ```"The flying fish is swimming!"```.

6. Override ```habitat``` in ```FlyingFish``` so it prints ```"The flying fish lives both in water and the sky!"```.

7. Instantiate an object of the ```FlyingFish``` class.

8. Call the ```fly```, ```swim```, and ```habitat``` methods and observe the outputs.

9. Use ```mro()``` or ```.__mro__``` on FlyingFish to inspect the method resolution order.
  
Hint
  
The order in which parent classes are listed in the class definition affects the method resolution order.
  
Example:
```
$ cat main.py
#!/usr/bin/env python3
from flyingfish import Fish, FlyingFish

flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()

$ ./main.py
The flying fish is swimming!
The flying fish is soaring!
The flying fish lives both in water and the sky!
```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/abc  
File: flyingfish.py  
  
---

## 3. The Mystical Dragon - Mastering Mixins
  
Background
  
Mixins are a way to add functionality to classes in a modular fashion. They are not meant to stand alone; they are meant to be combined with other classes to add behaviors. By using mixins, you can compose behaviors in classes without the need for deep or rigid inheritance hierarchies.
  
Objective
  
Design two mixin classes, ```SwimMixin``` and ```FlyMixin```, each equipped with methods ```swim``` and ```fly``` respectively. Next, construct a class ```Dragon``` that inherits from both mixins. The goal is to show that a ```Dragon``` instance can both swim and fly.
  
Instructions
  
1. Design a mixin called ```SwimMixin``` with a method ```swim``` that prints ```"The creature swims!"```.
2. Design another mixin called ```FlyMixin``` with a method ```fly``` that prints ```"The creature flies!"```.
3. Construct a class named ```Dragon``` that inherits from both ```SwimMixin``` and ```FlyMixin```.
4. In the ```Dragon``` class, add a method ```roar``` that prints ```"The dragon roars!"```.
5. Instantiate an object of the ```Dragon``` class.
6. Demonstrate the object’s abilities by calling ```swim```, ```fly```, and ```roar```.
  
Hint
  
Mixins should stay focused and provide a single capability. Here, one mixin provides swimming behavior and the other provides flying behavior.
  
Example:
```
$ cat main.py
#!/usr/bin/env python3
from dragon import Dragon

dragon = Dragon()
dragon.swim()
dragon.fly()
dragon.roar()

$ ./main.py
The creature swims!
The creature flies!
The dragon roars!
```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/abc  
File: dragon.py  
  
---

## 4. Extending the Python List

Background:
  
In Python, you can extend built-in classes to add or modify behavior. The ```list``` class provides a collection of methods and functionalities that handle list operations. By extending the ```list``` class, you can provide custom behaviors while retaining the original functionalities.
  
Objective:
  
Create a class named ```VerboseList``` that extends the Python ```list``` class. This custom class should print a notification message every time an item is added (using the ```append``` or ```extend``` methods) or removed (using the ```remove``` or ```pop``` methods).
  
Instructions:
  
1. Setting up the VerboseList Class:
  
- Define a class ```VerboseList``` that inherits from the built-in ```list``` class.
- Within ```VerboseList```, override the methods that modify the list: ```append```, ```extend```, ```remove```, and ```pop```.
2. Implementing Notifications:
  
- For the ```append``` method: After adding the item to the list, print a message like "Added [item] to the list."
- For the ```extend``` method: After extending the list, print a message like "Extended the list with [x] items." where [x] is the number of items added.
- For the ```remove``` method: Before removing the item from the list, print a message like "Removed [item] from the list."
- For the ```pop``` method: Before popping the item from the list, print a message like "Popped [item] from the list." If the index is not specified, default behavior is to pop the last item.
  
3. Testing:
- Instantiate a ```VerboseList``` object.
- Test all the overridden methods (```append```, ```extend```, ```remove```, and ```pop```) and ensure that the appropriate messages are printed for each operation.
  
Hints:
  
- Remember to call the original method of the ```list``` class using the ```super()``` function to ensure that the original functionality is retained. For example, for ```append```: ```super().append(item)```.
- Think about edge cases, such as trying to remove an item that doesn't exist in the list.
```
$ cat main.py 
#!/usr/bin/env python3
from ```VerboseList``` import ```VerboseList```

vl = ```VerboseList```([1, 2, 3])
vl.append(4)
vl.extend([5, 6])
vl.remove(2)
vl.pop()
vl.pop(0)

$ ./main.py 
Added [4] to the list.
Extended the list with [2] items.
Removed [2] from the list.
Popped [6] from the list.
Popped [1] from the list.
```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_oop/abc  
File: ```VerboseList```.py  
  