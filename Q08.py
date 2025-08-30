# Q8) Write a program to find the largest and smallest number in a list.
numbers = list(map(int, input("Enter numbers to be taken in the list seperated by space: ").split()))
print(f"List considered as input : {numbers}")
largest = max(numbers)
smallest = min(numbers)
print(f"The largest number in the list is: {largest}")
print(f"The smallest number in the list is: {smallest}")

# Example Input/Output:
# List considered as input : [20, 3, 1, 3, 14, 34, 25]
# The largest number in the list is: 34
# The smallest number in the list is: 1