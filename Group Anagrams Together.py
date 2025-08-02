# Given an array of words arr[], the task is to groups strings that are anagrams. An anagram is a word or phrase formed by rearranging the letters of another, using all the original letters exactly once.

# Example:

# Input: arr[] = ["act", "god", "cat", "dog", "tac"]
# Output: [["act", "cat", "tac"], ["god", "dog"]]
# Explanation: There are 2 groups of anagrams "god", "dog" make group 1. "act", "cat", "tac" make group 2.

# Input: arr[] = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
# Output: [["abc", "cab", "bac"], ["listen", "silent", "enlist"],["rat", "tar", "art"]]
# Explanation: 
# Group 1: "abc", "bac" and "cab" are anagrams.
# Group 2: "listen", "silent" and "enlist" are anagrams.
# Group 3: "rat", "tar" and "art" are anagrams.

# Try it on GfG Practice

words = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]

data={}

for word in words:
    key = ''.join(sorted(word))
    if key in data:
        data[key].append(word)
    else:
        data[key] =[word]

for i , group in enumerate(data.values(),start=1):
    print(f"Group{i}:- {group}")

    