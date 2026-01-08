# Input: "({[]})"
# Output: True

# Input: "([)]"
# Output: False

# s = "({[]})"

# bracket_map = {
#     ')' :'(',    
#     '}' : '{',
#     ']' : "["
# }

# stack=[]

# for char in s:
#     if char in bracket_map.values():
#         stack.append(char)

#     elif char in bracket_map.keys():
#         if not stack or stack[-1] != bracket_map[char]:
#             print(False)
#         stack.pop()

# print(len(stack)==0)


# Have the function BracketMatcher(str) take the str parameter being passed and 
# return 1 if the brackets are correctly matched and each one is accounted 
# for. Otherwise return 0. For example: if str is "(hello (world))", 
# then the output should be 1, but if str is "((hello (world))" 
# the the output should be 0 because the brackets do not correctly match up.
# Only "(" and ")" will be used as brackets. If str contains no brackets return 1.

# Input: "(coder)(byte))"
# # Output: 0
# Input: "(c(oder)) b(yte)"
# Output: 1

input = "(c(oder)) b(yte)"
pair = {
    ')' : '('
}

stack = []

for s in input:
    if s in pair.values():
        stack.append(s)
    elif s in pair.keys():
        if not stack or stack[-1] != pair[s]:
            print(0)
            break
        stack.pop()
else:
       if len(stack) == 0:
        print(1)
       else:
           print(0)
    