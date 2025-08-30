# Q23) Write a program to rotate a list by k positions.
lst = list(map(int, input("Enter numbers to be taken in the list seperated by space: ").split()))
k = int(input("Enter the number of positions to rotate the list by: "))
n = len(lst)
k = k % n  # Handle cases where k is greater than the length of the list
rotated_lst = lst[-k:] + lst[:-k]
print(f"List considered as input : {lst}")
print(f"List after rotating by {k} positions: {rotated_lst}")

# Example Input/Output:
# Enter numbers to be taken in the list seperated by space: 10 50 5 67 3 5 6
# Enter the number of positions to rotate the list by: 4
# List considered as input : [10, 50, 5, 67, 3, 5, 6]
# List after rotating by 4 positions: [67, 3, 5, 6, 10, 50, 5]