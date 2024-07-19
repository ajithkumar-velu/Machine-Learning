
'''
# Python Variables

a = 5 # int
b = "arun"  # str

print(a, b)

#Casting 

x = str(3)
y = int(3)
z = float(3)

print(f"int to str ={x}\nint to int = {y}\nint to float {z}")


# get the type 

c = 2
d = "arun"
e = 2.5

print(type(c), type(d), type(e))

# Many values to many variables

aa, bb, cc = 1, "arun", 3.4

print(aa, bb, cc)

# Unpack a collection

fruits = ["apple", "banana", 'orange']
q, w, r = fruits
print(q, w, r)


# output variable
print("This" +"Is"+"Example"+"For"+"+")
print("This", "is", "exaplem" "for", "comma")

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


#------------------------------- I now Basic of Python. because i will revice for remember and new this things are i pratice

a = "arun"
print(a[1])

for i in a:
    print(i)



print(f"lengh of a:", len(a))


print("b" not in  a)




'''




















'''


# string slicing
a = "This, example line"
b = "   This example line   "


#print(a[-5:-1])

print(a.upper())
print(a.lower())
print(b.strip())

print(a.replace("T", "h"))
print(a.split(","))

price = 59
txt = f"The price is {price:.3f} dollars"
print(txt)

print(a.encode())

'''

num = [1, 2, 3, 4]
count = 0
for i in num:
    if i-1 == 0 or (i-1) % 3 == 0:
        count +=1
    elif i+1 == 0 or (i+1) % 3 == 0:
        count +=1
        
print(count)
        
        
for i in range(5):
    print(i)g