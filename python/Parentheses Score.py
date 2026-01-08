# Input: "()" → Output: 1
# Input: "(())" → Output: 2
# Input: "()()" → Output: 2


s = "()()"

stack = [0]

for char in s:
    if char == '(':
        stack.append(0)
    else:
        inner = stack.pop()
        stack[-1] += 1 if inner == 0 else 2 * inner

print(stack)