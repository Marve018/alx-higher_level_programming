#!/usr/bin/python3
"""
script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

from urllib import request
from urllib import parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    data_encoded = parse.urlencode(data).encode('ascii')

    with request.urlopen(url, data=data_encoded) as response:
        print(response.read().decode('utf-8'))
