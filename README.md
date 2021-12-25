[![GitHub release](https://img.shields.io/github/release/Da4ndo/CEngine)](https://gitHub.com/Da4ndo/CEngine/releases/)
[![GitHub license](https://img.shields.io/github/license/Da4ndo/CEngine)](https://github.com/Da4ndo/CEngine/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Da4ndo/CEngine)](https://GitHub.com/Da4ndo/CEngine/issues/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Da4ndo/CEngine)

# CEngine

CEngine (Convert Engine)

![alt text](https://github.com/Mesteri05/CEngine/blob/main/images/cengine.icon.jpg)

This is an ***open-source*** *converter* for python to create **exe from py**. CEngine create *automatically* virtualenv and install the packages.

- It's using pyinstaller to create exe. 
- It's better because the executable is smaller (less bytes) and,
- **CEngine** starts a cleaning proccess and deletes the dist, build, *.spec files/directory when the converting is ended.

## CHANGELOG

1.0.5.1 (12/25/2021):

- Rework / Redesign **README.md**

## How does it work?

1. Creates a virtualenv.
2. Analyzes the target script to get the imports.
3. Installs the packages with pip.
4. Starts pyinstaller.


![alt text](https://github.com/Mesteri05/CEngine/blob/main/images/running_in_console.png)
Convert py to exe example 👆

![alt text2](https://github.com/Mesteri05/CEngine/blob/main/images/running_in_console2.png)
Convert py to exe 2 example 👆

## Usage

```
usage: cengine.exe [-h] [--script SCRIPT] [--name NAME] [--custom-args CUSTOM_ARGS]
                   [--add-imports ADD_IMPORTS [ADD_IMPORTS ...]]

options:
  -h, --help            show this help message and exit
  --script SCRIPT, --file SCRIPT
                        Define a script to be made into an executable
  --name NAME           Define the script name.
  --custom-args CUSTOM_ARGS
                        Add custom arguments.
  --add-imports ADD_IMPORTS [ADD_IMPORTS ...]
                        Add more imports.
```