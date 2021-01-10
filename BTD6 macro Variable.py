import pyautogui
import time

#For variable screen size
w,h = pyautogui.size()
print(w,h)
for x in range(0, 25):
    pyautogui.click(0.5*w, 0.787*h)
    time.sleep(2)
    pyautogui.click(0.953*w, .162*h)
    for x in range (0,2):
        pyautogui.click(.351*w, .509*h)
    for x in range (0, 5):
        pyautogui.click(.807*w, .741*h)
    for x in range (0,2):
        pyautogui.click(.807*w, .602*h)
    for x in range (0,2):
        pyautogui.click(.953*w,.917*h)
    time.sleep(1.5)
    pyautogui.click(.5*w, .81*h)
    time.sleep(.5)
    pyautogui.click(.5*w, .787*h)
    time.sleep(2)