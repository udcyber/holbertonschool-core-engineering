# Python - Functions & Modularity

---

## General Requirements

- Corrections will run on Ubuntu 20.04 LTS.
- Python version used for correction: Python 3.8.x.
- The first line of every Python file must be exactly:
```
#!/usr/bin/env python3
```  
- All files must:

	- Be executable.
	- End with a newline.
	- Be PEP8 compliant (pycodestyle 2.7.x).
- No external libraries are allowed.

- No use of sys.argv in this project.

- Each task must follow its own constraints precisely.

---

## 0. islower

Write a function:

```
def islower(c):
```  
The function <mark>must return ```True``` if ```c``` is a lowercase letter and ```False``` otherwise</mark>.

Constraints:  

- You are not allowed to use built-in string methods such as ```.islower()```.
- You must use ASCII logic (```ord()```).
- The function must return a boolean value.

Example:  
```
>>> islower('a')
True
>>> islower('A')
False
>>> islower('3')
False
```  
Repo:  

GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/functions_modules  
File: islower.py  

---

## 1. To Uppercase

Write a function:
```
def uppercase(str):
```  
The function must <mark>print the string in uppercase followed by a new line</mark>.
  
Constraints:  

- You are not allowed to use ```.upper()```.
- You must use ASCII conversion (```ord()``` and ```chr()```).
- The function must print the result directly.
- The function does not return a value.  
Example:  
```
>>> uppercase("Holberton")
HOLBERTON
```  
Repo:  

GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/functions_modules  
File: uppercase.py  

---

## 2. Print Last Digit

Write a function:
```
def print_last_digit(number):
```
The function must:
  
- Print the last digit of ```number```.
- Return the value of the last digit.
The last digit must always be positive.
  
Example:
```
>>> print_last_digit(98)
8
>>> print_last_digit(-1024)
4
```
The printed digit must appear without extra text.
  
Repo:  

GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/functions_modules  
File: print_last_digit.py  

---

## 3. a ^ b

Write a function:
```
def pow(a, b):
```
The function must return the value of ```a``` raised to the power of ```b```.

Constraints:
  
- You are not allowed to use the built-in exponent operator ```**```.
- You are not allowed to import modules.
- You must implement the logic manually using a loop.
  
Example:
```
>>> pow(2, 4)
16
>>> pow(5, 0)
1
```
  
Repo:  

GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/functions_modules  
File: pow.py  

---

## 4. Script Execution and Import Behavior
  
Introduction
  
Until now, you have defined functions and executed them within the same file. In this task, you will analyze what changes when functions are placed in one file and that file is reused from another.
  
When Python imports a file, it executes the file from top to bottom in order to create its namespace. This means that:
- Function definitions are executed.
- Variable assignments are executed.
- Any top-level statements (including ```print```) are also executed.
  
If execution is not controlled, importing a file can trigger unintended behavior.
  
The objective of this task is to:
- Observe the difference between executing a file directly and importing it.
- Understand why top-level code runs during import.
- Learn the role of ```if __name__ == "__main__"```.
- Distinguish clearly between defining behavior and executing behavior.
  
You must carefully observe the behavior before and after introducing the execution guard. The quiz following this task will evaluate your understanding of these concepts.
  
Instructions:
  
Create two files:  

File: ```simple_add.py```

- Define a function ```add(a, b)``` that returns the sum of two numbers.
- At the top level of the file (outside any function, but after the definition), call the function and print the result of:
```
add(3, 5)
```
  
File: ```test_import.py```

- Import ```simple_add```.
- Run ```python3 test_import.py```
Observe what happens.
  
Then modify ```simple_add.py```:
  
- Move the print call inside:
```
if __name__ == "__main__":
```  
Run again.

You must ensure:

- When running ```python3 simple_add.py```, the result is printed.
- When running ```python3 test_import.py```, nothing is printed.

Reflection (Before Quiz)
  
Before attempting the quiz, take a few minutes to reflect on the following points:

- Why does the print statement execute during import before adding the execution guard?
- What is the value of ```__name__``` when a file is executed directly?
- What is the value of ```__name__``` when a file is imported?
- Why does moving the print statement inside ```if __name__ == "__main__":``` change the behavior?
  
You are not required to submit written answers. However, you are strongly encouraged to reason through these questions carefully before continuing.
  
The quiz that follows:
  
- Has a strict time limit per question (between 45 and 60 seconds).
- Can only be attempted once (one-shot attempt).
Make sure you fully understand the execution model before starting the quiz.
  
Repo:  

GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/functions_modules  

---

## 5. Import a Simple Function from a Simple File

Write a program that imports the function ```add()``` from the file ```add_0.py``` and prints the result of the addition ```1 + 2 = 3```
```
def add(a, b):
```
  
The program must:  

- Assign ```1``` to a variable ```a```.
- Assign ```2``` to a variable ```b```.
- Print:
```
1 + 2 = 3
```  
Constraints:
  
- You are not allowed to use ```*``` for importing.
- You are not allowed to use ```__import__```.
- The program must not execute when imported.
  
Repo:  
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/functions_modules  
File: add.py  

---

## 6. My First Toolbox

Write a program that imports functions from ```calculator_1.py``` and prints the result of:
  
- addition
- subtraction
- multiplication
- division
  
Using:  
```
a = 10
b = 5
```
  
Each operation must be printed on its own line.
  
Constraints:  

- You are not allowed to use ```*``` for importing.
- The program must not execute when imported.
  
Repo:
  
- GitHub repository: holbertonschool-core-engineering  
- Directory: python_fundamentals/functions_modules  
- File: calculation.py  

---

## 7. Everything Can Be Imported

Write a program that imports the variable ```a``` from ```variable_load_5.py``` and prints its value.

Constraints:  

- You are not allowed to use ```*``` for importing.
- The program must not execute when imported.
  
Example: 
```
98
```
  
Repo:  

GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/functions_modules  
File: variable_load.py  
