# Input: arr[] = [2, 4, 1, 0, 2], x=1, y=2, yi=2, z=0
# Ouput: true true true
# Explanation: As x=1 is present in the array, so return 1. 
# After inserting y=2 at yi=2th index, the array becomes 2,4,2,1,0,2. After deleting z=0, the array becomes 2,4,2,1,2

arr = [2, 4, 1, 0, 2]
arr = [x for x in arr if x!=2]
print(arr)
arr.insert(0,10)
print(arr)
print(sorted(arr))