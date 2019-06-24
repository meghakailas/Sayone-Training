#program to  generate list and tuple
L=[]
T=()
data=input("Enter elemnts separated by comma:")
elements=data.split(",")
for i in elements:
    L.append(i)
print("The list is:",L)
T=tuple(L)
print("The tuple is:",T)


