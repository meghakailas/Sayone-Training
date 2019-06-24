#Write a Python program to print yesterday, today, tomororow

from datetime import datetime,timedelta
x=datetime.now()
# print(x)
print("Today is",x.strftime("%A"))
dy=x-timedelta(days=1)
print(dy)
print("Yesterday was:",dy.strftime("%A"))
tom=x+timedelta(days=1)
print("Tomorrow is:", tom.strftime("%A"))