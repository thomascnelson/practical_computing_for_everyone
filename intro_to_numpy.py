# importing the package
import numpy as np

# create an array
my_array = np.array([1,2,3,4,5])
my_array

foo = np.array(range(6))

# create a 2D array from lists
list1 = [0,1,2,3]
list2 = [4,5,6,7]
list3 = [7,8,9,0]
list4 = [1,2,3,4]
my_matrix = np.array([list1, list2, list3, list4])
my_matrix

# built-in methods and attrubutes
print(my_matrix.shape)
print(my_matrix.dtype)

print(my_matrix.max())
print(my_matrix.mean())

print(my_matrix.tolist())
print(my_matrix.T)
print(my_matrix.diagonal())
