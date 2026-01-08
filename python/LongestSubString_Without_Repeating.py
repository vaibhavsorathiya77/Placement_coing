# Input: s = "geeksforgeeks"
# Output: 7 
# Explanation: The longest substrings without repeating characters are "eksforg” and "ksforge", with lengths of 7.

# Input: s = "aaa"
# Output: 1
# Explanation: The longest substring without repeating characters is "a"

# Input: s = "abcdefabcbb"
# Output: 6
# Explanation: The longest substring without repeating characters is "abcdef".

text = "vaibhav"
# str(text)
# output = 4
n = len(text)

max_len = 0
substing = ""
for i in range(n):
    seen = set()
    current_string = ""
    for j in range(i,n):
        if text[j] not in seen:
            seen.add(text[j])
            current_string +=text[j]
            if len(current_string) > max_len:
                max_len = len(current_string)
                substing = current_string
print(f"The longest substring is :- {substing} and length is {max_len}")