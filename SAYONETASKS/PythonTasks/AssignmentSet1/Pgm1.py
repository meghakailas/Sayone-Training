# program to print dict{element:square}
dict={}
num=int(input("Enter how many numbers to find square:"))
for i in range(1,num+1):
    dict.update({i:i*i})
print(dict)