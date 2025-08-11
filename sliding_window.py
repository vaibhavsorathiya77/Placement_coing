# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

s = "abcabcbb"
l = 0
max_leng = 0
sett = set()
for r in range(len(s)):
    while s[r] in sett:
        sett.remove(s[l])
        l+=1
    sett.add(s[r])
    max_leng= max(max_leng,r-l+1)
print(max_leng)
    
