"""
          _____                _____                            _____                    _____                    _____                    _____          
         /\    \              |\    \                          /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \             |:\____\                        /::\____\                /::\    \                /::\____\                /::\____\        
       /::::\    \            |::|   |                       /::::|   |                \:::\    \              /::::|   |               /:::/    /        
      /::::::\    \           |::|   |                      /:::::|   |                 \:::\    \            /:::::|   |              /:::/    /         
     /:::/\:::\    \          |::|   |                     /::::::|   |                  \:::\    \          /::::::|   |             /:::/    /          
    /:::/__\:::\    \         |::|   |                    /:::/|::|   |                   \:::\    \        /:::/|::|   |            /:::/____/           
   /::::\   \:::\    \        |::|   |                   /:::/ |::|   |                   /::::\    \      /:::/ |::|   |           /::::\    \           
  /::::::\   \:::\    \       |::|___|______            /:::/  |::|___|______    ____    /::::::\    \    /:::/  |::|   | _____    /::::::\    \   _____  
 /:::/\:::\   \:::\ ___\      /::::::::\    \          /:::/   |::::::::\    \  /\   \  /:::/\:::\    \  /:::/   |::|   |/\    \  /:::/\:::\    \ /\    \ 
/:::/__\:::\   \:::|    |    /::::::::::\____\        /:::/    |:::::::::\____\/::\   \/:::/  \:::\____\/:: /    |::|   /::\____\/:::/  \:::\    /::\____\
\:::\   \:::\  /:::|____|   /:::/~~~~/~~              \::/    / ~~~~~/:::/    /\:::\  /:::/    \::/    /\::/    /|::|  /:::/    /\::/    \:::\  /:::/    /
 \:::\   \:::\/:::/    /   /:::/    /                  \/____/      /:::/    /  \:::\/:::/    / \/____/  \/____/ |::| /:::/    /  \/____/ \:::\/:::/    / 
  \:::\   \::::::/    /   /:::/    /                               /:::/    /    \::::::/    /                   |::|/:::/    /            \::::::/    /  
   \:::\   \::::/    /   /:::/    /                               /:::/    /      \::::/____/                    |::::::/    /              \::::/    /   
    \:::\  /:::/    /    \::/    /                               /:::/    /        \:::\    \                    |:::::/    /               /:::/    /    
     \:::\/:::/    /      \/____/                               /:::/    /          \:::\    \                   |::::/    /               /:::/    /     
      \::::::/    /                                            /:::/    /            \:::\    \                  /:::/    /               /:::/    /      
       \::::/    /                                            /:::/    /              \:::\____\                /:::/    /               /:::/    /       
        \::/____/                                             \::/    /                \::/    /                \::/    /                \::/    /        
         ~~                                                    \/____/                  \/____/                  \/____/                  \/____/         


""" 


def CountPairs(arr, n):
    arr.sort()
    count = 0
    l = 0; r = n - 1
    while (l < r):
        if (arr[l] + arr[r] > 0):
            count += (r - l)
            r -= 1
        else :
            l += 1
    return count 


n = int(input())
list_a = [int(i) for i in input().split()]
list_b = [int(i) for i in input().split()]
listRes = []
for i in range(0, n):
    listRes.append(list_a[i]-list_b[i])
print(CountPairs(listRes, len(listRes)))