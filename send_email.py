
from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height):
    from_email = "baloghtomas95@gmail.com"
    from_password = "72rpfj7xo7"
    to_email = email if isinstance(email, list) else [email]

    subject = "Collector email!"
    message = "Hello, this is your data %s and avegare height of our survey is %s" % (height, average_height)
    
    # msg=MIMEText(message, 'html')
    # msg['Subject']=subject
    # msg['To']=to_email
    # msg['From']=from_email

    msg = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (from_email, ", ".join(to_email), subject, message)

    gmail=smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    print(msg)
    gmail.sendmail(from_email,to_email, msg)
    gmail.close()
