# # Write a function to generate all subsets (power set) of a given list of unique integers.

# Input: [1, 2]  
# Output: [[], [1], [2], [1,2]]

def subsets(nums):
    result=[]
    def backtract(index,path):
        result.append(path[:])

        for i in range(index,len(nums)):
            path.append(nums[i])
            backtract(i+1,path)
            path.pop()

    backtract(0,[])
    return result

print(subsets([1,2]))
