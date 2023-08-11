#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg = sys.argv[1:]
    arg_len = len(arg)

    if arg_len > 1:
        print("{:d} arguments:" .formart(arg_len))
    elif arg_len == 1:
        print(f"{:d} argument:" .formart(arg_len))
    else:
        print("0 arguments.")

    for i in range(arg_len):
        print(f"{:d}: {:s}" .formart(i + 1, arg[i]))
