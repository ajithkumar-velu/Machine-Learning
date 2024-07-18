# pi = 3.14159265359
# print(pi*(4**2))
# print(2*pi*4)  #2pir
'''
import math
class area:
    def __init__(self, r):
        self.r = r

    def areaOfCircle(self):
        return (self.r**2)*math.pi
    def perimeter(self):
        return 2*self.r*math.pi
r = float(input("Enter the rt value: "))

a = area(r)
b = a.areaOfCircle()
c = a.perimeter()
print(f"{r} circle value is {b} and perimeter value ia {c}")
'''
#_---------------------------------------------------------------------------------------------------------
#Write a python program to create a person class. include attributes like name, country and date of birth.implement to detemine the person's age

# from datetime import date
# class person:
#     def __init__(self, Name, Country, DateOfBirth):
#         self.Name= Name
#         self.Country = Country
#         self.DateOfBirth = DateOfBirth
#     def calAge(self):
#         today = date.today()
#         age = today.year - (self.DateOfBirth).year - ((today.month, today.day) < ((self.DateOfBirth).month, (self.DateOfBirth).day))
#         return age
# name = input("Enter your name: ")
# country = input(f"Hi {name} what's your country: ")
# age = map(int, input(f"{name} enter your date of birth like this format 'yyyy mm dd': ").split())

# ajith = person(name, country, date(*age))
# print(f"{name} your are {ajith.calAge()} years old")
#------------------------------------------------------------------------------------------------------------

#Write a python program to create a calcuoator class. Include method for basic arithmatic operations
'''
import operator
class cal:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def addition(self):
        return operator.add(self.num1, self.num2)
    def subtraction(self):
        return operator.sub(self.num1, self.num2)
    def multiply(self):
        return operator.mul(self.num1, self.num2)
    def divion(self):
        if self.num1==0 or self.num2 == 0:
            print("Zero divion Error!")
        else:
            print(f"The divition of {self.num1} and {self.num2} is {operator.floordiv(self.num1, self.num2)}")
a = int(input())
b = int(input())
sum = cal(a, b)
print(f"The addition of {a} and {b} is {sum.addition()}")
print(f"The subtraction of {a} and {b} is {sum.subtraction()}")
print(f"The multiply of {a} and {b} is {sum.multiply()}")
sum.divion()'''
#-----0----------------------------------------------------------------------------------------------
#write a python program to create a class that represents a shape. include methods to calculate its 
#area and primeters implements subclass for difference shapes like circle, triangle and square
# import math
# class shape:
#     def cal_area(self):
#         pass
#     def cal_perimeter(self):
#         pass
# class circle(shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def cal_area(self):
#         return math.pi*(self.radius**2)
#     def cal_perimeter(self):
#         return 2*math.pi*self.radius
# class triangle(shape):
#     def __init__(self, b, h, s1, s2, s3):
#         self.b = b
#         self.h = h
#         self.s1 = s1
#         self.s2 = s2
#         self.s3= s3
#     def cal_area(self):
#         return 1/2*self.b*self.h
#     def cal_perimeter(self):
#         return self.s1+self.s2+self.s3

# class rectangle(shape):
#     def __init__(self, l, w):
#         self.l = l
#         self.w = w
#     def cal_area(self):
#         return self.l * self.w
#     def cal_perimeter(self):
#         return 2*(self.l + self.w)

# radius = int(input("Enter the redius value R: "))
# r = circle(radius)
# print(f"Radius of circle: {radius}\nCircle area: {r.cal_area()}\nCircle of perimeter is: {r.cal_perimeter()}\n\n")

# b, h, s1, s2, s3 = map(int, input("Enter the b and h values:").split())
# tri = triangle(b, h, s1, s2, s3)
# print(f"Triangle of circle is b = {b} and h = {h}\nside1 = {s1}\tside2 = {s2}\tside3 = {s3}\nArea of Triangle is: {tri.cal_area()}\nArea of perimeter is:{tri.cal_perimeter()}")


