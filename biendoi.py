from linecache import getline


def OctalToDecimal(num):

   decimal_value = 0
   base = 1
   while (num):
      last_digit = num % 10
      num = int(num / 10)
      decimal_value += last_digit * base
      base = base * 8
   return decimal_value

def numberToBase(n, b):
   if n == 0:
      return [0]
   digits = []
   while n:
      digits.append(int(n % b))
      n //= b
   return digits[::-1]

def calc(a ,b):
   res_10 = OctalToDecimal(a) - OctalToDecimal(b)
   res = int(''.join([str(i) for i in numberToBase(res_10, 8)]))
   return res

x = int(getline('biendoi.inp', 1))
to_oct = numberToBase(x, 8)
P = 0
Q = 0

for i in range(5):
   P = int(''.join([str(i) for i in to_oct]))
   sorted_list = sorted(to_oct)
   Q = int(''.join([str(i) for i in sorted_list]))
   to_oct = [int(i) for i in list(str(calc(P, Q)))]

final_num_8 = int(''.join([str(i) for i in to_oct]))
res = OctalToDecimal(final_num_8)
with open('biendoi.out', 'w') as output:
   output.write(str(res))
output.close()