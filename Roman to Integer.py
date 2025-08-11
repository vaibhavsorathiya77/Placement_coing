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
#  12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right.
#  However, the numeral for four is not IIII. Instead, the number four is written as IV. 
# Because the one is before the five we subtract it making four. 
# The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].


s = "MCMXCIV"

roman = {'I': 1, 'V' : 5, 'X': 10, 'L' : 50, 'C': 100, 'D': 500, 'M': 1000}

roman_map = [
    (1000, "M"),
    (900,  "CM"),
    (500,  "D"),
    (400,  "CD"),
    (100,  "C"),
    (90,   "XC"),
    (50,   "L"),
    (40,   "XL"),
    (10,   "X"),
    (9,    "IX"),
    (5,    "V"),
    (4,    "IV"),
    (1,    "I")
]

res = 0
# inttt = {1 : "I", 
# 5 : "V",
#  10 : "X",
#    50 : "L",
#      100 : "C", 
#      500 : "D",
#        1000 : "M",
#        }


for i in range(len(s)):
    if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
        res -= roman[s[i]]
    else:
        res+= roman[s[i]]
print(res)

num = ''
intre = 1994
for j , sz in roman_map:
    while intre >= j:
        num += sz
        intre -= j
print(num)