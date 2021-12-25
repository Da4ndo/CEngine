__title__ = "CEngine"
__version__ = "1.0.6"

__author__ = "Da4ndo"
__discord__ = "Da4ndo#0934"
__github__ = "https://github.com/Da4ndo"
__licence__ = "MIT"

import datetime, time
import os
import subprocess
import sys
from colorama import Fore
import colorama


colorama.init()

class WindowsBuilder():
    def __init__(self, script, name="script+time", custom_args=None, add_imports=[]):
        self.script = script
        self.name = name
        self.custom_args = custom_args
        self.add_imports = add_imports

    def build(self):
        print("INFO:\tStarting build...")
        script_path = os.path.abspath(self.script)
        dir_path = os.path.dirname(script_path)

        if self.name == "script+time":
            script_name = self.script.split("\ ".replace(" ", ""))[-1]
            if not script_name:
                script_name = self.script.split("/")[-1]
            self.name = f"{script_name}_{datetime.date.today()}".replace(".py", "")

        fh = open("NUL","w")
        process = subprocess.Popen("pip install virtualenv", stdout = fh, stderr = fh)
        process.wait()
        print("INFO:\tCreating virtualenv...")
        process = subprocess.Popen("virtualenv venv", stdout = fh, stderr = fh)
        process.wait()

        import dis
        from collections import defaultdict

        print(f"INFO:\tOpening {script_path}")
        with open(script_path, "r", encoding='utf-8') as f:
            statements = f.read()

        instructions = dis.get_instructions(statements)
        imports = [__ for __ in instructions if 'IMPORT' in __.opname]

        print(f"INFO:\tAnalyzing {self.script}")
        grouped = defaultdict(list)
        for instr in imports:
            grouped[instr.opname].append(instr.argval)

        script_imports = list(set(grouped["IMPORT_NAME"]))
        for x in self.add_imports: script_imports.append(x)

        if "win32api" in script_imports or "win32gui" in script_imports or "win32con" in script_imports or "win32serviceutil" in script_imports or "win32service" in script_imports or "win32event" in script_imports: 
            script_imports.append("pywin32")
            try:
                script_imports.remove("win32api")
            except:
                pass
            try:
                script_imports.remove("win32gui")
            except:
                pass
            try:
                script_imports.remove("win32con")
            except:
                pass    
            try:
                script_imports.remove("win32serviceutil")
            except:
                pass
            try:
                script_imports.remove("win32service")
            except:
                pass
            try:
                script_imports.remove("win32event")
            except:
                pass
        if "cv2" in script_imports: script_imports.append("opencv-python"), script_imports.remove("cv2")
        if "git" in script_imports: script_imports.append("GitPython"), script_imports.remove("git")
        script_imports.append("pyinstaller")
        script_imports = list(set(script_imports))
        for imp in script_imports:
            if "." in imp:
                imp = imp.split(".")[0]
            process = subprocess.Popen(f"venv\Scripts\pip.exe install --upgrade {imp}", stdout = fh, stderr = fh)
            process.wait()
            if process.returncode == 0 or process.returncode == "0": 
                print(f"{Fore.RESET}INFO:\t{imp} installed successfully.")
        
        fh.close()
        try:
            os.remove("NUL")
        except:
            pass

        print(Fore.RESET, end="\r")
        if self.custom_args:
            process = subprocess.Popen(f"venv\Scripts\pyinstaller.exe --onefile --name \"{self.name}\" {self.custom_args} \"{script_path}\"", shell=True, stdout=subprocess.PIPE)
            process.wait()

        else:
            process = subprocess.Popen(f"venv\Scripts\pyinstaller.exe --onefile --name \"{self.name}\" \"{script_path}\"", shell=True, stdout=subprocess.PIPE)
            process.wait()
           
        print("==================== PyInstaller End ====================\n")

        time.sleep(1)
        if not (process.returncode == 0 or process.returncode == "0"):
            print(f"*** Unable to create exe beacuse some error ***\n")
            return

        print("INFO:\tStarting cleaning process...")

        def clean_directory(path):
            try:
                os.rmdir(path)
            except:
                for file in os.listdir(path):
                    pfile = path + "\\" + file
                    if os.path.isdir(pfile):
                        clean_directory(pfile)
                    elif os.path.isfile(pfile): 
                        try: 
                            os.remove(pfile)
                        except FileNotFoundError:
                            pass
                        except Exception as e:
                            raise e
                os.rmdir(path)

        if self.custom_args:
            if "--onedir" in self.custom_args:
                clean_directory(f"{dir_path}\\build")
                print(f"INFO:\tCleaned build directory")

                clean_directory(f"{dir_path}\\venv")
                print(f"INFO:\tCleaned venv directory")

                try:
                    clean_directory(f"{dir_path}\\__pycache__")
                    print(f"INFO:\tCleaned ___pycache__ directory")

                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    os.remove(f"{dir_path}\\{self.name}.spec")
                    print(f"INFO:\tRemoved {self.name}.spec file")
                except:
                    pass

                path = os.path.abspath(f"{self.name}.exe")
                print(f"\n*** Build finished in {path} ***\n")

                return

        try:
            os.replace(f"./dist/{self.name}.exe", f"./{self.name}.exe")
        except Exception as e:
            print(f"INFO:\tRuntime Warning: Can't move file from dist ( ..\.\dist\ ) to base ( ..\.\ ) directory. --> Exception: {e}")
            print("INFO\tSkipping cleaning part beacuse warnings.")
            path = os.path.abspath(f"{self.name}.exe")
            print(f"\n*** Build finished in {path} ***\n")
            return

        time.sleep(1)


        clean_directory(f"{dir_path}\\dist")
        print(f"INFO:\tCleaned dist directory")

        clean_directory(f"{dir_path}\\build")
        print(f"INFO:\tCleaned build directory")

        clean_directory(f"{dir_path}\\venv")
        print(f"INFO:\tCleaned venv directory")

        try:
            clean_directory(f"{dir_path}\\__pycache__")
            print(f"INFO:\tCleaned ___pycache__ directory")

        except FileNotFoundError:
            pass
        except Exception as e:
            raise e

        try:
            os.remove(f"{dir_path}\\{self.name}.spec")
            print(f"INFO:\tRemoved {self.name}.spec file")
        except:
            pass

        path = os.path.abspath(f"{self.name}.exe")
        print(f"\n*** Build finished in {path} ***\n")

