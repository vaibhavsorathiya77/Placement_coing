# Given a list of integers, find the first element that occurs more than once, and return it.
# # If no such element exists, return -1.

# Input: [1, 2, 3, 5, 3, 2] ➜ Output: 3  



def is_seen(num):
    seen = set()
    for i in num:
        if i in seen:
            return i
        seen.add(i)
    return -1 
print(is_seen([1,2,3,5,3,2]))   