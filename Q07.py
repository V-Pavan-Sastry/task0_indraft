# Q7) Write a program to print the Fibonacci series up to n terms.

n = int(input("Enter the number of terms: "))

a, b = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence up to", n, "term:")
    print(a)
else:
    print("Fibonacci sequence up to", n, "terms:")
    while count < n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        count += 1

# Example Input/Output:
# Enter the number of terms: 7
# Fibonacci sequence up to 7 terms:
# 0 1 1 2 3 5 8 % 