1. Install PyInstaller
First, you need to install PyInstaller. Open a terminal or command prompt and run:

>> pip install pyinstaller

2. Navigate to Your Script's Directory
Use the cd command to navigate to the folder where your Python script (script.py) is located. For example:

>> cd path\to\your\script

3. Convert the Python Script to .exe
To convert your script, run the following PyInstaller command:

>> pyinstaller --onefile script.py

4. Locate the Executable
After PyInstaller finishes, you'll find the executable file in the dist folder inside your project directory:

project/dist/script.exe


5. Add an icon: If you want to add an icon to your executable:

>> pyinstaller --onefile --icon=icon.ico script.py
Replace icon.ico with the path to your icon file.

6. Hide the console window (for GUI applications):

>> pyinstaller --onefile --windowed script.py

Now, you have your .exe file, ready to run on any Windows machine without requiring Python!
