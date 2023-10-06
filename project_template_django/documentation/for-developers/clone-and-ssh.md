# Clone & SSH-checkout

## Add an `ssh-key` to your github account and modify your `ssh-config`.  

On posix systems.

    cat >> ~/.ssh/config <<EOL
    Host <desired-host-name>
        HostName github.com
        Port 22
    User <user-email>
    IdentityFile ~/.ssh/<private-key-added-and-sso-authed-on-github->

    EOL

Or on powershell.

    @"
    Host <desired-host-name>
        HostName github.com
        Port 22
    User <user-email>
    IdentityFile ~/.ssh/<private-key-added-and-sso-authed-on-github->

    "@ | Out-File -Append -FilePath "~/.ssh/config"


## Clone the repository.

    git clone git@<desired-host-name>:<account>/<repo>.git <directory>


## CWD

Change your working directory to the project root (using [zoxide](https://github.com/ajeetdsouza/zoxide)).

    z <directory>
