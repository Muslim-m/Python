#1. Convert List to 1D Array
#Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.
# Expected Output:
# Original List: [12.23, 13.32, 100, 36.32] One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]
import numpy as n
my_list=[12.23, 13.32, 100, 36.32]
print("Original list:",my_list)

array_1d=n.array(my_list)
print("One dimensional array:",array_1d)

#2. Create 3x3 Matrix (2?10)
# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
# Expected Output: [[ 2 3 4] [ 5 6 7] [ 8 9 10]]
import  numpy as np
arr=np.arange(2,11)
matrix=arr.reshape(3,3)
print(matrix)
#3. Null Vector (10) & Update Sixth Value
# Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.
# [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# Update sixth value to 11 [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]

import numpy as np
vector=np.zeros(10)
print("Original vector:",vector)

vector[5]=11
print("Updated vector:",vector)

#4.Array from 12 to 38
# Write a NumPy program to create an array with values ranging from 12 to 38.
# Expected Output:[12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
import numpy as np
arr=np.arange(12,38)
print("Values from 12 to 38 (exclusive of 38):",arr)

#5. Convert Array to Float Type
# Write a NumPy program to convert an array to a floating type.
# Sample output:
# Original array [1, 2, 3, 4]

import numpy as np
arr=np.array(range(1,6))
fl_convert= arr.astype(float)
print("Array converted to float",fl_convert)

#6. Celsius to Fahrenheit Conversion
#Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.

import numpy as np

# Sample array (Celsius values)
celsius = np.array([0, 12, 45.21, 34, 99.91])

# Convert Celsius to Fahrenheit
fahrenheit = celsius * 9/5 + 32

# Convert Fahrenheit back to Celsius
celsius_back = (fahrenheit - 32) * 5/9

# Print results
print("Values in Celsius degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)
print("Converted back to Celsius:", np.round(celsius_back, 2))


#7. Append Values to Array (Do self-tudy)
# Write a NumPy program to append values to the end of an array.
# Expected Output:
# Original array: [10, 20, 30]
# After append values to the end of the array: [10 20 30 40 50 60 70 80 90]
import numpy as np
my_np_array=np.array([10,20,30])
print("Original array:",my_np_array)
new_my_np_array=np.append(my_np_array,[40, 50, 60, 70, 80, 90])
print("After append values to the end of the array:",new_my_np_array)

#8.Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.

import numpy as np

# Generate a 1D array of 5 random floats
random_floats_1d = np.random.rand(int(10))
print("1D array of random floats:", np.round(random_floats_1d,2))
find_mean=np.mean(random_floats_1d)
print("Mean:",find_mean)
find_median=np.median(random_floats_1d)
print("Median:",find_median)
find_standard=np.std(random_floats_1d)
print("Standard:",find_standard)
#9 Find min and max
#Create a 10x10 array with random values and find the minimum and maximum values.
import numpy as np
arr=np.random.randint( 0,10,size=(10,10))
min_val=arr.min()
max_val=arr.max()
print("Max value:",max_val)
print("Min value",min_val)

#10 Create a 3x3x3 array with random values.
import numpy as np
arr = np.random.randint(0, 10, size=(3, 3, 3))
print("3x3x3 array with random integer values:\n", arr)

