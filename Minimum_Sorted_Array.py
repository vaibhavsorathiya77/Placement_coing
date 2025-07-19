# Minimum in a Sorted and Rotated Array
# Last Updated : 13 Dec, 2024
# Given a sorted array of distinct elements arr[] of size n that is rotated at some unknown point, the task is to find the minimum element in it. 

# Examples: 

# Input: arr[] = [5, 6, 1, 2, 3, 4]
# Output: 1
# Explanation: 1 is the minimum element present in the array.

# Input: arr[] = [3, 1, 2]
# Output: 1
# Explanation: 1 is the minimum element present in the array.

# Input: arr[] = [4, 2, 3]
# Output: 2
# Explanation: 2 is the only minimum element in the array.

# arr = [5, 6, 1, 2, 3, 4]
# # output = 1
# low = 0
# high = len(arr) - 1
# mid = (low + high) // 2
# mid1 = arr[mid]

# print(mid1)

# # while(low<=high):
# #     if mid > 0 and arr[mid]< arr[mid-1]:

def find_min(arr):
    low = 0 
    high = len(arr) - 1

    while low <=high:
        if arr[low] <= arr[high]:
            return arr[low]
        mid = (low + high) // 2
        next_element = (mid + 1) % len(arr)
        prev_elem = (mid - 1 + len(arr)) % len(arr)
        if arr[mid] <= arr[prev_elem] and arr[mid] <= arr[next_element]:
            return arr[mid]
          # Right half is sorted, go left
        if arr[mid] <= arr[high]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(find_min( [5, 6, 1, 2, 3, 4]))

    
