import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp-mail.outlook.com"# host for hotmail and outlook
sender_email = "Youremail@outlook.com or hotmail.com"
receiver_email = "reciver@domain.com"
password = input("Type your password and press enter:")
message = """\
Subject: Your subject

Your multiline text here
"""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print('Sent ✈')
