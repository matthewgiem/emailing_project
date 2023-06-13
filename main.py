import smtplib
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
