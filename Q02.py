# Q2) Write a function to check if a number is even or odd.
def is_even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number: "))
result = is_even_or_odd(num)
print(f"The number {num} is {result}")
# Example Input/Output:
# Enter a number: 4
# The number 4 is Even
# Enter a number: 7
# The number 7 is Odd