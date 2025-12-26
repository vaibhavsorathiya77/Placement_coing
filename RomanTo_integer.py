# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together.
 

# Example 1:

# Input: s = "III"
# Output: 3
 

s = "MMV"

symbol=dict(zip("IVXLCDM",[1,5,10,50,100,500,1000]))
result = 0
for i in range(len(s)-1):
    current = symbol[s[i]]
    next = symbol[s[i+1]]
    if current<next:
        result = result - current
    else:
        result = result+current
result = result + symbol[s[-1]]
print(result)