# l = int(input("Enter the value of l: "))
# w = int(input("Enter the value of w: "))
# rect = rectangle(l, w)
# print(f"\n\nl = {l}\tw = {w}\nArea of circle is: {rect.cal_area()}\narea of perimeter: {rect.cal_perimeter()}")
#---------------------------------------------------------------------------------------------------------
#oops inhertance
'''class Animal:
    name = ''
    def eat(self):
        print("I can eat")
class Dog(Animal):
    def display(self):
        print(f"My name is {self.name}")



labrador = Dog()
labrador.name = "Rahul"
labrador.eat()
labrador.display()'''#
#---------------------------------------------------------------------------------------------------------
#oops overloading
# class Animal:
#     def eat(self):
#         print("I can eat")
# class Dog(Animal):
#     def eat(self):
#         print("I like to eat bones")
# labrador = Dog()
# labrador.eat()

#how to access the superclass during the overloading

# class Animal:
#     def eat(self, name):
#         print(f"I can eat")
# class Dog(Animal):
#     def eat(self):
#         print("I like to eat bones")
#         super().eat()
# labrador = Dog()
# labrador.eat()

#Encapsulation
# class computer:
#     def __init__(self):
#         self.__maxprice=20
#         self.__age =22
#     def shell(self):
#         print(f"Selling price is", self.__maxprice)
#     def vayasu(self):
#         print(f"age = ", self.__age)
#     def setMaxPrice(self, price, val):
#         self.__maxprice = price
#         self.__age = val
    
# c =computer()
# c.vayasu()
# c.setMaxPrice(100, 23)
# c.vayasu()

'''class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
'''

#--------------------------------------------------------------------------------------------------------------\
#binary search tree
'''class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right =None
   
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def add(self, data):
        if not self.root:
            self.root = BSTNode(data)
            return
        self.recursiveAdd(data, self.root)
    def recursiveAdd(self, data, node):
        if data < node.data:
            if not node.left:
                node.left = BSTNode(data)
            else:
                self.recursiveAdd(data, node.left)
        elif data > node.data:
            if not node.right:
                node.right = BSTNode(data)
            else:
                self.recursiveAdd(data, node.right)
    def display(self):
        result = []
        self.inorderTraversal(self.root, result)
        print(result)
    def inorderTraversal(self, node, result):
        if not node:
            return None
        else:
            self.inorderTraversal(node.left, result)
            result.append(node.data)
            self.inorderTraversal(node.right, result)'''
# class btsNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#     def add(self, val):
#         if not self.root:
#             self.root = btsNode(val)
#             return
#         self.recursiveAdd(val, self.root)
#     def recursiveAdd(self, val, node):
#         if val < node.key:
#             if not node.left:
#                 node.left = btsNode(val)
#             else:
#                 self.recursiveAdd(val, node.left)
#         elif val > node.key:
#             if not node.right:
#                 node.right = btsNode(val)
#             else:
#                 self.recursiveAdd(val, node.right)
#     def display(self):
#         result = []
#         self.inorderTraversal(self.root, result)
#         print(result)
#     def inorderTraversal(self, node, result):
#         if not node:
#             return None
#         else:
#             self.inorderTraversal(node.left, result)
#             result.append(node.key)
#             self.inorderTraversal(node.right,result)
#     def searching(self, val):
#         self.ss(self.root, val)
#     def ss(self, node, val):
#         if node.key == val:
#             print(f"{node.key} it is found")
#         else:
#             if val < node.key:
#                 self.ss(node.left, val)
#             elif val > node.key:
#                 self.ss(node.right, val)
# bts = BinarySearchTree()
# bts.add(45)
# bts.add(10)
# bts.add(50)
# bts.add(9)
# bts.add(11)
# bts.add(46)
# bts.add(51)
# bts.display()
# bts.searching(46)
# #45, 10, 50, 9, 11, 46, 51
#----------------------------------------------------------------------------------------------------------
#stack using oops
'''class stack:
    def __init__(self):
        self.bucket = []
    def insert(self, val):
        print(f"Stack {val} value inserted")
        self.bucket.append(str(val))
    def display(self):
        print(f"Stack displaying")
        print(self.bucket)
    def pop(self):
        if len(self.bucket) == 0:
            print("Stack is Emtey")
        else:
            print(f"Stack {self.bucket[-1]} value Poped")
            self.bucket.pop()
    def size(self):
        print(f"Stack size is: {len(self.bucket)}")
stack1 = stack()
stack1.insert(7)
stack1.insert(4)
stack1.insert(8)
stack1.pop()
stack1.insert(97)
stack1.insert(23)
stack1.insert(836)
stack1.display()
stack1.size()'''
#----------------------------------------------------------------------------------------------------------
#Linked List
# Linked list implementation in Python


