# Given an array of positive integers arr[], 
# return the second largest element from the array. If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element.

# Examples:

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.

arr = [12, 35, 1, 10, 34, 1]

largest = 0
sec = 0

for x in arr:
    if x > largest:
        sec = largest     
        largest = x
    elif x > sec and x != largest:
        sec = x

print(largest, sec)
