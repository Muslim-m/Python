#1. Sort a Dictionary by Value
#Write a Python script to sort (ascending and descending) a dictionary by value.
# Sort dictionary by value
products = {'Product1': 10, 'Product2': 20, 'Product3': 30, 'Product4': 45, 'Product5': 88, 'Product6': 17, 'Product7': 33}
sorted_asc = dict(sorted(products.items(), key=lambda item: item[1]))
sorted_desc = dict(sorted(products.items(), key=lambda item: item[1], reverse=True))
print("Sorted by value (ascending):", sorted_asc)
print("Sorted by value (descending):", sorted_desc)

#2.Write a Python script to add a key to a dictionary.
#I provide two approach to solve it , in first , I use Square Bracket Notation, whereas in second one , i use  the update() Method:

my_dic = {0: 10, 1: 20}
my_dic[2] = 30
print("Updated dictionary (Method 1):", my_dic)

# Method 2: Using update() method
my_dic = {0: 10, 1: 20}
my_dic.update({2: 30})
print("Updated dictionary (Method 2):", my_dic)
#Concatenate Multiple Dictionaries
#3.Write a Python script to concatenate the following dictionaries to create a new one.
# I privide two approach to this puzzle
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
# Method 1: Using union operator (Python 3.9+)
combined_dict = dic1 | dic2 | dic3
print("Combined dictionary (Union Operator):", combined_dict)
# Method 2: Using dictionary unpacking
combined_dict2 = {**dic1, **dic2, **dic3}
print("Combined dictionary (Unpacking):", combined_dict2)

#4 Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
num=int(input("Enter num:"))
my_dic={x:x*x for x in range(1,num+1)}
print(my_dic)
#5 Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
my_dic={x:x**2 for x in range(1, 16)}
print(my_dic)
                                                  #Set Exercises
#1.Write a Python program to create a set.
set_list = {1, 2, 3, 'apple', 'Camel'}
for item in set_list:
    print(item)
#2.Write a Python program to iterate over sets.
my_set={1,2,3,'apple', 'Tolic'}
for item in my_set:
    print(item)
#3.Write a Python program to add member(s) to a set.
my_set={1,2,3,'apple', 'Tolic'}
my_set.add(8)
my_set.add("Muslim")
print("Updated set:",set_list)
#4.Write a Python program to remove item(s) from a given set.
fruits_set = {'apple', 'quince', 'banana', 'pear', 'cherry'}
fruits_set.discard('pear')
print("Removed set (using discard):", fruits_set)

# 5.Write a Python program to remove an item from a set if it is present in the set.
my_set = {1, 2, 3, 4, 5}
my_set.discard(3)
print("After discarding 3:", my_set)
my_set.discard(10) # No effect if 10 is not present
print('After trying  to discard 10( not in this set >>>', my_set)
