# Known bugs

## Windows

Problem: Something is using the applications port.

`Error: You don't have permission to access that port.`

Solution: Restart the host network service (administrator PowerShell)

```powershell
net stop hns; net start hns
```
