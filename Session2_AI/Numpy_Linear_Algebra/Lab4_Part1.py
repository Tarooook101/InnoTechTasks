import numpy as np


# 1. Write a Numpy program to get the Numpy version and show the Numpy build configuration. 
print("\n1. NumPy Version and Build Configuration:")
print(f"NumPy version: {np.__version__}")
print("Build configuration:")
np.show_config()


# 2. Write a NumPy program to test whether none of the elements of a given array are zero. 
print("\n" + "="*50)
print("2. Test whether none of the elements are zero:")
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 0, 3, 4, 5])
print(f"Array 1: {arr1}")
print(f"None are zero: {np.all(arr1 != 0)}")
print(f"Array 2: {arr2}")
print(f"None are zero: {np.all(arr2 != 0)}")


# 3. Write a NumPy program to test if any of the elements of a given array are non-zero.  
print("\n" + "="*50)
print("3. Test if any elements are non-zero:")
arr3 = np.array([0, 0, 0, 0])
arr4 = np.array([0, 0, 1, 0])
print(f"Array 3: {arr3}")
print(f"Any non-zero: {np.any(arr3 != 0)}")
print(f"Array 4: {arr4}")
print(f"Any non-zero: {np.any(arr4 != 0)}")


# 4. Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a number). 
print("\n" + "="*50)
print("4. Test for finiteness:")
arr5 = np.array([1, 2, np.inf, 4, np.nan])
print(f"Array: {arr5}")
print(f"Finite elements: {np.isfinite(arr5)}")


# 5. Write a NumPy program to test elements-wise for positive or negative infinity.  
print("\n" + "="*50)
print("5. Test for infinity:")
arr6 = np.array([1, np.inf, -np.inf, 4, np.nan])
print(f"Array: {arr6}")
print(f"Positive infinity: {np.isposinf(arr6)}")
print(f"Negative infinity: {np.isneginf(arr6)}")
print(f"Any infinity: {np.isinf(arr6)}")

# 6. Write a NumPy program to test element-wise for NaN of a given array. 
print("\n" + "="*50)
print("6. Test for NaN:")
arr7 = np.array([1, 2, np.nan, 4, 5])
print(f"Array: {arr7}")
print(f"NaN elements: {np.isnan(arr7)}")

# 7. Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.
print("\n" + "="*50)
print("7. Element-wise comparisons:")
arr8 = np.array([1, 2, 3, 4, 5])
arr9 = np.array([1, 1, 4, 4, 3])
print(f"Array 1: {arr8}")
print(f"Array 2: {arr9}")
print(f"Greater: {np.greater(arr8, arr9)}")
print(f"Greater or equal: {np.greater_equal(arr8, arr9)}")
print(f"Less: {np.less(arr8, arr9)}")
print(f"Less or equal: {np.less_equal(arr8, arr9)}")


# 8. Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays. 
print("\n" + "="*50)
print("8. Equal comparisons:")
arr10 = np.array([1.0, 2.0, 3.0])
arr11 = np.array([1.0, 2.1, 3.0])
print(f"Array 1: {arr10}")
print(f"Array 2: {arr11}")
print(f"Equal: {np.equal(arr10, arr11)}")
print(f"Close (tolerance): {np.allclose(arr10, arr11, atol=0.2)}")
print(f"Close element-wise: {np.isclose(arr10, arr11, atol=0.2)}")


# 9. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives.  
print("\n" + "="*50)
print("9. Array of zeros, ones, and fives:")
zeros = np.zeros(10)
ones = np.ones(10)
fives = np.full(10, 5)
combined = np.concatenate([zeros, ones, fives])
print(f"Combined array: {combined}")


# 10. Write a NumPy program to create an array of integers from 30 to 70. 
print("\n" + "="*50)
print("10. Integers from 30 to 70:")
arr12 = np.arange(30, 71)
print(f"Array: {arr12}")

# 11. Write a NumPy program to create an array of all even integers from 30 to 70. 
print("\n" + "="*50)
print("11. Even integers from 30 to 70:")
arr13 = np.arange(30, 71, 2)
print(f"Even numbers: {arr13}")

