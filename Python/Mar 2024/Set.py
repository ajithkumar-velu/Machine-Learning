######################################### Mar 05 ##########################################################
#Find the size of a set in python

# sys
'''
from sys import getsizeof
Set1 = {"A", 1, "B", 2, "C", 3}
Set2 = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu"}
Set3 = {(1, "Lion"), ( 2, "Tiger"), (3, "Fox")}
'''
 
#using getsizeof funtion

# print(getsizeof(Set1))
# print(getsizeof(Set2))
# print(getsizeof(Set3))


#using .__sizeof__() method
'''
print(int(Set1.__sizeof__()))
print(str(Set2.__sizeof__()))
print(str(Set3.__sizeof__()))
'''

#z################################################################################################
#Iterate over aset in python   22:50

#using forloop
'''
test_set = set("geEks")

for i in test_set:
    print(i)
'''

#Analysis


# importing libraries
'''
from timeit import default_timer as timer
import random

def test_func(s):
    for i in s:
        _ = i

random.seed(21)

for i in range(5):
    s = set()
    for j in range(int(1e6)):
        j = random.random()
        s.add(j)
    start= timer()
    test_func(s)
    end = timer()
    print(str(end- start))
'''

####################################################################################################
#iterate over a set using enumerateded for loop

# test_set = set("geEks")
# for i, j in enumerate(test_set):
#     print(i, j)

########################################-----Mar 06------------------##############################################
#Analysis
'''
from timeit import default_timer as timer
import random


def set_func(i):
    for s , m in enumerate(i):
        sw = m
random.seed(21)
for i in range(5):
    i = set()
    for j in range(int(1e6)):
        j = random.random()
        i.add(j)
    start = timer()
    set_func(i)
    end =timer()
    print(end-start)
'''

#set using index number

# a = "geEks"
# for i in range(len(a)):
#     print(a[i])

# analysis

# from timeit import default_timer as timer
# import random
# def set_func(test_):
#     e =list(test_)
#     for i in range(len(e)):
#         w= i
# random.seed(21)
# for i in range(5):
#     i = set()
#     for j in range(int(1e6)):
#         j = random.random()
#         i.add(j)
#     start = timer()
#     set_func(i)
#     end = timer()
#     print(end-start)

#iterating over a set using comprehenion and list constructor/initalizer
# a = "ajith"
# b = [i for i in a]
# print(*b)


#Anakytsis
"""
from timeit import default_timer as tomer 
import random

def set_func(d):
    s = [i for i in d]

random.seed(21)
for i in range(5):
    i = set()
    for j in range(int(1e6)):
        j = random.random()
        i.add(j)
    start = tomer()
    set_func(i) 
    end =tomer()
    print(end- start)
"""

#iterating over a set using iterator and loop

# a = set("aajith")
# b = iter(a)

# while True:
#     try:
#         print(next(b))
#     except StopIteration:
#         break

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Python | maximum and minimum in a set

# sets = set([8, 16, 24, 1, 25, 3, 10, 65, 55])

# print(max(sets), min(sets))
##################################################################################################
#Python remove item from set
'''
sets = set([8, 16, 24, 1, 25, 3, 10, 65, 55])
print(sets)
'''


#pop()

# while sets:
#     sets.pop()
#     print(sets)

# discard() using rempve maximum number in a set
"""
while sets:
    print(sets)
    sets.discard(max(sets))

"""

#remove()

# while sets:
#     sets.remove(next(iter(sets)))
#     print(sets)

#----------------------------------------------------------------------------------------------
#Python| check if two list have at least one element common

# a = [1, 2, 3, 4, 5]
# b = [5, 6, 7, 8, 9]

#using loop and statement
'''
for i in a:
    a=1
    if i in b:
        a = 0
        break
if a == 0:
    print("Yes")
else:
    print("NO")
'''

#TRaversal of list

# for i in a:
#     d = 0
#     for j in b:
#         if i == j:
#             d =1
#             break
# if d ==1:
#     print("True")
# else:
#     print("False")


#sets and property
'''
a = set(a)
b = set(b)
if a&b:
    print(True)
else:
    print(False)
'''

# using intersection method
# a =set(a)
# b = set(b)
# if a.intersection(b):
#     print("a")
# else:
#     print("no")


