#vairable length keyword arguments
def fun1(**k):
    for i in k:
        print(i,":",k[i])
    print()


fun1(car="Maruti",year=2018,owner="Rajiv")
fun1(emp=23,empname="Vijay",empage=21,empsl=22000)
