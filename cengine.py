__title__ = "CEngine"
__version__ = "1.0.7"

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

class Cleaner:
    class PyInstaller:
        class Windows:
            def clean(dir_path, filename, **options):
                print("INFO: Starting cleaning process...")
                filename = filename.replace(".py", "").replace(".exe", "")

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

                if options.get('custom_args', None):
                    if "--onedir" in options["custom_args"]:

                        try:
                            clean_directory(f"{dir_path}\\build")
                            print(f"INFO: Cleaned build directory")
                        except FileNotFoundError:
                            pass
                        except Exception as e:
                            raise e

                        try:
                            clean_directory(f"{dir_path}\\venv")
                            print(f"INFO: Cleaned venv directory")
                        except FileNotFoundError:
                            pass
                        except Exception as e:
                            raise e

                        try:
                            clean_directory(f"{dir_path}\\__pycache__")
                            print(f"INFO: Cleaned ___pycache__ directory")

                        except FileNotFoundError:
                            pass
                        except Exception as e:
                            raise e

                        try:
                            os.remove(f"{dir_path}\\{filename}.spec")
                            print(f"INFO: Removed {filename}.spec file")
                        except:
                            pass

                        return

                try:
                    clean_directory(f"{dir_path}\\dist")
                    print(f"INFO: Cleaned dist directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    clean_directory(f"{dir_path}\\build")
                    print(f"INFO: Cleaned build directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    clean_directory(f"{dir_path}\\venv")
                    print(f"INFO: Cleaned venv directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    clean_directory(f"{dir_path}\\__pycache__")
                    print(f"INFO: Cleaned ___pycache__ directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    os.remove(f"{dir_path}\\{filename}.spec")
                    print(f"INFO: Removed {filename}.spec file")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                print("")

        class Linux:
            def clean(dir_path, filename, **options):
                print("INFO: Starting cleaning process...")
                filename = filename.replace(".py", "").replace(".exe", "")

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

                if options.get('custom_args', None):
                    if "--onedir" in options["custom_args"]:
                        try:
                            clean_directory_linux(f"{dir_path}/build")
                            print(f"INFO: Cleaned build directory")
                        except FileNotFoundError:
                            pass
                        except Exception as e:
                            raise e

                        try:
                            clean_directory_linux(f"{dir_path}/venv")
                            print(f"INFO: Cleaned venv directory")
                        except FileNotFoundError:
                            pass
                        except Exception as e:
                            raise e

                        try:
                            clean_directory_linux(f"{dir_path}/__pycache__")
                            print(f"INFO: Cleaned ___pycache__ directory")
                        except FileNotFoundError:
                            pass
                        except Exception as e:
                            raise e

                        try:
                            os.remove(f"{dir_path}/{filename}.spec")
                            print(f"INFO: Removed {filename}.spec file")
                        except FileNotFoundError:
                            pass
                        except Exception as e:
                            raise e

                        return

                try:
                    clean_directory_linux(f"{dir_path}/dist")
                    print(f"INFO: Cleaned dist directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e    

                try:
                    clean_directory_linux(f"{dir_path}/build")
                    print(f"INFO: Cleaned build directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    clean_directory_linux(f"{dir_path}/venv")
                    print(f"INFO: Cleaned venv directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    clean_directory_linux(f"{dir_path}/__pycache__")
                    print(f"INFO: Cleaned ___pycache__ directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    os.remove(f"{dir_path}/{filename}.spec")
                    print(f"INFO: Removed {filename}.spec file")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e
            
                print("")

    class Nuitka:
        class Windows:
            def clean(dir_path, filename, **options):
                print("INFO: Starting cleaning process...")
                filename = filename.replace(".py", "").replace(".exe", "")

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

                try:
                    clean_directory(f"{dir_path}\\{filename}.dist")
                    print(f"INFO: Cleaned dist directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    clean_directory(f"{dir_path}\\{filename}.build")
                    print(f"INFO: Cleaned build directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e
                
                try:
                    clean_directory(f"{dir_path}\\{filename}.onefile-dist")
                    print(f"INFO: Cleaned onefile-dist directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    clean_directory(f"{dir_path}\\{filename}.onefile-build")
                    print(f"INFO: Cleaned onefile-build directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    clean_directory(f"{dir_path}\\venv")
                    print(f"INFO: Cleaned venv directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    clean_directory(f"{dir_path}\\__pycache__")
                    print(f"INFO: Cleaned ___pycache__ directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    os.remove(f"{dir_path}\\{filename}.spec")
                    print(f"INFO: Removed {filename}.spec file")
                except:
                    pass
                    
                print("")

        class Linux:
            def clean(dir_path, filename, **options):
                print("INFO: Starting cleaning process...")
                filename = filename.replace(".py", "").replace(".exe", "")

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

                try:
                    clean_directory_linux(f"{dir_path}/{filename}.dist")
                    print(f"INFO: Cleaned dist directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    clean_directory_linux(f"{dir_path}/{filename}.build")
                    print(f"INFO: Cleaned build directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    clean_directory_linux(f"{dir_path}/{filename}.onefile-dist")
                    print(f"INFO: Cleaned onefile-dist directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    clean_directory_linux(f"{dir_path}/{filename}.onefile-build")
                    print(f"INFO: Cleaned onefile-build directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    clean_directory_linux(f"{dir_path}/venv")
                    print(f"INFO: Cleaned venv directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    clean_directory_linux(f"{dir_path}/__pycache__")
                    print(f"INFO: Cleaned ___pycache__ directory")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e

                try:
                    os.remove(f"{dir_path}/{filename}.spec")
                    print(f"INFO: Removed {filename}.spec file")
                except FileNotFoundError:
                    pass
                except Exception as e:
                    raise e
            
                print("")

colorama.init()

class PyInstallerWindowsBuilder():
    def __init__(self, script, name="script+time", **kwargs):
        self.script = script
        self.name = name
        self.custom_args = kwargs.get('custom_args', [])
        self.add_imports = kwargs.get('add_imports', [])

    def build(self):
        print("INFO: Starting build...")
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
        print("INFO: Creating virtualenv...")
        process = subprocess.Popen("virtualenv venv", stdout = fh, stderr = fh)
        process.wait()

        import dis
        from collections import defaultdict

        print(f"INFO: Opening {script_path}")
        with open(script_path, "r", encoding='utf-8') as f:
            statements = f.read()

        instructions = dis.get_instructions(statements)
        imports = [__ for __ in instructions if 'IMPORT' in __.opname]

        print(f"INFO: Analyzing {self.script}")
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
                print(f"{Fore.RESET}INFO: {imp} installed successfully.")
        
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
           
        print(f"{Fore.RESET}==================== PyInstaller End ====================\n")

        time.sleep(1)
        if not (process.returncode == 0 or process.returncode == "0"):
            print(f"*** Unable to create exe beacuse some error ***")
            return
        
        try:
            os.replace(f"./dist/{self.name}.exe", f"./{self.name}.exe")
        except Exception as e:
            print(f"INFO: Runtime Warning: Can't move file from dist ( ..\.\dist\ ) to base ( ..\.\ ) directory. --> Exception: {e}")
            print("INFO\tSkipping cleaning part beacuse warnings.")
            path = os.path.abspath(f"{self.name}.exe")
            print(f"\n*** Build finished in {path} ***")
            return
        
        Cleaner.PyInstaller.Windows.clean(dir_path, self.script, custom_args=self.custom_args)        

        path = os.path.abspath(f"{self.name}.exe")
        print(f"*** Build finished in {path} ***")

class PyInstallerLinuxBuilder():
    def __init__(self, script, name="script+time", **kwargs):
        self.script = script
        self.name = name
        self.custom_args = kwargs.get('custom_args', [])
        self.add_imports = kwargs.get('add_imports', [])

    def build(self):
        print("INFO: Starting build...")
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
        print("INFO: Creating virtualenv...")
        process = subprocess.Popen("virtualenv venv", stdout = fh, stderr = fh)
        process.wait()

        import dis
        from collections import defaultdict

        print(f"INFO: Opening {script_path}")
        with open(script_path, "r", encoding='utf-8') as f:
            statements = f.read()

        instructions = dis.get_instructions(statements)
        imports = [__ for __ in instructions if 'IMPORT' in __.opname]

        print(f"INFO: Analyzing {self.script}")
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
                print(f"{Fore.RESET}INFO: {imp} installed successfully.")
        
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
           
        print(f"{Fore.RESET}==================== PyInstaller End ====================\n")

        time.sleep(1)
        if not (process.returncode == 0 or process.returncode == "0"):
            print(f"*** Unable to create exe beacuse some error ***")
            return

        try:
            os.replace(f"/dist/{self.name}.exe", f"./{self.name}.exe")
        except Exception as e:
            print(f"INFO: Warning: Can't move file from dist ( .././dist/ ) to base ( .././ ) directory. --> Exception: {e}")
            print("INFO\tSkipping cleaning part beacuse warnings.")
            path = os.path.abspath(f"{self.name}.exe")
            print(f"\n*** Build finished in {path} ***")
            return

        Cleaner.PyInstaller.Linux.clean(dir_path, self.script, custom_args=self.custom_args)

        path = os.path.abspath(f"{self.name}.exe")
        print(f"*** Build finished in {path} ***")

class NuitkaWindowsBuilder():
    def __init__(self, script, name="script+time", **kwargs):
        self.script = script
        self.name = name
        self.custom_args = kwargs.get('custom_args', [])
        self.add_imports = kwargs.get('add_imports', [])

    def build(self):
        print("INFO: Starting build...")
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
        print("INFO: Creating virtualenv...")
        process = subprocess.Popen("virtualenv venv", stdout = fh, stderr = fh)
        process.wait()

        import dis
        from collections import defaultdict

        print(f"INFO: Opening {script_path}")
        with open(script_path, "r", encoding='utf-8') as f:
            statements = f.read()

        instructions = dis.get_instructions(statements)
        imports = [__ for __ in instructions if 'IMPORT' in __.opname]

        print(f"INFO: Analyzing {self.script}")
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
        script_imports.append("nuitka")
        script_imports = list(set(script_imports))
        for imp in script_imports:
            if "." in imp:
                imp = imp.split(".")[0]
            process = subprocess.Popen(f"venv\Scripts\pip.exe install --upgrade {imp}", stdout = fh, stderr = fh)
            process.wait()
            if process.returncode == 0 or process.returncode == "0": 
                print(f"{Fore.RESET}INFO: {imp} installed successfully.")
        
        fh.close()
        try:
            os.remove("NUL")
        except:
            pass

        print(Fore.RESET, end="\r")
        process = subprocess.Popen(f"venv\Scripts\python -m nuitka --mingw64 \"{script_path}\" --standalone --onefile -o \"{self.name}.exe\" {self.custom_args}", shell=True, stdout=subprocess.PIPE)
        process.wait()
           
        print(f"{Fore.RESET}==================== Nuitka End ====================\n")

        time.sleep(1)
        if not (process.returncode == 0 or process.returncode == "0"):
            print(f"*** Unable to create exe beacuse some error ***")
            return
        
        Cleaner.Nuitka.Windows.clean(dir_path, self.script, custom_args=self.custom_args)

class NuitkaLinuxBuilder():
    def __init__(self, script, name="script+time", **kwargs):
        self.script = script
        self.name = name
        self.custom_args = kwargs.get('custom_args', [])
        self.add_imports = kwargs.get('add_imports', [])

    def build(self):
        print("INFO: Starting build...")
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
        print("INFO: Creating virtualenv...")
        process = subprocess.Popen("virtualenv venv", stdout = fh, stderr = fh)
        process.wait()

        import dis
        from collections import defaultdict

        print(f"INFO: Opening {script_path}")
        with open(script_path, "r", encoding='utf-8') as f:
            statements = f.read()

        instructions = dis.get_instructions(statements)
        imports = [__ for __ in instructions if 'IMPORT' in __.opname]

        print(f"INFO: Analyzing {self.script}")
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
        script_imports.append("nuitka")
        script_imports = list(set(script_imports))
        for imp in script_imports:
            if "." in imp:
                imp = imp.split(".")[0]
            process = subprocess.Popen(f"/venv/Scripts/pip install --upgrade {imp}", stdout = fh, stderr = fh)
            process.wait()
            if process.returncode == 0 or process.returncode == "0": 
                print(f"{Fore.RESET}INFO: {imp} installed successfully.")
        
        fh.close()
        try:
            os.remove("NUL")
        except:
            pass

        print(Fore.RESET, end="\r")
        process = subprocess.Popen(f"venv\Scripts\python -m nuitka --mingw64 \"{script_path}\" --standalone --onefile -o \"{self.name}.exe\" {self.custom_args}", shell=True, stdout=subprocess.PIPE)
        process.wait()
           
        print(f"{Fore.RESET}==================== Nuitka End ====================\n")

        time.sleep(1)
        if not (process.returncode == 0 or process.returncode == "0"):
            print(f"*** Unable to create exe beacuse some error ***")
            return

        Cleaner.Nuitka.Linux.clean(dir_path, self.script, custom_args=self.custom_args)

if __name__ == "__main__":
    print(f"CEngine (Convert Engine) Open-Source   Version: {__version__}")
    print("Respository: https://github.com/Da4ndo/CEngine/\n")
    time.sleep(0.5)
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--nuitka', action='store_true', help='Change from pyinstaller to nuitka compiler.', default=False)
    parser.add_argument('-s','--script', "--file", help='Define a script to be made into an executable.')
    parser.add_argument('-n','--name', help='Define the script name.', default="script+time")
    parser.add_argument('--add-imports', nargs="+", help='Add more imports.', default=[])
    parser.add_argument('--force-platform', help='Add custom arguments.', default=None)
    parser.add_argument('--clean', action='store_true', help='Clean failed builds.', default=False)

    options, unknown_args = parser.parse_known_args(sys.argv[1:])
    if not options.script:
        parser.error("Must provide either a script.")

    if options.force_platform: sys.platform = options.force_platform
    options.add_imports = list(options.add_imports)

    print(f"INFO: Recognized Platform: {sys.platform}")

    if sys.platform == "win32" or sys.platform == "win64":
        if options.nuitka:
            if options.clean:
                Cleaner.Nuitka.Windows.clean(os.path.dirname(os.path.abspath(options.script)), options.script)
                print("*** Cleanning process finished. ***")

            else:
                NuitkaWindowsBuilder(options.script, options.name, custom_args=" ".join(unknown_args), add_imports=options.add_imports).build()
        else:
            if options.clean:
                Cleaner.PyInstaller.Windows.clean(os.path.dirname(os.path.abspath(options.script)), options.script)
                print("*** Cleanning process finished. ***")

            else:
                PyInstallerWindowsBuilder(options.script, options.name, custom_args=" ".join(unknown_args), add_imports=options.add_imports).build()

    elif sys.platform == "linux" or sys.platform == "linux2":
        if options.nuitka:
            if options.clean:
                Cleaner.Nuitka.Linux.clean(os.path.dirname(os.path.abspath(options.script)), options.script)
                print("*** Cleanning process finished. ***")

            else:
                NuitkaLinuxBuilder( options.script, options.name, custom_args=" ".join(unknown_args), add_imports=options.add_imports).build()   
        else:
            if options.clean:
                Cleaner.PyInstaller.Linux.clean(os.path.dirname(os.path.abspath(options.script)), options.script)
                print("*** Cleanning process finished. ***")

            else:
                PyInstallerLinuxBuilder( options.script, options.name, custom_args=" ".join(unknown_args), add_imports=options.add_imports).build()  

    else:
        print("ERROR:\tThis platform is not supported.")