#Write a program to generate and print another tuple whose values are even numbers in the
#given tuple (1,2,3,4,5,6,7,8,9,10)

T1=(1,2,3,4,5,6,7,8,9,10)
L=[]
for i in T1:
    if(i%2==0):
        L.append(i)
print("The tuple containing even numbers is :" ,tuple(L))
