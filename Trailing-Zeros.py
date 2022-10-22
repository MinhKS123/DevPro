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



def findTrailingZeros(n):
    count = 0
    i = 5
    while (n / i>= 1):
        count += int(n / i)
        i *= 5
 
    return int(count)
n = int(input())
print(findTrailingZeros(n))