# 12. Write a NumPy program to create a 3x3 identity matrix. 
print("\n" + "="*50)
print("12. 3x3 Identity matrix:")
identity = np.eye(3)
print(identity)


# 13. Write a NumPy program to generate a random number between 0 and 1. 
print("\n" + "="*50)
print("13. Random number between 0 and 1:")
random_num = np.random.random()
print(f"Random number: {random_num}")

# 14. Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last. 
print("\n" + "="*50)
print("14. Vector 15 to 55, excluding first and last:")
arr14 = np.arange(15, 56)
print(f"Full array: {arr14}")
print(f"Without first and last: {arr14[1:-1]}")

# 15. Write a NumPy program to create a 3X4 array and iterate over it. 
print("\n" + "="*50)
print("15. 3x4 array iteration:")
arr15 = np.arange(12).reshape(3, 4)
print("3x4 Array:")
print(arr15)
print("\nIterating over array:")
for i, row in enumerate(arr15):
    for j, element in enumerate(row):
        print(f"Element at ({i},{j}): {element}")


# 16. Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50
print("\n16. Vector with evenly distributed values between 5 and 50:")
arr16 = np.linspace(5, 50, 10)
print(f"Vector: {arr16}")


# 17. Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15. 
print("\n" + "="*50)
print("17. Vector 0-20, change sign from 9 to 15:")
arr17 = np.arange(21)
print(f"Original: {arr17}")
arr17[9:16] *= -1
print(f"Modified: {arr17}")


# 18. Write a NumPy program to multiply the values of two given vectors. 
print("\n" + "="*50)
print("18. Multiply two vectors:")
vec1 = np.array([1, 2, 3, 4, 5])
vec2 = np.array([2, 3, 4, 5, 6])
result = vec1 * vec2
print(f"Vector 1: {vec1}")
print(f"Vector 2: {vec2}")
print(f"Product: {result}")

# 19. Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21. 
print("\n" + "="*50)
print("19. 3x4 matrix with values 10 to 21:")
arr19 = np.arange(10, 22).reshape(3, 4)
print(f"Matrix:\n{arr19}")

# 20. Write a NumPy program to find the number of rows and columns in a given matrix. 
print("\n" + "="*50)
print("20. Find rows and columns:")
test_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
rows, cols = test_matrix.shape
print(f"Matrix:\n{test_matrix}")
print(f"Rows: {rows}, Columns: {cols}")


# 21. Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5. 
print("\n" + "="*50)
print("21. 5x5 zero matrix with diagonal 1,2,3,4,5:")
arr21 = np.zeros((5, 5))
np.fill_diagonal(arr21, [1, 2, 3, 4, 5])
print(f"Matrix:\n{arr21}")

# 22. Write a NumPy program to create a 3x3x3 array filled with arbitrary values. 
print("\n" + "="*50)
print("22. 3x3x3 array with arbitrary values:")
arr22 = np.random.randint(1, 10, (3, 3, 3))
print(f"3D Array:\n{arr22}")


# 23. Write a NumPy program to compute the sum of all elements, the sum of each column and the sum of each row in a given array. 
print("\n" + "="*50)
print("23. Sum calculations:")
arr23 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Matrix:\n{arr23}")
print(f"Sum of all elements: {np.sum(arr23)}")
print(f"Sum of each column: {np.sum(arr23, axis=0)}")
print(f"Sum of each row: {np.sum(arr23, axis=1)}")

# 24. Write a NumPy program to compute the inner product of two given vectors. 
print("\n" + "="*50)
print("24. Inner product of two vectors:")
vec3 = np.array([1, 2, 3])
vec4 = np.array([4, 5, 6])
inner_product = np.dot(vec3, vec4)
print(f"Vector 1: {vec3}")
print(f"Vector 2: {vec4}")
print(f"Inner product: {inner_product}")

