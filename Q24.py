# Q24) Write a program to generate a dictionary where keys are numbers (1–10) and values are their squares.
squares_dict = {num: num**2 for num in range(1, 11)}
print("Dictionary of numbers and their squares:")
print(squares_dict)

# Example Input/Output:
# Dictionary of numbers and their squares:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}