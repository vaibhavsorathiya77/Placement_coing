# *********** Find the index of the first maximum element in a list ***********

# Input: [1, 3, 7, 7, 2]

# Output: 2 (first occurrence of 7)

# data = [1,3,7,7,2]

# highest_num= data[0]
# index_num = 1

# for i in range(len(data)):
#     if data[i] > highest_num:
#         highest_num = data[i]
#         index_num = i
# print(f"The index of the first maximum element in list is :- {index_num}")


# *********** Check if two strings are anagrams ***********

# Input: "listen" and "silent"

# Output: True

# Other Input: "apple" and "pale"

# Output: False

# def is_anagram(s):
#     feq={}
#     for ch in s:
#         if ch in feq:
#             feq[ch] += 1
#         else:
#             feq[ch] = 1
#     return feq

# s1 = 'listen'
# s2 = 'silent'
# print(is_anagram(s1)==is_anagram(s2))


# ***********  Find the first repeating element in a list ***********

# Input: [1, 2, 3, 5, 3, 2]

# Output: 3 (first number that repeats)

# data = [1,2,3,5,2,3]

# def is_seen(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#             return(num)
#         seen.add(num)
#     else:
#         return -1

# print(is_seen(data))

# *********** Find the element that appears only once (others appear twice) ***********
# Input: [4, 1, 2, 1, 2]
# Output: 4

# data = [4,1,2,1,2]
# feq = {}

# for nums in data:
#     if nums in feq:
#         feq[nums]+=1
#     else:
#         feq[nums]= 1
# for keys in feq:
#     if feq[keys] == 1:
#         print(keys)

#  ***********Generate all subsets (power set) of a list ***********

# Input: [1, 2]

# Output: [[], [1], [2], [1, 2]]

# nums = [1,2]
# result = [[]]

# for num in nums:
#     subsets = []
#     for sub in result:
#         sub = sub + [num]
#         subsets.append(sub)
#     result.extend(subsets)
# print(result)

# Validate balanced brackets using a stack

# Input: "()[]{}"

# Output: True

# Input: "(]"

# Output: False

# data = "()[]{}"
# stack = []
# pairs = {
#     ')' : '(',
#     ']' : '[',
#     '}' : '{'
# }

# for i in data:
#     if i in '([{':
#         stack.append(i)
#     elif i in ')]}':
#         if not stack:
#             print(False)
#             break
#         elif stack.pop() != pairs[i]:
#             print(False)
#             break
# else:
#     print(len(stack)==0)



# roman to interger 
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

# s = "XII"

# data = {
#     'I':1,
#     "V":5,
#     "X":10,
#     "L":50,
#     "C":100,
#     "D":500,
#     "M":1000
# }

# res = 0

# for i in range(len(s)):
#     if i + 1 < len(s) and data[s[i]] < data[s[i+1]]:
#         res-= data[s[i]]
#     else:
# #         res+=data[s[i]]
# # print(f"{s} in integer form is :- {res}")

# s = "abcabccd"
# l = 0
# long = 0
# sett = set()

# for r in range(len(s)):
#     while s[r] in sett:
#         sett.remove(s[l])
#         l+=1
#     sett.add(s[r])
#     long = max(long,r-l+1)
# print(long) 

# s = "abcabcbb"
# l = 0  # left pointer
# sett = set()
# max_len = 0
# substring = ""
# temp = []
# for r in range(len(s)):  # r = right pointer
#     while s[r] in sett:  # shrink until no repeat
#         sett.remove(s[l])
#         l += 1
    
#     sett.add(s[r])

#     # If new window is bigger, update answer
#     if (r - l + 1) > max_len:
#         max_len = r - l + 1
#         substring = s[l:r+1]

# # print("Length:", max_len)
# print("Substring:", substring)

# for ch in substring:
#     if ch == ch[::-1]:
#         temp.append[ch]
# print()
