# Q1)Write a program to swap two numbers without using a third variable.
num1 = int(input("Enter first number (num1): "))
num2 = int(input("Enter second number (num2): "))
print(f"Before swapping: num1 = {num1}, num2 = {num2}")
num1, num2 = num2, num1
print(f"After swapping: num1 = {num1}, num2 = {num2}")

# Example Input/Output:
# Enter first number (num1): 23
# Enter second number (num2): 24
# Before swapping: num1 = 23, num2 = 24
# After swapping: num1 = 24, num2 = 23