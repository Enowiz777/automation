# Import the Microsoft Teams PowerShell module
Import-Module -Name MicrosoftTeams

# Connect to Microsoft Teams (You may need to log in with your M365 admin credentials)
Connect-MicrosoftTeams


$teams = Get-Team
# $teams

$team = Get-Team -GroupId "dfd274d1-44fa-46e8-854c-9af363a3e772"

$team | Set-Team -Description "modified"




Write-Output "Hello I am going to do this"
Write-Warning "This is a warning message."
Write-Error "This is an error message."
Write-Verbose "This is a verbose message." -Verbose
Write-Debug "This is a debug message." -Debug