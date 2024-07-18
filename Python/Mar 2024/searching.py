# arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
# x = 110
# for i in range(len(arr)):
#     if arr[i] == x:
#         print(i)
# [print(i) for i in range(len(arr)) if arr[i]==x]

'''
def binary_search(arr, x, l, h):
    if h>=l:
        mid = (l+h)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr, x, l, mid-1)
        else:
            return binary_search(arr, x, mid+1, h)
    else:
        return -1
def bs(arr, x, l, h):
    
    while h>=l:
        mid = (l+h)//2
        if arr[mid]>x:
            h =mid-1
        elif arr[mid]<x:
            l = mid+1
        else:
            return mid
    return -1
def ff(arr, x):
    i = bisect.bisect_left(arr, x)
    if i != len(arr) and  arr[i]== x:
        return i
    return -1
arr = [2, 3, 4, 10, 40]
x = 1
result = binary_search(arr, x, 0, len(arr)-1)
if result != -1:
    print(f"{x} found at {result} index")
f = bs(arr, x, 0, len(arr)-1)
if f != -1:
    print(f"Element found at {f}")
else:
    print("Element not found")
import bisect'''

#-------------------------------------------------------------------------------------------------------------
#binary search

# def bins(arr,x, l, h):
    
#     mid = (l+h)//2
#     if arr[mid]==x:
#         return mid
#     elif arr[mid] > x:
#         return bins(arr, x, l, h-mid)
#     else:
#         return bins(arr, x, l+mid, h)

# def w(arr, x, l, h):
#     while True:
#         mid = (l+h)//2
#         if arr[mid]==x:
#             return mid
#         elif arr[mid]<x:
#             l = l+mid
#         else:
#             h = h-mid

# import bisect
# arr = [3, 4, 5, 6, 7, 8, 9]
# x=9
# i = bisect.bisect_left(arr, x)
# if x==arr[i]:
#     print(i)
# t = bins(arr, x, 0, len(arr)-1)
# a = w(arr, x, 0, len(arr)-1)
# print(t, a)
#---------------------------------------------------------------------------------------------------------------
#bobble sort
'''
arr = [-1, 45, 0, 11, -9]
for j in range(len(arr)):
    for i in range(0, len(arr)-j-1):
        if arr[i]>arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr)
'''
#---------------------------------------------------------------------------------------------------
#section sorting

# arr = [20, 12, 10, 15, 2]
# for i in range(len(arr)):
#     m = i
#     for j in range(i+1, len(arr)):
#         if arr[m]>arr[j]:
#             m = j
#     arr[i], arr[m] = arr[m], arr[i]
# print(arr)
#----------------------------------------------------------------------------------------------------
#insertion sorting
'''
def insertion_sorting(arr):
    for element in range(1, len(arr)):
        key = arr[element]
        pre = element-1
        while key<arr[pre] and pre>=0:
            arr[pre+1]=arr[pre]
            pre-=1
        arr[pre+1]=key
    return arr
arr = [9, 5, 1, 4, 3]
print(insertion_sorting(arr))'''
#-----------------------------------------------------------------------------------------------------
#Marge sort
# def mergesort(arr):
#     if len(arr)>1:
#         m = len(arr)//2
#         left = arr[:m]
#         right = arr[m:]
#         mergesort(left)
#         mergesort(right)
#         l = 0
#         r = 0
#         fb = 0
#         while l < len(left) and r < len(right):
#             if left[l]<right[r]:
#                 arr[fb] = left[l]
#                 l+=1
#             else:
#                 arr[fb]=right[r]
#                 r+=1
#             fb+=1
#         while l<len(left):
#             arr[fb]=left[l]
#             fb+=1
#             l+=1
#         while r<len(right):
#             arr[fb]=right[r]
#             fb+=1
#             r+=1
# arr = [6, 5, 12, 10, 9, 1, 1, -2]
# mergesort(arr)
# print(arr)

#------------------------------------------------------------------------------------------------------------
# MergeSort in Python


'''
def mergeSort(a):
    if len(a)>1:
        m = len(a)//2
        left = a[:m]
        right = a[m:]
        mergeSort(left)
        mergeSort(right)
        i=j=k=0
        while len(left)>i and len(right)>j:
            if left[i]<right[j]:
                a[k]=left[i]
                i+=1
            else:
                a[k]=right[j]
                j+=1
            k+=1
        while len(left)>i:
            a[k]=left[i]
            i+=1
            k+=1
        while len(right)>j:
            a[k]=right[j]
            j+=1
            k+=1
    
            
        

# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1, 1, -2]

    mergeSort(array)

    print("Sorted array is: ",array)
a = [1,5,3,3,3,2,7,8,9,0]
e = 0
while len(a)>e:
    print(a[e])
    e+=1'''
