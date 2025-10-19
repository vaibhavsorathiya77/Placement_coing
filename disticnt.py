# Input: [1, 2, 2, 3, 4, 4, 4, 5]
# Output: 5  # Elements: 1,2,3,4,5


def distinct(s):
    return len(set(s))

print(distinct([1,2,3,2,3,23,2,3,2,4,4,4,5]))