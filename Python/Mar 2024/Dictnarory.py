#sorting dictionary by key
'''
myDict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
key = sorted(myDict.keys())
r = {i:myDict[i] for i in key}
print(r)
'''  
# displaying keys in sorted ordeer
'''
key_value = {}
 
# Initializing value
key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323
for i in sorted(key_value.keys()):
    print(i, end=" ")
print(sorted(key_value.keys())
'''
#shorting Dictionary by key
'''
from collections import OrderedDict
dict = {'ravi': '10', 'rajnish': '9', 'sanjeev': '15', 'yash': '2', 'suraj': '32'}
print(OrderedDict(sorted(dict.items())))
print(dict.items())
'''
#sorting the key and vales using alphabetical using key
'''
key_value = {}
 
# Initializing value
key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323
for i in sorted(key_value.keys()):
    print((i, key_value[i]), end=" ")
'''
#Sorting the Keys and Values Alphabetically Using the Value
# Function calling
'''
def dictionairy():

	# Declaring hash function
	key_value = {}

# Initializing the value
	key_value[2] = 56
	key_value[1] = 2
	key_value[5] = 12
	key_value[4] = 24
	key_value[6] = 18
	key_value[3] = 323
	print(sorted(key_value))
	
	print(sorted(key_value.items(), key=lambda a: (a[1], a[0])))
dictionairy()
'''
#Sorting Dictionary By Value 
'''

# Creates a sorted dictionary (sorted by key)
import numpy as np

from collections import OrderedDict
dict = {'ravi': 10, 'rajnish': 9,
		'sanjeev': 15, 'yash': 2, 'suraj': 32}
print(dict)

keys = list(dict.keys())
values = list(dict.values())
sorted_value_index = np.argsort(values)
print(sorted_value_index)
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

print(sorted_dict)
'''
#------------------------------------------------------------------------------
'''
import collections
   
country_code = {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}
try :
    print(country_code["Nepal"])
except KeyError:
    print("Not found")
'''
#------------------------------------------------------------------------------
# Sum of dictionary valyes
'''
import functools, numpy as np
dict = {'a': 100, 'b': 200, 'c': 300}
l = list()
for x in dict:
    l.append(dict[x])
#print(sum(l))
s=0
for x in dict.values():
    s+=x
#print(s)
s=0
for x in dict:
    s+=dict[x]
#print(s)
#print(sum(dict.values()))
#print(functools.reduce(lambda a, b: a+dict[b], dict, 0))
#	print(sum(dict[i] for i in dict))

n = np.array(list(dict.values()))
print(sum(n))
'''
#-------------------------------------------------------------------------------
# dictionary size in byts
'''
import sys
dic1 = {"A": 1, "B": 2, "C": 3}
#print(sys.getsizeof(dict))
g = {'a': 100, 'b': 200, 'c': 300}
print(str(dic1.__sizeof__()))
# sample Dictionaries
dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}
print(sys.getsizeof(dic1))
# print the sizes of sample Dictionaries
print("Size of dic1: " + str(dic1.__sizeof__()) + "bytes")
print("Size of dic2: " + str(dic2.__sizeof__()) + "bytes")
print("Size of dic3: " + str(dic3.__sizeof__()) + "bytes")
'''
#-------------------------------------------------------------------------------
# sorted dictionary using values: itemgetter and lambada funtions
# myDict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# print(sorted(myDict.items(), key= lambda a: (a[1], a[0])))
'''
from operator import itemgetter
list = [{"name": "Nandini", "age": 20}, {"name": "Manjeet", "age": 20}, {"name": "Nikhil", "age": 19}]
print(list)
print(sorted(list, key = lambda a: (a["age"], a["name"])))
print(sorted(list, key = itemgetter("age", "name")))
'''
#--------------------------------------------------------------------------------
#merge 2 dictionaries
# Python code to merge dict using update() method
'''
# Driver code
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
# dict2.update(dict1)

# print(dict2)
from collections import ChainMap
def fun (a, b):
    res = a|b
    return res
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
s = fun(dict1, dict2)
print(s)

for i in dict2.keys():
    dict1[i]=dict2[i]
print(dict1)
g = ChainMap(dict1, dict2)
print(g)
'''
#----------------------------------------------------------------------------------------
#student mark system
'''
jack = {"name": "Jack Frost",
        "assignment": [80, 50, 40, 20],
        "test": [75, 75],
        "lab": [78.20, 77.20]
        }
 
# 2. James's dictionary
james = {"name": "James Potter",
         "assignment": [82, 56, 44, 30],
         "test": [80, 80],
         "lab": [67.90, 78.72]
         }
 
# 3. Dylan's dictionary
dylan = {"name": "Dylan Rhodes",
         "assignment": [77, 82, 23, 39],
         "test": [78, 77],
         "lab": [80, 80]
         }
 
# 4. Jessica's dictionary
jess = {"name": "Jessica Stone",
        "assignment": [67, 55, 77, 21],
        "test": [40, 50],
        "lab": [69, 44.56]
        }
 
# 5. Tom's dictionary
tom = {"name": "Tom Hanks",
       "assignment": [29, 89, 60, 56],
       "test": [65, 56],
       "lab": [50, 40.6]
       }
def grade(a):
    if a>=90:
        return "A"
    elif a>=80:
        return "B"
    elif a>=70:
        return "C"
    elif a>=60:
        return "D"
    else:
        return "E"
    
def  aver(a):
    return sum(a)/len(a)
def cal(a):
    ass = aver(a["assignment"])
    test = aver(a["test"])
    lab = aver(a["lab"])
    f = ass*0.1 + test*0.7 + lab*0.2
    return grade(f)
students = [jack, james, dylan, jess, tom]
for i in students:
    print(f"{i["name"]} grade is {cal(i)}")
'''
#----------------------------------day 2-----------------------------------------------------
# find three array common element
# Function to find common elements in three
# sorted arrays
'''
from collections import Counter
def commonElement(a, b, c):
	a = Counter(a)
	b = Counter(b)
	c = Counter(c)
	d = [i for i in (a & b & c)]
	print(d)
# Driver program
if __name__ == "__main__":
	ar1 = [1, 5, 10, 20, 40, 80]
	ar2 = [6, 7, 20, 80, 100]
	ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
	commonElement(ar1,ar2,ar3)
'''
#-----------------------------------------------------------------------------------------------
# find the win in election
'''
from collections import Counter
from operator import itemgetter
def electionresult(voter):
	counting = Counter(voter)
	b = max(counting.values())
	c =[i for i, j in counting.items() if j==b]
	print(c[0])
votes = ["john", "johnny", "jackie",  "johnny", "john", "jackie",  "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny", 
                    "john"]
electionresult(votes)
'''
#-----------------------------------------------------------------------------------------
#find the maxmamum unquie values
'''
from collections import Counter
from operator import itemgetter
test_dict = {"Gfg": [5, 7, 5, 4, 5],
             "is": [6, 7, 4, 3, 3],
             "Best": [9, 9, 6, 5, 5]}
k = sorted(test_dict, key=lambda a: len(set(test_dict[a])))[-1]
print(k)
'''
#-----------------------------------------------------------------------------------------
#from collections import Counter
#using not in method
#find yhe dublicates in dictionary
'''
s = "geeksforgeeks"
c = {}
for i in s:
    if i not in c:
        c[i] =1
    elif i in c:
        c[i] += 1
    dublicate = []
    for i, j in c.items():
        if 1<j:
            dublicate.append(i)
print(dublicate)
'''
# using Counter method
# s = "geeksforgeeks"
# print([i for i, j in Counter(s).items() if j>1])

