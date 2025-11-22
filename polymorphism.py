"""polymorphism"""

"""in python achiving polymorphism directly is imposible """

"""Polymorphism means "many forms" — it's the ability of objects to
 take multiple forms or for functions/methods to behave differently 
 based on context."""

"""example 1"""

# class c1:
#     def m1(self,a,b=0,c=0):
#         if b==0 and c==0:
#             print(a)
#         elif c==0:
#             print(a+b)
#         else:
#             print(a*b*c)
# obj=c1()
# obj.m1(2,4,6)

"""example 2"""

# class c1:
#     def m1(self,a):
#         print(a)
# class c2:
#     def m1(self,a,b):
#         print(a+b)
# def call(class_name,*args)


"""overloading a method """

# class c1:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self_o1,self_o2,self_o3): # type: ignore
#         n1=self_o1.a+self_o2.a+self_o3.a
#         n2=self_o1.b+self_o2.b+self_o3.b
#         return n1,n2
    
# obj1=c1(10,20)
# obj2=c1(20,50)
# obj3=c1(10,30)
# print(obj1.__add__(obj2,obj3))

# class c2:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __mul__(self_o1,self_o2,self_o3): # type: ignore
#         n1=self_o1.a*self_o2.a*self_o3.a
#         n2=self_o1.b*self_o2.b*self_o3.b
#         return n1,n2
    
# obj1=c2(10,20)
# obj2=c2(20,50)
# obj3=c2(10,30)
# print(obj1.__mul__(obj2,obj3))

# import os
 


# with open ('new.txt','w+') as f:
#     f.writelines(['new file is created'])
#     f.seek(0)
#     n=f.readlines()
#     # print(n)

# with open('new.txt','a+') as f:
#     f.write('\nthis line is appended')
#     f.seek(0)
#     n=f.read()
#     print(n)

import csv 
data=[
    ['name','marks'],
    ['rohan',50],
    ['ram',50],
    ['rahul',60]
]
# with open("student.csv","w") as f:
#     writer=csv.writer(f)
#     writer.writerows(data)

with open("student.csv",'r') as f:
    f.read