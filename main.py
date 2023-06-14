import smtplib
import random
import datetime as dt
from secret_variables import password, email

my_email = "giemmatthew@gmail.com"
password = password
send_email = email

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=send_email,
                        msg="Subject:test message\n\nHello World")


data = open("quotes.txt", "r")
quotes = data.readlines()


now = dt.datetime.now()
if now.weekday() == 2:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=send_email, msg=quotes[random.randint(0, 101)])
