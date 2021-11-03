import smtplib, ssl


send_mail():

message = """
    Subject: Walzcast Music Club Link!

    Body: Here's the link: https://open.spotify.com/playlist/2PmDkOQ3mRqpwETXsJeZJd?si=d98fbadff0fd4f25
    """

#send email here

port = 465 # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "walzcast@gmail.com"
receiver_email = str(input("What's your email?"))
password = input("Type your password and press enter: ")
#how do i get the program to remember the password so i don't have to enter it in everytime? 

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login("walzcast", password)
    server.sendmail(sender_email, receiver_email, message)
    # TODO: Send email here