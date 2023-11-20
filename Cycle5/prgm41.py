import csv
c=open('csv3.csv',newline='')
d=csv.DictReader(c)
print("Rollno   Student_name")
for i in d:
    print(i["ROLL NO"],'      ',i["STUDENT NAME"])