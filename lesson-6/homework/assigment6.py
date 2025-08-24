#1.Given a string txt, insert an underscore (_) after every third character.
# If a character is a vowel or already has an underscore after it,
# shift the underscore placement to the next character. No underscore should be added at the end.
def insert_underscore(txt):
    vowels = "aeiouAEIOU"
    result = ""
    count = 0  # counts characters since last underscore

    for i, char in enumerate(txt):
        result += char
        count += 1

        # Check if we need to insert underscore
        if count == 3:
            # Only insert if not vowel and next char is not underscore
            if i + 1 < len(txt) and txt[i] not in vowels and txt[i+1] != "_":
                result += "_"
            count = 0  # reset counter after trying to insert underscore

    return result

# Example usage
txt = "abcdefghijk"
print(insert_underscore(txt))

#2.The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.
def square_while(n):
    k=0

    while k<n:
        print(k**2)
        k+=1
n=int(input("Enter value n:"))

square_while(n)

#3.1. Loop-Based Exercises
n=5
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    print()
    i+=1
#3.2 Calculate sum of all numbers from 1 to a given number
number=int(input("Enter  number:"))
sum=0
i=1
while i<=number:
    sum+=i
    i+=1
print("Sum is ",sum)


# Exercise 4: Print multiplication table of a given number
num=int(input("Enter  a number:"))
multiple=1
while multiple<=10:
    print(f" {num}*{multiple}=", num*multiple )
    multiple+=1

#Exercise 6: Count the total number of digits in a number
num=int(input("Enter a number:"))
count=0
if num==0:
    count=1
else:
    if num<0:
        num=num
    while num > 0:
        count += 1
        num //= 10

print(count)
#Exercise 7: Print reverse number pattern
n = 5   # you can change this number
i = n

while i > 0:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i -= 1
#Exercise 8: Print list in reverse order using a loop
#list1 = [10, 20, 30, 40, 50]
list1 = [10, 20, 30, 40, 50]
i=len(list1)-1
while i>=0:
    print(list1[i])
    i-=1
# or
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)
#Exercise 9: Display numbers from -10 to -1 using a for loop
for x in range(-10, 0):
    print(x)
#Exercise 10: Display message “Done” after successful loop execution
print("Done!")
for x in range(0,5):
    print(x)
else:
    print("Done!")
#Exercise 11: Print all prime numbers within a range
start = 25
end = 50

print(f"Prime numbers between {start} and {end}:")

for num in range(start, end + 1):
    if num > 1:  # primes are greater than 1
        is_prime = True
        for i in range(2, int(num**0.5) + 1):  # check divisors up to √num
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

# Exercise 12: Display Fibonacci series up to 10 terms

n_terms = 10
a, b = 0, 1
count = 0

print("Fibonacci sequence:")
while count < n_terms:
    print(a, end="  ")
    a, b = b, a + b   # update values
    count += 1
#Exercise 13: Find the factorial of a given number

n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i  

print("Factorial:", fact)


# 4. Return Uncommon Elements of Lists
# Task
# Return the elements that are not common between two lists. The order of elements does not matter.
#
# Examples
# Input: list1 = [1, 1, 2], list2 = [2, 3, 4]
# Output: [1, 1, 3, 4]
#
# Input: list1 = [1, 2, 3], list2 = [4, 5, 6]
# Output: [1, 2, 3, 4, 5, 6]
#
# Input: list1 = [1, 1, 2, 3, 4, 2], list2 = [1, 3, 4, 5]
# Output: [2, 2, 5]
def uncommon_elements(list1, list2):
    result = []

    # Add elements from list1 that are not in list2
    for x in list1:
        if x not in list2:
            result.append(x)

    # Add elements from list2 that are not in list1
    for y in list2:
        if y not in list1:
            result.append(y)

    return result


# Examples
print(uncommon_elements([1, 1, 2], [2, 3, 4]))  # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]
