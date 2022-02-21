l=[]
n=int(input("Enter the num of records to be stored:"))

for i in range (n):
     e=input("Enter the record (Roll no, Name, Marks):")
     s=e.split()
     f=list(s)
     l.append(f)
print("----------------------3(i)---------------------")
print("Roll no", "Name", "Marks", sep='   ')

#(i)Printing the list in tabular form
for i in l:
    print(i[0], i[1], i[2], sep='        ')
print("----------------------3(ii)---------------------")
#(ii) Extracting and printing second record

m=l[1]
print(m[0], m[1], m[2], sep='   ')
