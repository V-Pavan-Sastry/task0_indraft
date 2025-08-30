# Q14)Write a function that accepts **kwargs and returns the sum of values.

def sum_of_values(**kwargs):
    return sum(kwargs.values())

result = sum_of_values(a=10, b=20, c=30)
print(f"The sum of values passed as keyword args to the function is: {result}")

# Example Input/Output:
# The sum of values passed as keyword args to the function is: 60