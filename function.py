

"""def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n - 1)  

number = 5
print(f"The factorial of {number} is {factorial(number)}")
"""
#5th code
'''def run(*scores, playername):
    average = sum(scores) / len(scores)
    print(f"{playername}'s average score is {average:.2f}")

run(90, 90, 90, 90, 90, playername="MS Dhoni")
run(91, 91, 91, 91, 91, playername="Rohit Sharma")
run(92, 92, 92, 92, 92, playername="Virat Kohli")

'''
#4th code
'''def fun1(*k,playername):
    s=0
    for i in k:
        s=s+i
    print("Total Runs",s,"by",playername)

    
fun1(110,82,3,44,55,playername="Virat Kolhi")
fun1(44,55,66,90,21,51,playername="Rohit Sharma")
fun1(88,99,100,22,playername="Hardik Pandya")
'''
#3rd code

'''def fun1(x,y,z):
    print(x)
    print(y)
    print(z)

fun1(z=4,x=5,y=6)'''

#2nd code
"""def fun(x,y=0,z=0):
    print(x+y+z)

fun(4,6,7)
fun(3,2)

"""
#1st code

"""def add(x,y):
    z=x+y
    return z  

p=int(input("Enter 1st number: "))
q=int(input("Enter 2nd number: "))
g=add(p,q)
print("Addition is",g)"""
