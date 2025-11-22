#faunction:- it is a reusable block of code which can be called as needed

# def f1():
#     print('hello')

# #indentation:- the indentatin is space which is given to code to conclude the code belongs to the fuction 

# def F2():
#     print('hellow')
#     print('max')

#the indentatin of evvery line should be the same or the syntex will give an error

#this reduses  the lines in the code

#it saves memory 

# data=[1,234,5,76,7]

# def revers():
#     for i in range(len(data)-1,-1,-1):
#         print(data[i], end=" ")

# revers()

# def m(a,b):
#     print(a*b)

# m(10,10)

# def table(a):
#     for i in range(1,11):
#         print(a,'x',i,'=',a*i)
#     print(" ")

# table(5)

# table(2)

# def fb(n):
#     a,b=0,1
#     for i in range(n):
#         print(a,end=" ")
#         a,b=b,a+b

# fb(10)

# def str(a):
#     h=''
#     for i in a:
#         h=i+h
#     print(h)

# str('dhananjay')

# def fac(a):
#     count=1
#     for i in range(1,a+1):
#         count*=i
#     print(count)

# fac(5)

# data = ['act','pots','stop','tops','cat','hat']
# mac=[]
# for i in data:
#     a=[]
#     for j in data:
#         if sorted(i)==sorted(j):
#             a.append(j)
#     if a not in mac:
#         mac.append(a)
# print(mac)


# n=int(input())
# data=[x for x in range(1,(n*10)+1) if x%n==0]
# print(data)

#nexted for loop in listcommprihension
# data= [(x+y) for x in range(1,5) for y in range(1,3)]
# print(data)

# data=(lambda x:x**2)(4)
# print(data)

# data = [(lambda x:x**2)(x) for x in range(1,5)]
# print(data)