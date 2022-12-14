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



def primes_sieve(limit):
    limitn = limit+1
    primes = list(range(2, limitn))

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            if f in primes:
                primes.remove(f)
    return primes
