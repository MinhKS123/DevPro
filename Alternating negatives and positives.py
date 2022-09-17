n = int(input())

nr = [int(i) for i in input().split(' ')]
nr2 = nr.copy()

counter = 0
max_counter = 0 
max_index = 0 
for i in range(1, len(nr2)):
    if nr2[i] == 0: 
        nr2[i] = 1
    if nr2[i-1] * nr2[i] < 0:
        counter += 1
        if counter > max_counter:
            max_counter = counter
            max_index = i
    else:
        counter = 0  
listRes = nr[max_index-max_counter:max_index+1]
print(len(listRes))
for _ in listRes:
    print(_, end = ' ')