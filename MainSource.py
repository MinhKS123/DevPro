"""
.___  ___.  __  .__   __.  __    __      __  ___      _______.
|   \/   | |  | |  \ |  | |  |  |  |    |  |/  /     /       |
|  \  /  | |  | |   \|  | |  |__|  |    |  '  /     |   (----`
|  |\/|  | |  | |  . `  | |   __   |    |    <       \   \    
|  |  |  | |  | |  |\   | |  |  |  |    |  .  \  .----)   |   
|__|  |__| |__| |__| \__| |__|  |__|    |__|\__\ |_______/    

"""         
listResult = []        
a = int(input())                                           
for i in range(a):
	e,k=map(int,input().split())
	for i in range(k):
		j = 2
		if e%2==0:
			e=e+2*(k-i)
			break
		else:
			while e%j!=0:
				j+=1
			if e%(j+1)==0:
				j+=1
			e+=j
	listResult.append(e)
for x in range(a):
    print(listResult[x])
    