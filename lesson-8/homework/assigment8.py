###Python Exception Handling: Exercises, Solutions, and Practice
#1.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
def devide_numbers(a, b):
    try:
        result = a / b
        print(result)

    except ZeroDivisionError:
        print("Cannot divide by zero!!")
a = int(input("Enter a:"))
b = int(input("Enter b:"))
devide_numbers(a, b)
# 2.Write a Python program that prompts the user to input an integer and raises a ValueError exception
# if the input is not a valid integer.
user_input=input("Please enter integer value:")
try:
    number=int(user_input)
    print(f"You  entered the integer: {number}")
except ValueError:
    print("Invalid input!! Please,enter a valid integer!!")
#3.Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
filename = "index.txt"
try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content")
        print(content)
except FileNotFoundError:
    print(f"Error!,The file {filename} does not exist")
#4.Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
def get_two_numbers():
    num1=input("Enter the first number:")
    num2=input("Enter the second number:")
    try:
        number1=int(num1)
        number2=int(num2)
        print(f"You entered the numbers:{number1} and {number2}")
        return number1, number2
    except ValueError:
        print("Invalid input! Both inputs must be numerical values.")
get_two_numbers()
#5.Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue
filename = "example.txt"

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except PermissionError:
    print(f"Permission denied: You do not have access to open '{filename}'.")
except FileNotFoundError:
    print(f"File not found: '{filename}' does not exist.")
#6.Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
my_list=[10,20,30,40,50,60]
index=7
try:
    value=my_list[index]
    print(f"The element at index {index} is {value}.")
except IndexError:
    print(f"The element at index {index} is out of range")
#7.Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    user_input=input("Enter a number:")
    number=float(user_input)
    print(f"You entered:{number}")
except KeyboardInterrupt:
    print("\nInput canlled by  the user")
except ValueError:
    print("Invalid input:Enter a valid number")
#8.Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
try:
    numerator=float(input("Enter a numerator:"))
    denominator=float(input("Enter a  denominator:"))
    result=numerator/denominator
    print(f"The result of {numerator}/{denominator} is {result}")
except ArithmeticError as e:
    print(f"ArithmeticError occurred:{e} ")
except ValueError as k:
    print(f"Invalid input: Please enter numeric values .{k}")
#9.Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

filename = "example.txt"

