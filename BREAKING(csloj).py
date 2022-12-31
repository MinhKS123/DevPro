n = int(input())
arr = [int(i) for i in input().split()]
max_now = arr[0]
min_now = arr[0]
res_max = 0
res_min = 0

for i in arr[1:len(arr)]:
   if i > max_now:
      max_now = i
      res_max += 1
   if i < min_now:
      min_now = i
      res_min += 1
print(res_max, res_min)