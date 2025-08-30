# Q6) Write a program to check if a string is a palindrome.

def is_palindrome(s):
    return s == s[::-1]
string = input("Enter a string: ")
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')

# Example Input/Output:
# Enter a string: racecar
# "racecar" is a palindrome.

# Enter a string: ram
# "ram" is not a palindrome.