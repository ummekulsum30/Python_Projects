import os
import math
import random
import smtplib

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)                                # To call gmail account Client.
s.starttls()
s.login("ummekulsum30122@gmail.com", "baki mjoz yocp btiy")            # To Login into your account.
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)                                  # Sending the OTP email.
o = input("Enter Your OTP >>: ")
if o == OTP:
    print("Congratulations!! Your Account has been Successfully Verified")
else:
    print("Please Check your OTP again")