'''
s = "geeksforgeeks"
c=  []
for i in s:
    if s.count(i)>1 and i not in c:
        c.append(i)
print(c)
'''
#using filter()
# s = "geeksforgeeks"
# a = filter(lambda x: s.count(x)>1 ,s)
# print(" ".join(set(a)))
#-----------------------------------feb29-------------------------------------------------
# group similer item to dictionary vales
#using defaultdict
'''
from collections import Counter, defaultdict
test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]
d = defaultdict(list)
r = {}
for i in test_list:
    d[i].append(i)
print(d)
'''
#using Counter and list comprhsion
# from collections import Counter
# test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]
# c = Counter(test_list)
# s  = {i:[i]*j for i, j in Counter(test_list).items()}
# print(s)

#using set() snd list comprehsion
'''
test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]
s = set(test_list)

d = {i:[i]*test_list.count(i) for i in s}
print(d)
l = {i:[] for i in s}
#2
[l[i].append(i) for i in test_list]
print(l)
# '''

# from itertools import groupby
# test_list = a_list = [("Animal", "cat"),  
#           ("Animal", "dog"),  
#           ("Bird", "peacock"),  
#           ("Bird", "pigeon")]
# l = groupby(test_list, lambda s: s[0])
# for i, j in l:
#     d = {i:list(j)}
# print(d)
#-----------------------------------------------------------------------------------------
#K’th Non-repeating Character in Python using List Comprehension and OrderedDict
'''
from collections import Counter
s = "geeksforgeeks"
g=3
h = [i for i, j in Counter(s).items() if j==1]
print(h[g-1])
'''
#-----------------------------------------------------------------------------------------
#Python – Replace String by Kth Dictionary value
# test_list = ["Gfg", "is", "Best"]
 
# # printing original list
# print("The original list : " + str(test_list))
 
# # initializing subs. Dictionary
# subs_dict = {
#     "Gfg" : [5, 6, 7], 
#     "is" : [7, 4, 2], 
# }
# k= 2
''' #list comprehsion
res = [i if i not in subs_dict else subs_dict[i][k] for i in test_list]
print (res)
'''
# get() & listcomprehsion

# res = [subs_dict.get(i, i)  for i in test_list]
# re = [i[k] if isinstance(i, list) else i for i in res]
# print(re)
'''
def f(s):
    return subs_dict[s][k] if s in subs_dict else s
res = list(map(f, test_list))
print(res)
'''
#------------------------------------------------------------------------------------------
#Python | Ways to remove a key from dictionary
'''
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
print(test_dict)
'''

#1)using del
# del test_dict['Mani']
# print(test_dict)

#2)using pop
'''
test_dict.pop("Mani")
print(test_dict)
'''
#3)using dict comperhsion and items
# a = {key:value for key, value in test_dict.items() if key != "Mani"}
# print(a)

#4) using dict comprehsion
'''
a = {key:test_dict[key] for key in test_dict if key != "Mani"}
print(a)
'''
# #using loop
# l = {}
# for i in test_dict:
#     if i != "Arushi":
#         l[i]=test_dict[i]
# print(l)

# Delete All items in dictionary
"""
del test_dict
try:
    print(test_dict)
except:
    print("Deleted")
"""
#2) using clear()
# test_dict.clear()
# print(test_dict)
#------------------------------------------------------------------------------------------
#Python – Replace words from Dictionary
# split get join
# test_str = 'geekforgeeks best for geeks'
# print(test_str)
# lookp_dict = {"best" : "good and better", "geeks" : "all CS aspirants"}
'''
k = []
s = test_str.split()
for i in s:
    k.append(lookp_dict.get(i, i))
print(" ".join(k))
'''
# using list comprehsion and join

# print(" ".join([lookp_dict.get(i, i)  for i in test_str.split()]))

#Using loop and lemp list
'''
f = []
for i in test_str.split():
    if i not in lookp_dict:
        f.append(i)
    else:
        f.append(lookp_dict[i])
print(" ".join(f))
'''
#----------------------------------------Mar 1---------------------------------------------------
#Python – Remove Dictionary Key Words
'''
import re
test_str = 'gfg is best for geeks'
print("The original string is : " + str(test_str))
test_dict = {'geeks': 1, 'best': 6}
'''

