import numpy as np

print("=" * 60)
print("NUMPY STATISTICS LAB TASKS 1-13 SOLUTION")
print("=" * 60)

# 1. Write a Python program to find the maximum and minimum value of a given flattened array
print("\n1. Maximum and minimum of flattened array:")
arr1 = np.array([[0, 1], [2, 3]])
print(f"Original flattened array:\n{arr1}")
max_val = np.max(arr1)
min_val = np.min(arr1)
print(f"Maximum value of the above flattened array: {max_val}")
print(f"Minimum value of the above flattened array: {min_val}")

# 2. Write a NumPy program to get the minimum and maximum value of a given array along the second axis. 
print("\n" + "="*50)
print("2. Min and max along second axis:")
arr2 = np.array([[0, 1], [2, 3]])
print(f"Original array:\n{arr2}")
max_axis1 = np.max(arr2, axis=1)
min_axis1 = np.min(arr2, axis=1)
print(f"Maximum value along the second axis: {max_axis1}")
print(f"Minimum value along the second axis: {min_axis1}")

# 3. Write a NumPy program to calculate the difference between the maximum and the minimum values of a given array along the second axis. 
print("\n" + "="*50)
print("3. Difference between max and min along second axis:")
arr3 = np.array([[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]])
print(f"Original array:\n{arr3}")
diff = np.max(arr3, axis=1) - np.min(arr3, axis=1)
print(f"Difference between max and min: {diff}")

# 4. Write a NumPy program to compute the 80th percentile for all elements in a given array along the second axis.  
print("\n" + "="*50)
print("4. 80th percentile along second axis:")
arr4 = np.array([1.0, 2.0, 3.0, 4.0])
percentile_80 = np.percentile(arr4, 80)
# Also show floor division as mentioned in expected output
floor_div = np.floor_divide(arr4, 2)
print(f"Original array: {arr4}")
print(f"80th percentile: {percentile_80}")
print(f"Largest integer smaller or equal to division by 2: {floor_div}")

# 5. Write a NumPy program to compute the median of flattened given array.  
print("\n" + "="*50)
print("5. Median of flattened array:")
arr5 = np.array([[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]])
print(f"Original array:\n{arr5}")
median_val = np.median(arr5)
print(f"Median of said array: {median_val}")

# 6. Write a NumPy program to compute the weighted of a given array.  
print("\n" + "="*50)
print("6. Weighted average:")
arr6 = np.array([0, 1, 2, 3, 4])
weights = np.array([1, 1, 1, 1, 1])  # Equal weights
weighted_avg = np.average(arr6, weights=weights)
print(f"Original array: {arr6}")
print(f"Weighted average: {weighted_avg}")

# Alternative with different weights
weights2 = np.array([1, 2, 3, 4, 5])
weighted_avg2 = np.average(arr6, weights=weights2)
print(f"With weights {weights2}: {weighted_avg2}")

# 7. Write a NumPy program to compute the mean, standard deviation, and variance of a given array along the second axis.  
print("\n" + "="*50)
print("7. Mean, std, variance along second axis:")
arr7 = np.array([0, 1, 2, 3, 4, 5])
mean_val = np.mean(arr7)
std_val = np.std(arr7)
var_val = np.var(arr7)
print(f"Original array: {arr7}")
print(f"Mean: {mean_val}")
print(f"Std: {std_val}")
print(f"Variance: {var_val}")

# 8. Write a NumPy program to compute the covariance matrix of two given arrays.  
print("\n" + "="*50)
print("8. Covariance matrix:")
arr8_1 = np.array([0, 1, 2])
arr8_2 = np.array([2, 1, 0])
cov_matrix = np.cov(arr8_1, arr8_2)
print(f"Original array1: {arr8_1}")
print(f"Original array2: {arr8_2}")
print(f"Covariance matrix:\n{cov_matrix}")

# 9. Write a NumPy program to compute cross-correlation of two given arrays.  
print("\n" + "="*50)
print("9. Cross-correlation:")
arr9_1 = np.array([0, 1, 3])
arr9_2 = np.array([2, 4, 5])
cross_corr = np.correlate(arr9_1, arr9_2, mode='full')
print(f"Original array1: {arr9_1}")
print(f"Original array2: {arr9_2}")
print(f"Cross-correlation: {cross_corr}")

# 10. Write a NumPy program to compute pearson product-moment correlation coefficients of two given arrays.  
print("\n" + "="*50)
print("10. Pearson correlation coefficients:")
arr10_1 = np.array([0, 1, 3])
arr10_2 = np.array([2, 4, 5])
corr_matrix = np.corrcoef(arr10_1, arr10_2)
print(f"Original array1: {arr10_1}")
print(f"Original array2: {arr10_2}")
print(f"Pearson correlation coefficients:\n{corr_matrix}")

# 11. Write a NumPy program to test element-wise of a given array for finiteness (not infinity or not Not a Number), positive or negative infinity, for NaN, for NaT (not a time), for negative infinity, for positive infinity. 
print("\n" + "="*50)
print("11. Test for various conditions:")

# Test for finiteness
test_arr = np.array([1, 2, np.inf])
finite_test = np.isfinite(test_arr)
print(f"Test for finiteness: {finite_test}")

# Test for infinity
inf_test = np.isinf(test_arr)
print(f"Test for infinity: {inf_test}")

# Test for NaN
nan_arr = np.array([np.nan, 1, 2])
nan_test = np.isnan(nan_arr)
print(f"Test for NaN: {nan_test}")

# Test for NaT (Not a Time)
nat_arr = np.array(['2020-01-01', 'NaT'], dtype='datetime64')
nat_test = np.isnat(nat_arr)
print(f"Test for NaT: {nat_test}")

# Test for negative infinity
neginf_arr = np.array([-np.inf, 0, np.inf])
neginf_test = np.isneginf(neginf_arr).astype(int)
print(f"Test for negative infinity: {neginf_test}")

# Test for positive infinity
posinf_test = np.isposinf(neginf_arr).astype(int)
print(f"Test for positive infinity: {posinf_test}")

# 12. Write a Python program to count number of occurrences of each value in a given array of non-negative integers. 
print("\n" + "="*50)
print("12. Count occurrences with bincount:")
arr12 = np.array([0, 1, 6, 1, 4, 1, 2, 2, 7])
counts = np.bincount(arr12)
print(f"Original array: {arr12}")
print(f"Number of occurrences of each value: {counts}")

# 13. Write a NumPy program to compute the histogram of nums against the bins.  
print("\n" + "="*50)
print("13. Compute histogram:")
nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])
hist, bin_edges = np.histogram(nums, bins)
print(f"nums: {nums}")
print(f"bins: {bins}")
print(f"Result: (array({hist}), array({bin_edges}))")

