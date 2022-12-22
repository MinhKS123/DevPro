from itertools import chain
from linecache import getline
from collections import Counter

m, n, k = [int(i) for i in getline('cau4.inp', 1).split()]
arr = [[int(i) for i in getline('cau4.inp', x).split()] for x in range(2, m+2)]
flatten_arr = chain.from_iterable(arr)
counter = Counter(flatten_arr)
list1 = []
for value in counter:
    list1.append(value)
list1 = list(set(list1))
list1.sort(reverse=True)
res = 0
for i in range(k+1):
    res += list1[i]
with open('cau4.out', 'w') as output:
    output.write(str(res))
output.close()