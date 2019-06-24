# Let 'a' be the list of users who likes a post! I want to get displayed as below.
# a. eg 1 :-
# a = []
# b. Output :
# Nobody likes This
# c. eg 2 :-
# a = ['Alice']
# d. Output :
# Alice likes This
# e. eg 3 :-
# a = ['Alice','Bob']
# f. Output :
# Alice and Bob likes This
# g. eg 4 :-
# a = ['Alice', 'Bob', 'Charls']
# h. Output :
# Alice, Bob and Charls likes This
# i. eg 5 :-
# a = ['Alice', 'Bob', 'Charls','Denny']
# j. Output :
# Alice, Bob and 2 others likes This
# k. eg 6 :-
# a = ['Alice', 'Bob', 'Charls','Denny','Emely']
# l. Output :
# Alice, Bob and 3 others likes This

a = ['Alice', 'Bob', 'Charls','Denny','Emely','rtyu']
lst=a

if (len(lst)==0):
    print("Nobody likes this")
if (len(lst)==1):
    print(str(lst[0]) +"likes this")
if(len(lst)==2):
    print(str(lst[0])+"and"+str(lst[1])+"likes this")
if (len(lst)==3):
    print(str(lst[0])+","+str(lst[1])+"and"+str(lst[2])+"likes this")
if(len(lst)>3):
    l=len(lst)-2
    print(str(lst[0])+","+str(lst[1])+" and "+str(l)+" others likes this")



