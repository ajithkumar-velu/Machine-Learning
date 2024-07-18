'''
n, x = int(input()), list(map(int, input().split()))
print(True if(all(0<i for i in x)) and any(str(j)==str(j)[::-1] for j in x) else False)
n, numbers = int(input()), list(map(int, input().split()))
print(True if all(x > 0 for x in numbers) and any(str(y) == str(y)[::-1] for y in numbers) else False)
k = lambda a, b, c:a+b 
d = []
for _ in range(5):
    #print (a**3)
    d.append(a**3)
    c = a+b
    a = b
    b = c
print(d)

n = 5
d = [0 if i == 0 else 1 if i == 1 else d[i-1] + d[i-2] for i in range(n)]
print(d)
'''
"""
def wrapper(f):
    def fun(l):
        # complete the function
        return f([f'+91 {mobile[-10:-5]} {mobile[-5:]}' for mobile in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
print(bool(12))
"""
"""
l = ["919025318805"]
for i in l:
    print(f"+91 {i[-10:-5]}")
w = [print(f'+91 {mobile[-10:-5]} {mobile[-5:]}') for mobile in l]
"""
#l = ["Mike Thomson": "20", "M", "Robert Bustle 32 M","Andria Bustle 30 F"]
#k = {key: value for key, value in input().split() for _ in range(3)}
#print(k)
# from collections import OrderedDict
# myDict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# print(OrderedDict(sorted(myDict.items())))
# print(myDict.keys())
# d = {f"{fn} {ln}":values for fn, ln, *values in (input().split() for i in range(2))}
# print(d)
'''
import operator

def person_lister(f):
    def inner(people):
        # complete the function
        people.sort(key=lambda x: (int(x[2])))
        print(people)
        return map(f, people)
    return inner

@person_lister
def name_format(person):
    print("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
'''
"""
from collections import OrderedDict
dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
print(dict)
v = sorted(dict.values())
print(v)
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
n=5
"""
for i in range(n+1):

    print(("#"*i).rjust(n))
print("#")
"""
"""
arr = [1, 2, 3, 4, 5]
t = set()
a = arr
for i in range(len(arr)):
    if arr[i] != False:
        
print(min(t), max(t))
"""
# from collections import Counter
# a = [4, 2, 3, 4, 4, 4]
# s = Counter(a)
# print(max(s.values()))
# print(s)
# for i in range(len(a)):
#     b=a.count(4)
#     print(b)
'''
``s = "04:59:59AM"
if s[-2:] == "PM":
    if int(s[:2]) == 12:
        print(s[:8])
    else:
        print(f"{int(s[:2])+12}:{s[3:8]}")
else:
    if int(s[:2]) == 12:
        print(f"0{abs(int(s[:2])-12)}:{s[3:8]}")
    else:
        print(s[:8])
'''


# def kangaroo(x1=2, v1=1, x2=1, v2=2):
#     # Write your code here
#     print("YES" if sum(x1,v1)==sum(x2,v2) else "NO")
# #kangaroo()
# print(sum(x1,v1))
k = lambda x: "yes" if x==1 else "NO"
print(k)