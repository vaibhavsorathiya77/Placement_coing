# Given a string s, the task is to find the maximum consecutive repeating character in the string.

# Note: We do not need to consider the overall count, but the count of repeating that appears in one place.

# Examples: 

# Input: s = "geeekk"
# Output: e
# Explanation: character e comes 3 times consecutively which is maximum.

# abhcjjjoakkackkkaek

def find_max_streak(s):
    current_count = 1
    max_char=""
    max_count = 0
    if len(s) == 1:
         return "Please enter a non-empty string."
    elif s == "":
        return f"String is '{s[0]}' and count is 1"
    else:

        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                current_count +=1
            else:
                current_count = 1
            if current_count > max_count:
                    max_count = current_count
                    max_char = s[i]
    return f"Longest character streak is '{max_char}' with a count of {max_count}"

s = input("enter a sting:- ")
print(find_max_streak(s))