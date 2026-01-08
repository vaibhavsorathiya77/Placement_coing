# Input: arr[] = [0, -1, 2, -3, 1], target = -2
# Output: true
# Explanation: There is a pair (1, -3) with the sum equal to given target, 1 + (-3) = -2.

# Input: arr[] = [1, -2, 1, 0, 5], target = 0
# Output: false
# Explanation: There is no pair with sum equals to given target.

# arr = [1,2,3,4,5]
# arr2 = [2,3,5,4,5]
# for i in range(len(arr)):
#     print(arr[i] + arr2[i])


arr = [0,-1,2,-3,1]
# find the target -2 ie pair 
target = -2
for i in range (len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j]==target:
            print(f"{arr[i]} + {arr[j]} = {target}")
