import math as m


def isPerfectSuare(R): 
    s = int(m.sqrt(R))  
    return s * s == R



def isFibonacci(k):
    return isPerfectSuare(5*k*k + 4) or isPerfectSuare(5*k*k - 4)

a = int(input())
if isFibonacci(a):
    print("YES")
else:
    print("NO")