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
