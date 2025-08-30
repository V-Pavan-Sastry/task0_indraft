#Q22) Write a program to implement bubble sort.

lst = list(map(int, input("Enter numbers to be taken in the list seperated by space: ").split()))
print(f"List before sorting: {lst}")
#bubble sort
for i in range(len(lst)):
    for j in range(0, len(lst)-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(f"List after sorting: {lst}")