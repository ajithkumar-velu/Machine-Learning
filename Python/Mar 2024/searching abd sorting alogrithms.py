# def insertion_sorting(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i-1
#         while j>=0 and arr[j]>key:
#             arr[j+1] = arr[j]
#             j-=1
#         arr[j+1] = key

# arr = [12, 11, 13, 5, 6]
# s = insertion_sorting(arr)
# for i in range(len(arr)):
#     print("%d" % arr[i], end= " ")


#quick sorting

''' 
def quick_sort(arr):    
    if len(arr)<=1:
        return(arr)
    else:
        pivot = arr[0]
        left= [i for i in arr[1:] if pivot>i]
        right = [i for i in arr[1:] if pivot <= i]
        return quick_sort(left) + [pivot] + quick_sort(right)
arr = [-2, 1, 1, 4, 7, 9, 10]

a = quick_sort(arr)
print(a)

'''
#selsection sort

# def selection_sort(array, size):
#     for i in range(size):
#         m = i
#         for j in range(i+1, size):
#             if array[m]>array[j]:
#                 m = j
#         array[i], array[m] = array[m], array[i]
# arr = [64, 25, 12, 22, 11]
# size = len(arr)
# selection_sort(arr, size)
# print(arr)


#___________________________________________________________________________________________________________
#stooge sort

'''
def stooge_sort(arr, l, h):
    if l>=h:
        return
    if arr[l]>arr[h]:
        t = arr[l]
        arr[l]= arr[h]
        arr[h] = t
    if h-l+1>2:
        t = (int)((h-l+1)/3)
        stooge_sort(arr, l, (h-t))
        stooge_sort(arr, (l+t), h)
        stooge_sort(arr, l, (h-t))
arr = [2, 4, 5, 3, 1]
n = len(arr)
stooge_sort(arr, 0, n-1)

for i in range(len(arr)):
    print(arr[i], end= " ")'''
#____________________________________________________________________________________________________
#insertion sort

# def insertion_sort(arr, n):
#     if n<=1:
#         return
    
# arr = [12, 11, 13, 5, 6]
# insertion_sort(arr, len(arr))
#--------------------------------------------------------------------------------------------
#bisect
'''
import bisect
li = [1, 3, 4, 4, 4, 6, 7]
print(bisect.bisect(li, 3))
print(bisect.bisect(li, 4, 0, 4))
print(bisect.bisect_right(li, 3))
print(bisect.bisect(li, 0))'''

#_________________________________________________________________________________________________
#shellsort

# def shell_sort(arr):
#     n = len(arr)
#     gap = n//2
#     while 0<gap:
#         for i in range(gap, n):
#             temp = arr[i]
#             j = i
#             while j>=gap and temp < arr[j - gap]:
#                 arr[j] = arr[j- gap]
#                 j -= gap
#             arr[j] = temp
#         gap//=2
# # Test the function
# arr = [12, 34, 54, 2, 3]
# print("Original Array:", arr)
# shell_sort(arr)
# print("Sorted Array:", arr)

#_______________________________________________________________________________________________________
#Bubblesort

"""
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]
a = bubbleSort(arr)
print(arr)"""
#_______________________________________________________________________________________________________
#section sort
# def sectionSort(arr):
#     for i in range(len(arr)):
#         m = i
#         for j in range(i+1, len(arr)):
#             if arr[m]>arr[j]:
#                 m = j
#         arr[m], arr[i] = arr[i], arr[m]
# arr = [64, 25, 12, 22, 11]
# a = sectionSort(arr)
# print(arr)

#_________________________________________________________________________________________________
#QuickSort
'''
def QuickSort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot = arr[0]
        left = [i for i in arr[1:] if pivot > i]
        right = [i for i in arr[1:] if pivot <= i]
        return QuickSort(left) + [pivot] + QuickSort(right)

arr = [64, 25, 12, 22, 11]
p = QuickSort(arr)
print(p)'''

#--_____---------------------____---_______-_____----------------------------------------------
#Redix sorting

# arr = [170, 45, 75, 90, 802, 24, 2, 66]
# d = 1
# m = 10
# condition =True
# while condition:
#     condition = False
#     temp = [[], [], [], [], [], [], [], [], [], []]
#     for i in arr:
#         p = i%m//d
#         temp[p].append(i)
#         if not condition and p>0:
#             condition = True
#     arr = []
#     for i in temp:
#         for j in i:
#             arr.append(j)
#     d*=10
#     m*=10
# print(arr)

#_________________________________________________________________________________________
#Counting sorting
'''
from functools import reduce
string = "geeksforgeeks"
print(reduce(lambda x, y: x+y, sorted(string)))'''
#----------------------------------------------------------------------------------------------------
#heap (max)
# def heapify(arr, n, i):
#     large = i
#     l = (2*i)+1
#     r = (2*i)+2
#     if l<n and arr[l]>arr[large]:
#         large = l
#     if r<n and arr[r]>arr[large]:
#         large = r
#     if large!=i:
#         arr[large], arr[i] = arr[i], arr[large]
#         heapify(arr, n, large)
# def heapSort(arr):
#     n = len(arr)
#     for i in range((n//2)-1, -1, -1):
#         heapify(arr, n, i)
#     for i in range(n-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)
# arr = [1, 12, 9, 5, 6, 10]
# heapSort(arr)
# n = len(arr)
# print("Sorted array is")
# for i in range(n):
#     print("%d " % arr[i], end='')   
#---------------------------------------------------------------------------------------------------
