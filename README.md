## CEngine 1.0.1

CEngine (Convert Engine)

This is a converter for python to create exe from py. CEngine create automatically virtualenv and install the packages. It's using pyinstaller to create exe. It's better beaceuse the file is smaller and only the exe appear in the same directory as the target script.

# Usage

Terminal command: `cengine --script myscriptname.py [--name "customname" (default name: %script_name%-%current_time%.exe) or --custom-args="--icon ../.../" (custom args is made for the user can specify args for pyinstaller)]`

![alt text](https://github.com/Mesteri05/CEngine/blob/main/images/running_in_console.png?raw=true)