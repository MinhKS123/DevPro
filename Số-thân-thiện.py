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



By Minh <3                                                                                                                                                    
"""


import math
n = [int(i)for i in input().split()]
a = n[0]
b = n[1]
cnt = 0
for i in range(a, b+1):
    reverse = str(i)
    gcd = math.gcd(int(reverse[::-1]), i)
    if gcd == 1:
        cnt += 1
print(cnt)
