from ctypes.wintypes import _COORD
import time 
import keyboard
from pyautogui import mouseDown 
from utils import scanForColour, click_at_loc

# config 
targetHex = "7018AD" # red
completeHEX = "33B6FF" 
coords = {
    "kick_btn": (963, 857),
    "upgrade_btn": (871, 586),
    "rebirth_menu": (99, 647),
    "rebirth_btn": (991, 776),
    "close_menu": (1307, 330)
    }

def kick():
    x,y = coords["kick_btn"]
    click_at_loc(x, y,0)
    time.sleep(0.20) # perfect kick level time 
    click_at_loc(x, y,0)
    time.sleep(5) # change to time for lucky block to be clicked and hatched 
    while True:
    # instantly exit if colour found
        if scanForColour(completeHEX):
            break

        keyboard.press("w")
        keyboard.press("space")

        # check constantly for 20 seconds
        start = time.time()

        while time.time() - start < 20:
            if scanForColour(completeHEX):
                keyboard.release("w")
                keyboard.release("space")
                break

            time.sleep(0.05)  # tiny delay so CPU doesn't explode

        keyboard.release("w")
        keyboard.release("space")

        # final exit check
        if scanForColour(completeHEX):
            
            keyboard.press("w")
            keyboard.press("space")
            time.sleep(0.5)
            keyboard.release("w")
            keyboard.release("space")
            keyboard.send("1")
            keyboard.send("1")
            break
            
def farmKickPower(count = 60):
    for i in range(count):
        pos = scanForColour(targetHex)
        if pos:
            click_at_loc(pos[0], pos[1],0)
            time.sleep(0.1)
           
def upgrade():
    click_at_loc(*coords["upgrade_btn"])

def toggleTraining():
    keyboard.send("1")

def rebirth():
    click_at_loc(*coords["rebirth_menu"])
    time.sleep(0.2)
    click_at_loc(*coords["rebirth_btn"])
    click_at_loc(*coords["close_menu"])

def runBot():
        global x
        # kick() 
        farmKickPower()
        # upgrade()
        # toggleTraining()
        # upgrade()
        # x += 1
        """if (x == 10):
            rebirth()
            x = 0"""

if __name__ == "__main__":
    print("Starting bot... Press Q to stop.")
    x = 0
    running = False

    last_f1 = False

    while True:
        current_f1 = keyboard.is_pressed("f1")

        if current_f1 and not last_f1:
            running = not running
            print("Running:", running)

        last_f1 = current_f1
        if keyboard.is_pressed("q"):
            break

        if running:
            runBot()

        time.sleep(0.1)
        