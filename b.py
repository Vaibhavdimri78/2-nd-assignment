#a = input("enter the comment")
#print(a)

#3
"""
a = int(input("enter first variable\n"))
b =complex(input("enter the complex variable\n"))
c = float(input("enter the third float variable"))
d= input("enter the first string")
e=input("enter second string")
print(a,b,c,d,e)
"""
#4
'''
a =5
b=5
print(id(a))
print(id(b))
#it gave same id value for both
c=5.0
print(id(c)) #data type changed so the id 
'''
#6
'''import keyword
print(keyword.kwlist)

#7
from a import u as U
print(U)

#8 
a = input("enter the first keyword that can be taken as data")
b =  input("enter the second keyword that can be taken as data")
c =  input("enter the third keyword that can be taken as data")
print(a,b,c)
'''
#9
Date = input("Enter today's date\n")
Time= input("Enter the time\n")
print(Date,Time,sep='__')
