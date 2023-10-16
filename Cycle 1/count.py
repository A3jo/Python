#Count the occurences of a word in a sentence.
a=input("Enter the sentence:").lower()
b=input("Enter the word:").lower()
c=a.count(b)
print("The number of times "+ b+" repeats in the senetence is " +str(c))