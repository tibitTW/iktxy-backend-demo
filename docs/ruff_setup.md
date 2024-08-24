# Ruff Setup

> Auto format python code with Ruff

## Format options

setup in `pyproject.toml` at root directory of project:

```toml
[tool.ruff]
builtins = ["_"]
line-length = 79
```

more options can be found at: <https://docs.astral.sh/ruff/settings/>

## Auto format when save file

add these lines in `.vscode/settings.json`:

```json
"editor.formatOnSave": true,
"editor.codeActionsOnSave": {
    "source.organizeImports":"explicit"
},
```