# 25. Write a NumPy program to add a vector to each row of a given matrix. 
print("\n" + "="*50)
print("25. Add vector to each row:")
matrix25 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector25 = np.array([10, 20, 30])
result25 = matrix25 + vector25
print(f"Original matrix:\n{matrix25}")
print(f"Vector to add: {vector25}")
print(f"Result:\n{result25}")


# 26. Write a NumPy program to check whether two arrays are equal (element wise) or not. 
print("\n" + "="*50)
print("26. Check if arrays are equal:")
arr26a = np.array([1, 2, 3, 4])
arr26b = np.array([1, 2, 3, 4])
arr26c = np.array([1, 2, 3, 5])
print(f"Array A: {arr26a}")
print(f"Array B: {arr26b}")
print(f"Array C: {arr26c}")
print(f"A equals B: {np.array_equal(arr26a, arr26b)}")
print(f"A equals C: {np.array_equal(arr26a, arr26c)}")


# 27. Write a NumPy program to create a new array of given shape (5,6) and type, filled with zeros. 
print("\n" + "="*50)
print("27. 5x6 zero array:")
arr27 = np.zeros((5, 6), dtype=int)
print(f"Shape: {arr27.shape}")
print(f"Array:\n{arr27}")

# 28. Write a NumPy program to sort a given array by row and column in ascending order. 
print("\n" + "="*50)
print("28. Sort array by rows and columns:")
arr28 = np.array([[9, 2, 3], [1, 8, 7], [6, 4, 5]])
print(f"Original:\n{arr28}")
sorted_rows = np.sort(arr28, axis=1)
print(f"Sorted by rows:\n{sorted_rows}")
sorted_cols = np.sort(arr28, axis=0)
print(f"Sorted by columns:\n{sorted_cols}")

# 29. Write a NumPy program to extract all numbers from a given array less and greater than a specified number. 
print("\n" + "="*50)
print("29. Extract numbers less/greater than 5:")
arr29 = np.array([1, 3, 5, 7, 9, 2, 4, 6, 8])
threshold = 5
less_than = arr29[arr29 < threshold]
greater_than = arr29[arr29 > threshold]
print(f"Original: {arr29}")
print(f"Less than {threshold}: {less_than}")
print(f"Greater than {threshold}: {greater_than}")

# 30. Write a NumPy program to replace all numbers in a given array equal, less and greater than a given number. 
print("\n" + "="*50)
print("30. Replace numbers based on conditions:")
arr30 = np.array([1, 3, 5, 7, 9, 2, 4, 6, 8])
threshold = 5
result30 = arr30.copy()
result30[result30 == threshold] = 100  # equal
result30[result30 < threshold] = -1    # less than
result30[result30 > threshold] = 999   # greater than
print(f"Original: {arr30}")
print(f"Modified: {result30}")
print("(Equal to 5 → 100, Less than 5 → -1, Greater than 5 → 999)")

# 31. Write a NumPy program to create a 4x4 array. Create an array from said array by swapping first and last, second and third columns. 
print("\n" + "="*50)
print("31. Swap columns in 4x4 array:")
arr31 = np.arange(16).reshape(4, 4)
print(f"Original:\n{arr31}")
# Swap columns: first with last, second with third
arr31_swapped = arr31[:, [3, 2, 1, 0]]
print(f"After swapping columns:\n{arr31_swapped}")

# 32. Write a NumPy program to swap rows and columns of a given array in reverse order. 
print("\n" + "="*50)
print("32. Reverse rows and columns:")
arr32 = np.arange(12).reshape(3, 4)
print(f"Original:\n{arr32}")
# Reverse both rows and columns
reversed_arr = arr32[::-1, ::-1]
print(f"Reversed:\n{reversed_arr}")


# 33. Write a NumPy program to multiply two given arrays of the same size element-byelement.
print("\n" + "="*50)
print("33. Element-wise multiplication:")
arr33a = np.array([[1, 2], [3, 4]])
arr33b = np.array([[5, 6], [7, 8]])
result33 = arr33a * arr33b
print(f"Array A:\n{arr33a}")
print(f"Array B:\n{arr33b}")
print(f"Element-wise product:\n{result33}")