# #1) split join replace
# for i in test_dict:
#     if i in test_str.split():
#         test_str = test_str.replace(i, "")
# print("".join(test_str))

#2) join split
'''
a = test_str.split()
print(" ".join([i for i in test_str.split() if i not in test_dict.keys()]))
'''
#3) lambda function
# l = list(filter(lambda a:a not in test_dict, test_str.split()))
# print(" ".join(l))

#4) re module 
'''
pattern = "|".join(test_dict)
result = re.sub(pattern, "", test_str)
print(result)
'''
#------------------------------------------------------------------------------------------
#Python | Remove all duplicates words from a given sentence

#1) Counter
# from collections import Counter
# s = "Python is great and Java is also great"
# print(f"Orginal string: {s}")
# # s = s.split()
# # print(" ".join((Counter(s)).keys()))
# s = s.split()
# a = []
# for i in s:
#     if i not in a:
#         a.append(i)
# print(" ".join(a))

# Python3 program
#2) dict.fromkeys() its return key: none
'''
string = 'Python is great and Java is also great'
print(dict.fromkeys(string.split(), 1))

print(' '.join(dict.fromkeys(string.split())))
'''
# set()
# # print(" ".join(set(s.split())))
# from functools import reduce
# unique_words = reduce(lambda x, y: x if y in x else x + [y], [[], ] + s.split())
# print(" ".join(unique_words))

#-------------------------------------------------------------------------------------------
#Python – Remove duplicate values across Dictionary Values
#from collections import Counter
# test_dict = {'Manjeet': [1, 4, 5, 6],
#              'Akash': [1, 8, 9],
#              'Nikhil': [10, 22, 4],
#              'Akshat': [5, 11, 22]}
'''
#using Countert and list comprehsion
c = Counter()
for i in test_dict.values():
    c.update(i)
res = {key: [v for v in value if c[v]==1] for key, value in test_dict.items()}
print(res)
'''
#Method #2 : Using extend(),count(),keys() methods and for loops
# v = []
# for i in test_dict.values():
#     v.extend(i)
# s = []
# for i in v:
#     if v.count(i) ==1:
#         s.append(i)
# print(s)
# d = dict()
# for key in test_dict.keys():
#     a = []
#     for k in test_dict[key]:
#         if k in s:
#             a.append(k)
#         d[key]= a
# print(d)

#Method #3: Using extend(),operator.countOf(),keys() methods and for loops
'''
import operator
e = []
for i in test_dict.values():
    e.extend(i)
y = []
for i in e:
    if (operator.countOf(e, i))==1:
        y.append(i)
d =dict()
for i in test_dict.keys():
    h = []
    for j in test_dict[i]:
        if j in y:
            h.append(j)
        d[i]= h
print(d)
'''

#Method #4: Using defaultdict() and set()
# from collections import defaultdict
# d = defaultdict(set)
# for i in test_dict.values():
#     for j in i:
#         d[j].add(id(i))
# res ={}
# for key, value in test_dict.items():
#     l = []
#     for k in value:
#         if len(d[k]) == 1:
#             l.append(k)
#         res[key]=l
# print(res)

#Method #5: Using list comprehension and dictionary comprehension
'''
from collections import Counter
re = [d for i in test_dict.values()  for d in i]
un = [i for i, j in (Counter(re)).items() if j==1 ]
d = {key:[k for k in value if k in un] for key, value in test_dict.items()}
print(d)
'''
#Method #6:  Using numpy:
# import numpy
# d = {}
# for i in test_dict.values():
#     un = numpy.unique(i)
#     print(un)

#-------------------------------------------------------------------------------------------
#reverseAlphabet = "zyxwvutsrqponmlkjihgfedcba"
'''
r = "zyxwvutsrqponmlkjihgfedcba"
s = r[::-1]
d = dict(zip(r,s))
input = 'paradox'
k =3
f = input[:k-1]
m = [d[i] for i in input[k-1:]]
print(f+''.join(m))
'''
#------------------------------------------------------------------------------------------
#Counting the frequencies in a list using dictionary in Python
#counter
#my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
'''
from collections import Counter
a = Counter(my_list)
[print("%d:%d"%(k, v)) for k, v in a.items()]
'''
#using loop and temp veriable
# k = {}
# for i in my_list:
#     if i not in k:
#         k[i]=1
#     else:
#         k[i]+=1
# {print("%d:%d"%(i, j)) for i, j in k.items()}

# count
'''
k = {}
for i in my_list:
    k[i]=my_list.count(i)
for i, j in k.items():
    print("%d:%d"%(i, j))
'''
#get()
# d = {}
# for i in my_list:
#     d[i] = d.get(i, 0)+1
# print(d)

#operator import countof
'''
from operator import countOf
s = {}
for i in my_list:
    s[i] = countOf(my_list, i)
for i, j in s.items():
    print("%d:%d"%(i, j))
'''
#----------------------------------------------------------------------------------------------
#Python - Dictionary values mean
#test_dict = {"Gfg" : 4, "is" : 7, "Best" : 8, "for" : 6, "Geeks" : 10} 

# k = 0
# for i in test_dict.values():
#     k = k+i
# print(k)
# print(k/len(test_dict))

#sum, len, values
'''
s = sum(test_dict.values())
l = len(test_dict)
print(s/l)
'''

#Method #3 : Using values() and mean() method of statistics module
# from statistics import mean
# print(mean(test_dict.values()))

#Method 4:Using the reduce function from the functools library
'''
from functools import reduce
d = reduce(lambda x, y: x+y, test_dict.values(), 0)
print(d/len(test_dict.values()))
'''

# using numpy
# import numpy
# print(numpy.mean(list(test_dict.values())))
# print(list(test_dict.values()))


#=--------------------------------Mar 02--------------------------------------------------------


