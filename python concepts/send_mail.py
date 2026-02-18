import smtplib, ssl
import config
"""
in my case i have stored my id pass in diff config.py file
"""

#
# sender =
# receivers =  #"vini.doshi96@gmail.com" #


sender_email = config.EMAIL_ADDRESS #"my@gmail.com" #"talhasay2u@gmail.com"
password =  config.PASSWORD #input("Type your password and press enter: ") #"talhasay2u@gmail.com"

receiver_email = config.EMAIL_ADDRESS
message = """
Subject: Hi there

This message is sent from talha
user wants to get in touch."""


smtp_server = "smtp.gmail.com"
port = 587  # For starttls

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print("message sent...")
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e," <- message not sent")
finally:
    server.quit()
