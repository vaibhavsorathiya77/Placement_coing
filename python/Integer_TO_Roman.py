n = 2005
result = " "

key = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
# symbol= dict(zip(key,value))

i =0

while n>0:
    if n >= value[i]:
        result += key[i]
        n -= value[i]
    else:
        i+=1
print(result)
