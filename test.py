#Q1``
# a = int(input())
# if a%2 == 0:
#     print("even")
# else:
#     print('odd')

#Q2
# a,b,c= map(int, input().split())
# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else:
#     print(c)
# year = int(input())

# if (year%4==0 and year%100!=0) or (year%400==0):
#     print("leap year")
# else:
#     print("not leap year")

#Q15
# a= int (input())
# if a==1:
#     print('monday')
# elif a==2:
#     print('tuesday')
# elif a==3:
#     print('wednesday')
# elif a==4:
#     print('thursday')
# elif a==5:
#     print('friday')
# elif a==6:
#     print('saturday')
# elif a==7:
#     print('sunday')
# else:
#     print('invalid input')

#Q14
# age= int(input("enter your age: "))
# if age>=60:
#     print('senior citizen')
# elif (age>=20 and age<60):
#     print('adult')
# elif (age>=13 and age<20):
#     print('teenager')
# elif (age>=5 and age<13):
#     print('child')
# elif (age>=2 and age<5):
#     print('toddler')
# elif (age>=0 and age<2):
#     print('infant')
# else:
#     print('invalid input')

#Q4
# marks= int(input("enter your marks: "))
# if marks>=90:
#     print('A')
# elif marks>=80:
#     print('B')
# elif marks>=70:
#     print('C')
# elif marks>=60:
#     print('D')
# elif marks<60:
#     print('f')
# else:
#     print('invalid input')

#Q5
# letter= input('enter a letter: ')
# volwels= ['a','e','i','o','u','A','E','I','O','U']
# if letter in volwels:
#     print('volwel')
# else:
#     print('consonent')

#Q6
# a= input('enter the arthamatic operator from given /n+,-,*,/')
# b= int(input("enter the first value  : "))
# c= int(input("enter the second value : "))
# if a==+:
#     print(a+b)
# elif (a==-):
#     print(a-b)
# elif (a==*) :
#     print(a*b)
# elif (a==/) :
#     print(a/b)
# else:
#     print("enter the valid input")

#Q7
# a= int(input())
# if a>0 :
#     print(f"the input is positive : ",a)
# elif a==0 :
#     print(f"the input is null : ",a)
# elif a<0 :
#     print(f"the input is negative : ",a)
# else:
#         print(f"the input is invalid")

# email= input("email address :")
# password= input("password :")

# a= int(input('''
#                 enter 1 for login
#                 enter 2 for exit'''))

#Q8    
# if a==1 :
#     new_email= input("enter the email : ")
#     new_password= input("enter the password : ")
#     if new_email==email and password==new_password :
#         print("login successful")
#     else :
#         if new_email!=email :
#             print("email address is wrong ")
#         elif new_password!=password :
#             print("the password is worng ")
#         else:
#             print("both are the wrong")
# else:
#     print("exited successfully")
    
#Q9
# a,b,c= map(int,input("enter the three sides of the thriangle :").split())

# if a+b>c or b+c>a or a+c>b :
#     print("the triangle is valid")
# else :
#     print ("triangle is not valid") 

#Q10
# a= float(input("enter the weight in Kg : "))
# b= float(input("enter the height in meter : "))

# bmi= a/(b**2)
# print(bmi)
# if bmi<18.5 :
#     print('under weight')
# elif bmi<24.9 :
#     print('normal weight')
# elif bmi<29.9 :
#     print('overweight')
# elif bmi>=30 :
#     print('obesity')
# else :
#     print('invalid input')

#Q11
# price= int(input())

# if price>=1000 :
#     discount=(price/100)*10
#     print(price-discount)
# elif price<1000 and price>=500 :
#     discount=(price/100)*5
#     print(price-discount)
# else:
#     print(price, "there is no discount on this product")


#Q12
# month= input('enter the name of the month')
# year= int(input("enter the year"))
# list=['jan','mar','may','jun','jul','aug','oct','dec']

# if month in list :
#     print("31 days")
# elif month=='apr' or month=='sep' or month=='nov' or month=='jun' :
#     print("30 days")
# elif year%4==0 and month=='feb' and year%100==0 and year%400!=0  :
#         print("29 days")
# elif year%100==0 and year%400!=0 and month=='feb' :
#         print("28 days")
# else :
#     print("invalid input")

#Q13


