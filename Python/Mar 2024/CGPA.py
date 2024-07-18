# credits= {'ipr' : 2,'ads' : 3, 'oose' : 3,
# 'python' : 3, 'ac' : 4, 'adslab' : 2, 'pythonlab' : 2, 'softskil' : 1, 'math':6}

# grade= {'ipr' : 7, 'ads' :7, 'oose' : 8, 'python' : 8,
# 'ac' : 7, 'adslab' : 9, 'pythonlab' :  10, 'softskil' : 9, 'math':4}
# up  = 0
# low = sum(credits.values())
# for i, j in zip(credits.values(), grade.values()):
#     up +=i*j
# gpa = up/low
# print(gpa)


'''credits= {'ipr' : [2, 7],'ads' : [3, 7], 'oose' : [3, 8], 'python' : [3, 8],
          'ac' : [4, 7], 'adslab' : [2, 9], 'pythonlab' : [2, 10], 'softskil' : [1, 9]}
low = sum(i[0] for i in credits.values())
up = sum(i[0]*i[1] for i in credits.values())
print(up/low)

'''

cg = dict()
countOfSub = int(input("Enter how many subject you have, and if you have any arrear ignore that subject: "))
print("Enter your credits & grade point\nlike if credit 4 and grade point 7: 4 7")

cg = {i : list(map(float, input().split())) for i in range(countOfSub)}
print(cg)
low = sum(i[0] for i in cg.values())
up = sum(i[0]*i[1] for i in cg.values())
print(f"your GPA: {up/low}")

#1: 6.933333333333334
#2: 7.0125
#3: 7.1909090909090905
#4: 7.524
#5: 7.654545454545455
#6: 6.1000000000000005

#CGPA = 7.06241134751773

'''
O  - 10
A+ - 9
A  - 8
B+ - 7
B  - 6


'''

