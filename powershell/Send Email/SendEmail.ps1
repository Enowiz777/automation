﻿# Find-MgGraphCommand -command Get-MgUser | Select -First 1 -ExpandProperty Permissions
Connect-MgGraph -Scopes "User.Read.All","Group.ReadWrite.All"
Get-MgUser