# sets of question:-
# # Input: ["A-B", "A-C", "B-D"]
# # Output: True

# # Input: ["A-B", "A-C", "B-D", "B-E", "B-F"]
# # Output: False
# # Input: "acc?7??sss?3rr1??????5"
# # Output: True

# # Input: "aa6?9"
# # Output: False

# # Input: "Hello world, this is Coderbyte!"
# # Output: "Coderbyte"

# Q1
# input = "Hello world, this is Coderbyte!".split()
# print(max(input,key=len))

####Q2

# def checker(s):
#     previous_digit = None
#     found = False
#     question_mark = 0

#     for w in s:
#         if w.isdigit():
#             digit = int(w)
#             if previous_digit is not None:
#                 if previous_digit + digit==10:
#                     if question_mark==3:
#                         return True
#             previous_digit = digit
#             question_mark = 0
#         if w =="?":
#             question_mark+=1
#     return found

# s = "acc?7??sss?3rr1??????5"
# print(checker(s))
# input= "acc?7??sss?3rr1??????5"

# previous_digit = None
# question_mark = 0
# found = False
# for w in input:
#     if w.isdigit():
#         digit = int(w)
#         if previous_digit is not None:
#             if previous_digit + digit == 10:
#                 if question_mark == 3:
#                     found = True
#         previous_digit = digit
#         question_mark = 0
#     if w == "?":
#         question_mark+=1
# print(found)

# Q3

# # Input: ["A-B", "A-C", "B-D"]
# # Output: True

# # Input: ["A-B", "A-C", "B-D", "B-E", "B-F"]
# # Output: False


# n=123
# print (int(str(n)[::-1]))

# input = ["A-B", "A-C", "B-D"]

# parent_count={}
# child_count = {}

# for w in input:
#     parent,child = w.split('-')

#     if parent in parent_count:
#         parent_count[parent] +=1
#     else:
#         parent_count[parent] =1
#     if child in child_count:
#         child_count[child] +=1
#     else:
#         child_count[child] =1
#     if parent_count[parent] >2 or child_count[child] > 1:
#         print(False)
#         break
# else:
#     print(True)



key = "IVXLCDM"
value = [1,5,10,50,100,500,1000]

symbol = dict(zip(key,value))

s = "DCCLXV"
result = 0
for i in range(len(s)-1):
    current = symbol[s[i]]
    next = symbol[s[i+1]]
    if current<next:
        result -= current 
    else:
        result += current

result = result + symbol[s[-1]]
print(result)


# n = 25
# left = 0
# right = n
# ans = 0

# while left<=right:
#     mid = (left+right)//2
#     sq = mid*mid
#     if sq == n:
#         ans = mid
#         break
#     elif sq<n:
#         ans = mid
#         left = mid +1
#     else:
#         right = mid - 1
# print (ans)