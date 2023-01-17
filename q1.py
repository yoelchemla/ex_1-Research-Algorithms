import sys
from copy import deepcopy
from sympy import *
import numpy as np
import doctest


def safe_call(f, x, y, z):
    """
    >>> safe_call(f2, 0 ,0, 0)
    0
    >>> safe_call(f1, 1, 2, 3.0)
    6.0
    >>> safe_call(f1, 0, 0, 0.0)
    0.0
    >>> safe_call(f1, 5, 6, 7)
    Traceback (most recent call last):
        ...
    Exception: invalid
    >>> safe_call(f1, 5, 9.0, 7.0)
    Traceback (most recent call last):
        ...
    Exception: invalid
    """
    ann_x = f.__annotations__.get('x')
    ann_y = f.__annotations__.get('y')
    ann_z = f.__annotations__.get('z')
    if ((type(x) == ann_x or ann_x is None) and (type(y) == ann_y or ann_y is None)
            and (type(z) == ann_z or ann_z is None)):
        return f(x, y, z)
    else:
        raise Exception("invalid")


def f1(x: int, y: int, z: float):
    return x + y + z


def f2(x: int, y: int, z):
    return x + y + z


if __name__ == "__main__":
    doctest.testmod()

    try:
        print("Check 1 exception: f1(x: int, y: int, z: float)")
        print("Send: (f1, 5, 6, 7)")
        print(safe_call(f1, 5, 6, 7))
    except Exception as e:
        print("exception")

        print()
        print()

    try:
        print("Check 2 exception: f1(x: int, y: int, z: float)")
        print("Send: (f1 , 5, 9.0, 7.0)")
        print(safe_call(f1, 5, 9.0, 7.0))
    except Exception as e:
        print("exception")

        print()
        print()

    try:
        print("Check 3 pass: f1(x: int, y: int, z: float)")
        print("Send: (f1 , 5, 6, 7.0)")
        print(safe_call(f1, 5, 6, 7.0))
    except Exception as e:
        print("valid")

    print()
    print()

    try:
        print("Check 4 pass: f2(x: int, y: int, z)")
        print("Send: (f2 , 5, 6, 7)")
        print(safe_call(f2, 5, 6, 7))
    except Exception as e:
        print("valid")

    print()
    print()

    try:
        print("Check 5 exception: f2(x: int, y: int, z)")
        print("Send: (f2 , 5, 6.0, 7.0)")
        print(safe_call(f2, 5, 6.0, 7.0))
    except Exception as e:
        print("exception")

    try:
        print("Check 6 pass: f1(x: int, y: int, z: float)")
        print("Send: (f1 , 0, 0, 0.0)")
        print(safe_call(f1, 0, 0, 0.0))
    except Exception as e:
        print("valid")

    print()
    print()

    try:
        print("Check 7 pass: f2(x: int, y: int, z)")
        print("Send: (f2 , 0, 0, 0.0)")
        print(safe_call(f2, 0, 0, 0))
    except Exception as e:
        print("valid")
