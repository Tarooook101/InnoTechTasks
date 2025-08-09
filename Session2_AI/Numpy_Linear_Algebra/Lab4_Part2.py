import numpy as np

print("=" * 60)
print("NUMPY DOCUMENT TASKS 1-25 SOLUTION")
print("=" * 60)

# 1. Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array. 
print("\n1. Convert list to 1D NumPy array:")
original_list = [12.23, 13.32, 100, 36.32]
arr1 = np.array(original_list)
print(f"Original List: {original_list}")
print(f"One-dimensional NumPy array: {arr1}")

# 2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10. 
print("\n" + "="*50)
print("2. 3x3 matrix with values 2 to 10:")
arr2 = np.arange(2, 11).reshape(3, 3)
print(arr2)

# 3. Write a NumPy program to create a null vector of size 10 and update the sixth value to 11
print("\n" + "="*50)
print("3. Null vector, update sixth value:")
arr3 = np.zeros(10)
print(f"Original: {arr3}")
arr3[5] = 11  # sixth element (index 5)
print(f"Update sixth value to 11: {arr3}")

# 4. Write a NumPy program to create an array with values ranging from 12 to 38.
print("\n" + "="*50)
print("4. Array from 12 to 38:")
arr4 = np.arange(12, 38)
print(arr4)

# 5. Write a NumPy program to reverse an array (the first element becomes the last). 
print("\n" + "="*50)
print("5. Reverse array:")
arr5 = np.arange(12, 38)
print(f"Original array: {arr5}")
reversed_arr = arr5[::-1]
print(f"Reverse array: {reversed_arr}")

# 6. Write a NumPy program to convert an array to a floating type. 
print("\n" + "="*50)
print("6. Convert to float type:")
arr6 = np.array([1, 2, 3, 4])
print(f"Original array: {arr6}")
float_arr = arr6.astype(float)
print(f"Array converted to float type: {float_arr}")

# 7. Write a NumPy program to append values to the end of an array. 
print("\n" + "="*50)
print("7. Append values to array:")
arr7 = np.array([10, 20, 30])
values_to_append = [40, 50, 60, 70, 80, 90]
result7 = np.append(arr7, values_to_append)
print(f"Original array: {arr7}")
print(f"After append values: {result7}")

# 8. Write a NumPy program to create an empty and full array. 
print("\n" + "="*50)
print("8. Create empty and full arrays:")
empty_arr = np.empty((3, 4))
full_arr = np.full((3, 3), 6)
print("Empty array:")
print(empty_arr)
print("Full array:")
print(full_arr)

# 9. Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.
print("\n" + "="*50)
print("9. Centigrade to Fahrenheit conversion:")
centigrade = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])

# Convert Centigrade to Fahrenheit: F = C * 9/5 + 32
c_to_f = centigrade * 9/5 + 32
# Convert Fahrenheit to Centigrade: C = (F - 32) * 5/9
f_to_c = (fahrenheit - 32) * 5/9

print(f"Centigrade values: {centigrade}")
print(f"Values in Fahrenheit: {c_to_f}")
print(f"Fahrenheit values: {fahrenheit}")
print(f"Values in Centigrade: {f_to_c}")

# 10. Write a NumPy program to test whether each element of a 1-D array is also present in a second array.
print("\n" + "="*50)
print("10. Test elements presence:")
arr10_1 = np.array([0, 10, 20, 40, 60])
arr10_2 = np.array([0, 40])
result10 = np.isin(arr10_1, arr10_2)
print(f"Array1: {arr10_1}")
print(f"Array2: {arr10_2}")
print(f"Compare each element: {result10}")

# 11. Write a NumPy program to find common values between two arrays. 
print("\n" + "="*50)
print("11. Find common values:")
arr11_1 = np.array([0, 10, 20, 40, 60])
arr11_2 = np.array([10, 30, 40])
common = np.intersect1d(arr11_1, arr11_2)
print(f"Array1: {arr11_1}")
print(f"Array2: {arr11_2}")
print(f"Common values: {common}")

# 12. Write a NumPy program to get the unique elements of an array. 
print("\n" + "="*50)
print("12. Get unique elements:")
arr12_1 = np.array([10, 10, 20, 20, 30, 30])
arr12_2 = np.array([[1, 1], [2, 3]])
unique1 = np.unique(arr12_1)
unique2 = np.unique(arr12_2)
print(f"Original array: {arr12_1}")
print(f"Unique elements: {unique1}")
print(f"Original array:\n{arr12_2}")
print(f"Unique elements: {unique2}")

# 13. Write a NumPy program to find the set difference between two arrays. The set difference will return sorted, distinct values in array1 that are not in array2. 
print("\n" + "="*50)
print("13. Set difference:")
arr13_1 = np.array([0, 10, 20, 40, 60, 80])
arr13_2 = np.array([10, 30, 40, 50, 70, 90])
difference = np.setdiff1d(arr13_1, arr13_2)
print(f"Array1: {arr13_1}")
print(f"Array2: {arr13_2}")
print(f"Set difference: {difference}")

