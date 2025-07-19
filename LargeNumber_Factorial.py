# Find the Factorial of a large number
# Factorial of a non-negative integer, is the multiplication of all integers smaller than or equal to n. 
# Examples: 

# Input: 100
# Output: 933262154439441526816992388562667004-
#          907159682643816214685929638952175999-
#          932299156089414639761565182862536979-
#          208272237582511852109168640000000000-
#          00000000000000

# Input: 50
# Output: 3041409320171337804361260816606476884-
#          4377641568960512000000000000

num = 100

fact = 1

for i in range(2,num):
    fact *=i
print(fact)