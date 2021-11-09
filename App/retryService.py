import time

import pyautogui
from mouseEvents import ClickService
from screenEvents import ScreenService
import config as c

class tries:
    def execute(retries, imgAddress) -> bool:        
        if retries > 10 or ScreenService.checkExistScreen(imgAddress) is False:
            print("Step : Retry - ", retries)
            print("Step : Image - ", imgAddress)
            return False
        else :
            while retries <= 10 and ScreenService.checkExistScreen(imgAddress) :
                print("Step : forcing click ", retries)
                time.sleep(1)
                if ClickService.executeOnscreen(pyautogui.locateOnScreen(imgAddress, confidence = .7)) is True :
                    print("Click Sucessful ", imgAddress)
                    break
                print("Tries ", retries)
                print("Image Not Found  " + imgAddress)
                retries += 1
                time.sleep(1)
        return True