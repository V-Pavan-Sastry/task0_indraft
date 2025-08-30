# Q16) Write a program to find all prime numbers in a given range.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
prime_numbers = [num for num in range(start, end + 1) if is_prime(num)]
print(f"Prime numbers between {start} and {end} are: {prime_numbers}")

# Example Input/Output:
# Enter the start of the range: 1       
# Enter the end of the range: 10
# Prime numbers between 1 and 10 are: [2, 3, 5, 7]