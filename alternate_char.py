#write a python script to display alternate charte from the both side
s=input("enter a string: ")
left=0
right=len(s)-1
result=[]
while left<=right:
    if left==right:
        result.append(s[left])
    else:
        result.append(s[left])
        result.append(s[right])
    left +=1
    right -=1
print("alternate characters from the both directions")
print(''.join(result))
