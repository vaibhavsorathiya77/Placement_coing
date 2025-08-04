# # Given a string containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.

# # A string is valid if:

# # Open brackets are closed by the same type of brackets.

# # Open brackets are closed in the correct order.

# Input: "()"         → Output: True  
# Input: "()[]{}"     → Output: True  
# Input: "(]"         → Output: False  

data = '()[]{}'
stack = []
pairs = {
    ')' : '(',
    ']' : '[',
    '}' : '{'
}

for ch in data:
    if ch in '([{':
        stack.append(ch)
    elif ch in ')]}':
        if not stack:
            print(False)
            break
        elif stack.pop() != pairs[ch]:
            print(False)
            break
else:
    print(len(stack)==0)
