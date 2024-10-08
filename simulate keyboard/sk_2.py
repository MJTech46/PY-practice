from pynput.keyboard import Controller, Key
import time

keyboard = Controller()

# Pause for 5 seconds before typing
time.sleep(5)

# Type "Hello, World!"
keyboard.type("Hello, World!")

# Press Ctrl + z
keyboard.press(Key.ctrl)
keyboard.press('z')
keyboard.release('z')
keyboard.release(Key.ctrl)

# keep your cursor here after executing this code: 
