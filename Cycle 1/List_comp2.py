#write python program to form a list of vowels slected from a given word.
v=['a','e','i','o','u']
w=input("enter the word:").lower()
list=[]
for i in w:
    if i in v:
        list.append(i)
print(list)


