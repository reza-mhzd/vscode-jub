""" 
this module execute 4 principle operation in mathematics
author: reza mohammdadizadeh
date: 11/3/2025
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

if __name__ == "__main__":
    print("this method called directly")
    assert add(1, 2) == 3, "this isn't good"
    assert multiply(2, 3) == 6, "this is wrong"
else:
    print(f"change name? {__name__}")