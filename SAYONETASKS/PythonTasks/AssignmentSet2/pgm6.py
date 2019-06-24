# Write a function to send email to given email addr
import smtplib
try:
    mail= smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('meghakailas.sayonetech@gmail.com','*****')

    mail.sendmail('meghakailas.sayonetech@gmail.com','lakshmi.sayonetech@gmail.com','ghhhgg')
    mail.close()
except Exception as e:
    print(str(e))