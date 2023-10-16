#Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.
lst=[]
n=int(input("enter the number of values:"))
for i in range(0,n):
    b=int(input("enter the value:"))
    if b>100:
        lst.append('over')
    else:
        lst.append(b)

print(lst)