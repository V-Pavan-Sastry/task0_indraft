# Q15) Write a program to find the common elements between two lists.

list1 = list(map(int, input("Enter numbers to be taken in the first list seperated by space: ").split()))
list2 = list(map(int, input("Enter numbers to be taken in the second list seperated by space: ").split()))
print(f"First list considered as input : {list1}")
print(f"Second list considered as input : {list2}")
common_elements = [element for element in list1 if element in list2]
print(f"The common elements between the two lists are: {common_elements}")

# Example Input/Output:
# Enter numbers to be taken in the first list seperated by space: 10 30 40 3
# Enter numbers to be taken in the second list seperated by space: 3 11 40 30
# First list considered as input : [10, 30, 40, 3]
# Second list considered as input : [3, 11, 40, 30]
# The common elements between the two lists are: [30, 40, 3]