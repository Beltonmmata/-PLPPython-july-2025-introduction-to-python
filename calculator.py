# Basic Calculator Program

# Collect user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

# Perform calculation
if operation == "+":
    result = num1 + num2
    symbol = "+"
elif operation == "-":
    result = num1 - num2
    symbol = "-"
elif operation == "*":
    result = num1 * num2
    symbol = "*"
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        symbol = "/"
    else:
        result = "Undefined (division by zero)"
        symbol = "/"
else:
    result = "Invalid operation"
    symbol = "?"

# Display result
print(f"\nResult: {num1} {symbol} {num2} = {result}")