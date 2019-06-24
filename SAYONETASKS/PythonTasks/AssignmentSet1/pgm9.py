#Read and print number of lines, words and characters in the given file.
F=open("f.txt",mode="r")
data=F.readlines()

countl=0
countw=0
countch=0
lst=[]

for line in data:
    line=line.strip("\n")
    countch+=len(line)
    countl+=1
    # line.split(" ")
    #print(line)
    word=line.split()
    print(word)
    for each in word:
        countw+=1



print("The total number of lines in the file is",countl)
print("The total number of words in the file is",countw)
print("the total nuber of charactres in file is:",countch)


