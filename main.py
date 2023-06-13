import smtplib
from password import password as ps

my_email = "matthew.giem@gmail.com"
password = ps

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)