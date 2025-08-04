# You are given a list where every element appears twice except one element, which appears only once. Find that element.
# Input: [4, 1, 2, 1, 2]
# Output: 4

data = [4, 1, 2, 1, 2]

d_feq = {}

for i in data:
    if i in d_feq:
        d_feq[i] += 1
    else:
        d_feq[i] = 1

for key in d_feq:
    if d_feq[key] == 1:
        print(key)
        break


