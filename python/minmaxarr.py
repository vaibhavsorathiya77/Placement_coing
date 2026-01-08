# Given an array arr[]. Your task is to find the minimum and maximum elements in the array.

# Examples:

# Input: arr[] = [1, 4, 3, -5, -4, 8, 6]
# Output: [-5, 8]
# Explanation: minimum and maximum elements of array are -5 and 8.
# Input: arr[] = [12, 3, 15, 7, 9]
# Output: [3, 15]
# Explanation: minimum and maximum element of array are 3 and 15.

arr = [1, 4, 3, -5, -4, 8, 6]

min_arr = arr[0]
max_arr = arr[0]

for x in arr:
    if x <  min_arr:
         min_arr =x

    if x > max_arr:
         max_arr =x

print(min_arr,max_arr)