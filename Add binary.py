# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

# a = "11"
# b = "1"

# rules = {
#     "000":"00", "001":"10", "010":"10", "100":"10",
#     "110":"01", "101":"01", "011":"01", "111":"11"
# }

# a,b = a.zfill(len(b)),b.zfill(len(a))

# carry,res = "0",[]

# for x, y in zip(a[::-1],b[::-1]):
#     s,carry = rules[x+y+carry]

#     res.append(s)

# if carry=="1":
#     res.append(carry)

# print("".join(res[::-1]))


        
# app2
# a ="11"
# b = "1"
# new_a =int(a,2)
# new_b = int(b,2)
# sum = new_a+new_b
# print(bin(sum)[2:])

# app3
a="11"
b="1"
print(bin(int(a,2)+int(b,2)).replace('0b',''))