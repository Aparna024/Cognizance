from numpy import *
a=array([])
f=int(input('First Number:'))
l=int(input('Last Number:'))
for i in range(f,l):
    a=append(a,i)
    for i in range(5):
        a=append(a,0)
a=append(a,l)
print(a)