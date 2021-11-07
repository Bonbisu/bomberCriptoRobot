import sys
from numpy import False_
import pyautogui
import config as c


class ScreenService:
    def __init__(self, pictureName):
        self.pictureName = pictureName

    def checkNewMap(self, waitTimer):
        location = pyautogui.locateOnScreen(
            c.newMapButtonImage, confidence=.8)
        if location is not None:
            pyautogui.leftClick(location)
            pyautogui.PAUSE = 15
            while pyautogui.locateOnScreen(c.newMapButtonImage, confidence=.8) is not None:
                pyautogui.leftClick(location)
                pyautogui.PAUSE = waitTimer
            return True
        return False

    def checkExist(self):
        if self.pictureName == '':
            return False
        if pyautogui.locateOnScreen(self.pictureName, confidence=.8) is not None:
            return True
        return False

    def checkError(self):
        if pyautogui.locateOnScreen(c.errorButtonImage, confidence=.8) is not None:
            return True
        if pyautogui.locateOnScreen(c.erroCenterModal, confidence=.8) is not None:
            return True
        if pyautogui.locateOnScreen(c.errorHeaderModal, confidence=.8) is not None:
            return True
        return False

    def update(self, pictureName):
        self.pictureName = pictureName