# class Node:
#     # Creating a node
#     def __init__(self, item):
#         self.item = item
#         self.next = None


# class LinkedList:

#     def __init__(self):
#         self.head = None



# linked_list = LinkedList()
# # Assign item values
# linked_list.head = Node(1)
# second = Node(2)
# third = Node(3)
# # Connect nodes
# linked_list.head.next = second
# second.next = third
# # Print the linked list item
# while linked_list.head != None:
#     print(linked_list.head.item, end=" ")
#     linked_list.head = linked_list.head.next
#-------------------------------------------------------------------------------------------------------
#linked list
'''class node:
    def __init__(self, item):
        self.item = item
        self.pointer = None
class LinkedList:
    def __init__(self):
        self.head = None
l = LinkedList()
l.head = node(1)
sec = node(2)
trid = node(3)
l.head.pointer = sec
sec.pointer = trid
while l.head != None:
    print(l.head.item, end = " ")
    l.head = l.head.pointer'''
#-------------------------------------------------------------------------------------------------------
#Linkedlist
'''class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
        else:
            cur = self.head
            while cur.pointer:
                cur = cur.pointer
            cur.pointer = newnode
    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end = " ")
            cur = cur.pointer
        print()
    def remove(self, data):
        if self.head is not None:
            if self.head.data == data:
                self.head = self.head.pointer
            else:
                cur = self.head
                while cur.pointer is not None and cur.pointer.data != data:
                    cur = cur.pointer
                if cur.pointer is not None:
                    cur.pointer = cur.pointer.pointer
                else:
                    print(f"{data} is not found in Linkelist")
        else:
            print(f"LinkedList is Empty")
link = LinkedList()
link.add(34)
link.add(4)
link.add(524)
link.add(14)
link.display()
link.remove(4)
link.display()
link.add(98)
link.add(4)'''

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def add(self, val):
#         if self.head is None:
#             self.head = Node(val)
#         else:
#             temp = self.head
#             while temp.next is not None:
#                 temp = temp.next
#             temp.next =  Node(val)
#     def display(self):
#         if self.head is None:
#             print("Linkedlist is empty")
#         else:
#             cur = self.head
#             while cur is not None:
#                 print(cur.data, end = " -->")
#                 cur = cur.next
#             print("None")
#     def remove(self, val):
#         if self.head is not None:
#             if self.head.data == val:
#                 self.head = self.head.next
#             else:
#                 cur = self.head
#                 while cur.next is not None and cur.next.data != val:
#                     cur = cur.next
#                 if cur.next is not None:
#                     cur.next = cur.next.next
#                 else:
#                     print(f"{val} is not found")
#         else:
#             print(f"stack is Empty")
        
# l = LinkedList()
# l.add(1)
# l.add(86)
# l.add(6)
# l.add(54)
# l.add(2)
# l.display()
# l.remove(2)
# l.display()
#----------------------------------------------------------------------------------------------------------------------
#Write a python program to create a class represents a shopping cart. Including method for adding and removing items. and calculate total price.
 
