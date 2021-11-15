#MAILING AUTOMATION

import smtplib #secure mail transfer protocol
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_user = "govindlalgupta9250@gmail.com"
email_send = "anshulshakya298@gmail.com"

subject = "Greeting To The Intern Acadmey"

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = "Greeting to The Intern Acadmey Hello from Abhishek gupta,Anshul Shakya and Vikram Negi Thanks To Intern Acadmey for giving us opportunity. "
msg.attach(MIMEText(body,'plain'))


text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

#Next, log in to the server
server.login("govindlalgupta9250@gmail.com", "Govind9210@")
#Send the mail

server.sendmail(email_user, email_send, text) 
server.quit()