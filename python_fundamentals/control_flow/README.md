# Python - Control Flow
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

- No functions are allowed in this project.

- No imports are allowed.

- Output must match expected formatting exactly.

---

0. Positive anything is better than negative nothing

Create a script that assigns a random integer to a variable named ```number```. Copy the following line exactly as it is, after the shebang line.
```
number = __import__('random').randint(-10, 10)
```  
The previous line will assign a random integer between -10 and 10 to the ```number``` variable. You don't need to focus on this yet.

Using conditional statements, print:
- ```<number> is positive``` if the number is greater than 0
- ```<number> is zero``` if the number equals 0
- ```<number> is negative``` if the number is less than 0  
Example:
```
spam@camelot:~/$ ./positive_or_negative.py 
-4 is negative
spam@camelot:~/$ ./positive_or_negative.py 
0 is zero
spam@camelot:~/$ ./positive_or_negative.py 
-3 is negative
spam@camelot:~/$ ./positive_or_negative.py 
-10 is negative
spam@camelot:~/$ ./positive_or_negative.py 
10 is positive
```  
  
Repo: 

GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/control_flow  
File: positive_or_negative.py  

---

1. The last digit

Assign a random integer to ```number```. Copy the following line exactly as it is, after the shebang line.
```
number = __import__('random').randint(-10000, 10000)
```  
<mark>Compute the last digit and print</mark>:

- ```Last digit of <number> is <digit> and is greater than 5```
- ```Last digit of <number> is <digit> and is 0```
- ```Last digit of <number> is <digit> and is less than 6 and not 0```  
Output must match exactly the expected structure.
```
spam@camelot:~/$ ./last_digit.py
Last digit of -9200 is 0 and is 0
spam@camelot:~/$ ./last_digit.py
Last digit of 5247 is 7 and is greater than 5
spam@camelot:~/$ ./last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
```
  
Repo:  

GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/control_flow  
File: last_digit.py  

---

2. Alphabet Game (Lowercase)

<mark>Print the lowercase alphabet except for ```q``` and ```e```<mark>.

Output must be continuous (no spaces, no new lines except at end).

Expected pattern:  
```
abcdfghijklmnoprstuvwxyz
```
  
Repo:  

GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/control_flow  
File: print_alphabt.py  

---
3. Hexadecimal Printing

<mark>Print numbers from 0 to 98 in decimal and hexadecimal</mark>.

Format:
```
0 = 0x0
1 = 0x1
...
98 = 0x62
```  
- You can only use one ```print``` function with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
  
Repo:  

GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/control_flow  
File: print_hexa.py  

---

4. 00...99

<mark>Print numbers from 0 to 99</mark> formatted as two-digit numbers separated by comma and space.

Last number must not be followed by comma.

Example beginning:
```
00, 01, 02, 03, ...
```  
- Correct formatting with leading zeros.
- No trailing comma.
- Exact spacing.
- The last number should be followed by a new line
- You can only use no more than 2 print functions - with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
  
Repo:

GitHub repository: holbertonschool-core-engineering  
Directory: python_fundamentals/control_flow  
File: print_comb2.py  

---
