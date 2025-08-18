# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

strts =  ["dog","racecar","car"]

if strts:
    min_len = min(len(s) for s in strts)
    prefix=""
    for i in range(min_len):
        chars = {s[i] for s in strts}
        if len(chars)== 1:
            prefix+=list(chars)[0]
        else:
            break
    print(prefix)
else:
    print("")
