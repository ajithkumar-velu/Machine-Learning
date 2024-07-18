#Python lambda funtion to check if value is in a list
# L = [1, 2, 3, 4, 5]
# k = 4
# a = lambda k, L: True if k in L else False
# if a:
#     print("Yes")

'''
def func(x):
    return x**(1/3)
print(func(27))

a = lambda x: x**(1/3)
print(a(27))
languages = ['Sanskrut', 'English', 'French', 'German'] 

l = lambda x : True if x in languages else False
print(l("English"))

'''

# l1 = [4, 2, 13, 21, 5] 
a = []

# for i in l1:
#     r = lambda i: i**2
#     a.append(r(i))
# print(a)

# r = list(map(lambda u: u**2, l1))
# print(r)

'''
l = list(map(lambda f: f**2, filter(lambda a: a%2!=0, l1)))
print(l)

d = lambda e: True if e%2==0 else False
print(d(12))'''

# l = lambda a, b: "Equel" if a==b else (f"{a} is graterthen {b}" if a>b else f"{a} is lessthen {b}")
# print(l(1, 2))

# a = lambda a: a**a if(a>0) else None
# print(a(2))

# a = list(map(lambda a: a**2, range(0, 5)))
# print(a)

# d = lambda a= 1, b=2: lambda c: a+b+c
# s = d()
# print(d()(10))


# list1 = [10, 21, 4, 45, 66, 93, 1]

# a, b =0, 0
# l = len(list(filter(lambda a: a if a%2==0 else None, list1)))
# print(l)

# print(9^2)

# arr1 = [1, 3, 4, 5, 7]
# arr2 = [2, 3, 5, 6]
# s =list(filter(lambda x : x in arr2, arr1))
# print(s)

'''
input = 'grrksfoegrrks'
c1 = 'e'
c2 = 'r'

d = list(map(lambda r: c1 if r==c2 else (c2 if r==c1 else r), input))
d = ''.join(d)
print(d)

my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70]
g = list(filter(lambda e:e if e%13==0 else None, my_list))
print(g)

my_list = ["geeks", "geeg", "keek", "practice", "aa"] 
r = list(filter(lambda a: a==a[::-1], my_list))
print(r)

my_list = ["geeks", "geeg", "keegs", "practice", "aa"] 
str = "eegsk"
s = list(filter(lambda x: sorted(x)==sorted(str), my_list))
print(s)'''


# List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
# l = list(map(lambda a: sorted(a)[-2], List))
# print(l)

# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

# d = list(filter(lambda a: a%2, li))
# print(d)

# ages = [13, 90, 17, 59, 21, 60, 5]

# f = list(filter(lambda x: x>18, ages))
# print(f)

'''
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

a = list(map(lambda x: x*2, li))
print(a)
animals = ['dog', 'cat', 'parrot', 'rabbit']

f = list(map(lambda x: x.upper(), animals))
print(f)'''
# from functools import reduce
# li = [5, 8, 10, 20, 50, 100]
# l = reduce(lambda x, y: x+y, li)
# print(l)
# lis = [1, 3, 5, 6, 2, ]

# m = reduce(lambda x, y: max(x, y), lis)
# print(m)


"""
list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
l = sorted(list, key = lambda x: x["age"])
print(l)

g = sorted(list, key=lambda x: (x["age"], x["name"]))
print(g)
f = sorted(list, key=lambda x: (x["age"], x["name"]), reverse=True)
print(f)"""

# a=10 
# b=24 
# c=15
# l = lambda a, b, c: max(a, b, c)
# print(l(a, b, c))

# f = lambda a, b, c: a if a>b and a>c else (b if b>a and b>c else c)
# print(f(a, b, c))

# from functools import reduce
# a = reduce(lambda a,b: max(a, b), [a,b,c])
# print(a)

# d = sorted([a, b, c], key= lambda x: x)[-1]
# print(d)
# a= 4
# b= 7
# print((lambda: a, lambda: b)[a<b]())


# Python program to sort a string and return
# its reverse string according to pattern string

# This function will return the reverse of sorted string
# according to the pattern

pat = "asbcklfdmegnot"

str = "eksge"

priority = list(pat)

	# Create a dictionary to store priority of each character
m = {priority[i]:i for i in range(len(priority))}
print(m)
str = list(str)
str.sort(key = lambda x: m[x])
print(str)
str.reverse()
print(''.join(str))
