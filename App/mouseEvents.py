import sys
from numpy import False_
import pyautogui
import time


class ClickService:
    def __init__(self, location, pictureName, waitTimer):
        self.location = location
        self.pictureName = pictureName
        self.waitTimer = waitTimer
        self.retry = 3
        
    def executeOnscreen(self):        
        while self.retry > 0 and self.location is None:
            self.location = pyautogui.locateOnScreen(self.pictureName,confidence=.8)
            time.sleep(1)
            self.retry = self.retry -1
        if self.retry <= 0:
            self.retry = 3
            return False  
        time.sleep(0.5)
        pyautogui.leftClick(self.location)        
        time.sleep(self.waitTimer)
        print("click realizado, botão: " + (self.pictureName))
        return True

    def findWorkers(self):
        while self.retry > 0:
            self.location = pyautogui.locateAllOnScreen(self.pictureName,confidence=.9)
            self.retry = self.retry -1
            for l in self.location:
                    time.sleep(0.5)
                    pyautogui.leftClick(l)
                    time.sleep(0.5)
                    pyautogui.leftClick()
                    print("click realizado, botão: " + (self.pictureName))
            time.sleep(0.2)
            pyautogui.scroll(-1)
            time.sleep(0.2)
            pyautogui.scroll(-1)
            time.sleep(0.2)
            pyautogui.scroll(-1)
            time.sleep(0.2)
            pyautogui.scroll(-1)
            time.sleep(0.2)
            pyautogui.scroll(-1)
            time.sleep(0.2)
            pyautogui.scroll(-1)
        self.retry = 3
        return True
    
    def update(self, location, pictureName, waitTimer):
        self.location = location
        self.pictureName = pictureName
        self.waitTimer = waitTimer
        self.retry = 3
    