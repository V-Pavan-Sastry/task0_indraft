######### swap two numbers without third variable ######

print("\n ########### swap two numbers without third variable ######\n")
num1=10
num2=20
print("Before Swapping")
print(f"Num 1: {num1}")
print(f"Num 2: {num2}")

num1 = num1 +num2
num2 = num1- num2
num1 = num1 -num2

print("After Swapping")
print(f"Num 1: {num1}")
print(f"Num 2: {num2}")

######### function to check if a number is even or odd ######

print("\n ########### function to check a number is even or odd######\n")
def is_even_or_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
num1=10
num2=33
print("Numbers considered for test")
print(f"Num 1: {num1} is {is_even_or_odd(num1)}")
print(f"Num 2: {num2} is {is_even_or_odd(num2)}")

