#Q21) Write a program to implement binary search.
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
arr = list(map(int, input("Enter sorted numbers separated by space: ").split()))
target = int(input("Enter the number to search: "))
result = binary_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")  

# Example Input/Output:
# Enter sorted numbers separated by space: 10 24 34 46 78 91
# Enter the number to search: 78
# Element found at index 4

# Enter sorted numbers separated by space: 10 14 56 78
# Enter the number to search: 65
# Element not found in the list