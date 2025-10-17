# Input: "({[]})"
# Output: True

# Input: "([)]"
# Output: False

s = "({[]})"

bracket_map = {
    ')' :'(',    
    '}' : '{',
    ']' : "["
}

stack=[]

for char in s:
    if char in bracket_map.values():
        stack.append(char)

    elif char in bracket_map.keys():
        if not stack or stack[-1] != bracket_map[char]:
            print(False)
        stack.pop()

print(len(stack)==0)
