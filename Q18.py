# Q18) Write a program to implement a simple calculator (using +, -, *, /).
def add(x, y):
    return x + y    
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter choice (1/2/3/4): ")
if choice in ['1', '2', '3', '4']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input")

# Example Input/Output:

# Select operation:
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# Enter choice (1/2/3/4): 1
# Enter first number: 2
# Enter second number: 3
# 2.0 + 3.0 = 5.0

# Select operation:
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# Enter choice (1/2/3/4): 2
# Enter first number: 17
# Enter second number: 3
# 17.0 - 3.0 = 14.0

# Select operation:
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# Enter choice (1/2/3/4): 3
# Enter first number: 23
# Enter second number: 4
# 23.0 * 4.0 = 92.0

# Select operation:
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# Enter choice (1/2/3/4): 4
# Enter first number: 34
# Enter second number: 3
# 34.0 / 3.0 = 11.333333333333334

# Select operation:
# Select operation:
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# Enter choice (1/2/3/4): 6
# Invalid input