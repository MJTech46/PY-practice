import pyautogui
import time

# Move the mouse to (100, 100) over 2 seconds
pyautogui.moveTo(100, 100, duration=2)

# Move the mouse relative to its current position
pyautogui.moveRel(50, 50, duration=1)

# Click at the current mouse position
pyautogui.click()
