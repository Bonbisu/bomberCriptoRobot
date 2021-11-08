import sys
import time
from numpy import False_
import pyautogui
import async_timeout
import asyncio

from IService import IService

ErrorButtons = ['App\\error_ok_modal.png','App\\error_center_modal.png','App\\error_header_modal.png']

class ErrorService(IService):
    async def CallBack() -> None:
        with async_timeout.timeout(60) :
           return await ErrorService.checkError()
    async def checkError():
        for button in ErrorButtons:
            print("async process")
            if pyautogui.locateOnScreen(button,confidence=.8) is not None:
                await ErrorService.errorThreat(pyautogui.locateOnScreen(button,confidence=.8))
        time.sleep(1)
    async def errorThreat(self,location):
        self.CallBack(self)
        return pyautogui.click(location)    


    