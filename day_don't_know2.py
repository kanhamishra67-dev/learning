"""constructor"""
"""it is aa special method which will execute automatically when we create the object of a class 
    when we create the object of a class we use __init__ for defining for defining constructor method
    a class can have a single constructor if you create two constructor the nearest constructor which 
    is close to the object or method will be executed"""

# class c1:
#     def __init__(self):
#         print("hello i am constructor")

# object=c1()
"""if we want to pass the value to the constructor we can pass the value in the parameterized constructor"""

# class c2:
#     def __init__(self):
#         print('hello i am first constructor')

#     def __init__(self):
#         print('hello i am second constructor')

#     def __init__(self):
#         print('hello i am third constructor')

# object=c2()

"""encapsulation : wrapping of data and methods into a single unit is called encapsulation"""


# class c3:
#     def m1(self,a,b):
#         self._a=a
#         self.__b=b

#     def display(self):
#         print("a:",self._a)
#         print("b:",self.__b)

#     def getter(self):
#         return self.__b
    
# obj=c3()
# obj.m1(10,20)
# obj.display()
# print(obj._a,obj.getter())

# class c4:
#     def __init__(self):
#         self.__a=0
#     def getter(self):
#         print(self.__a)
#     def setter(self,val):
#         self.__a=val

# obj=c4()
# obj.getter()
# obj.setter(100)
# obj.getter()

"""self id=s an instance of a class which is use to do following 
operation in the class :

1.declaring and accesing and modifying instance variable 
2.self is use to call the methids of your class 
3.we can access instance variable with the help of object"""

'''abstraction'''

"""abc = abstract bas class"""


# from abc import ABC,abstractmethod 

# class car(ABC):

#     @abstractmethod
#     def engine(self):
#         pass 

# class scorpio(car):

#     def engine(self):
#         power='120hp'
#     def start(self):
#         print("broom")

# s=scorpio()
# s.start()

# class c5:
#     data=100 
#     def m1(abc,a):
#         abc.a=a
#         print(abc.a)

# obj=c5()
# obj.m1(90)

# class paraent:
#     data=100 
#     def m1(abc,a):
#         abc.a=a
#         print(abc.a)

# class child(paraent):
#     def m1(self,b):
#         print("i am m2")
#         # super().m1(b)
#         paraent.m1(self,b)

# obj=child()
# obj.m1(10)

# class c1:
#     def __init__(self):
#         print("i am init from c1")

# class c2(c1):
#     def __init__(self):
#         super().__init__()
#         print("i am init from c2")

# class c3(c1):
#     def __init__(self):
#         super().__init__()
#         print("i am init from c3")

# class c4(c1):
#     def __init__(self):
#         super().__init__()
#         print("i am init from c4")

# obj = c4()
# m=c3()
# n=c2()

# class c0:
#     data=900
# class c1:
#     data=100 
#     def m1(self):
#         print("i am m1")

# class c2:
#     data=90
#     students=['rohan','ritik']
#     def m2(self):
#         print("i am m2")
#         super().m1()
#         print(super().data)

# class c3(c2,c1):
#     pass

# obj=c3()
# obj.m1()

# class c1:
#     data= 23
#     def m1(self):
#         print(" i am m1 ")
#         print(super().data)

# class c2:
#     data=34
#     student``

"""super() — quick explanation and examples

:-Purpose: return a proxy that lets a class call methods (or access attributes) 
from its parent (or next in MRO).

:-Python 3: use super() with no arguments inside instance methods.

:-Common uses: call parent init, extend parent methods, and support cooperative
 multiple inheritance."""

# class c1:
#     def __init__(self):
        