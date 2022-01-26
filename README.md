[![GitHub release](https://img.shields.io/github/release/Da4ndo/CEngine)](https://gitHub.com/Da4ndo/CEngine/releases/)
[![GitHub license](https://img.shields.io/github/license/Da4ndo/CEngine)](https://github.com/Da4ndo/CEngine/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Da4ndo/CEngine)](https://GitHub.com/Da4ndo/CEngine/issues/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Da4ndo/CEngine)

# CEngine

CEngine (Convert Engine)

![alt text](https://github.com/Mesteri05/CEngine/blob/main/images/cengine.icon.jpg)

This is an ***open-source*** *converter* for python to create **exe from py**. CEngine creates *automatically* virtualenv and installs the packages, and deletes unnecessary files after the build is complete.

- It's using **PyInstaller** or **Nuitka** to create exe. 
- It's better because the executable is smaller (less bytes) and,
- **CEngine** starts a cleaning proccess and deletes the dist, build, *.spec files/directories after the build is complete.

## CHANGELOG

1.0.8 (01/01/2022):

- Added `-b` | `--windows-defender-bypass` option.
- Solved issues, cleaned code.
- Code optionalization.

`More in changelog.txt`

## How does it work?

1. Creates a virtualenv.
2. Analyzes the target script to get the imports.
3. Installs the packages with pip.
4. Starts pyinstaller or nuitka.

![alt text](https://github.com/Mesteri05/CEngine/blob/main/images/running_in_console.png)
Virtualenv create processs and analyze proccess 👆

![alt text2](https://github.com/Mesteri05/CEngine/blob/main/images/running_in_console2.png)
Cleaning process 👆

## Usage

```
usage: cengine.py [-h] [--nuitka] [-s SCRIPT] [-n NAME] [-b] [--add-imports ADD_IMPORTS [ADD_IMPORTS ...]]
                  [--force-platform FORCE_PLATFORM] [--clean]

options:
  -h, --help            show this help message and exit
  --nuitka              Change from pyinstaller to nuitka compiler.
  -s SCRIPT, --script SCRIPT, --file SCRIPT
                        Define a script to be made into an executable.
  -n NAME, --name NAME  Define the script name.
  -b, --windows-defender-bypass
                        Bypass windows defeneder with base64 encode/decode.
  --add-imports ADD_IMPORTS [ADD_IMPORTS ...]
                        Add more imports.
  --force-platform FORCE_PLATFORM
                        Add custom arguments.
  --clean               Clean failed builds.
```
Convert: 

- cengine --script **cengine.py** --name **cengine** --icon **NONE** --version-file **cengine.version**
- cengine **--nuitka** --script **cengine.py** --name **cengine**

Clean:

- cengine --script **cengine.py** --clean
- cengine **--nuitka** --script **cengine.py** --clean