'''class shopingcart:
    def __init__(self):
        self.dict = dict()
    def additem(self, name, price):
        self.dict[name] = price
    def removeItem(self, name):
        print("Updated the Cart")
        self.dict.pop(name)
    def bill(self):
        print(f"Product         price\n---------------------------------------")
        for key, val in self.dict.items():
            #print(f"{key}       {val}")
            #print("{:<15} {:.2f}".format(key, val))
            print(f"{key:15} ${val:.2f}")
        print("---------------------------------------")
        print("{:<15} ${:.2f}".format("Total", sum(self.dict.values())))
customer1 = shopingcart()
customer1.additem("apple", 200)
customer1.additem("pinapple", 100)
customer1.additem("stoberi", 150)
customer1.additem("banana",110)
customer1.bill()
customer1.removeItem("stoberi")
customer1.bill()'''
#---------------------------------------------------------------------------------------------------------
#Write a Python program to create a class representing a stacl data structure. Including method for pusing, Poping and Displaying
'''class Stack:
    def __init__(self):
        self.list = []
    def push(self, data):
        self.list.append(data)
    def pop(self):
        if len(self.list) >0:
            print(f"Poped item: {self.list[-1]}")
            self.list.pop()
        else:
            print(f"Stack is Empty")
    def display(self):
        print(f"Stack itmes: {self.list}")
s1 = Stack()
s1.push(1)
s1.push(7)
s1.push(2)
s1.push(8)
s1.display()
s1.pop()
s1.display()'''
#-------------------------------------------------------------------------------------------------------------
#Write a puthon program to create a class representing a queue data structure. including Enqueueing and Dequeueing
'''class queue:
    def __init__(self):
        self.list = []
    def enqueueing(self, data):
        self.list.append(data)
    def dequeueing(self):
        if len(self.list)>0:
            print(f"dequeueed: {self.list[0]}")
            self.list.remove(self.list[0])
        else:
            print("Queue is Empty")
    def display(self):
        if len(self.list)>0:
            print(f"Queue is: {self.list}")
        else:
            print("Queue is Empty")
que = queue()
que.enqueueing(2)
que.enqueueing(1)
que.enqueueing(54)
que.enqueueing(76)
que.enqueueing(2)
que.enqueueing(82)
que.display()
que.dequeueing()'''
#--------------------------------------------------------------------------------------------------------------------------
#Write a python program to create a class representing a Bank. Incluing method for manageing customer A/C and trancactions
'''class Bank:
    def __init__(self):
        self.dict = dict()
    def newAc(self, ac, amount):
        if ac not in self.dict:
            self.dict[ac] =amount
            print(f"New A/c No.: {ac} Deposited Amount: {amount}\nAccount created successfully!")
        else:
            print("Account number already Exit!")
    def deposit(self, ac, amount):
        if ac in self.dict:
            self.dict[ac]+=amount
            print(f"Deposited ${amount} to A/c No. {ac}")
            print(f"Deposit successfully!")
        else:
            print("Account number does not Exit!")
    def withdraw(self, ac, amount):
        if ac in self.dict:
            print(f"Withdraw $.{amount} from A/c no:{ac}")
            if self.dict[ac]>=amount:
                self.dict[ac]-=amount
                print("Withdraw successfully!")
            else:
                print("Insufficient amount!")
        else:
            print(f"Account number does not Exit!")
    def balance(self, ac):
        if ac in self.dict:
            print(f"A/c No. {ac}\nAccount balance: {self.dict[ac]}")
        else:
            print(f"A/c number does not exit!")
person1 = Bank()
person1.newAc("SB-123", 1000)
person1.newAc("SB-124", 1500)
print()
person1.deposit("SB-123", 600)
person1.withdraw("SB-124", 350)
print()
person1.balance("SB-123")
person1.balance("SB-124")
print()
person1.withdraw("SB-124", 1200)
print()
person1.balance("SB-134")'''

