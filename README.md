# AIRBNB_CLONE
AirBnB Clone is simple clone/version of the AirBnB American Vacation Marketplace. This project is divided into several parts namely:
1. The Console (Command Intepreter)
2. Web Static
3. MySQL Storage
4. WebFramework -Templating
5. RESTful API
6. Web Dynamic

## 1. The Console
The console helps manage projects objects in development including:
1. Create a new object (ex: a User, Place etc)
2. Retrieve an object from a file. database etc
3. Do operations on objects (counting, computing stats etc)
4. Update object attributes
5. Destroy an object

### How To Start IT
```bash
$ ./console.py
(hbnd)
```

### How To Use It (Examples)
The Shell works in interactive mode
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
And in non-interactive mode
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## 2. Web Static
Contains the frontend of the AirBnB clone that is:
1. HTML (Structure of the Site)
2. CSS (Style and Design of the site)

<img width="1604" alt="airbnb_landing" src="https://user-images.githubusercontent.com/79806436/184349452-74961585-0e9b-4de7-9324-6e1e7736d927.png">
