# Given an array arr[] consisting of positive, negative, and zero values, find the maximum product that can be obtained from any contiguous subarray of arr[].

# Examples:

# Input: arr[] = [-2, 6, -3, -10, 0, 2]
# Output: 180
# Explanation: The subarray with maximum product is [6, -3, -10] with product = 6 * (-3) * (-10) = 180.

# Input: arr[] = [-1, -3, -10, 0, 6]
# Output: 30
# Explanation: The subarray with maximum product is [-3, -10] with product = (-3) * (-10) = 30.

# Input: arr[] = [2, 3, 4] 
# Output: 24 
# Explanation: For an array with all positive elements, the result is product of all elements. 


arr = [-2, 6, -3, -10, 0, 2]
# output = 180
max_array = arr[0]
sub_array = [arr[0]]
for i in range(len(arr)):
    current_array = 1
    temp_array = []
    for j in range(i,len(arr)):
        current_array *= arr[j]
        temp_array.append(arr[j])
        if current_array > max_array:
            max_array = current_array
            sub_array = temp_array.copy()

print(max_array)
print(sub_array)