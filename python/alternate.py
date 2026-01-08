# Input: arr[] = [1, 2, 3, 4]
# Output: 1 3
# Explanation:
# Take first element: 1
# Skip second element: 2
# Take third element: 3
# Skip fourth element: 4

arr = [1,2,3,5]

for i in range(0,len(arr),2):
    print(arr[i])