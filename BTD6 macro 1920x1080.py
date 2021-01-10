import pyautogui
import time

#For screen resolution of 1920 x 1080
#runs 25 times
for x in range(0, 25):
    pyautogui.click(960, 850)
    time.sleep(2)
    pyautogui.click(1830, 175)
    pyautogui.click(675, 550)
    pyautogui.click(675, 550)
    for x in range (0, 5):
        pyautogui.click(1550, 800)
    for x in range (0,2):
        pyautogui.click(1550, 650)
    for x in range (0,2):
        pyautogui.click(1830,990)
    time.sleep(1.5)
    pyautogui.click(960, 875)
    time.sleep(.5)
    pyautogui.click(960, 850)
    time.sleep(2)