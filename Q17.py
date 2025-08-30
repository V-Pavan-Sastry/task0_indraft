# Q17) Write a program to check if two strings are anagrams.
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print(f"First string considered as input : {str1}")
print(f"Second string considered as input : {str2}")
if are_anagrams(str1, str2):
    print(f'"{str1}" and "{str2}" are anagrams.')
else:
    print(f'"{str1}" and "{str2}" are not anagrams.')   

# Example Input/Output:

# Enter the first string: care
# Enter the second string: race
# First string considered as input : care
# Second string considered as input : race
# "care" and "race" are anagrams.

# Enter the first string: pandas
# Enter the second string: numpy
# First string considered as input : pandas
# Second string considered as input : numpy
# "pandas" and "numpy" are not anagrams.