orders = [
    {"id": 1, "customer": "X", "amount": 500},
    {"id": 2, "customer": "Y", "amount": 300},
    {"id": 3, "customer": "X", "amount": 200},
    {"id": 4, "customer": "Z", "amount": 400},
    {"id": 5, "customer": "Y", "amount": 100}
]

total_by_each={}
max_amount = 0
overall_amount =0

for order in orders:
    customer = order["customer"]
    amount = order["amount"]
    overall_amount +=order["amount"]

    if customer in total_by_each:
        total_by_each[customer] += amount
    else:
        total_by_each[customer] = amount
  
    if amount > max_amount:
        max_amount = amount

max_cust = max(total_by_each,key=total_by_each.get)

print(max_cust)
print(f"Total by each :- {total_by_each}")
print(f"Overallamount:- {overall_amount}")
print(max_amount)