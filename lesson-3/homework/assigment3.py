#1.Create a list containing five different fruits and print the third fruit.
fruits=['apple','pear','banana','limon','kiwi']
print("Name of third fruit:",fruits[2])
#2.Create two lists of numbers and concatenate them into a single list.
numbers1=[1,2,3,4,5]
numbers2=[6,7,8,9,10]
concatenated_list=numbers1+numbers2
print("All numbers in given two lists:",concatenated_list)
#3.Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
new_list = [numbers[0], numbers[len(numbers)//2], numbers[-1]]
print("New List =", new_list)
#4.Create a list of your five favorite movies and convert it into a tuple.
movies=['The Godfather','The Shawshank Redemption','The Dark Knight','Avatar','Angry Men']
movies_tuple=tuple(movies)
print(movies_tuple)
#5.Given a list of cities, check if "Paris" is in the list and print the result.
cities=['London','Man City','Paris','Liverpool','Madrid','Rome']
if 'Paris' in cities:
    print("Paris is in the given list")
else:
    print("Paris is not the given list")
#6.Create a list of numbers and duplicate it without using loops.
original_list = [1, 2, 3,4]
duplicated_list = original_list.copy()
print(duplicated_list)
#7.Given a list of numbers, swap the first and last elements.
numbers=[1,2,3,4,6,7,9,12,21,17]
numbers[0],numbers[-1]=numbers[-1],numbers[0]
print(numbers)
#8.Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
numbers=tuple(range(1,11))
sliced=numbers[3:7]
print(sliced)
#9.Create a list of colors and count how many times "blue" appears in the list.
colors=['yellow','white','red','blue','brown','blue','cyan','purple','blue','green']
color_count=colors.count('blue')
print("Number of times blue appears in the given list:",color_count)
#10.Given a tuple of animals, find the index of "lion".
animals=('chick','zebra','elephant','rabbit','lion','giraffe','bear')
animal_index=animals.index('lion')
print("Index of lion:",animal_index)
#11.Create two tuples of numbers and merge them into a single tuple.
numbers1=(1,3,7,9,17)
numbers2=(2,5,8,12)
merged_numbers=numbers1+numbers2
print("Merged numbers:",merged_numbers)
#12.Given a list and a tuple, find and print their lengths.
value_list=['a','b','d','k','j']
value_tuple=(1,2,4,'q','l','k',10)
print("Length of the list:",len(value_list))
print("Length of tuple:",len(value_tuple))
#13.Create a tuple of five numbers and convert it into a list.
numbers=(10,20,40,70,90)
converted_into_list=list(numbers)
print(converted_into_list)
#14.Given a tuple of numbers, find and print the maximum and minimum values.
numbers=(1,10,9,17,8,11,6)
max_number=max(numbers)
min_number=min(numbers)
print(f"Maximum number: {max_number} \nMinimum number:{min_number}")
#15.Create a tuple of words and print it in reverse order.
words=('My','learning','center','is','MAAB','academy')
reversed_word=words[::-1]
print(reversed_word)



