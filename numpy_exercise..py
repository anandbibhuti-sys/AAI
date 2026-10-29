import numpy as np

#Part 1: Creating and Inspecting Arrays

# 1D example array
arr_1D = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr_1D)
print(type(arr_1D))
print(arr_1D.ndim)
print(arr_1D.shape)
print(arr_1D.dtype)
print("\n++++++++++++++++++++++++\n")

# 2D example array
arr_2D = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2D)
print(type(arr_2D))
print(arr_2D.ndim)
print(arr_2D.shape)
print(arr_2D.dtype)

newarr = arr_1D.reshape(2, 5)
print(newarr)

#Array Indexing and Slicing
print('2nd row: ', arr_2D[1])
print('1st column: ', arr_2D[:,0])
print("\n++++++++++++++++++++++++\n")

#Part 3: Array Operations
print(newarr[1:])
print(newarr[:, 1:])
print(newarr[:, :3])
print("\n++++++++++++++++++++++++\n")

#Part 3: Array Operations
a = np.arange(1, 6)
b = np.arange(10, 15)
print(a)
print(b)
print(a + b)
print(np.add(a, b))
print(np.multiply(a, b))
print(np.sum(a))
print(np.mean(b))
print(np.max(a))
print(np.max(b))
print(np.maximum(a, b))
print(np.minimum(a, b))
print("\n++++++++++++++++++++++++\n")

#Part 4: Handling Large Datasets
data = np.random.rand(1000000)
print(data)
print(np.mean(data))
print(np.median(data))
print("\n++++++++++++++++++++++++\n")

#Part 5: Practice Challenges
array_3d = np.random.randint(0, 101, (3, 3, 3))
print(array_3d)
print(np.sum(array_3d))
max_axis0 = np.max(array_3d, axis=0)
print("Maximum along axis 0:\n", max_axis0)
min_axis0 = np.min(array_3d, axis=0)
print("\nMinimum along axis 0:\n", min_axis0)
print("\n++++++++++++++++++++++++\n")
#Create a linear space of 20 numbers from 1 to 100 and reshape into a 4x5 array
#Find the standard deviation of all the columns

linear_array = np.linspace(1, 100, 20).reshape(4, 5)
column_std = np.std(linear_array, axis=0)

print("Reshaped 4x5 Array:")
print(linear_array)
print("\nStandard Deviation of each column:")
print(column_std)
print("\n++++++++++++++++++++++++\n")
