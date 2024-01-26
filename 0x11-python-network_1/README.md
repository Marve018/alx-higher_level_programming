# 0x11-python-network_1

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

How to fetch internet resources with the Python package urllib
How to decode urllib body response
How to use the Python package requests #requestsiswaysimplerthanurllib
How to make HTTP GET request
How to make HTTP POST/PUT/etc. request
How to fetch JSON resources
How to manipulate data from an external service

### Tasks

mandatory
Write a Python script that fetches <https://alx-intranet.hbtn.io/status>

You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like the following example (tabulation before -)
You must use a with statement

``` h

guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
guillaume@ubuntu:~/0x11$
```

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x11-python-network_1
File: 0-hbtn_status.py
