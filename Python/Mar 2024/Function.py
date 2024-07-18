#___________________________________   Mar 07    ________________________________________________________________


# import inspect
# import collections
# print(inspect.signature(collections.Counter))

'''
def fun (a, b):
    return a**b
import inspect
print(inspect.signature(fun))

'''

# import inspect
# print(inspect.signature(len))

'''
import inspect
import collections
print(inspect.getfullargspec(collections.Counter))'''

#____________________________________________________________________________________________________
#How to print multiple arguments in Python
# def func(a, b):
#     return "it  is {0} and {1}".format(a, b)
# print(func("ajith", 2))

'''
def fuc(*arg):
    for i in arg:
        print(i, end="")
fuc("ajith", " is ", "now ", "learning ", "python ", 3.2)'''

# def func(**kwargs):
#     for k, v in kwargs.items():
#         print(k, v)

# func(name="geeks", n="-25")

#______________________________________________________________________________________________________________
# Python progeam to find the power of a number using

# def func(a, b):
#     if b==0:
#         return 1
#     return a*func(a, b-1) #2 2 2
# print(func(2, 3))


# # Creating Test DataSets using sklearn.datasets.make_blobs
# from sklearn.datasets import make_blobs
# from matplotlib import pyplot as plt 
# from matplotlib import style

# style.use("fivethirtyeight")

# X, y = make_blobs(n_samples = 100, centers = 3, 
# 			cluster_std = 1, n_features = 2)

# plt.scatter(X[:, 0], X[:, 1], s = 40, color = 'g')
# plt.xlabel("X")
# plt.ylabel("Y")

# plt.show()
# plt.clf()
#___________________________________________________________________________________________________________________
nums = [2,7,11,15]
target = 9
a = [[i, j] for i in range(len(nums)) for j in range(len(nums)) if nums[i]+nums[j]]
print(a[0])