#----------------------------------------------------------------------------------------------------------
#counting sort
# def counting_sort(arr):
#     max_value = max(arr)
#     count = [0] * (max_value + 1)
#     output = [0] * len(arr)
#     print(count, output)

#     # Step 1: Counting Phase
#     for num in arr:
#         count[num] += 1
#     print(count)

#     # Step 2: Cumulative Counting
#     for i in range(1, len(count)):
#         count[i] += count[i - 1]
#     print(count)

#     # Step 3: Build the Output Array
#     for num in arr:
#         output[count[num] - 1] = num
#         count[num] -= 1
#     print(output)
#     return output

# # Test the Counting Sort function
# arr = [4, 2, 2, 80, 3, 3, 1]
# #sorted_arr = counting_sort(arr)
# print("Sorted array:")

# count = [0]*(max(arr)+1)
# print(count)
# output = [0]*len(arr)
# for i in arr:
#     count[i]+=1
# for i in range(1, len(count)):
#     count[i]+=count[i-1]
# for i in arr:
#     output[count[i]-1]=i
#     count[i]-= 1
# print(output)
#-----------------------------------------------------------------------------------------------------------
#redix sort
'''
def redixsort(arr):
    m = 10
    d = 1
    t =0
    while len(str(max(arr)))>t:
        temp = [[], [], [], [], [], [], [], [], [], []]
        for i in arr:
            k = i%m//d
            temp[k].append(i)
        arr = []
        for i in temp:
            for j in i:
                arr.append(j)
        m*=10
        d*=10
        t+=1
    print(arr)
redixsort(arr)
'''
#--------------------------------------------------------------------------------------------------
## Bucket Sort in Python


# def bucketSort(arr):
#     bucket = [[] for i in range(len(arr))]
#     # for i in arr:
#     #     b = int(i*10)
#     #     bucket[b].append(i)
#     [bucket[int(i*10)].append(i) for i in arr]
#     for i in range(len(arr)):
#         bucket[i] = sorted(bucket[i])
#     print(bucket)
#     k = 0
#     for i in range(len(arr)):
#         for j in range(len(bucket[i])):
#             arr[k] = bucket[i][j]
#             k+=1
#     return arr

# array = [.42, .32, .33, .52, .37, .47, .51]
# #array = [121, 432, 564, 23, 1, 45, 788]
# print("Sorted Array in descending order is")
# print(bucketSort(array))
#-------------------------------------------------------------------------------------------------
# Heap Sort in python


# Heap Sort in python
'''

def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build max heap
    for i in range((n//2)-1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify root element
        heapify(arr, i, 0)


arr = [1, 12, 9, 5, 6, 10]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d " % arr[i], end='')

'''
#---------------------------------------------------------------------------------------------------------
#shell sorting
# def shellSort(arr, n):
#     s = n//2
#     while s>0:
#         for i in range(s, n):
#             temp = arr[i]
#             que = i
#             while que>=s and temp  <arr[que - s]:
#                 arr[que] = arr[que- s]
#                 que-=s
#             arr[que] = temp
#         s//=2
# data = [9, 8, 3, 7, 5, 6, 4, 1]
# shellSort(data, len(data))
# print(data)
#------------------------------------------------------------------------------------------------
#liner search
'''
data = [9, 8, 3, 7, 5, 6, 4, 1]
x = 6
for i in data:
    if x==i:
        print(f"{x} in at index {i-1}")'''
#-----------------------------------------------------------------------------------------------------

#bubble sort
def bubbleSort(data):
    for i in range(len(data)):

        for j in range(len(data)-1-i):
            if data[j]>data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
