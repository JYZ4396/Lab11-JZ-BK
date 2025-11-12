"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def logarithm(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Invalid input: log base and argument must be positive, and base cannot be 1")
    return math.log(a, b)

def exp(a, b):
    return a ** b

def square_root(a):
    """Return the square root of a, raising ValueError if a < 0."""
    try:
        if a < 0:
            raise ValueError("Cannot take square root of a negative number")
        return math.sqrt(a)
    except TypeError:
        raise ValueError("Input must be a number")

def hypotenuse(a, b):
    """Return the hypotenuse using Pythagorean theorem."""
    try:
        return math.hypot(a, b)
    except TypeError:
        raise ValueError("Both inputs must be numbers")

