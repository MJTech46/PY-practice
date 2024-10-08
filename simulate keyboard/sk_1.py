import pyautogui
import time

# Pause for 5 seconds before typing
time.sleep(5)

# Type the text as if typing on the keyboard
pyautogui.typewrite("Hello, World!", interval=0.1)  # Interval between keystrokes

# Simulate 'Ctrl + z' for undo
pyautogui.hotkey('ctrl', 'z')
pyautogui.hotkey('ctrl', 'z')


# keep your cursor here after executing this code: 
