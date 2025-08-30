# Q4)Write a function to reverse a string.

def reverse_string(s):
    return s[::-1]

string = input("Enter a string: ")
reversed_str = reverse_string(string)
print(f"The reversed string is: {reversed_str}")

# Example Input/Output:
# Enter a string: raceboat
# The reversed string is: taobecar