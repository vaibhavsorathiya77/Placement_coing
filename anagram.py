# Check if two Strings are Anagrams of each other
# Last Updated : 25 Jul, 2025
# Given two non-empty strings s1 and s2 of lowercase letters, determine if they are anagrams — i.e., if they contain the same characters with the same frequencies.

# Examples:

# Input: s1 = “geeks”  s2 = “kseeg”
# Output: true
# Explanation: Both the string have same characters with same frequency. So, they are anagrams.

# Input: s1 = "allergy", s2 = "allergyy"
# Output: false
# Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character. Since the frequency of characters differs, the strings are not anagrams.

# Input: s1 = "listen", s2 = "lists"
# Output: false
# Explanation: The characters in the two strings are not the same — some are missing or extra. So, they are not anagrams.

def check_anagram(s1):
    s1_feq={}
    for ch in s1:
        if ch in s1_feq:
            s1_feq[ch]+=1
        else:
            s1_feq[ch]=1
    return s1_feq

s1 ="vabhiav"
s2="vaibhav"

if check_anagram(s1) == check_anagram(s2):
    print("Yes the string is anagram")
else:
    print("No the the string is not anagram")

# # using sorted
# s1="vai"
# s2="iav"
# if sorted(s1) == sorted(s2):
#     print(True)
# else:
#     print(False)