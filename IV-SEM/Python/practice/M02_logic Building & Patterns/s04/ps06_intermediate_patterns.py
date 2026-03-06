'''
input = [1,2,3,4,5]
output = [1,4,9,16,25]

li = [1, 2, 3, 4, 5]
res = []
for i in li:
    res.append(i ** 2)
print(res)
print([i ** 2 for i in li])

input = [1,2,3,4,5]
output = [2,4]

li = [1, 2, 3, 4, 5]

res = []
for i in li:
    if i % 2 == 0:
        res.append(i)

print(res)

print([i for i in li if i % 2 == 0])'''

'''#['a', 'b', 'c' ] => "abc"

li1 = ['a','b','c']
res = " "
for ch in li1:
    res += ch 
print(res)
print("".join(li1))
'''
'''
input: 4
output:
    *
   **
   ***
   ****
'''
'''n = int(input())
for i in range(1,n+1):
    print(" " * (n - i) + "*" * i)
    
'''
'''
input  = 4
output = 
* * * *
 * * *
  * *
   *
'''
n = int(input())
for i in range(n):
    print(" " * i + "* " * (n - i)) 
    '''
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
'''
n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* "  * i)
         
         
    '''  1 2
        1 2 3
       1 2 3 4'''
    n = int(input())
    for i in range(1, n + 1):
        print(" " * (n - i) + " ".join(str(j) for j in range(1, i + 1)))

        '''
        A
        B C
        D E F
        G H I J'''
n = int(input())
ch = 65
for i in range(1, n + 1):
    print(" " * (n - i) + " ".join(chr(ch + j) for j in range(i)))
    ch += i
    '''
    n = 5
    output :
    1
    1 1 
    1 2 1
    1 3 3 1
    1 4 6 4 1 '''
    n = int(input())
    for i in range(n):
        print(" " * (n - i), end="")
        c = 1
        for j in range(i + 1):
            print(c, end=" ")
            c = c * (i - j) // (j + 1)
        print()

    