# 14. Write a NumPy program to compare two arrays using NumPy. 
print("\n" + "="*50)
print("14. Compare arrays:")
a = np.array([1, 2])
b = np.array([4, 5])
print(f"Array a: {a}")
print(f"Array b: {b}")
print(f"a > b: {a > b}")
print(f"a >= b: {a >= b}")
print(f"a < b: {a < b}")
print(f"a <= b: {a <= b}")

# 15. Write a NumPy program to sort along the first and last axes of an array. 
print("\n" + "="*50)
print("15. Sort along different axes:")
arr15 = np.array([[4, 6], [2, 1]])
print(f"Original array:\n{arr15}")
sort_first = np.sort(arr15, axis=0)
sort_last = np.sort(arr15, axis=1)
print(f"Sort along first axis:\n{sort_first}")
print(f"Sort along last axis:\n{sort_last}")

# 16. Write a NumPy program to get the values and indices of the elements that are bigger than 10 in a given array.
print("\n" + "="*50)
print("16. Values and indices bigger than 10:")
arr16 = np.array([[0, 10, 20], [20, 30, 40]])
print(f"Original array:\n{arr16}")
mask = arr16 > 10
values = arr16[mask]
indices = np.where(arr16 > 10)
print(f"Values bigger than 10: {values}")
print(f"Their indices: {indices}")

# 17. Write a NumPy program to create a contiguous flattened array. 
print("\n" + "="*50)
print("17. Flatten array:")
arr17 = np.array([[10, 20, 30], [20, 40, 50]])
print(f"Original array:\n{arr17}")
flattened = arr17.flatten()
print(f"New flattened array: {flattened}")

# 18. Write a NumPy program to create a 2-dimensional array of size 2 x 3 (composed of 4byte integer elements), also print the shape, type and data type of the array.
print("\n" + "="*50)
print("18. 2x3 array with 4-byte integers:")
arr18 = np.zeros((2, 3), dtype=np.int32)
print(f"Shape: {arr18.shape}")
print(f"Type: {type(arr18)}")
print(f"Data type: {arr18.dtype}")
print(f"Array:\n{arr18}")

# 19. Write a NumPy program to create another shape from an array without changing its data. 
print("\n" + "="*50)
print("19. Reshape array:")
arr19 = np.arange(1, 7)
shape_3x2 = arr19.reshape(3, 2)
shape_2x3 = arr19.reshape(2, 3)
print(f"Original 1D: {arr19}")
print(f"Reshape 3x2:\n{shape_3x2}")
print(f"Reshape 2x3:\n{shape_2x3}")

# 20. Write a NumPy program to create a new array of 3*5, filled with 2. 
print("\n" + "="*50)
print("20. 3x5 array filled with 2:")
arr20 = np.full((3, 5), 2)
print(arr20)

# 21. Write a NumPy program to create an array of 10's with the same shape and type as the given array. 
print("\n" + "="*50)
print("21. Array of 10's with same shape:")
original = np.array([1, 2, 3, 4])
arr21 = np.full_like(original, 10)
print(f"Original: {original}")
print(f"Array of 10's: {arr21}")

# 22. Write a NumPy program to create a 2-D array whose diagonal equals [4, 5, 6, 8] and 0's elsewhere. 
print("\n" + "="*50)
print("22. Diagonal array:")
arr22 = np.diag([4, 5, 6, 8])
print(arr22)

# 23. Write a NumPy program to create a 1-D array with values from 0 to 50 and an array from 10 to 50.
print("\n" + "="*50)
print("23. Arrays with different ranges:")
arr23_1 = np.arange(0, 50)
arr23_2 = np.arange(10, 50)
print(f"Array from 0 to 50:\n{arr23_1}")
print(f"Array from 10 to 50:\n{arr23_2}")

# 24. Write a NumPy program to find the 4th element of a specified array. 
print("\n" + "="*50)
print("24. Find 4th element:")
arr24 = np.array([[2, 4, 6], [6, 8, 10]])
fourth_element = arr24.flat[3]  # 4th element in flattened array
print(f"Array:\n{arr24}")
print(f"Fourth element: {fourth_element}")

# 25. Write a NumPy program to test whether specified values are present in an array. 
print("\n" + "="*50)
print("25. Test if values are present:")
arr25 = np.array([[1.12, 2., 3.45], [2.33, 5.12, 6.]])
test_values = [1.12, 7.0, 3.45, 9.0, 2.33]
print(f"Original array:\n{arr25}")
print("Testing values:", test_values)
for val in test_values:
    is_present = np.any(arr25 == val)
    print(f"Value {val} present: {is_present}")