#-----------------------------------------------------------------------------------------------------------------
#Binary search Tree
'''class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def add(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        self.addrecursive(data, self.root)
    def addrecursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.addrecursive(data, node.left)
        elif data> node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.addrecursive(data, node.right)
    def inordersearch(self, node, result):
        if node is None:
            return None
        else:
            self.inordersearch(node.left, result)
            result.append(node.data)
            self.inordersearch(node.right, result)
    def re(self):
        result = []
        self.inordersearch(self.root, result)
        print(result)
    def searching(self, val):
        self.ss(self.root, val)
    def ss(self, node, val):
        if node.data == val:
            print(f"{val} is found")
        else:
            if node.data > val:
                self.ss(node.left, val)
            elif node.data < val:
                self.ss(node.right, val)
l = BinarySearchTree()
l.add(45)
l.add(10)
l.add(50)
l.add(9)
l.add(11)
l.add(46)
l.add(51)
l.re()
l.searching(9)'''

#--------------------------------------------------------------------------------------------------------------
#LinkedList
'''class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None
class Linkedlost:
    def __init__(self):
        self.head = None
    def add(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            cur = self.head
            while cur.pointer is not None:
                cur = cur.pointer
            cur.pointer = newnode
    def print(self):
        if self.head is None:
            print(f"Linkedlist is Empty")
        else:
            cur = self.head 
            while cur is not None:
                print(cur.data, end = " ")
                cur = cur.pointer
        print()
    def remove(self, data):
        if self.head is not None:
            if self.head.data == data:
                self.head = self.head.pointer
            else:
                cur = self.head
                while cur.pointer is not None and cur.pointer.data !=data:
                    cur = cur.pointer
                cur.pointer = cur.pointer.pointer
        else:
            print(f"Element not found")
l = Linkedlost()
l.add(1)
l.add(6)
l.add(4)
l.add(76)
l.add(34)
l.add(8)
l.print()
l.remove(76)
l.print()'''
#------------------------------------------------------------------------------------------------------
#Write a python program to create a single linked list, Append some items and iterate throught the list

'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def insert(self, data):
        node =Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count+=1
    def iterate(self):
        node = self.head
        while node:
            yield node.data
            node=node.next
l = LinkedList()
l.insert("ajith")
l.insert("arun")
l.insert("aswini")
l.insert("panju")
l.insert("vaanmathi")
for i in l.iterate():
    print(i, end = " ")
print(f"\nhead : {l.head.data}  tail : {l.tail.data} count : {l.count}")
'''
#-------------------------------------------------------------------------------------------------------------
#Write a python program to find the size of single linkedlist
'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = Node
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count+=1
l = LinkedList()
l.insert(3)
l.insert(2)
l.insert(6)
l.insert(7)
print(l.count)'''
#----------------------------------------------------------------------------------------------------------------------------
'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def insert(self, data):
        node =Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count+=1
    def iterate(self):
        node = self.head
        a= []
        while node:
            a.append(node.data)
            yield node.data
            node=node.next
            
    def find(self, data):
        for i in self.iterate():
            if data == i:
                return True
        return False
            
            
l = LinkedList()
l.insert("ajith")
l.insert("arun")
l.insert("aswini")
l.insert("panju")
l.insert("vaanmathi")
if l.find("vaanmath"):
    print(True)
else:print(False)
for i in l.iterate():
    print(i, end = "-->")
