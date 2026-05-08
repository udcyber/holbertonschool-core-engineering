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

---

3. Print a matrix of integers
  
Write a function that <mark>prints a matrix of integers</mark>.
  
Prototype:
```
def print_matrix_integer(matrix=[[]]):
```
- ```matrix``` is a list of lists (2D list).
- Format each row on its own line.
- Values in a row must be separated by a single space.  
  
Execution example:
```
$ cat main.py
#!/usr/bin/env python3
print_matrix_integer = __import__('print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)

$ ./main.py
1 2 3
4 5 6
7 8 9
```
  
Repo:  
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/core_data_structures  
File: print_matrix_integer.py  

---

4. Tuple addition
  
Write a function that <mark>adds two tuples</mark>.
  
Prototype:
```
def add_tuple(tuple_a=(), tuple_b=()):
```
  
- Return a new tuple with exactly two integers.
- Treat missing values as ```0```.
- Ignore values beyond the first two.  
  
Execution example:
```
$ cat main.py
#!/usr/bin/env python3
add_tuple = __import__('add_tuple').add_tuple

print(add_tuple((1, 89), (88, 11)))
print(add_tuple((1, 89), (1, )))
print(add_tuple((1, 89), ()))
print(add_tuple((), ()))

$ ./main.py
(89, 100)
(2, 89)
(1, 89)
(0, 0)
```
  
Repo:  
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/core_data_structures  
File: add_tuple.py  

---

5. Common elements in two sets

Write a function that <mark>returns a set of common elements in two sets</mark>.

Prototype:
```
def common_elements(set_1, set_2):
```
- Return a new set containing only elements present in both ```set_1``` and ```set_2```.
  
Execution example:
```
$ cat main.py
#!/usr/bin/env python3
common_elements = __import__('common_elements').common_elements

set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
print(sorted(list(common_elements(set_1, set_2))))

$ ./main.py
['C']
```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/core_data_structures  
File: common_elements.py  

---

6. Update or add a key/value in a dictionary

Write a function that <mark>replaces or adds a key/value pair in a dictionary</mark>.

Prototype:
```
def update_dictionary(a_dictionary, key, value):
```
- If ```key``` already exists, replace its value.
- If ```key``` does not exist, create it.
- Return the (updated) dictionary.
  
Execution example:
```
$ cat main.py
#!/usr/bin/env python3
update_dictionary = __import__('update_dictionary').update_dictionary

d = {'language': 'C', 'number': 89, 'track': 'Low level'}
print(update_dictionary(d, 'language', 'Python'))
print(update_dictionary(d, 'city', 'San Francisco'))

$ ./main.py
{'language': 'Python', 'number': 89, 'track': 'Low level'}
{'language': 'Python', 'number': 89, 'track': 'Low level', 'city': 'San Francisco'}
```
  
Repo:  

GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/core_data_structures  
File: update_dictionary.py  

---

7. Best score

Write a function that <mark>returns the key with the biggest integer value</mark>.

Prototype:
```
def best_score(a_dictionary):
```
- You may assume that all values are integers.
- If ```a_dictionary``` is ```None``` or empty, return ```None```.
- You may assume all values are different.
  
Execution example:
```
$ cat main.py
#!/usr/bin/env python3
best_score = __import__('best_score').best_score

scores = {'John': 12, 'Bob': 14, 'Mike': 15, 'Molly': 16, 'Adam': 10}
print(best_score(scores))
print(best_score(None))

$ ./main.py
Molly
None
```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/core_data_structures  
File: best_score.py  
