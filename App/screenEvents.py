import sys
import async_timeout
from numpy import False_
import pyautogui
from IService import IService
import config as c


class ScreenService(IService):
    async def checkNewMap(waitTimer):
        location = pyautogui.locateOnScreen(
            c.newMapButtonImage, confidence=.8)
        if location is not None:
            pyautogui.leftClick(location)
            while pyautogui.locateOnScreen(c.newMapButtonImage, confidence=.8) is not None:
                pyautogui.leftClick(location)
                pyautogui.PAUSE = waitTimer

    async def CallBack() -> None:
        with async_timeout.timeout(60) :
           return await ScreenService.checkNewMap(5)

    def checkExistScreen(image) -> bool:
        if image == '':
            return False
        if pyautogui.locateOnScreen(image, confidence=.8) is not None:
            print("click true in image : " + image)
            return True
        print("click false in image : " + image)
        return False
        
    def checkStoppedScreen(oldScreen) -> bool:
        if pyautogui.locateOnScreen(oldScreen, confidence=.8) is not None:
            print("check if workers sleep : TRUE")
            return True
        print("check if workers sleep : FALSE")
        return False
