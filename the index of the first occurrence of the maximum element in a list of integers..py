# Write a function in Python to return the index of the first occurrence of the maximum element in a list of integers.
# If the list is empty, return -1.

# Input: [1, 3, 7, 7, 2]  
# Output: 2  # index of first 7


# inp = [1,3,7,7,2]
# print(f"The first occurecne is {inp.index(max(inp))}")


# manualll
# highest_num = inp[0]
# highest_index = 0

# for i in range(1,len(inp)):
#     if inp[i] > highest_num:
#         highest_num = inp[i]
#         highest_index = i
# print(highest_index)

# def finding_highest_occurence(num):
#     if not num:
#         return -1
#     else:
#         max_num = num[0]
#         max_index = 0
#         for i in range(1,len(num)):
#             if num[i] > max_num:
#                 max_num=num[i]
#                 max_index = i
#         return max_index
# num = [1,3,7,7,2]
# print(f"The index is :- {finding_highest_occurence(num)}")

#  checking anagram or not

# def is_anagram(s):
#     s_feq= {}
#     for ch in s:
#         if ch in s_feq:
#             s_feq[ch] +=1
#         else:
#             s_feq[ch] = 1
#     return  s_feq

# s = "listen"
# s2 = "silent"
# # if sorted(s) == sorted(s2):
# #     print(True)
# # else:
# #     print(False)
# print(is_anagram(s) == is_anagram(s2))



