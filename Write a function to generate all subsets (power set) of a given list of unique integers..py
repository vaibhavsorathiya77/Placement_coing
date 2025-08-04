# # Write a function to generate all subsets (power set) of a given list of unique integers.

# Input: [1, 2]  
# Output: [[], [1], [2], [1,2]]

nums = [1,2]
result = [[]]

for num in nums:
    subsets = []
    for sub in result:
        sub = sub + [num]
        subsets.append(sub)
    result.extend(subsets)
    
print(result)