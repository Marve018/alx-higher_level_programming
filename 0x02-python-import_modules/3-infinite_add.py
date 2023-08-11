#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    arg = sys.argv[1:]
    for i in range(len(arg)):
        total += int(arg[i])
    print(total)
