import smtplib
from secret_variables import password, email

my_email = "matthew.giem@gmail.com"
password = password

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail()