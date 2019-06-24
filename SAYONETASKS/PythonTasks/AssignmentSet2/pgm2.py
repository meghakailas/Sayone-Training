#Get email input from user and check it is valid or not(Output: valid/ Invalid)
import re
pattern='^([a-zA-Z0-9-._]+)@([a-zA-Z0-9]+)\.([a-z]{2,3})([.a-z]{,2})$'
email=input("Enter mail id:")

m=re.match(pattern,email)
if m:
    print("valid")
else:
    print("Invalid")


