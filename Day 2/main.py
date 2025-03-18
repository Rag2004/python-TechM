
# 1. Error Classification - Fixing syntax and logical errors
# Fixed missing colon in for loop
for i in range(5):  
    print(i)

# Fixed division by zero by adding exception handling
try:
    x = 10 / 0  
except ZeroDivisionError:
    x = None
    print("Error: Division by zero")

# Fixed incorrect formula for area of a circle
def calculate_area(radius):
    return 3.14 * radius ** 2  

# 2. Debugging Complex Functions - Handling invalid input

def process_data(data):
    total = 0
    count = 0
    for item in data:
        try:
            total += int(item)
            count += 1
        except ValueError:
            print(f"Skipping invalid item: {item}")  # If item is not a number, skip it
    return total / count if count > 0 else 0  # Avoid division by zero

print(process_data(['10', '20', 'abc', '30']))

# 3. Advanced Debugging Challenge - Preventing division by zero
import random

def unreliable_function():
    number = random.choice([0, 1, 2])
    if number == 0:
        return "Error: Division by zero"  # Prevent crash by checking for zero
    return 10 / number

for i in range(10):
    print(unreliable_function())

# 4. Writing Debug-Friendly Code - Adding error handling

def calculate_discount(price, discount):
    try:
        discount = float(discount)  # Convert discount to float
        return price - (price * discount / 100)
    except ValueError:
        return "Error: Invalid discount format"  # Handle incorrect input

print(calculate_discount(100, '10%'))

# 5. Rubber Duck Debugging - Explain step-by-step
numbers = [1, 2, 3, 4, 5]
result = 1
for num in numbers:
    result *= num  # Multiply result by each number in the list
print("Product:", result)  # Output the final product

# 6. Advanced Challenge - Fixing race conditions with threading
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:  # Use lock to prevent race conditions
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Counter:", counter)  # Now correctly expected to be 200000

# 7. Activity: Debug with Breakpoints - Fixed division by zero

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"  # Added check to prevent crash
    return a / b

a = 10
b = 2  # Fixed division by zero
print(divide(a, b))

# 8. Memory Leaks and Performance Debugging - Optimized function

def efficient_function():
    return [i * 2 for i in range(100000)]  # Using list comprehension for efficiency

print(len(efficient_function()))

# 9. Unexpected None - Fixed missing return statement

def add(a, b):
    return a + b  # Added return statement

print(add(3, 4))

# 10. Silent Failures - Properly handling exceptions
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught an error: {e}")  # Print error message instead of silently failing
