# pip-module
Python module for using pip from Python scripts

## Installation

To install the module, clone this repository

```bash
git clone https://github.com/PiciAkk/pip-module
```

## Usage

1. Go to the cloned folder

```bash
cd pip-module
```

2. Make a new Python script

```bash
touch main.py
```

3. Write something in that script

```python
from pip-module import pip

pip().install("packageName") # install the package with the name `packageName` 
pip().uninstall("packageName") # uninstall the package with the name `packageName`

pip().runCommand("command", "packageName") # run the command `command` with the name `packageName`

# more functions coming soon
```
