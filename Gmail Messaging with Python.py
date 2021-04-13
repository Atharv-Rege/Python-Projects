#Before doing this please enable less secure apps in google
#Here is the Link: https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OQcNJt0OcK83-dOBolnzviJIRlqzyi4B92CbbpHjqSDBYp-5J5JwWqiCnuY_EhLe2oZYaKdO21SngjqvB2gg3-RqJY8A
import smtplib
from email.message import EmailMessage
from string import Template
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
