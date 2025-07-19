# Given an array prices[] of length N, representing the prices of the stocks on different days, the task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell.

# Note: Stock must be bought before being sold.

# Examples:

# Input: prices[] = {7, 10, 1, 3, 6, 9, 2}
# Output: 8
# Explanation: Buy for price 1 and sell for price 9. 

# Input: prices[] = {7, 6, 4, 3, 1} 
# Output: 0
# Explanation: Since the array is sorted in decreasing order, 0 profit can be made without making any transaction.

prices  = [7,8,10,1,3,6,9,2]
max_profit = 0
min_price = prices[0]

for i in range(1,len(prices)):
    if prices[i] < min_price:
        min_price = prices[i]
    profit = prices[i] - min_price
    if profit > max_profit:
        max_profit = profit

print(max_profit)