print(f"\nhead : {l.head.data}  tail : {l.tail.data} count : {l.count}")
'''
#----------------------------------------------------------------------------------------------------------
#Write a python program to access a specific item in a single linkedlist using index value
'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def insert(self, data):
        node =Node(data)
        if not self.head :
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail= node
        self.count+=1
    def iterate(self):
        cut = self.head
        while cut:
            yield cut.data
            cut = cut.next
    def __getitem__(self, idx):
        if idx > self.count - 1:
            print("Index outof rtange")
        else:
            cur = self.head
            for i in range(idx):
                cur = cur.next
            return cur.data
l = LinkedList()
l.insert("a")
l.insert("arun")
l.insert("fkn")
l.insert("dgf")
for i in l.iterate():
    print(i, end = " ")
print(l.count)
print(l[2])'''
#-----------------------------------------------------------------------------------------------------------
#Linked list
'''class Node:
    def __init__(self, data):
        self.data= data
        self.pointer = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def add(self, data):
        node = Node(data)
        
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            cur = self.head
            while cur.pointer is not None:
                cur = cur.pointer
            cur.pointer =node
            self.tail = node
        self.count+=1
    def display(self):
        if self.head is None:
            print("Linked list is Empty")
        else:
            cur = self.head
            while cur is not None:
                print(cur.data, end = " ")
                cur = cur.pointer
        print()
        
    def remove(self, data):
        if self.head == data:
            self.head = self.head.pointer
        else:
            cur = self.head 
            while cur.pointer is not None and cur.pointer.data != data:
                cur = cur.pointer
            cur.pointer = cur.pointer.pointer
    def __getitem__(self, index):
        if index>self.count-1:
            print("index outof range")
        else:
            cur = self.head
            for i in range(index):
                cur = cur.pointer
            return cur.data
    def __setitem__(self, index, value):
        if index>self.count-1:
            print("index outof range")
        else:
            cur = self.head
            for i in range(index):
                cur = cur.pointer
            cur.data = value
    def first(self):    
        self.head = self.head.pointer
    
    
l = LinkedList()
l.add(1)
l.add(3)
l.add(7)
l.add(4)
l.add("arun")
l.add("hari")
l.display()
print(f'count of {l.count}')
l.remove(7)
l.display()
l[4] = "aaaaaaaaaa"
l.display()
l.first()
l.display()
print(l.tail.data)'''
#---------------------------------------------------------------------------------------------------
#linked List -------------All operations--------------------------
'''class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None
        #Insertion
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        #Insertion
    def Insertion(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            cur = self.head
            while cur.pointer:
                cur = cur.pointer
            cur.pointer = node
            self.tail = node
        self.count+=1
    def display(self):
        if not self.head:
            print("Linked list is Empty")
        else:
            cur = self.head
            while cur:
                print(cur.data, end="-->")
                cur = cur.pointer
        print()
    def __getitem__(self, idx):
        if self.count-1 < idx:
            print("Invalid value")
        else:
            cur = self.head
            for i in range(idx):
                cur = cur.pointer
            print(cur.data)
    def __setitem__(self, idx, data):
        cur = self.head
        for i in range(idx):
            cur = cur.pointer
        cur.data = data
        print(cur.data)
    def InsertionAtBinging(self, data):
        newnode = Node(data)
        newnode.pointer = self.head
        self.head = newnode
    def InsertAtEnd(self, data):
        cur = self.head
        while cur.pointer:
            cur = cur.pointer
        cur.pointer= Node(data)
    def deleteBeginning(self):
        self.head = self.head.pointer
    def deleteEnd(self):
        cur = self.head
        while cur.pointer.pointer:
            cur = cur.pointer
        cur.pointer = None
    def searching(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return print(f"{data} found")
            cur = cur.pointer
        return print(f"{data} not found")
    def sort(self):
        if self.head is None:
            return

        # Initialize variables for sorting
        current_node = self.head
        is_sorted = False

        while not is_sorted:
            is_sorted = True
            while current_node.pointer is not None:
                if current_node.data > current_node.pointer.data:
                    # Swap the data of the nodes
                    current_node.data, current_node.pointer.data = (current_node.pointer.data, current_node.data)
                    is_sorted = False
                current_node = current_node.pointer
            current_node = self.head
    def sorting(self):
        c = self.head
        tf = False
        while not tf:
            tf = True
            while c.pointer is not None:
                if c.data > c.pointer.data:
                    c.data, c.pointer.data = c.pointer.data, c.data
                    tf = False
                c =c.pointer
        
l = LinkedList()
l.Insertion(2)
l.Insertion(1)
l.Insertion(8)
l.Insertion(45)
l.Insertion(86)
l.display()
l.sorting()
l.display()
print(l.head.data)'''
#------------------------------------------Mar 25--------------------------------------------------------------------
#Doubly Linked list
'''class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                del current
                break
            current = current.next

    def insert(self, data, position):
        if position < 0:
            raise ValueError("Position cannot be negative")
        if position == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current = self.head
        current_pos = 0
        while current_pos < position - 1 and current:
            current = current.next
            current_pos += 1
        if not current:
            raise IndexError("Position out of bounds")
        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(0)
dll.display()  # Output: 0 1 2 3
dll.delete(2)
dll.display()  # Output: 0 1 10 2 3
dll.insert(10, 2)

dll.insert(-1, 0)
dll.display()  # Output: -1 0 1 10 2 3

#dll.insert(5, 6)  # Raises IndexError: Position out of bounds
'''
#------------------------------------------------------------------------------------------------------------------
# Doubly Linked list
'''class Node():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter =0
    def append(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
            self.tail = newNode
            newNode.prev = cur
        self.counter +=1
    def prepend(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        self.counter+=1
    def postpend(self, data):
        newNode = Node(data)
        if not self.head:
            print(f"Doubly Linked list is Empty")
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
            self.tail = newNode
            cur.prev =cur
    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end="-->")
            cur = cur.next
        print()
    def __setitem__(self, idx, data):
        
        if self.counter-1 < idx:
            print(f"Index out of range!")
        else:
            cur = self.head
            for i in range(idx):
                cur = cur.next
            cur.data = data
    def insertBetween(self, data, prev_data, next_data):
        newNode =Node(data)
        current = self.head
        while current:
            if current.data == prev_data and current.next.data == next_data:
                newNode.next = current.next
                newNode.prev = current
                current.next.prev = newNode
                current.prev = newNode
                break
            current = current.next    
    def deleteBeginning(self):
        current = self.head
        if current:
            self.head = current.next
            self.prev = None
    def deleteEnd(self):
        if not self.head:
            print("Doubly Linked list is Empty")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        self.tail = current
        current.next = None
    def delete(self, data):
        if self.head.data == data:
            self.head =self.head.next
            return
        current = self.head
        while current.next is not None and current.next.data!= data:
            current =current.next
        current.next = current.next.next
        current.prev = current
    def display_backward(self):
        current = self.head
        if not current:
            print("Current is Empty")
        while current.next:
            
            current = current.next
        while current:
            print(current.data, end ="-->")
            current = current.prev
        print()
    def re(self):
        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev
        self.head, self.tail = self.tail, self.head
    def searching(self, data):
        if self.head.data == data:
            return print("data found")
        else:
            current = self.head
            while current.next:
                if current.data == data:
                    print("data founddddd")
                    return
                current = current.next
        return print("Data not found")
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.display()
dll.delete(4)
dll.display()'''
#------------------------------------------------------------------------------------------------------------
#Write a Python program to create a Balanced Binary Search Tree (BST) 
# using an array of elements where array elements are sorted in ascending order.
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sorted_array_to_bst(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])

    # Recursively build left and right subtrees
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid + 1:])

    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        inorder_traversal(root.right)
        print(root.data, end=" ")

# Example usage:
if __name__ == "__main__":
    sorted_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    root = sorted_array_to_bst(sorted_nums)

    print("Inorder traversal of the created BST:")
    inorder_traversal(root)

