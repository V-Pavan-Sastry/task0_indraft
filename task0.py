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

######## factorial of a number.######

print("\n ########### factorial of a number ######\n")
def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
num1=7
num2=4
print("Numbers whose factorial is found")
print(f"Factorial of Num 1: {num1} is {fact(num1)}")
print(f"Factorial of Num 2: {num2} is {fact(num2)}")

########## reverse a string ####### 
print("\n ########### reverse a string ######\n")
def reverse_str(str1:str):
    str2=str1[::-1]
    return str2
s1="Hello"
s2="Python"
print("Strings that are reversed")
print(f"s1: {str(s1)}  ===> s1 after reversing: {reverse_str(s1)}")
print(f"s2: {str(s2)}  ===> s2 after reversing :{reverse_str(s2)}")

########## count vowels and consonants in a string ####### 
print("\n ###########  count vowels and consonants in a string ######\n")
def count_vowels_and_consonants(str1:str):
    vowels=0
    consonants=0
    for i in str1:
        if i in ['a','e','i','o','u']:
            vowels+=1
        else:
            consonants+=1
    return vowels , consonants
s1="Hello"
s2="Python"
s1_vowels,s1_consonants=count_vowels_and_consonants(s1)
s2_vowels,s2_consonants=count_vowels_and_consonants(s2)
print("Strings that are reversed")
print(f"s1: {str(s1)}  ===> no of vowels : {s1_vowels} and consonants: {s1_consonants}")
print(f"s2: {str(s2)}  ===> no of vowels : {s2_vowels} and consonants: {s2_consonants}")

##########  check if a string is a palindrome.####### 
print("\n ###########   check if a string is a palindrome. ######\n")
def check_palindrome(str1:str):
    s=str1.upper() #covert all chars to uppercase
    if s==s[::-1]:
        return "a palindrome"
    else:
        return "not a palindrome"
s1="Hello"
s2="Racecar"
print("Strings that are checked for palindrome ")
print(f"s1: {str(s1)}  is {check_palindrome(s1)}")
print(f"s2: {str(s2)}  is {check_palindrome(s2)}")


