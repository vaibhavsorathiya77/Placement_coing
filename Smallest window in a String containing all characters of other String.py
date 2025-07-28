# Given two strings s (length m) and p (length n), the task is to find the smallest substring ---
# in s that contains all characters of p, including duplicates. If no such substring exists, return "-1".
#  If multiple substrings of the same length are found, return the one with the smallest starting index.

# Examples: 

# Input: s = "timetopractice", p = "toc"
# Output: toprac
# Explanation: "toprac" is the smallest substring in which "toc" can be found.

# Input: s = "zoomlazapzo", p = "oza"
# Output: apzo
# Explanation: "apzo" is the smallest substring in which "oza" can be found.

s = "timetopractice"
to_find = "toc"

min_len = len(s) + 1
min_substring = ""

for i in range(len(s)):
    for j in range(i + len(to_find), len(s)+1):  # substring length >= len(to_find)
        window = s[i:j]
        all_found = True

        for char in to_find:
            if char not in window:
                all_found = False
                break

        if all_found:
            if len(window) < min_len:
                min_len = len(window)
                min_substring = window

print(f"Smallest substring containing '{to_find}': {min_substring}")

        
       