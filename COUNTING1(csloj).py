from collections import Counter as Cnt

n = int(input())
arr = [int(i) for i in input().split()]
res = []
cnt = Cnt(arr)
for values in arr:
    res.append(cnt[values]-1)
for i in res:
    print(i, end = ' ')