# Input: "aaabbcdddd"

# Output: "a3b2c1d4"

# Explanation:

# "aaa" → "a3"

# "bb" → "b2"

# "c" → "c1"

# "dddd" → "d4"

# The output string should represent each character followed by the number of times it appears

s = "aaabbcdddd"

# char={}
count=1
result =''
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        count+=1
    else:
        result+=s[i-1] + str(count)
        count = 1
result+=s[-1] + str(count)

print(result)