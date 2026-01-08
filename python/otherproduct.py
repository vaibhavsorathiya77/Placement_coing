# Example 1

# Input:
# [1, 2, 3, 4, 5]

# Output:
# [120, 60, 40, 30, 24]

s = [1,2,3,4,5]
ans =[]

for i in range(len(s)):
    pro =1
    for j in range(len(s)):
        if i != j:
            pro*=s[j]
    ans.append(pro)
print(ans)