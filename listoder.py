orders= [
    {"id":1, "customer":"A",
     "amount":250},
     {"id":2, "customer":"B", "amount":300},
     {"id": 3, "customer":"A", "amount":150}
]

total = {}

for order in orders:
    customer = order["customer"]
    amount = order["amount"]

    if customer in total:
        total[customer]+=amount
    else:
        total[customer] = amount

print(total)