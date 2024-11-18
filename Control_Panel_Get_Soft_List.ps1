$dontinclude = 'Microsoft','Realtek','Intel','AMD','Driver','Redistributable','Visual C\+\+','.NET', 'Windows', 'NVIDIA', 'Java'

Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* , `
                    HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* |
Select-Object DisplayName, Publisher, InstallLocation |
Where-Object {
    $exclude = $false
    foreach ($term in $dontinclude) {
        if ($_.'DisplayName' -match $term -or $_.'Publisher' -match $term -or $_.'InstallLocation' -match $term) {
            $exclude = $true
            break
        }
    }
    # Only include items where $exclude is false
    $exclude -eq $false
} |
# Remove the 'Publisher' property from the output
Select-Object DisplayName |
Sort-Object DisplayName
