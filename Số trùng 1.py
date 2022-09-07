n = input()
d = 0
y = (n[1:-1])
cnt = 1
for i in range(len(y)):
    cnt += 10 ** i 
cnt += int(y)
print(cnt)