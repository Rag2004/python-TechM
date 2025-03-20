# 1. Investigate Circular Imports
# Fix the circular import problem between module_a.py and module_b.py.
# module_a.py file
def func_a():
    return "Function A"

def call_func_b():
    from module_b import func_b  # Import inside function
    return func_b()

print(call_func_b())
