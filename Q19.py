# Q19) Write a program to read command-line arguments using sys.argv.
import sys
if len(sys.argv) < 2:
    print("No command-line arguments provided.")
else:
    print("Command-line arguments:")
    for arg in sys.argv[1:]:
        print(arg) 
# Example Input/Output:
# python3 Q19.py 10 20 40
# Command-line arguments:
# 10
# 20
# 40

# python3 Q19.py 10      
# Command-line arguments:
# 10