#Python counter and dictionary intersection example (Make a string using deletion and rearrangement)
'''
from collections import Counter
str1 = 'ABHISHEKsinGH1'
str2 = 'gfhfBHkooIHnfndSHEKsiAnG'
str1 = Counter(str1)
str2 = Counter(str2)
print("yes" if(str1&str2)==str1 else "No")
'''
#-------------------------------------------------------------------------------------------------
#Python dictionary, set and counter to check if frequencies can become same
# from collections import Counter
# input = 'xxxyyzzt'
# c = Counter(input)
# k = list(set(c.values()))
# if len(k)>2:
#     print("No")
# elif len(k) == 2 and k[1]-k[0]>1:
#     print("No")
# else:
#     print("Yes")
#------------------------------------------------------------------------------------------------
#Possible Words using given characters in Python
# from collections import Counter
# input = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
# charSet = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
# def charCount(word):
#     dict = {}
#     for i in word:
#         if i not in dict:
#             dict[i]= 1
#         else:
#             dict[i]+=1
#     print(dict)
# word = "goooo"
# print(dict(Counter(word)))
# charCount(word)

'''
for i in input:
    d = dict(Counter(i))
    f=0
    for g in d:
        #print(f'{charSet.count(g)}=={d[g]}')
        if g not in charSet:
            f = 1
        elif charSet.count(g)!=d[g]:
            f=1
  

    if f ==0:
        print(i)
'''
# set().issubset()

# for i in input:
    
#     if set(i).issubset(set(charSet)):
#         print(i)
#----------------------------------Mar 03--------------------------------------------------------
#Python – Maximum record value key in dictionary
# from functools import reduce
# test_dict = {'gfg' : {'Manjeet' : 5, 'Himani' : 10},
#              'is' : {'Manjeet' : 8, 'Himani' : 9},
#              'best' : {'Manjeet' : 10, 'Himani' : 15}}
# k = 'Himani'
#using loop
'''
o = 0
j = None
for i in test_dict:

    if test_dict[i][key]>o:
        o = test_dict[i][key]
        n = i
print(n)
'''
# lambda max()
#print(str(max(test_dict, key= lambda j: test_dict[j][k])))

#Method 3: list comprehsion
# l = [i[k] for i in test_dict.values()]
# m = max(l)
# i = l.index(m)
# r = list(test_dict.keys())
# print(r[i])
#-------------------------------------------------------------------------------------------------
#Python – Extract values of Particular Key in Nested Values


#
#loop
# t= []
# for i in test_dict.keys():
#     t.append(test_dict[i][temp])
# print(t)

#list comprehsion and items()
'''
l = [test_dict[i][temp] for i, j in test_dict.items() if temp in j]
print(l)
'''
#------------------------------------------------------------------------------------------------
# Python – Convert Key-Value list Dictionary to List of Lists

#loop
#test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
'''
s =[]
for k, v in test_dict.items():
    s.append([k]+v)
print(s)
'''

#List comphersions
# l = [[i]+j for i, j in test_dict.items()]
# print(l)

#map dict.keys()
'''
r = list(map(lambda a: [a]+test_dict[a], test_dict.keys()))
print(r)
'''
#keys() insert()
# l = []
# for i in test_dict.keys():
#   test_dict[i].insert(0, i)
#   l.append(test_dict[i])
# print(l)

#zip() list comprehsion
'''
l = [[i]+j for i , j in zip(test_dict.keys(), test_dict.values())]
print(l)
'''
# nusted list comphreshion

# l = [[i]+test_dict[i] for i in test_dict]
# print(l)

#Method 7: Using the items() method of the dictionary along with a for loop. 
'''
l = []
for i, j in test_dict.items():
    l.append([i]+j)
print(l)
'''

#---------------------------------------------------------------------------------------------------
#Python – Convert List to List of dictionaries

#Method #1 : Using loop + dictionary comprehension
'''
test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
key_list = ["name", "number"]
'''
# l = []
# for i in range(0, len(test_list), 2):
#     l.append({key_list[0]:test_list[i], key_list[1]:test_list[i+1]})
# print(l)

#Method #2 : Using dictionary comprehension + list comprehension
'''
l = [{key_list[0]:test_list[i], key_list[1]:test_list[i+1]} for i in range(0, len(test_list), 2)]
print(l)
'''

#----------------------------------------------------------------------------------------------------
#Python – Convert Lists of List to Dictionary
'''
from functools import reduce
test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
'''
# res =dict()
# for i in test_list:
#     res[tuple(i[:2])]=tuple(i[2:])
# print(res)
'''
l = {tuple(i[:2]):tuple(i[2:]) for i in test_list}
print(l)
'''
# def a(c, d):
#     c.update(d)
#     return c
# l = reduce(a, [{tuple(i[:2]):tuple(i[2:])} for i in test_list])
# print(l)
#-------------------------------------------------------------------------------------------------
#Python – Convert List of Dictionaries to List of Lists

# import pandas as pd

# test_list = [{'Nikhil' : 17, 'Akash' : 18, 'Akshat' : 20},
#              {'Nikhil' : 21, 'Akash' : 30, 'Akshat' : 10},
#              {'Nikhil' : 31, 'Akash' : 12, 'Akshat' : 19}]
# # l = list()
# k = []
# for i, j in enumerate(test_list):
#     if i == 0:
#         k.append(list(j.keys()))
#         k.append(list(j.values()))
#     else:
#         k.append(list(j.values()))
# print(k)
#list comprehsion
'''
l = [[i for i in test_list[0]], [list(j.values()) for j in test_list]]
print(l)
'''

#map lambda
# res = list(map(lambda x: list(x.values()), test_list))
# res.insert(0, list(test_list[0].keys()))
# print(res)

# pandas
'''
res = pd.DataFrame(test_list)
k = res.values.tolist()
k.insert(0, list(test_list[0].keys()))
print(k)
'''

# k = list(test_list[0].keys())
# v = [list(i.values()) for i in test_list]
# z = [k]+list(zip(*v))
# print(z)
#----------------------------------------------------------------------------------------------------------

