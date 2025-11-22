# class car:
#     model='2025'
#     colour='red'
#     def start(self):
#         print("car started")

#     def stop(self):
#         print("car stopped")

# alto800=car()
# # print(alto800.colour)
# # print(alto800.model)
# # alto800.start()
# # alto800.stop()
# # alto800.model='2024'
# # print(alto800.model)

# fortuner=car()
# # fortuner.model='2023'
# # fortuner.colour='black'
# # print(fortuner.colour)
# # print(fortuner.model)

# # data=[23,45,67,89,12,34,56,78,90]

# class student:
#     def record(self,subject,marks):
#         self.subject=subject
#         self.marks=marks

# nohan=student()
# nohan.record('maths',95)

# sohan=student()
# sohan.record('maths',88)

# data=['''hello my name is nohan i scored {} marks in {}'''.format(nohan.marks,nohan.subject),
#       '''hello my name is sohan i scored {} marks in {}'''.format(sohan.marks,sohan.subject)]

# # print(data)

# '''there is a real world sinario you have to create a class named class
#  and the attribute and the method of it :
#  take the example of your college :'''

# class college:
#     college_name='jit of engineering'
#     location='borawan'
#     courses_offered=['b-tech','mba','mca','polytechnic']
#     admission_time=['may','june','july']
#     def courses(self):
#         print("courses offered : ",self.courses_offered)

#     def principal(self):
#         print("principal name : mr. atul upadhay")   

#     def admission_process(self):
#         print("admission process starts from : ",self.admission_time)

# jit=college()
# print(jit.college_name)
# print(jit.location)
# jit.courses()
# jit.principal()
# jit.admission_time.append('august')
# jit.courses_offered.append('diploma')
# print(jit.courses_offered)
# print(jit.admission_time)

"""if there is no class variable named by your class name then it will create instance variable"""

# class c1:
#     a=10 
#     def m1(self):
#         print(c1.a)
#         c1.b=100
#         c1.a+=10
#         print(c1.a)
#         c1.b+=100
#         print(c1.b)

# obj=c1()
# obj.m1()

# class c1:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#         print("hello! i am constructor")

# obj=c1(10,20)

# class c2:
#     data=90
#     def m1(self):
#         print("i am m1 method" )


# obj=c2()
# # del obj.data
# print(obj.data)

# class c3:
#     def m1(self):
#         print("hello jitans")
    
# class c4:
#     def m2(self):
#         print("before executing m1 method")
#         # c3().m1() this is also a method to call a class or function 
#         c3().m1()
# obj=c4()
# obj.m2()

