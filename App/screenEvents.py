import sys
from numpy import False_
import pyautogui

class ScreenService:
    def __init__(self,pictureName): 
        self.pictureName = pictureName

    def checkNewMap(self, waitTimer):
        location = pyautogui.locateOnScreen('App\\new_map_button.png',confidence=.8)
        if location is not None:
            pyautogui.leftClick(location)
            pyautogui.PAUSE = 15
            while pyautogui.locateOnScreen('App\\new_map_button.png',confidence=.8) is not None:
                pyautogui.leftClick(location)
                pyautogui.PAUSE = waitTimer        
            return True
        return False
    
    def checkExist(self):
        if self.pictureName == '':
            return False        
        if pyautogui.locateOnScreen(self.pictureName,confidence=.8) is not None:
            return True
        return False    
        
    def checkError(self):
        if pyautogui.locateOnScreen('App\\error_ok_modal.png',confidence=.8) is not None:
            return True
        if pyautogui.locateOnScreen('App\\error_center_modal.png',confidence=.8) is not None:
            return True
        if pyautogui.locateOnScreen('App\\error_header_modal.png',confidence=.8) is not None:
            return True
        return False
    
    def update(self,pictureName): 
        self.pictureName = pictureName
    