# notebooks

Jupyter Notebooks to make your daily life easier


## gogogo kiss

TLDR: copy & paste me, GO.

Keep it short and simple - debugging for the TLDR generation.
includes module level imports and all django-settings available.
Preferrably use this notebook in the `vscode` directly.


## Develop with me

The more complex introduction in how to setup the django environment for the notebook.
works with the `browser`, `shell_plus`, for projects `using podman` and directly in `vscode`.

You can also attach the debugger to the notebook.


## Debug api login

Introduction to debugging, api login, user creation, management commands ...


## Common Issues

When running a notebook from an apps directory, *imports* from the same
module your're running the notebook from, might be messed up (_name mangling_).
So it's recommended to run notebooks from the dedicated notebooks directory or another specific place.
