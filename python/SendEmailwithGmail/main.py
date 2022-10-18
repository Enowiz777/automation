#
from email.message import EmailMessage
from app2 import password
import ssl
import smtplib
from jinja2 import Environment, FileSystemLoader, PackageLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader("email-templates-master"),
    autoescape=select_autoescape(["html", "xml"]),
)

template = env.get_template("1/index.html")
html = template.render()


# Predefined variables.
email_sender = "enowiz89@gmail.com"
# Import from app2.py and mask it when I upload in a github.
email_password = password
email_receiver = "enochpark89@gmail.com"
subject = "Don't forget to subscribe"
body = """
# When you watch a video, please hit subscribe.
"""

# Create an email message
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(html, subtype="html")

# Create a SSL context
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


# Import SSL and SMTP library
