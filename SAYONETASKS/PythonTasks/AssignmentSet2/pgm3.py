#Write a program to find all mobile number inside a string
import re
str=input("Enter text:")
x=re.findall(r'\d{10}', str)
print("The mobile numbers in the text are:",x)


