# t1
# Input: "()" → Output: 1
# Input: "(())" → Output: 2
# Input: "()()" → Output: 2

# t2

# Input: "({[]})"
# Output: True

# Input: "([)]"
# Output: False

# t3
# orders= [
#     {"id":1, "customer":"A",
#      "amount":250},
#      {"id":2, "customer":"B", "amount":300},
#      {"id": 3, "customer":"A", "amount":150}
# ]

# t4 
# orders = [
#     {"id": 1, "customer": "X", "amount": 500},
#     {"id": 2, "customer": "Y", "amount": 300},
#     {"id": 3, "customer": "X", "amount": 200},
#     {"id": 4, "customer": "Z", "amount": 400},
#     {"id": 5, "customer": "Y", "amount": 100}
# ]


# for t2

# Input: "({[]})"
# Output: True

# Input: "([)]"
# Output: False

# s = "({[]})"

# bracket_map ={
#     ')':'(',
#     '}':'{',
#     ']':'['
# }

# stack=[]


# for char in s:
#     if char in bracket_map.values():
#         stack.append(char)
#     elif char in bracket_map.keys():
#         if not stack or stack[-1] != bracket_map[char]:
#             print(False)
#         stack.pop()
# print(len(stack)==0)

# # t3
# orders= [
#     {"id":1, "customer":"A",
#      "amount":250},
#      {"id":2, "customer":"B", "amount":300},
#      {"id": 3, "customer":"A", "amount":150}
# ]

# total_by_each ={}
# for order in orders:
#     customer = order["customer"]
#     amount = order["amount"]

#     if customer in total_by_each:
#         total_by_each[customer] += amount
#     else:
#         total_by_each[customer] = amount
# print(total_by_each)



# t4 
orders = [
    {"id": 1, "customer": "X", "amount": 500},
    {"id": 2, "customer": "Y", "amount": 300},
    {"id": 3, "customer": "X", "amount": 200},
    {"id": 4, "customer": "Z", "amount": 400},
    {"id": 5, "customer": "Y", "amount": 100}
]

total=0
max_amount = 0
total_byeach={}

for order in orders:
    customer = order["customer"]
    amount = order ["amount"]
    total += order["amount"]

    if customer in total_byeach:
        total_byeach[customer] += amount
    else:
        total_byeach[customer] = amount

print(total_byeach)
print(total)
max_customer = max(total_byeach,key=total_byeach.get)
print(max_customer)