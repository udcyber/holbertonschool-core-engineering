# Python - File Handling

---

## Requirements

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

---

## 0. Read file

Write a function that reads a text file (```UTF8```) and prints it to stdout:

Prototype:
```
def read_file(filename=""):
```
- You must use the ```with``` statement
- You don't need to manage ```file permission``` or ```file doesn't exist exceptions```.
- You are not allowed to import any module
```
spam@camelot:~/$ cat main.py
#!/usr/bin/env python3
read_file = __import__('read_file').read_file

read_file("my_file_0.txt")

spam@camelot:~/$ cat my_file_0.txt
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
spam@camelot:~/$ ./main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
spam@camelot:~/$ 
```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_advanced/file_handling  
File: read_file.py  
  
---

## 1. Write to a file

Write a function that writes a string to a text file (```UTF-8```) and returns the number of characters written:
  
Prototype:
```
def write_file(filename="", text=""):
```
- You must use the ```with``` statement
- You don't need to manage file permission exceptions.
- Your function should create the file if it doesn't exist.
- Your function should overwrite the content of the file if it already exists.
- You are not allowed to import any module
```
spam@camelot:~/$ cat 1-main.py
#!/usr/bin/env python3
write_file = __import__('write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)

spam@camelot:~/$ ./1-main.py
24
spam@camelot:~/$ cat my_first_file.txt
This School is so cool!
spam@camelot:~/$ 
```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_advanced/file_handling  
File: write_file.py  
  
---

## 2. Append to a file

Write a function that appends a string at the end of a text file (```UTF-8```) and returns the number of characters added:
Prototype:
```
def append_write(filename="", text=""):
```
- If the file doesn't exist, it should be created
- You must use the ```with``` statement
- You don't need to manage ```file permission``` or ```file doesn't exist``` exceptions.
- You are not allowed to import any module
```
spam@camelot:~/$ cat 2-main.py
#!/usr/bin/env python3
append_write = __import__('append_write').append_write

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)

spam@camelot:~/$ cat file_append.txt
cat: file_append.txt: No such file or directory
spam@camelot:~/$ ./2-main.py
24
spam@camelot:~/$ cat file_append.txt
This School is so cool!
spam@camelot:~/$ ./2-main.py
24
spam@camelot:~/$ cat file_append.txt
This School is so cool!
This School is so cool!
spam@camelot:~/$ 
```
  
Repo:
  
GitHub repository: holbertonschool-core-engineering  
Directory: python_advanced/file_handling  
File: append_write.py  
  