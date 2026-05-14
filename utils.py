import time 
import pyautogui
import pydirectinput

def click_at_loc(x,y, delay = 0.2, count = 1):
    pydirectinput.moveTo(x, y)
    time.sleep(delay)
    pydirectinput.moveTo(x+1, y+1)
    for i in range(count):
        pydirectinput.click()

def scanForColour(targetHex, step = 15):

    target = tuple(int(targetHex[i:i+2], 16) for i in (0, 2, 4)) # hex to rgb
    screenshot = pyautogui.screenshot() # screenshot whole screen 
    
    for x in range(0, screenshot.width, step):
        for y in range(0, screenshot.height, step):
            if screenshot.getpixel((x, y)) == target:
                return (x, y)
    return None
