# Q9) Write a program to remove duplicates from a list.
lst = list(map(int, input("Enter numbers to be taken in the list seperated by space: ").split()))
print(f"List considered as input : {lst}")
#Using set to remove duplicates
lst_no_duplicates = list(set(lst))
print(f"List after removing duplicates: {lst_no_duplicates}")

# Example Input/Output:
# Enter numbers to be taken in the list seperated by space: 10 20 30 40 10 45 40 20
# List considered as input : [10, 20, 30, 40, 10, 45, 40, 20]
# List after removing duplicates: [40, 10, 45, 20, 30]