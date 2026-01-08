# for mono

# alpha ="abcdefghijklmnopqrstuvwxyz"
# key = "zyxwvutsrqponmlkjihgfedcba"
# pt="vaibhav"
# data={}
# for i,j in zip(alpha,key):
#     data[i]=j
# for i in pt:
#     print(data[i],end="")


# for anagram

# def check_anagram(s1):
#     feq={}
#     for ch in s1:
#         if ch in feq:
#             feq[ch]+=1
#         else:
#             feq[ch]=1
#     return feq

# s1="vaibhav"
# s2="viabvah"
# if check_anagram(s1)==check_anagram(s2):
#     print("yes")
# else:
#     print("no")

# for group anagram

# s1 = ["act", "god", "cat", "dog", "tac"]
# data={}
# for word in s1:
#     key=''.join(sorted(word))
#     if key in data:
#         data[key].append(word)
#     else:
#         data[key]=[word]
# for i,grp in enumerate(data.values(),start=1):
#     print(f'Group{i}:- {grp}')

# for valid para

s1 = "[({})]"
stack=[]
pairs={
    ')' : "(",
    "}" : "{",
    "]" : "[",
}

for ch in s1:
    if ch in "[({":
        stack.append(ch)
    elif ch in '])}':
        if not stack:
            print(False)
            break
        elif stack.pop() != pairs[ch]:
            print(False)
else:
    print(len(stack)==0)