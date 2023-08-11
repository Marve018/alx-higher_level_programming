#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    module_names = dir(hidden_4)
    for i in (module_names):
        if i[:2] != "__":
            print("{:s}" .format(i))
