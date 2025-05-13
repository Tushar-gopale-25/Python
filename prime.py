x=int(input("Enter the number of prime: "))
for i in range(2,x):
    if(x%i==0):
        print(x,"it is not prime")
else:
    print(x,"i is prime")
