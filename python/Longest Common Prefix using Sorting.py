# Given an array of strings arr[], the task is to return the longest common prefix 
# among each and every strings present in the array. If there’s no prefix common in all the strings, return “”.

# Examples:

# Input: arr[] = [“geeksforgeeks”, “geeks”, “geek”, “geezer”]
# Output: “gee”
# Explanation: “gee” is the longest common prefix in all the given strings: “geeksforgeeks”, “geeks”, “geeks” and “geezer”.

# Input: arr[] = [“apple”, “ape”, “april”]
# Output : “ap”
# Explanation: “ap” is the longest common prefix in all the given strings: “apple”, “ape” and “april”.

# Input: arr[] = [“hello”, “world”]
# Output: “”
# # Explanation: There’s no common prefix in the given strings.

# s =  ['geeksforgeeks',"geeks","geek","geezer"]
# s1 = sorted(s)
# pre='gee'
# for ch in s1:
#     if ch.startswith(pre):
#         print(ch)
arr = ['geeksforgeeks', 'geeks', 'geek', 'geezer']

prefix = ""
min_len = min(len(word) for word in arr)  # Only check up to shortest word length

for i in range(min_len):
    char = arr[0][i]  # Take the i-th char from first word
    if all(word[i] == char for word in arr):
        prefix += char
    else:
        break

print("Longest common prefix:", prefix)
