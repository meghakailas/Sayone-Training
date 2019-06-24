#Write a program that accepts a comma separated sequence of words as input and prints the
#words in a comma-separated sequence after sorting them alphabetically.

def sortString(string):
    words=string.split(",")
    words.sort()
    #print values
    for i in words:
        print(i,end=" ")


data=input("Enter strings separated by comas:")
sortString(data)

