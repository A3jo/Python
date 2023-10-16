#write python program to generate positive list of numbers froma given list of integers.

lst=[]
a=int(input("enter the number of elements of the list:"))
for i in range(0,a):
    el=int(input("enter the element:"))
    lst.append(el)
    print("list",lst)
print("positive numbers are:")
for i in lst:
    if i>=0:
        print(i)