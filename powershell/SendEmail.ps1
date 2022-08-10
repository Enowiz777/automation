Connect-ExchangeOnline
Connect-MgGraph


$body  = @{
    content = Get-content -path "C:\Users\Enoch\Documents\Software Development\automation\powershell\Send Email\Templates\email-templates-master\11\index.html" -raw
    ContentType = 'html'
}

#recipients
$EmailAddress  = @{address = 'enowiz89@gmail.com'} # https://docs.microsoft.com/en-us/graph/api/resources/recipient?view=graph-rest-1.0
$Recipient = @{EmailAddress = $EmailAddress}  # https://docs.microsoft.com/en-us/graph/api/resources/emailaddress?view=graph-rest-1.0

$Message = New-MgUserMessage -UserId enoch.park@enowiz.com -Body $body -ToRecipients $Recipient -Subject "subject" 

Send-MgUserMessage -UserId "enoch.park@enowiz.com" -MessageId $Message.Id
