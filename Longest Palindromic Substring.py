# Given a string s, find the longest substring which is a palindrome. 
# If there are multiple answers, then find the first appearing substring.

# Examples:

# Input: s = "forgeeksskeegfor"
# Output: "geeksskeeg"
# Explanation: The longest substring that reads the same forward and backward 
# is "geeksskeeg". Other palindromes like "kssk" or "eeksskee" are shorter.

# Input: s = "Geeks"
# Output: "ee"
# Explanation: The substring "ee" is the longest palindromic part in "Geeks". All others are shorter single characters.

# Input: s = "abc"
# Output: "a"
# Explanation: No multi-letter palindromes exist. So the first character "a" is returned as the longest palindromic substring.


s = 'Geeks'
sub=[]
temp=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        sub.append(s[i:j])
# print(sub)
for ch in sub:
    if ch == ch[::-1]:
        temp.append(ch)
print(f"Longest substring with palindrome is {max(temp,key=len)}")
print(temp)