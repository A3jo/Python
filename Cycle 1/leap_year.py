#1.Write a python program to display future leap years from current year to final year entered by the user.

c=int(input("enter the current year:"))
f=int(input("enter the final year:"))
print("The Leap years between " + str(c) + " and " + str(f) +  " are:")
for i in range(c,f+1):
    if(i%4==0)and(i%100!=0)or(i%400==0):
        print(i)
