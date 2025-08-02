# Given a string s representing an expression containing various types of brackets: {}, (), and [], the task is to determine whether the brackets in the expression are balanced or not. A balanced expression is one where every opening bracket has a corresponding closing bracket in the correct order.

# Example: 

# Input: s = "[{()}]"
# Output: true
# Explanation:  All the brackets are well-formed.

# Input: s = "[()()]{}"
# Output: true
# Explanation: All the brackets are well-formed.

# Input: s = "([]"
# Output: false
# Explanation: The expression is not balanced as there is a missing ')' at the end.

# Input:  s = "([{]})"
# Output: false
# Explanation: The expression is not balanced because there is a closing ']' before the closing '}'.


s = "[()()]{}"
stack = []
pairs={')':"("
       ,"}":"{"
       ,"]":"["
       }
for ch in s:
    if ch in '[(({':
        stack.append(ch)
    elif ch in '}]))':
        if not stack:
            print(False)
            break
        elif stack.pop() != pairs[ch]:
            print(False)
            break
else:
    print(len(stack)==0)