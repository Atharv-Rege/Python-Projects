import smtplib
from email.message import EmailMessage
from pathlib import Path

email = EmailMessage()

email['from'] = "Your Name"
email['to'] = 'To email address'
email['subject'] = 'Subject'
email.set_content("""
You can put your multiple line text here
                  """
                  )

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("Your google email", 'Your google password')
    smtp.send_message(email)
    print('Sent ✈')
# Click the run button to run it
