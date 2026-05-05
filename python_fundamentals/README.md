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
- Output must match expected formatting exactly.
- No external libraries are allowed unless explicitly requested.

---

1. Deterministic Script Output

Create an executable file named ```structured_output.py``` that prints exactly:

```
Language: Python
Version: 3
Pi approx: 3.14
Computation valid: True
```  

Constraints:

- The float must be derived from a numeric value and formatted to two decimals.
- The boolean must result from evaluating a comparison expression.
- At least one line must use formatted string interpolation.
- No input is allowed.

Execution example:
```
./structured_output.py
```  
The output must match exactly.

