# Q20) Write a program to count the number of words in a text file.
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            print(words)
            return len(words)
    except FileNotFoundError:
        return "File not found. Please check the file path."
    
print(count_words_in_file('sample.txt'))

# Example Input/Output:
# ['hello', 'python', 'is', 'a', 'simple', 'language', 'anybody', 'can', 'learn', 'it']
# 10
