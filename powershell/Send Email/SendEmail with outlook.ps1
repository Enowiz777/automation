# Create an Outlook application object
$outlook = New-Object -ComObject Outlook.Application

# Create a new mail item
$mail = $outlook.CreateItem(0)

# Set the properties of the email
$mail.Subject = "This is the subject of the email"
$mail.Body = "This is the body of the email"
$mail.To = "recipient@example.com"
$mail.Send()