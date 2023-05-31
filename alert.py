#alert.py
import ssl

import requests
import smtplib
import os
from email.message  import EmailMessage


def send_email(receiver,file):

	#smtp_server = "smtp.gmail.com"
	#port = 587
	email_sender = "enter email"
	email_receiver = receiver
	email_password = '<app pw>' 


	subject = """ALERT:File {} deleted""".format(file)

	body = """ {} file has been deleted """.format(file)

	em = EmailMessage()
	em['From'] = email_sender
	em['To'] = email_receiver
	em['Subject'] = subject
	em.set_content(body)


	context = ssl.create_default_context()

	with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
		smtp.login(email_sender, email_password)
		smtp.sendmail(email_sender, email_receiver, em.as_string())

def new_send(receiver,file):
	#smtp_server = "smtp.gmail.com"
	#port = 587
	email_sender = "chikson.49@gmail.com"
	email_receiver = receiver
	email_password = os.environ.get("APP_PW")


	subject = """ALERT:File {} """.format(file)

	body = """ file {} has been Edited or created""".format(file)

	em = EmailMessage()
	em['From'] = email_sender
	em['To'] = email_receiver
	em['Subject'] = subject
	em.set_content(body)


	context = ssl.create_default_context()

	with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
		smtp.login(email_sender, email_password)
		smtp.sendmail(email_sender, email_receiver, em.as_string())
