# Q25) Write a program to find the longest word in a given sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len)
print(f"The longest word in the given sentence is: '{longest_word}'")

# Example Input/Output:
# Enter a sentence: I am student learning python programming
# The longest word in the given sentence is: 'programming'