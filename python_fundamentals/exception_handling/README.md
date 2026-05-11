# Python - Exception Handling
---

## General Requirements
  
- Corrections will run on Ubuntu 20.04 LTS.
- Python version used for correction: Python 3.8.x.
- Every Python file must start exactly with:
  #!/usr/bin/env python3
- Every Python file must:

    - Be executable.
    - End with a newline.
    - Be PEP8 compliant (pycodestyle 2.7.x).
- No external libraries are allowed.

- Unless explicitly stated, do not use broad ```except:``` blocks.

---

## 0. Safe list printing

Write a function that <mark>prints ```x``` elements of a list</mark>.

Prototype:
```
def safe_print_list(my_list=[], x=0):
```
  
- ```my_list``` can contain any type (integer, string, etc.)
- All elements must be printed on the same line followed by a new line.
- ```x``` represents the number of elements to print
- ```x``` can be bigger than the length of ```my_list```
- Returns the real number of elements printed
- You have to use ```try: / except:```
- You are not allowed to import any module
- You are not allowed to use ```len()```
  
```
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
safe_print_list = __import__('safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print(f"elements: {nb_print}")

spam@camelot:~/$ ./main.py
12
nb_print: 2
spam@camelot:~/$ 
```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/exception_handling  
File: safe_print_list.py
  
---

## 1. Safe integer printing

Write a function that <mark>prints an integer with ```"{:d}".format()```</mark> followed by a new line.

Prototype:  
```
def safe_print_integer(value):
```
- If ```value``` is an integer, print it and return ```True```.
- Otherwise, return ```False```.
- You have to use ```try: / except:```
- You are not allowed to import any module
- You are not allowed to use ```type()```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/exception_handling  
File: safe_print_integer.py
  
---

## 2. Safe list printing with type handling

Write a function that <mark>prints the first ```x``` elements of a list</mark>.

Prototype:
```
def safe_print_list_integers(my_list=[], x=0):
```
- Print only integers.
- Skip elements that are not integers.
- Return the number of integers printed.
- All integers have to be printed on the same line followed by a new line.
- ```my_list``` can contain any type (integer, string, etc.)
- You have to use ```try: / except:```
  
```
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
safe_print_list_integers = __import__('safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

spam@camelot:~/$ ./main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "//safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
spam@camelot:~/$ 
```
  
Repo:

GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/exception_handling  
File: safe_print_list_integers.py  
  
---

3. Divide two integers safely
  
Write a function that <mark>divides two integers</mark>.
  
Prototype:
```
def safe_print_division(a, b):
```
- Perform the division inside a ```try``` block.
- If any other exception occurs, print ```"Inside result: None"```.
- Always print ```"Inside result: <result>"``` using ```finally```.
- Return the result (or ```None```).
  
```
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
safe_print_division = __import__('safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

spam@camelot:~/$ ./main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
spam@camelot:~/$ 
```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/exception_handling  
File: safe_print_division.py  
  
---

4. Raise exception
  
Write a function that <mark>raises a ```TypeError```</mark>.

Prototype:
```
def raise_exception():
```
- The function must raise a ```TypeError```.

Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/exception_handling  
File: raise_exception.py  
  
---

5. Raise a message

Write a function that <mark>raises a ```NameError``` with a custom message</mark>.

Prototype:
```
def raise_exception_msg(message=""):
```
  
- The function must raise a ```NameError``` with ```message```.
  
Repo:

GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/exception_handling  
File: raise_exception_msg.py  
  