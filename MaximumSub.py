# Given an integer array arr[], find the subarray (containing at least one element) which has the maximum possible sum, and return that sum.
# Note: A subarray is a continuous part of an array.

# Examples:

# Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
# Output: 11
# Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.

# Input: arr[] = [-2, -4]
# Output: -2
# Explanation: The subarray [-2] has the largest sum -2.

# Input: arr[] = [5, 4, 1, 7, 8]
# Output: 25
# Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25.


arr = [5,4,1,7,8]
#output = 25

sum = arr[0]
max_sum = 0
temp = [arr[0]]

for i in range(len(arr)):
    current_array=0
    temp_arry = []
    for j in range(i,len(arr)):
        current_array += arr[j] 
        temp_arry.append(arr[j])
        max_sum = current_array
        if current_array > sum:
            sum = current_array
            temp = temp_arry.copy()

print(sum)
print(temp)