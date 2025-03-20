# 1. Investigate Circular Imports
# Fix the circular import problem between module_a.py and module_b.py.
# module_a.py

def func_a():
    return "Function A"

def call_func_b():
    from module_b import func_b  # Import inside function
    return func_b()

# module_b.py
def func_b():
    return "Function B"

print(call_func_b())

#  2. Dynamic Module Loading
# Write a program that dynamically imports and executes a function from any module specified by the user.

import importlib

module_name = input("Enter module name: ")  
function_name = input("Enter function name: ") 
argument = float(input("Enter argument: ")) 

try:
 
    module = importlib.import_module(module_name)

    func = getattr(module, function_name)
    
    # Execute function and print result
    result = func(argument)
    print("Output:", result)

except ModuleNotFoundError:
    print("Error: Module not found!")
except AttributeError:
    print("Error: Function not found in module!")
except Exception as e:
    print("Error:", e)

# 3. Custom Module with Exception Handling
# Create a custom module calculator.py that handles division by zero and invalid inputs gracefully.

# calculator.py
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return f"Error: {e}"
# main.py
import calculator

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

   
    result = calculator.divide(num1, num2)
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter numbers.")

# 4. Advanced Import Strategies
import importlib

# Module and function to check
module_name = "math"
function_name = "sqrt"

try:
    # Dynamically import the module
    module = importlib.import_module(module_name)

    # Check if the function exists in the module
    if hasattr(module, function_name):
        func = getattr(module, function_name)
        result = func(16) 
        print(f"Result: {result}")
    else:
        print(f"Function '{function_name}' not found in module '{module_name}'.")
except ImportError:
    print(f"Module '{module_name}' could not be imported.")

# 5. Optimize Import Time
# Single import 

import time

start = time.time()
import math  # Import only the required module
end = time.time()

print(f"Single import time: {end - start:.6f} seconds")


# Import Everything (from module import *)

import time

start = time.time()
from math import *  # Importing all functions from the module
end = time.time()

print(f"Wildcard import time: {end - start:.6f} seconds")