class LinuxBuilder():
    def __init__(self, script, name="script+time", custom_args=None, add_imports=[]):
        self.script = script
        self.name = name
        self.custom_args = custom_args
        self.add_imports = add_imports

    def build(self):
        print("INFO:\tStarting build...")
        script_path = os.path.abspath(self.script)
        dir_path = os.path.dirname(script_path)

        if self.name == "script+time":
            script_name = self.script.split("\ ".replace(" ", ""))[-1]
            if not script_name:
                script_name = self.script.split("/")[-1]
            self.name = f"{script_name}_{datetime.date.today()}".replace(".py", "")

        fh = open("NUL","w")
        process = subprocess.Popen("pip install virtualenv", stdout = fh, stderr = fh)
        process.wait()
        print("INFO:\tCreating virtualenv...")
        process = subprocess.Popen("virtualenv venv", stdout = fh, stderr = fh)
        process.wait()

        import dis
        from collections import defaultdict

        print(f"INFO:\tOpening {script_path}")
        with open(script_path, "r", encoding='utf-8') as f:
            statements = f.read()

        instructions = dis.get_instructions(statements)
        imports = [__ for __ in instructions if 'IMPORT' in __.opname]

        print(f"INFO:\tAnalyzing {self.script}")
        grouped = defaultdict(list)
        for instr in imports:
            grouped[instr.opname].append(instr.argval)

        script_imports = list(set(grouped["IMPORT_NAME"]))
        for x in self.add_imports: script_imports.append(x)

        if "win32api" in script_imports or "win32gui" in script_imports or "win32con" in script_imports or "win32serviceutil" in script_imports or "win32service" in script_imports or "win32event" in script_imports: 
            script_imports.append("pywin32")
            try:
                script_imports.remove("win32api")
            except:
                pass
            try:
                script_imports.remove("win32gui")
            except:
                pass
            try:
                script_imports.remove("win32con")
            except:
                pass    
            try:
                script_imports.remove("win32serviceutil")
            except:
                pass
            try:
                script_imports.remove("win32service")
            except:
                pass
            try:
                script_imports.remove("win32event")
            except:
                pass
        if "cv2" in script_imports: script_imports.append("opencv-python"), script_imports.remove("cv2")
        if "git" in script_imports: script_imports.append("GitPython"), script_imports.remove("git")
        script_imports.append("pyinstaller")
        script_imports = list(set(script_imports))
        for imp in script_imports:
            if "." in imp:
                imp = imp.split(".")[0]
            process = subprocess.Popen(f"/venv/Scripts/pip install --upgrade {imp}", stdout = fh, stderr = fh)
            process.wait()
            if process.returncode == 0 or process.returncode == "0": 
                print(f"{Fore.RESET}INFO:\t{imp} installed successfully.")
        
        fh.close()
        try:
            os.remove("NUL")
        except:
            pass

        print(Fore.RESET, end="\r")
        if self.custom_args:
            process = subprocess.Popen(f"/venv/Scripts/pyinstaller --onefile --name \"{self.name}\" {self.custom_args} \"{script_path}\"", shell=True, stdout=subprocess.PIPE)
            process.wait()

        else:
            process = subprocess.Popen(f"/venv/Scripts/pyinstaller --onefile --name \"{self.name}\" \"{script_path}\"", shell=True, stdout=subprocess.PIPE)
            process.wait()
           
        print("==================== PyInstaller End ====================\n")

        time.sleep(1)
        if not (process.returncode == 0 or process.returncode == "0"):
            print(f"*** Unable to create exe beacuse some error ***\n")
            return

        def clean_directory_linux(path):
            try:
                os.rmdir(path)
            except:
                for file in os.listdir(path):
                    pfile = path + "/" + file
                    if os.path.isdir(pfile):
                        clean_directory_linux(pfile)
                    elif os.path.isfile(pfile): 
                        try: 
                            os.remove(pfile)
                        except FileNotFoundError:
                            pass
                        except Exception as e:
                            raise e
                os.rmdir(path)     

        if self.custom_args:
            if "--onedir" in self.custom_args:
                clean_directory_linux(f"{dir_path}\\build")
                print(f"INFO:\tCleaned build directory")

                clean_directory_linux(f"{dir_path}\\venv")
                print(f"INFO:\tCleaned venv directory")

                try:
                    clean_directory_linux(f"{dir_path}\\__pycache__")
                    print(f"INFO:\tCleaned ___pycache__ directory")

                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    os.remove(f"{dir_path}\\{self.name}.spec")
                    print(f"INFO:\tRemoved {self.name}.spec file")
                except:
                    pass

                path = os.path.abspath(f"{self.name}.exe")
                print(f"\n*** Build finished in {path} ***\n")

                return

        try:
            os.replace(f"/dist/{self.name}.exe", f"./{self.name}.exe")
        except Exception as e:
            print(f"INFO:\tWarning: Can't move file from dist ( .././dist/ ) to base ( .././ ) directory. --> Exception: {e}")
            print("INFO\tSkipping cleaning part beacuse warnings.")
            path = os.path.abspath(f"{self.name}.exe")
            print(f"\n*** Build finished in {path} ***\n")
            return

        print("INFO:\tStarting Cleaning process..")
        time.sleep(1)

                

        clean_directory_linux(f"{dir_path}/dist")
        print(f"INFO:\tCleaned dist directory")


        clean_directory_linux(f"{dir_path}/build")
        print(f"INFO:\tCleaned build directory")

        clean_directory_linux(f"{dir_path}/venv")
        print(f"INFO:\tCleaned venv directory")
        try:
            clean_directory_linux(f"{dir_path}/__pycache__")
            print(f"INFO:\tCleaned ___pycache__ directory")

        except FileNotFoundError:
            pass
        except Exception as e:
            raise e

        try:
            os.remove(f"{dir_path}/{self.name}.spec")
            print(f"INFO:\tRemoved {self.name}.spec file")
        except:
            pass

        path = os.path.abspath(f"{self.name}.exe")
        print(f"\n*** Build finished in {path} ***\n")

if __name__ == "__main__":
    if "cengine-no-flag" not in os.environ:
        print(f"CEngine (Convert Engine) Open-Source   Version: {__version__}")
        print("Respository: https://github.com/Da4ndo/CEngine/\n")
    time.sleep(0.5)
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--script', "--file", help='Define a script to be made into an executable')
    parser.add_argument('--name', help='Define the script name.', default="script+time")
    parser.add_argument('--custom-args', help='Add custom arguments.', default=None)
    parser.add_argument('--add-imports', nargs="+", help='Add more imports.', default=[])
    options = parser.parse_args(sys.argv[1:])
    if not options.script:
        parser.error("Must provide either a script")
    
    print(f"INFO:\tRecognized Platform: {sys.platform}")

    options.add_imports = list(options.add_imports)

    if sys.platform == "win32" or sys.platform == "win64":
        WindowsBuilder(options.script, options.name, options.custom_args, options.add_imports).build()
    elif sys.platform == "linux" or sys.platform == "linux2":
        LinuxBuilder(options.script, options.name, options.custom_args, options.add_imports).build()   