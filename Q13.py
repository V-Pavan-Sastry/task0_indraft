# Q13) Write a function to find the second largest number in a list.

def second_largest(numbers):
    if len(numbers) < 2:
        return None
    temp=numbers #declare a temporary list
    temp.remove(max(temp)) #remove the largest number
    return max(temp) #return the largest number from the modified list

lst = list(map(int, input("Enter numbers to be taken in the list seperated by space: ").split()))
print(f"List considered as input : {lst}")
print(f"The second largest number in the list is: {second_largest(lst)}")

# Example Input/Output:
# Enter numbers to be taken in the list seperated by space: 10 20 30 90 50
# List considered as input : [10, 20, 30, 90, 50]
# The second largest number in the list is: 50