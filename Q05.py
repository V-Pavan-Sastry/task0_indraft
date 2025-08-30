# Q5)Write a program to count vowels and consonants in a string.
def count_vowels_and_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = sum(1 for char in s if char in vowels)
    c_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return v_count, c_count

string = input("Enter a string: ")
vowels_count, consonants_count = count_vowels_and_consonants(string)
print(f"Number of vowels: {vowels_count}")
print(f"Number of consonants: {consonants_count}")

# Example Input/Output:
# Enter a string: rockstar
# Number of vowels: 2
# Number of consonants: 6