import webbrowser
import pyautogui
from mouseEvents import ClickService
from screenEvents import ScreenService
import config as c
import time
import random
from retryService import tries


class worker:
    def findWorkers() -> bool:
            print("START Worker Select Process => ") 
            count = 0
            time.sleep(5)
            while pyautogui.locateAllOnScreen(c.worker_button,confidence=.9) is None and pyautogui.locateOnScreen(c.worker_heroes_button,confidence=.9) is not None:
                if tries.execute(count, c.worker_heroes_button) is False:
                    count += 1
                    pyautogui.scroll(-5)
                    time.sleep(3)
                    if count > 100:
                        print("click fail in image : " + c.worker_heroes_button)            
                        return False
                    if pyautogui.locateAllOnScreen(c.worker_stamina_bar,confidence=.9) is not None:
                        break
                time.sleep(5)                    
            print("click " + str(count) + " in image : " + c.worker_heroes_button)
            count = 0
            
            for l in pyautogui.locateAllOnScreen(c.worker_stamina_bar,confidence=.9):
                if count > 2 :
                    print("3 heroes selected ") 
                    count = 0
                    break
                time.sleep(2)
                newLocation = pyautogui.locateOnScreen(c.worker_button, c.worker_stamina_bar, confidence=.9)
                pyautogui.leftClick(newLocation)
                time.sleep(2)
                pyautogui.leftClick(newLocation)
                time.sleep(2)
                if newLocation.__len__() > 2 :
                    count += 1                
            

            if pyautogui.locateOnScreen(c.general_close_button) is not None:
                count = 0
                tries.execute(count, c.general_close_button)

            print("End Worker Select Process") 
            while pyautogui.locateOnScreen(c.start_farm_treasure_image) is None and count < 100:
                print("Trying start the farm") 
                count += 1
                pass
            count = 0
            
            while tries.execute(count, c.start_farm_treasure_image) is False :
                count += 1
                if count > 100 :
                    break
                pass
            print("Farm Start! ")
            time.sleep(10)
            return count <= 0
    # findWorkers() # < teste