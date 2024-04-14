import pyautogui
import time

print("Move the mouse to the desired location and wait for 5 seconds...")
time.sleep(5)

x, y = pyautogui.position()
print(f"Send button coordinate: x={x}, y={y}")
