Install pywin32 to create a python Windows Service controlled by SCM.

First download python2.7 and install it, including pip
cd into C:\Python2.7\Scripts
pip install pypiwin32

Then download pyinstaller using pip
Pip install pyinstaller

Then compile testsvc.py file into an .exe file, run:
pyinstaller --onefile --hidden-import win32timezone testsvc.py
It will create a folder name dist under current folder where you run this command, then create a testsvc.exe there
Go to that dist folder and run below command to install/start/stop/remove your testsvc

testsvc.exe install

remember to copy the serviceConfig.txt into C: of the machine
check the log file under C: too after service gets started