#Python – Convert key-values list to flat dictionary

# test_dict = {'month' : [1, 2, 3],
#              'name' : ['Jan', 'Feb', 'March']}

#print(dict(zip(test_dict["month"],test_dict['name'])))

#values and dict 
'''
k = list(test_dict.values())
d = dict()
for i in range(len(k[0])):
    d[k[0][i]]= k[1][i]
print(d)
'''

#idct comprehsion

# a = {test_dict['month'][i]:test_dict['name'][i] for i in range(len(test_dict["month"]))}
# print(a)

'''
res=dict()
for i in range(len(test_dict['month'])):
    res[test_dict["month"][i]]=test_dict["name"][i]
print(res)
'''
#----------------------------------------------------------------------------------------------------
#Python | Convert a list of Tuples into Dictionary

# def dic(t, d):
#     for i, j in t:
#         d.setdefault(i, [])
#     print(d)

# tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
#         ("suraj", 20), ("akhil", 25), ("ashish", 30)]

# d =dict()
#dic(tups, d)
'''
for i in range(len(tups)):
    d[tups[i][0]]= tups[i][1]
print(d)
'''
# d =dict()
# for n, m in tups:
#     d.setdefault(n, []).append(m)
# print(d)

'''
d = dict(tups)
print(d)
'''

# for i in tups:
#     if i[0] not in d:
#         d[i[0]]= [i[1]]
# print(d)

'''
res = {i:[j] for i, j in tups}
print(res)
'''
#-----------------------------------------------------------------------------------------------------
#Python – Convert Nested dictionary to Mapped Tuple

# from collections import defaultdict
# test_dict = {'gfg' : {'x' : 5, 'y' : 6}, 'is' : {'x' : 1, 'y' : 4},
#                                       'best' : {'x' : 8, 'y' : 3}}
# l =defaultdict(tuple)

# #Method #1 : Using list comprehension + generator expression
# f = [(x, tuple(h[x] for h in test_dict.values())) for x in test_dict['gfg']]
# print(f)

# Method #2 : Using defaultdict() + loop
'''
for i , j in test_dict.items():
    for s in j:
        l[s]+=(j[s],)
print(str(list(l.items())))
'''
# d = [(i, tuple(test_dict[j][i] for j in test_dict)) for i in test_dict['gfg']]
# print(d)

#-----------------------------------------------------------------------------------------------------
# way to conver string to dictionary
#Method 1: Splitting a string to generate a key: value pair of the dictionary

#str = " Jan = January; Feb = February; Mar = March"
#print(dict(i.split("=") for i in str.split(";")))

#ethod 2: Using 2 strings to generate the key:value pair for the dictionary 
'''
str1 = "Jan, Feb, March"
str2 = "January | February | March"
str1 = str1.split(",")
str2 = str2.split("|")
'''


'''
d = dict()
for i in range(len(str1)):
    d[str1[i]]= str2[i]
print(d)
'''
# # using zip() method to combian the key:value pairs extract from 2 strings
# print(dict(zip(str1, str2)))

#Method 4: If the string is itself in the form of string dictionary
'''
import ast
str = '{"Jan" : "January", "Feb" : "February", "Mar" : "March"}'

d = ast.literal_eval(str)
print(d)
'''
#using split() index slicing
# v = dict()
# str = " Jan = January; Feb = February; Mar = March"
# for i in str.split(";"):
#     a = i[:i.index("=")]
#     b = i[i.index("=")+1:]
#     v[a]=b
# print(v)

#------------------------------------------------------------------------------------------------------
#Python – Convert dictionary to K sized dictionaries

# import itertools
# test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3, 'for' : 4, 'geeks' : 5, 'CS' : 6}
# k = 2

#using loop
'''
l = list()
d = dict()
c = 0
for i in test_dict:
    d[i]=test_dict[i]
    c+=1
    if c == k:
        l.append(d)
        c = 0
        d=dict()

# printing result 
print("The converted list : " + str(l)) 
'''

#using list comprehsion
# print(len(test_dict))
# s = [dict(list(test_dict.items())[i:k+i]) for i in range(0, len(test_dict), k)]
# print(s)

#ittertools iter islice
'''
s = list()
i = iter(test_dict.items())
while True:
    e = dict(itertools.islice(i, k))
    if not e:
        break
    s.append(e)
print(s)
'''

#-------------------------------------------------------------------------------------------------
#python - convert matrix to Dictionary
'''
d = dict()
test_list = [[5, 6, 7], [8, 3, 2], [8, 2, 1]] 
'''

# #loop
# for i in range(len(test_list)):
#     d[i+1]=test_list[i]
# print(d)

#dict comprehsion
'''
s = {i+1:test_list[i] for i in range(len(test_list))}
print(s)
'''

# #enumerate
# a = {i+1:test_list[i] for i, j in enumerate(test_list)}
# print(a)

#-------------------------------------Mar 04---------------------------------------------------------------
#creating a nusted dictionary using givan liast
'''
test_dict = {'Gfg' : 4, 'is' : 5, 'best' : 9} 
test_list = [8, 3, 2, 0]
d = dict()
'''

# #loop
# c =0
# for i, j in test_dict.items():
#     d[test_list[c]]={i:j}
#     c+=1
# print(d)

#zip
'''
z = dict(zip(test_list, dict(test_dict.items())))
d =dict()
for i, j in zip(test_list, test_dict.items()):
    d[i] = dict([j])
print(d)
'''

#zip dict comprehsion

# l = {i:dict([j]) for i, j in zip(test_list, test_dict.items())}
# print(l)

#---------------------------------------------------------------------------------------------
#Swapping hierarchy in nusted dictionary
# from collections import defaultdict
# test_dict = {'Gfg': { 'a' : [1, 3], 'b' : [3, 6], 'c' : [6, 7, 8]},
#              'Best': { 'a' : [7, 9], 'b' : [5, 3, 2], 'd' : [0, 1, 0]}}
# res = dict()

