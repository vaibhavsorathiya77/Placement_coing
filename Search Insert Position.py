# # Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
#  If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7

# nums = [1,3,5,6]
# key = 5
# # i= 0
# for i in range(len(nums)):
#     if nums[i] == key:
#         print(i)
           

# nums = [1, 3, 5, 6]
# target = 5

# left, right = 0, len(nums)
# while left < right:
#     mid = (left + right) // 2
#     if nums[mid] < target:
#         left = mid + 1
#     else:
#         right = mid

# print(left)     

def searchInsert( nums, target):
        
        for i in range(0,len(nums)):
            if nums[i] == target:
                return i
        
        nums.append(target)
        nums.sort()

        for i in range(0,len(nums)):
            if nums[i] == target:
                return i

nums=[1,5,2,6]
target = 5
print(searchInsert(nums,target))