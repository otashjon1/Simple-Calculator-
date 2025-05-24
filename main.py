def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b

def calculator():
    num1 = float(input("Enter the first number: "))
    operator = input("Choose an operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    else:
        result = "Invalid operator!"

    print(f"Result: {result}")

calculator()
