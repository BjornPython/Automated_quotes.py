import random
import smtplib
from email.message import EmailMessage
import ssl

with open("quotes.txt") as data_file:
    quotes = data_file.readlines()
    quote = random.choice(quotes)

my_email = ""
my_pass = ""
email_receiver = [""]
subject = "Daily Motivational Quote."
body = quote

em = EmailMessage()
em["From"] = my_email
em["Subject"] = subject
em.set_content(body)
context = ssl.create_default_context()


def send_email(recipient):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as connection:
        connection.login(my_email, my_pass)
        connection.sendmail(my_email,
                            recipient,
                            em.as_string()
                            )


for email in email_receiver:
    send_email(email)