#using collectios Counter
'''
from collections import Counter
a = Counter(a)
b = Counter(b)
def ww():
    for k , v in a.items():
        for j, e in b.items():
            if k == j:
                return "yes"
    return "No"
print(ww())
'''

# #using countof
# from operator import countOf
# f = 0
# for i in a:
#     if countOf(b, i) >0:
#         f =1
#         break
# if f==1:
#     print("True")
# else:
#     print(False)

#any and list comprehenion method
'''
print(any(i in b for i in a))
'''

#-----------------------------------------------------------------------------------------------------
#Python program to find common elements in three list using set 12:02
'''
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]


a= set(ar1)
b = set(ar2)
c = set(ar3)
d =list()
'''


# #using intersection
# e = a.intersection(b)
# f = e.intersection(c)
# print(f)

#using loop
'''
h = set()
for i in ar1:
    if i in ar2 and ar3:
        h.add(i)
print(h)
'''    

#list comprehenion

# a = [i for i in a if i in b and c]
# print(a)


# for i in ar1:
#     if i in ar2 and ar3:
#         d.append(i)
# print(list(set(d)))

#filter

'''
k = list(filter(lambda i: i in ar2 and ar3, ar1))
print(k)
'''

###########################################################################################################3
#Python | find missing and addtional values in two list 12:16

# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [4, 5, 6, 7, 8]

"""
print(list(set(list1).difference((set(list2)))))
print(set(list2).difference(list1))
"""

# import numpy as np

# a = np.array(list1)
# #print(a)

# print(np.setdiff1d(list1, list2))
# print(np.setdiff1d(list2, list1))

#---------------------------------------------------------------------------------------------------
#Python Difference between two list 12:32

'''
list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35] 
'''

#previos methods
# import numpy as np
# print(set(list1).difference(list2))

# print(np.setdiff1d(list1, list2))

#IN mthod to campare two list

'''
d = list()

for i in list1:
    if i  not in list2:
        d.append(i)
print(d)
'''

#using list comprehence

# s = [i for i in list1 if i not in list2]
# print(s)

#using set
'''
s =set(list2)
print([i for i in list1 if i not in s])
'''

#using zip()    corresponding elsement
# print(all([i==j for i, j in zip(list1, list2) if i==j]))

#Counter
'''
from collections import Counter

a = Counter(list1)
b = Counter(list2)
print(a==b)
'''

######################################################################################################33
#Python difference to find lost element from a dublicate arry

# A = [1, 4, 5, 7, 9]
# B = [4, 5, 7, 9]

# a = set(A)
# b = set(B)
# if len(a)> len(b):
#     print(list(a-b))
# else:
#     print("no")
#---------------------------------------------------------------------------------------------------

#Python program to count to number of vowels using set in given string
# import re
# string = "GeekforGeeks!"
# vowels = "AEIOUaeiou"

#using count of
# a = sum(vowels.count(i) for i in string)
# print(a)

#using ffor loop
'''
s =0
for i in string:
    if i in vowels:
        s+=1
print(s)
'''

# #using list comprehenion
# s= [vowels.count(i) for i in string]
# print(sum(s))

#RegEx
'''
pattern = re.findall(r"[AEIOUaeiou]", string)
print(len(pattern))
'''

#--------------------------------------------------------------------------------------------------------
#Concatenated string with uncommon characters in Python  15:14
'''
S1 = 'aacdb'
S2 = 'gafd'


Sq1 = set(S1)
Sq2 = set(S2)
'''
#using difference method
'''
a = set(S1).difference(S2)
b = set(S2).difference(S1)
print(''.join(a)+''.join(b))
'''

#take common characters
# c = list(Sq1&Sq2)
# d = [i for i in S1 if i not in c] + [i for i in S2 if i not in c]
# print(''.join(d))

#symmetric deffterence
'''
d = Sq1.symmetric_difference(Sq2)
print(''.join(d))
'''

#^
# print(''.join(Sq1^Sq2))

#Counter
"""
from collections import Counter
s1 = Counter(S1)
s2 = Counter(S2)

f = []
for i in s1:
    if i not in s2:
        f.append(i)
for j in s2:
    if j not in s1:
        f.append(j)
f.sort()
print(''.join(f))
"""