try:
    # Try to open the file in text mode (default encoding)
    with open(filename, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except UnicodeDecodeError:
    print(f"UnicodeDecodeError: Cannot decode the contents of '{filename}' due to encoding issues.")
except FileNotFoundError:
    print(f"File not found: '{filename}' does not exist.")
except PermissionError:
    print(f"Permission denied: You do not have access to open '{filename}'.")
#10.Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
try:
    my_list=[1,3,2,56,9,5]
    my_list.push(8)
except AttributeError as e:
    print(f"AttributeError occurred:{e}")
#correct way to add element for list
my_list.append(8)
print("Updated list:",my_list)
#Python File Input Output: Exercises, Practice, Solution
#1.Write a Python program to read an entire text file.
file_path="index.txt"
try:
    with open(file_path,"r") as file:
        file_content=file.read()
    print(file_content)
except FileNotFoundError:
    print(f"Error:The file {file_path} was not found")
#2.Write a Python program to read first n lines of a file.
file_path="index.txt"
try:
    with open(file_path, "r") as file:
        first_line=file.readline()
    print(first_line.strip())
except FileNotFoundError:
    print(f"The file {file_path} was not found")
#3.Write a Python program to append text to a file and display the text.
from sys import exception

file_path="index.txt"
text_to_append="This is new lesson for me"
try:
    with open(file_path, "a") as file:
        file.write(text_to_append+'\n')
    print(f"Text appended to {file_path} successfully.")
except exception() as e:
    print(f"Error appending to file {e}")
#4.Write a Python program to read last n lines of a file.
file_path="index.txt"
n=10
try:
    with open(file_path, "r") as file:
        line=file.readline()
        last_n_line=line[-n:]
        for line in last_n_line:
            print(line.strip())
except FileNotFoundError:
    print(f"The file {file_path} was not found")
#5.Write a Python program to read a file line by line and store it into a list.
file_path="index.txt"
lines_list=[]
try:
    with open(file_path, "r") as file:
      for line in file:
          lines_list.append(line.strip())
    print("Lines stored in the list")
    print(lines_list)
except FileNotFoundError:
    print(f"Error:The file {file_path} was not found")
#6.Write a Python program to read a file line by line and store it into a variable.
file_path="index.txt"
list_variable=[]
try:
    with open(file_path,"r") as file:
        for line in file:
            list_variable.append(line.strip())
    print("Lines stored in variable")
    print(list_variable)
except FileNotFoundError:
    print(f"Error:The file {file_path} was not found")
#7.Write a Python program to read a file line by line and store it into an array.
file_path = "example.txt"

try:
    # Initialize an empty list (array)
    lines_array = []

    with open(file_path, "r") as file:
        for line in file:
            lines_array.append(line.strip())  # Remove newline characters

    print("Lines stored in array:")
    print(lines_array)

except FileNotFoundError:
    print(f"The file {file_path} was not found.")
#8.Write a Python program to find the longest words.
file_path="index.txt"
try:
    with open(file_path,"r") as file:
        text=file.read()
    import string
    text = text.translate(str.maketrans('', '', string.punctuation))
    words=text.split()
    max_length=max(len(word) for word in words)
    longest_words=[word for word in words if len(word)==max_length]
    print("Longest word(s) in the file:")
    for word in longest_words:
        print(word)
except FileNotFoundError:
    print(f"The file {file_path} was not found.")
#9.Write a Python program to count the number of lines in a text file.
with open(r"index.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)
#10.Write a Python program to count the frequency of words in a file.
import string
from string import punctuation

file_path="index.txt"
with open(file_path,"r") as file:
    text=file.read()
text=text.lower()
text=text.translate(str.maketrans('','',string.punctuation))
words=text.split()
word_frequency={}
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word]=1
for word, freq in word_frequency.items():
    print(f"{word}:{freq}")
#11.Write a Python program to get the file size of a plain file
import  os
file_path="index.txt"
file_size=os.path.getsize(file_path)
print(f"The size of {file_size} is {file_size} bytes")
#12.Write a Python program to write a list to a file.
file_path="index.txt"
my_list=[2,True,"Apple","peach","bread",9,7]
with open(file_path,"w") as file:
    for line in my_list:
        file.write(f"{line}\n")
#13.Write a Python program to copy the contents of a file to another file.
#Method 1
source_file="index.txt"
destination_file="copy_index.txt"
with open(source_file,"r") as src:
    content=src.read()
with open(destination_file,"w") as dest:
    dest.write(content)
print(f"Content of {source_file} have copies to {destination_file} .")
#Method 2
file_path="S.txt"
with open("C.txt","w") as fw,open("S.txt","r") as fr:
    fw.writelines(line for line in fr)
#14.Write a Python program to combine each line from the first file with the corresponding line in the second file.
# File paths
file1 = "file1.txt"
file2 = "file2.txt"
output_file = "combined.txt"

# Open all files using 'with'
with open(file1, "r") as f1, open(file2, "r") as f2, open(output_file, "w") as out:
    # Use zip() to iterate through both files simultaneously
    for line1, line2 in zip(f1, f2):
        # Strip newline characters and combine lines with a space
        combined_line = line1.strip() + " " + line2
        out.write(combined_line)

print(f"Lines from '{file1}' and '{file2}' have been combined into '{output_file}'.")
#15.Write a Python program to read a random line from a file.
import  random
with open("index.txt","r") as choicefile:
    linelist=choicefile.readlines()
choice=random.choice(linelist)
print(choice)
#16.Write a Python program to assess if a file is closed or not.
file_path = "index.txt"

with open(file_path, "r") as f:
    print("Is the file closed inside with block?", f.closed)  # False

print("Is the file closed after with block?", f.closed)  # True
#17.Write a Python program to remove newline characters from a file.
input_file="index.txt"
output_file="index_no_newlines.txt"
with open(input_file,"r") as fr , open(output_file,"w") as fw:
    for line in fr:
        fw.write(line.strip() +" \n")
print(f"Newlines removed and content saved to {output_file}.")
#18.Write a Python program that takes a text file as input and returns the number of words in a given text file.
file_path="index.txt"
with open(file_path,"r") as file:
    text=file.read()
words=text.strip()
num_words=len(words)
print(f"The file {file_path} contains {num_words} words.")
#19.Write a Python program to extract characters from various text files and put them into a list.
# List of file names
files = ["file1.txt", "file2.txt", "file3.txt"]  # Replace with your files
all_characters = []

for file_path in files:
    with open(file_path, "r") as f:
        # Read the file and extend the list with all characters
        all_characters.extend(list(f.read()))

print("All characters from files:")
print(all_characters)
#20.Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
import  string
for letter in string.ascii_uppercase:
    filename=f"{letter}.txt"
    with open(filename,'w') as file:
        file.write(f"This is file {filename}\n")
print("26 text files from A.text to Z.text have been created")
#21.Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.
import  string
# Number of letters per line
letters_per_line = 5  # You can change this number

# Open the file to write
with open("alphabet.txt", "w") as f:
    alphabet = string.ascii_uppercase  # 'A' to 'Z'

    for i in range(0, len(alphabet), letters_per_line):
        # Slice the string to get letters_per_line letters
        line = alphabet[i:i+letters_per_line]
        f.write(line + "\n")  # Write the line with a newline

print("File 'alphabet.txt' created with letters arranged per line.")



