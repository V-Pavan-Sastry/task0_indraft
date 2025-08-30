# Q12) Write a program to merge two dictionaries.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
merged_dict =dict1.copy()
for key, value in dict2.items():
    merged_dict[key] = value
print("Merged Dictionary:", merged_dict)

# Example Input/Output:
# Dictionary 1: {'a': 1, 'b': 2, 'c': 3}
# Dictionary 2: {'d': 4, 'e': 5, 'f': 6}
# Merged Dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}