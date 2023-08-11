#!/usr/bin/python3
import calculator_1 as func

if __name__ == "__main__":
    a = 10
    b = 5
    print(f"{a} + {b} = {func.add(a, b)}")
    print(f"{a} - {b} = {func.sub(a, b)}")
    print(f"{a} * {b} = {func.mul(a, b)}")
    print(f"{a} / {b} = {func.div(a, b)}")