data = [9, 8, 3, 7, 5, 6, 4, 1]
bubbleSort(data)
print(data)
#-----------------------------------------------------------------------------------------------------------------------
#selection sort
'''def selectionSort(darta):
    for i in range(len(data)):
        mine = i 
        for j in range(i+1, len(data)):
            if data[mine]>data[j]:
                mine=j
        data[i], data[mine]= data[mine], data[i]
data = [9, 8, 3, 7, 5, 6, 4, 1]
selectionSort(data)
print(data)
'''
#-----------------------------------------------------------------------------------------------------
#insertion
# def insertion(arr):
#     for i in range(1, len(arr)):
#         temp = arr[i]
#         j = i-1
#         while j>=0 and temp <arr[j]:
#             arr[j+1] = arr[j]
#             j-=1
#         arr[j+1] = temp
# arr = [9, 8, 3, 7, 5, 6, 4, 1]
# insertion(arr)
# print(arr)
#---------------------------------------------------------------------------------------------------------------
#merge sort
'''def mergeSort(data):
    if 1<len(data):

        mid = len(data)//2
        left = data[:mid]
        right = data[mid:]
        mergeSort(left)
        mergeSort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                data[k] =left[i]
                i+=1
            else:
                data[k] = right[j]
                j+=1
            k+=1
        while i<len(left):
            data[k] =  left[i]
            i+=1
            k+=1
        while j<len(right):
            data[k] = right[j]
            j+=1
            k+=1
        
data = [9, 8, 3, 7, 5, 6, 4, 1]
mergeSort(data)
print(data)'''
#---------------------------------------------------------------------------------------------------------
#Quick sort
# def quickSort(data):
#     if len(data)<=1:
#         return data
#     else:
#         pivot = data[0]
#         left = [i for i in data[1:] if i<pivot]
#         right = [i for i in data[1:] if i>=pivot]
#         return quickSort(left) + [pivot] + quickSort(right)
# data = [9, 8, 3, 7, 5, 6, 4, 1]
# quickSort(data)
# print(quickSort(data))
#------------------------------------------------------------------------------------------------------
#Counting sort
"""def countingSort(arr):
    m = max(arr)
    count = [0]*(m+1)
    output = [0]*len(arr)
    for i in arr:
        count[i]+=1
    for i in range(1, len(count)):
        count[i]+=count[i-1]
    for i in arr:
        output[count[i]-1] = i
        count[i]-=1
    print(output)
data = [9, 8, 3, 7, 5, 6, 4, 1]

c = [0]*(max(data)+1)
o = [0]*(len(data))
for i in data:
    c[i]+=1
for i in range(1, len(c)):
    c[i] += c[i-1]
for i in data:
    o[c[i]-1] = i
print(o)"""
#-----------------------------------------------------------------------------------------------------
#redix sort
# def redixSort(arr):
#     d = 1
#     m = 10
#     c = 0
#     while c<len(str(max(arr))):

#         temp = [[], [], [], [], [], [], [], [], [], []]
#         for i in arr:
#             temp[i%m//d].append(i)
#         arr= []
#         for i in temp:
#             for j in i:
#                 arr.append(j)
#         print(arr)
#         c+=1
# data = [9, 8, 3, 7, 5, 6, 4, 1, 81]
# redixSort(data)
#-----------------------------------------------------------------------------------------------------
#bucket sort
'''def bucketSort(arr):
    b = [[] for i in range(len(arr))]
    for i in arr:
        b[int(i*10)].append(i)
    for i in range(len(b)):
        b[i].sort()
    t = 0
    for i in range(len(arr)):
        for j in range(len(b[i])):
            arr[t] = b[i][j]
            t+=1
    print(arr)
        
array = [.42, .32, .33, .52, .37, .47, .51]
bucketSort(array)'''
#------------------------------------------------------------------------------------------------------------------------------------------
#max heap sort
# def heapify(arr, n, i):
#     large = i
#     l = 2*i+1
#     r = 2*i+2
#     if l<n and arr[i] < arr[l]:
#         large = l
#     if r<n and arr[large] < arr[r]:
#         large = r
#     if large != i:
#         arr[i], arr[large] = arr[large], arr[i]
#         heapify(arr, n, large)
# def heapsort(arr):
#     n = len(arr)
#     for i in range(n//2, -1, -1):
#         heapify(arr, n, i)
#     for i in range(n-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)
# arr = [1, 12, 9, 5, 6, 10]
# heapsort(arr)
# n = len(arr)
# print("Sorted array is")
# for i in range(n):
#     print("%d " % arr[i], end='')
#---------------------------------------------------------------------------------------------------
#shellsort
'''def shellSort(arr, n):
    intervel = n//2
    while intervel>0:
        for i in range(intervel, n):
            temp = arr[i]
            j = i
            while j>=intervel and temp<arr[j- intervel]:
                arr[j] = arr[j - intervel]
                j-=intervel
            arr[j] = temp 
        intervel//=2
data = [9, 8, 3, 7, 5, 6, 4, 1]
size = len(data)
shellSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)'''
#-------------------------------------------------------------------------------------------------------
#LinerSerach
# array = [2, 4, 0, 1, 9]
# x = 1
# for i in range(len(array)):
#     if x==array[i]:
#         print("yes",i, "it s index ") 
#-------------------------------------------------------------------------------------------------------
#binary search
'''
def binarySearch(arr, x, l, h):
    if l<h:
        mid = l+(h-l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid]>x:
            return binarySearch(arr, x, l, mid-1)
        else:
            return binarySearch(arr, x, 1+mid, h)
    else:
        return -1
array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
'''
#---------------------------------------------------------------------------------------------------------
