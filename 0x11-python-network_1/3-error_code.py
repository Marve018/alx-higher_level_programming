#!/usr/bin/python3
"""
Manage urllib.error.HTTPError exceptions and print: Error code:
"""
import sys
from urllib import error, request


if __name__ == "__main__":

    url = request.Request(sys.argv[1])
    try:
        with request.urlopen(url) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
