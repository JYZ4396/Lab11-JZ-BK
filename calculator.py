"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def log(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Invalid input: log base and argument must be positive, and base cannot be 1")
    return math.log(a, b)

def exp(a, b):
    return a ** b


