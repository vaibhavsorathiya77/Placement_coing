# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def length_subtirng(s):
    l = 0
    max_s = 0
    sett = set()
    for r in range(len(s)):
        while s[r] in sett:
            sett.remove(s[l])
            l+=1
        sett.add(s[r])
        max_s = max(max_s,r-l+1)
    return max_s

print(length_subtirng("abcaabc"))
    
