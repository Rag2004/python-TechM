import calculator

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

   
    result = calculator.divide(num1, num2)
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter numbers.")
