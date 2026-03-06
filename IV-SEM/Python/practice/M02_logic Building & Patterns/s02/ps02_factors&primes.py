'''Read a number from user and print all the factors of that number.
input : 12
output : 1 2 3 4 6 12'''
'''
n = int(input())
for  i in range(1, n+1):
    if n % i == 0:
        print(i, end=' ')
print(n)
'''


'''GCD of two numbers'''
a = int(input())
b = int(input())
while b:
    a, b = b, a % b
print(a)

import math
print(math.gcd(a,b))