#-------------------------------------------------------------------------------------------------------
#Python program to accept the string which contain all vowels  # 3:48

# string = "SEEquoiaL"

# vowel = "aeiou"

#loop

# s = set()
# for i in string.lower():
#     if i in vowels:
#         s.add(i)
# if len(s) == len(vowel):
#     print("Accept")
# else:
#     print("NOt")

#   count()

'''
s = string.lower()

vowels = [s.count("a"), s.count("e"), s.count("i"), s.count("o"), s.count("u")]
if vowels.count(0)==0:
    print("Accept")
else:
    print("Not")
'''

#intersections
# print("Yes" if len(set(string.lower()).intersection(vowel))==5 else "No")

# import re
# c = re.compile(r'[^aeiou]')
# pattern = c.findall(string.lower())
# if len(pattern):
#     print("Not Accept")
# else:
#     print("Accept")

# subset
'''
if set(vowel).issubset(set(string.lower())):
    print("Accept")
else:
    print("not accept")
'''

#Counter

# from collections import Counter
# g = 0
# c = Counter(string.lower())
# for i in c:
#     if i in vowel:
#         g +=1
# if g == 5:
#     print("Accept")
# else:
#     print("Not accept")

#all()

'''
if all(v in string.lower() for v in vowel):
    print("Accept")
else:
    print("Not Accept")
'''

#difference method
# if len(set(vowel).difference(set(string.lower()))) ==0 :
#     print("Accept")
# else:
#     print("Not accept")

#-------------------------------------------------------------------------------------------------------
#Pyhton | check if given string is binary string or not


#string = "101010000111"

#using set
'''
s = set(string)
b = {'0', '1'}
if s == b or s=={"0"} or s=={"1"}:
    print("Yes")
else:
    print("NO")

'''

#iterator

# a = "01"
# v =0
# for i in string:
#     if i not in a:
#         v = 1
#         break
# if v == 0:
#     print("Yes")
# else:
#     print("NO")

#RegEx
'''
import re 
d = re.compile(r"[^01]")
if d.findall(string):
    print("Not")
else:
    print("Yes")
'''

#using try and execpt
'''
try:
    int(string, 2)
    print("yes")
except ValueError:
    print("No")
    '''

# a = string.count('1')+ string.count("0")
# if a== len(string):
#     print("Yes")
# else:
#     print("No")
# print(a)

#using replace

'''
r = "01"
for i in r:
    string = string.replace(i, "")
if len(string) == 0:
    print("Yes")
else:
    print("no")
'''

#all()

# if all(i in "01" for i in string):
#     print("Yes")
# else:
#     print("no")

# issubset()

'''
d = set("01")
if d.issubset(string):
    print("Yes")
else:
    print("NO")
print(d)
'''

#RegEx
# import re
# regex = r"[^01]"
# if re.search(regex, string):
#     print("No")
# else:
#     print("yes")

#--------------------------------------------------------------------------------------------------------
#Python set tyo check is string is pangram

#using ascii_lowercase

#string ="The quick brown fox jumps over the lazy dog".lower()
# from string import ascii_lowercase
# a = ascii_lowercase
# string= set(string)

# if set(a)-string ==set([]):
#     print("yes")
# else:
#     print("No")

#

#using replace set ascii_lowercase join sort
'''
from string import ascii_lowercase

string = string.replace(' ', '')
string = list(set(string))
string.sort()
string = ''.join(string)

a = ascii_lowercase
if string == a:
    print('Yes')
else:
    print("no")
'''

#lower replace len
# c =0
# string = string.replace(' ', "")

# string = list(set(string))
# string.sort()
# string = ''.join(string)

# print(string)
# for i in string:
#     if i in ascii_lowercase:
#         c+=1
# if ascii_lowercase == string:
#     print("Yes")
# else:
#     print("No")