'''
for key, val in test_dict.items():
    for key_in, val_in in val.items():
        if key_in not in res:
            temp = dict()
        else:
            temp = res[key_in] # a:
        temp[key] = val_in      #gfg:[1,3]
        res[key_in] = temp      #a:gfg[1, 3]
print(str(res))
'''

# loop, defaultdict
'''
d = defaultdict(dict)
for k, v in test_dict.items():
    for a, b in v.items():
        d[a][k] = b
print(dict(d))
'''
#----------------------------------------------------------------------------------------------------
# #python reverse distionaykeys order
# from collections import OrderedDict, deque

# test_dict = {'gfg' : 4, 'is' : 2, 'best' : 5}
'''
a = OrderedDict(reversed(list(test_dict.items())))
print(dict(reversed(list(test_dict.items()))))
'''

# #deque

# from collections import OrderedDict, deque #import deque

# def reverse_dict_keys_order(test_dict):#define input
# 	keys_deque = deque(test_dict.keys())#get keys
# 	keys_deque.reverse()#reverse the keys
# 	new_dict = {key: test_dict[key] for key in keys_deque}#assign values to the key
# 	new_ordered_dict = OrderedDict(new_dict)#assign to new dict
# 	return new_ordered_dict#return result

# test_dict={'is': 2, 'gfg': 4,'best': 5}#input
# print(reverse_dict_keys_order(test_dict))#print output


#popitem()
'''
s = dict()
while test_dict:
    a , b= test_dict.popitem()
    s[a]=b
print(s)
'''
# from operator import countOf
# # # sorted reversed
# # a = {i:test_dict[i] for i in sorted(test_dict, key=lambda x: list(test_dict.keys()).index(x), reverse=True)}
# # print(a)

# #extract key's value if key presend in list and distionary

# test_list = ["Gfg", "is", "Good", "for", "Geeks"]
 
# # initializing Dictionary
# test_dict = {"Gfg" : 2, "is" : 4, "Best" : 6}

# K = "Gfg"

#all
'''
r = None
if all(K in i for i in [test_dict, test_list]):
    r = test_dict[K]
print(r)
'''

# #set()
# if K in set(test_list).intersection(test_dict):
#     print(test_dict[K])

# operator
'''
if K in test_dict and K in test_list:
    print(test_dict[K])
'''

#countof

# if countOf(test_dict, K)>0 and countOf(test_list, K)>0:
#     print(test_dict[K])

#any
'''
if K in test_dict and K in test_list:
    print(test_dict[K])
'''

#try except

# try:
#     if K in test_list and K in test_dict.keys():
#         print(test_dict[K])
# except KeyError:
#     res = None

#try except get()
'''
try:
    if K in test_dict and K in test_list:
        print(test_dict.get(K))
except:
    pass
'''

# # loop to iterat alll
# for i in test_list:
#     if i == K:
#         print(test_dict.get(K))
#         break

#numpy
'''
import numpy as np
if np.isin(K, test_list) and np.isin(K, list(test_dict.keys())):
    print(test_dict.get(K))
'''
#-----------------------------------------------------------------------------------------------------
#remove keys with values gtaterth K(including max values)

# test_dict = {'Gfg' : 3, 'is' : 7, 'best' : 10, 'for' : 6, 'geeks' : 'CS'} 
# K=7
# e = dict()
# for i in test_dict:
#     if isinstance(test_dict[i], str):
#         e[i]=test_dict[i]
#     elif k>test_dict[i]:
#         e[i]=test_dict[i]
# print(e)

#dictionary comprehion isinstance
'''
res = dict(filter(lambda item: not (isinstance(item[1], int) and item[1] > K-1), test_dict.items()))
print(res)
'''

#---------------------------------------------------------------------------------------------------------
#python remove keys with substring values

# test_dict = {1 : 'Gfg is best for geeks', 2 : 'Gfg is good', 3 : 'I love Gfg'}
# sub_list = ['love', 'good']
# d = dict()

#for loop
"""
for k, v in test_dict.items():
    if not any(i in v for i in sub_list):
        d[k]=v
print(d)
"""

# #using dictionary comprehsion + any()
# l = {k:v for k, v in test_dict.items() if not any(i in v for i in sub_list)}
# print(l)

#pop
'''
for k, v in list(test_dict.items()):
    print(k, v)
    for j in sub_list:
        if j in v:
            test_dict.pop(k)
print(test_dict)
'''
#labda and filter()
# l = dict(filter(lambda x: not any(i in x[1] for i in sub_list) , test_dict.items()))
# print(l)

#-------------------------------------------------------------------------------------------------
#python Dictionay with count of pairs 1.26

# test_list = [{"gfg": 2, "best" : 4},  
#              {"gfg": 2, "is" : 3, "best" : 4},  
#              {"gfg": 2}] 
# # s = 0
# d = {}
# for i in test_list:
#     if len(i)>s:
#         s =len(i)
#         d = i
# print(d)

#map key len
'''
print(max(test_list, key=len))
'''

#------------------------------------------------------------------------------------------------------
#Append dictionay keys ad vaues in Dictionay 1.45

#using list() key() values()
'''
test_dict = {"Gfg" : 1, "is" :  3, "Best" : 2}
'''
'''
l = list()
for i in test_dict.keys():
    l.append(i)
for j in test_dict.values():
    l.append(j)
print(l)
'''
# #list() keys() values()
# print(list(test_dict.keys())+list(test_dict.values()))

# from itertools import chain
# print(list(chain(test_dict.keys(), test_dict.values())))

#using list() keY() values() eextend()
'''
a = list(test_dict.keys())
b = list(test_dict.values())
a.extend(b)
print(a)
'''

#using zip() fintion and list comprehions

# l = [i for i in zip(test_dict.values(), test_dict.keys())]
# print(l)

#using sorted and list comprehsion

# k = list(test_dict.keys())
# v = [i for i in test_dict.values()]
# print(k+v)

