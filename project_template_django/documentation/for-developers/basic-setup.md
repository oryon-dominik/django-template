# Basic setup for your machine to start developing

The project assumes `python` with `poetry`, `podman` and `compose` are
installed and running.

Most of us are using `vscode` as their editor, so we will install it as well.
Skip, if you are using another editor.

And of course, we rely on `git`.

On posix you probably know how to install `pyenv`, `podman` and `compose` from
your package manager yourself. Otherwise you're perfeclty capable to adapt, I
guess. Just ask if you need help.

Windows:
```powershell
# Install the newest powershell.
Invoke-Expression "& { $(irm https://aka.ms/install-powershell.ps1) } -UseMSI"

# Install [scoop](https://scoop.sh/).
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

# Install your editor.
scoop install vscode

# Install the newest python via pyenv.
scoop install pyenv
pyenv update
pyenv install <project-python-version>
pyenv local <project-python-version>
# Install poetry.
curl -sSL https://install.python-poetry.org | python -

# Install git and git-lfs.
scoop install git
scoop install git-lfs

# Install podman and compose.
scoop install main/podman
scoop install main/docker-compose

# Start the podman-machine.
podman machine init
podman machine start
```
