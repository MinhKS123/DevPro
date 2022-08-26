from math import gcd
for hahahahahahahahahahahahahahahahahahahahahahahahahahahahahaha in range(int(input())):
    n = int(input())
    i = 1
    cosum,ans = 0,0
    while i*i <= n:
        if n%i == 0:
            ans += (i*n)//gcd(i,n)
            cosum += i
            if i != n//i:
                j = n//i
                ans += (j*n)//gcd(j,n)
                cosum += j
        i += 1
    ans += n*((n*(n+1))//2-cosum)
    print(ans)
