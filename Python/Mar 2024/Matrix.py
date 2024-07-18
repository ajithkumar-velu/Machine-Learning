#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      Mar 7       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
#Adding subtracting in matrix in python

 
# importing numpy as np
# import numpy as np
 
 
# # creating first matrix
# A = np.array([[1, 2], [3, 4]])
 
# # creating second matrix
# B = np.array([[4, 5], [6, 7]])

# print(A+B)
'''
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[4, 5], [6, 7]]
r = [[0, 0], [0, 0]]
for i in range(len(A)):
    for j in range(len(matrix1[i])):
        print(matrix1[i][j]-matrix2[i][j], end=" ")
    print()

'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@222
#Row wise element adding in tuple matrix
# test_list = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]
# t = [6, 7, 8]

# r = [[i+ (t[k],) for i in v] for k, v in enumerate(test_list)]
# print(r)

# loop
"""
a =[]
for k, v in enumerate(test_list):
    a.append(list(map(lambda x: x+(t[k],) , v)))
print(a)

"""
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Python Matrix product
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

# a = [j for i in test_list for j in i]
# d = 1
# for i in a:
#     d*=i
# print(d)

#using chain

'''
from itertools import chain

c = chain(*test_list)
f = 1
for i in c:
    f*=i
print(f)
'''

# #extend()
# f =1
# k = []
# d = [k.extend(i) for i in test_list]
# for i in k:
#     f*=i

# print(f)

#reduce operator
'''
from functools import reduce
from operator import mul
s = []
d = [s.extend(i) for i in test_list]
d = reduce(lambda x, y: mul(x,y), s, 1)
print(d)'''

# #loop
# r =1
# for i in test_list:
#     for j in i:
#         r*=j
# print(r)
#---------------------------------------------------------------------------------------------------------
#Python | Kth colunm of the matrix
'''
test_list = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]

k =2
'''
# #using list comprehenion
# p = [test_list[i][2] for i in range(len(test_list))]
# print(p)

#zip()
'''
l =[]
for i in zip(*test_list):
    l.append(i)
print(l[k])

print(list(zip(*test_list))[k])'''

# #numpy
# import numpy as np
# a = np.array(test_list)
# print(a[:,k])

#loop
'''
r = []
for i in range(len(test_list)):
    r.append(test_list[i][k])
print(r)

'''

#map()
# a = list(map(lambda x:x[k] , test_list))
# print(a)

#-----------------------------------------------------------------------------------------------------
#Python | Type casting whole list and Matrix
test_matrix = [[5, 6, 8], [8, 5, 3], [9, 10, 3]]

'''
test_list = [1, 4, 9, 10, 19]
print(list(map(str, test_list)))
l = [list(map(str, i)) for i in test_matrix]
d = list(map(lambda x: list(map(str, x)), test_matrix))
print(l)
print(d)'''

import numpy as np
p = np.array(test_matrix, dtype=str)
print(p)