import math
 
def lcmSum(n):
    Sum = 0
    for i in range(1, n + 1):
        gcd = math.gcd(i, n)
        lcm = (i * n) // gcd
        Sum = Sum + lcm
    return Sum
list1 = []
NoT = int(input())
for i in range(1, NoT+1):
    list1.append(int(input()))
for x in range(0, NoT):
    print(lcmSum(list1[x]))
