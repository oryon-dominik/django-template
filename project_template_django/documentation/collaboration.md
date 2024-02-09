# Collaboration

## checklist

- [ ] Read [the documentation](./index.md).
- [ ] Perform self- or peer-reviewed assessments of all code committed.
- [ ] Use the [pre-commit-hooks](./for-developers/commithooks.md) defined in `.pre-commit-config.yaml`.
- [ ] The code effectively maintains test coverage for crucial components and passes all [pytest](./for-developers/pytest) runs.
- [ ] The code is thoroughly and thoughtfully documented to facilitate collaborative work.

Install the pre-commit hooks.
```bash
pre-commit install
```
Run tests to verify that everything is working.
```bash
pytest
```
Work on the code.
```bash
...
```
After a commit add yourself to the [CONTRIBUTERS.txt].
```bash
contributors-txt --aliases .\config\contributors\aliases.json
```

## communication via code tags

The following tags are used:

- `TODO`: For tasks that need to be done.
- `FIXME`: For things that need to be fixed, that are currently broken.
- `WTF`: For everything that makes you wonder why it is like this. Might be a bug, might be a hack, might be a feature.
- `TBD`: To be discussed. Need clear elaboration or decision.
- `BUG`: Clear bugs that need to be fixed.
- `HACK`: Quick hacks and dirty workarounds, that work but bring some oddities.

Also link to open issues, external documentations or pull request if applicable.

The `vscode` extensions `aaron-bond.better-comments` and
`Gruntfuggly.todo-tree` are recommended to emphasize and list all tags in the code.
