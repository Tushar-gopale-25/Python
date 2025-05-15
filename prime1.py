l1=[]
sr=int(input("Enter the Starting range: "))
er=int(input("Enter the Ending range: "))
for x in range(sr,er):
    for i in range(2,x):
        if x%i==0:
            break
    else:
        print(x, end=" ")
        l1.append(x)
l=len(l1)
index=l//2
print("\nSum is",l1[index]+l1[index-1])
