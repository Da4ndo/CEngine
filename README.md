# CEngine 1.0.5

CEngine (Convert Engine)

This is a *converter* for python to create **exe from py**. CEngine create *automatically* virtualenv and install the packages.

- It's using pyinstaller to create exe. 
- It's better because the executable is smaller (less bytes) and,
- **CEngine** starts a cleaning proccess and
deletes the dist, build, *.spec files/directory when the converting is ended.

## CHANGELOG

1.0.5 (11/20/2021):

- Added **--add-imports** parameter

1.0.4 (10/24/2021):

- Fixing cleaning issues

1.0.3 (09/27/2021):
    
- Added Linux support
- Fixing bugs
- Can be run by py file, not just exe. ( ./obfuscated_py/obf_cengine.py )

## Usage

Terminal command: `cengine --script myscriptname.py [--name "customname" (default name: %script_name%-%current_time%.exe) or --custom-args="--icon ../.../" (custom args is made for the user can specify args for pyinstaller) or --add-imports discord python-opencv ...]`

![alt text](https://github.com/Mesteri05/CEngine/blob/main/images/running_in_console.png?raw=true)

===========================================================================

![alt text2](https://github.com/Mesteri05/CEngine/blob/main/images/running_in_console2.png?raw=true)
