# How-to-debugging

You can use the debugger attached to `vscode`.  
The workspace (if used) is already configured to use the correct python
interpreter and the correct working directory and may be attached to the pytest
or python process. So you can set breakpoints and debug your code here.
`Ctrl+Shift+D` will open the debug view.

`print` statements in the code pollute the commit history and are an anti-pattern.

We have a dev-logger, which is usally better than print statements:

```python
import logging
log = logging.getLogger("dev")
```

If print statements are used for debugging nevertheless, they should follow a
simple convention and all start with `>>> ` to make them distinguishable from
regular print statements. Debugging-print statements should be removed before
the code is committed.
