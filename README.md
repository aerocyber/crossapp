# crossapp

A zipapp based app packaging and distribution utility for Python.


## Statistics

[![OSSAR](https://github.com/aerocyber/crossapp/actions/workflows/ossar-analysis.yml/badge.svg)](https://github.com/aerocyber/crossapp/actions/workflows/ossar-analysis.yml) [![CodeQL](https://github.com/aerocyber/crossapp/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/aerocyber/crossapp/actions/workflows/codeql-analysis.yml) [![Python package](https://github.com/aerocyber/crossapp/actions/workflows/python-package.yml/badge.svg)](https://github.com/aerocyber/crossapp/actions/workflows/python-package.yml)

Crossapp is  a Python package that provides a simple and easy to use interface to create and distribute Python applications. It is based on Python's zipapp module, which is a tool that allows you to create a standalone application from a Python source file.

## Installation

Currently, Crossapp is only available for Python 3.6 and above. To install Crossapp, run the following command:

```bash
python3 -m pip install crossapp --user --upgrade
```

or, for latest(dev) un-released version,

```bash
python3 -m pip install --user --upgrade git+https://github.com/aerocyber/crossapp#egg=crossapp
```

## Usage

Crossapp comes with a simple command line interface that allows you to create, distribute and use Python applications. To use Crossapp, run the following command:

```bash
crossapp <command> [<args>]
```

## Help

Run the following command to get help on a command:

```bash
crossapp <command> --help
```

To get help on all commands, run:

```bash
crossapp --help
```

## System Requirements

OS: Linux, macOS, Windows

Minimal Python version: 3.6

pip version: 19.0.0 or higher
