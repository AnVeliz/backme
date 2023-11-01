# BackMe

Python 3 must be installed as well as the `venv` module.

Use the `Makefile` to run the tool. There are following options supported:
| Argument | Default Value | Purpose |
| -------- | ------------- | ------- |
| `-f`     | `./data`      | Set the source data folder |
| `-t`     | `./data_archive`      | Set the target data folder |
| `-s`     | `./data`      | Set a list of patterns to skip |


### Example of a comand to run the archiver:

Interactive run: `make run ARGS="-f ./data -t ./data_archive -s '**/node_modules/*' '*.log'"`.

Non interactive run (without asking for the operation confirmation): `make run ARGS="-y -f ./data -t ./data_archive -s '**/node_modules/*' '*.log'"`.