#---------------------------------------------------------------------------------------------------
#Python Extract unique values Dictionary values 2:04
# from itertools import chain
# test_dict = {'gfg': [5, 6, 7, 8],
#              'is': [10, 11, 7, 5],
#              'best': [6, 12, 10, 8],
#              'for': [1, 2, 5]}
# l = list(sorted({j for i in test_dict.values() for j in i}))
# print(l)


# l = [j for i in test_dict.values() for j in i]
# print(set(l))

#chain sorted values
'''
from itertools import chain

print(list(sorted(set(chain(*test_dict.values())))))
'''

#extend and sort()

# l = list(test_dict.values())
# d = list()
# for i in l:
#     d.extend(i)
# f = list()
# for i in d:
#     if i not in  f:
#         f.append(i)
# f.sort()
# print(f)

#Counter append sort()
'''
from collections import Counter
d = list(j for i in test_dict.values() for j in i)
a = Counter(d)
h = list(a.keys())
h.sort()
print(h)
'''

# #operator.countof
# from operator import countOf

# a = list(test_dict.values())
# l =[j for i in a for j in i]
# h = list()
# for i in l:
#     if countOf(h, i) == 0:
#         h.append(i)
# h.sort()
# print(h)

'''
a = list(set(sum(test_dict.values(), [])))
print(a)
'''

#------------------------------------------------------------------------------------------------------
#Python keys associated with values in dictionary
# from collections import defaultdict
# test_dict = {'gfg' : [1, 2, 3], 'is' : [1, 4], 'best' : [4, 2]} 

# d = defaultdict(list)
# for k, v in test_dict.items():
#     for i in v:
#         d[i].append(k)
# print(str(dict(d)))

#dict comprehsion + dict
'''
d = {}
for k, v in test_dict.items():
    for i in v:
        if i in d:
            d[i].append(k)
        else:
            d[i]=[k]
print(d)
'''

# #using setdefault()
# d =dict()
# for k, v in test_dict.items():
#     for i in v:
#         d.setdefault(i, []).append(k)
# print(d)

#----------------------------------------------------------------------------------------------------
#Python - filter dictioary values in heterogeneous dictionary 6.48

# test_dict = {'Gfg' : 4, 'is' : 2, 'best' : 3, 'for' : 'geeks'}
# k =3

#type dictionary comprehsion
# d = dict()
# for k, v in test_dict.items():
#     if type(v) != int or v>3:
#         d[k]=v
# print(d)

# isintance dictionary comprehenion
'''
d = {key:val for key, val in test_dict.items() if not isinstance(val, int) or val>k}
print(d)
'''

# #filter lambda
# f = dict(filter(lambda item: not(isinstance(item[1], int) and item[1]<=k), test_dict.items()))
# print(f)

#-------------------------------------------------------------------------------------------------
# #print anagrams togather in python using list and dictionary
# input=['cat', 'dog', 'tac', 'god', 'act']
# d = dict()
# for i in input:
#     k = ''.join(sorted(i))
#     if k in d.keys():
#         d[k].append(i)
#     else:
#         d[k] = []
#         d[k].append(i)
# o = ''  
# for key, val in d.items():
#     o = o+" ".join(val)+" "

#------------------------------------Mar 05 6:46----------------------------------------------------------------
#Python Dictionay | check if binary representation of two numbers of anagram
#from collections import Counter
# a = 8 
# b = 4
# a = bin(a)[2:]
# b = bin(b)[2:]

# l = len(a)-len(b)
# if len(a)>len(b):
#     b = l*'0'+b
# else:
#     a = l*"0"+b
# a = Counter(a)
# b = Counter(b)
# if a==b:
#     print("Yes")
# else:
#     print("No")

#zfill(4)
'''
a = 8
b = 4

a = bin(a)[2:].zfill(32)
b = bin(b)[2:].zfill(32)
s = Counter(a)
f = Counter(b)
if s == f:
    print("Yes")
else:
    print("No")
'''

#--------------------------------------------------------------------------------------------------
# #Python Conter to find the size of largest subset of anagrams words
# from collections import Counter
#input = 'ant magenta magnate tan gnamate'
# input = input.split(" ")
# print(input)
# for i in range(len(input)):
#     input[i] = "".join(sorted(input[i]))
# a = Counter(input)
# print(max(a.values()))

#d = dict()
'''
for i in input.split(" "):
    s = ''.join(sorted(i))
    if s not in  d:
        d[s]=[]
    d[s].append(i)
st =max([len(i) for i in d.values()])
print(st)
'''
#------------------------------------------------------------------------------------------------
#Python sort Dictionary keys and values List 9:05
'''
test_dict = {'gfg': [7, 6, 3], 
             'is': [2, 10, 3], 
             'best': [19, 4]}
'''
# using loop + sorted
# d = dict()
# for key, val in test_dict.items():
#     d[key] = sorted(val)
# print(dict(sorted(d.items())))

#using dictionary comprehenion
'''
d = dict(sorted({key:sorted(val) for key, val in test_dict.items()}.items()))
print(d)
'''

#lambda dictionary comprehenion
# d = dict(sorted(test_dict.items(), key = lambda x: x[0]))
# for key, val in d.items():
#     d[key] = sorted(val)
# print(d)

#zip
'''
keys = list(test_dict.keys())
values = list(test_dict.values())
d = sorted(zip(keys, values), key=lambda x: x[0])
d = {k:sorted(v) for k, v in d}
print(d)
'''
#------------------------------------------------------------------------------------------------------
#Python sort dictionary by values summation

#test_dict = {'Gfg' : [6, 7, 4], 'is' : [4, 3, 2], 'best' : [7, 6, 5]} 

#sorted + dictionay comprehenion sum()

# d = {k: sum(v) for k, v in test_dict.items()}
# w = sorted(d.items(), key = lambda x: x[1])
# print(dict(w))

