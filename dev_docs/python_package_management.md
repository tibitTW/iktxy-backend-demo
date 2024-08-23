# Python Package Management

使用 poetry 進行環境與套件管理

## Virtual Environment

execute this command to use `.venv` as virtual environment folder:

```shell
poetry config virtualenvs.in-project true
```

create virtual env:

```shell
poetry env use python
```

enter virtual env:

```shell
poetry shell
```

exit:

```shell
exit
```

## Package Management

add a package:

```shell
poetry add <package-name>
```

or add a package to dev dependencies:

```shell
poetry add <package-name> --group dev
# or
poetry add <package-name> -G dev
```

export packages to `requirements.txt` (add `--without-hashes` to drop hashes):

```shell
poetry export -f requirements.txt -o requirements.txt
# including dev dependencies
poetry export -f requirements.txt -o requirements.txt --with dev
```
