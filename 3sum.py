# Given an array arr[], the task is to find all possible indices {i, j, k} of triplet {arr[i], arr[j], arr[k]} such that their sum is equal to zero and all indices in a triplet should be distinct (i != j, j != k, k != i). We need to return indices of a triplet in sorted order, i.e., i < j < k.

# Examples :

# Input: arr[] = {0, -1, 2, -3, 1}
# Output: {{0, 1, 4}, {2, 3, 4}}
# Explanation:  Two triplets with sum 0 are:
# arr[0] + arr[1] + arr[4] = 0 + (-1) + 1 = 0
# arr[2] + arr[3] + arr[4] = 2 + (-3) + 1 = 0

# Input: arr[] = {1, -2, 1, 0, 5}
# Output: {{0, 1, 2}}
# Explanation: Only triplet which satisfies the condition is arr[0] + arr[1] + arr[2] = 1 + (-2) + 1 = 0

# Input: arr[] = {2, 3, 1, 0, 5}
# Output: {{}}
# Explanation: There is no triplet with sum 0

arr = [0, -1, 2, -3, 1]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            if arr[i] + arr[j] + arr[k] == 0:
                print(f"{arr[i]} + {arr[j]} + {arr[k]} = 0 (indices: {i},{j},{k})")