#--------------------------------            Mar 07                --------------------------------------------------------
#Python set | Pairs of compelete string in two set
'''
from string import ascii_lowercase
#Python set| Pairs of complete string in two set  7:03
set1 = ['abcdefgh', 'geeksforgeeks','lmnopqrst', 'abc'] 
set2 = ['ijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz','defghijklmnopqrstuvwxyz'] 
c=0
for i in set1:
    for j in set2:
        res = i+j
        temp = list(set([i for i in res if ord(i)>=ord('a') and ord(i)<=ord('z')]))
        temp.sort()
        temp=''.join(temp)
        if ascii_lowercase == temp:
            c+=1
print(c)
'''
##########################################################################################################
#Pyrhon set | check whether a given string is heterogram or not

#usingm Conter
#input = 'the big dwarf only jumps'

# from collections import Counter
# c = Counter(''.join(input.split(" ")))
# f= 1
# for k, v in c.items():
#     if v != 1:
#         f = 0
# if f==0:
#     print("No")
# else:
#     print("yes")

#set
'''
t = ''
for i in ''.join(input.split(" ")):
    if ord(i)>=ord("a") and ord(i)<=ord('z'):
        t+=i
if len(t) == len(set(t)):
    print("yes")
else:
    print("No")

    '''
#--------------------------------------------------------------------------------------------------------
#python profgram to convert set into Tuple and Tuple into Set  10:40
#s = {'a', 'b', 'c', 'd', 'e'}
# a = [i for i in s]

# print(type((*s,)))
# print(type([*s,]))

# print(sorted(s))
# print(list(map(lambda a: a, s)))

# print([*s,])
# print(list(s.copy()))

# print(s)
# print(type(s))
# s = str(s)
# print(s)
# print(type(s))

# print(type(','.join(s)))
#from functools import reduce
# a =  reduce(lambda a, b: a+' '+b, s)
# print(a)
#d = "ajith"
# print(set())
# print(reduce(lambda a, b: set(a,b), d))

#print(dict.fromkeys(d, 0))

########################################################################################################################################
#set update() in python to dounion of an arrays

'''
input = [[1, 2, 2, 4, 3, 6],
            [5, 1, 3, 4],
            [9, 5, 7, 1],
            [2, 4, 1, 3]]
a  = set()
for i in input:
    a.update(i)
print(a)
'''
#-----------------------------------------------------------------------------------------------
# #Python intersection two list

# lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
# lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
# lst1 = set(lst1)
# print(lst1.intersection(set(lst2)))

'''
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
print(set(lst1) & set(lst2))
'''

#using filter

# lst1 = [1, 6, 7, 10, 13, 28, 32, 41, 58, 63]
# lst2 = [[13, 17, 18, 21, 32], [7, 11, 13, 14, 28], [1, 5, 6, 8, 15, 16]]

# a = [list(filter(lambda a: a in lst1, i)) for i in lst2]
# print(a)
# from functools import reduce
# d = [reduce(lambda e: e[0] ,i) for i in lst2]


#-######################################################################################################
#Python program to get all subsets of given size of a set
'''
import itertools
I = {1, 2, 3}
n = 2

# a = list(itertools.combinations(I, n))
# print(a)
e = []
for i in I:
    for j in I:
        e.append((i,j))
print(set(e))
'''

###############################################################################################################
#Python Dictionary | set and Count3er to check if frequnencies can become same
# str = 'xyyz'
# from collections import Counter

# d = Counter(str)
# s = list(set(d.values()))
# print(set(d.values()))
# if len(s)>2:
#     print("NO")
# elif  len(s) == 2 and s[1]-s[0]>1:
#     print("No")
# else:
#     print("yes")

# a = '54321'
# print(set(a))
# print(list(set(a)))
#________________________________________________________________________________________
# Python3 code to calculate age in years

# from datetime import date

# def calculateAge(birthDate):
# 	today = date.today()
# 	age = today.year - birthDate.year -((today.month, today.day) <(birthDate.month, birthDate.day))

# 	return age
	
# # Driver code 
# print(calculateAge(date(2001, 10, 29)), "years")
#----------------------------------------------------------------------------------------------------
from collections import deque
import itertools
dq = deque("abc")
dq.append('d')
dq.appendleft('z')
dq.extend('efg')
dq.extendleft('yxw')
print(dq)
dq.pop()
dq.popleft()
dq.rotate(2)
dq.rotate(-2)
print(list(itertools.islice(dq, 3, 7)))
print(dq)
