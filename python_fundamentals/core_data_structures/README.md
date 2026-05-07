# Python - Core Data Structures

---

## General Requirements
- Corrections will run on Ubuntu 20.04 LTS.
- Python version used for correction: Python 3.8.x.
- Every Python file must start exactly with:
```
#!/usr/bin/env python3
```  
- Every Python file must:

	- Be executable.
	- End with a newline.
	- Be PEP8 compliant (pycodestyle 2.7.x).
- No external libraries are allowed.

- Unless explicitly stated otherwise, do not import modules.

---

0. Print a list of integers

Updated Project Instruction
  
Write a function that prints all integers of a list.  
- Prototype: ```def print_list_integer(my_list=[])```
- Format: one integer per line
- You may assume every element of ```my_list``` is an integer.

⚠️ Important note:
You are expected to explicitly format integers using ```:d``` in your ```print``` statement. Even if your function works correctly without it, most of the automated checks will fail if ```:d``` is not used.

Execution example:  
```
$ cat main.py
#!/usr/bin/env python3
print_list_integer = __import__('print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

$ ./main.py
1
2
3
4
5
```  
Repo:  

GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/core_data_structures  
File: print_list_integer.py  

---

1. Safe access to a list element

Write a function that retrieves an element from a list like in C.

- Prototype: ```def element_at(my_list, idx):```
- If ```idx``` is negative or out of range, return ```None```.
- Otherwise, return the element at position ```idx```.
  
Execution example:  
```
$ cat main.py
#!/usr/bin/env python3
element_at = __import__('element_at').element_at

my_list = ["a", "b", "c", "d", "e"]
print(element_at(my_list, 3))
print(element_at(my_list, -1))
print(element_at(my_list, 15))

$ ./main.py
d
None
None
```
  
Repo:  

GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/core_data_structures  
File: element_at.py  

---

2. Replace an element in a list

Write a function that replaces an element of a list at a specific position.

- Prototype: ```def replace_in_list(my_list, idx, element):```
- If ```idx``` is negative or out of range, return the original list unchanged.
- Otherwise, replace the element at position ```idx``` with ```element``` and return the list.
  
Execution example:
```
$ cat main.py
#!/usr/bin/env python3
replace_in_list = __import__('replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
print(replace_in_list(my_list, 3, 99))
print(replace_in_list(my_list, 15, 99))

$ ./main.py
[1, 2, 3, 99, 5]
[1, 2, 3, 99, 5]
```
  
Repo:  

GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/core_data_structures  
File: replace_in_list.py  