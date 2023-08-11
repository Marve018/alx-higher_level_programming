#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg = sys.argv[1:]
    arg_len = len(arg)

    if arg_len > 1:
        print(f"{arg_len} arguments:")
    elif arg_len == 1:
        print(f"{arg_len} argument:")
    else:
        print("0 arguments.")

    for i in range(arg_len):
        print(f"{i + 1}: {arg[i]}")
