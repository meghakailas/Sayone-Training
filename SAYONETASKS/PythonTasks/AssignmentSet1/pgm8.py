#Get a list of numbers from users and print the smallest odd number.
def smallOdd(list,len):
    LOdd=[]

    for i in list:
        if (i%2!=0):
            LOdd.append(i)
    print("The odd numbers list is",LOdd)
    #find smallest odd number
    LOdd.sort()
    print("the smallest odd number is :", LOdd[0])

Lst=[]
n=int(input("Enter the count of numbers to be inserted:"))
for i in range(0,n):
    Lst.append(int(input("Enter number:")))

smallOdd(Lst,n)