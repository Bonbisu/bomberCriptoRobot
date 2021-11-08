import sys
from numpy import False_
import pyautogui
import time
from pyscreeze import locate
import config as c


class ClickService:
    def executeOnscreen(location) -> bool:        
        if location is None:
            return False
        time.sleep(3)
        pyautogui.leftClick(location)
        time.sleep(3)
        pyautogui.leftClick(location)        
        time.sleep(3)
        return True

    def closeScreen() -> None:
        pyautogui.hotkey(c.closeTabCmd)

    def update(self, location, pictureName, waitTimer):
        self.location = location
        self.pictureName = pictureName
        self.waitTimer = waitTimer
        self.retry = 3
    