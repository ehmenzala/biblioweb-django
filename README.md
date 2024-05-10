# Biblioweb. Now Built With Django

## Table of Contents

- [Features](#features)
- [Run this Project](#run-this-project)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Install the Python Required Packages](#install-the-python-required-packages)
  - [Start the Development Server](#start-the-development-server)

## Features

1. Fullstack library application.
2. Online book reader.
3. Session auth handling.
4. _Coming soon..._

## Run this Project

### Create a Virtual Environment

It is strongly recommended for Python projects to use a virtual environment, to prevent package clutter and versions conflicts.

**Anaconda**

For more information, visit the [official Conda documentation website](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

```
$ conda create --name <virtual-environment-name>
```

```
$ conda activate <virtual-environment-name>
```

**Venv**

```
$ sudo apt-get install python3-venv
```

```
$ python3 -m venv <virtual-environment-name>
```

```
$ source <virtual-environment-name>/bin/activate
```

Make sure you choose the right Python interpreter in your IDE or text editor after creating your virtual environment.

_💡 **If you are using VSCode**, you can do this using the shortcut `Ctrl` + `Shift` + `P`. Then choose the option "Python: Select Interpreter," and select your interpreter (The one with your virtual environment name at the end)._

### Install the Python Required Packages

Make sure to `cd` into the project's root.

```
$ pip install requirements.txt
```

### Start the Development Server

```
$ python manage.py runserver --settings=config.settings.settings
```
