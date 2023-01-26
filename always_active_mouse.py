import pyautogui
import time

while True:
    x, y = pyautogui.size()
    pyautogui.moveTo(x * 0.5, y * 0.5)
    pyautogui.moveTo(x * 0.51, y * 0.51)
    time.sleep(10)
