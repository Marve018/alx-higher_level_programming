#!/usr/bin/python3
"""Using sys and requests module to send a post request"""

import requests
import sys


if __name__ == "__main__":
    # get the URL from the command line
    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"

    data = {'q': letter}
    response = requests.post(url, data=data)

    try:
        parsed_response = response.json()

        if parsed_response == {}:
            print("No result")
        else:
            print("[{}] {}".format(parsed_response.get(
                "id"), parsed_response.get("name")))
    except ValueError:
        print("Not a valid JSON")
