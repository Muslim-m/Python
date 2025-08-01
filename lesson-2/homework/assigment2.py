#Homework Exercises
#1. Age Calculator
#Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

name=str(input('Enter name: '))
date_of_birth= 2025-int(input("Enter birth date: ")) 

print("User's name is : ", name)
print("User's age is : ", date_of_birth)

##2 Extract Car Names

#Extract car names from the following text:
#txt = 'LMaasleitbtui'
txt = 'LMaasleitbtui'.lower()  # Convert to lowercase for easier comparison

car_names = ['tesla', 'audi', 'subaru', 'bmw', 'ford', 'kia', 'honda', 'toyota', 'mazda', 'jeep']

found_cars = []

for car in car_names:
    temp_txt = list(txt)
    found = True
    for char in car:
        if char in temp_txt:
            temp_txt.remove(char)
        else:
            found = False
            break
    if found:
        found_cars.append(car)

print("Extracted car names:", found_cars)
#3. Extract Car Names
#Extract car names from the following text:
#txt = 'MsaatmiazD'
txt = 'MsaatmiazD'.lower()

car_names = ['tesla', 'audi', 'subaru', 'bmw', 'ford', 'kia', 'honda', 'toyota', 'mazda', 'jeep']

found_cars = []

for car in car_names:
    temp_txt = list(txt)
    found = True
    for char in car:
        if char in temp_txt:
            temp_txt.remove(char)
        else:
            found = False
            break
    if found:
        found_cars.append(car)

print("Extracted car names:", found_cars)

    

#4. Extract Residence Area
#Extract the residence area from the following text:
txt="I'am John. I am from London"
x=txt.split(" ")[5]
print(x)



#5. Reverse String
#Write a Python program that takes a user input string and prints it in reverse order.

text=str(input("Enter one word: "))[::-1]
print(text)


#6.Count Vowels
#Write a Python program that counts the number of vowels in a given string.



txt = input("Enter your text: ")
print(txt)

vowels = 'aeiouAEIOU'
count = 0

for c in txt:
    if c in vowels:
        count += 1

print('Number of vowels in this text is', count)



# 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.


a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))

li=[i for i in range(a,b+1)]
max_number=max(li)
print("Range list: ",li )
print("Max number is: ", max_number)


# 8.Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

a=input("Enter a word:")
if a.lower()==a[::-1].lower():
    print(f"{a} is palindrome")
else:
    print(f"{a} is not palindrome")

# 9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user

email_address=input('Enter email address:')
if '@' in email_address:
    domain=email_address.split('@')[1]
    print('Domain of email address is ', domain)
else:
    print("Invalid email_address")
    
# 10. Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.
    
import random
import string

# Password length
length = 12

# Characters to choose from
letters = string.ascii_letters        # a-zA-Z
digits = string.digits                # 0-9
special_chars = string.punctuation    # !@#$%^&*()_+...

# Combine all characters
all_chars = letters + digits + special_chars

# Randomly choose characters
password = ''.join(random.choice(all_chars) for _ in range(length))

print("Generated Password:", password)  
    
    





