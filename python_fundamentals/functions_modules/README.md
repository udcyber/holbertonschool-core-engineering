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

0. islower

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