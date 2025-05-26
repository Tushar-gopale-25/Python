r=int(input("Enter the range: "))
a,b=-1,1
for i in range(r):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
