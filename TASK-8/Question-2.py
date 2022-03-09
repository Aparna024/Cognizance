from numpy import *
while True:
    a = array([])
    n = int(input("Enter the number of values you want for First array:  "))
    for i in range(n):
        e = int(input("Element:  "))
        a = append(a, e)
    b = array([])
    m = int(input("Enter the number of values you want for the second array:  "))
    for i in range(m):
        f = int(input("Element:  "))
        b = append(b, f)
    print("First Array:",a)
    print("Second Array:",b)
    c=a==b
    e=c.all()
    print(e)
    r=input("Do you want to check one more time(y/n)?")
    if r=='y':
        True
    if r=='n':
        break