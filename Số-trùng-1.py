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


n = input()
d = 0
y = (n[1:-1])
cnt = 1
for i in range(len(y)):
    cnt += 10 ** i 
cnt += int(y)
print(cnt)