#map dictionary comprehenion + sorted + sum
'''
a = {i:sum(map(lambda x: x, test_dict[i])) for i in test_dict}
v = sorted(a.items(), key= lambda x: x[1])
print(v)
# '''
# #defaultdict
# from collections import defaultdict

# c = dict()
# for k, v in test_dict.items():
#     c[k]=sum(v)
# s = dict(sorted(c.items(), key= lambda x: x[1]))
# print(s)
#-----------------------------------------------------------------------------------------------------
#Python sort Dictionary list by key's value list index 12:45

# #sorted lambda funtion
# test_list = [{"Gfg" : [6, 7, 8], "is" : 9, "best" : 10}, 
#              {"Gfg" : [2, 0, 3], "is" : 11, "best" : 19},
#              {"Gfg" : [4, 6, 9], "is" : 16, "best" : 1}]

# k = "Gfg"
# inx = 2
# k2 = "best"
# s = sorted(test_list, key=lambda x: x[k][inx])
# print(s)

#
'''
res = sorted(sorted(test_list, key = lambda x: x[k2]), key = lambda x: x[k][inx])
print(res)
'''

#list comprehenion _ buildin sorted function

# res = [d for d in sorted(test_list, key = lambda x: x[k][inx])]
# print(res)

#heapq
'''
from heapq import nsmallest

a = nsmallest(len(test_list), test_list, key = lambda x: x[k][inx])
print(a)
'''

#----------------------------------------------------------------------------------------------------------------------------------------
#python sort nusted keys by values 3:35


# test_dict = {'Nikhil' : {'English' : 5, 'Maths' :  2, 'Science' : 14},
#              'Akash' : {'English' : 15, 'Maths' :  7, 'Science' : 2},
#              'Akshat' : {'English' : 5, 'Maths' :  50, 'Science' : 20}}

# sorted lambda
"""
d = {k:sorted(v.items(), key = lambda x: x[1]) for k, v in test_dict.items()}
print(d)
"""

# #itemgetter
# from operator import itemgetter

# s = {k:sorted(v.items(), key=itemgetter(1)) for k, v in test_dict.items()}
# print(s)

#-------------------------------------------------------------------------------------------------
#python scoring Matrix using dictionary
'''
test_list = [['gfg', 'is', 'best'], ['gfg', 'is', 'for', 'geeks']]
test_dict = {'gfg' : 5, 'is' : 10, 'best' : 13, 'for' : 2, 'geeks' : 15}
'''
l = list()
# for i in test_list:
#     s=0
#     for j in i:
#         if j in test_dict:
#             s+=test_dict[j]
#     l.append(s)
# print(l)

#using list comprehenion + sum()
'''

s = [sum(test_dict[j] if j in test_dict else 0 for j in i) for i in test_list]
print(s)
'''

#-------------------------------------------------------------------------------------------------------
#Pyhton factor frequency dictionary
'''
test_list = [2, 4, 6, 8, 3, 9, 12, 15, 16, 18]
res = list()
'''
# for i in range(1, max(test_list)):
#     res[i] = 0
#     for j in test_list:
#         if j %i ==0:
#             res[i]+=1
# print(res)

#loop + sum()   
'''
for i in range(1, max(test_list)):
    res[i]= sum(j%i==0 for j in test_list)
print(res)
'''

#ittertool.chain +Counterxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx///////////////////////////////xxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxx//////////////////////////xxxxxxxxx////////////////////////x//////////////xxxxxxxx
'''
from collections import Counter
from itertools import chain

res = {i:Counter(chain(*[[j for j in range(1, i+1) if key%j==0] for key in test_list]))[i] for i in range(1, max(test_list)+1)}
print(res)
'''
#/////////////////////////////////////////////////////////////xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/////////////////////////////
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx///////////////////////////////////////xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx//
#    012
#------------------------------------------------------------------------------------------------------
'''
a = "abc"
v = set()
for i in range(len(a)):
    for j in range(i, len(a)):
        v.add(a[i:j+1])
print(v)
d = set()

for i in range(len(a)):
    for j in range(i, len(a)):
        d.add(a[i:j+1])  # i=0-2 i=0 0-2 i=1 1-2                    a, ab, abc,  b, bc, c
print(len(d))

'''
#------------------------------------------------------------------------------------------------------
#Building a Unordered graph and find shotest path using dictionary in Python
from collections import defaultdict

edges = [
    ["A", "B"], ["A", "E"], 
    ["A", "C"], ["B", "D"],
    ["B", "E"], ["C", "F"],
    ["C", "G"], ["D", "E"]
    ]
# d = defaultdict(list)
# for i in edges:
#     d[i[0]].append(i[1])
#     d[i[1]].append(i[0])
# print(d)



# We can use stl container list as a double
# ended queue to store the cache keys, with
# the descending time of reference from front
# to back and a set container to check presence
# of a key. But to fetch the address of the key
# in the list using find(), it takes O(N) time.
# This can be optimized by storing a reference
# (iterator) to each key in a hash map.
class LRUCache:
	# store keys of cache
	def __init__(self, n):
		self.csize = n
		self.dq = []
		self.ma = {}


	# Refers key x with in the LRU cache
	def refer(self, x):
		
		# not present in cache
		if x not in self.ma.keys():
			# cache is full
			if len(self.dq) == self.csize:
				# delete least recently used element
				last = self.dq[-1]

				# Pops the last element
				ele = self.dq.pop();

				# Erase the last
				del self.ma[last]

		# present in cache
		else:
			del self.dq[self.ma[x]]

		# update reference
		self.dq.insert(0, x)
		self.ma[x] = 0;

	# Function to display contents of cache
	def display(self):

		# Iterate in the deque and print
		# all the elements in it
		print(self.dq)

# Driver Code
ca = LRUCache(4)

ca.refer(1)
ca.refer(2)
ca.refer(3)
ca.refer(1)
ca.refer(4)
ca.refer(5)
ca.display()
# This code is contributed by Satish Srinivas
