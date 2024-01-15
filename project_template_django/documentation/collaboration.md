## Checklist for collaboration

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
