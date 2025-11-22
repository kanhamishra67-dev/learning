# n=int(input())
# m=(n*2)-1

# for i in range(n):
#     for j in range(m):
#         if i+j==((m-1)/2) or i==(n-1) or j-i==((m-1)/2) :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=int(input())
# m=(n+1)//2
# for i in range(n):
#     for j in range(m):
#         if j==0 or i-j==0 or i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(9):
#     for j in range(8):
#         if (i>=2 and i<=6 and j==0) or (j<=3 and (i==2 or i==6)) or j-i==3 or j+i==11 or (i+j==4 and i-j==4) or (j==3) :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=int(input())

# for i in range((n*2)-1):
#     if i<=(n-1):
#         for j in range(i+1):
#             print('*',end="")
#         for k in range(((n*2)-1)-(2*(i+1))):
#             print(" ",end="")
#         if i<n-1:    
#                 for l in range(i+1):
#                     print("*",end="")
#         else :
#                 for o in range(n-1):
#                     print("*",end="")     
#     else:
#         for m in range((n*2)-i-1):
#             print("*",end="")
#         for p in range((2*(i-n+1))-1):
#             print(" ",end="")
#         for q in range((n*2)-i-1):
#             print("*",end="") 
#     print()

# n=int(input())

# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print(" * ",end=" ")
#     print()
    
# n=int(input())

# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(n-i):
#         print(" * ",end=" ")
#     print()

# n=int(input())

# for i in range((n*2)-1):
#     if i<n:
#         for j in range(n-i):
#             print(" ",end=" ")
#         for k in range(i+1):
#             print(" * ",end=" ")
#         print()
#     else:
#         for l in range(i-(n-2)):
#             print(" ",end=" ")
#         for m in range((n*2-1)-i):
#             print(" * ",end=" ")
#         print()
