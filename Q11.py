# Q11) Write a program to count the frequency of each element in a list.

lst = list(map(int, input("Enter numbers to be taken in the list seperated by space: ").split()))
print(f"List considered as input : {lst}")
freq = {}
for item in lst:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1
print("Frequency of each element in the list:",freq)

# Example Input/Output:
# Enter numbers to be taken in the list seperated by space: 2 3 2 4 2 1 4 5 7 8
# List considered as input : [2, 3, 2, 4, 2, 1, 4, 5, 7, 8]
# Frequency of each element in the list: {2: 3, 3: 1, 4: 2, 1: 1, 5: 1, 7: 1, 8: 1}