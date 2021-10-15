import smtplib, ssl



message = """\
    Subject: Hi there
    
    Body: I hope you are having a good Friday!"""

#send email here

port = 465 # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "ahscodes@gmail.com"
receiver_email = "walz.andrew@gmail.com"
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login("ahscodes", password)
    server.sendmail(sender_email, receiver_email, message)
    # TODO: Send email here